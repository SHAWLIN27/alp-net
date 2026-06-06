Here is the complete bilingual leaf node for the **Centripetal Acceleration Formula**.

---

# 1. Overview / 概述

**English:**
This sub-topic derives and applies the **centripetal acceleration formula**, $a = \frac{v^2}{r} = r\omega^2$. It is the core mathematical relationship that quantifies how quickly an object’s velocity vector changes direction when moving in a circle. Understanding this formula is essential for linking [[Angular Measures]] (like $\omega$) to linear speed ($v$) and for calculating the net force required for circular motion via [[Newton’s Laws of Motion]]. This formula is the prerequisite for all calculations involving [[Centripetal Force]], [[Banked Tracks and Conical Pendulum]], and [[Circular Orbits]].

**中文:**
本子知识点推导并应用**向心加速度公式** $a = \frac{v^2}{r} = r\omega^2$。这是量化物体做圆周运动时速度矢量方向变化快慢的核心数学关系。理解该公式对于将[[Angular Measures|角量]]（如 $\omega$）与线速度（$v$）联系起来，以及通过[[Newton’s Laws of Motion|牛顿运动定律]]计算圆周运动所需的合力至关重要。该公式是计算[[Centripetal Force|向心力]]、分析[[Banked Tracks and Conical Pendulum|倾斜轨道与圆锥摆]]以及研究[[Circular Orbits|圆形轨道]]的先决条件。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Centripetal Acceleration** / 向心加速度 | The acceleration of an object moving in a circle at constant speed, directed towards the center of the circle. | 物体以恒定速率做圆周运动时，指向圆心的加速度。 |
| **Radial Direction** / 径向 | The direction pointing towards the center of the circle, perpendicular to the instantaneous velocity. | 指向圆心、垂直于瞬时速度的方向。 |
| **Tangential Speed ($v$)** / 线速度 | The constant magnitude of the velocity vector of an object in uniform circular motion. | 物体在匀速圆周运动中速度矢量的大小（恒定值）。 |
| **Angular Speed ($\omega$)** / 角速度 | The rate of change of angular displacement, measured in rad/s. | 角位移的变化率，单位为 rad/s。 |

---

# 3. Key Concepts / 关键概念

**English:**
The key insight is that even when speed is constant, **direction changes**, and a change in velocity implies acceleration. For a small angular displacement $\Delta\theta$, the change in the velocity vector $\Delta v$ points towards the center. By geometry, $\Delta v = v \Delta\theta$. Dividing by time $\Delta t$ gives $a = \frac{\Delta v}{\Delta t} = v \frac{\Delta\theta}{\Delta t} = v\omega$. Since $v = r\omega$, we get the two equivalent forms: $a = \frac{v^2}{r}$ and $a = r\omega^2$.

**Common Pitfall:** Students often think the acceleration is zero because the speed is constant. Remember: acceleration is a vector; a change in direction is an acceleration.
**Prerequisite:** This derivation relies on understanding [[Angular Measures]] (radians) and the small-angle approximation $\sin\theta \approx \theta$.

**中文:**
关键洞察在于，即使速率恒定，**方向也在改变**，速度的变化意味着存在加速度。对于一个小的角位移 $\Delta\theta$，速度矢量 $\Delta v$ 的变化指向圆心。通过几何关系，$\Delta v = v \Delta\theta$。除以时间 $\Delta t$ 得到 $a = \frac{\Delta v}{\Delta t} = v \frac{\Delta\theta}{\Delta t} = v\omega$。由于 $v = r\omega$，我们得到两个等价形式：$a = \frac{v^2}{r}$ 和 $a = r\omega^2$。

**常见错误：** 学生常因速率恒定而误认为加速度为零。请记住：加速度是矢量；方向的变化就是一种加速度。
**先决条件：** 该推导依赖于理解[[Angular Measures|角量]]（弧度）和小角度近似 $\sin\theta \approx \theta$。

---

# 4. Formulas / 公式

$$ a = \frac{v^2}{r} = r\omega^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $a$ | Centripetal acceleration | 向心加速度 | $\text{m/s}^2$ |
| $v$ | Tangential (linear) speed | 线速度 | $\text{m/s}$ |
| $r$ | Radius of circular path | 圆周运动半径 | $\text{m}$ |
| $\omega$ | Angular speed | 角速度 | $\text{rad/s}$ |

**Derivation / 推导:**
1. For a small angle $\Delta\theta$, arc length $\Delta s = r \Delta\theta$.
2. The change in velocity vector $\Delta v = v \Delta\theta$ (from vector triangle geometry).
3. Acceleration $a = \frac{\Delta v}{\Delta t} = v \frac{\Delta\theta}{\Delta t} = v\omega$.
4. Substitute $v = r\omega$ to get $a = \frac{v^2}{r}$.

**Conditions / 适用条件:**
- **Uniform circular motion** (constant speed).
- **Inertial reference frame** (the acceleration is real, not fictitious).

