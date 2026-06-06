# 1. Overview / 概述

**English:**
Linear momentum is a fundamental concept in physics that quantifies the "quantity of motion" possessed by an object. It combines both the mass and velocity of an object into a single vector quantity, making it essential for analyzing collisions, explosions, and interactions between objects. This sub-topic introduces the definition of linear momentum, its vector nature, and its relationship to [[Newton's Laws of Motion]].

Understanding momentum is crucial because it forms the foundation for the [[Impulse-Momentum Theorem]] and the [[Conservation of Momentum]] principle. Unlike kinetic energy, momentum is always conserved in isolated systems, making it a powerful tool for solving problems involving collisions and interactions. This concept bridges Newtonian mechanics with more advanced topics in physics.

**中文:**
线性动量是物理学中一个基本概念，它量化了物体所具有的"运动量"。它将物体的质量和速度结合成一个矢量量，对于分析碰撞、爆炸和物体之间的相互作用至关重要。本子知识点介绍线性动量的定义、矢量性质及其与[[牛顿运动定律]]的关系。

理解动量至关重要，因为它构成了[[冲量-动量定理]]和[[动量守恒定律]]的基础。与动能不同，动量在孤立系统中总是守恒的，这使其成为解决碰撞和相互作用问题的有力工具。这个概念将牛顿力学与物理学中更高级的主题联系起来。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Linear Momentum** / 线性动量 | The product of an object's mass and its velocity; a vector quantity with the same direction as the velocity. | 物体质量与其速度的乘积；矢量，方向与速度方向相同。 |
| **Momentum** / 动量 | A measure of the quantity of motion of a moving body, given by mass × velocity. | 运动物体运动量的度量，由质量×速度给出。 |
| **Vector Quantity** / 矢量 | A physical quantity that has both magnitude and direction. | 既有大小又有方向的物理量。 |
| **Scalar Quantity** / 标量 | A physical quantity that has magnitude only, with no direction. | 只有大小没有方向的物理量。 |
| **Inertia** / 惯性 | The tendency of an object to resist changes in its state of motion; related to mass. | 物体抵抗运动状态变化的趋势；与质量有关。 |
| **System** / 系统 | A defined collection of objects under consideration for analysis. | 为分析而定义的物体集合。 |

---

# 3. Key Concepts / 关键概念

**English:**
Linear momentum $\vec{p}$ is defined as the product of an object's mass $m$ and its velocity $\vec{v}$:

$$\vec{p} = m\vec{v}$$

**Key points to understand:**

1. **Vector Nature**: Momentum is a vector quantity, meaning it has both magnitude and direction. The direction of momentum is always the same as the direction of velocity. This is crucial when analyzing collisions — momentum in opposite directions must be assigned opposite signs.

2. **Relationship to Newton's Laws**: Momentum is deeply connected to [[Newton's Laws of Motion]]. Newton's Second Law can be expressed in terms of momentum: the net force acting on an object equals the rate of change of its momentum. This is actually Newton's original formulation of the law.

3. **Mass vs. Velocity**: Both mass and velocity contribute equally to momentum. A heavy object moving slowly can have the same momentum as a light object moving fast. For example, a truck (2000 kg) moving at 5 m/s has the same momentum as a car (1000 kg) moving at 10 m/s.

4. **Conservation Context**: Momentum is a conserved quantity in isolated systems (no external forces). This makes it invaluable for analyzing collisions and explosions, as explored in [[Conservation of Momentum]].

5. **Common Pitfalls**:
   - Forgetting that momentum is a vector — direction matters!
   - Confusing momentum with kinetic energy (momentum is a vector, kinetic energy is a scalar)
   - Using speed instead of velocity in calculations
   - Forgetting to convert units (mass must be in kg, velocity in m/s)

**中文:**
线性动量 $\vec{p}$ 定义为物体质量 $m$ 与其速度 $\vec{v}$ 的乘积：

$$\vec{p} = m\vec{v}$$

**关键理解点：**

1. **矢量性质**：动量是矢量，既有大小又有方向。动量的方向始终与速度方向相同。这在分析碰撞时至关重要——相反方向的动量必须赋予相反的符号。

2. **与牛顿定律的关系**：动量与[[牛顿运动定律]]密切相关。牛顿第二定律可以用动量表示：作用在物体上的净力等于其动量的变化率。这实际上是牛顿对该定律的原始表述。

3. **质量与速度**：质量和速度对动量的贡献同等重要。缓慢移动的重物可以与快速移动的轻物具有相同的动量。例如，卡车（2000 kg）以5 m/s运动与汽车（1000 kg）以10 m/s运动具有相同的动量。

4. **守恒背景**：动量在孤立系统（无外力）中是守恒量。这使得它对于分析碰撞和爆炸非常宝贵，详见[[动量守恒定律]]。

