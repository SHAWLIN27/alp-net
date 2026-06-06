# 1. Overview / 概述

**English:**
Viscous drag is the resistive force experienced by an object moving through a fluid (liquid or gas). This sub-topic focuses on the quantitative description of viscous drag for small, spherical objects moving slowly through a fluid — a scenario governed by **Stokes' Law**. Understanding viscous drag is essential for explaining why objects like raindrops or ball bearings eventually reach a constant speed ([[Terminal Velocity in Fluids]]) when falling through a fluid. It also connects to the broader concept of [[Forces in Fluids (Upthrust and Viscous Force)]], where upthrust (buoyancy) and drag act together against weight. This sub-topic builds directly on [[Types of Force]] and provides a foundation for understanding energy dissipation in fluids, linking to [[Work Done by a Force]].

**中文:**
粘性阻力是物体在流体（液体或气体）中运动时所受到的阻碍力。本子知识点聚焦于小球体在流体中缓慢运动时粘性阻力的定量描述——这由**斯托克斯定律**所支配。理解粘性阻力对于解释为什么雨滴或滚珠轴承在流体中下落时最终会达到恒定速度（[[Terminal Velocity in Fluids]]）至关重要。它还与更广泛的[[Forces in Fluids (Upthrust and Viscous Force)]]概念相联系，其中上推力（浮力）和阻力与重力共同作用。本子知识点直接建立在[[Types of Force]]之上，并为理解流体中的能量耗散提供了基础，与[[Work Done by a Force]]相关联。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Viscous Drag** / 粘性阻力 | A resistive force that opposes the motion of an object through a fluid, caused by the internal friction (viscosity) of the fluid. | 阻碍物体在流体中运动的阻力，由流体的内摩擦（粘性）引起。 |
| **Stokes' Law** / 斯托克斯定律 | For a small sphere moving at low speed through a viscous fluid, the viscous drag force $F$ is given by $F = 6\pi\eta r v$, where $\eta$ is the fluid viscosity, $r$ is the sphere's radius, and $v$ is its speed. | 对于在粘性流体中低速运动的小球体，粘性阻力 $F$ 由 $F = 6\pi\eta r v$ 给出，其中 $\eta$ 是流体粘度，$r$ 是球体半径，$v$ 是其速度。 |
| **Viscosity** / 粘度 | A measure of a fluid's resistance to flow; high viscosity fluids (e.g., honey) are "thick" and resist deformation. | 流体抵抗流动能力的度量；高粘度流体（如蜂蜜）很“稠”，抵抗形变。 |
| **Laminar Flow** / 层流 | Smooth, orderly fluid flow in parallel layers, with no mixing between layers; a condition for Stokes' Law to be valid. | 平滑、有序的流体流动，呈平行层状，层间无混合；是斯托克斯定律成立的条件。 |
| **Terminal Velocity** / 终端速度 | The constant speed reached by a falling object when the net force (weight minus upthrust minus drag) becomes zero. | 下落物体在净力（重力减去上推力再减去阻力）为零时达到的恒定速度。 |

---

# 3. Key Concepts / 关键概念

**English:**
Viscous drag arises from the internal friction within a fluid. When an object moves through a fluid, it must push fluid molecules out of the way. The fluid's viscosity $\eta$ quantifies how "sticky" or resistant the fluid is to this motion. For a small sphere moving slowly (so that flow remains [[Laminar Flow|laminar]]), **Stokes' Law** provides a simple linear relationship between drag force $F$, speed $v$, sphere radius $r$, and fluid viscosity $\eta$:

$$F = 6\pi\eta r v$$

**Key points to understand:**
1. **Proportional to speed:** Unlike kinetic friction (which is constant), viscous drag increases linearly with speed for small, slow objects. This is why a ball bearing dropped in oil initially accelerates but then approaches a constant speed ([[Terminal Velocity in Fluids]]).
2. **Proportional to radius:** Larger spheres experience more drag at the same speed because they displace more fluid.
3. **Proportional to viscosity:** The drag is larger in more viscous fluids (e.g., glycerine vs. water).

**Common pitfalls:**
- **Confusing viscous drag with friction:** Viscous drag is speed-dependent; kinetic friction is not.
- **Forgetting the conditions for Stokes' Law:** It only applies to small spheres, low speeds, and laminar flow. For large objects or high speeds (turbulent flow), drag is proportional to $v^2$ (not $v$).
- **Neglecting upthrust:** In many problems, both [[Upthrust and Archimedes' Principle]] and viscous drag act on a falling sphere. The net force is weight minus upthrust minus drag.

**Physical interpretation:**
Imagine a sphere moving through a fluid. Fluid layers adjacent to the sphere are dragged along, creating a velocity gradient. The viscous drag is the force required to maintain this gradient against the fluid's internal resistance. Stokes' Law is derived from solving the Navier-Stokes equations for low Reynolds number flow — a key result in fluid dynamics.

**中文:**
粘性阻力源于流体内部的摩擦。当物体在流体中运动时，它必须推开流体分子。流体的粘度 $\eta$ 量化了流体对这种运动的“粘滞”或抵抗程度。对于缓慢运动的小球体（保持[[Laminar Flow|层流]]状态），**斯托克斯定律**给出了阻力 $F$、速度 $v$、球体半径 $r$ 和流体粘度 $\eta$ 之间的简单线性关系：

$$F = 6\pi\eta r v$$

**关键理解点：**
1. **与速度成正比：** 与动摩擦（恒定）不同，对于缓慢运动的小物体，粘性阻力随速度线性增加。这就是为什么在油中下落的滚珠轴承最初加速，然后接近恒定速度（[[Terminal Velocity in Fluids]]）。
2. **与半径成正比：** 在相同速度下，更大的球体受到更大的阻力，因为它们排开更多流体。
3. **与粘度成正比：** 在更粘稠的流体中（如甘油 vs. 水），阻力更大。

**常见误区：**
- **混淆粘性阻力与摩擦：** 粘性阻力与速度相关；动摩擦则不是。
- **忘记斯托克斯定律的适用条件：** 它仅适用于小球体、低速和层流。对于大物体或高速（湍流），阻力与 $v^2$ 成正比（而非 $v$）。
- **忽略上推力：** 在许多问题中，[[Upthrust and Archimedes' Principle]] 和粘性阻力同时作用于下落球体。净力是重力减去上推力再减去阻力。

**物理诠释：**
想象一个球体在流体中运动。与球体相邻的流体层被拖拽，形成速度梯度。粘性阻力就是维持这种梯度以对抗流体内部阻力所需的力。斯托克斯定律是通过求解低雷诺数流动的纳维-斯托克斯方程推导得出的——这是流体动力学中的一个关键结果。

---

# 4. Formulas / 公式

## Stokes' Law / 斯托克斯定律

$$F = 6\pi\eta r v$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F$ | Viscous drag force | 粘性阻力 | N |
| $\eta$ | Dynamic viscosity of the fluid | 流体的动力粘度 | Pa·s (or N·s/m²) |
| $r$ | Radius of the sphere | 球体半径 | m |
| $v$ | Speed of the sphere relative to the fluid | 球体相对于流体的速度 | m/s |

**Derivation / 推导:**
Stokes' Law is derived from the Navier-Stokes equations under the assumption of low Reynolds number ($Re \ll 1$), where inertial forces are negligible compared to viscous forces. The derivation involves integrating the pressure and shear stress distributions over the sphere's surface. For A-Level, you only need to know the formula and its applications, not the derivation.

**Conditions / 适用条件:**
- The object must be a **small sphere**.
- The flow must be **laminar** (low Reynolds number, $Re < 0.1$ typically).
- The fluid must be **incompressible** and **Newtonian** (viscosity constant).
- The sphere must be moving at **low speed** (no turbulence).
- The sphere must be **smooth** and **rigid**.

> 📷 **IMAGE PROMPT — F1: Stokes' Law Force Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a small sphere (radius r) moving downward through a viscous fluid. Three arrows: weight (W) downward, upthrust (U) upward, viscous drag (F) upward. Labels: "Stokes' Law: F = 6πηrv". Fluid shown as light blue background with wavy lines indicating viscosity. Sphere labeled "radius r". Speed arrow labeled "v". Simple, educational, white background.
>
> **中文描述:**
> 一个干净的教科书式矢量图，显示一个小球体（半径 r）在粘性流体中向下运动。三个箭头：向下的重力（W）、向上的上推力（U）、向上的粘性阻力（F）。标签："斯托克斯定律：F = 6πηrv"。流体显示为浅蓝色背景，带有波浪线表示粘度。球体标注"半径 r"。速度箭头标注"v"。简单、教育性、白色背景。
>
> **Labels Required / 需要标注:**
> * F (viscous drag) — upward arrow
> * W (weight) — downward arrow
> * U (upthrust) — upward arrow
> * r (radius) — on sphere
> * v (velocity) — downward arrow
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> Essential for drawing free-body diagrams of a sphere falling through a fluid, a common exam question.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — I1: Viscosity Comparison (Water vs. Honey)**
>
> **English Prompt:**
> A split-screen 3D render comparing two spheres falling through different fluids. Left side: a metal sphere falling through clear water (low viscosity) — fast descent, small drag arrows. Right side: identical sphere falling through golden honey (high viscosity) — slow descent, large drag arrows. Both fluids shown in transparent containers. Labels: "Water (η low)" and "Honey (η high)". Drag force arrows labeled "F_drag" with different sizes. Speed arrows labeled "v" with different lengths. Photorealistic, educational, clean lighting.
>
> **中文描述:**
> 一个分屏3D渲染图，比较两个球体在不同流体中下落。左侧：金属球体在清澈的水中下落（低粘度）——快速下落，小阻力箭头。右侧：相同球体在金黄色的蜂蜜中下落（高粘度）——缓慢下落，大阻力箭头。两种流体显示在透明容器中。标签："水（η 低）"和"蜂蜜（η 高）"。阻力箭头标注"F_drag"，大小不同。速度箭头标注"v"，长度不同。照片级真实感、教育性、干净照明。
>
> **Labels Required / 需要标注:**
> * η (viscosity) values
> * F_drag arrows (different sizes)
> * v arrows (different lengths)
> * Sphere (identical in both)
>
> **Style / 风格:** Photorealistic 3D render / 照片级真实感3D渲染
>
> **Exam Relevance / 考试关联:**
> Helps students intuitively understand how viscosity affects drag and terminal velocity — a common conceptual question.

---

# 6. Worked Example / 典型例题

### Example 1: Calculating Viscous Drag

### Question / 题目
**English:**
A small steel ball bearing of radius 0.50 mm falls through glycerine at a constant speed of 0.12 m/s. The viscosity of glycerine is 1.5 Pa·s. Calculate the viscous drag force acting on the ball bearing.

**中文:**
一个小钢滚珠轴承半径为0.50 mm，在甘油中以0.12 m/s的恒定速度下落。甘油的粘度为1.5 Pa·s。计算作用在滚珠轴承上的粘性阻力。

### Solution / 解答
**Step 1:** Identify the known quantities.
- Radius $r = 0.50 \text{ mm} = 0.50 \times 10^{-3} \text{ m} = 5.0 \times 10^{-4} \text{ m}$
- Speed $v = 0.12 \text{ m/s}$
- Viscosity $\eta = 1.5 \text{ Pa·s}$

**Step 2:** Apply Stokes' Law.
$$F = 6\pi\eta r v$$

**Step 3:** Substitute values.
$$F = 6\pi \times (1.5) \times (5.0 \times 10^{-4}) \times (0.12)$$

**Step 4:** Calculate.
$$F = 6\pi \times 1.5 \times 5.0 \times 10^{-4} \times 0.12$$
$$F = 6\pi \times 9.0 \times 10^{-5}$$
$$F = 54\pi \times 10^{-5}$$
$$F = 1.70 \times 10^{-3} \text{ N} \quad (\text{using } \pi \approx 3.142)$$

### Final Answer / 最终答案
**Answer:** $1.70 \times 10^{-3} \text{ N}$ **答案:** $1.70 \times 10^{-3} \text{ N}$

### Quick Tip / 提示
Always convert radius to meters before using Stokes' Law. Watch out for units: viscosity is often given in Pa·s (which is equivalent to N·s/m²).

---

### Example 2: Finding Terminal Velocity

### Question / 题目
**English:**
A small sphere of radius 2.0 mm and density 7800 kg/m³ falls through oil of density 900 kg/m³ and viscosity 0.85 Pa·s. Calculate its terminal velocity. (Assume Stokes' Law applies.)

**中文:**
一个小球体半径为2.0 mm，密度为7800 kg/m³，在密度为900 kg/m³、粘度为0.85 Pa·s的油中下落。计算其终端速度。（假设斯托克斯定律适用。）

### Solution / 解答
**Step 1:** At terminal velocity, net force = 0.
$$\text{Weight} - \text{Upthrust} - \text{Drag} = 0$$
$$\text{Weight} = \text{Upthrust} + \text{Drag}$$

**Step 2:** Write expressions for each force.
- Weight: $W = mg = \rho_{\text{sphere}} V g = \rho_{\text{sphere}} \left(\frac{4}{3}\pi r^3\right) g$
- Upthrust: $U = \rho_{\text{fluid}} V g = \rho_{\text{fluid}} \left(\frac{4}{3}\pi r^3\right) g$
- Drag (Stokes' Law): $F = 6\pi\eta r v$

**Step 3:** Substitute into the equilibrium equation.
$$\rho_{\text{sphere}} \left(\frac{4}{3}\pi r^3\right) g = \rho_{\text{fluid}} \left(\frac{4}{3}\pi r^3\right) g + 6\pi\eta r v$$

**Step 4:** Solve for $v$.
$$6\pi\eta r v = \frac{4}{3}\pi r^3 g (\rho_{\text{sphere}} - \rho_{\text{fluid}})$$
$$v = \frac{2 r^2 g (\rho_{\text{sphere}} - \rho_{\text{fluid}})}{9\eta}$$

**Step 5:** Substitute values.
- $r = 2.0 \text{ mm} = 2.0 \times 10^{-3} \text{ m}$
- $g = 9.81 \text{ m/s}^2$
- $\rho_{\text{sphere}} = 7800 \text{ kg/m}^3$
- $\rho_{\text{fluid}} = 900 \text{ kg/m}^3$
- $\eta = 0.85 \text{ Pa·s}$

$$v = \frac{2 \times (2.0 \times 10^{-3})^2 \times 9.81 \times (7800 - 900)}{9 \times 0.85}$$

$$v = \frac{2 \times 4.0 \times 10^{-6} \times 9.81 \times 6900}{7.65}$$

$$v = \frac{2 \times 4.0 \times 10^{-6} \times 67689}{7.65}$$

$$v = \frac{5.415 \times 10^{-1}}{7.65}$$

$$v = 0.0708 \text{ m/s}$$

### Final Answer / 最终答案
**Answer:** $7.08 \times 10^{-2} \text{ m/s}$ **答案:** $7.08 \times 10^{-2} \text{ m/s}$

### Quick Tip / 提示
The formula $v = \frac{2 r^2 g (\rho_{\text{sphere}} - \rho_{\text{fluid}})}{9\eta}$ is a derived result for terminal velocity under Stokes' Law. Memorize it — it's a common exam shortcut!

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is Stokes' Law and what does each symbol represent?
Q (CN): 斯托克斯定律是什么？每个符号代表什么？
A (EN): $F = 6\pi\eta r v$, where $F$ = viscous drag force, $\eta$ = fluid viscosity, $r$ = sphere radius, $v$ = speed.
A (CN): $F = 6\pi\eta r v$，其中 $F$ = 粘性阻力，$\eta$ = 流体粘度，$r$ = 球体半径，$v$ = 速度。

**Flashcard 2:**
Q (EN): What are the conditions for Stokes' Law to be valid?
Q (CN): 斯托克斯定律成立的条件是什么？
A (EN): Small sphere, low speed, laminar flow (low Reynolds number), incompressible Newtonian fluid, smooth rigid sphere.
A (CN): 小球体、低速、层流（低雷诺数）、不可压缩牛顿流体、光滑刚性球体。

**Flashcard 3:**
Q (EN): How does viscous drag differ from kinetic friction?
Q (CN): 粘性阻力与动摩擦有何不同？
A (EN): Viscous drag is proportional to speed (for laminar flow), while kinetic friction is approximately constant regardless of speed.
A (CN): 粘性阻力与速度成正比（在层流中），而动摩擦与速度无关，近似恒定。

**Flashcard 4:**
Q (EN): Write the derived formula for terminal velocity of a sphere falling through a viscous fluid under Stokes' Law.
Q (CN): 写出在斯托克斯定律下，球体在粘性流体中下落的终端速度推导公式。
A (EN): $v = \frac{2 r^2 g (\rho_{\text{sphere}} - \rho_{\text{fluid}})}{9\eta}$
A (CN): $v = \frac{2 r^2 g (\rho_{\text{sphere}} - \rho_{\text{fluid}})}{9\eta}$

**Flashcard 5:**
Q (EN): What happens to the viscous drag force if the sphere's radius is doubled (all else constant)?
Q (CN): 如果球体半径加倍（其他条件不变），粘性阻力会如何变化？
A (EN): The drag force doubles (since $F \propto r$).
A (CN): 阻力加倍（因为 $F \propto r$）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Viscous Drag and Stokes' Law"
  cn: "粘性阻力与斯托克斯定律"
parent_topic: "Forces in Fluids (Upthrust and Viscous Force)"
parent_hub: "[[Forces in Fluids (Upthrust and Viscous Force)]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Upthrust and Archimedes' Principle]]"
  - "[[Terminal Velocity in Fluids]]"
  - "[[Types of Force]]"
  - "[[Work Done by a Force]]"
language: bilingual_en_cn