# Two-Stage Motion Problems / 两阶段运动问题

---

## 1. Overview / 概述

**English:**
Two-stage motion problems involve an object undergoing motion that can be divided into two distinct phases, each with its own constant acceleration. These problems are common in real-world scenarios such as a car accelerating from rest then braking, or a ball thrown upward that then falls back down. The key skill is recognizing where one stage ends and the next begins, and correctly transferring kinematic variables (like final velocity of stage 1 becoming initial velocity of stage 2) across the boundary.

This sub-topic builds directly on [[The Five SUVAT Equations]] and [[Choosing the Right Equation]], and requires a solid understanding of [[Displacement, Velocity and Acceleration]]. It is a crucial stepping stone to more complex topics like [[Projectile Motion]] and [[Motion Graphs]].

**中文:**
两阶段运动问题涉及物体运动可分为两个不同阶段，每个阶段具有各自的恒定加速度。这类问题常见于现实场景，例如汽车从静止加速然后刹车，或球被向上抛出然后落回地面。关键技能是识别一个阶段何时结束、下一阶段何时开始，并正确地在边界处传递运动学变量（例如阶段1的末速度成为阶段2的初速度）。

本子知识点建立在[[The Five SUVAT Equations]]和[[Choosing the Right Equation]]之上，需要扎实理解[[Displacement, Velocity and Acceleration]]。它是学习更复杂主题如[[Projectile Motion]]和[[Motion Graphs]]的重要阶梯。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Two-Stage Motion** / 两阶段运动 | Motion that can be divided into two separate phases, each with constant acceleration, where the final conditions of stage 1 become the initial conditions of stage 2. | 可分为两个独立阶段的运动，每个阶段具有恒定加速度，阶段1的最终条件成为阶段2的初始条件。 |
| **Boundary Condition** / 边界条件 | The point in time and space where one stage of motion ends and the next begins; typically where velocity and displacement are continuous. | 运动一个阶段结束、下一阶段开始的时间和空间点；通常速度和位移在此处连续。 |
| **Stage Transition** / 阶段过渡 | The process of transferring kinematic variables (especially velocity and displacement) from the end of stage 1 to the start of stage 2. | 将运动学变量（特别是速度和位移）从阶段1结束传递到阶段2开始的过程。 |
| **Piecewise Constant Acceleration** / 分段恒定加速度 | Acceleration that is constant within each stage but may change value between stages. | 在每个阶段内加速度恒定，但阶段之间可能改变数值。 |
| **Total Displacement** / 总位移 | The sum of displacements from all stages, taking direction into account. | 考虑方向后，所有阶段位移的总和。 |
| **Total Time** / 总时间 | The sum of time intervals from all stages. | 所有阶段时间间隔的总和。 |

---

## 3. Key Concepts / 关键概念

**English:**

### The Transition Principle
The most critical idea in two-stage problems is that **the final velocity of stage 1 becomes the initial velocity of stage 2**. Similarly, the displacement at the end of stage 1 is the starting position for stage 2. This continuity is what links the two stages together.

### Step-by-Step Problem-Solving Strategy

1. **Identify the two stages** — Look for changes in acceleration (e.g., "then brakes are applied", "after reaching a certain speed").
2. **List known variables for each stage** — Use a SUVAT table for each stage separately.
3. **Find the linking variable** — Usually the velocity at the transition point.
4. **Solve stage 1** — Use [[Choosing the Right Equation]] to find the linking velocity.
5. **Transfer the linking velocity** — Set $u_2 = v_1$ (final velocity of stage 1 = initial velocity of stage 2).
6. **Solve stage 2** — Use the appropriate SUVAT equation.
7. **Combine results** — Add displacements and times if total quantities are required.

### Common Pitfalls

- **Forgetting to transfer velocity** — The most frequent mistake. Always check: $v_1 = u_2$.
- **Using wrong sign conventions** — If acceleration changes direction (e.g., from acceleration to deceleration), ensure signs are consistent.
- **Assuming total displacement is simply the sum** — Only if motion is in one direction; if direction reverses, displacements may partially cancel.
- **Mixing up time intervals** — Each stage has its own time $t_1$ and $t_2$; total time $t_{total} = t_1 + t_2$.

### Real-World Examples
- A car accelerating from rest to a speed limit, then travelling at constant speed (though constant speed is a special case with $a=0$).
- A ball thrown upward (stage 1: upward with $g$ downward) and falling back (stage 2: downward with $g$ downward).
- A train braking to a stop, then reversing (two stages with different acceleration directions).

**中文:**

### 过渡原则
两阶段问题中最关键的概念是：**阶段1的末速度成为阶段2的初速度**。同样，阶段1结束时的位移是阶段2的起始位置。这种连续性是将两个阶段联系起来的纽带。

### 分步解题策略