5. **常见陷阱**：
   - 忘记动量是矢量——方向很重要！
   - 混淆动量和动能（动量是矢量，动能是标量）
   - 在计算中使用速率而不是速度
   - 忘记单位换算（质量必须用kg，速度用m/s）

---

# 4. Formulas / 公式

## Primary Formula / 主要公式

$$\vec{p} = m\vec{v}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{p}$ | Linear momentum | 线性动量 | kg·m/s |
| $m$ | Mass | 质量 | kg |
| $\vec{v}$ | Velocity | 速度 | m/s |

## Alternative Form / 替代形式

For magnitude only (when direction is not needed):

$$p = mv$$

Where $p$ is the magnitude of momentum, $m$ is mass, and $v$ is speed.

## Newton's Second Law in Momentum Form / 牛顿第二定律的动量形式

$$\vec{F} = \frac{d\vec{p}}{dt}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{F}$ | Net force | 净力 | N |
| $\frac{d\vec{p}}{dt}$ | Rate of change of momentum | 动量变化率 | kg·m/s² |

**Derivation / 推导:**
Starting from Newton's Second Law: $\vec{F} = m\vec{a}$
Since $\vec{a} = \frac{d\vec{v}}{dt}$:
$\vec{F} = m\frac{d\vec{v}}{dt} = \frac{d(m\vec{v})}{dt} = \frac{d\vec{p}}{dt}$

**Conditions / 适用条件:**
- The formula $\vec{p} = m\vec{v}$ applies to all objects with mass and velocity
- For objects moving at relativistic speeds (near speed of light), relativistic momentum must be used
- The momentum form of Newton's Second Law applies when mass is constant (for variable mass systems, a more general form is needed)

> 📷 **IMAGE PROMPT — MOM-001: Momentum Vector Diagram**
>
> **English Prompt:**
> A clean educational vector diagram showing two objects with different masses and velocities but equal momentum. Left side: a large truck (2000 kg) moving right at 5 m/s with a large momentum vector arrow labeled "p = 10,000 kg·m/s". Right side: a small car (1000 kg) moving right at 10 m/s with an equally large momentum vector arrow labeled "p = 10,000 kg·m/s". Both momentum arrows should be the same length. Include mass and velocity labels on each object. Use a white background with blue and red color scheme. Textbook style, 2D side view.
>
> **中文描述:**
> 一个清晰的教育矢量图，显示两个质量和速度不同但动量相等的物体。左侧：一辆大卡车（2000 kg）以5 m/s向右运动，带有一个大的动量矢量箭头，标注"p = 10,000 kg·m/s"。右侧：一辆小汽车（1000 kg）以10 m/s向右运动，带有一个同样大的动量矢量箭头，标注"p = 10,000 kg·m/s"。两个动量箭头长度相同。每个物体上标注质量和速度。使用白色背景，蓝红色配色方案。教科书风格，2D侧视图。
>
> **Labels Required / 需要标注:**
> * Truck: m = 2000 kg, v = 5 m/s
> * Car: m = 1000 kg, v = 10 m/s
> * Both: p = 10,000 kg·m/s (arrows of equal length)
>
> **Style / 风格:** Textbook vector diagram, 2D side view
>
> **Exam Relevance / 考试关联:**
> This diagram helps students understand that momentum depends on both mass and velocity, and that different combinations can yield the same momentum value.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — MOM-002: Momentum Direction and Sign Convention**
>
> **English Prompt:**
> A 2D educational diagram showing a horizontal line with a ball moving to the right (positive direction) and another ball moving to the left (negative direction). Each ball has a momentum vector arrow. The right-moving ball has a red arrow pointing right labeled "p = +mv" and the left-moving ball has a blue arrow pointing left labeled "p = -mv". Include a coordinate axis at the bottom showing positive x-direction to the right. Clean white background, textbook style. Include a small note box: "Momentum is a vector — direction matters!"
>
> **中文描述:**
> 一个2D教育图，显示一条水平线，一个球向右运动（正方向），另一个球向左运动（负方向）。每个球都有一个动量矢量箭头。向右运动的球有一个指向右的红色箭头，标注"p = +mv"；向左运动的球有一个指向左的蓝色箭头，标注"p = -mv"。底部包含一个坐标轴，显示正x方向向右。干净的白色背景，教科书风格。包含一个小注释框："动量是矢量——方向很重要！"
>
> **Labels Required / 需要标注:**
> * Right-moving ball: p = +mv (red arrow)
> * Left-moving ball: p = -mv (blue arrow)
> * Coordinate axis with +x direction
>
> **Style / 风格:** Textbook vector diagram, 2D
>
> **Exam Relevance / 考试关联:**
> Essential for understanding sign conventions in momentum problems, especially when calculating total momentum of a system with objects moving in opposite directions.

---

# 6. Worked Example / 典型例题

## Example 1: Basic Momentum Calculation / 例题1：基本动量计算

### Question / 题目
**English:**
A cricket ball of mass 160 g is bowled at a speed of 30 m/s towards a batsman. Calculate the momentum of the ball.

**中文:**
一个质量为160克的板球以30 m/s的速度向击球手投出。计算球的动量。

### Solution / 解答

**Step 1: Convert units / 步骤1：单位换算**
Mass must be in kg:
$$m = 160 \text{ g} = 0.160 \text{ kg}$$

**Step 2: Apply momentum formula / 步骤2：应用动量公式**
$$p = mv$$
$$p = 0.160 \times 30$$
$$p = 4.8 \text{ kg·m/s}$$

**Step 3: State direction / 步骤3：说明方向**
The momentum is directed towards the batsman (in the direction of motion).

### Final Answer / 最终答案
**Answer:** $p = 4.8 \text{ kg·m/s}$ towards the batsman
**答案:** $p = 4.8 \text{ kg·m/s}$，方向朝向击球手

### Quick Tip / 提示
Always convert mass to kilograms before calculating momentum. A common mistake is to leave mass in grams, which gives an answer 1000 times too small.

---

## Example 2: Comparing Momenta / 例题2：比较动量

### Question / 题目
**English:**
A car of mass 1200 kg travels at 15 m/s. A motorcycle of mass 200 kg travels at 90 m/s. Which has greater momentum?

**中文:**
一辆质量为1200 kg的汽车以15 m/s行驶。一辆质量为200 kg的摩托车以90 m/s行驶。哪个动量更大？

### Solution / 解答

**Step 1: Calculate car's momentum / 步骤1：计算汽车的动量**
$$p_{\text{car}} = m_{\text{car}} \times v_{\text{car}}$$
$$p_{\text{car}} = 1200 \times 15 = 18,000 \text{ kg·m/s}$$

**Step 2: Calculate motorcycle's momentum / 步骤2：计算摩托车的动量**
$$p_{\text{motorcycle}} = m_{\text{motorcycle}} \times v_{\text{motorcycle}}$$
$$p_{\text{motorcycle}} = 200 \times 90 = 18,000 \text{ kg·m/s}$$

**Step 3: Compare / 步骤3：比较**
Both have the same momentum: 18,000 kg·m/s.

### Final Answer / 最终答案
**Answer:** Both have equal momentum (18,000 kg·m/s)
**答案:** 两者动量相等（18,000 kg·m/s）

### Quick Tip / 提示
This example shows that momentum depends on both mass and velocity. A lighter object can have the same momentum as a heavier object if it moves faster. This is why a small bullet can have significant momentum despite its small mass.

---

# 7. Flashcards / 闪卡

---

**Q (EN):** What is the definition of linear momentum?
**Q (CN):** 线性动量的定义是什么？
**A (EN):** Linear momentum is the product of an object's mass and its velocity. It is a vector quantity given by p = mv, with direction same as velocity.
**A (CN):** 线性动量是物体质量与其速度的乘积。它是矢量，由p = mv给出，方向与速度方向相同。

---

**Q (EN):** What are the SI units of momentum?
**Q (CN):** 动量的SI单位是什么？
**A (EN):** kg·m/s (kilogram meters per second). It can also be expressed as N·s (newton seconds).
**A (CN):** kg·m/s（千克米每秒）。也可以表示为N·s（牛顿秒）。

---

**Q (EN):** Is momentum a scalar or vector quantity? Why does this matter?
**Q (CN):** 动量是标量还是矢量？为什么这很重要？
**A (EN):)** Momentum is a vector quantity. This matters because when calculating total momentum of a system, we must consider direction — momenta in opposite directions have opposite signs.
**A (CN):** 动量是矢量。这很重要，因为计算系统总动量时必须考虑方向——相反方向的动量具有相反的符号。

---

**Q (EN):** How is momentum related to Newton's Second Law?
**Q (CN):** 动量与牛顿第二定律有何关系？
**A (EN):** Newton's Second Law can be written as F = dp/dt, meaning the net force equals the rate of change of momentum. This is Newton's original formulation.
**A (CN):** 牛顿第二定律可以写成F = dp/dt，意味着净力等于动量变化率。这是牛顿的原始表述。

---

**Q (EN):** A 50 g tennis ball travels at 40 m/s. What is its momentum?
**Q (CN):** 一个50克的网球以40 m/s运动。它的动量是多少？
**A (EN):** p = mv = 0.050 × 40 = 2.0 kg·m/s (Remember to convert 50 g to 0.050 kg!)
**A (CN):** p = mv = 0.050 × 40 = 2.0 kg·m/s（记得将50克转换为0.050千克！）

---

# 8. Metadata / 元数据

```yaml
title:
  en: Definition of Linear Momentum
  cn: 线性动量的定义
parent_topic: Linear Momentum and Impulse
parent_hub: "[[Linear Momentum and Impulse]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Impulse and Force-Time Graphs]]"
  - "[[Impulse-Momentum Theorem]]"
  - "[[Conservation of Momentum]]"
prerequisites:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn