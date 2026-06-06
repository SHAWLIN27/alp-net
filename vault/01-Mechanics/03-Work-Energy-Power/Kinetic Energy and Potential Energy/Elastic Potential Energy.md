# 1. Overview / 概述

**English:**
Elastic Potential Energy (EPE) is the energy stored in a deformable object — such as a spring, rubber band, or elastic material — when it is stretched or compressed. This sub-topic explores how EPE is defined, calculated, and applied, particularly for objects obeying Hooke's Law. Understanding EPE is essential for linking [[Work Done by a Force]] to energy storage, and it forms a key component of the broader [[Kinetic Energy and Potential Energy]] topic. EPE is also critical for solving problems involving [[Conservation of Energy]], where elastic energy converts into [[Kinetic Energy (KE)]] or [[Gravitational Potential Energy (GPE)]].

**中文:**
弹性势能（EPE）是指可变形物体（如弹簧、橡皮筋或弹性材料）在被拉伸或压缩时储存的能量。本子知识点探讨了EPE的定义、计算和应用，特别是对于遵循胡克定律的物体。理解EPE对于将[[Work Done by a Force]]与能量储存联系起来至关重要，并且是更广泛的[[Kinetic Energy and Potential Energy]]主题的关键组成部分。EPE在涉及[[Conservation of Energy]]的问题中也至关重要，其中弹性能转化为[[Kinetic Energy (KE)]]或[[Gravitational Potential Energy (GPE)]]。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Elastic Potential Energy** / 弹性势能 | The energy stored in an elastic object when it is deformed (stretched or compressed) from its natural length. | 弹性物体从其自然长度发生形变（拉伸或压缩）时储存的能量。 |
| **Hooke's Law** / 胡克定律 | The force required to stretch or compress a spring is directly proportional to the extension or compression, provided the elastic limit is not exceeded. | 在弹性限度内，拉伸或压缩弹簧所需的力与伸长量或压缩量成正比。 |
| **Spring Constant** / 弹簧常数 | A measure of the stiffness of a spring, defined as the force per unit extension. | 衡量弹簧刚度的量，定义为单位伸长量所需的力。 |
| **Elastic Limit** / 弹性限度 | The maximum deformation from which an elastic object can return to its original shape. | 弹性物体能够恢复原状的最大形变量。 |
| **Extension** / 伸长量 | The increase in length of an object from its natural length. | 物体从其自然长度增加的长度。 |
| **Compression** / 压缩量 | The decrease in length of an object from its natural length. | 物体从其自然长度减少的长度。 |

---

# 3. Key Concepts / 关键概念

**English:**
Elastic Potential Energy arises from the work done to deform an elastic object. When you stretch a spring, you apply a force that increases as the spring extends (according to Hooke's Law: $F = kx$). The work done against this restoring force is stored as EPE.

The key relationship is that EPE equals the area under the force-extension graph. For a spring obeying Hooke's Law, this area is a triangle, giving $E_e = \frac{1}{2}kx^2$.

**Important distinctions:**
- EPE is **not** the same as [[Gravitational Potential Energy (GPE)]] — GPE depends on height, while EPE depends on deformation.
- EPE can convert to [[Kinetic Energy (KE)]] when a spring is released, as seen in projectile launchers or oscillating systems.
- The [[Work-Energy Theorem]] connects EPE to work: the work done to stretch a spring equals the change in EPE.

**Common pitfalls:**
- Forgetting that $x$ is the **extension** (or compression) from natural length, not the total length.
- Using $E_e = \frac{1}{2}kx^2$ only when Hooke's Law is obeyed (within elastic limit).
- Confusing EPE with the force $F = kx$ — EPE is energy, force is not.

**中文:**
弹性势能来源于对弹性物体做功使其形变。当你拉伸弹簧时，施加的力随着弹簧伸长而增加（根据胡克定律：$F = kx$）。克服这种恢复力所做的功以EPE的形式储存。

关键关系是EPE等于力-伸长量图下的面积。对于遵循胡克定律的弹簧，这个面积是一个三角形，因此 $E_e = \frac{1}{2}kx^2$。

**重要区别：**
- EPE **不同于** [[Gravitational Potential Energy (GPE)]] — GPE取决于高度，而EPE取决于形变。
- 当弹簧释放时，EPE可以转化为[[Kinetic Energy (KE)]]，如在弹射器或振荡系统中。
- [[Work-Energy Theorem]]将EPE与功联系起来：拉伸弹簧所做的功等于EPE的变化。

**常见错误：**
- 忘记 $x$ 是从自然长度的**伸长量**（或压缩量），而不是总长度。
- 仅在胡克定律成立时（弹性限度内）使用 $E_e = \frac{1}{2}kx^2$。
- 混淆EPE与力 $F = kx$ — EPE是能量，力不是。

---

# 4. Formulas / 公式

## Primary Formula

$$ E_e = \frac{1}{2} k x^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $E_e$ | Elastic Potential Energy | 弹性势能 | J (Joules) |
| $k$ | Spring constant | 弹簧常数 | N/m |
| $x$ | Extension or compression from natural length | 从自然长度的伸长量或压缩量 | m |

## Alternative Formula (from Work)

$$ E_e = \text{Area under } F \text{-} x \text{ graph} = \frac{1}{2} F_{\text{max}} x $$

Where $F_{\text{max}}$ is the maximum force applied.

**Derivation / 推导:**
1. Hooke's Law: $F = kx$
2. Work done = area under $F$-$x$ graph = $\frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times x \times F$
3. Substitute $F = kx$: $E_e = \frac{1}{2} \times x \times (kx) = \frac{1}{2} k x^2$

**Conditions / 适用条件:**
- The object must obey Hooke's Law (linear elastic behavior).
- The deformation must be within the elastic limit.
- $x$ is measured from the natural (unstretched) length.

> 📷 **IMAGE PROMPT — EPE-01: Force-Extension Graph for Elastic Potential Energy**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a force-extension (F-x) graph for a spring obeying Hooke's Law. The graph is a straight line through the origin with positive slope. The area under the line is shaded as a right triangle, labeled "Elastic Potential Energy = ½ kx²". Axes are labeled: "Force F (N)" on the y-axis and "Extension x (m)" on the x-axis. A small spring icon is shown next to the graph. Color scheme: blue line, light blue shaded triangle, white background. Minimalist and educational.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示遵循胡克定律的弹簧的力-伸长量（F-x）图。图形是一条通过原点的直线，斜率为正。线下区域被阴影填充为直角三角形，标注为"弹性势能 = ½ kx²"。坐标轴标注：y轴为"力 F (N)"，x轴为"伸长量 x (m)"。图旁有一个小弹簧图标。配色：蓝色线条，浅蓝色阴影三角形，白色背景。极简且具有教育意义。
>
> **Labels Required / 需要标注:**
> * "Force F (N)" on y-axis
> * "Extension x (m)" on x-axis
> * "Elastic Potential Energy = ½ kx²" inside the shaded triangle
> * "F = kx" next to the line
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This graph is frequently used in exams to calculate EPE from the area under the F-x graph, especially when the spring constant is unknown.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — EPE-02: Spring System Converting Elastic Potential Energy to Kinetic Energy**
>
> **English Prompt:**
> A 3D-rendered, photorealistic scene showing a horizontal spring system on a frictionless surface. The spring is attached to a wall on the left and a block on the right. Three stages are shown from left to right: (1) Spring compressed, block stationary, label "EPE = max, KE = 0"; (2) Spring at natural length, block moving, label "EPE = 0, KE = max"; (3) Spring stretched, block stationary, label "EPE = max, KE = 0". Arrows indicate the direction of motion. The spring is metallic silver, the block is red, and the surface is light gray. Labels are in white text with black outlines. Clean, educational, and exam-focused.
>
> **中文描述:**
> 一个3D渲染、照片级真实的场景，显示无摩擦表面上的水平弹簧系统。弹簧左侧连接墙壁，右侧连接一个木块。从左到右显示三个阶段：(1) 弹簧压缩，木块静止，标注"EPE = 最大, KE = 0"；(2) 弹簧处于自然长度，木块运动，标注"EPE = 0, KE = 最大"；(3) 弹簧拉伸，木块静止，标注"EPE = 最大, KE = 0"。箭头指示运动方向。弹簧为金属银色，木块为红色，表面为浅灰色。标签为白色文字带黑色轮廓。干净、具有教育意义且针对考试。
>
> **Labels Required / 需要标注:**
> * Stage 1: "EPE = max, KE = 0"
> * Stage 2: "EPE = 0, KE = max"
> * Stage 3: "EPE = max, KE = 0"
> * Arrows showing direction of motion
>
> **Style / 风格:** 3D render / 3D渲染
>
> **Exam Relevance / 考试关联:**
> This diagram illustrates the energy conversion between EPE and KE, a common exam topic in conservation of energy problems.

---

# 6. Worked Example / 典型例题

### Example 1: Calculating Elastic Potential Energy

### Question / 题目
**English:**
A spring has a spring constant of $200 \text{ N/m}$. It is stretched by $0.05 \text{ m}$ from its natural length. Calculate the elastic potential energy stored in the spring.

**中文:**
一根弹簧的弹簧常数为 $200 \text{ N/m}$。它从其自然长度被拉伸了 $0.05 \text{ m}$。计算弹簧中储存的弹性势能。

### Solution / 解答
**Step 1:** Identify the known values.
- $k = 200 \text{ N/m}$
- $x = 0.05 \text{ m}$

**Step 2:** Apply the formula for EPE.
$$ E_e = \frac{1}{2} k x^2 $$

**Step 3:** Substitute the values.
$$ E_e = \frac{1}{2} \times 200 \times (0.05)^2 $$

**Step 4:** Calculate.
$$ E_e = \frac{1}{2} \times 200 \times 0.0025 $$
$$ E_e = 100 \times 0.0025 $$
$$ E_e = 0.25 \text{ J} $$

### Final Answer / 最终答案
**Answer:** $0.25 \text{ J}$ **答案:** $0.25 \text{ J}$

### Quick Tip / 提示
Always square the extension $x$ **before** multiplying by $k$. A common mistake is to calculate $\frac{1}{2} k x$ instead of $\frac{1}{2} k x^2$.

---

### Example 2: Energy Conversion (EPE to KE)

### Question / 题目
**English:**
A spring with spring constant $500 \text{ N/m}$ is compressed by $0.10 \text{ m}$ and then released to launch a $0.20 \text{ kg}$ block on a frictionless surface. What is the maximum speed of the block?

**中文:**
一根弹簧常数为 $500 \text{ N/m}$ 的弹簧被压缩了 $0.10 \text{ m}$，然后释放，将一个 $0.20 \text{ kg}$ 的木块在无摩擦表面上弹射出去。木块的最大速度是多少？

### Solution / 解答
**Step 1:** Identify known values.
- $k = 500 \text{ N/m}$
- $x = 0.10 \text{ m}$
- $m = 0.20 \text{ kg}$

**Step 2:** Apply conservation of energy. All EPE converts to KE.
$$ E_e = \frac{1}{2} k x^2 = \frac{1}{2} m v^2 $$

**Step 3:** Solve for $v$.
$$ \frac{1}{2} k x^2 = \frac{1}{2} m v^2 $$
$$ k x^2 = m v^2 $$
$$ v^2 = \frac{k x^2}{m} $$
$$ v = \sqrt{\frac{k x^2}{m}} $$

**Step 4:** Substitute values.
$$ v = \sqrt{\frac{500 \times (0.10)^2}{0.20}} $$
$$ v = \sqrt{\frac{500 \times 0.01}{0.20}} $$
$$ v = \sqrt{\frac{5}{0.20}} $$
$$ v = \sqrt{25} $$
$$ v = 5.0 \text{ m/s} $$

### Final Answer / 最终答案
**Answer:** $5.0 \text{ m/s}$ **答案:** $5.0 \text{ m/s}$

### Quick Tip / 提示
In conservation of energy problems, always check if the surface is frictionless. If friction is present, some energy would be lost as heat, and the final speed would be lower.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the formula for elastic potential energy stored in a spring obeying Hooke's Law?
Q (CN): 遵循胡克定律的弹簧中储存的弹性势能的公式是什么？
A (EN): $E_e = \frac{1}{2} k x^2$, where $k$ is the spring constant and $x$ is the extension or compression from natural length.
A (CN): $E_e = \frac{1}{2} k x^2$，其中 $k$ 是弹簧常数，$x$ 是从自然长度的伸长量或压缩量。

**Flashcard 2:**
Q (EN): What does the area under a force-extension graph represent?
Q (CN): 力-伸长量图下的面积代表什么？
A (EN): The work done to stretch or compress the spring, which equals the elastic potential energy stored.
A (CN): 拉伸或压缩弹簧所做的功，等于储存的弹性势能。

**Flashcard 3:**
Q (EN): What is the condition for using $E_e = \frac{1}{2} k x^2$?
Q (CN): 使用 $E_e = \frac{1}{2} k x^2$ 的条件是什么？
A (EN): The spring must obey Hooke's Law and the deformation must be within the elastic limit.
A (CN): 弹簧必须遵循胡克定律，且形变必须在弹性限度内。

**Flashcard 4:**
Q (EN): How does elastic potential energy convert to kinetic energy in a spring-block system?
Q (CN): 在弹簧-木块系统中，弹性势能如何转化为动能？
A (EN): When the spring is released, the stored EPE is converted to KE of the block. At the natural length, all EPE has become KE, giving maximum speed.
A (CN): 当弹簧释放时，储存的EPE转化为木块的KE。在自然长度处，所有EPE都变成了KE，达到最大速度。

**Flashcard 5:**
Q (EN): What is the difference between elastic potential energy and gravitational potential energy?
Q (CN): 弹性势能和重力势能有什么区别？
A (EN): EPE depends on the deformation (stretch/compression) of an elastic object, while GPE depends on the height of an object in a gravitational field.
A (CN): EPE取决于弹性物体的形变（拉伸/压缩），而GPE取决于物体在重力场中的高度。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Elastic Potential Energy
  cn: 弹性势能
parent_topic: Kinetic Energy and Potential Energy
parent_hub: "[[Kinetic Energy and Potential Energy]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Kinetic Energy (KE)]]"
  - "[[Gravitational Potential Energy (GPE)]]"
  - "[[Work-Energy Theorem]]"
prerequisites:
  - "[[Work Done by a Force]]"
related_topics:
  - "[[Conservation of Energy]]"
language: bilingual_en_cn