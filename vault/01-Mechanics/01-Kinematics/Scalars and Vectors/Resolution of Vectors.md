# 1. Overview / 概述

**English:**
Resolution of vectors is the process of splitting a single vector into two perpendicular components, typically horizontal and vertical. This is one of the most powerful techniques in A-Level Physics because it allows us to analyse forces, velocities, and other vector quantities in two dimensions using simple trigonometry. Instead of dealing with a single vector at an angle, we break it down into two independent components that act at right angles to each other. This technique is essential for solving problems in [[Projectile Motion]], [[Types of Force]], and [[Displacement, Velocity and Acceleration]]. It is the inverse operation of [[Vector Addition and Subtraction]] — instead of combining vectors, we are separating them.

**中文:**
矢量的分解是将一个矢量分解为两个互相垂直的分量（通常是水平分量和垂直分量）的过程。这是A-Level物理中最强大的技巧之一，因为它使我们能够使用简单的三角学在二维空间中分析力、速度和其他矢量量。我们不是处理一个倾斜的矢量，而是将其分解为两个相互垂直的独立分量。这项技术对于解决[[Projectile Motion]]、[[Types of Force]]和[[Displacement, Velocity and Acceleration]]中的问题至关重要。它是[[Vector Addition and Subtraction]]的逆运算——不是将矢量合并，而是将它们分开。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Resolution of Vectors** / 矢量的分解 | The process of splitting a single vector into two perpendicular components, usually horizontal and vertical, whose vector sum equals the original vector. | 将一个矢量分解为两个互相垂直的分量（通常是水平和垂直分量），这两个分量的矢量和等于原矢量。 |
| **Component** / 分量 | One of the perpendicular parts into which a vector is resolved. | 矢量被分解后得到的其中一个垂直部分。 |
| **Horizontal Component** / 水平分量 | The component of a vector that acts parallel to the horizontal axis (x-direction). | 矢量中平行于水平轴（x方向）的分量。 |
| **Vertical Component** / 垂直分量 | The component of a vector that acts parallel to the vertical axis (y-direction). | 矢量中平行于垂直轴（y方向）的分量。 |
| **Angle of Resolution** / 分解角度 | The angle between the original vector and one of its components, used to determine the magnitudes of the components. | 原矢量与其一个分量之间的夹角，用于确定分量的大小。 |

---

# 3. Key Concepts / 关键概念

**English:**
The resolution of a vector relies on the fundamental principle that any vector can be represented as the sum of two perpendicular vectors. This is based on the geometry of a right-angled triangle.

Consider a vector $\vec{F}$ of magnitude $F$ making an angle $\theta$ with the horizontal axis. The horizontal component $F_x$ and vertical component $F_y$ are given by:

$$F_x = F \cos \theta$$
$$F_y = F \sin \theta$$

**Step-by-step reasoning:**
1. Identify the vector and its magnitude $F$.
2. Determine the angle $\theta$ the vector makes with the horizontal (or a chosen reference axis).
3. The adjacent side to $\theta$ gives the horizontal component: $F_x = F \cos \theta$.
4. The opposite side to $\theta$ gives the vertical component: $F_y = F \sin \theta$.

**Physical interpretation:**
- The components are independent — changing one component does not affect the other.
- The original vector is the hypotenuse of the right-angled triangle formed by its components.
- This is the reverse of [[Vector Addition and Subtraction]] using the parallelogram law.

**Common pitfalls:**
- **Wrong angle:** Always check which angle you are using. If the angle is measured from the vertical, swap $\sin$ and $\cos$.
- **Sign convention:** Components can be negative depending on direction (e.g., leftward or downward).
- **Forgetting the vector nature:** Components are vectors, not scalars — they have direction.

**中文:**
矢量的分解基于一个基本原理：任何矢量都可以表示为两个垂直矢量的和。这是基于直角三角形的几何关系。

考虑一个大小为 $F$、与水平方向夹角为 $\theta$ 的矢量 $\vec{F}$。水平分量 $F_x$ 和垂直分量 $F_y$ 由下式给出：

$$F_x = F \cos \theta$$
$$F_y = F \sin \theta$$

**逐步推理：**
1. 确定矢量及其大小 $F$。
2. 确定矢量与水平方向（或选定的参考轴）的夹角 $\theta$。
3. $\theta$ 的邻边给出水平分量：$F_x = F \cos \theta$。
4. $\theta$ 的对边给出垂直分量：$F_y = F \sin \theta$。

**物理意义：**
- 分量是独立的——改变一个分量不会影响另一个分量。
- 原矢量是其分量构成的直角三角形的斜边。
- 这是使用平行四边形法则进行[[Vector Addition and Subtraction]]的逆过程。

**常见错误：**
- **角度错误：** 始终检查使用的角度。如果角度是从垂直方向测量的，则交换 $\sin$ 和 $\cos$。
- **符号约定：** 分量可能为负值，具体取决于方向（例如，向左或向下）。
- **忘记矢量的性质：** 分量是矢量，不是标量——它们有方向。

> 📷 **IMAGE PROMPT — VEC-RES-01: Vector Resolution Triangle**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a single vector F (red arrow) at angle θ above the horizontal. The vector is the hypotenuse of a right-angled triangle. The horizontal component Fx (blue arrow) runs along the base, and the vertical component Fy (green arrow) runs along the height. All three vectors form a closed right triangle. Labels: "F", "Fx = F cos θ", "Fy = F sin θ", "θ". White background, professional physics diagram style, clear arrowheads, dashed construction lines forming the triangle.
>
> **中文描述:**
> 一个清晰的教科书式矢量图，显示一个矢量 F（红色箭头）与水平方向成 θ 角。该矢量是直角三角形的斜边。水平分量 Fx（蓝色箭头）沿底边，垂直分量 Fy（绿色箭头）沿高。三个矢量构成一个封闭的直角三角形。标签："F"、"Fx = F cos θ"、"Fy = F sin θ"、"θ"。白色背景，专业物理图风格，清晰的箭头，虚线构成三角形。
>
> **Labels Required / 需要标注:**
> * F (original vector)
> * Fx = F cos θ (horizontal component)
> * Fy = F sin θ (vertical component)
> * θ (angle with horizontal)
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is the foundation for all vector resolution problems in A-Level Physics exams.

---

# 4. Formulas / 公式

## Primary Formula

$$F_x = F \cos \theta \quad \text{and} \quad F_y = F \sin \theta$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F$ | Magnitude of the original vector | 原矢量的大小 | N, m/s, etc. |
| $F_x$ | Horizontal component | 水平分量 | Same as $F$ |
| $F_y$ | Vertical component | 垂直分量 | Same as $F$ |
| $\theta$ | Angle between vector and horizontal | 矢量与水平方向的夹角 | degrees (°) or radians (rad) |

## Alternative Form (Angle from Vertical)

If the angle $\phi$ is measured from the vertical:

$$F_x = F \sin \phi \quad \text{and} \quad F_y = F \cos \phi$$

## Inverse Relationship (Recombination)

To find the original vector from its components:

$$F = \sqrt{F_x^2 + F_y^2} \quad \text{and} \quad \theta = \tan^{-1}\left(\frac{F_y}{F_x}\right)$$

**Derivation / 推导:**
From the right-angled triangle:
- $\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{F_x}{F} \Rightarrow F_x = F \cos \theta$
- $\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{F_y}{F} \Rightarrow F_y = F \sin \theta$

**Conditions / 适用条件:**
- The vector must be resolved into perpendicular components (usually horizontal and vertical).
- The angle must be measured consistently from the chosen reference axis.
- This method works for any vector quantity: force, velocity, displacement, acceleration, etc.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — VEC-RES-02: Real-World Vector Resolution**
>
> **English Prompt:**
> A 3D-rendered physics illustration showing a person pulling a box with a rope at an angle of 30° above the horizontal. The rope force vector F (red arrow) is shown at 30° from horizontal. Two dashed arrows show the resolution: a horizontal component Fx (blue arrow) pulling the box forward, and a vertical component Fy (green arrow) lifting the box slightly. The box is on a flat surface with friction. Labels: "F", "Fx = F cos 30°", "Fy = F sin 30°", "θ = 30°". Warm lighting, realistic textures, educational diagram style with clear annotations.
>
> **中文描述:**
> 一个3D渲染的物理插图，显示一个人用绳子以与水平方向成30°角拉一个箱子。绳子拉力矢量 F（红色箭头）显示为与水平方向成30°角。两个虚线箭头显示分解：水平分量 Fx（蓝色箭头）向前拉箱子，垂直分量 Fy（绿色箭头）稍微抬起箱子。箱子在带有摩擦力的平坦表面上。标签："F"、"Fx = F cos 30°"、"Fy = F sin 30°"、"θ = 30°"。暖色照明，逼真纹理，带有清晰标注的教育图风格。
>
> **Labels Required / 需要标注:**
> * F (tension in rope)
> * Fx = F cos 30° (horizontal component)
> * Fy = F sin 30° (vertical component)
> * θ = 30° (angle)
>
> **Style / 风格:** 3D rendered educational illustration
>
> **Exam Relevance / 考试关联:**
> This real-world scenario is a common exam question type — resolving forces on inclined ropes.

---

# 6. Worked Example / 典型例题

### Example 1: Basic Resolution

### Question / 题目
**English:**
A force of 50 N acts at an angle of 40° above the horizontal. Calculate the horizontal and vertical components of this force.

**中文:**
一个大小为50 N的力与水平方向成40°角。计算该力的水平和垂直分量。

### Solution / 解答

**Step 1:** Identify the given values.
- $F = 50 \text{ N}$
- $\theta = 40^\circ$

**Step 2:** Calculate the horizontal component.
$$F_x = F \cos \theta = 50 \times \cos 40^\circ$$
$$F_x = 50 \times 0.7660 = 38.3 \text{ N}$$

**Step 3:** Calculate the vertical component.
$$F_y = F \sin \theta = 50 \times \sin 40^\circ$$
$$F_y = 50 \times 0.6428 = 32.1 \text{ N}$$

### Final Answer / 最终答案
**Answer:** Horizontal component = 38.3 N, Vertical component = 32.1 N
**答案:** 水平分量 = 38.3 N，垂直分量 = 32.1 N

### Quick Tip / 提示
Always check if your calculator is in degree mode! A common mistake is using radian mode, which gives completely wrong answers.

---

### Example 2: Recombination (Inverse)

### Question / 题目
**English:**
A velocity vector has a horizontal component of 12 m/s and a vertical component of 5.0 m/s. Calculate the magnitude and direction of the original velocity.

**中文:**
一个速度矢量的水平分量为12 m/s，垂直分量为5.0 m/s。计算原速度的大小和方向。

### Solution / 解答

**Step 1:** Calculate the magnitude using Pythagoras.
$$v = \sqrt{v_x^2 + v_y^2} = \sqrt{12^2 + 5.0^2}$$
$$v = \sqrt{144 + 25} = \sqrt{169} = 13 \text{ m/s}$$

**Step 2:** Calculate the direction.
$$\theta = \tan^{-1}\left(\frac{v_y}{v_x}\right) = \tan^{-1}\left(\frac{5.0}{12}\right)$$
$$\theta = \tan^{-1}(0.4167) = 22.6^\circ \text{ above the horizontal}$$

### Final Answer / 最终答案
**Answer:** Magnitude = 13 m/s, Direction = 22.6° above the horizontal
**答案:** 大小 = 13 m/s，方向 = 与水平方向成22.6°

### Quick Tip / 提示
Remember: $\tan \theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{F_y}{F_x}$. Always state the direction clearly (e.g., "above the horizontal" or "below the horizontal").

---

# 7. Flashcards / 闪卡

**Q (EN):** What is the formula for the horizontal component of a vector F at angle θ above the horizontal?
**Q (CN):** 与水平方向成θ角的矢量F的水平分量公式是什么？
**A (EN):** $F_x = F \cos \theta$
**A (CN):** $F_x = F \cos \theta$

---

**Q (EN):** How do you find the magnitude of the original vector from its components?
**Q (CN):** 如何从分量求原矢量的大小？
**A (EN):** $F = \sqrt{F_x^2 + F_y^2}$ (Pythagoras' theorem)
**A (CN):** $F = \sqrt{F_x^2 + F_y^2}$（勾股定理）

---

**Q (EN):** What is the key difference between resolving a vector and adding vectors?
**Q (CN):** 矢量分解和矢量相加的关键区别是什么？
**A (EN):)** Resolution splits one vector into two perpendicular components; addition combines two or more vectors into one resultant.
**A (CN):** 分解是将一个矢量拆分为两个垂直分量；相加是将两个或多个矢量合并为一个合矢量。

---

**Q (EN):** If a force of 100 N acts at 30° above horizontal, what is the vertical component?
**Q (CN):** 如果一个100 N的力与水平方向成30°角，垂直分量是多少？
**A (EN):** $F_y = 100 \sin 30^\circ = 100 \times 0.5 = 50 \text{ N}$
**A (CN):** $F_y = 100 \sin 30^\circ = 100 \times 0.5 = 50 \text{ N}$

---

**Q (EN):** What is the relationship between vector resolution and right-angled triangles?
**Q (CN):** 矢量分解和直角三角形之间有什么关系？
**A (EN):** The original vector is the hypotenuse, and the components are the adjacent and opposite sides of a right-angled triangle.
**A (CN):** 原矢量是斜边，分量是直角三角形的邻边和对边。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Resolution of Vectors
  cn: 矢量的分解
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
  - "[[Vector Addition and Subtraction]]"
  - "[[Displacement, Velocity and Acceleration]]"
  - "[[Projectile Motion]]"
  - "[[Types of Force]]"
language: bilingual_en_cn