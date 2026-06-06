Here is the complete bilingual leaf node for **Horizontal and Vertical Components** within the [[Projectile Motion]] topic.

---

# 1. Overview / 概述

**English:**
This sub-topic is the **foundational principle** of all [[Projectile Motion]] analysis. It explains how to treat a single curved trajectory as two independent, straight-line motions: one horizontal (constant velocity) and one vertical (constant acceleration due to gravity). By resolving the initial velocity into its [[Scalars and Vectors|vector components]], we can apply the [[Equations of Motion (SUVAT)]] separately to each axis. This decomposition is the key to solving for [[Time of Flight and Range]], [[Maximum Height]], and interpreting [[Projectile Motion Graphs]].

**中文:**
本子知识点是分析所有[[Projectile Motion]]的**基础原理**。它解释了如何将一个弯曲的轨迹分解为两个独立的直线运动：水平方向（匀速运动）和垂直方向（匀加速运动，加速度为重力加速度）。通过将初速度分解为[[Scalars and Vectors|矢量分量]]，我们可以分别在两个轴上应用[[Equations of Motion (SUVAT)]]。这种分解是求解[[Time of Flight and Range]]、[[Maximum Height]]以及解读[[Projectile Motion Graphs]]的关键。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Resolution of Velocity** / 速度分解 | The process of splitting a single velocity vector into two perpendicular components (usually horizontal and vertical) using trigonometry. | 将一个速度矢量分解为两个互相垂直的分量（通常为水平和垂直分量）的三角函数过程。 |
| **Horizontal Component ($u_x$)** / 水平分量 | The component of initial velocity acting parallel to the ground; it remains constant throughout the flight (ignoring air resistance). | 初速度中平行于地面的分量；在整个飞行过程中保持不变（忽略空气阻力）。 |
| **Vertical Component ($u_y$)** / 垂直分量 | The component of initial velocity acting perpendicular to the ground; it changes uniformly due to gravitational acceleration ($g$). | 初速度中垂直于地面的分量；由于重力加速度 ($g$) 而均匀变化。 |
| **Independence of Motion** / 运动的独立性 | The principle that horizontal and vertical motions do not affect each other; they can be analyzed separately. | 水平运动和垂直运动互不影响的原则；它们可以分开分析。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core idea is that a projectile’s motion is **two-dimensional** but can be treated as two **one-dimensional** problems.

1.  **The Initial Velocity Vector ($u$):** A projectile is launched with speed $u$ at an angle $\theta$ to the horizontal.
2.  **Trigonometric Resolution:**
    *   **Horizontal:** $u_x = u \cos \theta$ (Adjacent to the angle).
    *   **Vertical:** $u_y = u \sin \theta$ (Opposite to the angle).
3.  **Why Separate?**
    *   **Horizontal (x-axis):** No force acts (ignoring air resistance). Therefore, acceleration $a_x = 0$. This means $u_x$ is **constant**.
    *   **Vertical (y-axis):** Gravity acts downwards. Therefore, acceleration $a_y = -g$ (usually $-9.81 \text{ m/s}^2$). This means $u_y$ changes over time.
4.  **Applying [[Equations of Motion (SUVAT)]]:** You must use the correct component for the correct axis.
    *   For horizontal motion: $s_x = u_x t$ (since $a=0$).
    *   For vertical motion: $v_y = u_y + a_y t$, $s_y = u_y t + \frac{1}{2} a_y t^2$, $v_y^2 = u_y^2 + 2 a_y s_y$.

**Common Pitfall:** Students often mix up the components (e.g., using $u \sin \theta$ for the horizontal distance). Always draw a right-angled triangle with the launch angle to check which component is $\cos$ and which is $\sin$.

**中文:**
核心思想是抛体运动是**二维**的，但可以当作两个**一维**问题来处理。

1.  **初速度矢量 ($u$):** 抛体以速率 $u$ 和水平方向夹角 $\theta$ 被抛出。
2.  **三角函数分解:**
    *   **水平方向:** $u_x = u \cos \theta$ (角的邻边)。
    *   **垂直方向:** $u_y = u \sin \theta$ (角的对边)。
3.  **为什么要分开?**
    *   **水平方向 (x轴):** 没有力作用（忽略空气阻力）。因此，加速度 $a_x = 0$。这意味着 $u_x$ 是**恒定**的。
    *   **垂直方向 (y轴):** 重力向下作用。因此，加速度 $a_y = -g$ (通常为 $-9.81 \text{ m/s}^2$)。这意味着 $u_y$ 随时间变化。
4.  **应用[[Equations of Motion (SUVAT)]]:** 必须为正确的轴使用正确的分量。
    *   对于水平运动: $s_x = u_x t$ (因为 $a=0$)。
    *   对于垂直运动: $v_y = u_y + a_y t$, $s_y = u_y t + \frac{1}{2} a_y t^2$, $v_y^2 = u_y^2 + 2 a_y s_y$。

**常见错误:** 学生经常混淆分量（例如，用 $u \sin \theta$ 来计算水平距离）。始终画出包含发射角的直角三角形来检查哪个分量是 $\cos$，哪个是 $\sin$。

> 📷 **IMAGE PROMPT — VEC-01: Velocity Vector Resolution Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram. A projectile is launched from the origin (0,0) at an angle θ above the horizontal. A single arrow representing the initial velocity vector 'u' points up and to the right. From the tip of this arrow, dashed lines drop down to the x-axis and back to the y-axis, forming a right-angled triangle. The horizontal arrow is labeled 'u cos θ' and the vertical arrow is labeled 'u sin θ'. The angle θ is clearly marked between the vector 'u' and the horizontal axis. Use a white background, black lines, and blue arrows for the components.
>
> **中文描述:**
> 一个干净的教科书式矢量图。一个抛体从原点 (0,0) 以与水平方向夹角 θ 发射。一个代表初速度矢量 'u' 的箭头指向右上方。从这个箭头的顶端，虚线向下延伸到 x 轴并折回 y 轴，形成一个直角三角形。水平箭头标记为 'u cos θ'，垂直箭头标记为 'u sin θ'。角度 θ 清晰地标在矢量 'u' 和水平轴之间。使用白色背景、黑色线条和蓝色箭头表示分量。
>
> **Labels Required / 需要标注:**
> *   Initial Velocity (u) / 初速度 (u)
> *   Horizontal Component (u cos θ) / 水平分量 (u cos θ)
> *   Vertical Component (u sin θ) / 垂直分量 (u sin θ)
> *   Launch Angle (θ) / 发射角 (θ)
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This is the first step in almost every projectile motion calculation. Understanding this diagram is essential for solving range, time of flight, and maximum height problems.

---

# 4. Formulas / 公式

The two key formulas for resolving the initial velocity vector:

$$ u_x = u \cos \theta $$
$$ u_y = u \sin \theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $u$ | Initial launch speed | 初始发射速率 | $\text{m s}^{-1}$ |
| $\theta$ | Launch angle (from horizontal) | 发射角（与水平方向夹角） | $^\circ$ or rad |
| $u_x$ | Horizontal component of initial velocity | 初速度的水平分量 | $\text{m s}^{-1}$ |
| $u_y$ | Vertical component of initial velocity | 初速度的垂直分量 | $\text{m s}^{-1}$ |

**Derivation / 推导:**
Given a right-angled triangle where the hypotenuse is $u$, the adjacent side to angle $\theta$ is $u_x$, and the opposite side is $u_y$.
*   $\cos \theta = \frac{\text{Adjacent}}{\text{Hypotenuse}} = \frac{u_x}{u} \implies u_x = u \cos \theta$
*   $\sin \theta = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{u_y}{u} \implies u_y = u \sin \theta$

**Conditions / 适用条件:**
*   The angle $\theta$ must be measured from the **horizontal**.
*   This resolution is valid for any initial velocity vector, regardless of the subsequent motion.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — PROJ-02: Independence of Motion Demonstration**
>
> **English Prompt:**
> A split-screen 3D render showing two balls released simultaneously from the same height. The left ball is dropped straight down (pure vertical motion). The right ball is launched horizontally (pure horizontal motion). A grid of vertical and horizontal lines is behind them. A stroboscopic effect shows their positions at equal time intervals. The key visual point is that both balls are at the exact same vertical height at each flash, proving that the horizontal motion of the right ball does not affect its vertical fall. The left ball's path is a straight vertical line. The right ball's path is a curved parabola. Labels: "Ball A (Dropped)" and "Ball B (Launched Horizontally)". Use a clean, educational style with a dark background and bright neon trails.
>
> **中文描述:**
> 一个分屏3D渲染图，显示两个球从同一高度同时释放。左边的球垂直下落（纯垂直运动）。右边的球被水平抛出（纯水平运动）。它们后面有一个由垂直线和水平线组成的网格。频闪效果显示了它们在相等时间间隔内的位置。关键的视觉点是两个球在每次闪光时都处于完全相同的垂直高度，证明了右边球的水平运动不影响其垂直下落。左边球的路径是一条垂直直线。右边球的路径是一条弯曲的抛物线。标签："球A（下落）"和"球B（水平抛出）"。使用干净的教育风格，深色背景和明亮的霓虹轨迹。
>
> **Labels Required / 需要标注:**
> *   Ball A (Dropped) / 球A (下落)
> *   Ball B (Launched Horizontally) / 球B (水平抛出)
> *   Equal vertical displacement / 相等的垂直位移
> *   Parabolic path / 抛物线路径
>
> **Style / 风格:** 3D render with stroboscopic effect / 带频闪效果的3D渲染
>
> **Exam Relevance / 考试关联:**
> This is a classic demonstration of the independence of motion, a concept frequently tested in multiple-choice and theory questions. It explains why the time of flight depends only on the vertical motion.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A ball is kicked from ground level with an initial speed of $20 \text{ m s}^{-1}$ at an angle of $30^\circ$ to the horizontal. Calculate the horizontal and vertical components of the initial velocity.

**中文:**
一个球从地面以 $20 \text{ m s}^{-1}$ 的初速度，与水平方向成 $30^\circ$ 角被踢出。计算初速度的水平分量和垂直分量。

### Solution / 解答
**Step 1: Identify knowns.**
$u = 20 \text{ m s}^{-1}$, $\theta = 30^\circ$

**Step 2: Calculate the horizontal component ($u_x$).**
$$ u_x = u \cos \theta = 20 \times \cos(30^\circ) = 20 \times \frac{\sqrt{3}}{2} = 10\sqrt{3} \approx 17.3 \text{ m s}^{-1} $$

**Step 3: Calculate the vertical component ($u_y$).**
$$ u_y = u \sin \theta = 20 \times \sin(30^\circ) = 20 \times \frac{1}{2} = 10 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** $u_x = 17.3 \text{ m s}^{-1}$, $u_y = 10 \text{ m s}^{-1}$
**答案:** $u_x = 17.3 \text{ m s}^{-1}$, $u_y = 10 \text{ m s}^{-1}$

### Quick Tip / 提示
Always check if your calculator is in **Degree (DEG)** mode when working with angles in degrees. A common mistake is having it in Radian (RAD) mode, which gives a completely wrong answer.

---

# 7. Flashcards / 闪卡

**Card 1**
Q (EN): What are the two formulas for resolving a projectile's initial velocity $u$ at angle $\theta$ into horizontal and vertical components?
Q (CN): 将抛体初速度 $u$ 在角度 $\theta$ 下分解为水平和垂直分量的两个公式是什么？
A (EN): Horizontal: $u_x = u \cos \theta$; Vertical: $u_y = u \sin \theta$.
A (CN): 水平方向: $u_x = u \cos \theta$; 垂直方向: $u_y = u \sin \theta$.

**Card 2**
Q (EN): What is the acceleration of a projectile in the horizontal direction (ignoring air resistance)?
Q (CN): 在忽略空气阻力的情况下，抛体在水平方向的加速度是多少？
A (EN): Zero ($a_x = 0$). The horizontal velocity is constant.
A (CN): 零 ($a_x = 0$)。水平速度是恒定的。

**Card 3**
Q (EN): What is the acceleration of a projectile in the vertical direction?
Q (CN): 抛体在垂直方向的加速度是多少？
A (EN): The acceleration due to gravity, $g$, acting downwards ($a_y = -g \approx -9.81 \text{ m s}^{-2}$).
A (CN): 重力加速度 $g$，方向向下 ($a_y = -g \approx -9.81 \text{ m s}^{-2}$)。

**Card 4**
Q (EN): What is the "Independence of Motion" principle?
Q (CN): 什么是“运动的独立性”原理？
A (EN): The horizontal and vertical motions of a projectile are independent; they do not affect each other and can be analyzed separately.
A (CN): 抛体的水平运动和垂直运动是独立的；它们互不影响，可以分开分析。

**Card 5**
Q (EN): If a ball is thrown horizontally at 10 m/s from a cliff, what is its initial vertical velocity component?
Q (CN): 如果一个球从悬崖上以 10 m/s 的水平速度被抛出，它的初始垂直速度分量是多少？
A (EN): Zero ($u_y = 0 \text{ m/s}$). The launch angle is $0^\circ$, so $u_y = u \sin 0^\circ = 0$.
A (CN): 零 ($u_y = 0 \text{ m/s}$)。发射角为 $0^\circ$，所以 $u_y = u \sin 0^\circ = 0$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Horizontal and Vertical Components
  cn: 水平分量与垂直分量
parent_topic: Projectile Motion
parent_hub: "[[Projectile Motion]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Time of Flight and Range]]"
  - "[[Maximum Height]]"
  - "[[Projectile Motion Graphs]]"
language: bilingual_en_cn