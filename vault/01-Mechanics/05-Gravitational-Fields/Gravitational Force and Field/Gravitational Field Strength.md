# Gravitational Field Strength / 引力场强度

---

## 1. Overview / 概述

**English:**
Gravitational field strength $g$ is a fundamental concept that quantifies the gravitational force per unit mass at any point in a gravitational field. It tells us how "strong" gravity is at a given location — whether on Earth’s surface, inside a planet, or far out in space. This sub-topic bridges [[Newton's Law of Universal Gravitation]] with the practical measurement of gravitational effects, and is essential for understanding [[Gravitational Potential]] and [[Circular Orbits]]. At A-Level, you must distinguish between the uniform field approximation near Earth’s surface and the radial field described by Newton’s law, and be able to calculate $g$ for any mass distribution.

**中文:**
引力场强度 $g$ 是一个基本概念，它量化了引力场中每单位质量所受的引力大小。它告诉我们某个位置的引力有多“强”——无论是在地球表面、行星内部还是遥远的太空中。本子知识点将[[牛顿万有引力定律]]与引力效应的实际测量联系起来，是理解[[引力势]]和[[圆周轨道]]的基础。在A-Level中，你必须区分地球表面附近的均匀场近似和牛顿定律描述的径向场，并能够计算任意质量分布的 $g$。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Gravitational Field Strength** / 引力场强度 | The gravitational force per unit mass acting on a small test mass placed at a point in the field. | 作用在置于场中某点的小测试质量上的单位质量的引力。 |
| **Test Mass** / 测试质量 | A mass small enough that it does not significantly disturb the field it is measuring. | 足够小以至于不会显著干扰其所测量场的质量。 |
| **Uniform Field** / 均匀场 | A region where the gravitational field strength is constant in both magnitude and direction. | 引力场强度大小和方向都恒定的区域。 |
| **Radial Field** / 径向场 | A field where the direction of $g$ is always toward the centre of the mass, and magnitude varies with distance. | 场的方向始终指向质量中心，大小随距离变化的场。 |
| **Inverse Square Law** / 平方反比定律 | The relationship that $g \propto 1/r^2$ for a point mass or spherical mass. | 对于点质量或球形质量，$g \propto 1/r^2$ 的关系。 |
| **g-field** / g场 | Another name for gravitational field strength, often used in vector diagrams. | 引力场强度的另一种名称，常用于矢量图中。 |

---

## 3. Key Concepts / 关键概念

**English:**

### 3.1 Definition from Force
Gravitational field strength is defined as:
$$ g = \frac{F}{m} $$
where $F$ is the gravitational force on a test mass $m$. This is a **vector** quantity — it has both magnitude and direction (always toward the source mass).

### 3.2 Two Key Formulas
There are two expressions for $g$, and you must know when to use each:

1. **Near Earth’s surface (uniform field approximation):**
   $$ g = \frac{GM}{R^2} $$
   where $M$ is Earth’s mass, $R$ is Earth’s radius. This gives $g \approx 9.81 \text{ N kg}^{-1}$ (or $\text{m s}^{-2}$).

2. **At any distance $r$ from centre of mass $M$ (radial field):**
   $$ g = \frac{GM}{r^2} $$
   This is derived from [[Newton's Law of Universal Gravitation]]: $F = \frac{GMm}{r^2}$, then $g = F/m$.

### 3.3 Relationship with Acceleration
Crucially, $g$ has **the same numerical value and units** as the acceleration due to gravity. From [[Newton's Laws of Motion]], $F = ma$, so:
$$ mg = ma \implies a = g $$
Thus, in free fall, an object accelerates at $g$ regardless of its mass — a key result from Galileo’s experiments.

### 3.4 Vector Nature
- **Direction:** Always toward the centre of the mass creating the field.
- **Superposition:** For multiple masses, the net $g$ is the vector sum of individual fields. This is essential for problems involving two or more planets.

### 3.5 Uniform vs Radial Fields
| Feature | Uniform Field | Radial Field |
| ------- | ------------- | ------------ |
| Magnitude | Constant | $g \propto 1/r^2$ |
| Direction | Constant (e.g., downward) | Always toward centre |
| Example | Near Earth’s surface | Far from Earth, or around any point mass |
| Field lines | Parallel, equally spaced | Radial lines converging at centre |

### 3.6 Common Pitfalls
- **Units:** $g$ is in $\text{N kg}^{-1}$ or $\text{m s}^{-2}$ — both are equivalent.
- **$g$ vs $G$:** Do not confuse $g$ (field strength) with $G$ (gravitational constant, $6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$).
- **$r$ is from centre:** In $g = GM/r^2$, $r$ is the distance from the **centre** of the mass, not the surface.
- **Test mass assumption:** The test mass must be small enough not to affect the field.

**中文:**

### 3.1 从力的定义出发
引力场强度定义为：
$$ g = \frac{F}{m} $$
其中 $F$ 是作用在测试质量 $m$ 上的引力。这是一个**矢量**量——既有大小也有方向（始终指向源质量）。

### 3.2 两个关键公式
$g$ 有两种表达式，你必须知道何时使用：

1. **地球表面附近（均匀场近似）：**
   $$ g = \frac{GM}{R^2} $$
   其中 $M$ 是地球质量，$R$ 是地球半径。这给出 $g \approx 9.81 \text{ N kg}^{-1}$（或 $\text{m s}^{-2}$）。

2. **距质量 $M$ 中心任意距离 $r$ 处（径向场）：**
   $$ g = \frac{GM}{r^2} $$
   这是从[[牛顿万有引力定律]]推导出来的：$F = \frac{GMm}{r^2}$，然后 $g = F/m$。

### 3.3 与加速度的关系
关键的是，$g$ 与重力加速度具有**相同的数值和单位**。根据[[牛顿运动定律]]，$F = ma$，所以：
$$ mg = ma \implies a = g $$
因此，在自由落体中，物体以 $g$ 加速，与其质量无关——这是伽利略实验的关键结果。

### 3.4 矢量性质
- **方向：** 始终指向产生场的质量中心。
- **叠加原理：** 对于多个质量，净 $g$ 是各个场的矢量和。这对于涉及两个或多个行星的问题至关重要。

### 3.5 均匀场与径向场
| 特征 | 均匀场 | 径向场 |
| ---- | ------ | ------ |
| 大小 | 恒定 | $g \propto 1/r^2$ |
| 方向 | 恒定（例如向下） | 始终指向中心 |
| 示例 | 地球表面附近 | 远离地球，或围绕任何点质量 |
| 场线 | 平行、等间距 | 汇聚于中心的径向线 |

### 3.6 常见陷阱
- **单位：** $g$ 的单位是 $\text{N kg}^{-1}$ 或 $\text{m s}^{-2}$——两者等价。
- **$g$ 与 $G$：** 不要混淆 $g$（场强度）与 $G$（引力常数，$6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$）。
- **$r$ 是从中心算起：** 在 $g = GM/r^2$ 中，$r$ 是到质量**中心**的距离，而不是表面。
- **测试质量假设：** 测试质量必须足够小，以免影响场。

---

## 4. Formulas / 公式

### Primary Formula: Gravitational Field Strength

$$ g = \frac{GM}{r^2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $g$ | Gravitational field strength | 引力场强度 | $\text{N kg}^{-1}$ or $\text{m s}^{-2}$ |
| $G$ | Universal gravitational constant | 万有引力常数 | $6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$ |
| $M$ | Mass of the object creating the field | 产生场的物体质量 | $\text{kg}$ |
| $r$ | Distance from centre of mass $M$ | 距质量 $M$ 中心的距离 | $\text{m}$ |

### Alternative Form: From Force Definition

$$ g = \frac{F}{m} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F$ | Gravitational force on test mass | 作用在测试质量上的引力 | $\text{N}$ |
| $m$ | Test mass | 测试质量 | $\text{kg}$ |

### Derivation / 推导

Starting from [[Newton's Law of Universal Gravitation]]:
$$ F = \frac{GMm}{r^2} $$

By definition, $g = F/m$, so:
$$ g = \frac{1}{m} \cdot \frac{GMm}{r^2} = \frac{GM}{r^2} $$

This shows that $g$ is independent of the test mass $m$ — a fundamental property of gravitational fields.

### Conditions / 适用条件

1. **Point mass or spherical mass:** The formula $g = GM/r^2$ is valid only for point masses or for points **outside** a spherically symmetric mass distribution.
2. **Outside the mass:** For points inside a uniform sphere, $g \propto r$ (linear relationship).
3. **No other masses:** The formula assumes the field is created only by mass $M$.
4. **Non-relativistic:** Valid only when $r$ is much larger than the Schwarzschild radius (not relevant at A-Level).

> 📷 **IMAGE PROMPT — GFS-01: Gravitational Field Strength vs Distance Graph**
>
> **English Prompt:**
> A clean, textbook-style graph showing gravitational field strength $g$ on the y-axis (units: N kg⁻¹) against distance $r$ from centre of a planet on the x-axis (units: m). The graph has two distinct regions: for $r < R$ (inside the planet), a straight line through origin showing $g \propto r$; for $r > R$ (outside), a smooth curve showing $g \propto 1/r^2$ decreasing asymptotically to zero. Label the planet radius $R$ with a vertical dashed line. Mark the surface value $g_s = GM/R^2$. Use a white background, black lines, and clear axis labels. Include a small diagram of a planet with radial field lines in the corner.
>
> **中文描述:**
> 一个干净的教科书式图表，y轴为引力场强度 $g$（单位：N kg⁻¹），x轴为距行星中心的距离 $r$（单位：m）。图表有两个不同区域：$r < R$（行星内部）为通过原点的直线，显示 $g \propto r$；$r > R$（外部）为平滑曲线，显示 $g \propto 1/r^2$ 渐近趋于零。用垂直虚线标记行星半径 $R$。标记表面值 $g_s = GM/R^2$。使用白色背景、黑色线条和清晰的轴标签。在角落包含一个带有径向场线的行星小图。
>
> **Labels Required / 需要标注:**
> * $g_s = GM/R^2$ (surface value)
> * $R$ (planet radius)
> * $g \propto r$ (inside)
> * $g \propto 1/r^2$ (outside)
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This graph is frequently tested in multiple-choice and data-analysis questions. Students must be able to interpret both regions and explain why $g$ is maximum at the surface.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — GFS-02: Uniform vs Radial Field Comparison**
>
> **English Prompt:**
> A side-by-side comparison diagram. Left side: Uniform gravitational field near Earth's surface — parallel, equally spaced vertical arrows pointing downward, with a small person standing on Earth's surface. Right side: Radial gravitational field around a planet — arrows pointing radially inward toward the planet's centre, with spacing increasing (arrows getting shorter) as distance increases. Use a 3D isometric perspective. Colour scheme: Earth in blue and green, arrows in red. Include labels: "Uniform Field (near surface)" and "Radial Field (far from surface)". Add a small compass rose showing direction.
>
> **中文描述:**
> 并排对比图。左侧：地球表面附近的均匀引力场——平行、等间距的垂直向下箭头，有一个小人站在地球表面。右侧：行星周围的径向引力场——箭头径向向内指向行星中心，间距随距离增加而增大（箭头变短）。使用3D等轴测视角。配色方案：地球为蓝绿色，箭头为红色。包含标签："均匀场（表面附近）"和"径向场（远离表面）"。添加一个小指南针显示方向。
>
> **Labels Required / 需要标注:**
> * Uniform Field / 均匀场
> * Radial Field / 径向场
> * Earth / 地球
> * Direction of $g$ / $g$的方向
>
> **Style / 风格:** 3D isometric render, textbook quality
>
> **Exam Relevance / 考试关联:**
> Understanding the difference between uniform and radial fields is essential for choosing the correct formula in exam problems. This visual comparison helps avoid common mistakes.

---

## 6. Worked Example / 典型例题

### Example 1: Calculating $g$ at Different Altitudes

### Question / 题目
**English:**
The mass of Earth is $M_E = 5.97 \times 10^{24} \text{ kg}$ and its radius is $R_E = 6.37 \times 10^6 \text{ m}$. $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$.

(a) Calculate the gravitational field strength at Earth’s surface.
(b) Calculate the gravitational field strength at an altitude of 300 km above Earth’s surface.
(c) By what percentage has $g$ decreased at this altitude?

**中文:**
地球质量 $M_E = 5.97 \times 10^{24} \text{ kg}$，半径 $R_E = 6.37 \times 10^6 \text{ m}$。$G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$。

(a) 计算地球表面的引力场强度。
(b) 计算距地球表面 300 km 高处的引力场强度。
(c) 在此高度，$g$ 减少了百分之几？

### Solution / 解答

**(a) Surface:**
$$ g_{\text{surface}} = \frac{GM_E}{R_E^2} = \frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{(6.37 \times 10^6)^2} $$

$$ g_{\text{surface}} = \frac{3.98 \times 10^{14}}{4.06 \times 10^{13}} = 9.81 \text{ N kg}^{-1} $$

**(b) At altitude $h = 300 \text{ km} = 3.00 \times 10^5 \text{ m}$:**
Distance from centre: $r = R_E + h = 6.37 \times 10^6 + 3.00 \times 10^5 = 6.67 \times 10^6 \text{ m}$

$$ g_{\text{altitude}} = \frac{GM_E}{r^2} = \frac{3.98 \times 10^{14}}{(6.67 \times 10^6)^2} = \frac{3.98 \times 10^{14}}{4.45 \times 10^{13}} = 8.94 \text{ N kg}^{-1} $$

**(c) Percentage decrease:**
$$ \text{Percentage decrease} = \frac{g_{\text{surface}} - g_{\text{altitude}}}{g_{\text{surface}}} \times 100\% = \frac{9.81 - 8.94}{9.81} \times 100\% = 8.87\% $$

### Final Answer / 最终答案
**Answer:** (a) $9.81 \text{ N kg}^{-1}$ (b) $8.94 \text{ N kg}^{-1}$ (c) $8.87\%$ decrease
**答案：** (a) $9.81 \text{ N kg}^{-1}$ (b) $8.94 \text{ N kg}^{-1}$ (c) 减少了 $8.87\%$

### Quick Tip / 提示
**EN:** Always use distance from the **centre** of the planet, not the surface. Convert km to m before calculating.
**CN:** 始终使用到行星**中心**的距离，而不是表面。计算前将 km 转换为 m。

---

### Example 2: Comparing $g$ on Different Planets

### Question / 题目
**English:**
Planet X has twice the mass of Earth and three times the radius. Calculate the gravitational field strength on the surface of Planet X in terms of Earth’s $g_E$.

**中文:**
行星 X 的质量是地球的两倍，半径是地球的三倍。计算行星 X 表面的引力场强度，用地球的 $g_E$ 表示。

### Solution / 解答

Let $M_X = 2M_E$ and $R_X = 3R_E$.

$$ g_X = \frac{GM_X}{R_X^2} = \frac{G(2M_E)}{(3R_E)^2} = \frac{2GM_E}{9R_E^2} = \frac{2}{9} \cdot \frac{GM_E}{R_E^2} = \frac{2}{9} g_E $$

### Final Answer / 最终答案
**Answer:** $g_X = \frac{2}{9} g_E$
**答案：** $g_X = \frac{2}{9} g_E$

### Quick Tip / 提示
**EN:** For ratio problems, write the formula for each planet and divide. The constants $G$ cancel out.
**CN:** 对于比例问题，写出每个行星的公式然后相除。常数 $G$ 会消去。

---

## 7. Flashcards / 闪卡

**Flashcard 1:**
- **Q (EN):** Define gravitational field strength.
- **Q (CN):** 定义引力场强度。
- **A (EN):** The gravitational force per unit mass acting on a small test mass placed at a point in the field. $g = F/m$.
- **A (CN):** 作用在置于场中某点的小测试质量上的单位质量的引力。$g = F/m$。

**Flashcard 2:**
- **Q (EN):** State the formula for gravitational field strength at a distance $r$ from the centre of a mass $M$.
- **Q (CN):** 写出距质量 $M$ 中心距离 $r$ 处的引力场强度公式。
- **A (EN):** $g = GM/r^2$
- **A (CN):** $g = GM/r^2$

**Flashcard 3:**
- **Q (EN):** What are the units of gravitational field strength?
- **Q (CN):** 引力场强度的单位是什么？
- **A (EN):** $\text{N kg}^{-1}$ or $\text{m s}^{-2}$ (both are equivalent).
- **A (CN):** $\text{N kg}^{-1}$ 或 $\text{m s}^{-2}$（两者等价）。

**Flashcard 4:**
- **Q (EN):** How does $g$ vary with distance $r$ from the centre of a planet (outside the planet)?
- **Q (CN):** 在行星外部，$g$ 如何随距行星中心的距离 $r$ 变化？
- **A (EN):)** $g \propto 1/r^2$ (inverse square law).
- **A (CN):** $g \propto 1/r^2$（平方反比定律）。

**Flashcard 5:**
- **Q (EN):** What is the difference between a uniform gravitational field and a radial gravitational field?
- **Q (CN):** 均匀引力场和径向引力场有什么区别？
- **A (EN):** Uniform: constant magnitude and direction (parallel field lines). Radial: magnitude $\propto 1/r^2$, direction always toward centre (converging field lines).
- **A (CN):** 均匀场：大小和方向恒定（场线平行）。径向场：大小 $\propto 1/r^2$，方向始终指向中心（场线汇聚）。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Gravitational Field Strength
  cn: 引力场强度
parent_topic: Gravitational Force and Field
parent_hub: "[[Gravitational Force and Field]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Newton's Law of Universal Gravitation]]"
  - "[[Radial vs Uniform Gravitational Fields]]"
  - "[[Gravitational Potential]]"
  - "[[Circular Orbits]]"
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Centripetal Acceleration and Force]]"
language: bilingual_en_cn