---
# Vector Operations (Dot Product, Cross Product)
# 向量运算（点积、叉积）

---

# 1. Overview / 概述

**English:**
This sub-topic extends the basic concept of [[Scalars and Vectors]] by introducing two fundamental operations that combine vectors: the **dot product** (scalar product) and the **cross product** (vector product). In A-Level Physics, the dot product is essential for calculating **work done** by a force at an angle ($W = \vec{F} \cdot \vec{s}$) and **magnetic flux** ($\Phi = \vec{B} \cdot \vec{A}$). The cross product is crucial for understanding **torque** ($\vec{\tau} = \vec{r} \times \vec{F}$) and the **magnetic force** on a moving charge ($\vec{F} = q\vec{v} \times \vec{B}$). Mastering these operations allows you to solve problems involving non-parallel vectors efficiently, moving beyond simple addition and subtraction. This leaf node focuses on the definitions, geometric interpretations, and key applications of these two products, linking directly to [[Trigonometric Functions and Identities for Physics]] for angle calculations.

**中文:**
本子知识点将基础的[[Scalars and Vectors|标量与向量]]概念进行延伸，引入了两种结合向量的基本运算：**点积**（标量积）和**叉积**（向量积）。在A-Level物理中，点积对于计算力在角度下所做的**功** ($W = \vec{F} \cdot \vec{s}$) 和**磁通量** ($\Phi = \vec{B} \cdot \vec{A}$) 至关重要。叉积对于理解**力矩** ($\vec{\tau} = \vec{r} \times \vec{F}$) 和运动电荷所受的**磁力** ($\vec{F} = q\vec{v} \times \vec{B}$) 至关重要。掌握这些运算能让你高效地解决涉及非平行向量的问题，超越简单的加减法。本叶节点聚焦于这两种积的定义、几何解释和关键应用，并直接链接到[[Trigonometric Functions and Identities for Physics|物理中的三角函数与恒等式]]以进行角度计算。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (Mathematical Requirements) | Edexcel IAL (WPH11 U1: Mathematical Skills) |
|-----------|-------------|
| Understand and use the scalar (dot) product of two vectors. | Understand the concept of the scalar (dot) product of two vectors. |
| Understand and use the vector (cross) product of two vectors. | Understand the concept of the vector (cross) product of two vectors. |
| Apply these products to physical situations (e.g., work done, magnetic force). | Apply these products to physical situations (e.g., work done, torque). |

**Examiner Expectations / 考官期望:**
- **EN:** You must be able to calculate the dot product using both the component form ($\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$) and the magnitude-angle form ($\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$). For the cross product, you must be able to find its magnitude using $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$ and determine its direction using the right-hand rule. You are not expected to calculate the cross product in component form for A-Level exams.
- **CN:** 你必须能够使用分量形式 ($\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$) 和大小-角度形式 ($\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$) 计算点积。对于叉积，你必须能使用 $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$ 求出其大小，并使用右手定则确定其方向。A-Level考试不要求你使用分量形式计算叉积。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Dot Product (Scalar Product)** / 点积（标量积） | An operation on two vectors that produces a scalar quantity. It is defined as $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$, where $\theta$ is the angle between the vectors. | 对两个向量进行运算，产生一个标量。定义为 $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$，其中 $\theta$ 是两向量间的夹角。 | Forgetting the $\cos\theta$ factor; thinking the result is a vector. |
| **Cross Product (Vector Product)** / 叉积（向量积） | An operation on two vectors that produces a vector quantity. Its magnitude is $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$, and its direction is perpendicular to both original vectors (right-hand rule). | 对两个向量进行运算，产生一个向量。其大小为 $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$，方向垂直于两个原始向量（右手定则）。 | Forgetting the $\sin\theta$ factor; confusing the direction with the dot product; using the left hand. |
| **Right-Hand Rule** / 右手定则 | A mnemonic for determining the direction of the cross product. Point fingers in direction of $\vec{A}$, curl them towards $\vec{B}$; thumb points in direction of $\vec{A} \times \vec{B}$. | 用于确定叉积方向的助记法。手指指向 $\vec{A}$ 方向，向 $\vec{B}$ 方向弯曲；拇指指向 $\vec{A} \times \vec{B}$ 的方向。 | Using the left hand; curling fingers in the wrong order. |
| **Orthogonal / Perpendicular** / 正交 / 垂直 | Two vectors are orthogonal if their dot product is zero ($\vec{A} \cdot \vec{B} = 0$). | 如果两个向量的点积为零 ($\vec{A} \cdot \vec{B} = 0$)，则它们正交。 | Thinking that a zero dot product always means the vectors are perpendicular (it does, unless one vector is zero). |
| **Parallel** / 平行 | Two vectors are parallel if their cross product is zero ($\vec{A} \times \vec{B} = 0$). | 如果两个向量的叉积为零 ($\vec{A} \times \vec{B} = 0$)，则它们平行。 | Confusing this with the condition for the dot product. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Dot Product (Scalar Product) / 点积（标量积）

### Explanation / 解释
**English:**
The dot product is a way to multiply two vectors to get a scalar. It answers the question: "How much of one vector is acting in the direction of the other?" The formula $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$ shows that the result is the product of the magnitudes of the two vectors and the cosine of the angle between them. If the vectors are parallel ($\theta = 0^\circ$), $\cos\theta = 1$, and the dot product is maximum ($|\vec{A}||\vec{B}|$). If they are perpendicular ($\theta = 90^\circ$), $\cos\theta = 0$, and the dot product is zero. This is a key test for perpendicularity. In component form, for vectors $\vec{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$ and $\vec{B} = B_x\hat{i} + B_y\hat{j} + B_z\hat{k}$, the dot product is $\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$. This is often easier for calculation. The primary physical application is calculating **work done**: $W = \vec{F} \cdot \vec{s} = Fs\cos\theta$, where only the component of force parallel to displacement does work. Another is **magnetic flux**: $\Phi = \vec{B} \cdot \vec{A} = BA\cos\theta$, where $\vec{A}$ is the area vector (perpendicular to the surface).

**中文:**
点积是将两个向量相乘得到一个标量的方法。它回答了这样一个问题："一个向量有多少作用在另一个向量的方向上？" 公式 $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$ 表明，结果是两个向量的大小与它们之间夹角余弦的乘积。如果向量平行 ($\theta = 0^\circ$)，$\cos\theta = 1$，点积最大 ($|\vec{A}||\vec{B}|$)。如果它们垂直 ($\theta = 90^\circ$)，$\cos\theta = 0$，点积为零。这是垂直性的关键测试。在分量形式中，对于向量 $\vec{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$ 和 $\vec{B} = B_x\hat{i} + B_y\hat{j} + B_z\hat{k}$，点积为 $\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$。这通常更易于计算。主要的物理应用是计算**功**：$W = \vec{F} \cdot \vec{s} = Fs\cos\theta$，其中只有平行于位移的力分量做功。另一个是**磁通量**：$\Phi = \vec{B} \cdot \vec{A} = BA\cos\theta$，其中 $\vec{A}$ 是面积向量（垂直于表面）。

### Physical Meaning / 物理意义
**English:** The dot product measures the projection of one vector onto another. It tells you the component of vector $\vec{A}$ that lies along the direction of vector $\vec{B}$, multiplied by the magnitude of $\vec{B}$.
**中文:** 点积衡量一个向量在另一个向量上的投影。它告诉你向量 $\vec{A}$ 在向量 $\vec{B}$ 方向上的分量，乘以 $\vec{B}$ 的大小。

### Common Misconceptions / 常见误区
- **EN:** Thinking the dot product is a vector. It is a scalar.
- **CN:** 认为点积是向量。它是标量。
- **EN:** Forgetting the $\cos\theta$ factor when using the magnitude-angle form.
- **CN:** 使用大小-角度形式时忘记 $\cos\theta$ 因子。
- **EN:** Confusing the dot product with simple multiplication of magnitudes.
- **CN:** 将点积与简单的大小相乘混淆。

### Exam Tips / 考试提示
- **EN:** If a question asks for "work done" and the force is at an angle to the displacement, you must use the dot product: $W = Fs\cos\theta$.
- **CN:** 如果问题要求计算"功"，且力与位移成一定角度，你必须使用点积：$W = Fs\cos\theta$。
- **EN:** To find the angle between two vectors, rearrange the dot product formula: $\cos\theta = \frac{\vec{A} \cdot \vec{B}}{|\vec{A}||\vec{B}|}$.
- **CN:** 要找到两个向量之间的夹角，重新排列点积公式：$\cos\theta = \frac{\vec{A} \cdot \vec{B}}{|\vec{A}||\vec{B}|}$。

> 📷 **IMAGE PROMPT — DOT-PROD-01: Geometric Interpretation of Dot Product**
> A diagram showing two vectors, A and B, originating from the same point. A dashed line is drawn from the tip of vector A perpendicular to vector B, showing the projection of A onto B. The angle θ between them is labeled. The formula A·B = |A||B|cosθ is displayed next to the diagram.

## 4.2 The Cross Product (Vector Product) / 叉积（向量积）

### Explanation / 解释
**English:**
The cross product is a way to multiply two vectors to get a third vector. It answers the question: "What is the vector that is perpendicular to both original vectors, and how large is it?" The magnitude of the result is $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$. This is maximum when the vectors are perpendicular ($\theta = 90^\circ$, $\sin\theta = 1$) and zero when they are parallel ($\theta = 0^\circ$, $\sin\theta = 0$). The direction of the resulting vector is given by the **right-hand rule**: point the fingers of your right hand in the direction of the first vector ($\vec{A}$), curl them towards the second vector ($\vec{B}$), and your thumb points in the direction of the cross product ($\vec{A} \times \vec{B}$). The cross product is anti-commutative: $\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$. The primary physical application is calculating **torque**: $\vec{\tau} = \vec{r} \times \vec{F}$, where $\vec{r}$ is the position vector from the pivot to the point of force application. The magnitude of torque is $\tau = rF\sin\theta$. Another is the **magnetic force** on a moving charge: $\vec{F} = q\vec{v} \times \vec{B}$, with magnitude $F = qvB\sin\theta$.

**中文:**
叉积是将两个向量相乘得到第三个向量的方法。它回答了这样一个问题："垂直于两个原始向量的向量是什么，它有多大？" 结果的大小是 $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$。当向量垂直时 ($\theta = 90^\circ$, $\sin\theta = 1$) 最大，当它们平行时 ($\theta = 0^\circ$, $\sin\theta = 0$) 为零。结果向量的方向由**右手定则**给出：将右手的手指指向第一个向量 ($\vec{A}$) 的方向，向第二个向量 ($\vec{B}$) 的方向弯曲，拇指指向叉积 ($\vec{A} \times \vec{B}$) 的方向。叉积是反交换的：$\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$。主要的物理应用是计算**力矩**：$\vec{\tau} = \vec{r} \times \vec{F}$，其中 $\vec{r}$ 是从支点到力作用点的位置向量。力矩的大小是 $\tau = rF\sin\theta$。另一个是运动电荷所受的**磁力**：$\vec{F} = q\vec{v} \times \vec{B}$，大小为 $F = qvB\sin\theta$。

### Physical Meaning / 物理意义
**English:** The cross product measures the "perpendicular component" of one vector relative to another. The magnitude is the area of the parallelogram formed by the two vectors.
**中文:** 叉积衡量一个向量相对于另一个向量的"垂直分量"。其大小是由这两个向量构成的平行四边形的面积。

### Common Misconceptions / 常见误区
- **EN:** Thinking the cross product is a scalar. It is a vector.
- **CN:** 认为叉积是标量。它是向量。
- **EN:** Forgetting the $\sin\theta$ factor when calculating the magnitude.
- **CN:** 计算大小时忘记 $\sin\theta$ 因子。
- **EN:** Using the left hand for the right-hand rule.
- **CN:** 使用左手进行右手定则。
- **EN:** Getting the order wrong in the right-hand rule (fingers from first to second vector).
- **CN:** 右手定则中顺序搞错（手指从第一个向量指向第二个向量）。

### Exam Tips / 考试提示
- **EN:** For torque problems, identify the pivot point, the position vector $\vec{r}$ from the pivot to the force, and the angle between $\vec{r}$ and $\vec{F}$.
- **CN:** 对于力矩问题，确定支点、从支点到力的位置向量 $\vec{r}$，以及 $\vec{r}$ 和 $\vec{F}$ 之间的夹角。
- **EN:** For magnetic force on a current-carrying wire ($\vec{F} = I\vec{l} \times \vec{B}$), the length vector $\vec{l}$ is in the direction of the current.
- **CN:** 对于载流导线所受的磁力 ($\vec{F} = I\vec{l} \times \vec{B}$)，长度向量 $\vec{l}$ 的方向与电流方向相同。
- **EN:** You will not be asked to calculate the cross product in component form (e.g., using determinants) in A-Level exams.
- **CN:** A-Level考试不会要求你使用分量形式（例如，使用行列式）计算叉积。

> 📷 **IMAGE PROMPT — CROSS-PROD-01: Right-Hand Rule for Cross Product**
> A 3D diagram showing two vectors, A (red) and B (blue), originating from the same point. A right hand is shown with fingers pointing in the direction of A, curling towards B. The thumb points in the direction of the resulting vector C = A × B (green), which is perpendicular to both A and B. The angle θ between A and B is labeled.

---

# 5. Essential Equations / 核心公式

## 5.1 Dot Product (Scalar Product) / 点积（标量积）

$$ \vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\vec{A} \cdot \vec{B}$ | Dot product of A and B | A和B的点积 | Depends on context (e.g., J for work, Wb for flux) |
| $|\vec{A}|$ | Magnitude of vector A | 向量A的大小 | Depends on context (e.g., N, m, T) |
| $|\vec{B}|$ | Magnitude of vector B | 向量B的大小 | Depends on context (e.g., m, m², A) |
| $\theta$ | Angle between vectors A and B | 向量A和B之间的夹角 | degrees or radians |

**Component Form / 分量形式:**
$$ \vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z $$

**Conditions / 适用条件:**
- **EN:** The dot product is defined for any two vectors of the same dimension.
- **CN:** 点积适用于任何两个维度相同的向量。

**Limitations / 局限性:**
- **EN:** The result is a scalar, so it cannot represent a direction.
- **CN:** 结果是标量，因此不能表示方向。

## 5.2 Cross Product (Vector Product) / 叉积（向量积）

$$ |\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $|\vec{A} \times \vec{B}|$ | Magnitude of the cross product of A and B | A和B的叉积的大小 | Depends on context (e.g., Nm for torque, N for force) |
| $|\vec{A}|$ | Magnitude of vector A | 向量A的大小 | Depends on context (e.g., m, C, T) |
| $|\vec{B}|$ | Magnitude of vector B | 向量B的大小 | Depends on context (e.g., N, m/s, A) |
| $\theta$ | Angle between vectors A and B | 向量A和B之间的夹角 | degrees or radians |

**Direction / 方向:**
- **EN:** Given by the right-hand rule. The resulting vector is perpendicular to both $\vec{A}$ and $\vec{B}$.
- **CN:** 由右手定则给出。结果向量垂直于 $\vec{A}$ 和 $\vec{B}$。

**Conditions / 适用条件:**
- **EN:** The cross product is defined for any two vectors in 3D space.
- **CN:** 叉积适用于三维空间中的任何两个向量。

**Limitations / 局限性:**
- **EN:** The cross product is not defined for 2D vectors, but its magnitude can still be calculated if the vectors are considered to be in a plane.
- **CN:** 叉积不适用于二维向量，但如果将向量视为在平面内，仍可计算其大小。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Dot Product vs. Angle / 点积与角度的关系

### Axes / 坐标轴
- **X-axis:** Angle $\theta$ between vectors (0° to 180°)
- **Y-axis:** Dot product $\vec{A} \cdot \vec{B}$ (in units of $|\vec{A}||\vec{B}|$)

### Shape / 形状
- **EN:** A cosine curve. It starts at a maximum positive value at $\theta = 0^\circ$, crosses zero at $\theta = 90^\circ$, and reaches a minimum negative value at $\theta = 180^\circ$.
- **CN:** 余弦曲线。从 $\theta = 0^\circ$ 的最大正值开始，在 $\theta = 90^\circ$ 处过零，在 $\theta = 180^\circ$ 处达到最小负值。

### Gradient Meaning / 斜率含义
- **EN:** The gradient is $-|\vec{A}||\vec{B}|\sin\theta$, which is the negative of the magnitude of the cross product.
- **CN:** 斜率为 $-|\vec{A}||\vec{B}|\sin\theta$，即叉积大小的负值。

### Area Meaning / 面积含义
- **EN:** Not applicable for this graph.
- **CN:** 不适用于此图。

### Exam Interpretation / 考试解读
- **EN:** A zero dot product indicates the vectors are perpendicular. A negative dot product indicates the angle between them is greater than 90°.
- **CN:** 点积为零表示向量垂直。点积为负表示它们之间的夹角大于90°。

## 6.2 Cross Product Magnitude vs. Angle / 叉积大小与角度的关系

### Axes / 坐标轴
- **X-axis:** Angle $\theta$ between vectors (0° to 180°)
- **Y-axis:** Magnitude of cross product $|\vec{A} \times \vec{B}|$ (in units of $|\vec{A}||\vec{B}|$)

### Shape / 形状
- **EN:** A sine curve. It starts at zero at $\theta = 0^\circ$, reaches a maximum at $\theta = 90^\circ$, and returns to zero at $\theta = 180^\circ$.
- **CN:** 正弦曲线。从 $\theta = 0^\circ$ 的零开始，在 $\theta = 90^\circ$ 处达到最大值，在 $\theta = 180^\circ$ 处回到零。

### Gradient Meaning / 斜率含义
- **EN:** The gradient is $|\vec{A}||\vec{B}|\cos\theta$, which is the dot product.
- **CN:** 斜率为 $|\vec{A}||\vec{B}|\cos\theta$，即点积。

### Area Meaning / 面积含义
- **EN:** Not applicable for this graph.
- **CN:** 不适用于此图。

### Exam Interpretation / 考试解读
- **EN:** A zero cross product magnitude indicates the vectors are parallel. A maximum cross product magnitude indicates the vectors are perpendicular.
- **CN:** 叉积大小为零表示向量平行。叉积大小最大表示向量垂直。

---

# 7. Required Diagrams / 必备图表

## 7.1 Work Done by a Force at an Angle / 力在角度下做功

### Description / 描述
- **EN:** A diagram showing a force $\vec{F}$ applied to an object, causing a displacement $\vec{s}$. The force is at an angle $\theta$ to the displacement. The component of the force parallel to the displacement ($F\cos\theta$) is shown.
- **CN:** 一个图表，显示施加在物体上的力 $\vec{F}$ 导致位移 $\vec{s}$。力与位移成 $\theta$ 角。显示了平行于位移的力分量 ($F\cos\theta$)。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — VEC-OPS-01: Work Done by a Force at an Angle**
> A simple 2D diagram. A block is shown on a horizontal surface. An arrow labeled "F" points from the block at an angle θ above the horizontal. Another arrow labeled "s" points horizontally to the right from the block. A dashed line shows the horizontal component of F, labeled "F cos θ". The angle θ between F and s is marked. The equation W = F s cos θ is displayed.

### Labels Required / 需要标注
- **EN:** Force $\vec{F}$, displacement $\vec{s}$, angle $\theta$, component $F\cos\theta$.
- **CN:** 力 $\vec{F}$，位移 $\vec{s}$，角度 $\theta$，分量 $F\cos\theta$。

### Exam Importance / 考试重要性
- **EN:** This is the most common application of the dot product in mechanics.
- **CN:** 这是力学中点积最常见的应用。

## 7.2 Torque from a Force / 力产生的力矩

### Description / 描述
- **EN:** A diagram showing a force $\vec{F}$ applied at a point on a lever arm, with a position vector $\vec{r}$ from the pivot to the point of application. The angle $\theta$ between $\vec{r}$ and $\vec{F}$ is shown. The perpendicular component of the force ($F\sin\theta$) is shown.
- **CN:** 一个图表，显示施加在杠杆臂上某点的力 $\vec{F}$，以及从支点到作用点的位置向量 $\vec{r}$。显示了 $\vec{r}$ 和 $\vec{F}$ 之间的夹角 $\theta$。显示了力的垂直分量 ($F\sin\theta$)。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — VEC-OPS-02: Torque from a Force**
> A 2D diagram. A pivot point is shown as a small circle. A line (the lever arm) extends from the pivot. At the end of the lever arm, a force vector F is applied at an angle θ to the lever arm. The position vector r from the pivot to the point of force application is shown along the lever arm. A dashed line shows the perpendicular component of F, labeled "F sin θ". The equation τ = r F sin θ is displayed.

### Labels Required / 需要标注
- **EN:** Pivot, position vector $\vec{r}$, force $\vec{F}$, angle $\theta$, component $F\sin\theta$.
- **CN:** 支点，位置向量 $\vec{r}$，力 $\vec{F}$，角度 $\theta$，分量 $F\sin\theta$。

### Exam Importance / 考试重要性
- **EN:** This is the most common application of the cross product in mechanics.
- **CN:** 这是力学中叉积最常见的应用。

---

# 8. Worked Examples / 典型例题

## Example 1: Work Done by a Force / 例1：力所做的功

### Question / 题目
**English:**
A force of $\vec{F} = (3\hat{i} + 4\hat{j})$ N acts on an object, causing a displacement of $\vec{s} = (5\hat{i} + 2\hat{j})$ m. Calculate the work done by the force.

**中文:**
一个力 $\vec{F} = (3\hat{i} + 4\hat{j})$ N 作用在一个物体上，产生了 $\vec{s} = (5\hat{i} + 2\hat{j})$ m 的位移。计算该力所做的功。

### Solution / 解答
**Step 1: Recall the formula for work done using the dot product.**
$W = \vec{F} \cdot \vec{s}$

**Step 2: Use the component form of the dot product.**
$\vec{F} \cdot \vec{s} = F_x s_x + F_y s_y$

**Step 3: Substitute the values.**
$W = (3)(5) + (4)(2) = 15 + 8 = 23$ J

### Final Answer / 最终答案
**Answer:** 23 J | **答案：** 23 J

### Quick Tip / 提示
- **EN:** When vectors are given in component form, use the component form of the dot product. It is much faster than finding the magnitudes and the angle.
- **CN:** 当向量以分量形式给出时，使用点积的分量形式。这比求大小和角度快得多。

## Example 2: Magnitude of Torque / 例2：力矩的大小

### Question / 题目
**English:**
A force of 10 N is applied to the end of a 0.5 m long spanner at an angle of 30° to the spanner. Calculate the magnitude of the torque produced about the pivot.

**中文:**
一个10 N的力施加在0.5 m长的扳手末端，与扳手成30°角。计算绕支点产生的力矩大小。

### Solution / 解答
**Step 1: Recall the formula for the magnitude of torque.**
$\tau = |\vec{r} \times \vec{F}| = rF\sin\theta$

**Step 2: Identify the variables.**
$r = 0.5$ m (position vector from pivot to point of force application)
$F = 10$ N (force)
$\theta = 30^\circ$ (angle between $\vec{r}$ and $\vec{F}$)

**Step 3: Substitute the values.**
$\tau = (0.5)(10)\sin(30^\circ) = 5 \times 0.5 = 2.5$ Nm

### Final Answer / 最终答案
**Answer:** 2.5 Nm | **答案：** 2.5 Nm

### Quick Tip / 提示
- **EN:** The angle $\theta$ is always the angle between the position vector $\vec{r}$ and the force vector $\vec{F}$. Make sure you identify this correctly.
- **CN:** 角度 $\theta$ 始终是位置向量 $\vec{r}$ 和力向量 $\vec{F}$ 之间的夹角。确保你正确识别了它。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate work done using dot product (component form) | High | Easy | 📝 *待填入* |
| Calculate work done using dot product (magnitude-angle form) | High | Easy | 📝 *待填入* |
| Calculate torque magnitude using cross product | High | Easy | 📝 *待填入* |
| Determine if vectors are perpendicular or parallel | Medium | Medium | 📝 *待填入* |
| Find the angle between two vectors using dot product | Low | Medium | 📝 *待填入* |
| Apply right-hand rule for magnetic force direction | Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Calculate, Determine, Find, Show that, State, Explain
- **CN:** 计算，确定，求出，证明，陈述，解释

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
While vector operations are primarily a mathematical tool, they are essential for analyzing data in practical experiments.
- **Work Done:** In experiments involving forces at angles (e.g., an object pulled up an incline), you must use the dot product to calculate the work done by the pulling force.
- **Torque:** In experiments on moments and equilibrium (e.g., balancing a metre rule), you use the cross product concept (often simplified to $F \times d$) to calculate torque. Understanding the perpendicular component is key.
- **Magnetic Force:** In experiments investigating the force on a current-carrying wire in a magnetic field, the cross product determines the direction of the force (Fleming's left-hand rule is a practical application of the right-hand rule for cross products).
- **Uncertainties:** When calculating a quantity that involves a dot or cross product (e.g., work done $W = Fs\cos\theta$), you must propagate uncertainties from the measured values of $F$, $s$, and $\theta$.

**中文:**
虽然向量运算主要是一种数学工具，但它们对于分析实验数据至关重要。
- **功：** 在涉及角度力的实验中（例如，物体被拉上斜面），你必须使用点积来计算拉力所做的功。
- **力矩：** 在力矩和平衡的实验中（例如，平衡一把米尺），你使用叉积概念（通常简化为 $F \times d$）来计算力矩。理解垂直分量是关键。
- **磁力：** 在调查载流导线在磁场中受力的实验中，叉积决定了力的方向（弗莱明左手定则是叉积右手定则的实际应用）。
- **不确定度：** 当计算涉及点积或叉积的量时（例如，功 $W = Fs\cos\theta$），你必须从 $F$、$s$ 和 $\theta$ 的测量值中传递不确定度。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    subgraph "Vector Operations"
        direction TB
        A[Vector Operations] --> B[Dot Product]
        A --> C[Cross Product]
    end

    subgraph "Dot Product"
        direction LR
        B --> D[Definition: A·B = |A||B|cosθ]
        B --> E[Component Form: AxBx + AyBy + AzBz]
        B --> F[Result: Scalar]
        B --> G[Application: Work Done W = F·s]
        B --> H[Application: Magnetic Flux Φ = B·A]
    end

    subgraph "Cross Product"
        direction LR
        C --> I[Definition: |A×B| = |A||B|sinθ]
        C --> J[Direction: Right-Hand Rule]
        C --> K[Result: Vector]
        C --> L[Application: Torque τ = r × F]
        C --> M[Application: Magnetic Force F = qv × B]
    end

    subgraph "Prerequisites"
        N[Scalars and Vectors]
        O[Trigonometric Functions]
    end

    subgraph "Related Topics"
        P[Simple Harmonic Motion]
        Q[Differentiation for Kinematics]
    end

    N --> A
    O --> B
    O --> C
    P -.-> L
    Q -.-> G
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Dot Product:** $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$ (scalar). **Cross Product:** $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$ (vector, direction by right-hand rule). |
| **Key Formula / 核心公式** | **Dot (Component):** $\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$. **Cross (Magnitude):** $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$. |
| **Key Graph / 核心图表** | **Dot vs. θ:** Cosine curve (max at 0°, zero at 90°). **Cross vs. θ:** Sine curve (zero at 0°, max at 90°). |
| **Exam Tip / 考试提示** | **Dot:** Use for work, flux. Zero dot product = perpendicular. **Cross:** Use for torque, magnetic force. Zero cross product = parallel. Use right-hand rule for direction. |