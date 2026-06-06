Here is the complete bilingual leaf node for **Escape Velocity**, designed as a standalone Obsidian note and knowledge graph leaf.

---

# 1. Overview / 概述

**English:**
Escape velocity is the minimum speed an object must have to break free from a planet’s or star’s gravitational field without further propulsion. It is a direct application of the principle of conservation of energy, linking [[Gravitational Potential Energy in a Radial Field]] with [[Kinetic Energy and Potential Energy]]. This concept is crucial for understanding space travel, atmospheric retention, and the formation of black holes. It represents the boundary between a bound orbit (like a satellite) and an unbound trajectory (like an interstellar probe).

**中文:**
逃逸速度是物体无需额外动力即可摆脱行星或恒星引力场所需的最小速度。它是能量守恒原理的直接应用，将[[Gravitational Potential Energy in a Radial Field|径向场中的引力势能]]与[[Kinetic Energy and Potential Energy|动能和势能]]联系起来。这个概念对于理解太空旅行、大气层保留以及黑洞的形成至关重要。它代表了束缚轨道（如卫星）与非束缚轨迹（如星际探测器）之间的界限。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Escape Velocity** / 逃逸速度 | The minimum speed required for an object to escape the gravitational field of a massive body, reaching an infinite distance with zero kinetic energy. | 物体摆脱大质量天体引力场所需的最小速度，到达无穷远处时动能为零。 |
| **Bound Orbit** / 束缚轨道 | A closed trajectory (circular or elliptical) where the total mechanical energy of the orbiting body is negative. | 一种闭合轨迹（圆形或椭圆形），其中轨道物体的总机械能为负。 |
| **Unbound Trajectory** / 非束缚轨迹 | An open trajectory (parabolic or hyperbolic) where the total mechanical energy is zero or positive, allowing escape. | 一种开放轨迹（抛物线或双曲线），其总机械能为零或正，允许逃逸。 |
| **Gravitational Binding Energy** / 引力结合能 | The energy required to separate a body from a gravitational system to infinity; equal to the magnitude of the total gravitational potential energy. | 将物体从引力系统中分离到无穷远处所需的能量；等于总引力势能的大小。 |

---

# 3. Key Concepts / 关键概念

**English:**
The derivation of escape velocity relies on the principle of conservation of mechanical energy. We consider an object of mass $m$ on the surface of a planet of mass $M$ and radius $R$.

1.  **Initial State:** The object has kinetic energy $E_k = \frac{1}{2}mv^2$ and gravitational potential energy $E_p = -\frac{GMm}{R}$ (from [[Gravitational Potential (V)]]).
2.  **Final State (at infinity):** For the object to just escape, its speed must drop to zero at infinity ($r \to \infty$). Therefore, $E_k(\infty) = 0$ and $E_p(\infty) = 0$.
3.  **Energy Conservation:** $E_k(\text{surface}) + E_p(\text{surface}) = E_k(\infty) + E_p(\infty)$.

This gives:
$$\frac{1}{2}mv^2 - \frac{GMm}{R} = 0 + 0$$

Solving for $v$ gives the escape velocity $v_{esc}$.

**Common Pitfall:** Students often confuse escape velocity with the orbital velocity required for a [[Circular Orbits|circular orbit]]. Escape velocity is $\sqrt{2}$ times larger than the orbital velocity at the same radius. Also, escape velocity is independent of the mass of the escaping object—a feather and a rocket require the same speed to escape (ignoring air resistance).

**中文:**
逃逸速度的推导依赖于机械能守恒原理。我们考虑一个质量为 $m$ 的物体位于质量为 $M$、半径为 $R$ 的行星表面。

1.  **初始状态：** 物体具有动能 $E_k = \frac{1}{2}mv^2$ 和引力势能 $E_p = -\frac{GMm}{R}$（来自[[Gravitational Potential (V)|引力势]]）。
2.  **最终状态（无穷远处）：** 要使物体恰好逃逸，其速度在无穷远处必须降为零（$r \to \infty$）。因此，$E_k(\infty) = 0$ 且 $E_p(\infty) = 0$。
3.  **能量守恒：** $E_k(\text{表面}) + E_p(\text{表面}) = E_k(\infty) + E_p(\infty)$。

由此得出：
$$\frac{1}{2}mv^2 - \frac{GMm}{R} = 0 + 0$$

解出 $v$ 即得到逃逸速度 $v_{esc}$。

**常见误区：** 学生经常将逃逸速度与[[Circular Orbits|圆形轨道]]所需的轨道速度混淆。在同一半径下，逃逸速度是轨道速度的 $\sqrt{2}$ 倍。此外，逃逸速度与逃逸物体的质量无关——忽略空气阻力，羽毛和火箭需要相同的速度才能逃逸。

---

# 4. Formulas / 公式

The primary formula for escape velocity from a spherical body:

$$ v_{esc} = \sqrt{\frac{2GM}{R}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v_{esc}$ | Escape velocity | 逃逸速度 | $\text{m s}^{-1}$ |
| $G$ | Gravitational constant | 引力常量 | $\text{N m}^2 \text{kg}^{-2}$ |
| $M$ | Mass of the central body | 中心天体质量 | $\text{kg}$ |
| $R$ | Radius of the central body | 中心天体半径 | $\text{m}$ |

**Derivation / 推导:**
As shown in Section 3, from conservation of energy:
$$\frac{1}{2}mv_{esc}^2 - \frac{GMm}{R} = 0$$
$$\frac{1}{2}mv_{esc}^2 = \frac{GMm}{R}$$
$$v_{esc}^2 = \frac{2GM}{R}$$
$$v_{esc} = \sqrt{\frac{2GM}{R}}$$

**Conditions / 适用条件:**
- The formula applies only to escape from a **spherically symmetric, non-rotating** body.
- It assumes **no other forces** (e.g., air resistance, thrust) act on the object after launch.
- The object is launched from the **surface** ($r = R$). For escape from a point at distance $r > R$, replace $R$ with $r$.

> 📷 **IMAGE PROMPT — VESC-01: Escape Velocity Energy Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a planet (Earth) on the left. A small rocket is on the surface. Two arrows emanate from the rocket: one short arrow labeled "Orbital Velocity (v_o)" curving into a circular orbit, and one long arrow labeled "Escape Velocity (v_esc)" shooting straight out and fading into deep space. A vertical energy bar graph on the right shows the "Total Energy" line at zero for escape and negative for orbit. Use a dark blue space background with white and yellow labels.
>
> **中文描述:**
> 一个清晰的教科书式矢量图，左侧显示一颗行星（地球）。表面有一枚小火箭。从火箭发出两个箭头：一个短箭头标记为“轨道速度 (v_o)”，弯曲进入圆形轨道；一个长箭头标记为“逃逸速度 (v_esc)”，直线射出并消失在深空中。右侧的垂直能量柱状图显示，逃逸的“总能量”线为零，轨道的为负。使用深蓝色太空背景，白色和黄色标签。
>
> **Labels Required / 需要标注:**
> * $v_{esc} = \sqrt{2} v_o$
> * Total Energy = 0 (Escape)
> * Total Energy < 0 (Bound Orbit)
>
> **Style / 风格:** Textbook vector / 2D diagram
>
> **Exam Relevance / 考试关联:**
> This diagram visually reinforces the relationship between orbital and escape velocity, a common exam comparison question.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — VESC-02: Escape from Different Planets**
>
> **English Prompt:**
> A side-by-side comparison infographic. Left: A small, low-mass planet (like Mars) with a small rocket easily flying away with a short speed arrow. Right: A large, high-mass planet (like Jupiter) with the same rocket struggling, requiring a much longer speed arrow to escape. The background is a simple gradient. Include a text box at the bottom: "Escape velocity depends on mass and radius: $v_{esc} = \sqrt{2GM/R}$". Use a clean, educational illustration style.
>
> **中文描述:**
> 一个并排比较的信息图。左侧：一个低质量小行星（如火星），一枚小火箭轻松飞走，速度箭头较短。右侧：一个高质量大行星（如木星），同一枚火箭挣扎着，需要长得多的速度箭头才能逃逸。背景是简单的渐变。底部包含文本框：“逃逸速度取决于质量和半径：$v_{esc} = \sqrt{2GM/R}$”。使用干净的教育插图风格。
>
> **Labels Required / 需要标注:**
> * Low M, Small R → Low $v_{esc}$
> * High M, Large R → High $v_{esc}$
>
> **Style / 风格:** Educational infographic / 2D illustration
>
> **Exam Relevance / 考试关联:**
> Helps students intuitively understand why different celestial bodies have different escape velocities, a common qualitative exam question.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
The mass of the Earth is $6.0 \times 10^{24} \text{ kg}$ and its radius is $6.4 \times 10^6 \text{ m}$. Calculate the escape velocity from the Earth's surface. ($G = 6.67 \times 10^{-11} \text{ N m}^2 \text{kg}^{-2}$)

**中文:**
地球的质量为 $6.0 \times 10^{24} \text{ kg}$，半径为 $6.4 \times 10^6 \text{ m}$。计算从地球表面的逃逸速度。（$G = 6.67 \times 10^{-11} \text{ N m}^2 \text{kg}^{-2}$）

### Solution / 解答
1.  **Write the formula / 写出公式:**
    $$v_{esc} = \sqrt{\frac{2GM}{R}}$$

2.  **Substitute values / 代入数值:**
    $$v_{esc} = \sqrt{\frac{2 \times (6.67 \times 10^{-11}) \times (6.0 \times 10^{24})}{6.4 \times 10^6}}$$

3.  **Calculate numerator / 计算分子:**
    $$2 \times 6.67 \times 10^{-11} \times 6.0 \times 10^{24} = 80.04 \times 10^{13} = 8.004 \times 10^{14}$$

4.  **Divide by radius / 除以半径:**
    $$\frac{8.004 \times 10^{14}}{6.4 \times 10^6} = 1.2506 \times 10^8$$

5.  **Take square root / 开平方根:**
    $$v_{esc} = \sqrt{1.2506 \times 10^8} \approx 1.12 \times 10^4 \text{ m s}^{-1}$$

### Final Answer / 最终答案
**Answer:** $1.12 \times 10^4 \text{ m s}^{-1}$ (or 11.2 km/s)
**答案:** $1.12 \times 10^4 \text{ m s}^{-1}$ (或 11.2 km/s)

### Quick Tip / 提示
**EN:** Always check your units. If you use $G$ in $\text{N m}^2 \text{kg}^{-2}$, $M$ in kg, and $R$ in m, your answer will be in $\text{m s}^{-1}$. Remember to convert km to m if necessary.
**CN:** 始终检查单位。如果 $G$ 的单位是 $\text{N m}^2 \text{kg}^{-2}$，$M$ 的单位是 kg，$R$ 的单位是 m，那么答案的单位就是 $\text{m s}^{-1}$。必要时记得将 km 转换为 m。

---

# 7. Flashcards / 闪卡

**Card 1:**
Q (EN): What is the definition of escape velocity?
Q (CN): 逃逸速度的定义是什么？
A (EN): The minimum speed required for an object to escape the gravitational field of a massive body, reaching an infinite distance with zero kinetic energy.
A (CN): 物体摆脱大质量天体引力场所需的最小速度，到达无穷远处时动能为零。

**Card 2:**
Q (EN): Write the formula for escape velocity from a planet of mass M and radius R.
Q (CN): 写出从质量为 M、半径为 R 的行星逃逸的速度公式。
A (EN): $v_{esc} = \sqrt{\frac{2GM}{R}}$
A (CN): $v_{esc} = \sqrt{\frac{2GM}{R}}$

**Card 3:**
Q (EN): How does escape velocity compare to orbital velocity at the same radius?
Q (CN): 在同一半径下，逃逸速度与轨道速度相比如何？
A (EN): Escape velocity is $\sqrt{2}$ times larger than the orbital velocity.
A (CN): 逃逸速度是轨道速度的 $\sqrt{2}$ 倍。

**Card 4:**
Q (EN): Does escape velocity depend on the mass of the escaping object?
Q (CN): 逃逸速度取决于逃逸物体的质量吗？
A (EN): No, it is independent of the mass of the escaping object.
A (CN): 不，它与逃逸物体的质量无关。

**Card 5:**
Q (EN): What is the condition for an object to be in a bound orbit?
Q (CN): 物体处于束缚轨道的条件是什么？
A (EN): Its total mechanical energy (kinetic + gravitational potential) must be negative.
A (CN): 其总机械能（动能 + 引力势能）必须为负。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Escape Velocity
  cn: 逃逸速度
parent_topic: Gravitational Potential
parent_hub: "[[Gravitational Potential]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Gravitational Potential Energy in a Radial Field]]"
  - "[[Gravitational Potential (V)]]"
  - "[[Potential Gradients]]"
  - "[[Circular Orbits]]"
language: bilingual_en_cn