1. **识别两个阶段** — 寻找加速度的变化（例如"然后刹车被施加"、"达到一定速度后"）。
2. **列出每个阶段的已知变量** — 为每个阶段分别制作SUVAT表格。
3. **找到连接变量** — 通常是过渡点的速度。
4. **求解阶段1** — 使用[[Choosing the Right Equation]]找到连接速度。
5. **传递连接速度** — 设 $u_2 = v_1$（阶段1的末速度 = 阶段2的初速度）。
6. **求解阶段2** — 使用适当的SUVAT方程。
7. **合并结果** — 如果需要总量，则相加位移和时间。

### 常见错误

- **忘记传递速度** — 最常见的错误。始终检查：$v_1 = u_2$。
- **使用错误的符号约定** — 如果加速度改变方向（例如从加速到减速），确保符号一致。
- **假设总位移就是简单相加** — 仅当运动方向一致时才成立；如果方向反转，位移可能部分抵消。
- **混淆时间间隔** — 每个阶段有自己的时间 $t_1$ 和 $t_2$；总时间 $t_{total} = t_1 + t_2$。

### 现实例子
- 汽车从静止加速到限速，然后匀速行驶（匀速是 $a=0$ 的特殊情况）。
- 球向上抛出（阶段1：向上，$g$ 向下）然后落回（阶段2：向下，$g$ 向下）。
- 火车刹车停止，然后倒车（两个阶段加速度方向不同）。

---

## 4. Formulas / 公式

The core formulas are the five SUVAT equations, applied separately to each stage:

$$v = u + at$$

$$s = ut + \frac{1}{2}at^2$$

$$v^2 = u^2 + 2as$$

$$s = \frac{(u+v)}{2}t$$

$$s = vt - \frac{1}{2}at^2$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $u$ | Initial velocity | 初速度 | m s$^{-1}$ |
| $v$ | Final velocity | 末速度 | m s$^{-1}$ |
| $a$ | Acceleration | 加速度 | m s$^{-2}$ |
| $s$ | Displacement | 位移 | m |
| $t$ | Time | 时间 | s |

### The Transition Equation / 过渡方程

The key linking relationship:

$$v_1 = u_2$$

Where $v_1$ is the final velocity of stage 1 and $u_2$ is the initial velocity of stage 2.

### Total Quantities / 总量

$$s_{total} = s_1 + s_2$$

$$t_{total} = t_1 + t_2$$

**Conditions / 适用条件:**
- Acceleration is constant within each stage.
- The transition point is clearly defined (e.g., when brakes are applied, when the ball reaches maximum height).
- Direction is consistently defined (choose a positive direction and stick to it).

> 📷 **IMAGE PROMPT — SUVAT-TS01: Two-Stage Motion Diagram**
>
> **English Prompt:**
> A clean vector diagram showing a two-stage motion scenario. Left side: a car accelerating from rest (stage 1, a₁ positive, u₁=0, v₁ at transition). Middle: a dashed vertical line labeled "Transition Point" with v₁ = u₂. Right side: the car decelerating (stage 2, a₂ negative, u₂ = v₁, v₂ = 0). Below each stage, show the SUVAT variables listed in a table format. Use blue for stage 1, red for stage 2. Include a position-time graph below showing two parabolic segments meeting at the transition point. Clean textbook style, white background, black labels with colored variable highlights.
>
> **中文描述:**
> 一个清晰的两阶段运动矢量图。左侧：汽车从静止加速（阶段1，a₁为正，u₁=0，过渡点v₁）。中间：一条虚线垂直线标记为"过渡点"，标注v₁ = u₂。右侧：汽车减速（阶段2，a₂为负，u₂ = v₁，v₂ = 0）。每个阶段下方以表格形式列出SUVAT变量。阶段1用蓝色，阶段2用红色。下方显示位置-时间图，两个抛物线线段在过渡点相接。干净的教科书风格，白色背景，黑色标签，彩色变量高亮。
>
> **Labels Required / 需要标注:**
> * Stage 1: u₁=0, a₁, v₁, s₁, t₁
> * Transition: v₁ = u₂
> * Stage 2: u₂=v₁, a₂, v₂=0, s₂, t₂
> * Total: s_total = s₁ + s₂, t_total = t₁ + t₂
>
> **Style / 风格:** Textbook vector diagram with graph
>
> **Exam Relevance / 考试关联:**
> This diagram directly illustrates the structure of typical exam questions on two-stage motion. Students should be able to sketch this and label all variables.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — SUVAT-TS02: Ball Thrown Upward Two-Stage Motion**
>
> **English Prompt:**
> A vertical diagram showing a ball thrown upward from ground level. Split the motion into two stages with a horizontal dashed line at the maximum height. Stage 1 (upward): ball rising, arrows showing velocity decreasing (shorter arrows), acceleration g downward (constant arrow). Stage 2 (downward): ball falling, arrows showing velocity increasing (longer arrows), acceleration g downward (same constant arrow). At the maximum height, label "v=0, transition point". Show SUVAT tables for each stage. Include a velocity-time graph on the right showing a straight line crossing zero at the transition. Clean physics textbook style, white background, blue and red color coding for stages.
>
> **中文描述:**
> 一个垂直方向图，显示球从地面向上抛出。用一条水平虚线在最高点将运动分为两个阶段。阶段1（向上）：球上升，箭头显示速度减小（箭头变短），加速度g向下（恒定箭头）。阶段2（向下）：球下落，箭头显示速度增加（箭头变长），加速度g向下（相同恒定箭头）。在最高点标注"v=0，过渡点"。为每个阶段显示SUVAT表格。右侧包含速度-时间图，显示一条直线在过渡点穿过零。干净的物理教科书风格，白色背景，阶段用蓝色和红色编码。
>
> **Labels Required / 需要标注:**
> * Stage 1: u₁=+u, a₁=-g, v₁=0, s₁=H, t₁
> * Transition: v₁=0=u₂
> * Stage 2: u₂=0, a₂=-g, v₂=-u, s₂=-H, t₂
> * Graph: v-t line with slope -g, crossing t-axis at transition
>
> **Style / 风格:** Textbook vector diagram with graph
>
> **Exam Relevance / 考试关联:**
> This is a classic exam scenario. Understanding the symmetry (time up = time down, speed at return = initial speed) is a key exam shortcut.

---

## 6. Worked Example / 典型例题

### Example 1: Car Accelerating Then Braking

### Question / 题目
**English:**
A car starts from rest and accelerates uniformly at $2.0 \text{ m s}^{-2}$ for $5.0$ seconds. The driver then applies the brakes, causing a uniform deceleration of $4.0 \text{ m s}^{-2}$ until the car stops.

(a) Calculate the maximum speed reached by the car.
(b) Calculate the total distance travelled by the car.
(c) Calculate the total time for the journey.

**中文:**
一辆汽车从静止开始，以 $2.0 \text{ m s}^{-2}$ 的加速度匀加速 $5.0$ 秒。然后司机刹车，产生 $4.0 \text{ m s}^{-2}$ 的匀减速，直到汽车停止。

(a) 计算汽车达到的最大速度。
(b) 计算汽车行驶的总距离。
(c) 计算整个行程的总时间。

### Solution / 解答

**Stage 1: Acceleration**

Known: $u_1 = 0$, $a_1 = +2.0 \text{ m s}^{-2}$, $t_1 = 5.0 \text{ s}$

(a) Find $v_1$ (maximum speed):

Using $v = u + at$:

$$v_1 = 0 + (2.0)(5.0) = 10 \text{ m s}^{-1}$$

**Transition:** $v_1 = u_2 = 10 \text{ m s}^{-1}$

**Stage 2: Deceleration**

Known: $u_2 = 10 \text{ m s}^{-1}$, $a_2 = -4.0 \text{ m s}^{-2}$ (negative because deceleration), $v_2 = 0$

(b) Find $s_2$:

Using $v^2 = u^2 + 2as$:

$$0 = (10)^2 + 2(-4.0)s_2$$
$$0 = 100 - 8s_2$$
$$s_2 = 12.5 \text{ m}$$

Find $s_1$:

Using $s = ut + \frac{1}{2}at^2$:

$$s_1 = 0 + \frac{1}{2}(2.0)(5.0)^2 = 25 \text{ m}$$

Total distance: $s_{total} = s_1 + s_2 = 25 + 12.5 = 37.5 \text{ m}$

(c) Find $t_2$:

Using $v = u + at$:

$$0 = 10 + (-4.0)t_2$$
$$t_2 = 2.5 \text{ s}$$

Total time: $t_{total} = t_1 + t_2 = 5.0 + 2.5 = 7.5 \text{ s}$

### Final Answer / 最终答案

**Answer:**
(a) $10 \text{ m s}^{-1}$
(b) $37.5 \text{ m}$
(c) $7.5 \text{ s}$

**答案:**
(a) $10 \text{ m s}^{-1}$
(b) $37.5 \text{ m}$
(c) $7.5 \text{ s}$

### Quick Tip / 提示
Always draw a velocity-time graph for two-stage problems. The area under the graph gives displacement, and the slopes give accelerations. For this problem, the v-t graph is a triangle with base 7.5 s and height 10 m s$^{-1}$, so area = $\frac{1}{2} \times 7.5 \times 10 = 37.5$ m — a quick check!

---

### Example 2: Ball Thrown Upward

### Question / 题目
**English:**
A ball is thrown vertically upward from ground level with an initial speed of $15 \text{ m s}^{-1}$. Take $g = 10 \text{ m s}^{-2}$.

(a) Calculate the maximum height reached.
(b) Calculate the time taken to return to ground level.
(c) Calculate the speed of the ball just before it hits the ground.

**中文:**
一个球从地面以 $15 \text{ m s}^{-1}$ 的初速度竖直向上抛出。取 $g = 10 \text{ m s}^{-2}$。

(a) 计算达到的最大高度。
(b) 计算返回地面所需的时间。
(c) 计算球即将落地时的速度。

### Solution / 解答

**Stage 1: Upward motion**

Take upward as positive. Known: $u_1 = +15 \text{ m s}^{-1}$, $a_1 = -10 \text{ m s}^{-2}$, $v_1 = 0$ (at maximum height)

(a) Find $s_1$ (maximum height):

Using $v^2 = u^2 + 2as$:

$$0 = (15)^2 + 2(-10)s_1$$
$$0 = 225 - 20s_1$$
$$s_1 = 11.25 \text{ m}$$

Find $t_1$:

Using $v = u + at$:

$$0 = 15 + (-10)t_1$$
$$t_1 = 1.5 \text{ s}$$

**Transition:** $v_1 = 0 = u_2$

**Stage 2: Downward motion**

Known: $u_2 = 0$, $a_2 = -10 \text{ m s}^{-2}$ (still downward, so same sign), $s_2 = -11.25 \text{ m}$ (downward displacement)

(b) Find $t_2$:

Using $s = ut + \frac{1}{2}at^2$:

$$-11.25 = 0 + \frac{1}{2}(-10)t_2^2$$
$$-11.25 = -5t_2^2$$
$$t_2^2 = 2.25$$
$$t_2 = 1.5 \text{ s}$$

Total time: $t_{total} = t_1 + t_2 = 1.5 + 1.5 = 3.0 \text{ s}$

(c) Find $v_2$:

Using $v = u + at$:

$$v_2 = 0 + (-10)(1.5) = -15 \text{ m s}^{-1}$$

Speed = $|v_2| = 15 \text{ m s}^{-1}$

### Final Answer / 最终答案

**Answer:**
(a) $11.25 \text{ m}$
(b) $3.0 \text{ s}$
(c) $15 \text{ m s}^{-1}$

**答案:**
(a) $11.25 \text{ m}$
(b) $3.0 \text{ s}$
(c) $15 \text{ m s}^{-1}$

### Quick Tip / 提示
For symmetrical vertical motion under gravity (no air resistance), time up = time down, and speed at return = initial speed. This symmetry can save you calculation time in exams. However, always show the full working for method marks.

---

## 7. Flashcards / 闪卡

**Flashcard 1**

Q (EN): What is the key linking relationship between two stages of motion?
Q (CN): 两个运动阶段之间的关键连接关系是什么？
A (EN): The final velocity of stage 1 becomes the initial velocity of stage 2: $v_1 = u_2$.
A (CN): 阶段1的末速度成为阶段2的初速度：$v_1 = u_2$。

**Flashcard 2**

Q (EN): A car accelerates from rest at 2 m s$^{-2}$ for 4 s, then brakes at 4 m s$^{-2}$. What is the maximum speed?
Q (CN): 汽车从静止以2 m s$^{-2}$加速4秒，然后以4 m s$^{-2}$刹车。最大速度是多少？
A (EN): $v = u + at = 0 + 2 \times 4 = 8 \text{ m s}^{-1}$
A (CN): $v = u + at = 0 + 2 \times 4 = 8 \text{ m s}^{-1}$

**Flashcard 3**

Q (EN): What is the most common mistake in two-stage motion problems?
Q (CN): 两阶段运动问题中最常见的错误是什么？
A (EN): Forgetting to transfer the velocity from stage 1 to stage 2 (not setting $u_2 = v_1$).
A (CN): 忘记将速度从阶段1传递到阶段2（没有设 $u_2 = v_1$）。

**Flashcard 4**

Q (EN): For a ball thrown upward and returning to the same height, what is the total displacement?
Q (CN): 对于向上抛出并返回同一高度的球，总位移是多少？
A (EN): Zero, because the ball returns to its starting point.
A (CN): 零，因为球返回起点。

**Flashcard 5**

Q (EN): How do you calculate total distance in a two-stage problem?
Q (CN): 如何计算两阶段问题中的总距离？
A (EN): Add the distances from each stage: $s_{total} = s_1 + s_2$ (all positive values).
A (CN): 将每个阶段的距离相加：$s_{total} = s_1 + s_2$（所有正值）。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Two-Stage Motion Problems
  cn: 两阶段运动问题
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
  - "[[Free Fall Under Gravity]]"
prerequisites:
  - "[[Displacement, Velocity and Acceleration]]"
related_topics:
  - "[[Motion Graphs]]"
  - "[[Projectile Motion]]"
language: bilingual_en_cn