# Vector Addition and Subtraction / 向量加法与减法

---

# 1. Overview / 概述

**English:**
Vector addition and subtraction are fundamental operations in physics that allow us to combine or compare vector quantities such as [[Vector Quantities|displacement]], velocity, and force. Unlike scalars, vectors have both magnitude and direction, so their addition and subtraction must account for direction through geometric or algebraic methods. This sub-topic introduces two primary techniques: the **graphical method** (tip-to-tail) and the **component method** (using [[Resolution of Vectors]]). Mastering these operations is essential for solving problems in [[Displacement, Velocity and Acceleration|kinematics]], [[Types of Force|statics]], and [[Projectile Motion]].

**中文:**
向量加法与减法是物理学中的基本运算，用于组合或比较位移、速度和力等[[Vector Quantities|向量量]]。与标量不同，向量既有大小又有方向，因此它们的加减必须通过几何或代数方法考虑方向。本子知识点介绍两种主要技巧：**图解法**（首尾相接法）和**分量法**（利用[[Resolution of Vectors|向量分解]]）。掌握这些运算对于解决[[Displacement, Velocity and Acceleration|运动学]]、[[Types of Force|静力学]]和[[Projectile Motion|抛体运动]]中的问题至关重要。

---

# 2. Core Definition / 核心定义

| Term (EN/CN)                   | Definition (EN)                                                                                                                   | Definition (CN)                    |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Vector Addition** / 向量加法     | The operation of combining two or more vectors to produce a resultant vector that represents their combined effect.               | 将两个或多个向量组合成一个合向量的运算，该合向量代表它们的综合效果。 |
| **Vector Subtraction** / 向量减法  | The operation of finding the difference between two vectors, equivalent to adding the negative of the second vector to the first. | 求两个向量之差的运算，等价于将第一个向量加上第二个向量的负向量。   |
| **Resultant Vector** / 合向量     | The single vector that has the same effect as the sum of two or more vectors.                                                     | 与两个或多个向量之和具有相同效果的一个向量。             |
| **Negative Vector** / 负向量      | A vector with the same magnitude as the original but opposite direction (180° rotated).                                           | 大小与原向量相同但方向相反（旋转180°）的向量。          |
| **Tip-to-Tail Method** / 首尾相接法 | A graphical method where vectors are drawn sequentially, with the tail of each vector placed at the tip of the previous one.      | 一种图解法，依次绘制向量，每个向量的尾部放在前一个向量的头部。    |
| **Component Method** / 分量法     | An algebraic method that resolves vectors into perpendicular components, adds components separately, then recombines.             | 一种代数方法，将向量分解为垂直分量，分别相加分量，然后重新组合。   |

---

# 3. Key Concepts / 关键概念

**English:**

### Graphical Addition: Tip-to-Tail Method
The most intuitive way to add vectors is the **tip-to-tail method**:
1. Draw the first vector to scale, with correct direction.
2. Place the tail of the second vector at the tip of the first.
3. Continue for all vectors.
4. The **resultant vector** is drawn from the tail of the first vector to the tip of the last vector.

This method works for any number of vectors and is especially useful for visualizing [[Vector Quantities|vector quantities]] in two dimensions.

### Vector Subtraction
Vector subtraction is defined as adding the **negative vector**:
$$ \vec{A} - \vec{B} = \vec{A} + (-\vec{B}) $$

The negative vector $-\vec{B}$ has the same magnitude as $\vec{B}$ but points in the opposite direction. Graphically, to subtract $\vec{B}$ from $\vec{A}$, reverse the direction of $\vec{B}$ and then add it tip-to-tail to $\vec{A}$.

### Component Method (Algebraic)
For precise calculations, use the **component method** (requires [[Resolution of Vectors]]):
1. Resolve each vector into $x$ and $y$ components.
2. Sum all $x$-components: $R_x = \sum A_x$
3. Sum all $y$-components: $R_y = \sum A_y$
4. Find resultant magnitude: $R = \sqrt{R_x^2 + R_y^2}$
5. Find resultant direction: $\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)$

### Common Pitfalls
- **Forgetting direction**: Vectors are not scalars; direction matters in addition.
- **Wrong angle reference**: Always specify which angle (e.g., from positive $x$-axis, from north).
- **Sign errors in components**: $x$-components to the right are positive; to the left, negative. Similarly for $y$.
- **Confusing subtraction**: Remember $\vec{A} - \vec{B}$ is NOT the same as $\vec{B} - \vec{A}$; they point in opposite directions.

**中文:**

### 图解法：首尾相接法
最直观的向量加法是**首尾相接法**：
1. 按比例绘制第一个向量，方向正确。
2. 将第二个向量的尾部放在第一个向量的头部。
3. 对所有向量重复此过程。
4. **合向量**从第一个向量的尾部画到最后一个向量的头部。

此方法适用于任意数量的向量，特别有助于可视化二维中的[[Vector Quantities|向量量]]。

### 向量减法
向量减法定义为加上**负向量**：
$$ \vec{A} - \vec{B} = \vec{A} + (-\vec{B}) $$

负向量 $-\vec{B}$ 的大小与 $\vec{B}$ 相同，但方向相反。图解法中，要从 $\vec{A}$ 中减去 $\vec{B}$，将 $\vec{B}$ 的方向反转，然后首尾相接加到 $\vec{A}$ 上。

### 分量法（代数法）
精确计算使用**分量法**（需要[[Resolution of Vectors|向量分解]]）：
1. 将每个向量分解为 $x$ 和 $y$ 分量。
2. 求和所有 $x$ 分量：$R_x = \sum A_x$
3. 求和所有 $y$ 分量：$R_y = \sum A_y$
4. 求合向量大小：$R = \sqrt{R_x^2 + R_y^2}$
5. 求合向量方向：$\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)$

### 常见错误
- **忘记方向**：向量不是标量；加法中方向很重要。
- **角度参考错误**：始终明确指定角度（例如，从正 $x$ 轴、从正北方向）。
- **分量符号错误**：向右的 $x$ 分量为正；向左为负。$y$ 分量同理。
- **混淆减法**：记住 $\vec{A} - \vec{B}$ 与 $\vec{B} - \vec{A}$ 不同；它们方向相反。

---

# 4. Formulas / 公式

## Resultant Vector Magnitude and Direction

$$ R = \sqrt{R_x^2 + R_y^2} $$

$$ \theta = \tan^{-1}\left(\frac{R_y}{R_x}\right) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $R$ | Magnitude of resultant vector | 合向量的大小 | Same as input vectors |
| $R_x$ | Sum of all $x$-components | 所有 $x$ 分量的和 | Same as input vectors |
| $R_y$ | Sum of all $y$-components | 所有 $y$ 分量的和 | Same as input vectors |
| $\theta$ | Direction of resultant (from positive $x$-axis) | 合向量的方向（从正 $x$ 轴起算） | degrees (°) or radians |

## Vector Subtraction Formula

$$ \vec{A} - \vec{B} = \vec{A} + (-\vec{B}) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{A}$ | First vector | 第一个向量 | — |
| $\vec{B}$ | Second vector | 第二个向量 | — |
| $-\vec{B}$ | Negative of $\vec{B}$ (same magnitude, opposite direction) | $\vec{B}$ 的负向量（大小相同，方向相反） | — |

**Derivation / 推导:**
The component method formula follows directly from [[Resolution of Vectors]] and the Pythagorean theorem. When vectors are resolved into perpendicular components, the $x$ and $y$ components are independent scalars that can be added algebraically. The resultant is then the vector sum of the perpendicular components.

**Conditions / 适用条件:**
- The component method requires a consistent coordinate system (usually Cartesian).
- The tip-to-tail method works for any vectors in any orientation.
- Vector subtraction is defined only for vectors of the same type (e.g., both displacements, both forces).

> 📷 **IMAGE PROMPT — VEC-ADD-01: Tip-to-Tail Vector Addition Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing the tip-to-tail addition of two vectors A and B. Vector A (blue, 4 units long, pointing 30° above horizontal) and Vector B (red, 3 units long, pointing 60° below horizontal) are drawn tip-to-tail. The resultant vector R (green, dashed) connects the tail of A to the tip of B. All vectors are labeled with arrows. A coordinate grid is faintly visible in the background. The diagram is on a white background with clear, bold labels. Style: educational vector illustration, flat design, high contrast.
>
> **中文描述:**
> 一个干净、教科书风格的向量图，展示两个向量 A 和 B 的首尾相接加法。向量 A（蓝色，4 单位长，与水平方向成 30° 向上）和向量 B（红色，3 单位长，与水平方向成 60° 向下）首尾相接绘制。合向量 R（绿色，虚线）连接 A 的尾部和 B 的头部。所有向量都标有箭头。背景中隐约可见坐标网格。白色背景，清晰粗体标签。风格：教育向量插图，平面设计，高对比度。
>
> **Labels Required / 需要标注:**
> * $\vec{A}$ (blue arrow)
> * $\vec{B}$ (red arrow)
> * $\vec{R} = \vec{A} + \vec{B}$ (green dashed arrow)
> * Angles: 30°, 60°
>
> **Style / 风格:** Textbook vector / flat design
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding the geometric interpretation of vector addition, which is frequently tested in AS-level exams for graphical solutions.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — VEC-ADD-02: Vector Subtraction Visualization**
>
> **English Prompt:**
> A side-by-side comparison diagram showing vector subtraction. Left panel: Two vectors A (blue, pointing right-up) and B (red, pointing right-down). Right panel: The subtraction A - B is shown as A + (-B), where -B is drawn as a red dashed arrow pointing opposite to B. The resultant R = A - B is shown as a green arrow. All vectors have arrowheads and labels. Clean white background, educational style, suitable for a physics textbook. Include angle markers where helpful.
>
> **中文描述:**
> 一个并排比较图，展示向量减法。左面板：两个向量 A（蓝色，指向右上方）和 B（红色，指向右下方）。右面板：减法 A - B 显示为 A + (-B)，其中 -B 绘制为红色虚线箭头，指向与 B 相反。结果 R = A - B 显示为绿色箭头。所有向量都有箭头和标签。干净的白色背景，教育风格，适合物理教科书。在有用处包含角度标记。
>
> **Labels Required / 需要标注:**
> * $\vec{A}$, $\vec{B}$, $-\vec{B}$, $\vec{R} = \vec{A} - \vec{B}$
>
> **Style / 风格:** Textbook vector / flat design
>
> **Exam Relevance / 考试关联:**
> Vector subtraction is often tested in the context of relative velocity and displacement problems.

---

# 6. Worked Example / 典型例题

### Example 1: Graphical Addition

#### Question / 题目
**English:**
A hiker walks 5.0 km east, then 3.0 km north. Using the tip-to-tail method, find the magnitude and direction of the resultant displacement.

**中文:**
一名徒步者向东走 5.0 km，然后向北走 3.0 km。使用首尾相接法，求合位移的大小和方向。

#### Solution / 解答

**Step 1: Draw the vectors tip-to-tail**
- First vector: 5.0 km east (→)
- Second vector: 3.0 km north (↑), tail at tip of first vector

**Step 2: Draw the resultant**
- From tail of first to tip of second

**Step 3: Calculate magnitude**
Using Pythagoras:
$$ R = \sqrt{5.0^2 + 3.0^2} = \sqrt{25 + 9} = \sqrt{34} \approx 5.83 \text{ km} $$

**Step 4: Calculate direction**
$$ \theta = \tan^{-1}\left(\frac{3.0}{5.0}\right) = \tan^{-1}(0.6) \approx 31.0^\circ $$
Direction: $31.0^\circ$ north of east (or $031.0^\circ$ bearing)

#### Final Answer / 最终答案
**Answer:** Magnitude = 5.83 km, Direction = 31.0° north of east
**答案:** 大小 = 5.83 km，方向 = 东偏北 31.0°

#### Quick Tip / 提示
In graphical addition, always draw vectors to scale and use a protractor for accurate angle measurement. For exam problems, the component method is often more precise.

---

### Example 2: Component Method

#### Question / 题目
**English:**
Two forces act on a point: $\vec{F}_1 = 10 \text{ N}$ at $30^\circ$ above the positive $x$-axis, and $\vec{F}_2 = 8 \text{ N}$ at $120^\circ$ from the positive $x$-axis. Find the resultant force magnitude and direction.

**中文:**
两个力作用在一个点上：$\vec{F}_1 = 10 \text{ N}$，方向为与正 $x$ 轴成 $30^\circ$ 向上；$\vec{F}_2 = 8 \text{ N}$，方向为与正 $x$ 轴成 $120^\circ$。求合力的大小和方向。

#### Solution / 解答

**Step 1: Resolve into components**

For $\vec{F}_1$:
$$ F_{1x} = 10 \cos 30^\circ = 10 \times 0.866 = 8.66 \text{ N} $$
$$ F_{1y} = 10 \sin 30^\circ = 10 \times 0.5 = 5.00 \text{ N} $$

For $\vec{F}_2$ (120° is in quadrant II):
$$ F_{2x} = 8 \cos 120^\circ = 8 \times (-0.5) = -4.00 \text{ N} $$
$$ F_{2y} = 8 \sin 120^\circ = 8 \times 0.866 = 6.93 \text{ N} $$

**Step 2: Sum components**
$$ R_x = 8.66 + (-4.00) = 4.66 \text{ N} $$
$$ R_y = 5.00 + 6.93 = 11.93 \text{ N} $$

**Step 3: Find magnitude**
$$ R = \sqrt{4.66^2 + 11.93^2} = \sqrt{21.72 + 142.32} = \sqrt{164.04} \approx 12.81 \text{ N} $$

**Step 4: Find direction**
$$ \theta = \tan^{-1}\left(\frac{11.93}{4.66}\right) = \tan^{-1}(2.56) \approx 68.7^\circ $$
Since both $R_x$ and $R_y$ are positive, the resultant is in quadrant I.

#### Final Answer / 最终答案
**Answer:** Magnitude = 12.8 N, Direction = 68.7° above the positive $x$-axis
**答案:** 大小 = 12.8 N，方向 = 与正 $x$ 轴成 68.7° 向上

#### Quick Tip / 提示
Always check the quadrant of your resultant! The $\tan^{-1}$ function only gives angles in quadrants I and IV. If $R_x$ is negative, add 180° to the angle.

---

# 7. Flashcards / 闪卡

**Flashcard 1**
- **Q (EN):** What is the tip-to-tail method for vector addition?
- **Q (CN):** 什么是向量加法的首尾相接法？
- **A (EN):** A graphical method where vectors are drawn sequentially, with the tail of each vector placed at the tip of the previous one. The resultant is drawn from the tail of the first to the tip of the last.
- **A (CN):** 一种图解法，依次绘制向量，每个向量的尾部放在前一个向量的头部。合向量从第一个向量的尾部画到最后一个向量的头部。

**Flashcard 2**
- **Q (EN):** How is vector subtraction defined?
- **Q (CN):** 向量减法是如何定义的？
- **A (EN):** Vector subtraction is defined as adding the negative vector: $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$, where $-\vec{B}$ has the same magnitude as $\vec{B}$ but opposite direction.
- **A (CN):** 向量减法定义为加上负向量：$\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$，其中 $-\vec{B}$ 的大小与 $\vec{B}$ 相同，但方向相反。

**Flashcard 3**
- **Q (EN):** What are the steps of the component method for vector addition?
- **Q (CN):** 向量加法的分量法有哪些步骤？
- **A (EN):** 1) Resolve each vector into $x$ and $y$ components. 2) Sum all $x$-components: $R_x = \sum A_x$. 3) Sum all $y$-components: $R_y = \sum A_y$. 4) Find magnitude: $R = \sqrt{R_x^2 + R_y^2}$. 5) Find direction: $\theta = \tan^{-1}(R_y/R_x)$.
- **A (CN):** 1) 将每个向量分解为 $x$ 和 $y$ 分量。2) 求和所有 $x$ 分量：$R_x = \sum A_x$。3) 求和所有 $y$ 分量：$R_y = \sum A_y$。4) 求大小：$R = \sqrt{R_x^2 + R_y^2}$。5) 求方向：$\theta = \tan^{-1}(R_y/R_x)$。

**Flashcard 4**
- **Q (EN):** What is a common mistake when using the component method?
- **Q (CN):** 使用分量法时常见的错误是什么？
- **A (EN):)** Forgetting to check the quadrant of the resultant. The $\tan^{-1}$ function only gives angles in quadrants I and IV. If $R_x$ is negative, add 180° to the angle.
- **A (CN):** 忘记检查合向量的象限。$\tan^{-1}$ 函数只给出象限 I 和 IV 中的角度。如果 $R_x$ 为负，则在角度上加 180°。

**Flashcard 5**
- **Q (EN):** What is the difference between $\vec{A} - \vec{B}$ and $\vec{B} - \vec{A}$?
- **Q (CN):** $\vec{A} - \vec{B}$ 和 $\vec{B} - \vec{A}$ 有什么区别？
- **A (EN):** They have the same magnitude but opposite directions. $\vec{A} - \vec{B} = -(\vec{B} - \vec{A})$.
- **A (CN):** 它们大小相同但方向相反。$\vec{A} - \vec{B} = -(\vec{B} - \vec{A})$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Vector Addition and Subtraction
  cn: 向量加法与减法
parent_topic: Scalars and Vectors
parent_hub: "[[Scalars and Vectors]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Scalar Quantities]]"
  - "[[Vector Quantities]]"
  - "[[Resolution of Vectors]]"
  - "[[Displacement, Velocity and Acceleration]]"
  - "[[Projectile Motion]]"
  - "[[Types of Force]]"
language: bilingual_en_cn