# 1. Overview / 概述

**English:**
Inelastic collisions are a fundamental class of collisions where kinetic energy is NOT conserved, although total momentum is always conserved. This sub-topic explores the defining characteristics of inelastic collisions, the concept of "loss" of kinetic energy (which transforms into other forms like heat, sound, or deformation), and the special case of perfectly inelastic collisions where objects stick together after impact. Understanding inelastic collisions is crucial for analyzing real-world scenarios such as car crashes, clay ball impacts, and many everyday interactions where objects deform or generate heat. This builds directly on [[Linear Momentum and Impulse]] and contrasts with [[Elastic Collisions]] within the broader [[Conservation of Momentum]] topic.

**中文:**
非弹性碰撞是一类基本的碰撞类型，其中动能不守恒，但总动量始终守恒。本子知识点探讨非弹性碰撞的定义特征、动能"损失"的概念（转化为其他形式，如热能、声能或形变能），以及完全非弹性碰撞这一特殊情况——物体碰撞后粘在一起运动。理解非弹性碰撞对于分析现实世界中的场景至关重要，例如车祸、黏土球碰撞以及物体变形或产生热量的日常相互作用。这直接建立在[[Linear Momentum and Impulse]]的基础上，并与[[Conservation of Momentum]]主题中的[[Elastic Collisions]]形成对比。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Inelastic Collision** / 非弹性碰撞 | A collision in which kinetic energy is not conserved; some kinetic energy is transformed into other forms of energy (e.g., heat, sound, deformation). Total momentum is conserved. | 动能不守恒的碰撞；部分动能转化为其他形式的能量（如热能、声能、形变能）。总动量守恒。 |
| **Perfectly Inelastic Collision** / 完全非弹性碰撞 | A special type of inelastic collision where the colliding objects stick together and move with a common velocity after the collision. Maximum kinetic energy is lost. | 一种特殊的非弹性碰撞，碰撞物体粘在一起并以共同速度运动。动能损失最大。 |
| **Coefficient of Restitution ($e$)** / 恢复系数 | A measure of the "bounciness" of a collision; for inelastic collisions, $0 < e < 1$; for perfectly inelastic collisions, $e = 0$. | 衡量碰撞"弹性"程度的量；对于非弹性碰撞，$0 < e < 1$；对于完全非弹性碰撞，$e = 0$。 |
| **Kinetic Energy Loss** / 动能损失 | The amount of kinetic energy transformed into other forms during an inelastic collision, calculated as $\Delta KE = KE_{\text{after}} - KE_{\text{before}}$ (negative value). | 非弹性碰撞中转化为其他形式的动能数量，计算为 $\Delta KE = KE_{\text{after}} - KE_{\text{before}}$（负值）。 |
| **Deformation Energy** / 形变能 | The energy absorbed by objects as they permanently deform during an inelastic collision. | 物体在非弹性碰撞中因永久形变而吸收的能量。 |

---

# 3. Key Concepts / 关键概念

**English:**
The central idea of inelastic collisions is that while momentum is always conserved (as per [[Conservation of Momentum]]), kinetic energy is not. This is the key distinction from [[Elastic Collisions]].

**Step-by-step reasoning for analyzing an inelastic collision:**

1. **Identify the system:** Determine the objects involved and ensure no external forces act during the collision (or that they are negligible).
2. **Apply conservation of momentum:** Use $m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$ (for non-sticking) or $m_1 u_1 + m_2 u_2 = (m_1 + m_2) v$ (for perfectly inelastic).
3. **Calculate initial kinetic energy:** $KE_{\text{before}} = \frac{1}{2} m_1 u_1^2 + \frac{1}{2} m_2 u_2^2$
4. **Calculate final kinetic energy:** $KE_{\text{after}} = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2$
5. **Find the energy loss:** $\Delta KE = KE_{\text{after}} - KE_{\text{before}}$ (this will be negative)

