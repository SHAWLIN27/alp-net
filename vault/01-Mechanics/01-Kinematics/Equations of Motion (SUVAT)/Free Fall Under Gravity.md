Here is the complete bilingual leaf node for **Free Fall Under Gravity**, designed as a standalone Obsidian note and knowledge graph node.

---

# 1. Overview / 概述

**English:**
Free fall is a specific application of the [[Equations of Motion (SUVAT)]] where the only force acting on an object is gravity. This sub-topic explores how objects accelerate towards the Earth at a constant rate, known as the acceleration due to gravity ($g$). We apply the [[The Five SUVAT Equations]] with a fixed acceleration ($a = g$) to predict the motion of falling objects, ignoring air resistance. Understanding free fall is the foundation for more complex topics like [[Projectile Motion]] and is a classic exam scenario for testing your ability to choose the correct SUVAT equation.

**中文:**
自由落体是[[Equations of Motion (SUVAT)]]的一个特定应用，其中作用在物体上的唯一力是重力。本子知识点探讨物体如何以恒定速率（即重力加速度 $g$）向地球加速。我们应用[[The Five SUVAT Equations]]，并设定恒定加速度 ($a = g$)，来预测下落物体的运动，同时忽略空气阻力。理解自由落体是学习更复杂主题（如[[Projectile Motion]]）的基础，也是测试你选择正确SUVAT方程能力的经典考试场景。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Free Fall** / 自由落体 | Motion under the influence of gravity only, with no other forces (e.g., air resistance) acting. | 仅在重力作用下（无空气阻力等其他力）的运动。 |
| **Acceleration due to Gravity ($g$)** / 重力加速度 | The constant acceleration experienced by an object in free fall near the Earth's surface. | 物体在地球表面附近自由下落时所经历的恒定加速度。 |
| **Terminal Velocity** / 终端速度 | The constant maximum velocity reached by a falling object when air resistance balances the weight. (Not in free fall) | 下落物体在空气阻力与重量平衡时达到的恒定最大速度。（非自由落体） |
| **Air Resistance** / 空气阻力 | A frictional force that opposes the motion of an object through air. (Neglected in ideal free fall) | 一种阻碍物体在空气中运动的摩擦力。（在理想自由落体中忽略） |

---

# 3. Key Concepts / 关键概念

**English:**
The core concept of free fall is that **all objects, regardless of their mass, accelerate at the same rate** in a gravitational field (in the absence of air resistance). This was famously demonstrated by Galileo.

When solving free fall problems, you apply the [[The Five SUVAT Equations]] with the following key adaptations:
1.  **Acceleration ($a$):** This is always $g$, which is approximately $9.81 \text{ m/s}^2$ **downwards**. You must define a sign convention (e.g., downwards is positive).
2.  **Initial Velocity ($u$):** For an object "dropped" from rest, $u = 0$. For an object "thrown" downwards, $u$ is positive. For an object "thrown" upwards, $u$ is positive in the upward direction, but $g$ is negative.
3.  **Displacement ($s$):** This is the vertical distance from the starting point. It can be positive or negative depending on your sign convention.

**Common Pitfall:** Students often forget to define a sign convention. If you choose "upwards as positive," then $g$ must be $-9.81 \text{ m/s}^2$. If you choose "downwards as positive," then $g$ is $+9.81 \text{ m/s}^2$. Consistency is key.

**中文:**
自由落体的核心概念是：**在重力场中（忽略空气阻力），所有物体，无论质量大小，都以相同的加速度下落**。伽利略曾著名地证明了这一点。

在解决自由落体问题时，你应用[[The Five SUVAT Equations]]，并进行以下关键调整：
1.  **加速度 ($a$):** 这始终是 $g$，方向**向下**，约为 $9.81 \text{ m/s}^2$。你必须定义一个正负号约定（例如，向下为正）。
2.  **初速度 ($u$):** 对于从静止状态“释放”的物体，$u = 0$。对于“向下抛”的物体，$u$ 为正。对于“向上抛”的物体，$u$ 在向上方向为正，但 $g$ 为负。
3.  **位移 ($s$):** 这是从起点开始的垂直距离。根据你的正负号约定，它可以是正数或负数。

**常见错误：** 学生常常忘记定义正负号约定。如果你选择“向上为正”，那么 $g$ 必须是 $-9.81 \text{ m/s}^2$。如果你选择“向下为正”，那么 $g$ 是 $+9.81 \text{ m/s}^2$。一致性是关键。

---

# 4. Formulas / 公式

The primary formula for free fall is the same as the SUVAT equations, but with $a = g$.

$$ s = ut + \frac{1}{2}gt^2 $$

$$ v = u + gt $$

$$ v^2 = u^2 + 2gs $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $s$ | Vertical displacement from start | 从起点开始的垂直位移 | m |
| $u$ | Initial vertical velocity | 初始垂直速度 | m/s |
| $v$ | Final vertical velocity | 最终垂直速度 | m/s |
| $g$ | Acceleration due to gravity ($9.81 \text{ m/s}^2$) | 重力加速度 ($9.81 \text{ m/s}^2$) | m/s² |
| $t$ | Time | 时间 | s |

**Derivation / 推导:**
No new derivation is needed. These are the standard SUVAT equations with $a$ replaced by $g$.

**Conditions / 适用条件:**
- The object is in **free fall** (only gravity acts).
- **Air resistance is negligible**.
- The value of $g$ is constant (near the Earth's surface).
- Motion is vertical.

> 📷 **IMAGE PROMPT — F01: Free Fall Sign Convention Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing two scenarios for free fall. Left side: A ball is dropped from a height of 20m. An arrow points downwards labeled "g = +9.81 m/s²" and "s = +20 m". Right side: A ball is thrown upwards from the ground. An arrow points upwards labeled "u = +15 m/s" and a separate arrow points downwards labeled "g = -9.81 m/s²". Both diagrams have a clear y-axis with positive direction indicated. Use a white background with blue and red arrows.
>
> **中文描述:**
> 一个清晰、教科书风格的矢量图，展示了自由落体的两种情景。左侧：一个球从20米高处释放。一个向下的箭头标注为“g = +9.81 m/s²”和“s = +20 m”。右侧：一个球从地面向上抛出。一个向上的箭头标注为“u = +15 m/s”，另一个向下的箭头标注为“g = -9.81 m/s²”。两个图都有一个清晰的y轴，并标明了正方向。使用白色背景，蓝色和红色箭头。
>
> **Labels Required / 需要标注:**
> * g = +9.81 m/s² (downwards)
> * g = -9.81 m/s² (downwards)
> * u = 0 m/s (dropped)
> * u = +15 m/s (thrown up)
> * s = +20 m (displacement)
> * y-axis with "+" direction
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This diagram is crucial for understanding how to correctly assign signs to $u$, $s$, and $g$ in exam problems. A wrong sign convention is the most common mistake.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — F02: Feather and Hammer on the Moon**
>
> **English Prompt:**
> A photorealistic 3D render of an astronaut on the surface of the Moon. The astronaut is holding a feather in one hand and a hammer in the other, both at the same height. The astronaut is just about to drop them. In the background, the Earth is visible in the dark sky. The scene is lit by harsh sunlight from the side, creating long shadows. The surface is grey and dusty. The focus is on the two objects, showing they are at the exact same height.
>
> **中文描述:**
> 一张宇航员在月球表面的逼真3D渲染图。宇航员一只手拿着一根羽毛，另一只手拿着一把锤子，两者在同一高度。宇航员正准备释放它们。背景中，地球在黑暗的天空中可见。场景被来自侧面的强烈阳光照亮，投下长长的阴影。表面是灰色且布满灰尘的。焦点在两个物体上，显示它们处于完全相同的高度。
>
> **Labels Required / 需要标注:**
> * "Feather" (羽毛)
> * "Hammer" (锤子)
> * "Same height" (同一高度)
> * "No air resistance" (无空气阻力)
>
> **Style / 风格:** Photorealistic 3D render
>
> **Exam Relevance / 考试关联:**
> This image illustrates the key principle that in the absence of air resistance (like on the Moon), all objects fall at the same rate regardless of mass. This is a classic conceptual question in exams.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A stone is dropped from rest from the top of a cliff. It takes 3.0 seconds to hit the ground. Calculate the height of the cliff. (Take $g = 9.81 \text{ m/s}^2$)

**中文:**
一块石头从悬崖顶部由静止释放。它需要3.0秒才能落到地面。计算悬崖的高度。（取 $g = 9.81 \text{ m/s}^2$）

### Solution / 解答
1.  **List knowns (正方向: Downwards):**
    *   $u = 0 \text{ m/s}$ (dropped from rest)
    *   $t = 3.0 \text{ s}$
    *   $g = +9.81 \text{ m/s}^2$ (downwards is positive)
    *   $s = ?$

2.  **Choose the right equation:**
    We have $u$, $t$, $g$, and need $s$. The equation without $v$ is:
    $$ s = ut + \frac{1}{2}gt^2 $$

3.  **Substitute and solve:**
    $$ s = (0)(3.0) + \frac{1}{2}(9.81)(3.0)^2 $$
    $$ s = 0 + \frac{1}{2}(9.81)(9) $$
    $$ s = 4.905 \times 9 $$
    $$ s = 44.145 \text{ m} $$

### Final Answer / 最终答案
**Answer:** The height of the cliff is 44 m (to 2 significant figures). **答案:** 悬崖的高度是44米（保留两位有效数字）。

### Quick Tip / 提示
**English:** Always state your sign convention at the start of the solution. For a dropped object, $u=0$ simplifies the equation significantly.
**中文:** 在解题开始时始终说明你的正负号约定。对于释放的物体，$u=0$ 可以大大简化方程。

---

# 7. Flashcards / 闪卡

**Q (EN):** What is the value of acceleration due to gravity ($g$) near the Earth's surface?
**Q (CN):** 地球表面附近的重力加速度 ($g$) 的值是多少？
**A (EN):** $9.81 \text{ m/s}^2$ downwards.
**A (CN):** 向下 $9.81 \text{ m/s}^2$。

---

**Q (EN):** In free fall, if air resistance is ignored, which object falls faster: a 1 kg ball or a 10 kg ball?
**Q (CN):** 在自由落体中，如果忽略空气阻力，1公斤的球和10公斤的球哪个下落得更快？
**A (EN):)** They fall at the same rate. All objects accelerate at $g$ regardless of mass.
**A (CN):** 它们下落的速度相同。所有物体无论质量大小，都以 $g$ 加速。

---

**Q (EN):** What is the initial velocity ($u$) of an object that is "dropped" from rest?
**Q (CN):** 一个从静止状态“释放”的物体的初速度 ($u$) 是多少？
**A (EN):** $u = 0 \text{ m/s}$.
**A (CN):** $u = 0 \text{ m/s}$。

---

**Q (EN):** If you choose "upwards as positive," what sign should you use for $g$?
**Q (CN):** 如果你选择“向上为正”，$g$ 应该使用什么符号？
**A (EN):** Negative ($-9.81 \text{ m/s}^2$), because gravity acts downwards.
**A (CN):** 负号 ($-9.81 \text{ m/s}^2$)，因为重力方向向下。

---

**Q (EN):** Which SUVAT equation is best to find displacement ($s$) when you know $u$, $t$, and $g$?
**Q (CN):** 当你知道 $u$、$t$ 和 $g$ 时，哪个SUVAT方程最适合求位移 ($s$)？
**A (EN):** $s = ut + \frac{1}{2}gt^2$.
**A (CN):** $s = ut + \frac{1}{2}gt^2$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Free Fall Under Gravity
  cn: 重力作用下的自由落体
parent_topic: Equations of Motion (SUVAT)
parent_hub: "[[Equations of Motion (SUVAT)]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[The Five SUVAT Equations]]"
  - "[[Choosing the Right Equation]]"
  - "[[Two-Stage Motion Problems]]"
  - "[[Displacement, Velocity and Acceleration]]"
language: bilingual_en_cn