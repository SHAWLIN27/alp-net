Here is the complete bilingual leaf node for **Gravitational Potential (V)**.

---

# 1. Overview / 概述

**English:**
This sub-topic introduces the concept of **Gravitational Potential ($V$)**, a scalar quantity that describes the gravitational field at a point in terms of the work done per unit mass to bring a test mass from infinity. Unlike [[Gravitational Force and Field]] (which is a vector), potential allows us to calculate energy changes without worrying about direction. This concept is fundamental to understanding [[Gravitational Potential Energy in a Radial Field]], [[Escape Velocity]], and [[Circular Orbits]]. For A-Level students, mastering the sign convention (potential is always negative) is the most critical step.

**中文:**
本子知识点介绍**引力势 ($V$)** 的概念。这是一个标量，描述了将单位质量从无穷远移动到某一点所做的功。与矢量性质的[[Gravitational Force and Field|引力场]]不同，势能让我们无需考虑方向即可计算能量变化。这个概念是理解[[Gravitational Potential Energy in a Radial Field|径向场中的引力势能]]、[[Escape Velocity|逃逸速度]]和[[Circular Orbits|圆形轨道]]的基础。对于A-Level学生来说，掌握符号约定（势能始终为负）是最关键的一步。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Gravitational Potential ($V$)** / 引力势 | The work done per unit mass in bringing a small test mass from infinity to that point in the field. | 将单位质量的小测试质量从无穷远移动到场中该点所做的功。 |
| **Infinity** / 无穷远 | A point where the gravitational field strength is zero and the potential is defined as zero. | 引力场强度为零且势能被定义为零的点。 |
| **Equipotential Surface** / 等势面 | A surface on which the gravitational potential is constant. No work is done moving a mass along this surface. | 引力势恒定的表面。沿此表面移动质量不做功。 |
| **Negative Potential** / 负势 | A consequence of the attractive nature of gravity; work must be done *against* the field to move a mass away from the Earth. | 引力吸引性质的后果；必须*克服*场做功才能将质量移离地球。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core idea is that **gravitational potential is a scalar field**. For a point mass $M$, the potential at a distance $r$ is given by $V = -\frac{GM}{r}$.

*   **Why is it negative?** Imagine you are at infinity ($V=0$). Gravity is attractive, so as you fall towards Earth, the field does work *on* you, converting gravitational potential energy into kinetic energy. To bring you back to infinity, you must do work *against* the field. Therefore, the potential at any finite point is *less than* zero (negative). This is a common pitfall: students often forget the negative sign in calculations.

*   **Scalar Addition:** Because $V$ is a scalar, the total potential at a point due to multiple masses is simply the algebraic sum of their individual potentials: $V_{total} = V_1 + V_2 + ...$. This is much simpler than vector addition for [[Gravitational Force and Field]].

*   **Relation to [[Potential Gradients]]:** The gravitational field strength $g$ is the negative gradient of the potential: $g = -\frac{dV}{dr}$. On a graph of $V$ vs $r$, the steeper the slope, the stronger the field.

*   **Equipotentials:** These are spherical shells around a point mass. They are always perpendicular to field lines. Moving along an equipotential requires zero work.

**中文:**
核心概念是**引力势是一个标量场**。对于点质量 $M$，在距离 $r$ 处的势能为 $V = -\frac{GM}{r}$。

*   **为什么是负的？** 想象你在无穷远处 ($V=0$)。引力是吸引的，所以当你落向地球时，场对你做功，将引力势能转化为动能。要将你带回无穷远，你必须克服场做功。因此，任何有限点的势能都*小于*零（负的）。这是一个常见的陷阱：学生经常在计算中忘记负号。

*   **标量叠加：** 因为 $V$ 是标量，某一点由于多个质量产生的总势能，就是它们各自势能的代数和：$V_{total} = V_1 + V_2 + ...$。这比[[Gravitational Force and Field|引力场]]的矢量叠加要简单得多。

*   **与[[Potential Gradients|势梯度]]的关系：** 引力场强度 $g$ 是势能的负梯度：$g = -\frac{dV}{dr}$。在 $V$ 对 $r$ 的图上，斜率越陡，场越强。

*   **等势面：** 这些是围绕点质量的球形壳。它们始终垂直于场线。沿着等势面移动不做功。

> 📷 **IMAGE PROMPT — V01: Potential Well Diagram**
>
> **English Prompt:**
> A 3D rendered "potential well" graph. The x and y axes represent spatial coordinates (x, y), and the z-axis represents Gravitational Potential (V). The surface is a deep, smooth funnel shape, colored from dark blue (most negative, at the center) to bright yellow/white (zero, at the edges). A small glowing sphere representing a test mass is shown at the rim of the funnel. Arrows point down the slope, labeled "Field Direction (g)". A dashed circle on the funnel wall is labeled "Equipotential Surface".
>
> **中文描述:**
> 一个3D渲染的“势阱”图。x轴和y轴代表空间坐标，z轴代表引力势(V)。表面是一个深而平滑的漏斗形状，颜色从深蓝色（最负，中心）渐变到亮黄色/白色（零，边缘）。一个小发光球体代表测试质量，位于漏斗边缘。箭头指向斜坡下方，标注为“场方向(g)”。漏斗壁上的虚线圆标注为“等势面”。
>
> **Labels Required / 需要标注:**
> * V = 0 (at infinity / 在无穷远处)
> * V = -GM/r (at point / 在点处)
> * g = -dV/dr (Gradient / 梯度)
>
> **Style / 风格:** 3D render, scientific visualization
>
> **Exam Relevance / 考试关联:**
> Helps visualize why potential is negative and how field strength relates to the slope of the potential.

---

# 4. Formulas / 公式

### Formula 1: Gravitational Potential for a Point Mass

$$ V = -\frac{GM}{r} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $V$ | Gravitational Potential | 引力势 | J kg$^{-1}$ |
| $G$ | Gravitational Constant | 万有引力常数 | N m$^2$ kg$^{-2}$ |
| $M$ | Mass of the object creating the field | 产生场的物体质量 | kg |
| $r$ | Distance from the center of mass $M$ | 距质量 $M$ 中心的距离 | m |

**Derivation / 推导:**
Work done to move a mass $m$ from infinity to a point $r$ is $W = \int_{\infty}^{r} F \, dr = \int_{\infty}^{r} \frac{GMm}{r^2} \, dr = -\frac{GMm}{r}$. Potential is work per unit mass: $V = \frac{W}{m} = -\frac{GM}{r}$.

**Conditions / 适用条件:**
*   Applies to a point mass or a spherically symmetric object (like a planet or star).
*   $r$ must be greater than the radius of the object.

### Formula 2: Potential Difference

$$ \Delta V = V_B - V_A = \frac{W}{m} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\Delta V$ | Change in gravitational potential | 引力势的变化 | J kg$^{-1}$ |
| $W$ | Work done against the field | 克服场做的功 | J |
| $m$ | Mass of the object moved | 被移动物体的质量 | kg |

**Conditions / 适用条件:**
*   Work is done *against* the field if moving to a higher (less negative) potential.
*   Work is done *by* the field if moving to a lower (more negative) potential.

> 📷 **IMAGE PROMPT — V02: V vs r Graph**
>
> **English Prompt:**
> A clean 2D vector graph. X-axis: "Distance from center (r)". Y-axis: "Gravitational Potential (V)". A smooth curve starts from the bottom left (very negative, near r=0) and asymptotically approaches the x-axis (V=0) as r increases. The curve is labeled "V = -GM/r". A tangent line is drawn at a point on the curve, with a note: "Gradient = -g". The area under the curve between two points is shaded and labeled "Work done per unit mass (ΔV)".
>
> **中文描述:**
> 一个清晰的2D矢量图。X轴：“距中心距离(r)”。Y轴：“引力势(V)”。一条平滑曲线从左下角开始（非常负，靠近r=0），随着r增加渐近地接近X轴(V=0)。曲线标注为“V = -GM/r”。在曲线上某点画了一条切线，并附注：“梯度 = -g”。两点之间的曲线下面积被阴影覆盖，标注为“单位质量所做的功(ΔV)”。
>
> **Labels Required / 需要标注:**
> * V = 0 (asymptote / 渐近线)
> * V ∝ -1/r
> * Gradient = -g
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> Directly tested in CAIE 9702/22/O/N/16 Q5 and Edexcel IAL WPH14/01. Students must interpret the graph to find field strength from gradient.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — V03: Equipotentials and Field Lines**
>
> **English Prompt:**
> A 2D cross-section diagram. A large blue circle in the center represents a planet (M). Concentric dashed circles around it represent equipotential surfaces (V1, V2, V3, where V1 < V2 < V3 < 0). Red arrows pointing radially inward from the outer equipotential to the planet represent gravitational field lines (g). A small black dot is shown moving along one of the dashed circles (equipotential) with a note: "W = 0". Another dot is shown moving radially inward with a note: "Work done by field (ΔV negative)".
>
> **中文描述:**
> 一个2D横截面图。中心一个大蓝圈代表行星(M)。围绕它的同心虚线圆代表等势面(V1, V2, V3, 其中 V1 < V2 < V3 < 0)。从外部等势面径向指向行星的红色箭头代表引力场线(g)。一个小黑点沿着其中一个虚线圆（等势面）移动，并附注：“W = 0”。另一个点径向向内移动，并附注：“场做功 (ΔV 为负)”。
>
> **Labels Required / 需要标注:**
> * M (Planet / 行星)
> * V1, V2, V3 (Equipotentials / 等势面)
> * g (Field lines / 场线)
> * "No work along equipotential" / “沿等势面不做功”
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> Tests understanding of the relationship between field lines and equipotentials. Common in multiple-choice questions.

---

# 6. Worked Example / 典型例题

### Example 1: Calculating Potential and Work Done

**Question / 题目**
**English:**
The mass of the Earth is $6.0 \times 10^{24}$ kg and its radius is $6.4 \times 10^6$ m. $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$.
(a) Calculate the gravitational potential at the Earth's surface.
(b) Calculate the work done to move a 500 kg satellite from the Earth's surface to a point where the potential is $-1.0 \times 10^7$ J kg$^{-1}$.

**中文:**
地球质量为 $6.0 \times 10^{24}$ kg，半径为 $6.4 \times 10^6$ m。$G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$。
(a) 计算地球表面的引力势。
(b) 计算将一颗500 kg的卫星从地球表面移动到一个势能为 $-1.0 \times 10^7$ J kg$^{-1}$ 的点所做的功。

### Solution / 解答

**(a)**
$$ V_{surface} = -\frac{GM}{r} = -\frac{(6.67 \times 10^{-11})(6.0 \times 10^{24})}{6.4 \times 10^6} $$
$$ V_{surface} = -\frac{4.002 \times 10^{14}}{6.4 \times 10^6} = -6.25 \times 10^7 \text{ J kg}^{-1} $$

**(b)**
Work done $W = m \Delta V = m (V_{final} - V_{initial})$
$$ W = 500 \times [(-1.0 \times 10^7) - (-6.25 \times 10^7)] $$
$$ W = 500 \times (5.25 \times 10^7) = 2.625 \times 10^{10} \text{ J} $$

### Final Answer / 最终答案
**Answer:** (a) $-6.25 \times 10^7$ J kg$^{-1}$ (b) $2.63 \times 10^{10}$ J
**答案:** (a) $-6.25 \times 10^7$ J kg$^{-1}$ (b) $2.63 \times 10^{10}$ J

### Quick Tip / 提示
Always remember the negative sign! The work done is positive because you are moving the satellite *against* the field to a higher (less negative) potential. **始终记住负号！** 所做的功是正的，因为你是*克服*场将卫星移动到一个更高（负得少）的势能处。

---

# 7. Flashcards / 闪卡

**Card 1:**
Q (EN): Define gravitational potential at a point.
Q (CN): 定义某一点的引力势。
A (EN): The work done per unit mass in bringing a small test mass from infinity to that point.
A (CN): 将单位质量的小测试质量从无穷远移动到该点所做的功。

**Card 2:**
Q (EN): Why is gravitational potential always negative?
Q (CN): 为什么引力势总是负的？
A (EN): Because gravity is attractive. Work must be done against the field to move a mass to infinity (where V=0), so potential at any finite point is less than zero.
A (CN): 因为引力是吸引的。必须克服场做功才能将质量移动到无穷远（V=0），所以任何有限点的势能都小于零。

**Card 3:**
Q (EN): State the formula for gravitational potential due to a point mass M at a distance r.
Q (CN): 写出点质量M在距离r处产生的引力势公式。
A (EN): $V = -\frac{GM}{r}$
A (CN): $V = -\frac{GM}{r}$

**Card 4:**
Q (EN): What is the relationship between gravitational field strength (g) and potential (V)?
Q (CN): 引力场强度(g)和势(V)之间的关系是什么？
A (EN): $g = -\frac{dV}{dr}$. The field strength is the negative gradient of the potential.
A (CN): $g = -\frac{dV}{dr}$。场强是势的负梯度。

**Card 5:**
Q (EN): How much work is done moving a mass along an equipotential surface?
Q (CN): 沿着等势面移动质量做了多少功？
A (EN): Zero work is done because the potential is constant.
A (CN): 不做功，因为势是恒定的。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Gravitational Potential (V)
  cn: 引力势 (V)
parent_topic: Gravitational Potential
parent_hub: "[[Gravitational Potential]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Gravitational Potential Energy in a Radial Field]]"
  - "[[Escape Velocity]]"
  - "[[Potential Gradients]]"
  - "[[Circular Orbits]]"
prerequisites:
  - "[[Gravitational Force and Field]]"
  - "[[Kinetic Energy and Potential Energy]]"
language: bilingual_en_cn