**Physical interpretation:**
The "lost" kinetic energy is not destroyed but transformed. In a car crash, kinetic energy goes into:
- Deforming the metal (deformation energy)
- Generating heat (thermal energy)
- Creating sound waves (sound energy)
- Possibly breaking chemical bonds

**Common pitfalls:**
- ❌ **Assuming kinetic energy is conserved** — This is only true for elastic collisions.
- ❌ **Forgetting to square velocities** — Kinetic energy uses $v^2$, not $v$.
- ❌ **Using the wrong mass** — For perfectly inelastic collisions, the combined mass is $m_1 + m_2$.
- ❌ **Confusing momentum conservation with energy conservation** — Momentum is ALWAYS conserved in collisions (no external forces); energy is NOT always conserved.

**中文:**
非弹性碰撞的核心思想是：动量始终守恒（根据[[Conservation of Momentum]]），但动能不守恒。这是与[[Elastic Collisions]]的关键区别。

**分析非弹性碰撞的逐步推理：**

1. **确定系统：** 识别涉及的物体，确保碰撞过程中没有外力作用（或可忽略）。
2. **应用动量守恒：** 使用 $m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$（不粘在一起）或 $m_1 u_1 + m_2 u_2 = (m_1 + m_2) v$（完全非弹性）。
3. **计算初始动能：** $KE_{\text{before}} = \frac{1}{2} m_1 u_1^2 + \frac{1}{2} m_2 u_2^2$
4. **计算最终动能：** $KE_{\text{after}} = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2$
5. **求能量损失：** $\Delta KE = KE_{\text{after}} - KE_{\text{before}}$（结果为负值）

**物理意义：**
"损失"的动能并未被摧毁，而是转化为其他形式。在车祸中，动能转化为：
- 金属变形（形变能）
- 产生热量（热能）
- 产生声波（声能）
- 可能破坏化学键

**常见错误：**
- ❌ **假设动能守恒** — 这仅适用于弹性碰撞。
- ❌ **忘记对速度取平方** — 动能使用 $v^2$，不是 $v$。
- ❌ **使用错误的质量** — 对于完全非弹性碰撞，组合质量为 $m_1 + m_2$。
- ❌ **混淆动量守恒与能量守恒** — 动量在碰撞中始终守恒（无外力）；能量并非始终守恒。

---

# 4. Formulas / 公式

## Formula 1: Momentum Conservation (General Inelastic)

$$ m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $m_1, m_2$ | Masses of objects 1 and 2 | 物体1和2的质量 | kg |
| $u_1, u_2$ | Initial velocities before collision | 碰撞前的初始速度 | m/s |
| $v_1, v_2$ | Final velocities after collision | 碰撞后的最终速度 | m/s |

## Formula 2: Momentum Conservation (Perfectly Inelastic)

$$ m_1 u_1 + m_2 u_2 = (m_1 + m_2) v $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v$ | Common final velocity after sticking | 粘在一起后的共同最终速度 | m/s |

## Formula 3: Kinetic Energy Loss

$$ \Delta KE = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 - \left( \frac{1}{2} m_1 u_1^2 + \frac{1}{2} m_2 u_2^2 \right) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\Delta KE$ | Change in kinetic energy (negative for inelastic) | 动能变化（非弹性为负值） | J |

## Formula 4: Coefficient of Restitution

$$ e = \frac{v_2 - v_1}{u_1 - u_2} $$

For inelastic: $0 < e < 1$; For perfectly inelastic: $e = 0$

**Derivation / 推导:**
The coefficient of restitution is defined as the ratio of relative speed after collision to relative speed before collision. For perfectly inelastic collisions, $v_1 = v_2 = v$, so $e = \frac{v - v}{u_1 - u_2} = 0$.

**Conditions / 适用条件:**
- No external forces during collision (or negligible)
- For 1D collisions (for 2D, see [[Two-Dimensional Collisions]])
- Objects are point masses or rigid bodies (simplified model)

> 📷 **IMAGE PROMPT — F01: Perfectly Inelastic Collision Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a perfectly inelastic collision between two balls. Left side: Ball A (mass m₁, velocity u₁) moving right, Ball B (mass m₂, velocity u₂) moving left. Right side: A single combined ball (mass m₁+m₂) moving right with velocity v. Arrows indicate velocity vectors with labels. Below: Energy bar chart showing initial KE (two bars) and final KE (one smaller bar) with "Energy Lost" annotation showing transformation to heat and sound. White background, blue and red color scheme, clear labels in English.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，展示两个球之间的完全非弹性碰撞。左侧：球A（质量m₁，速度u₁）向右运动，球B（质量m₂，速度u₂）向左运动。右侧：一个组合球（质量m₁+m₂）以速度v向右运动。箭头表示速度矢量并带有标签。下方：能量条形图显示初始动能（两个条）和最终动能（一个较小的条），并标注"能量损失"显示转化为热量和声音。白色背景，蓝红色配色方案，清晰的英文标签。
>
> **Labels Required / 需要标注:**
> * Before collision / 碰撞前
> * After collision / 碰撞后
> * m₁, u₁ (Ball A)
> * m₂, u₂ (Ball B)
> * m₁+m₂, v (Combined)
> * KE lost → heat + sound / 动能损失 → 热量 + 声音
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for visualizing the key difference between before and after states in perfectly inelastic collisions, which is a common exam question type.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — F02: Kinetic Energy Distribution in Inelastic Collisions**
>
> **English Prompt:**
> A detailed infographic-style diagram comparing energy distribution in elastic vs. inelastic collisions. Left panel: Elastic collision — two balls bounce apart, energy bar chart shows KE₁ + KE₂ = KE₁' + KE₂' (equal total). Right panel: Inelastic collision — two balls deform and stick, energy bar chart shows KE₁ + KE₂ > KE₁+₂' with a portion labeled "Deformation Energy," "Heat," and "Sound." Color gradient from blue (KE) to red (lost energy). Arrows showing energy flow. Clean white background, professional textbook style, English labels.
>
> **中文描述:**
> 一个详细的信息图风格图表，比较弹性碰撞与非弹性碰撞中的能量分布。左侧面板：弹性碰撞——两个球弹开，能量条形图显示 KE₁ + KE₂ = KE₁' + KE₂'（总和相等）。右侧面板：非弹性碰撞——两个球变形并粘在一起，能量条形图显示 KE₁ + KE₂ > KE₁+₂'，一部分标注为"形变能"、"热量"和"声音"。颜色从蓝色（动能）渐变到红色（损失的能量）。箭头显示能量流动。干净的白色背景，专业教科书风格，英文标签。
>
> **Labels Required / 需要标注:**
> * Elastic Collision / 弹性碰撞
> * Inelastic Collision / 非弹性碰撞
> * Kinetic Energy (KE) / 动能
> * Deformation Energy / 形变能
> * Heat / 热量
> * Sound / 声音
> * Total Energy Conserved / 总能量守恒
>
> **Style / 风格:** Infographic / 信息图
>
> **Exam Relevance / 考试关联:**
> Helps students understand WHY kinetic energy is "lost" — it's transformed, not destroyed. This conceptual understanding is frequently tested in exam questions about energy conservation.

---

# 6. Worked Example / 典型例题

### Example 1: Perfectly Inelastic Collision

### Question / 题目
**English:**
A 2.0 kg clay ball moving at 6.0 m/s to the right collides head-on with a 4.0 kg clay ball moving at 2.0 m/s to the left. The balls stick together after the collision.

(a) Calculate the velocity of the combined mass after the collision.
(b) Calculate the kinetic energy lost during the collision.
(c) Determine the coefficient of restitution.

**中文:**
一个2.0 kg的黏土球以6.0 m/s的速度向右运动，与一个4.0 kg的黏土球以2.0 m/s的速度向左运动发生正碰。碰撞后两球粘在一起。

(a) 计算碰撞后组合体的速度。
(b) 计算碰撞过程中损失的动能。
(c) 确定恢复系数。

### Solution / 解答

**(a) Velocity after collision:**

Take right as positive direction.

Using conservation of momentum:
$$ m_1 u_1 + m_2 u_2 = (m_1 + m_2) v $$

$$ (2.0)(6.0) + (4.0)(-2.0) = (2.0 + 4.0) v $$

$$ 12.0 - 8.0 = 6.0 v $$

$$ 4.0 = 6.0 v $$

$$ v = \frac{4.0}{6.0} = 0.67 \text{ m/s (to the right)} $$

**(b) Kinetic energy lost:**

Initial KE:
$$ KE_{\text{before}} = \frac{1}{2} (2.0)(6.0)^2 + \frac{1}{2} (4.0)(2.0)^2 $$
$$ KE_{\text{before}} = \frac{1}{2} (2.0)(36) + \frac{1}{2} (4.0)(4) $$
$$ KE_{\text{before}} = 36 + 8 = 44 \text{ J} $$

Final KE:
$$ KE_{\text{after}} = \frac{1}{2} (6.0)(0.67)^2 $$
$$ KE_{\text{after}} = \frac{1}{2} (6.0)(0.449) $$
$$ KE_{\text{after}} = 1.35 \text{ J} $$

Energy lost:
$$ \Delta KE = KE_{\text{after}} - KE_{\text{before}} = 1.35 - 44 = -42.65 \text{ J} $$

So 42.65 J of kinetic energy is transformed into other forms.

**(c) Coefficient of restitution:**

For perfectly inelastic collision, $e = 0$ (since the balls stick together).

### Final Answer / 最终答案
**Answer:**
(a) $v = 0.67$ m/s to the right
(b) 42.65 J lost
(c) $e = 0$

**答案:**
(a) $v = 0.67$ m/s 向右
(b) 损失 42.65 J
(c) $e = 0$

### Quick Tip / 提示
**English:** In perfectly inelastic collisions, always use the combined mass $(m_1 + m_2)$ for the final momentum equation. The coefficient of restitution is always 0 for these collisions — no calculation needed!

**中文:** 在完全非弹性碰撞中，始终使用组合质量 $(m_1 + m_2)$ 进行最终动量方程计算。对于这类碰撞，恢复系数始终为0——无需计算！

---

### Example 2: General Inelastic Collision

### Question / 题目
**English:**
A 3.0 kg trolley moving at 4.0 m/s collides with a stationary 2.0 kg trolley. After the collision, the 3.0 kg trolley moves at 1.5 m/s in the same direction.

(a) Calculate the velocity of the 2.0 kg trolley after the collision.
(b) Determine if the collision is elastic or inelastic.
(c) Calculate the percentage of kinetic energy lost.

**中文:**
一个3.0 kg的小车以4.0 m/s的速度与一个静止的2.0 kg的小车碰撞。碰撞后，3.0 kg的小车以1.5 m/s的速度沿相同方向运动。

(a) 计算碰撞后2.0 kg小车的速度。
(b) 判断该碰撞是弹性还是非弹性。
(c) 计算动能损失的百分比。

### Solution / 解答

**(a) Velocity of 2.0 kg trolley:**

Using conservation of momentum:
$$ m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 $$

$$ (3.0)(4.0) + (2.0)(0) = (3.0)(1.5) + (2.0) v_2 $$

$$ 12.0 = 4.5 + 2.0 v_2 $$

$$ 2.0 v_2 = 7.5 $$

$$ v_2 = 3.75 \text{ m/s} $$

**(b) Elastic or inelastic?**

Initial KE:
$$ KE_{\text{before}} = \frac{1}{2} (3.0)(4.0)^2 + \frac{1}{2} (2.0)(0)^2 $$
$$ KE_{\text{before}} = 24 + 0 = 24 \text{ J} $$

Final KE:
$$ KE_{\text{after}} = \frac{1}{2} (3.0)(1.5)^2 + \frac{1}{2} (2.0)(3.75)^2 $$
$$ KE_{\text{after}} = \frac{1}{2} (3.0)(2.25) + \frac{1}{2} (2.0)(14.06) $$
$$ KE_{\text{after}} = 3.375 + 14.06 = 17.44 \text{ J} $$

Since $KE_{\text{before}} \neq KE_{\text{after}}$, the collision is **inelastic**.

**(c) Percentage of KE lost:**

$$ \text{Percentage lost} = \frac{KE_{\text{before}} - KE_{\text{after}}}{KE_{\text{before}}} \times 100\% $$

$$ \text{Percentage lost} = \frac{24 - 17.44}{24} \times 100\% = \frac{6.56}{24} \times 100\% = 27.3\% $$

### Final Answer / 最终答案
**Answer:**
(a) $v_2 = 3.75$ m/s
(b) Inelastic (KE is not conserved)
(c) 27.3% of KE lost

**答案:**
(a) $v_2 = 3.75$ m/s
(b) 非弹性（动能不守恒）
(c) 损失 27.3% 的动能

### Quick Tip / 提示
**English:** To check if a collision is elastic or inelastic, ALWAYS calculate and compare the total kinetic energy before and after. If they're equal, it's elastic. If not, it's inelastic. Don't assume based on appearance!

**中文:** 要判断碰撞是弹性还是非弹性，始终计算并比较碰撞前后的总动能。如果相等，则为弹性；如果不相等，则为非弹性。不要凭外观判断！

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the key difference between elastic and inelastic collisions?
Q (CN): 弹性碰撞和非弹性碰撞的关键区别是什么？
A (EN): In elastic collisions, kinetic energy is conserved. In inelastic collisions, kinetic energy is NOT conserved (some is transformed into heat, sound, deformation, etc.). Momentum is conserved in BOTH types.
A (CN): 在弹性碰撞中，动能守恒。在非弹性碰撞中，动能不守恒（部分转化为热能、声能、形变能等）。两种碰撞中动量都守恒。

**Flashcard 2:**
Q (EN): What is a perfectly inelastic collision?
Q (CN): 什么是完全非弹性碰撞？
A (EN): A collision where the objects stick together and move with a common velocity after impact. Maximum kinetic energy is lost, and the coefficient of restitution e = 0.
A (CN): 物体碰撞后粘在一起并以共同速度运动的碰撞。动能损失最大，恢复系数 e = 0。

**Flashcard 3:**
Q (EN): What formula is used for momentum conservation in a perfectly inelastic collision?
Q (CN): 完全非弹性碰撞中使用什么公式进行动量守恒？
A (EN): m₁u₁ + m₂u₂ = (m₁ + m₂)v, where v is the common final velocity.
A (CN): m₁u₁ + m₂u₂ = (m₁ + m₂)v，其中 v 是共同最终速度。

**Flashcard 4:**
Q (EN): What happens to the "lost" kinetic energy in an inelastic collision?
Q (CN): 非弹性碰撞中"损失"的动能去了哪里？
A (EN): It is transformed into other forms of energy: deformation energy (permanent shape change), thermal energy (heat), and sound energy. Total energy is still conserved.
A (CN): 它转化为其他形式的能量：形变能（永久形状变化）、热能（热量）和声能。总能量仍然守恒。

**Flashcard 5:**
Q (EN): How do you calculate the coefficient of restitution for a collision?
Q (CN): 如何计算碰撞的恢复系数？
A (EN): e = (v₂ - v₁)/(u₁ - u₂). For elastic collisions, e = 1. For perfectly inelastic collisions, e = 0. For inelastic collisions, 0 < e < 1.
A (CN): e = (v₂ - v₁)/(u₁ - u₂)。对于弹性碰撞，e = 1。对于完全非弹性碰撞，e = 0。对于非弹性碰撞，0 < e < 1。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Inelastic Collisions
  cn: 非弹性碰撞
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
  - "[[Elastic Collisions]]"
  - "[[Explosions and Recoil]]"
  - "[[Two-Dimensional Collisions]]"
  - "[[Linear Momentum and Impulse]]"
language: bilingual_en_cn