> 📷 **IMAGE PROMPT — [CAC-01]: Vector Derivation of Centripetal Acceleration**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing an object moving in a circle of radius r. Two velocity vectors v1 and v2 are drawn at two points separated by a small angle Δθ. A separate vector triangle shows v1, v2, and Δv pointing towards the center. Labels: "v1", "v2", "Δv", "r", "Δθ". Use blue for velocity vectors, red for Δv, black for geometry. White background, 2D top-down view.
>
> **中文描述:**
> 一个清晰的教科书式矢量图，显示一个物体在半径为 r 的圆上运动。在两个相隔小角度 Δθ 的点上画出两个速度矢量 v1 和 v2。一个单独的矢量三角形显示 v1、v2 和指向圆心的 Δv。标签："v1"、"v2"、"Δv"、"r"、"Δθ"。速度矢量用蓝色，Δv 用红色，几何线用黑色。白色背景，二维俯视图。
>
> **Labels Required / 需要标注:**
> * v1, v2 (tangential velocity vectors)
> * Δv (change in velocity, pointing radially inward)
> * r (radius)
> * Δθ (angular displacement)
>
> **Style / 风格:** Textbook vector / 2D diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is the standard derivation proof required for A-Level exam questions (especially CAIE 9702/14.2).

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — [CAC-02]: Comparing a = v²/r and a = rω²**
>
> **English Prompt:**
> A split-screen infographic. Left side: a car on a circular track of radius r, with a label showing a = v²/r. Right side: a rotating disc with a point on the edge, with a label showing a = rω². Arrows show the direction of acceleration towards the center. Use a photorealistic 3D render style with a dark blue background and glowing neon labels.
>
> **中文描述:**
> 一个分屏信息图。左侧：一辆在半径为 r 的圆形轨道上的汽车，标签显示 a = v²/r。右侧：一个旋转的圆盘，边缘有一个点，标签显示 a = rω²。箭头显示加速度指向圆心。使用逼真的 3D 渲染风格，深蓝色背景，发光霓虹灯标签。
>
> **Labels Required / 需要标注:**
> * a = v²/r (left)
> * a = rω² (right)
> * r (radius)
> * v (tangential speed)
> * ω (angular speed)
>
> **Style / 风格:** Photorealistic 3D render
>
> **Exam Relevance / 考试关联:**
> Helps students choose the correct form of the formula based on given data (linear vs. angular).

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:** A stone is whirled in a horizontal circle of radius 0.50 m at a constant speed of 3.0 m/s. Calculate the centripetal acceleration of the stone.
**中文:** 一块石头在半径为 0.50 m 的水平圆周上以 3.0 m/s 的恒定速率旋转。计算石头的向心加速度。

### Solution / 解答
1. **Identify knowns:** $v = 3.0 \text{ m/s}$, $r = 0.50 \text{ m}$.
2. **Choose formula:** Since $v$ and $r$ are given, use $a = \frac{v^2}{r}$.
3. **Substitute:** $a = \frac{(3.0)^2}{0.50} = \frac{9.0}{0.50}$.
4. **Calculate:** $a = 18 \text{ m/s}^2$.

### Final Answer / 最终答案
**Answer:** $18 \text{ m/s}^2$ **答案:** $18 \text{ m/s}^2$

### Quick Tip / 提示
Always check units: $v$ in m/s, $r$ in m. If given $\omega$ instead of $v$, use $a = r\omega^2$.

---

# 7. Flashcards / 闪卡

**Q (EN):** What is the formula for centripetal acceleration in terms of tangential speed and radius?
**Q (CN):** 用线速度和半径表示的向心加速度公式是什么？
**A (EN):** $a = \frac{v^2}{r}$
**A (CN):** $a = \frac{v^2}{r}$

**Q (EN):** What is the formula for centripetal acceleration in terms of angular speed and radius?
**Q (CN):** 用角速度和半径表示的向心加速度公式是什么？
**A (EN):** $a = r\omega^2$
**A (CN):** $a = r\omega^2$

**Q (EN):** Why is there a centripetal acceleration even when speed is constant?
**Q (CN):** 为什么即使速率恒定也存在向心加速度？
**A (EN):)** Because the direction of the velocity vector is continuously changing.
**A (CN):** 因为速度矢量的方向在不断变化。

**Q (EN):** What is the direction of centripetal acceleration?
**Q (CN):** 向心加速度的方向是什么？
**A (EN):** Towards the center of the circle (radially inward).
**A (CN):** 指向圆心（径向向内）。

**Q (EN):** If the radius of a circle is doubled and speed remains constant, what happens to centripetal acceleration?
**Q (CN):** 如果圆的半径加倍而速率不变，向心加速度会如何变化？
**A (EN):** It halves (since $a \propto 1/r$).
**A (CN):** 减半（因为 $a \propto 1/r$）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Centripetal Acceleration Formula
  cn: 向心加速度公式
parent_topic: Centripetal Acceleration and Force
parent_hub: "[[Centripetal Acceleration and Force]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Centripetal Force]]"
  - "[[Banked Tracks and Conical Pendulum]]"
  - "[[Angular Measures]]"
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn