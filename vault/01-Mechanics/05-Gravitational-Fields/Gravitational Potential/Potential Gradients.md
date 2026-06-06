# 1. Overview / 概述

**English:**
The gravitational potential gradient describes how gravitational potential ($V$) changes with distance ($r$) from a mass. It is a vector quantity that directly relates to the gravitational field strength ($g$). This sub-topic bridges the gap between [[Gravitational Potential (V)]] and [[Gravitational Force and Field]], showing that the field is the negative gradient of the potential. Understanding potential gradients is essential for analyzing radial fields, predicting satellite motion, and solving problems involving [[Escape Velocity]] and [[Circular Orbits]].

**中文:**
引力势梯度描述了引力势 ($V$) 随距离 ($r$) 的变化率。它是一个矢量，直接与引力场强度 ($g$) 相关。本子知识点连接了[[Gravitational Potential (V)]]和[[Gravitational Force and Field]]，表明引力场是势的负梯度。理解势梯度对于分析径向场、预测卫星运动以及解决涉及[[Escape Velocity]]和[[Circular Orbits]]的问题至关重要。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Gravitational Potential Gradient** / 引力势梯度 | The rate of change of gravitational potential with respect to distance in a given direction. | 引力势在给定方向上随距离的变化率。 |
| **Field Strength** / 场强度 | The force per unit mass experienced by a test mass in a gravitational field. | 测试质量在引力场中每单位质量所受的力。 |
| **Radial Field** / 径向场 | A gravitational field where the field lines point radially towards or away from a central mass. | 场线指向或远离中心质量的引力场。 |
| **Negative Gradient** / 负梯度 | The relationship $g = -\frac{dV}{dr}$, indicating that potential decreases as you move towards a mass. | 关系式 $g = -\frac{dV}{dr}$，表示势随靠近质量而减小。 |
| **Uniform Field** / 均匀场 | A field where the field strength is constant in magnitude and direction. | 场强度大小和方向都恒定的场。 |
| **Equipotential Surface** / 等势面 | A surface where gravitational potential is constant; no work is done moving along it. | 引力势恒定的表面；沿其移动不做功。 |

---

# 3. Key Concepts / 关键概念

**English:**
The gravitational potential gradient is the mathematical link between [[Gravitational Potential (V)]] and [[Gravitational Force and Field]]. In a radial field around a point mass $M$, the potential is given by $V = -\frac{GM}{r}$. The gradient is:

$$ g = -\frac{dV}{dr} = -\frac{GM}{r^2} $$

This shows that the field strength $g$ is the negative of the potential gradient. The negative sign indicates that potential decreases (becomes more negative) as you move towards the mass — the field points in the direction of decreasing potential.

**Step-by-step reasoning:**
1. Start with $V = -\frac{GM}{r}$.
2. Differentiate with respect to $r$: $\frac{dV}{dr} = \frac{GM}{r^2}$.
3. Apply the negative sign: $g = -\frac{dV}{dr} = -\frac{GM}{r^2}$.
4. The magnitude $|g| = \frac{GM}{r^2}$ matches the inverse-square law.

**Physical interpretation:**
- A steep gradient (large $\frac{dV}{dr}$) means a strong field.
- Equipotential surfaces are perpendicular to field lines.
- In a [[Uniform Field]] (e.g., near Earth's surface), $g$ is constant, so $V$ changes linearly with height: $\Delta V = g \Delta h$.

**Common pitfalls:**
- Forgetting the negative sign: $g = -\frac{dV}{dr}$, not $+\frac{dV}{dr}$.
- Confusing gradient with potential itself: gradient is a rate of change, not a value.
- Applying the radial formula to uniform fields without adjustment.

**中文:**
引力势梯度是[[Gravitational Potential (V)]]和[[Gravitational Force and Field]]之间的数学桥梁。在点质量 $M$ 周围的径向场中，势为 $V = -\frac{GM}{r}$。梯度为：

$$ g = -\frac{dV}{dr} = -\frac{GM}{r^2} $$

这表明场强度 $g$ 是势梯度的负值。负号表示势随靠近质量而减小（变得更负）——场指向势减小的方向。

**逐步推理：**
1. 从 $V = -\frac{GM}{r}$ 开始。
2. 对 $r$ 求导：$\frac{dV}{dr} = \frac{GM}{r^2}$。
3. 应用负号：$g = -\frac{dV}{dr} = -\frac{GM}{r^2}$。
4. 大小 $|g| = \frac{GM}{r^2}$ 与平方反比定律一致。

**物理解释：**
- 陡峭的梯度（大的 $\frac{dV}{dr}$）意味着强场。
- 等势面垂直于场线。
- 在[[Uniform Field]]中（例如地球表面附近），$g$ 恒定，因此 $V$ 随高度线性变化：$\Delta V = g \Delta h$。

**常见错误：**
- 忘记负号：$g = -\frac{dV}{dr}$，而不是 $+\frac{dV}{dr}$。
- 混淆梯度与势本身：梯度是变化率，不是值。
- 将径向公式不加调整地应用于均匀场。

---

# 4. Formulas / 公式

## Formula 1: General Relationship

$$ g = -\frac{dV}{dr} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $g$ | Gravitational field strength | 引力场强度 | N kg$^{-1}$ or m s$^{-2}$ |
| $V$ | Gravitational potential | 引力势 | J kg$^{-1}$ |
| $r$ | Distance from center of mass | 距质量中心的距离 | m |

## Formula 2: Radial Field Specific

$$ g = -\frac{GM}{r^2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $G$ | Gravitational constant | 引力常数 | N m$^2$ kg$^{-2}$ |
| $M$ | Mass of central body | 中心天体质量 | kg |
| $r$ | Distance from center | 距中心的距离 | m |

**Derivation / 推导:**
1. $V = -\frac{GM}{r}$
2. $\frac{dV}{dr} = \frac{GM}{r^2}$ (differentiate)
3. $g = -\frac{dV}{dr} = -\frac{GM}{r^2}$

**Conditions / 适用条件:**
- Applies to radial fields around point masses or spherically symmetric bodies.
- For uniform fields, use $\Delta V = g \Delta h$ where $g$ is constant.

> 📷 **IMAGE PROMPT — VG01: Potential Gradient Diagram**
>
> **English Prompt:**
> A 2D cross-section diagram showing a large central mass (Earth) at the center. Concentric circles represent equipotential surfaces labeled V1, V2, V3 (V1 more negative, closer to Earth). Arrows perpendicular to these circles point radially inward, labeled "g = -dV/dr". The spacing between equipotential surfaces decreases closer to Earth, showing steeper gradient. Include a small test mass m at two positions: one far (small arrow) and one near (large arrow). Color scheme: blue equipotentials, red field arrows, grey Earth. Clean textbook vector style with white background.
>
> **中文描述:**
> 一个二维截面图，中心有一个大质量（地球）。同心圆代表等势面，标记为 V1、V2、V3（V1 更负，更靠近地球）。垂直于这些圆的箭头径向向内，标记为 "g = -dV/dr"。等势面之间的间距越靠近地球越小，显示梯度更陡。在两个位置放置小测试质量 m：远处（小箭头）和近处（大箭头）。配色：蓝色等势面，红色场箭头，灰色地球。干净的教科书矢量风格，白色背景。
>
> **Labels Required / 需要标注:**
> * Central mass M (地球)
> * Equipotential surfaces V1, V2, V3
> * Field arrows g
> * Test mass m at two positions
> * Distance r from center
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> Essential for understanding the relationship between potential and field strength in radial fields.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — VG02: Uniform vs Radial Field Comparison**
>
> **English Prompt:**
> Split diagram comparing two gravitational fields. Left side: Uniform field near Earth's surface — parallel equipotential lines (horizontal, equally spaced) with vertical downward arrows of equal length. Label: "Uniform Field: g = constant, ΔV = gΔh". Right side: Radial field around a point mass — concentric circular equipotentials with radial inward arrows of varying length (longer near mass). Label: "Radial Field: g = -GM/r²". Include a small graph below each: left graph shows V vs h (straight line), right graph shows V vs r (hyperbolic curve). Clean textbook vector style, white background, blue and red color scheme.
>
> **中文描述:**
> 对比两种引力场的分割图。左侧：地球表面附近的均匀场——平行的等势线（水平、等间距），等长的垂直向下箭头。标签："均匀场：g = 常数，ΔV = gΔh"。右侧：点质量周围的径向场——同心圆等势面，径向向内箭头长度变化（靠近质量处更长）。标签："径向场：g = -GM/r²"。每个下方有一个小图：左侧 V 对 h 图（直线），右侧 V 对 r 图（双曲线）。干净的教科书矢量风格，白色背景，蓝红配色。
>
> **Labels Required / 需要标注:**
> * Uniform field: parallel equipotentials, constant g arrows
> * Radial field: concentric equipotentials, varying g arrows
> * Graphs: V vs h (linear), V vs r (inverse)
>
> **Style / 风格:** Textbook vector diagram with graphs
>
> **Exam Relevance / 考试关联:**
> Helps distinguish between uniform and radial field behavior, a common exam comparison question.

---

# 6. Worked Example / 典型例题

## Example 1: Calculating Field Strength from Potential Gradient

### Question / 题目
**English:**
The gravitational potential near a planet is given by $V = -4.0 \times 10^7 \, \text{J kg}^{-1}$ at a distance of $2.0 \times 10^7 \, \text{m}$ from its center. The potential gradient at this point is $2.0 \, \text{J kg}^{-1} \, \text{m}^{-1}$. Calculate:
(a) The gravitational field strength at this point.
(b) The mass of the planet. ($G = 6.67 \times 10^{-11} \, \text{N m}^2 \, \text{kg}^{-2}$)

**中文:**
某行星附近的引力势在距其中心 $2.0 \times 10^7 \, \text{m}$ 处为 $V = -4.0 \times 10^7 \, \text{J kg}^{-1}$。该点的势梯度为 $2.0 \, \text{J kg}^{-1} \, \text{m}^{-1}$。计算：
(a) 该点的引力场强度。
(b) 行星的质量。（$G = 6.67 \times 10^{-11} \, \text{N m}^2 \, \text{kg}^{-2}$）

### Solution / 解答

**(a) Field strength:**
$$ g = -\frac{dV}{dr} = -2.0 \, \text{J kg}^{-1} \, \text{m}^{-1} = -2.0 \, \text{N kg}^{-1} $$

The negative sign indicates the field points towards the planet. Magnitude: $2.0 \, \text{N kg}^{-1}$.

**(b) Mass of planet:**
From $g = \frac{GM}{r^2}$:
$$ M = \frac{g r^2}{G} = \frac{2.0 \times (2.0 \times 10^7)^2}{6.67 \times 10^{-11}} $$
$$ M = \frac{2.0 \times 4.0 \times 10^{14}}{6.67 \times 10^{-11}} = \frac{8.0 \times 10^{14}}{6.67 \times 10^{-11}} $$
$$ M = 1.20 \times 10^{25} \, \text{kg} $$

### Final Answer / 最终答案
**Answer:** (a) $g = 2.0 \, \text{N kg}^{-1}$ towards planet (b) $M = 1.20 \times 10^{25} \, \text{kg}$
**答案:** (a) $g = 2.0 \, \text{N kg}^{-1}$ 指向行星 (b) $M = 1.20 \times 10^{25} \, \text{kg}$

### Quick Tip / 提示
Remember: $g = -\frac{dV}{dr}$ always. The gradient $\frac{dV}{dr}$ is positive (potential increases with r), so $g$ is negative (pointing inward). For magnitude, use $|g| = \frac{GM}{r^2}$.

---

## Example 2: Potential Difference in a Uniform Field

### Question / 题目
**English:**
A satellite moves from a point where gravitational potential is $-6.0 \times 10^7 \, \text{J kg}^{-1}$ to a point where it is $-5.0 \times 10^7 \, \text{J kg}^{-1}$. The gravitational field is approximately uniform in this region with $g = 8.0 \, \text{N kg}^{-1}$. Calculate the vertical distance moved.

**中文:**
一颗卫星从引力势为 $-6.0 \times 10^7 \, \text{J kg}^{-1}$ 的点移动到 $-5.0 \times 10^7 \, \text{J kg}^{-1}$ 的点。该区域引力场近似均匀，$g = 8.0 \, \text{N kg}^{-1}$。计算垂直移动的距离。

### Solution / 解答
For a uniform field: $\Delta V = g \Delta h$
$$ \Delta V = (-5.0 \times 10^7) - (-6.0 \times 10^7) = 1.0 \times 10^7 \, \text{J kg}^{-1} $$
$$ \Delta h = \frac{\Delta V}{g} = \frac{1.0 \times 10^7}{8.0} = 1.25 \times 10^6 \, \text{m} $$

The satellite moves upward (away from Earth) by $1.25 \times 10^6 \, \text{m}$.

### Final Answer / 最终答案
**Answer:** $\Delta h = 1.25 \times 10^6 \, \text{m}$ (upward)
**答案:** $\Delta h = 1.25 \times 10^6 \, \text{m}$（向上）

### Quick Tip / 提示
In uniform fields, potential increases linearly with height. The gradient $g$ is constant, so $\Delta V = g \Delta h$ is a direct application of $g = -\frac{dV}{dr}$.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the relationship between gravitational field strength and potential gradient?
Q (CN): 引力场强度和势梯度之间的关系是什么？
A (EN): $g = -\frac{dV}{dr}$. Field strength is the negative of the potential gradient.
A (CN): $g = -\frac{dV}{dr}$。场强度是势梯度的负值。

**Flashcard 2:**
Q (EN): In a radial field, what is the potential gradient $\frac{dV}{dr}$ equal to?
Q (CN): 在径向场中，势梯度 $\frac{dV}{dr}$ 等于什么？
A (EN): $\frac{dV}{dr} = \frac{GM}{r^2}$ (positive, since V increases with r).
A (CN): $\frac{dV}{dr} = \frac{GM}{r^2}$（正值，因为 V 随 r 增加而增加）。

**Flashcard 3:**
Q (EN): Why is there a negative sign in $g = -\frac{dV}{dr}$?
Q (CN): 为什么 $g = -\frac{dV}{dr}$ 中有负号？
A (EN): Because gravitational field points towards the mass (decreasing potential), while $\frac{dV}{dr}$ is positive (potential increases with distance).
A (CN): 因为引力场指向质量（势减小），而 $\frac{dV}{dr}$ 是正值（势随距离增加而增加）。

**Flashcard 4:**
Q (EN): In a uniform gravitational field, how does potential vary with height?
Q (CN): 在均匀引力场中，势如何随高度变化？
A (EN): Linearly: $\Delta V = g \Delta h$, where $g$ is constant.
A (CN): 线性变化：$\Delta V = g \Delta h$，其中 $g$ 是常数。

**Flashcard 5:**
Q (EN): What does a steep potential gradient indicate about the gravitational field?
Q (CN): 陡峭的势梯度表明引力场如何？
A (EN): A steep gradient means a strong gravitational field (large $g$).
A (CN): 陡峭的梯度意味着强引力场（大的 $g$）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Potential Gradients"
  cn: "势梯度"
parent_topic: "Gravitational Potential"
parent_hub: "[[Gravitational Potential]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Gravitational Potential (V)]]"
  - "[[Gravitational Potential Energy in a Radial Field]]"
  - "[[Escape Velocity]]"
  - "[[Gravitational Force and Field]]"
  - "[[Circular Orbits]]"
language: bilingual_en_cn