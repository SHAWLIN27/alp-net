# 1. Overview / 概述

**English:**
Elastic collisions are a fundamental class of collisions where **both momentum and kinetic energy are conserved**. This distinguishes them from inelastic collisions, where kinetic energy is lost to heat, sound, or deformation. In the real world, perfectly elastic collisions are rare (e.g., subatomic particles, ideal gas molecules), but many macroscopic collisions (like billiard balls or steel ball bearings) approximate elastic behavior closely enough for A-Level analysis.

This sub-topic builds directly on [[Linear Momentum and Impulse]] and is a critical application of the [[Conservation of Momentum]] principle. Understanding elastic collisions allows you to solve for unknown velocities after a collision using two simultaneous equations — one from momentum conservation, one from kinetic energy conservation. This is a high-leverage skill for AS Physics exams, often appearing in multi-step problems and practical contexts.

**中文:**
弹性碰撞是一类基本的碰撞类型，其特点是**动量和动能均守恒**。这使其区别于非弹性碰撞（动能损失为热能、声能或形变能）。在现实世界中，完全弹性碰撞很少见（例如亚原子粒子、理想气体分子），但许多宏观碰撞（如台球或钢珠）足够接近弹性行为，可用于A-Level分析。

本子知识点直接建立在[[Linear Momentum and Impulse]]之上，是[[Conservation of Momentum]]原理的关键应用。理解弹性碰撞使您能够通过两个联立方程（一个来自动量守恒，一个来自动能守恒）求解碰撞后的未知速度。这是AS物理考试中的高价值技能，常出现在多步骤问题和实验情境中。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Elastic Collision** / 弹性碰撞 | A collision in which both total momentum and total kinetic energy of the system are conserved. | 系统总动量和总动能均守恒的碰撞。 |
| **Perfectly Elastic** / 完全弹性 | An idealized collision with no energy loss; relative speed of approach equals relative speed of separation. | 理想化的无能量损失碰撞；接近相对速度等于分离相对速度。 |
| **Relative Speed of Approach** / 接近相对速度 | The speed at which two objects move toward each other before collision: $u_1 - u_2$ (if moving in same direction) or $u_1 + u_2$ (if opposite). | 碰撞前两物体相互接近的速度。 |
| **Relative Speed of Separation** / 分离相对速度 | The speed at which two objects move apart after collision: $v_2 - v_1$ (if moving in same direction). | 碰撞后两物体相互分离的速度。 |
| **Coefficient of Restitution ($e$)** / 恢复系数 | For elastic collisions, $e = 1$; defined as $e = \frac{\text{relative speed of separation}}{\text{relative speed of approach}}$ | 对于弹性碰撞，$e=1$；定义为分离相对速度与接近相对速度之比。 |

---

# 3. Key Concepts / 关键概念

**English:**

### The Two Conservation Laws
For any elastic collision between two objects A and B:

1. **Momentum Conservation** (always true for any collision in an isolated system):
   $$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

2. **Kinetic Energy Conservation** (only for elastic collisions):
   $$\frac{1}{2}m_A u_A^2 + \frac{1}{2}m_B u_B^2 = \frac{1}{2}m_A v_A^2 + \frac{1}{2}m_B v_B^2$$

### The "Relative Speed" Shortcut
A powerful result derived from combining both equations is that for a perfectly elastic collision:

$$u_1 - u_2 = -(v_1 - v_2)$$

Or equivalently: **relative speed of approach = relative speed of separation**.

This is often faster to use than solving the full quadratic system, especially in exam contexts.

### Common Scenarios

| Scenario | Key Result |
|----------|------------|
| Equal masses, one stationary | The moving mass stops; the stationary mass moves with the original velocity. |
| Equal masses, both moving | The two masses exchange velocities. |
| Very unequal masses (e.g., ball vs. wall) | The lighter mass reverses direction with nearly the same speed. |

### Common Pitfalls
- **Forgetting the sign convention**: Velocities are vectors — always define a positive direction.
- **Assuming kinetic energy is always conserved**: Only for elastic collisions. Check the problem statement carefully.
- **Using the relative speed shortcut without checking elasticity**: It only applies when $e=1$.
- **Mixing up $u$ and $v$**: $u$ = initial velocity, $v$ = final velocity.

**中文:**

### 两条守恒定律
对于两个物体A和B之间的弹性碰撞：

1. **动量守恒**（任何孤立系统中的碰撞都成立）：
   $$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

2. **动能守恒**（仅适用于弹性碰撞）：
   $$\frac{1}{2}m_A u_A^2 + \frac{1}{2}m_B u_B^2 = \frac{1}{2}m_A v_A^2 + \frac{1}{2}m_B v_B^2$$

### "相对速度"快捷方法
将两个方程联立推导出的强大结果是：对于完全弹性碰撞：

$$u_1 - u_2 = -(v_1 - v_2)$$

等价于：**接近相对速度 = 分离相对速度**。

这通常比求解完整的二次方程组更快，尤其在考试中。

### 常见场景

| 场景 | 关键结果 |
|------|----------|
| 质量相等，一个静止 | 运动物体停止；静止物体以原速度运动。 |
| 质量相等，两者都运动 | 两物体交换速度。 |
| 质量悬殊（如球撞墙） | 轻质物体以几乎相同速度反向运动。 |

### 常见错误
- **忘记符号约定**：速度是矢量——始终定义正方向。
- **假设动能总是守恒**：仅适用于弹性碰撞。仔细阅读题目。
- **未检查弹性条件就使用相对速度快捷方法**：仅当$e=1$时适用。
- **混淆$u$和$v$**：$u$=初速度，$v$=末速度。

---

# 4. Formulas / 公式

## Primary Formula Set

$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 \quad \text{(Momentum)}$$

$$\frac{1}{2}m_1 u_1^2 + \frac{1}{2}m_2 u_2^2 = \frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2 \quad \text{(Kinetic Energy)}$$

## Derived Shortcut (for $e=1$)

$$u_1 - u_2 = v_2 - v_1$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $m_1, m_2$ | Masses of objects 1 and 2 | 物体1和2的质量 | kg |
| $u_1, u_2$ | Initial velocities (before collision) | 初速度（碰撞前） | m s$^{-1}$ |
| $v_1, v_2$ | Final velocities (after collision) | 末速度（碰撞后） | m s$^{-1}$ |

**Derivation / 推导:**

From momentum: $m_1(u_1 - v_1) = m_2(v_2 - u_2)$ ...(1)
From KE: $m_1(u_1^2 - v_1^2) = m_2(v_2^2 - u_2^2)$ ...(2)

Factor (2): $m_1(u_1 - v_1)(u_1 + v_1) = m_2(v_2 - u_2)(v_2 + u_2)$

Divide (2) by (1): $u_1 + v_1 = v_2 + u_2$

Rearrange: $u_1 - u_2 = v_2 - v_1$ ✓

**Conditions / 适用条件:**
- Perfectly elastic collision ($e=1$)
- No external forces (isolated system)
- One-dimensional motion (head-on collision)

> 📷 **IMAGE PROMPT — ELC-01: Elastic Collision Velocity Diagram**
>
> **English Prompt:**
> A clean physics textbook-style vector diagram showing two balls of masses m1 and m2 approaching each other with velocities u1 and u2 (left side), then separating with velocities v1 and v2 (right side). Use a horizontal axis with a positive direction arrow. Label all velocities with arrows above the balls. Use distinct colors: ball 1 in blue, ball 2 in red. Include a dashed vertical line at the collision point. Below the diagram, show the two conservation equations. Clean white background, professional exam-style layout.
>
> **中文描述:**
> 教科书风格的矢量图，显示两个质量分别为m1和m2的球体以速度u1和u2相互接近（左侧），然后以速度v1和v2分离（右侧）。使用水平轴和正方向箭头。在球体上方用箭头标注所有速度。球1用蓝色，球2用红色。在碰撞点处画一条虚线垂直线。图下方显示两个守恒方程。白色背景，专业考试风格。
>
> **Labels Required / 需要标注:**
> * Before collision: $u_1$, $u_2$, $m_1$, $m_2$
> * After collision: $v_1$, $v_2$, $m_1$, $m_2$
> * Positive direction arrow
> * "Before" and "After" labels
>
> **Style / 风格:** Textbook vector / 2D clean diagram
>
> **Exam Relevance / 考试关联:**
> Essential for setting up collision problems correctly. Many students lose marks by mislabeling velocities or forgetting direction signs.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — ELC-02: Equal Mass Elastic Collision Demonstration**
>
> **English Prompt:**
> A 3D-rendered physics demonstration showing Newton's Cradle with five steel balls. The leftmost ball is pulled back and about to strike. Show a freeze-frame at the moment of collision with motion blur lines. Use metallic silver balls, thin wires, and a wooden frame. Add small velocity vectors (arrows) above the balls: one arrow pointing right above the left ball, and one arrow pointing right above the rightmost ball (showing energy transfer). Include a text overlay: "Elastic Collision: Equal Mass → Velocity Exchange". Warm studio lighting, shallow depth of field, photorealistic style.
>
> **中文描述:**
> 3D渲染的物理演示，显示五个钢球的牛顿摆。最左边的球被拉回并即将撞击。显示碰撞瞬间的定格画面，带有运动模糊线条。使用金属银色球体、细线和木制框架。在球体上方添加小的速度矢量箭头：左球上方一个向右的箭头，最右球上方一个向右的箭头（显示能量传递）。叠加文字："弹性碰撞：等质量→速度交换"。温暖的影棚灯光，浅景深，照片级真实风格。
>
> **Labels Required / 需要标注:**
> * "Before: Ball A moving, Ball B stationary"
> * "After: Ball A stationary, Ball B moving"
> * Velocity arrows with labels $u$ and $v$
>
> **Style / 风格:** Photorealistic 3D render
>
> **Exam Relevance / 考试关联:**
> Newton's Cradle is the classic demonstration of elastic collisions. Understanding this visual helps students intuitively grasp velocity exchange in equal-mass collisions.

---

# 6. Worked Example / 典型例题

## Example 1: Equal Mass Elastic Collision

### Question / 题目
**English:**
A ball of mass 0.50 kg moving at 4.0 m s$^{-1}$ collides head-on and elastically with a stationary ball of mass 0.50 kg. Calculate the velocities of both balls after the collision.

**中文:**
一个质量为0.50 kg、以4.0 m s$^{-1}$运动的球与一个质量为0.50 kg的静止球发生正面弹性碰撞。计算碰撞后两球的速度。

### Solution / 解答

**Step 1: Define variables and sign convention**
Let positive direction be the initial direction of the moving ball.

$m_1 = 0.50 \text{ kg}, u_1 = +4.0 \text{ m s}^{-1}$
$m_2 = 0.50 \text{ kg}, u_2 = 0 \text{ m s}^{-1}$
$v_1 = ?, v_2 = ?$

**Step 2: Apply momentum conservation**
$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$
$$0.50(4.0) + 0.50(0) = 0.50 v_1 + 0.50 v_2$$
$$2.0 = 0.50(v_1 + v_2)$$
$$v_1 + v_2 = 4.0 \quad \text{(1)}$$

**Step 3: Apply elastic condition (relative speed shortcut)**
$$u_1 - u_2 = v_2 - v_1$$
$$4.0 - 0 = v_2 - v_1$$
$$v_2 - v_1 = 4.0 \quad \text{(2)}$$

**Step 4: Solve simultaneous equations**
From (1): $v_2 = 4.0 - v_1$
Substitute into (2): $(4.0 - v_1) - v_1 = 4.0$
$4.0 - 2v_1 = 4.0$
$-2v_1 = 0$
$v_1 = 0 \text{ m s}^{-1}$

Then $v_2 = 4.0 - 0 = 4.0 \text{ m s}^{-1}$

### Final Answer / 最终答案
**Answer:** After collision, ball 1 is stationary ($v_1 = 0$) and ball 2 moves at 4.0 m s$^{-1}$ in the original direction. **答案:** 碰撞后，球1静止（$v_1=0$），球2以4.0 m s$^{-1}$沿原方向运动。

### Quick Tip / 提示
For equal-mass elastic collisions where one object is initially stationary, the objects **exchange velocities**. Memorize this pattern — it saves time in exams!

对于等质量弹性碰撞且一个物体初始静止的情况，物体**交换速度**。记住这个模式——考试中能节省时间！

---

## Example 2: Unequal Mass Elastic Collision

### Question / 题目
**English:**
A 2.0 kg trolley moving at 3.0 m s$^{-1}$ collides elastically with a 1.0 kg trolley moving at 1.0 m s$^{-1}$ in the same direction. Calculate their velocities after collision.

**中文:**
一个2.0 kg的小车以3.0 m s$^{-1}$运动，与一个以1.0 m s$^{-1}$同向运动的1.0 kg小车发生弹性碰撞。计算碰撞后它们的速度。

### Solution / 解答

**Step 1: Define variables**
$m_1 = 2.0 \text{ kg}, u_1 = +3.0 \text{ m s}^{-1}$
$m_2 = 1.0 \text{ kg}, u_2 = +1.0 \text{ m s}^{-1}$

**Step 2: Momentum conservation**
$$2.0(3.0) + 1.0(1.0) = 2.0 v_1 + 1.0 v_2$$
$$6.0 + 1.0 = 2v_1 + v_2$$
$$2v_1 + v_2 = 7.0 \quad \text{(1)}$$

**Step 3: Elastic condition**
$$u_1 - u_2 = v_2 - v_1$$
$$3.0 - 1.0 = v_2 - v_1$$
$$v_2 - v_1 = 2.0 \quad \text{(2)}$$

**Step 4: Solve**
From (2): $v_2 = v_1 + 2.0$
Substitute into (1): $2v_1 + (v_1 + 2.0) = 7.0$
$3v_1 + 2.0 = 7.0$
$3v_1 = 5.0$
$v_1 = 1.67 \text{ m s}^{-1}$

Then $v_2 = 1.67 + 2.0 = 3.67 \text{ m s}^{-1}$

### Final Answer / 最终答案
**Answer:** $v_1 = 1.67 \text{ m s}^{-1}$, $v_2 = 3.67 \text{ m s}^{-1}$ (both in original direction). **答案:** $v_1 = 1.67 \text{ m s}^{-1}$, $v_2 = 3.67 \text{ m s}^{-1}$（均沿原方向）。

### Quick Tip / 提示
Always check your answer: the heavier object should slow down, and the lighter object should speed up. If your answer violates this intuition, recheck your signs!

始终检查答案：较重的物体应减速，较轻的物体应加速。如果答案违反这一直觉，重新检查符号！

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): What two quantities are conserved in an elastic collision?
Q (CN): 弹性碰撞中哪两个量守恒？
A (EN): Both momentum and kinetic energy are conserved.
A (CN): 动量和动能均守恒。

**Flashcard 2**
Q (EN): What is the relative speed relationship for a perfectly elastic collision?
Q (CN): 完全弹性碰撞的相对速度关系是什么？
A (EN): Relative speed of approach = Relative speed of separation ($u_1 - u_2 = v_2 - v_1$).
A (CN): 接近相对速度 = 分离相对速度 ($u_1 - u_2 = v_2 - v_1$)。

**Flashcard 3**
Q (EN): In an elastic collision between two equal masses where one is stationary, what happens?
Q (CN): 在等质量且一个静止的弹性碰撞中，会发生什么？
A (EN): The moving mass stops and the stationary mass moves with the original velocity (velocity exchange).
A (CN): 运动物体停止，静止物体以原速度运动（速度交换）。

**Flashcard 4**
Q (EN): What is the coefficient of restitution ($e$) for a perfectly elastic collision?
Q (CN): 完全弹性碰撞的恢复系数($e$)是多少？
A (EN): $e = 1$.
A (CN): $e = 1$。

**Flashcard 5**
Q (EN): Why can't we use only kinetic energy conservation to solve an elastic collision problem?
Q (CN): 为什么不能仅用动能守恒来求解弹性碰撞问题？
A (EN): Because we have two unknown velocities, so we need two equations: momentum conservation AND kinetic energy conservation (or the relative speed shortcut).
A (CN): 因为有两个未知速度，所以需要两个方程：动量守恒和动能守恒（或相对速度快捷方法）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Elastic Collisions
  cn: 弹性碰撞
parent_topic: Conservation of Momentum
parent_hub: "[[Conservation of Momentum]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Inelastic Collisions]]"
  - "[[Explosions and Recoil]]"
  - "[[Two-Dimensional Collisions]]"
  - "[[Linear Momentum and Impulse]]"
prerequisites:
  - "[[Linear Momentum and Impulse]]"
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn