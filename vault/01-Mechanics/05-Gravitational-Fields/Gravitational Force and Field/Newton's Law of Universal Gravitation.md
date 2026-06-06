Here is the complete bilingual leaf node for **Newton's Law of Universal Gravitation**.

---

# 1. Overview / 概述

**English:**
Newton’s Law of Universal Gravitation is the foundational principle describing the attractive force between any two objects with mass. This sub-topic introduces the mathematical form of the law, the concept of the gravitational constant $G$, and the conditions under which the law applies. It is the core mechanism that governs everything from falling apples to planetary orbits, linking directly to [[Gravitational Field Strength]] and providing the basis for [[Circular Orbits]].

Understanding this law requires a solid grasp of [[Newton's Laws of Motion]] (specifically the Third Law) and the inverse-square relationship. It is a prerequisite for exploring [[Gravitational Potential]] and more complex field models.

**中文:**
牛顿万有引力定律是描述任何两个有质量的物体之间吸引力的基本原理。本子知识点介绍了该定律的数学形式、引力常数 $G$ 的概念以及定律的适用条件。它是支配从苹果落地到行星轨道一切现象的核心机制，直接联系到[[Gravitational Field Strength|引力场强度]]，并为[[Circular Orbits|圆周轨道]]提供了基础。

理解这一定律需要扎实掌握[[Newton's Laws of Motion|牛顿运动定律]]（特别是第三定律）和平方反比关系。它是探索[[Gravitational Potential|引力势]]和更复杂场模型的前提。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Newton's Law of Universal Gravitation** / 牛顿万有引力定律 | Every particle of matter in the universe attracts every other particle with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between their centers. | 宇宙中每个质点都以一种力吸引其他每个质点，该力与它们质量的乘积成正比，与它们中心之间距离的平方成反比。 |
| **Gravitational Constant ($G$)** / 引力常数 | The universal constant of proportionality in Newton's law of gravitation, equal to $6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$. | 牛顿万有引力定律中的普适比例常数，等于 $6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$。 |
| **Point Mass** / 质点 | An idealized object with mass concentrated at a single point; the law applies exactly to point masses. | 质量集中于一点的理想化物体；该定律精确适用于质点。 |
| **Inverse Square Law** / 平方反比定律 | A relationship where a physical quantity is inversely proportional to the square of the distance from the source. | 物理量与距源距离的平方成反比的关系。 |
| **Center of Mass** / 质心 | The point at which the entire mass of an object can be considered to act; used for spherical objects in the law. | 物体全部质量可视为作用其上的点；对于球形物体，该定律使用质心。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core of this law is the **inverse-square relationship**. The force $F$ is proportional to $1/r^2$, meaning if the distance between two masses doubles, the gravitational force becomes one-quarter of its original value. This is a direct consequence of the geometry of a sphere and the conservation of flux in three-dimensional space.

The law also implies **Newton's Third Law**: the force on mass $m_1$ due to $m_2$ is equal in magnitude and opposite in direction to the force on $m_2$ due to $m_1$. This is why gravitational forces always come in pairs.

**Common Pitfall:** Students often forget that the distance $r$ is measured from the **center** of the masses, not from their surfaces. For spherical objects (like planets), the law applies as if all mass is concentrated at the [[Center of Mass]].

**Application to Extended Objects:** For a uniform sphere, the law works perfectly using the distance between centers. For irregular shapes, we must treat them as collections of point masses and sum the forces (using calculus).

**中文:**
该定律的核心是**平方反比关系**。力 $F$ 与 $1/r^2$ 成正比，这意味着如果两个质量之间的距离加倍，引力将变为原来的四分之一。这是球体几何学和三维空间中通量守恒的直接结果。

该定律也隐含了**牛顿第三定律**：$m_1$ 对 $m_2$ 的力与 $m_2$ 对 $m_1$ 的力大小相等、方向相反。这就是为什么引力总是成对出现。

**常见错误：** 学生经常忘记距离 $r$ 是从质量的**中心**测量的，而不是从它们的表面。对于球形物体（如行星），该定律适用，就好像所有质量都集中在[[Center of Mass|质心]]一样。

**对扩展物体的应用：** 对于均匀球体，使用中心之间的距离，该定律完美适用。对于不规则形状，我们必须将其视为点质量的集合，并对力求和（使用微积分）。

> 📷 **IMAGE PROMPT — F01: Inverse Square Law Diagram**
>
> **English Prompt:**
> A clean, textbook-style 2D vector diagram. Two labeled spheres (mass m1 and m2) separated by distance r (measured center-to-center). Arrows show gravitational force F on each sphere pointing toward the other. A small inset graph shows F vs r with a steep curve (1/r^2 shape). Labels: "F ∝ 1/r²", "r = distance between centers". White background, black lines, blue arrows.
>
> **中文描述:**
> 一个干净的教科书式二维矢量图。两个标记的球体（质量 m1 和 m2）相距距离 r（从中心到中心测量）。箭头显示每个球体上的引力 F 指向另一个球体。一个小插图显示 F 与 r 的关系，曲线陡峭（1/r² 形状）。标签："F ∝ 1/r²"，"r = 中心之间的距离"。白色背景，黑色线条，蓝色箭头。
>
> **Labels Required / 需要标注:**
> * m1, m2 (masses)
> * r (distance between centers)
> * F (gravitational force arrows)
> * Graph: F vs r
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> Essential for understanding the inverse-square relationship and correct distance measurement.

---

# 4. Formulas / 公式

$$ F = G \frac{m_1 m_2}{r^2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F$ | Gravitational force between masses | 两质量之间的引力 | N |
| $G$ | Gravitational constant ($6.67 \times 10^{-11}$) | 引力常数 | $\text{N m}^2 \text{ kg}^{-2}$ |
| $m_1, m_2$ | Masses of the two objects | 两个物体的质量 | kg |
| $r$ | Distance between centers of mass | 质心之间的距离 | m |

**Derivation / 推导:**
The law is empirical (based on observation). Newton deduced it by comparing the acceleration of the Moon toward Earth ($a_m = v^2/r$) with the acceleration due to gravity on Earth's surface ($g = 9.81 \text{ m s}^{-2}$). He found that the force varied as $1/r^2$, leading to the proportional relationship $F \propto m_1 m_2 / r^2$, with $G$ as the constant of proportionality.

**Conditions / 适用条件:**
1. The objects must be **point masses** or **uniform spheres**.
2. The law applies to **all masses**, but is only significant when at least one mass is very large (e.g., a planet).
3. The distance $r$ must be much larger than the size of the objects for the point mass approximation to be valid.

> 📷 **IMAGE PROMPT — F02: Newton's Apple and Moon Thought Experiment**
>
> **English Prompt:**
> A split illustration. Left side: an apple falling from a tree toward Earth, with a label "g = 9.81 m/s²". Right side: the Moon in orbit around Earth, with a curved path and a label "a_m = v²/r". A dashed line connects the apple to the Moon, with a text bubble: "Same force? F ∝ 1/r²". Earth is drawn as a blue sphere. Style: hand-drawn sketch, sepia tones, reminiscent of Newton's notebooks.
>
> **中文描述:**
> 一个分割的插图。左侧：一个苹果从树上掉向地球，标签为 "g = 9.81 m/s²"。右侧：月球绕地球轨道运行，带有弯曲路径和标签 "a_m = v²/r"。一条虚线连接苹果和月球，带有一个文本框："同一种力？F ∝ 1/r²"。地球被画成一个蓝色球体。风格：手绘草图，棕褐色调，让人联想到牛顿的笔记本。
>
> **Labels Required / 需要标注:**
> * Apple: g = 9.81 m/s²
> * Moon: a_m = v²/r
> * Earth
> * Text bubble: "Same force?"
>
> **Style / 风格:** Hand-drawn sketch
>
> **Exam Relevance / 考试关联:**
> Helps students understand the historical derivation and the universality of the law.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — F03: Gravitational Force Between Two Spheres**
>
> **English Prompt:**
> A 3D rendered scene. Two large, textured spheres (one blue like Earth, one grey like the Moon) floating in a dark space background. A glowing, dashed line connects their centers, labeled "r". Two glowing arrows (F and -F) point from each sphere toward the other, showing equal and opposite forces. A faint grid on the spheres shows their centers. Labels: "m₁", "m₂", "F = G m₁m₂ / r²". Soft lighting, realistic textures, cinematic.
>
> **中文描述:**
> 一个 3D 渲染场景。两个大的、有纹理的球体（一个像地球一样蓝色，一个像月球一样灰色）漂浮在黑暗的太空背景中。一条发光的虚线连接它们的中心，标记为 "r"。两个发光的箭头（F 和 -F）从每个球体指向另一个，显示大小相等、方向相反的力。球体上有一个微弱的网格显示它们的中心。标签："m₁"，"m₂"，"F = G m₁m₂ / r²"。柔和的光线，逼真的纹理，电影感。
>
> **Labels Required / 需要标注:**
> * m₁, m₂
> * r (dashed line)
> * F and -F (force arrows)
> * Formula: F = G m₁m₂ / r²
>
> **Style / 风格:** 3D render, cinematic
>
> **Exam Relevance / 考试关联:**
> Visualizes the vector nature of the force and the center-to-center distance.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
Two identical uniform spheres, each of mass 500 kg, are placed with their centers 2.0 m apart. Calculate the gravitational force between them. ($G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$)

**中文:**
两个相同的均匀球体，每个质量为 500 kg，它们的中心相距 2.0 m。计算它们之间的引力。（$G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$）

### Solution / 解答
**Step 1:** Write down the formula.
$$ F = G \frac{m_1 m_2}{r^2} $$

**Step 2:** Substitute values.
$$ F = (6.67 \times 10^{-11}) \times \frac{500 \times 500}{(2.0)^2} $$

**Step 3:** Calculate.
$$ F = (6.67 \times 10^{-11}) \times \frac{250000}{4} $$
$$ F = (6.67 \times 10^{-11}) \times 62500 $$
$$ F = 4.17 \times 10^{-6} \text{ N} $$

### Final Answer / 最终答案
**Answer:** $4.17 \times 10^{-6} \text{ N}$ **答案:** $4.17 \times 10^{-6} \text{ N}$

### Quick Tip / 提示
**English:** Always check your units! The force is very small for everyday masses because $G$ is tiny. This is why we don't feel gravitational attraction between two people.

**中文:** 始终检查你的单位！因为 $G$ 非常小，日常质量的力非常小。这就是为什么我们感觉不到两个人之间的引力。

---

# 7. Flashcards / 闪卡

**Q (EN):** State Newton's Law of Universal Gravitation.
**Q (CN):** 陈述牛顿万有引力定律。
**A (EN):** Every particle attracts every other particle with a force proportional to the product of their masses and inversely proportional to the square of the distance between their centers.
**A (CN):** 每个质点都以一种力吸引其他每个质点，该力与它们质量的乘积成正比，与它们中心之间距离的平方成反比。

**Q (EN):** What is the value and unit of the gravitational constant G?
**Q (CN):** 引力常数 G 的值和单位是什么？
**A (EN):)** $6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$
**A (CN):** $6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$

**Q (EN):** If the distance between two masses is tripled, what happens to the gravitational force?
**Q (CN):** 如果两个质量之间的距离变为三倍，引力会发生什么变化？
**A (EN):** The force becomes one-ninth ($1/9$) of its original value.
**A (CN):** 力变为原值的九分之一 ($1/9$)。

**Q (EN):** For a uniform sphere, from where is the distance r measured in the law of gravitation?
**Q (CN):** 对于一个均匀球体，万有引力定律中的距离 r 从何处测量？
**A (EN):** From the center of the sphere.
**A (CN):** 从球体的中心。

**Q (EN):** Why don't two people standing next to each other feel a gravitational attraction?
**Q (CN):** 为什么站在一起的两个人感觉不到引力？
**A (EN):** Because the gravitational constant G is extremely small, so the force between small masses is negligible.
**A (CN):** 因为引力常数 G 非常小，所以小质量之间的力可以忽略不计。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Newton's Law of Universal Gravitation"
  cn: "牛顿万有引力定律"
parent_topic: "Gravitational Force and Field"
parent_hub: "[[Gravitational Force and Field]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Gravitational Field Strength]]"
  - "[[Radial vs Uniform Gravitational Fields]]"
  - "[[Gravitational Potential]]"
  - "[[Circular Orbits]]"
language: bilingual_en_cn