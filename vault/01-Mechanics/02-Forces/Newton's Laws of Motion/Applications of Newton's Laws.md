# Applications of Newton's Laws / 牛顿定律的应用

---

## 1. Overview / 概述

**English:**
This sub-topic explores how Newton's three laws of motion are applied to solve real-world physics problems. Building on [[Newton's Second Law (F=ma)]] and [[Newton's Third Law (Action-Reaction)]], we examine systems involving connected bodies, pulleys, inclined planes, and tension forces. Understanding these applications is essential for analyzing dynamics problems in mechanics — from simple lifts to complex Atwood machines. The key skill is translating physical situations into mathematical equations using [[Free-body Diagrams]].

**中文:**
本子知识点探讨如何将牛顿三定律应用于解决实际物理问题。基于[[牛顿第二定律 (F=ma)]]和[[牛顿第三定律 (作用力与反作用力)]]，我们研究涉及连接体、滑轮、斜面和张力力的系统。理解这些应用对于分析力学中的动力学问题至关重要——从简单的电梯到复杂的阿特伍德机。关键技能是使用[[受力分析图]]将物理情境转化为数学方程。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Connected Bodies** / 连接体 | Two or more objects linked by strings, rods, or direct contact, moving together as a system. | 两个或多个通过绳子、杆或直接接触连接的物体，作为一个系统一起运动。 |
| **Tension** / 张力 | The pulling force transmitted through a string, cable, or chain when it is taut. | 绳子、缆绳或链条拉紧时传递的拉力。 |
| **Normal Reaction** / 法向反作用力 | The perpendicular contact force exerted by a surface on an object resting on it. | 表面对放置在其上的物体施加的垂直接触力。 |
| **Resultant Force** / 合力 | The single force that produces the same effect as all forces acting on an object combined. | 与作用在物体上的所有力组合效果相同的单一力。 |
| **System Approach** / 系统方法 | Treating multiple connected objects as a single entity to simplify force analysis. | 将多个连接物体视为一个整体以简化受力分析。 |

---

## 3. Key Concepts / 关键概念

**English:**

### 3.1 The System Approach
When analyzing connected bodies, we can either:
- **Treat the whole system**: Apply $F = ma$ to all objects together, ignoring internal forces (like tension between them).
- **Analyze individual objects**: Apply $F = ma$ to each object separately, including internal forces.

The choice depends on what we need to find. For acceleration of the whole system, use the system approach. For tension or contact forces, analyze individual objects.

### 3.2 Common Scenarios

**Scenario A: Two masses connected by a string over a pulley (Atwood machine)**
- The lighter mass accelerates upward, the heavier mass accelerates downward.
- Tension is the same throughout the string (assuming massless, inextensible string).
- Acceleration is the same magnitude for both masses.

**Scenario B: Object on a rough inclined plane**
- Resolve weight into components parallel ($mg\sin\theta$) and perpendicular ($mg\cos\theta$) to the plane.
- Friction opposes motion: $F_f = \mu R$ where $R = mg\cos\theta$.
- Net force down the plane: $F_{net} = mg\sin\theta - F_f$.

**Scenario C: Lift (elevator) problems**
- Apparent weight = normal reaction force.
- When accelerating upward: $R - mg = ma$ → $R = m(g+a)$ (heavier feeling).
- When accelerating downward: $mg - R = ma$ → $R = m(g-a)$ (lighter feeling).
- In free fall ($a=g$): $R=0$ → weightlessness.

### 3.3 Common Pitfalls
- **Forgetting direction**: Always define a positive direction and stick to it.
- **Mixing up action-reaction pairs**: Tension on mass A and tension on mass B are NOT an action-reaction pair — they are the same force transmitted through the string.
- **Ignoring friction**: On inclined planes, always check if friction is present.
- **Assuming massless strings**: In A-Level problems, strings are usually assumed massless and inextensible.

**中文:**

### 3.1 系统方法
分析连接体时，我们可以：
- **整体分析**：对所有物体一起应用 $F = ma$，忽略内力（如它们之间的张力）。
- **逐个分析**：对每个物体分别应用 $F = ma$，包括内力。

选择取决于我们需要求什么。求整个系统的加速度时使用系统方法。求张力或接触力时，逐个分析物体。

### 3.2 常见场景

**场景A：通过滑轮用绳子连接的两个质量（阿特伍德机）**
- 较轻的质量向上加速，较重的质量向下加速。
- 绳子中的张力处处相等（假设绳子无质量、不可伸长）。
- 两个质量的加速度大小相等。

**场景B：粗糙斜面上的物体**
- 将重力分解为平行于斜面（$mg\sin\theta$）和垂直于斜面（$mg\cos\theta$）的分量。
- 摩擦力阻碍运动：$F_f = \mu R$，其中 $R = mg\cos\theta$。
- 沿斜面向下的合力：$F_{net} = mg\sin\theta - F_f$。

**场景C：电梯问题**
- 表观重量 = 法向反作用力。
- 向上加速时：$R - mg = ma$ → $R = m(g+a)$（感觉更重）。
- 向下加速时：$mg - R = ma$ → $R = m(g-a)$（感觉更轻）。
- 自由落体时（$a=g$）：$R=0$ → 失重。

### 3.3 常见错误
- **忘记方向**：始终定义正方向并保持一致。
- **混淆作用力与反作用力对**：质量A上的张力和质量B上的张力不是作用力与反作用力对——它们是通过绳子传递的同一个力。
- **忽略摩擦力**：在斜面上，始终检查是否存在摩擦力。
- **假设绳子无质量**：在A-Level问题中，通常假设绳子无质量且不可伸长。

---

## 4. Formulas / 公式

### Key Formula 1: Newton's Second Law for a System

$$ F_{net} = m_{total} \times a $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F_{net}$ | Net external force on the system | 系统所受合外力 | N |
| $m_{total}$ | Total mass of all objects | 所有物体的总质量 | kg |
| $a$ | Acceleration of the system | 系统的加速度 | m/s² |

### Key Formula 2: Object on an Inclined Plane

$$ F_{parallel} = mg\sin\theta $$
$$ F_{perpendicular} = mg\cos\theta $$
$$ F_{friction} = \mu R = \mu mg\cos\theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\theta$ | Angle of incline | 斜面角度 | ° or rad |
| $\mu$ | Coefficient of friction | 摩擦系数 | dimensionless |
| $R$ | Normal reaction force | 法向反作用力 | N |

### Key Formula 3: Lift (Elevator) Problems

$$ R = m(g \pm a) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $R$ | Apparent weight (normal reaction) | 表观重量（法向反作用力） | N |
| $g$ | Acceleration due to gravity | 重力加速度 | m/s² |
| $a$ | Acceleration of lift | 电梯的加速度 | m/s² |

**Derivation / 推导:**
For upward acceleration: $R - mg = ma$ → $R = m(g + a)$
For downward acceleration: $mg - R = ma$ → $R = m(g - a)$

**Conditions / 适用条件:**
- Strings are massless and inextensible
- Pulleys are frictionless and massless
- Air resistance is neglected unless stated

> 📷 **IMAGE PROMPT — F01: Atwood Machine Free-Body Diagram**
>
> **English Prompt:**
> A clean textbook-style vector diagram showing an Atwood machine: two masses (m₁ and m₂, with m₂ > m₁) connected by a string passing over a frictionless pulley at the top. Include free-body diagrams for each mass: m₁ has upward tension T and downward weight m₁g; m₂ has upward tension T and downward weight m₂g. Arrows should be labeled with force names and magnitudes. The acceleration direction should be indicated: m₁ upward, m₂ downward. Use a white background with blue and red arrows. Include a small note: "Tension T is the same throughout the string."
>
> **中文描述:**
> 一个干净的教科书式矢量图，展示阿特伍德机：两个质量（m₁和m₂，m₂ > m₁）通过绳子连接，绳子绕过顶部的无摩擦滑轮。包括每个质量的受力分析图：m₁受到向上的张力T和向下的重力m₁g；m₂受到向上的张力T和向下的重力m₂g。箭头应标注力名称和大小。应标明加速度方向：m₁向上，m₂向下。使用白色背景，蓝色和红色箭头。包含小注："张力T在绳子中处处相等。"
>
> **Labels Required / 需要标注:**
> * m₁, m₂ (masses)
> * T (tension arrows on both masses)
> * m₁g, m₂g (weight arrows)
> * a (acceleration direction for each mass)
> * "Frictionless pulley" label
>
> **Style / 风格:** Textbook vector / clean diagram
>
> **Exam Relevance / 考试关联:**
> This is the most common setup for connected bodies problems in A-Level exams. Understanding the free-body diagrams is essential for writing correct equations.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — F02: Inclined Plane with Connected Masses**
>
> **English Prompt:**
> A detailed 3D-rendered diagram showing a physics setup: a mass m₁ on a rough inclined plane (angle θ = 30°) connected by a string over a pulley at the top of the incline to a hanging mass m₂. Include force arrows on m₁: weight mg resolved into components mg sinθ (parallel, down the plane) and mg cosθ (perpendicular, into the plane), normal reaction R (perpendicular, out of the plane), tension T (up the plane), and friction F_f (down the plane, opposing motion). On m₂: tension T (upward) and weight m₂g (downward). Use a warm color palette with clear labels. The background should be a simple classroom or lab setting.
>
> **中文描述:**
> 一个详细的3D渲染图，展示物理设置：粗糙斜面上的质量m₁（角度θ = 30°）通过绳子连接，绳子绕过斜面顶部的滑轮连接到悬挂的质量m₂。在m₁上包含力箭头：重力mg分解为平行分量mg sinθ（沿斜面向下）和垂直分量mg cosθ（垂直进入斜面），法向反作用力R（垂直离开斜面），张力T（沿斜面向上），摩擦力F_f（沿斜面向下，阻碍运动）。在m₂上：张力T（向上）和重力m₂g（向下）。使用暖色调，清晰标注。背景为简单的教室或实验室环境。
>
> **Labels Required / 需要标注:**
> * m₁, m₂
> * θ = 30°
> * mg sinθ, mg cosθ, R, T, F_f on m₁
> * T, m₂g on m₂
> * Direction of acceleration a
>
> **Style / 风格:** 3D render / educational illustration
>
> **Exam Relevance / 考试关联:**
> This combined inclined-plane-and-pulley setup appears frequently in exam questions testing both resolution of forces and connected bodies analysis.

---

## 6. Worked Example / 典型例题

### Example 1: Atwood Machine

### Question / 题目
**English:**
Two masses, 3.0 kg and 5.0 kg, are connected by a light inextensible string passing over a frictionless pulley. The system is released from rest. Calculate:
(a) The acceleration of the system.
(b) The tension in the string.
Take $g = 9.81 \text{ m/s}^2$.

**中文:**
两个质量分别为3.0 kg和5.0 kg的物体，通过一根轻质不可伸长的绳子连接，绳子绕过无摩擦滑轮。系统从静止释放。计算：
(a) 系统的加速度。
(b) 绳子中的张力。
取 $g = 9.81 \text{ m/s}^2$。

### Solution / 解答

**Step 1: Define positive direction**
Let positive direction be the direction of motion: 5.0 kg mass moving downward, 3.0 kg mass moving upward.

**Step 2: System approach for acceleration**
For the whole system:
- Net force = weight of 5.0 kg - weight of 3.0 kg
- $F_{net} = m_2g - m_1g = (5.0 - 3.0) \times 9.81 = 19.62 \text{ N}$
- Total mass = $5.0 + 3.0 = 8.0 \text{ kg}$
- Using $F_{net} = m_{total}a$:
  $$ a = \frac{F_{net}}{m_{total}} = \frac{19.62}{8.0} = 2.45 \text{ m/s}^2 $$

**Step 3: Individual analysis for tension**
Consider the 3.0 kg mass (moving upward):
$$ T - m_1g = m_1a $$
$$ T = m_1(g + a) = 3.0 \times (9.81 + 2.45) = 36.78 \text{ N} $$

Check with the 5.0 kg mass (moving downward):
$$ m_2g - T = m_2a $$
$$ T = m_2(g - a) = 5.0 \times (9.81 - 2.45) = 36.80 \text{ N} $$
(Slight rounding difference — consistent.)

### Final Answer / 最终答案
**Answer:** (a) $a = 2.45 \text{ m/s}^2$ (b) $T = 36.8 \text{ N}$
**答案:** (a) $a = 2.45 \text{ m/s}^2$ (b) $T = 36.8 \text{ N}$

### Quick Tip / 提示
Always check your tension by using the other mass — if they don't match, you've made an error. The system approach gives acceleration quickly, but you must analyze individual objects to find tension.

---

### Example 2: Object on an Inclined Plane

### Question / 题目
**English:**
A 2.0 kg block is placed on a rough plane inclined at 25° to the horizontal. The coefficient of friction between the block and the plane is 0.30. The block is released from rest. Calculate the acceleration of the block down the plane. Take $g = 9.81 \text{ m/s}^2$.

**中文:**
一个2.0 kg的物块放置在粗糙斜面上，斜面与水平面成25°角。物块与斜面之间的摩擦系数为0.30。物块从静止释放。计算物块沿斜面下滑的加速度。取 $g = 9.81 \text{ m/s}^2$。

### Solution / 解答

**Step 1: Resolve forces**
Weight component down the plane: $mg\sin\theta = 2.0 \times 9.81 \times \sin 25° = 8.29 \text{ N}$
Normal reaction: $R = mg\cos\theta = 2.0 \times 9.81 \times \cos 25° = 17.78 \text{ N}$
Friction force: $F_f = \mu R = 0.30 \times 17.78 = 5.33 \text{ N}$

**Step 2: Apply Newton's Second Law**
Net force down the plane: $F_{net} = mg\sin\theta - F_f = 8.29 - 5.33 = 2.96 \text{ N}$
$$ a = \frac{F_{net}}{m} = \frac{2.96}{2.0} = 1.48 \text{ m/s}^2 $$

### Final Answer / 最终答案
**Answer:** $a = 1.48 \text{ m/s}^2$ down the plane
**答案:** $a = 1.48 \text{ m/s}^2$ 沿斜面向下

### Quick Tip / 提示
Always resolve weight into components parallel and perpendicular to the plane. The normal reaction is $mg\cos\theta$, not $mg$ — a common mistake!

---

## 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): What is the system approach in connected bodies problems?
Q (CN): 连接体问题中的系统方法是什么？
A (EN): Treating all connected objects as a single system, applying F = ma to the total mass with only external forces, ignoring internal forces like tension.
A (CN): 将所有连接物体视为一个系统，对总质量应用F = ma，只考虑外力，忽略张力等内力。

**Flashcard 2**
Q (EN): How do you find tension in a string connecting two masses over a pulley?
Q (CN): 如何求通过滑轮连接两个质量的绳子中的张力？
A (EN): Analyze one mass individually using F = ma. For the lighter mass moving up: T - mg = ma. For the heavier mass moving down: mg - T = ma. Solve for T.
A (CN): 对其中一个质量单独应用F = ma。对于向上运动的较轻质量：T - mg = ma。对于向下运动的较重质量：mg - T = ma。解出T。

**Flashcard 3**
Q (EN): What is the apparent weight of a person in a lift accelerating upward?
Q (CN): 在向上加速的电梯中，人的表观重量是多少？
A (EN): R = m(g + a), where R is the normal reaction (apparent weight), m is mass, g is gravity, a is upward acceleration. The person feels heavier.
A (CN): R = m(g + a)，其中R是法向反作用力（表观重量），m是质量，g是重力加速度，a是向上加速度。人感觉更重。

**Flashcard 4**
Q (EN): How do you resolve weight on an inclined plane?
Q (CN): 如何在斜面上分解重力？
A (EN): Weight mg is resolved into: mg sinθ parallel to the plane (downward) and mg cosθ perpendicular to the plane (into the plane). The normal reaction R = mg cosθ.
A (CN): 重力mg分解为：平行于斜面的mg sinθ（向下）和垂直于斜面的mg cosθ（进入斜面）。法向反作用力R = mg cosθ。

**Flashcard 5**
Q (EN): What happens to apparent weight in a freely falling lift?
Q (CN): 在自由落体的电梯中，表观重量会发生什么变化？
A (EN): R = m(g - a) = m(g - g) = 0. The person experiences weightlessness because the normal reaction is zero.
A (CN): R = m(g - a) = m(g - g) = 0。人经历失重，因为法向反作用力为零。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Applications of Newton's Laws
  cn: 牛顿定律的应用
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
  - "[[Newton's First Law (Inertia)]]"
  - "[[Newton's Second Law (F=ma)]]"
  - "[[Newton's Third Law (Action-Reaction)]]"
  - "[[Free-body Diagrams]]"
  - "[[Linear Momentum and Impulse]]"
  - "[[Conservation of Momentum]]"
language: bilingual_en_cn