# 1. Overview / 概述

**English:**
Newton's First Law of Motion, also known as the **Law of Inertia**, is the foundation of classical mechanics. It states that an object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted upon by a net external force. This sub-topic introduces the concept of **inertia** as a property of mass, and explains why objects resist changes to their motion. Understanding this law is essential before studying [[Newton's Second Law (F=ma)]] and [[Newton's Third Law (Action-Reaction)]], as it defines the condition for equilibrium and the role of unbalanced forces. It also connects to [[Linear Momentum and Impulse]] through the idea of motion persistence.

**中文:**
牛顿第一运动定律，也称为**惯性定律**，是经典力学的基础。它指出：除非受到净外力的作用，否则静止的物体保持静止，运动的物体保持匀速直线运动。本子知识点介绍了**惯性**作为质量属性的概念，并解释了物体为何抵抗运动状态的改变。理解这一定律是学习[[牛顿第二定律 (F=ma)]]和[[牛顿第三定律 (作用力与反作用力)]]的前提，因为它定义了平衡条件和不平衡力的作用。它还与[[线性动量与冲量]]通过运动持续性的概念相联系。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Newton's First Law** / 牛顿第一定律 | Every object continues in its state of rest or uniform motion in a straight line unless acted upon by a resultant (net) external force. | 每个物体都保持静止或匀速直线运动状态，除非受到净外力的作用。 |
| **Inertia** / 惯性 | The property of an object that resists any change in its state of motion; directly proportional to its mass. | 物体抵抗其运动状态改变的性质；与质量成正比。 |
| **Equilibrium** / 平衡 | A state where the net force acting on an object is zero, resulting in zero acceleration (either at rest or moving at constant velocity). | 作用在物体上的合力为零的状态，导致加速度为零（静止或匀速运动）。 |
| **Net Force** / 净力 | The vector sum of all forces acting on an object; also called resultant force. | 作用在物体上所有力的矢量和；也称为合力。 |
| **Uniform Motion** / 匀速运动 | Motion at constant speed in a straight line (constant velocity). | 沿直线以恒定速度运动（恒定速度）。 |

---

# 3. Key Concepts / 关键概念

**English:**
Newton's First Law is often misunderstood as "objects naturally come to rest." In reality, objects only stop because of **external forces** like friction or air resistance. The law reveals two key ideas:

1. **Inertia is mass-dependent:** A heavier object (e.g., a lorry) has more inertia than a lighter one (e.g., a bicycle), meaning it requires a larger force to change its motion. This is why it's harder to push a car than a shopping trolley.

2. **Equilibrium condition:** When the [[Free-body Diagrams]] show that all forces cancel out (net force = 0), the object is in equilibrium. It can be either stationary or moving at constant velocity — both are valid states under the First Law.

**Common pitfalls:**
- Thinking "at rest" is the only natural state — constant velocity is equally natural.
- Confusing inertia with force — inertia is a property, not a force.
- Forgetting that friction is an external force — in idealised problems, we often "ignore friction" to apply the First Law.

**中文:**
牛顿第一定律常被误解为“物体会自然停下来”。实际上，物体停止运动只是因为**外力**（如摩擦力或空气阻力）的作用。该定律揭示了两个关键思想：

1. **惯性取决于质量：** 较重的物体（如卡车）比轻的物体（如自行车）具有更大的惯性，这意味着需要更大的力才能改变其运动状态。这就是为什么推汽车比推购物车更难。

2. **平衡条件：** 当[[受力分析图]]显示所有力相互抵消（净力 = 0）时，物体处于平衡状态。它可以是静止的，也可以是以恒定速度运动——这两种状态在第一定律下都是有效的。

**常见误区：**
- 认为“静止”是唯一自然状态——匀速运动同样自然。
- 混淆惯性和力——惯性是一种属性，不是力。
- 忘记摩擦力是外力——在理想化问题中，我们经常“忽略摩擦力”来应用第一定律。

> 📷 **IMAGE PROMPT — N1L-01: Inertia Demonstration**
>
> **English Prompt:**
> A split-screen 3D render showing two scenarios: Left side — a person pushing a heavy lorry with difficulty (lorry barely moves); Right side — same person easily pushing a bicycle. Both on a frictionless surface. Labels: "Large mass = large inertia" on lorry side, "Small mass = small inertia" on bicycle side. Clean white background, textbook style, with force arrows showing equal pushing force but different acceleration outcomes.
>
> **中文描述:**
> 分屏3D渲染图，展示两个场景：左侧——一个人费力推重型卡车（卡车几乎不动）；右侧——同一个人轻松推自行车。两者都在无摩擦表面上。标签：卡车侧“大质量 = 大惯性”，自行车侧“小质量 = 小惯性”。干净白色背景，教科书风格，力箭头显示相同的推力但不同的加速度结果。
>
> **Labels Required / 需要标注:**
> * "Large mass = large inertia" / "大质量 = 大惯性"
> * "Small mass = small inertia" / "小质量 = 小惯性"
> * Force arrows (F) on both objects
>
> **Style / 风格:** 3D render, textbook vector
>
> **Exam Relevance / 考试关联:**
> Helps students visualise why mass determines inertia, a common exam concept.

---

# 4. Formulas / 公式

Newton's First Law is a **qualitative law** — it does not have a single formula like F=ma. However, it is mathematically expressed through the **equilibrium condition**:

$$ \sum \vec{F} = 0 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\sum \vec{F}$ | Vector sum of all forces (net force) | 所有力的矢量和（净力） | N (newtons) |
| $0$ | Zero net force | 净力为零 | N (newtons) |

**Derivation / 推导:**
From [[Newton's Second Law (F=ma)]], if $\sum \vec{F} = 0$, then $a = 0$, meaning velocity is constant (including zero). This is the mathematical basis of the First Law.

**Conditions / 适用条件:**
- The object must be viewed from an **inertial reference frame** (non-accelerating frame).
- All forces (including friction, air resistance, etc.) must be considered.
- The law applies to both stationary objects and objects moving at constant velocity.

> 📷 **IMAGE PROMPT — N1L-02: Equilibrium Diagram**
>
> **English Prompt:**
> A free-body diagram of a book resting on a table. Two arrows: upward normal force (N) and downward weight (W), equal in length. Below: a car moving at constant velocity on a straight road, with forward driving force (F_drive) and backward friction (F_friction) equal in length. Labels: "Net force = 0 → Equilibrium" on both. Clean vector style, pastel colours, textbook layout.
>
> **中文描述:**
> 一本书放在桌子上的受力分析图。两个箭头：向上的法向力 (N) 和向下的重力 (W)，长度相等。下方：一辆汽车在直路上匀速行驶，向前的驱动力 (F_drive) 和向后的摩擦力 (F_friction) 长度相等。标签：两者都标注“净力 = 0 → 平衡”。干净矢量风格，柔和色彩，教科书布局。
>
> **Labels Required / 需要标注:**
> * N (normal force / 法向力)
> * W (weight / 重力)
> * F_drive (driving force / 驱动力)
> * F_friction (friction / 摩擦力)
> * "Net force = 0 → Equilibrium" / "净力 = 0 → 平衡"
>
> **Style / 风格:** Textbook vector, clean
>
> **Exam Relevance / 考试关联:**
> Essential for drawing free-body diagrams in equilibrium problems.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — N1L-03: Inertia in a Car Crash**
>
> **English Prompt:**
> A photorealistic side-view of a car crash test dummy inside a car that suddenly stops. The dummy continues moving forward (due to inertia) while the car has stopped. Labels: "Inertia keeps dummy moving forward" and "Car stops due to external force (wall)". Seatbelt shown restraining the dummy. Dramatic lighting, slow-motion effect, crash test laboratory setting. Style: photorealistic, cinematic.
>
> **中文描述:**
> 汽车碰撞测试假人在突然停下的汽车内的逼真侧视图。假人因惯性继续向前运动，而汽车已停止。标签：“惯性使假人继续向前运动”和“汽车因外力（墙壁）停止”。显示安全带约束假人。戏剧性灯光，慢动作效果，碰撞测试实验室环境。风格：逼真，电影感。
>
> **Labels Required / 需要标注:**
> * "Inertia keeps dummy moving forward" / "惯性使假人继续向前运动"
> * "Car stops due to external force (wall)" / "汽车因外力（墙壁）停止"
> * Seatbelt / 安全带
>
> **Style / 风格:** Photorealistic, cinematic
>
> **Exam Relevance / 考试关联:**
> Real-world application of inertia — common in exam questions about safety features.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A 1500 kg car is travelling at 20 m/s on a straight, horizontal road. The driver sees a red light and applies the brakes, causing a constant braking force of 6000 N. Using Newton's First Law, explain why the car continues to move forward after the brakes are applied, and calculate the deceleration of the car.

**中文:**
一辆1500 kg的汽车在平直水平道路上以20 m/s的速度行驶。司机看到红灯后刹车，产生6000 N的恒定制动力。利用牛顿第一定律解释为什么刹车后汽车继续向前运动，并计算汽车的减速度。

### Solution / 解答

**Step 1: Apply Newton's First Law / 应用牛顿第一定律**
- Before braking: The car is in uniform motion (constant velocity). According to Newton's First Law, it will continue moving at 20 m/s unless a net external force acts on it.
- When brakes are applied: The braking force is an external force that changes the car's motion. However, due to **inertia**, the car resists this change and continues moving forward while decelerating.

**Step 2: Calculate deceleration / 计算减速度**
Using [[Newton's Second Law (F=ma)]]:
$$ F = ma $$
$$ 6000 = 1500 \times a $$
$$ a = \frac{6000}{1500} = 4 \, \text{m/s}^2 $$

The deceleration is 4 m/s² (negative acceleration).

**Step 3: Interpret / 解释**
The car continues forward because its inertia (mass) resists the change in motion. The braking force provides the net external force needed to overcome this inertia and slow the car down.

### Final Answer / 最终答案
**Answer:** The car continues forward due to inertia (Newton's First Law). Deceleration = 4 m/s².
**答案:** 汽车因惯性（牛顿第一定律）继续向前运动。减速度 = 4 m/s²。

### Quick Tip / 提示
**EN:** In exam questions, always mention "inertia" when explaining why an object continues moving despite a force acting on it. Use the phrase "resists change in motion."
**CN:** 在考试题目中，解释物体在受力时为何继续运动时，一定要提到“惯性”。使用“抵抗运动状态改变”这一表述。

---

# 7. Flashcards / 闪卡

**Q (EN):** State Newton's First Law of Motion.
**Q (CN):** 陈述牛顿第一运动定律。
**A (EN):** Every object continues in its state of rest or uniform motion in a straight line unless acted upon by a resultant external force.
**A (CN):** 每个物体都保持静止或匀速直线运动状态，除非受到净外力的作用。

---

**Q (EN):** What is inertia, and what property of an object determines its inertia?
**Q (CN):** 什么是惯性？物体的什么属性决定其惯性大小？
**A (EN):** Inertia is the property of an object that resists changes to its state of motion. It is determined by the object's mass — larger mass means greater inertia.
**A (CN):** 惯性是物体抵抗运动状态改变的性质。它由物体的质量决定——质量越大，惯性越大。

---

**Q (EN):** A book is resting on a table. According to Newton's First Law, why does it remain at rest?
**Q (CN):** 一本书放在桌子上。根据牛顿第一定律，它为什么保持静止？
**A (EN):** The net force on the book is zero (weight downward equals normal force upward), so it remains at rest due to inertia.
**A (CN):** 书上的净力为零（向下的重力等于向上的法向力），因此由于惯性而保持静止。

---

**Q (EN):** What is the condition for an object to be in equilibrium?
**Q (CN):** 物体处于平衡状态的条件是什么？
**A (EN):** The net (resultant) force acting on the object must be zero: $\sum \vec{F} = 0$.
**A (CN):** 作用在物体上的净（合）力必须为零：$\sum \vec{F} = 0$。

---

**Q (EN):** A car is moving at constant velocity on a straight road. Is it in equilibrium? Explain.
**Q (CN):** 一辆汽车在直路上匀速行驶。它处于平衡状态吗？解释原因。
**A (EN):)** Yes, it is in equilibrium because the net force is zero — the driving force equals the frictional force, so there is no acceleration.
**A (CN):** 是的，它处于平衡状态，因为净力为零——驱动力等于摩擦力，所以没有加速度。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Newton's First Law (Inertia)
  cn: 牛顿第一定律（惯性）
parent_topic: Newton's Laws of Motion
parent_hub: "[[Newton's Laws of Motion]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Newton's Second Law (F=ma)]]"
  - "[[Newton's Third Law (Action-Reaction)]]"
  - "[[Applications of Newton's Laws]]"
  - "[[Free-body Diagrams]]"
  - "[[Linear Momentum and Impulse]]"
language: bilingual_en_cn