# 1. Overview / 概述

**English:**
This sub-topic introduces the **radian** as the SI unit for measuring angles, which is fundamental to understanding circular motion and oscillatory systems in A-Level Physics. Unlike degrees, radians provide a natural, dimensionless measure of angle based on the geometry of a circle. **Angular displacement** ($\theta$) describes the angle through which an object rotates about a fixed axis, analogous to linear displacement in translational motion. Mastering radians and angular displacement is essential before progressing to [[Angular Velocity]], [[Period and Frequency]], and the [[Relationship Between Linear and Angular Quantities]]. This concept builds directly on [[Displacement, Velocity and Acceleration]] from linear kinematics and is a prerequisite for [[Centripetal Acceleration and Force]].

**中文:**
本子知识点介绍**弧度**作为测量角度的SI单位，这对于理解A-Level物理中的圆周运动和振动系统至关重要。与度数不同，弧度基于圆的几何结构提供了一种自然的、无量纲的角度度量。**角位移** ($\theta$) 描述了物体绕固定轴旋转的角度，类似于平移运动中的线位移。掌握弧度和角位移是学习[[Angular Velocity]]、[[Period and Frequency]]以及[[Relationship Between Linear and Angular Quantities]]的基础。本概念直接建立在[[Displacement, Velocity and Acceleration]]的线性运动学基础上，也是学习[[Centripetal Acceleration and Force]]的前提。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Radian** / 弧度 | The angle subtended at the centre of a circle by an arc equal in length to the radius of the circle. | 在圆中，弧长等于半径时所对应的圆心角。 |
| **Angular Displacement** / 角位移 | The angle through which a point or line has been rotated in a specified direction about a fixed axis. | 一个点或线段绕固定轴沿指定方向旋转过的角度。 |
| **Arc Length** / 弧长 | The distance along the curved path of a circle between two points on its circumference. | 圆周上两点之间沿曲线路径的距离。 |
| **Radius** / 半径 | The distance from the centre of a circle to any point on its circumference. | 从圆心到圆周上任意一点的距离。 |
| **Dimensionless Quantity** / 无量纲量 | A quantity that has no physical dimension; radians are dimensionless because they are defined as a ratio of lengths. | 没有物理量纲的量；弧度是无量纲的，因为它被定义为长度的比值。 |

---

# 3. Key Concepts / 关键概念

**English:**

### What is a Radian?
A radian is defined using the geometry of a circle. Consider a circle of radius $r$. If you measure an arc along the circumference that has length $s = r$, then the angle $\theta$ at the centre that subtends this arc is exactly **1 radian**. This definition makes radians a natural and mathematically convenient unit.

The key relationship is:
$$ \theta = \frac{s}{r} $$
where:
- $\theta$ = angle in radians (rad)
- $s$ = arc length (m)
- $r$ = radius (m)

Since both $s$ and $r$ are lengths, their ratio is dimensionless. This is why radians are considered a "pure" or dimensionless unit.

### Converting Between Degrees and Radians
A full circle is $360^\circ$ and also $2\pi$ radians. Therefore:
$$ 2\pi \text{ rad} = 360^\circ $$
$$ \pi \text{ rad} = 180^\circ $$
$$ 1 \text{ rad} = \frac{180^\circ}{\pi} \approx 57.3^\circ $$

Common conversions to memorise:
- $90^\circ = \frac{\pi}{2}$ rad
- $60^\circ = \frac{\pi}{3}$ rad
- $45^\circ = \frac{\pi}{4}$ rad
- $30^\circ = \frac{\pi}{6}$ rad

### Angular Displacement ($\theta$)
Angular displacement is the **vector** quantity representing the change in angular position. For A-Level purposes, we often treat it as a scalar magnitude with a sign convention (clockwise or anticlockwise). The SI unit is the radian (rad).

Unlike linear displacement, angular displacement can exceed $2\pi$ radians for multiple rotations. For example, 3 complete rotations corresponds to $\theta = 3 \times 2\pi = 6\pi$ rad.

### Why Radians Matter in Physics
When deriving formulas for [[Angular Velocity]] ($\omega = \frac{\Delta\theta}{\Delta t}$) and [[Centripetal Acceleration and Force]] ($a = \omega^2 r$), the mathematics only works cleanly when angles are measured in radians. Using degrees would introduce awkward conversion factors. This is why all A-Level circular motion formulas require angles in radians.

**Common Pitfall:** Students often forget to convert degrees to radians before using formulas like $s = r\theta$ or $\omega = \frac{\Delta\theta}{\Delta t}$. Always check your calculator is in **radian mode** for circular motion problems.

**中文:**

### 什么是弧度？
弧度是利用圆的几何结构定义的。考虑一个半径为 $r$ 的圆。如果沿着圆周测量一段弧长 $s = r$，那么这段弧所对应的圆心角 $\theta$ 正好是 **1弧度**。这个定义使弧度成为一种自然且数学上方便的单位。

关键关系是：
$$ \theta = \frac{s}{r} $$
其中：
- $\theta$ = 角度（弧度）
- $s$ = 弧长（米）
- $r$ = 半径（米）

由于 $s$ 和 $r$ 都是长度，它们的比值是无量纲的。这就是为什么弧度被认为是"纯"或无单位的量。

### 度数与弧度的转换
一个完整的圆是 $360^\circ$，也是 $2\pi$ 弧度。因此：
$$ 2\pi \text{ rad} = 360^\circ $$
$$ \pi \text{ rad} = 180^\circ $$
$$ 1 \text{ rad} = \frac{180^\circ}{\pi} \approx 57.3^\circ $$

需要记忆的常见转换：
- $90^\circ = \frac{\pi}{2}$ rad
- $60^\circ = \frac{\pi}{3}$ rad
- $45^\circ = \frac{\pi}{4}$ rad
- $30^\circ = \frac{\pi}{6}$ rad

### 角位移 ($\theta$)
角位移是表示角位置变化的**矢量**量。在A-Level中，我们通常将其视为带有符号约定（顺时针或逆时针）的标量大小。SI单位是弧度（rad）。

与线位移不同，角位移可以超过 $2\pi$ 弧度（多圈旋转）。例如，3整圈旋转对应 $\theta = 3 \times 2\pi = 6\pi$ rad。

### 为什么弧度在物理学中很重要
在推导[[Angular Velocity]] ($\omega = \frac{\Delta\theta}{\Delta t}$) 和[[Centripetal Acceleration and Force]] ($a = \omega^2 r$) 的公式时，只有当角度以弧度测量时，数学运算才能顺利进行。使用度数会引入麻烦的转换因子。这就是为什么所有A-Level圆周运动公式都要求角度以弧度表示。

**常见错误：** 学生在使用 $s = r\theta$ 或 $\omega = \frac{\Delta\theta}{\Delta t}$ 等公式时，经常忘记将度数转换为弧度。在处理圆周运动问题时，务必检查计算器是否处于**弧度模式**。

---

# 4. Formulas / 公式

### Formula 1: Arc Length Relationship

$$ s = r\theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $s$ | Arc length | 弧长 | m |
| $r$ | Radius of circle | 圆的半径 | m |
| $\theta$ | Angle in radians | 角度（弧度） | rad |

**Derivation / 推导:**
From the definition of a radian: $\theta = \frac{s}{r}$. Rearranging gives $s = r\theta$.

**Conditions / 适用条件:**
- $\theta$ must be in **radians** (not degrees)
- The arc is part of a circle of constant radius $r$

### Formula 2: Conversion Between Degrees and Radians

$$ \theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180} $$
$$ \theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\theta_{\text{rad}}$ | Angle in radians | 弧度角度 | rad |
| $\theta_{\text{deg}}$ | Angle in degrees | 度数角度 | $^\circ$ |

**Conditions / 适用条件:**
Always valid for any angle.

> 📷 **IMAGE PROMPT — RAD-01: Radian Definition Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a circle with centre O. A radius line OA is drawn from O to point A on the circumference. Another radius line OB is drawn from O to point B on the circumference. The arc AB is highlighted in a different colour (e.g., red) and labelled "s = r". The angle AOB is marked with a curved arrow and labelled "θ = 1 radian". The radius is labelled "r". Use a white background, black lines, and minimal colour accents. Include a small note: "θ = s/r = 1 when s = r".
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示一个圆心为O的圆。从O到圆周上的点A画一条半径OA。从O到圆周上的点B画另一条半径OB。弧AB用不同颜色（如红色）突出显示，并标注"s = r"。角AOB用弯曲箭头标记，并标注"θ = 1 radian"。半径标注为"r"。使用白色背景、黑色线条和少量色彩点缀。包含小注："θ = s/r = 1 when s = r"。
>
> **Labels Required / 需要标注:**
> * Centre O / 圆心O
> * Radius r / 半径r
> * Arc length s = r / 弧长 s = r
> * Angle θ = 1 rad / 角度 θ = 1 rad
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is frequently used in exam questions to test the definition of a radian. Students must be able to reproduce this definition from memory.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — RAD-02: Angular Displacement Visualisation**
>
> **English Prompt:**
> A 3D-rendered diagram showing a rotating disc or wheel. The disc is shown in two positions: initial position (dashed outline, grey) and final position (solid, blue). A radial line from the centre to the edge is drawn in both positions. The angle between these two radial lines is marked with a curved arrow and labelled "θ (angular displacement)". An arc along the circumference between the two positions is highlighted in red and labelled "s (arc length)". The radius is labelled "r". Include a small axis arrow showing the direction of rotation (anticlockwise). Use a clean, educational 3D style with soft lighting and a gradient background.
>
> **中文描述:**
> 一个3D渲染图，显示一个旋转的圆盘或轮子。圆盘显示在两个位置：初始位置（虚线轮廓，灰色）和最终位置（实线，蓝色）。在两个位置都画了一条从圆心到边缘的径向线。这两条径向线之间的角度用弯曲箭头标记，并标注"θ (angular displacement)"。圆周上两个位置之间的弧用红色突出显示，并标注"s (arc length)"。半径标注为"r"。包含一个小箭头显示旋转方向（逆时针）。使用干净的教育3D风格，柔和的灯光和渐变背景。
>
> **Labels Required / 需要标注:**
> * Initial position / 初始位置
> * Final position / 最终位置
> * θ (angular displacement) / θ (角位移)
> * s (arc length) / s (弧长)
> * r (radius) / r (半径)
> * Direction of rotation / 旋转方向
>
> **Style / 风格:** 3D render, educational
>
> **Exam Relevance / 考试关联:**
> Helps students visualise the relationship between angular displacement and arc length, a common exam topic.

---

# 6. Worked Example / 典型例题

### Example 1: Converting Degrees to Radians

**Question / 题目**
**English:** Convert the following angles from degrees to radians:
(a) $45^\circ$
(b) $120^\circ$
(c) $270^\circ$

**中文:** 将以下角度从度数转换为弧度：
(a) $45^\circ$
(b) $120^\circ$
(c) $270^\circ$

**Solution / 解答**
Use the conversion factor $\frac{\pi}{180}$:

(a) $45^\circ \times \frac{\pi}{180} = \frac{45\pi}{180} = \frac{\pi}{4}$ rad

(b) $120^\circ \times \frac{\pi}{180} = \frac{120\pi}{180} = \frac{2\pi}{3}$ rad

(c) $270^\circ \times \frac{\pi}{180} = \frac{270\pi}{180} = \frac{3\pi}{2}$ rad

**Final Answer / 最终答案**
**Answer:** (a) $\frac{\pi}{4}$ rad, (b) $\frac{2\pi}{3}$ rad, (c) $\frac{3\pi}{2}$ rad
**答案:** (a) $\frac{\pi}{4}$ rad, (b) $\frac{2\pi}{3}$ rad, (c) $\frac{3\pi}{2}$ rad

**Quick Tip / 提示**
Memorise the common conversions: $30^\circ = \frac{\pi}{6}$, $45^\circ = \frac{\pi}{4}$, $60^\circ = \frac{\pi}{3}$, $90^\circ = \frac{\pi}{2}$, $180^\circ = \pi$. This will save time in exams.

---

### Example 2: Using $s = r\theta$

**Question / 题目**
**English:** A bicycle wheel has a radius of 35 cm. The wheel rotates through an angle of $150^\circ$. Calculate the distance travelled by a point on the rim of the wheel.

**中文:** 一个自行车轮的半径为35厘米。车轮旋转了 $150^\circ$ 的角度。计算车轮边缘上一点移动的距离。

**Solution / 解答**

**Step 1:** Convert the angle to radians.
$$ \theta = 150^\circ \times \frac{\pi}{180} = \frac{150\pi}{180} = \frac{5\pi}{6} \text{ rad} $$

**Step 2:** Use the formula $s = r\theta$.
$$ s = 0.35 \times \frac{5\pi}{6} $$
$$ s = 0.35 \times 2.618 $$
$$ s = 0.916 \text{ m} $$

**Final Answer / 最终答案**
**Answer:** 0.916 m (or 91.6 cm)
**答案:** 0.916 米（或 91.6 厘米）

**Quick Tip / 提示**
Always convert degrees to radians before using $s = r\theta$. Also, ensure units are consistent — convert cm to m if the answer is required in metres.

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): Define a radian.
Q (CN): 定义弧度。
A (EN): A radian is the angle subtended at the centre of a circle by an arc equal in length to the radius of the circle.
A (CN): 弧度是圆中弧长等于半径时所对应的圆心角。

**Flashcard 2**
Q (EN): What is the relationship between arc length, radius, and angle in radians?
Q (CN): 弧长、半径和弧度角度之间有什么关系？
A (EN): $s = r\theta$, where $s$ is arc length, $r$ is radius, and $\theta$ is the angle in radians.
A (CN): $s = r\theta$，其中 $s$ 是弧长，$r$ 是半径，$\theta$ 是弧度角度。

**Flashcard 3**
Q (EN): Convert $60^\circ$ to radians.
Q (CN): 将 $60^\circ$ 转换为弧度。
A (EN): $\frac{\pi}{3}$ rad.
A (CN): $\frac{\pi}{3}$ rad。

**Flashcard 4**
Q (EN): Why must angles be in radians for circular motion formulas?
Q (CN): 为什么圆周运动公式中的角度必须使用弧度？
A (EN): Because the derivations of formulas like $\omega = \frac{\Delta\theta}{\Delta t}$ and $a = \omega^2 r$ rely on the dimensionless nature of radians. Using degrees would introduce awkward conversion factors.
A (CN): 因为像 $\omega = \frac{\Delta\theta}{\Delta t}$ 和 $a = \omega^2 r$ 这样的公式推导依赖于弧度的无量纲性质。使用度数会引入麻烦的转换因子。

**Flashcard 5**
Q (EN): What is angular displacement?
Q (CN): 什么是角位移？
A (EN): Angular displacement is the angle through which a point or line has been rotated in a specified direction about a fixed axis, measured in radians.
A (CN): 角位移是一个点或线段绕固定轴沿指定方向旋转过的角度，以弧度为单位测量。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Radians and Angular Displacement
  cn: 弧度与角位移
parent_topic: Angular Measures
parent_hub: "[[Angular Measures]]"
subject: Physics
syllabus:
  - CAIE 9702: 14.1 (a-e)
  - Edexcel IAL: WPH14 U4: 5.1-5.4
level: A2
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Angular Velocity]]"
  - "[[Period and Frequency]]"
  - "[[Relationship Between Linear and Angular Quantities]]"
  - "[[Centripetal Acceleration and Force]]"
prerequisites:
  - "[[Displacement, Velocity and Acceleration]]"
language: bilingual_en_cn