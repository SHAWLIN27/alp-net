# 1. Overview / 概述

**English:**
Kepler's Third Law is a cornerstone of orbital mechanics, describing the relationship between a planet's orbital period and its average distance from the Sun. For A-Level Physics, this law is extended to any two-body gravitational system — from planets orbiting stars to satellites orbiting Earth. It states that the square of the orbital period ($T$) is proportional to the cube of the semi-major axis ($r$) of the orbit. This sub-topic bridges [[Gravitational Force and Field]] with [[Circular Orbits]], providing a powerful tool for calculating orbital periods and distances. Understanding Kepler's Third Law is essential for analyzing [[Geostationary Satellites]] and comparing different [[Orbital Velocity]] scenarios.

**中文:**
开普勒第三定律是轨道力学的基石，描述了行星轨道周期与其到太阳平均距离之间的关系。在A-Level物理中，这一定律被推广到任何两体引力系统——从绕恒星运行的行星到绕地球运行的卫星。它指出轨道周期的平方（$T$）与轨道半长轴的立方（$r$）成正比。本子知识点将[[Gravitational Force and Field]]与[[Circular Orbits]]联系起来，为计算轨道周期和距离提供了强大工具。理解开普勒第三定律对于分析[[Geostationary Satellites]]和比较不同的[[Orbital Velocity]]场景至关重要。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Kepler's Third Law** / 开普勒第三定律 | The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit. | 行星轨道周期的平方与其轨道半长轴的立方成正比。 |
| **Orbital Period ($T$)** / 轨道周期 | The time taken for a celestial body to complete one full orbit around another body. | 天体绕另一天体完成一次完整轨道运行所需的时间。 |
| **Semi-major Axis ($r$)** / 半长轴 | Half the longest diameter of an elliptical orbit; for circular orbits, it equals the orbital radius. | 椭圆轨道最长直径的一半；对于圆形轨道，等于轨道半径。 |
| **Proportionality Constant ($k$)** / 比例常数 | The constant $k = \frac{GM}{4\pi^2}$ in Kepler's Third Law, where $M$ is the mass of the central body. | 开普勒第三定律中的常数 $k = \frac{GM}{4\pi^2}$，其中 $M$ 是中心天体的质量。 |
| **Two-body System** / 两体系统 | A gravitational system consisting of two bodies orbiting their common center of mass. | 由两个绕共同质心运行的天体组成的引力系统。 |
| **Geostationary Orbit** / 地球静止轨道 | A circular orbit at an altitude of approximately 35,786 km above Earth's equator, where the orbital period equals Earth's rotational period (24 hours). | 地球赤道上方约35,786公里高度的圆形轨道，轨道周期等于地球自转周期（24小时）。 |

---

# 3. Key Concepts / 关键概念

**English:**
Kepler's Third Law emerges from the balance between [[Gravitational Force and Field]] and [[Centripetal Acceleration and Force]]. For a satellite of mass $m$ in a circular orbit of radius $r$ around a central body of mass $M$ (where $M \gg m$), the gravitational force provides the necessary centripetal force:

$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

Since orbital speed $v = \frac{2\pi r}{T}$, substituting gives:

$$ \frac{GMm}{r^2} = \frac{m(2\pi r/T)^2}{r} $$

Simplifying yields Kepler's Third Law:

$$ T^2 = \frac{4\pi^2}{GM} r^3 $$

**Key insights:**
1. **Mass independence**: The orbital period $T$ does NOT depend on the satellite's mass $m$ — only on the central body's mass $M$ and orbital radius $r$.
2. **Proportionality**: $T^2 \propto r^3$ means doubling the orbital radius increases the period by a factor of $2^{3/2} \approx 2.83$.
3. **Central body dependence**: The constant $\frac{4\pi^2}{GM}$ is different for different central bodies (e.g., Sun vs. Earth).
4. **Circular vs. elliptical**: For circular orbits, $r$ is the orbital radius; for elliptical orbits, $r$ is the semi-major axis.

**Common pitfalls:**
- Forgetting that $M$ is the mass of the central body, not the orbiting body.
- Using $r$ as the altitude above the surface instead of the distance from the center.
- Confusing $T$ (period) with $f$ (frequency) — they are reciprocals: $T = 1/f$.

**中文:**
开普勒第三定律源于[[Gravitational Force and Field]]与[[Centripetal Acceleration and Force]]之间的平衡。对于质量为$m$、绕质量为$M$的中心天体（$M \gg m$）在半径为$r$的圆形轨道上运行的卫星，引力提供所需的向心力：

$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

由于轨道速度 $v = \frac{2\pi r}{T}$，代入得：

$$ \frac{GMm}{r^2} = \frac{m(2\pi r/T)^2}{r} $$

简化后得到开普勒第三定律：

$$ T^2 = \frac{4\pi^2}{GM} r^3 $$

**关键要点：**
1. **质量无关性**：轨道周期$T$不依赖于卫星质量$m$——只取决于中心天体质量$M$和轨道半径$r$。
2. **比例关系**：$T^2 \propto r^3$意味着轨道半径加倍会使周期增加$2^{3/2} \approx 2.83$倍。
3. **中心天体依赖性**：常数$\frac{4\pi^2}{GM}$对于不同的中心天体（如太阳与地球）是不同的。
4. **圆形与椭圆形**：对于圆形轨道，$r$是轨道半径；对于椭圆形轨道，$r$是半长轴。

**常见错误：**
- 忘记$M$是中心天体的质量，而不是轨道天体的质量。
- 将$r$误用为距地表的高度，而不是距中心的距离。
- 混淆$T$（周期）与$f$（频率）——它们是倒数关系：$T = 1/f$。

---

# 4. Formulas / 公式

## Primary Formula: Kepler's Third Law

$$ T^2 = \frac{4\pi^2}{GM} r^3 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T$ | Orbital period | 轨道周期 | s (seconds) |
| $r$ | Orbital radius (distance from center of central body) | 轨道半径（距中心天体中心的距离） | m (metres) |
| $G$ | Gravitational constant ($6.67 \times 10^{-11}$) | 引力常数 | N·m²/kg² |
| $M$ | Mass of central body | 中心天体质量 | kg (kilograms) |

## Alternative Forms

$$ T = 2\pi \sqrt{\frac{r^3}{GM}} $$

$$ r = \sqrt[3]{\frac{GMT^2}{4\pi^2}} $$

## For Comparing Two Orbits Around the Same Central Body

$$ \frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3} $$

**Derivation / 推导:**
1. Start with gravitational force = centripetal force: $\frac{GMm}{r^2} = \frac{mv^2}{r}$
2. Cancel $m$: $\frac{GM}{r^2} = \frac{v^2}{r}$
3. Substitute $v = \frac{2\pi r}{T}$: $\frac{GM}{r^2} = \frac{(2\pi r/T)^2}{r}$
4. Simplify: $\frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}$
5. Rearrange: $T^2 = \frac{4\pi^2}{GM} r^3$

**Conditions / 适用条件:**
- The orbiting body's mass $m$ is negligible compared to the central body's mass $M$ ($m \ll M$).
- The orbit is circular (for A-Level, elliptical orbits use semi-major axis).
- Only gravitational force acts on the orbiting body.
- The central body is stationary (or the reduced mass approximation holds).

> 📷 **IMAGE PROMPT — KPL-01: Kepler's Third Law Proportionality Graph**
>
> **English Prompt:**
> A clean, textbook-style graph showing the relationship between orbital period T (y-axis) and orbital radius r (x-axis) for satellites around Earth. The curve shows T² ∝ r³. Include three labeled data points: Low Earth Orbit (r = 7,000 km, T ≈ 90 min), Medium Earth Orbit (r = 26,000 km, T ≈ 12 h), and Geostationary Orbit (r = 42,000 km, T = 24 h). Use a log-log scale to show the straight-line relationship with slope 3/2. Color scheme: blue curve, black axes, red data points. Include gridlines. Style: clean vector illustration for A-Level textbook.
>
> **中文描述:**
> 一张干净的教科书风格图表，显示地球卫星轨道周期T（y轴）与轨道半径r（x轴）之间的关系。曲线显示T² ∝ r³。包括三个标注的数据点：低地球轨道（r = 7,000 km，T ≈ 90 min）、中地球轨道（r = 26,000 km，T ≈ 12 h）和地球静止轨道（r = 42,000 km，T = 24 h）。使用对数-对数坐标显示斜率为3/2的直线关系。配色方案：蓝色曲线、黑色坐标轴、红色数据点。包括网格线。风格：适合A-Level教科书的干净矢量图。
>
> **Labels Required / 需要标注:**
> * "Low Earth Orbit (LEO)" at (7,000 km, 90 min)
> * "Medium Earth Orbit (MEO)" at (26,000 km, 12 h)
> * "Geostationary Orbit (GEO)" at (42,000 km, 24 h)
> * Axes: "Orbital Period T / s" and "Orbital Radius r / m"
> * Annotation: "T² ∝ r³"
>
> **Style / 风格:** Textbook vector illustration
>
> **Exam Relevance / 考试关联:**
> This graph is frequently used in exam questions to test understanding of the proportionality relationship and to calculate orbital parameters for different satellite types.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — KPL-02: Derivation of Kepler's Third Law**
>
> **English Prompt:**
> A step-by-step visual derivation of Kepler's Third Law. Left panel: A large central body (Earth, blue sphere) with a small satellite (grey sphere) in a circular orbit of radius r. Arrows show gravitational force F_g (red arrow pointing inward) and centripetal acceleration a_c (blue arrow pointing inward). Right panel: The mathematical derivation showing the equation flow: F_g = F_c → GMm/r² = mv²/r → v = 2πr/T → GM/r² = (2πr/T)²/r → T² = (4π²/GM)r³. Use a clean white background, black text for equations, and color-coded arrows. Include a box highlighting the final formula. Style: educational infographic for A-Level Physics.
>
> **中文描述:**
> 开普勒第三定律的分步视觉推导。左侧面板：一个大的中心天体（地球，蓝色球体）和一个在半径为r的圆形轨道上的小卫星（灰色球体）。箭头显示引力F_g（红色箭头指向内）和向心加速度a_c（蓝色箭头指向内）。右侧面板：数学推导显示方程流程：F_g = F_c → GMm/r² = mv²/r → v = 2πr/T → GM/r² = (2πr/T)²/r → T² = (4π²/GM)r³。使用干净的白色背景、黑色文字方程和彩色箭头。包括一个突出最终公式的方框。风格：A-Level物理教育信息图。
>
> **Labels Required / 需要标注:**
> * "Central Body (Mass M)" on Earth
> * "Satellite (Mass m)" on satellite
> * "Orbital Radius r" as a line from center to satellite
> * "F_g = GMm/r²" next to gravitational arrow
> * "a_c = v²/r" next to centripetal arrow
> * Final formula in highlighted box: "T² = (4π²/GM)r³"
>
> **Style / 风格:** Educational infographic / textbook illustration
>
> **Exam Relevance / 考试关联:**
> Derivation questions are common in A-Level exams. Understanding the derivation helps students apply the formula correctly and avoid common mistakes.

---

# 6. Worked Example / 典型例题

## Example 1: Calculating Orbital Period

### Question / 题目
**English:**
A satellite orbits Earth at an altitude of 300 km above the surface. Given:
- Earth's radius $R_E = 6.37 \times 10^6$ m
- Earth's mass $M_E = 5.97 \times 10^{24}$ kg
- Gravitational constant $G = 6.67 \times 10^{-11}$ N·m²/kg²

Calculate the orbital period of the satellite in minutes.

**中文:**
一颗卫星在距地表300公里的高度绕地球运行。已知：
- 地球半径 $R_E = 6.37 \times 10^6$ m
- 地球质量 $M_E = 5.97 \times 10^{24}$ kg
- 引力常数 $G = 6.67 \times 10^{-11}$ N·m²/kg²

计算卫星的轨道周期（以分钟为单位）。

### Solution / 解答

**Step 1:** Calculate orbital radius $r$ (distance from Earth's center)
$$ r = R_E + h = 6.37 \times 10^6 + 300 \times 10^3 = 6.67 \times 10^6 \text{ m} $$

**Step 2:** Apply Kepler's Third Law
$$ T^2 = \frac{4\pi^2}{GM_E} r^3 $$

$$ T^2 = \frac{4\pi^2}{(6.67 \times 10^{-11})(5.97 \times 10^{24})} \times (6.67 \times 10^6)^3 $$

**Step 3:** Calculate step by step
$$ GM_E = (6.67 \times 10^{-11})(5.97 \times 10^{24}) = 3.98 \times 10^{14} \text{ m}^3/\text{s}^2 $$

$$ r^3 = (6.67 \times 10^6)^3 = 2.97 \times 10^{20} \text{ m}^3 $$

$$ T^2 = \frac{4\pi^2}{3.98 \times 10^{14}} \times 2.97 \times 10^{20} $$

$$ T^2 = \frac{39.48}{3.98 \times 10^{14}} \times 2.97 \times 10^{20} $$

$$ T^2 = 9.92 \times 10^{-14} \times 2.97 \times 10^{20} $$

$$ T^2 = 2.95 \times 10^7 \text{ s}^2 $$

**Step 4:** Find $T$
$$ T = \sqrt{2.95 \times 10^7} = 5430 \text{ s} $$

**Step 5:** Convert to minutes
$$ T = \frac{5430}{60} = 90.5 \text{ minutes} $$

### Final Answer / 最终答案
**Answer:** $T \approx 90.5$ minutes **答案:** $T \approx 90.5$ 分钟

### Quick Tip / 提示
**EN:** Always remember to add Earth's radius to the altitude to get the orbital radius $r$. A common mistake is using altitude directly in the formula.
**CN:** 始终记得将地球半径加上高度才能得到轨道半径$r$。常见的错误是直接在公式中使用高度。

---

## Example 2: Comparing Orbits

### Question / 题目
**English:**
A geostationary satellite orbits Earth at a radius of $4.22 \times 10^7$ m with a period of 24 hours. Another satellite orbits at a radius of $2.11 \times 10^7$ m. Calculate the orbital period of the second satellite.

**中文:**
一颗地球静止卫星在半径为$4.22 \times 10^7$ m的轨道上运行，周期为24小时。另一颗卫星在半径为$2.11 \times 10^7$ m的轨道上运行。计算第二颗卫星的轨道周期。

### Solution / 解答

**Step 1:** Use the ratio form of Kepler's Third Law (same central body)
$$ \frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3} $$

**Step 2:** Substitute known values
$$ \frac{(24 \text{ h})^2}{T_2^2} = \frac{(4.22 \times 10^7)^3}{(2.11 \times 10^7)^3} $$

**Step 3:** Simplify the radius ratio
$$ \frac{(4.22 \times 10^7)^3}{(2.11 \times 10^7)^3} = \left(\frac{4.22}{2.11}\right)^3 = 2^3 = 8 $$

**Step 4:** Solve for $T_2$
$$ \frac{576}{T_2^2} = 8 $$

$$ T_2^2 = \frac{576}{8} = 72 $$

$$ T_2 = \sqrt{72} = 8.49 \text{ hours} $$

### Final Answer / 最终答案
**Answer:** $T_2 \approx 8.49$ hours **答案:** $T_2 \approx 8.49$ 小时

### Quick Tip / 提示
**EN:** When comparing two orbits around the same central body, use the ratio form — it's faster and avoids calculating $G$ and $M$ separately.
**CN:** 当比较绕同一中心天体的两个轨道时，使用比例形式——更快且无需单独计算$G$和$M$。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): State Kepler's Third Law for circular orbits.
Q (CN): 陈述圆形轨道的开普勒第三定律。
A (EN): The square of the orbital period is directly proportional to the cube of the orbital radius: $T^2 \propto r^3$, or $T^2 = \frac{4\pi^2}{GM}r^3$.
A (CN): 轨道周期的平方与轨道半径的立方成正比：$T^2 \propto r^3$，或 $T^2 = \frac{4\pi^2}{GM}r^3$。

**Flashcard 2:**
Q (EN): What does the constant $k = \frac{4\pi^2}{GM}$ in Kepler's Third Law depend on?
Q (CN): 开普勒第三定律中的常数 $k = \frac{4\pi^2}{GM}$ 取决于什么？
A (EN): It depends only on the mass $M$ of the central body. Different central bodies (e.g., Sun vs. Earth) have different constants.
A (CN): 只取决于中心天体的质量$M$。不同的中心天体（如太阳与地球）有不同的常数。

**Flashcard 3:**
Q (EN): If the orbital radius of a satellite is doubled, by what factor does its orbital period increase?
Q (CN): 如果卫星的轨道半径加倍，其轨道周期增加多少倍？
A (EN): The period increases by a factor of $2^{3/2} \approx 2.83$. Because $T \propto r^{3/2}$.
A (CN): 周期增加 $2^{3/2} \approx 2.83$ 倍。因为 $T \propto r^{3/2}$。

**Flashcard 4:**
Q (EN): What is the orbital radius of a geostationary satellite?
Q (CN): 地球静止卫星的轨道半径是多少？
A (EN): Approximately $4.22 \times 10^7$ m (about 42,000 km from Earth's center, or 35,786 km altitude).
A (CN): 大约 $4.22 \times 10^7$ m（距地心约42,000公里，或高度35,786公里）。

**Flashcard 5:**
Q (EN): Why doesn't the mass of the satellite appear in Kepler's Third Law?
Q (CN): 为什么卫星的质量不出现在开普勒第三定律中？
A (EN): Because the satellite's mass cancels out when equating gravitational force ($GMm/r^2$) to centripetal force ($mv^2/r$). The period depends only on the central body's mass and orbital radius.
A (CN): 因为在引力（$GMm/r^2$）等于向心力（$mv^2/r$）时，卫星质量被消去。周期只取决于中心天体的质量和轨道半径。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Kepler's Third Law"
  cn: "开普勒第三定律"
parent_topic: "Circular Orbits"
parent_hub: "[[Circular Orbits]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Orbital Velocity]]"
  - "[[Geostationary Satellites]]"
prerequisites:
  - "[[Gravitational Force and Field]]"
  - "[[Centripetal Acceleration and Force]]"
related_topics:
  - "[[Gravitational Potential]]"
language: bilingual_en_cn