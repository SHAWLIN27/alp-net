# Speed and Velocity / 速率与速度

---

## 1. Overview / 概述

**English:**
Speed and velocity are fundamental concepts in kinematics that describe how fast an object is moving. While often confused in everyday language, in physics they have distinct meanings: speed is a scalar quantity that only tells us "how fast," while velocity is a vector quantity that tells us "how fast AND in what direction." This distinction is crucial for understanding [[Displacement, Velocity and Acceleration]] and forms the foundation for more advanced topics like [[Acceleration]] and [[Equations of Motion (SUVAT)]]. Understanding the difference between scalars and vectors (see [[Scalars and Vectors]]) is essential before tackling this sub-topic.

**中文:**
速率和速度是运动学中描述物体运动快慢的基本概念。虽然在日常用语中经常混淆，但在物理学中它们有明确的区别：速率是标量，只告诉我们"多快"；而速度是矢量，告诉我们"多快 AND 朝哪个方向"。这一区别对于理解[[位移、速度和加速度]]至关重要，也是学习[[加速度]]和[[运动方程（SUVAT）]]等更高级主题的基础。在学习本子知识点之前，理解标量和矢量的区别（参见[[标量与矢量]]）是必要的。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Speed** / 速率 | The rate of change of distance with time. A scalar quantity. | 距离随时间的变化率。标量。 |
| **Velocity** / 速度 | The rate of change of displacement with time. A vector quantity. | 位移随时间的变化率。矢量。 |
| **Average Speed** / 平均速率 | Total distance traveled divided by total time taken. | 总路程除以总时间。 |
| **Average Velocity** / 平均速度 | Total displacement divided by total time taken. | 总位移除以总时间。 |
| **Instantaneous Speed** / 瞬时速率 | The speed at a particular instant in time. | 某一特定时刻的速率。 |
| **Instantaneous Velocity** / 瞬时速度 | The velocity at a particular instant in time. | 某一特定时刻的速度。 |

---

## 3. Key Concepts / 关键概念

**English:**

### The Scalar-Vector Distinction
The most important concept here is that **speed is a scalar** (magnitude only) while **velocity is a vector** (magnitude AND direction). This means:
- Speed is always positive (or zero)
- Velocity can be positive, negative, or zero depending on direction
- Two objects can have the same speed but different velocities if they move in different directions

### Average vs. Instantaneous
- **Average speed/velocity** considers the entire journey
- **Instantaneous speed/velocity** is what a speedometer reads at a specific moment

### Common Pitfall: Speed from Velocity
The magnitude of instantaneous velocity equals instantaneous speed. However, the magnitude of **average** velocity does NOT equal average speed unless motion is in a straight line without changing direction.

### Relationship to [[Displacement and Distance]]
- Speed uses [[Displacement and Distance|distance]] (scalar path length)
- Velocity uses [[Displacement and Distance|displacement]] (vector from start to end)

### Connection to [[Motion Graphs]]
- On a displacement-time graph, the gradient gives velocity
- On a distance-time graph, the gradient gives speed

**中文:**

### 标量与矢量的区别
这里最重要的概念是：**速率是标量**（只有大小），而**速度是矢量**（大小和方向）。这意味着：
- 速率总是正值（或零）
- 速度可以是正、负或零，取决于方向
- 两个物体如果运动方向不同，可以有相同的速率但不同的速度

### 平均与瞬时
- **平均速率/速度**考虑整个运动过程
- **瞬时速率/速度**是速度表在某一特定时刻的读数

### 常见误区：从速度得到速率
瞬时速度的大小等于瞬时速率。但是，**平均**速度的大小不等于平均速率，除非运动是直线且不改变方向。

### 与[[位移与距离]]的关系
- 速率使用[[位移与距离|距离]]（标量路径长度）
- 速度使用[[位移与距离|位移]]（从起点到终点的矢量）

### 与[[运动图像]]的联系
- 在位移-时间图像上，斜率给出速度
- 在距离-时间图像上，斜率给出速率

---

## 4. Formulas / 公式

### Speed / 速率

$$ \text{Speed} = \frac{\text{Distance}}{\text{Time}} \quad \text{or} \quad v = \frac{d}{t} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v$ | speed | 速率 | m/s |
| $d$ | distance | 距离 | m |
| $t$ | time | 时间 | s |

### Velocity / 速度

$$ \text{Velocity} = \frac{\text{Displacement}}{\text{Time}} \quad \text{or} \quad \vec{v} = \frac{\vec{s}}{t} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{v}$ | velocity | 速度 | m/s |
| $\vec{s}$ | displacement | 位移 | m |
| $t$ | time | 时间 | s |

### Average Speed vs. Average Velocity / 平均速率与平均速度

$$ \text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}} $$

$$ \text{Average Velocity} = \frac{\text{Total Displacement}}{\text{Total Time}} $$

**Derivation / 推导:**
These are definitions, not derived formulas. They come directly from the definitions of speed and velocity as rates of change.

**Conditions / 适用条件:**
- These formulas assume constant speed/velocity over the time interval
- For instantaneous values, we use calculus: $v = \frac{ds}{dt}$ or $\vec{v} = \frac{d\vec{s}}{dt}$
- Average formulas work for any motion, but the result is an average, not the actual speed/velocity at any moment

> 📷 **IMAGE PROMPT — F01: Speed vs Velocity Comparison Diagram**
>
> **English Prompt:**
> A split diagram showing two scenarios side by side. Left side: a person walking along a curved path from point A to point B, with the curved path labeled "Distance = 100m" and a straight arrow from A to B labeled "Displacement = 60m East". Right side: a car on a straight road moving east at 20 m/s, with a speedometer showing 20 m/s and a direction arrow labeled "East". Both diagrams should have clear labels in English. Clean textbook vector style with blue and red color coding (blue for scalar, red for vector).
>
> **中文描述:**
> 一个分屏对比图。左侧：一个人沿弯曲路径从A点走到B点，弯曲路径标注"距离=100m"，从A到B的直箭头标注"位移=60m 向东"。右侧：一辆汽车在直路上向东行驶，速度为20 m/s，速度表显示20 m/s，方向箭头标注"向东"。两个图都有清晰的英文标注。干净的教科书矢量风格，蓝色和红色编码（蓝色代表标量，红色代表矢量）。
>
> **Labels Required / 需要标注:**
> * "Distance = 100m" (curved path)
> * "Displacement = 60m East" (straight arrow)
> * "Speed = 20 m/s" (speedometer)
> * "Velocity = 20 m/s East" (direction arrow)
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This diagram directly addresses the most common exam question: distinguishing between speed and velocity. Students must understand that the same journey can have different values for speed and velocity.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — F02: Average vs Instantaneous Velocity**
>
> **English Prompt:**
> A displacement-time graph showing a curved line. Three points are marked: A (at t=0s, s=0m), B (at t=5s, s=20m), and C (at t=10s, s=30m). A straight dashed line connects A to C, labeled "Average velocity = 3 m/s". At point B, a tangent line is drawn, labeled "Instantaneous velocity = 6 m/s". The graph has labeled axes: "Displacement (m)" on y-axis and "Time (s)" on x-axis. Clean textbook vector style with grid lines.
>
> **中文描述:**
> 一个位移-时间图，显示一条曲线。标记三个点：A（t=0s, s=0m）、B（t=5s, s=20m）和C（t=10s, s=30m）。一条虚线连接A到C，标注"平均速度=3 m/s"。在B点画一条切线，标注"瞬时速度=6 m/s"。图有标注的坐标轴：y轴为"位移(m)"，x轴为"时间(s)"。干净的教科书矢量风格，带网格线。
>
> **Labels Required / 需要标注:**
> * "Average velocity = 3 m/s" (dashed line A-C)
> * "Instantaneous velocity = 6 m/s" (tangent at B)
> * Axes: "Displacement (m)" and "Time (s)"
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This graph is a common exam question type. Students must be able to calculate average velocity from the chord and instantaneous velocity from the tangent.

---

## 6. Worked Example / 典型例题

### Example 1: Average Speed vs Average Velocity

### Question / 题目
**English:**
A runner completes one lap of a 400m circular track in 50 seconds. Calculate:
(a) The average speed of the runner
(b) The average velocity of the runner

**中文:**
一名跑步者在50秒内完成一圈400米的圆形跑道。计算：
(a) 跑步者的平均速率
(b) 跑步者的平均速度

### Solution / 解答

**Part (a): Average Speed**

$$ \text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}} = \frac{400 \text{ m}}{50 \text{ s}} = 8.0 \text{ m/s} $$

**Part (b): Average Velocity**

After one complete lap, the runner returns to the starting point, so:
- Total displacement = 0 m (start and end at same point)
- Average velocity = 0/50 = 0 m/s

$$ \text{Average Velocity} = \frac{\text{Total Displacement}}{\text{Total Time}} = \frac{0 \text{ m}}{50 \text{ s}} = 0 \text{ m/s} $$

### Final Answer / 最终答案
**Answer:** (a) 8.0 m/s (b) 0 m/s
**答案:** (a) 8.0 m/s (b) 0 m/s

### Quick Tip / 提示
**English:** When an object returns to its starting point, displacement is zero, so average velocity is always zero — regardless of how fast it moved!
**中文:** 当物体回到起点时，位移为零，所以平均速度总是零——无论它运动得多快！

---

### Example 2: Calculating Velocity from Displacement

### Question / 题目
**English:**
A car travels 200 m east in 10 seconds, then 100 m west in 5 seconds. Calculate:
(a) The total distance traveled
(b) The total displacement
(c) The average speed
(d) The average velocity

**中文:**
一辆汽车向东行驶200米用时10秒，然后向西行驶100米用时5秒。计算：
(a) 总路程
(b) 总位移
(c) 平均速率
(d) 平均速度

### Solution / 解答

**Part (a): Total Distance**
$$ \text{Total Distance} = 200 \text{ m} + 100 \text{ m} = 300 \text{ m} $$

**Part (b): Total Displacement**
Taking east as positive:
$$ \text{Total Displacement} = 200 \text{ m (east)} + (-100 \text{ m (west)}) = 100 \text{ m east} $$

**Part (c): Average Speed**
$$ \text{Average Speed} = \frac{300 \text{ m}}{15 \text{ s}} = 20 \text{ m/s} $$

**Part (d): Average Velocity**
$$ \text{Average Velocity} = \frac{100 \text{ m east}}{15 \text{ s}} = 6.67 \text{ m/s east} $$

### Final Answer / 最终答案
**Answer:** (a) 300 m (b) 100 m east (c) 20 m/s (d) 6.67 m/s east
**答案:** (a) 300 m (b) 100 m 向东 (c) 20 m/s (d) 6.67 m/s 向东

### Quick Tip / 提示
**English:** Always include direction when stating velocity! A velocity without direction is incomplete.
**中文:** 在表述速度时一定要包含方向！没有方向的速度是不完整的。

---

## 7. Flashcards / 闪卡

**Card 1:**
Q (EN): What is the difference between speed and velocity?
Q (CN): 速率和速度有什么区别？
A (EN): Speed is a scalar (magnitude only), velocity is a vector (magnitude and direction).
A (CN): 速率是标量（只有大小），速度是矢量（大小和方向）。

**Card 2:**
Q (EN): What is the formula for average speed?
Q (CN): 平均速率的公式是什么？
A (EN): Average speed = total distance / total time
A (CN): 平均速率 = 总路程 / 总时间

**Card 3:**
Q (EN): What is the formula for average velocity?
Q (CN): 平均速度的公式是什么？
A (EN): Average velocity = total displacement / total time
A (CN): 平均速度 = 总位移 / 总时间

**Card 4:**
Q (EN): If a runner completes one lap of a circular track, what is their average velocity?
Q (CN): 如果跑步者完成一圈圆形跑道，他们的平均速度是多少？
A (EN): Zero, because displacement is zero (returns to starting point).
A (CN): 零，因为位移为零（回到起点）。

**Card 5:**
Q (EN): What does the gradient of a displacement-time graph represent?
Q (CN): 位移-时间图像的斜率代表什么？
A (EN): Velocity (instantaneous velocity if tangent, average velocity if chord).
A (CN): 速度（切线代表瞬时速度，弦线代表平均速度）。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Speed and Velocity
  cn: 速率与速度
parent_topic: Displacement, Velocity and Acceleration
parent_hub: "[[Displacement, Velocity and Acceleration]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Displacement and Distance]]"
  - "[[Acceleration]]"
  - "[[Terminal Velocity]]"
prerequisites:
  - "[[Scalars and Vectors]]"
related_topics:
  - "[[Motion Graphs]]"
  - "[[Equations of Motion (SUVAT)]]"
language: bilingual_en_cn