Here is the complete bilingual leaf node for **Equilibrium Conditions**, designed as a standalone Obsidian note and knowledge graph leaf node.

---

# 1. Overview / 概述

**English:**
This sub-topic explores the conditions under which an object is in **equilibrium** — meaning it is either at rest or moving with constant velocity. In the context of [[Free-body Diagrams]], equilibrium is the state where the net force (and net moment) acting on a body is zero. This is a foundational concept for applying [[Newton's Laws of Motion]], specifically Newton's First Law. Understanding equilibrium allows you to solve for unknown forces (e.g., tension, reaction forces) in static systems, such as a book on a table or a hanging sign. This leaf node focuses on the **translational equilibrium** condition (forces), while the rotational aspect is covered in [[Moments and Torque]].

**中文:**
本子知识点探讨物体处于**平衡**状态的条件——即物体保持静止或匀速直线运动。在 [[Free-body Diagrams]] 的背景下，平衡是指作用在物体上的合力（以及合力矩）为零的状态。这是应用 [[Newton's Laws of Motion]]，特别是牛顿第一定律的基础概念。理解平衡可以让你求解静态系统中的未知力（例如张力、支持力），比如桌子上的书或悬挂的招牌。本叶节点专注于**平动平衡**条件（力），而转动平衡方面则在 [[Moments and Torque]] 中讨论。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Equilibrium** / 平衡 | A state where the net force (vector sum of all forces) acting on an object is zero, resulting in zero acceleration. | 物体所受合力（所有力的矢量和）为零的状态，导致加速度为零。 |
| **Translational Equilibrium** / 平动平衡 | The condition where the sum of all forces in any direction is zero, i.e., $\sum F_x = 0$ and $\sum F_y = 0$. | 在任何方向上所有力的总和为零的条件，即 $\sum F_x = 0$ 和 $\sum F_y = 0$。 |
| **Net Force** / 合力 | The single force that represents the vector sum of all forces acting on an object. | 代表作用在物体上所有力的矢量和的单一力。 |
| **Static Equilibrium** / 静态平衡 | A specific type of equilibrium where the object is at rest (velocity = 0). | 物体处于静止状态（速度 = 0）的一种特定平衡类型。 |
| **Dynamic Equilibrium** / 动态平衡 | A specific type of equilibrium where the object moves with constant velocity (acceleration = 0). | 物体以恒定速度运动（加速度 = 0）的一种特定平衡类型。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core idea of equilibrium is that **forces balance out**. When you draw a [[Free-body Diagrams|Free-body Diagram]] for an object in equilibrium, the arrows representing forces must form a closed polygon when placed head-to-tail. This is the graphical representation of the vector sum being zero.

**Step-by-step reasoning for solving equilibrium problems:**
1.  **Identify the object** in equilibrium.
2.  **Draw a Free-body Diagram** showing all forces acting *on* the object. Remember to include [[Types of Force|Weight]], [[Types of Force|Normal Reaction]], [[Types of Force|Tension]], [[Types of Force|Friction]], etc.
3.  **Choose a coordinate system** (usually horizontal and vertical, or parallel and perpendicular to an inclined plane).
4.  **Resolve forces** into components along your chosen axes. This is crucial for forces at angles, as detailed in [[Resolving Forces on Inclined Planes]].
5.  **Apply the equilibrium conditions:**
    *   $\sum F_x = 0$ (Sum of forces in the x-direction is zero)
    *   $\sum F_y = 0$ (Sum of forces in the y-direction is zero)
6.  **Solve the resulting equations** for the unknown quantities.

**Common Pitfalls:**
*   **Forgetting to resolve forces:** A force at an angle contributes to both horizontal and vertical equilibrium.
*   **Incorrect sign convention:** Be consistent with your chosen positive direction (e.g., up is positive, right is positive).
*   **Confusing equilibrium with Newton's Second Law:** Equilibrium is a *special case* of $F=ma$ where $a=0$. If $a \neq 0$, the object is not in equilibrium.

**中文:**
平衡的核心思想是**力相互抵消**。当你为处于平衡状态的物体绘制 [[Free-body Diagrams|Free-body Diagram]] 时，代表力的箭头在首尾相连时必须形成一个封闭的多边形。这是矢量和为零的图形表示。

**解决平衡问题的分步推理：**
1.  **确定**处于平衡状态的**物体**。
2.  **绘制 Free-body Diagram**，显示作用在物体上的所有力。记得包括 [[Types of Force|Weight]]、[[Types of Force|Normal Reaction]]、[[Types of Force|Tension]]、[[Types of Force|Friction]] 等。
3.  **选择坐标系**（通常是水平和垂直，或平行和垂直于斜面）。
4.  **将力分解**到所选坐标轴的分量上。这对于有角度的力至关重要，详见 [[Resolving Forces on Inclined Planes]]。
5.  **应用平衡条件：**
    *   $\sum F_x = 0$（x方向上的合力为零）
    *   $\sum F_y = 0$（y方向上的合力为零）
6.  **解方程**求未知量。

**常见错误：**
*   **忘记分解力：** 有角度的力对水平和垂直平衡都有贡献。
*   **符号约定错误：** 对你选择的正方向保持一致（例如，向上为正，向右为正）。
*   **混淆平衡与牛顿第二定律：** 平衡是 $F=ma$ 的一个*特例*，其中 $a=0$。如果 $a \neq 0$，物体不处于平衡状态。

---

# 4. Formulas / 公式

The fundamental condition for translational equilibrium:

$$ \sum \vec{F} = 0 $$

This vector equation is equivalent to two scalar equations (in 2D):

$$ \sum F_x = 0 $$
$$ \sum F_y = 0 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\sum \vec{F}$ | Vector sum of all forces | 所有力的矢量和 | N (Newtons) |
| $\sum F_x$ | Sum of all force components in the x-direction | x方向上所有力分量的和 | N |
| $\sum F_y$ | Sum of all force components in the y-direction | y方向上所有力分量的和 | N |

**Derivation / 推导:**
From [[Newton's Laws of Motion|Newton's First Law]], an object will remain at rest or in uniform motion unless acted upon by a net external force. Therefore, if the velocity is constant ($a=0$), the net force must be zero. From Newton's Second Law ($F=ma$), if $a=0$, then $F=0$.

**Conditions / 适用条件:**
*   The object must be in **translational equilibrium** (no linear acceleration).
*   The forces must be **coplanar** (acting in the same plane) for the 2D equations to be sufficient.
*   For **static equilibrium**, the object must also be in rotational equilibrium (no net moment), which is covered in [[Moments and Torque]].

> 📷 **IMAGE PROMPT — EQ-01: Closed Force Triangle for Equilibrium**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing three forces (Tension T, Weight W, and Normal Reaction R) acting on a point mass hanging from two strings. The forces are arranged head-to-tail to form a closed triangle, with arrows clearly showing the direction. The diagram should have labels for each force and a note: "Closed Polygon = Equilibrium". Use a white background with black and blue lines.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示三个力（张力 T、重量 W 和支持力 R）作用在一个由两根绳子悬挂的质点上。这些力首尾相连排列成一个封闭的三角形，箭头清晰显示方向。图表应标注每个力，并附注："封闭多边形 = 平衡"。使用白色背景，黑色和蓝色线条。
>
> **Labels Required / 需要标注:**
> *   Tension (T)
> *   Weight (W)
> *   Normal Reaction (R)
> *   "Closed Polygon = Equilibrium"
>
> **Style / 风格:** Textbook vector / 2D diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is crucial for understanding the vector nature of equilibrium. Many exam questions ask students to draw or interpret such a force triangle to solve for unknown forces.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — EQ-02: Free-body Diagram of a Book on a Table**
>
> **English Prompt:**
> A simple, clear 2D diagram showing a book resting on a horizontal table. The book is represented as a rectangle. Two arrows originate from the center of the book: a downward arrow labeled "Weight (W)" and an upward arrow of equal length labeled "Normal Reaction (R)". The lengths of the arrows should be identical to visually show equilibrium. The background is white, and the diagram is in a clean, vector style.
>
> **中文描述:**
> 一个简单清晰的2D图表，显示一本书静止在水平桌子上。书用一个矩形表示。从书的中心发出两个箭头：一个向下的箭头标注为"重量 (W)"，一个长度相等的向上箭头标注为"支持力 (R)"。箭头的长度应相同，以直观显示平衡。背景为白色，图表为干净的矢量风格。
>
> **Labels Required / 需要标注:**
> *   Weight (W)
> *   Normal Reaction (R)
> *   "Book at rest"
>
> **Style / 风格:** Textbook vector / 2D diagram
>
> **Exam Relevance / 考试关联:**
> This is the most basic example of equilibrium. Students must be able to identify that the normal reaction force balances the weight, resulting in a net force of zero.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A 5.0 kg sign is suspended by two light, inextensible strings, as shown in the diagram. String A makes an angle of $30^\circ$ with the horizontal, and String B makes an angle of $60^\circ$ with the horizontal. The sign is in equilibrium. Calculate the tension in String A ($T_A$) and String B ($T_B$). (Take $g = 9.81 \text{ m/s}^2$)

**中文:**
一个 5.0 kg 的招牌由两根轻质、不可伸长的绳子悬挂，如图所示。绳子 A 与水平方向成 $30^\circ$ 角，绳子 B 与水平方向成 $60^\circ$ 角。招牌处于平衡状态。计算绳子 A 的张力 ($T_A$) 和绳子 B 的张力 ($T_B$)。（取 $g = 9.81 \text{ m/s}^2$）

### Solution / 解答
**Step 1: Draw a Free-body Diagram**
The forces acting on the sign are:
*   Weight ($W = mg$) acting downwards.
*   Tension from String A ($T_A$) at $30^\circ$ above the horizontal.
*   Tension from String B ($T_B$) at $60^\circ$ above the horizontal.

**Step 2: Resolve Forces**
Resolve $T_A$ and $T_B$ into horizontal ($x$) and vertical ($y$) components.
*   $T_{A,x} = T_A \cos(30^\circ)$ (to the left)
*   $T_{A,y} = T_A \sin(30^\circ)$ (upwards)
*   $T_{B,x} = T_B \cos(60^\circ)$ (to the right)
*   $T_{B,y} = T_B \sin(60^\circ)$ (upwards)
*   $W = mg = (5.0)(9.81) = 49.05 \text{ N}$ (downwards)

**Step 3: Apply Equilibrium Conditions**
Let right be positive $x$, and up be positive $y$.

**Horizontal Equilibrium ($\sum F_x = 0$):**
$$ -T_A \cos(30^\circ) + T_B \cos(60^\circ) = 0 $$
$$ T_B \cos(60^\circ) = T_A \cos(30^\circ) $$
$$ T_B (0.5) = T_A (0.866) $$
$$ T_B = 1.732 T_A \quad \text{(Equation 1)} $$

**Vertical Equilibrium ($\sum F_y = 0$):**
$$ T_A \sin(30^\circ) + T_B \sin(60^\circ) - W = 0 $$
$$ T_A (0.5) + T_B (0.866) = 49.05 \quad \text{(Equation 2)} $$

**Step 4: Solve the Equations**
Substitute Equation 1 into Equation 2:
$$ 0.5 T_A + 0.866 (1.732 T_A) = 49.05 $$
$$ 0.5 T_A + 1.5 T_A = 49.05 $$
$$ 2.0 T_A = 49.05 $$
$$ T_A = 24.525 \text{ N} $$

Now, find $T_B$:
$$ T_B = 1.732 \times 24.525 = 42.48 \text{ N} $$

### Final Answer / 最终答案
**Answer:** $T_A = 24.5 \text{ N}$, $T_B = 42.5 \text{ N}$ (to 3 significant figures)
**答案:** $T_A = 24.5 \text{ N}$, $T_B = 42.5 \text{ N}$（保留三位有效数字）

### Quick Tip / 提示
**English:** Always start by drawing a clear Free-body Diagram. If you have two unknowns, you will need two equations (usually from horizontal and vertical equilibrium). If the system is symmetric, the tensions will be equal, simplifying the calculation.
**中文:** 始终从绘制清晰的 Free-body Diagram 开始。如果有两个未知数，则需要两个方程（通常来自水平和垂直平衡）。如果系统是对称的，张力将相等，从而简化计算。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What are the two conditions for an object to be in translational equilibrium?
Q (CN): 物体处于平动平衡的两个条件是什么？
A (EN): The sum of all forces in the x-direction is zero ($\sum F_x = 0$), and the sum of all forces in the y-direction is zero ($\sum F_y = 0$).
A (CN): x方向上所有力的总和为零 ($\sum F_x = 0$)，且y方向上所有力的总和为零 ($\sum F_y = 0$)。

**Flashcard 2:**
Q (EN): What is the difference between static and dynamic equilibrium?
Q (CN): 静态平衡和动态平衡有什么区别？
A (EN): Static equilibrium means the object is at rest (v=0). Dynamic equilibrium means the object is moving with constant velocity (a=0).
A (CN): 静态平衡意味着物体静止（v=0）。动态平衡意味着物体以恒定速度运动（a=0）。

**Flashcard 3:**
Q (EN): If an object is in equilibrium, what can you say about its acceleration?
Q (CN): 如果一个物体处于平衡状态，关于它的加速度你能得出什么结论？
A (EN): Its acceleration is zero.
A (CN): 它的加速度为零。

**Flashcard 4:**
Q (EN): A book is resting on a table. Name the two forces acting on it that are in equilibrium.
Q (CN): 一本书静止在桌子上。说出作用在它上面并处于平衡的两个力。
A (EN): Weight (downwards) and Normal Reaction (upwards).
A (CN): 重量（向下）和支持力（向上）。

**Flashcard 5:**
Q (EN): What is the graphical representation of an object in equilibrium?
Q (CN): 物体处于平衡状态的图形表示是什么？
A (EN): When the force vectors are placed head-to-tail, they form a closed polygon.
A (CN): 当力矢量首尾相连时，它们形成一个封闭的多边形。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Equilibrium Conditions
  cn: 平衡条件
parent_topic: Free-body Diagrams
parent_hub: "[[Free-body Diagrams]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Drawing Free-body Diagrams]]"
  - "[[Resolving Forces on Inclined Planes]]"
  - "[[Types of Force]]"
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn