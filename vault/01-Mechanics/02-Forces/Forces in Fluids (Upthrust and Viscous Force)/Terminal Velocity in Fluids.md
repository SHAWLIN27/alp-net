Here is the complete bilingual leaf node for **Terminal Velocity in Fluids**, designed as a standalone Obsidian note and knowledge graph leaf node.

---

# 1. Overview / 概述

**English:**
This sub-topic explores what happens when an object falls through a fluid (liquid or gas). Initially, the object accelerates due to [[Types of Force|weight]]. As its speed increases, the [[Viscous Drag and Stokes' Law|viscous drag]] force also increases. Eventually, the drag force (combined with [[Upthrust and Archimedes' Principle|upthrust]]) balances the weight, resulting in zero net force and constant velocity. This constant maximum speed is called **terminal velocity**. This concept is crucial for understanding skydiving, sedimentation, and the motion of particles in fluids. It directly applies Newton's First and Second Laws of Motion.

**中文:**
本子知识点探讨物体在流体（液体或气体）中下落时会发生什么。最初，物体因[[Types of Force|重力]]而加速。随着速度增加，[[Viscous Drag and Stokes' Law|粘性阻力]]也随之增大。最终，阻力（与[[Upthrust and Archimedes' Principle|浮力]]共同作用）与重力平衡，导致合力为零，速度恒定。这个恒定的最大速度称为**终端速度**。这个概念对于理解跳伞、沉淀以及流体中粒子的运动至关重要。它直接应用了牛顿第一和第二运动定律。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Terminal Velocity** / 终端速度 | The constant maximum velocity reached by an object falling through a fluid when the net force acting on it is zero. | 物体在流体中下落时，当作用在其上的合力为零时所达到的恒定最大速度。 |
| **Net Force** / 合力 | The vector sum of all forces acting on an object. | 作用在物体上所有力的矢量和。 |
| **Acceleration** / 加速度 | The rate of change of velocity. It is proportional to the net force acting on an object ($F=ma$). | 速度的变化率。它与作用在物体上的合力成正比 ($F=ma$)。 |
| **Equilibrium** / 平衡 | A state where the net force on an object is zero, resulting in either rest or constant velocity (dynamic equilibrium). | 物体所受合力为零的状态，导致物体静止或匀速运动（动态平衡）。 |
| **Viscous Drag** / 粘性阻力 | A resistive force acting on an object moving through a fluid, opposing its motion. | 物体在流体中运动时，阻碍其运动的阻力。 |

---

# 3. Key Concepts / 关键概念

**English:**
The journey to terminal velocity is a classic example of dynamic equilibrium.

1.  **Initial Stage (t=0):** The object is released from rest. Its velocity $v=0$. Therefore, the [[Viscous Drag and Stokes' Law|viscous drag]] force $F_d = 0$. The only forces acting are [[Types of Force|weight]] $W$ downwards and [[Upthrust and Archimedes' Principle|upthrust]] $U$ upwards. The net force $F_{net} = W - U$ is downwards, so the object accelerates downwards ($a = F_{net}/m$).

2.  **Acceleration Phase:** As the object speeds up, the drag force $F_d$ increases (for a sphere, $F_d \propto v$ at low speeds, or $F_d \propto v^2$ at higher speeds). The net force decreases: $F_{net} = W - U - F_d$. Consequently, the acceleration decreases. The object is still speeding up, but at a decreasing rate.

3.  **Terminal Velocity (Equilibrium):** Eventually, the drag force grows large enough that $F_d + U = W$. The net force becomes zero ($F_{net} = 0$). According to Newton's First Law, the object will now continue moving at a constant velocity. This constant velocity is the **terminal velocity**, $v_t$.

**Common Pitfall:** Students often think that when net force is zero, the object stops. This is incorrect. Zero net force means **no change** in velocity (no acceleration), not zero velocity. The object continues at its terminal velocity.

**中文:**
到达终端速度的过程是动态平衡的经典例子。

1.  **初始阶段 (t=0):** 物体从静止释放。其速度 $v=0$。因此，[[Viscous Drag and Stokes' Law|粘性阻力]] $F_d = 0$。作用在其上的力只有向下的[[Types of Force|重力]] $W$ 和向上的[[Upthrust and Archimedes' Principle|浮力]] $U$。合力 $F_{net} = W - U$ 向下，因此物体向下加速 ($a = F_{net}/m$)。

2.  **加速阶段:** 随着物体加速，阻力 $F_d$ 增大（对于球体，低速时 $F_d \propto v$，高速时 $F_d \propto v^2$）。合力减小：$F_{net} = W - U - F_d$。因此，加速度减小。物体仍在加速，但加速的速率在减小。

3.  **终端速度（平衡）:** 最终，阻力增大到足以使 $F_d + U = W$。合力变为零 ($F_{net} = 0$)。根据牛顿第一定律，物体将保持匀速运动。这个恒定速度就是**终端速度** $v_t$。

**常见误区:** 学生常认为当合力为零时，物体会停止。这是错误的。合力为零意味着速度**不变**（无加速度），而不是速度为零。物体会以其终端速度继续运动。

---

# 4. Formulas / 公式

For an object falling through a fluid, the condition for terminal velocity is:

$$ W = U + F_d $$

Or, in terms of forces:

$$ mg = \rho_{fluid} V g + F_d $$

Where $F_d$ is the drag force at terminal velocity.

For a small sphere falling at low speed (laminar flow), using [[Viscous Drag and Stokes' Law|Stokes' Law]] ($F_d = 6\pi \eta r v$), the terminal velocity $v_t$ can be derived:

$$ mg = \rho_{fluid} V g + 6\pi \eta r v_t $$

$$ \frac{4}{3}\pi r^3 \rho_{sphere} g = \frac{4}{3}\pi r^3 \rho_{fluid} g + 6\pi \eta r v_t $$

$$ v_t = \frac{2r^2 g (\rho_{sphere} - \rho_{fluid})}{9\eta} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v_t$ | Terminal velocity | 终端速度 | m s$^{-1}$ |
| $r$ | Radius of sphere | 球体半径 | m |
| $g$ | Acceleration due to gravity | 重力加速度 | m s$^{-2}$ |
| $\rho_{sphere}$ | Density of sphere | 球体密度 | kg m$^{-3}$ |
| $\rho_{fluid}$ | Density of fluid | 流体密度 | kg m$^{-3}$ |
| $\eta$ | Dynamic viscosity of fluid | 流体动力粘度 | Pa s (or N s m$^{-2}$) |

**Derivation / 推导:**
1.  State equilibrium condition: $W = U + F_d$.
2.  Substitute expressions: $mg = \rho_{fluid} V g + 6\pi \eta r v_t$.
3.  Substitute mass ($m = \rho_{sphere} V$) and volume ($V = \frac{4}{3}\pi r^3$).
4.  Rearrange to solve for $v_t$.

**Conditions / 适用条件:**
- The formula $v_t = \frac{2r^2 g (\rho_{sphere} - \rho_{fluid})}{9\eta}$ is derived from [[Viscous Drag and Stokes' Law|Stokes' Law]].
- It only applies to **small spheres** moving at **low speeds** in a **laminar flow** regime (Reynolds number < 1).
- For larger objects or higher speeds (e.g., a skydiver), the drag force is proportional to $v^2$, and a different, empirical formula is needed.

> 📷 **IMAGE PROMPT — FVF-TV-01: Forces Reaching Equilibrium**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a sphere falling through a fluid. Three vertical arrows originate from the center of the sphere. A long, thick red arrow labeled "Weight (W)" points downwards. A medium-length blue arrow labeled "Upthrust (U)" points upwards. A short green arrow labeled "Drag (F_d)" points upwards. The diagram is split into three stages side-by-side: Stage 1 (t=0, v=0) shows only W and U, with a large net force. Stage 2 (accelerating) shows W, U, and a growing F_d, with a smaller net force. Stage 3 (v = v_t) shows all three arrows, with W = U + F_d, and a label "Net Force = 0". Clean white background, black text labels.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示一个球体在流体中下落。从球心发出三个垂直箭头。一个长而粗的红色箭头标为“重力 (W)”，指向下方。一个中等长度的蓝色箭头标为“浮力 (U)”，指向上方。一个短的绿色箭头标为“阻力 (F_d)”，指向上方。该图并排分为三个阶段：阶段1 (t=0, v=0) 只显示 W 和 U，合力很大。阶段2 (加速中) 显示 W、U 和一个增长的 F_d，合力较小。阶段3 (v = v_t) 显示所有三个箭头，W = U + F_d，并标有“合力 = 0”。干净的白色背景，黑色文字标签。
>
> **Labels Required / 需要标注:**
> * Weight (W)
> * Upthrust (U)
> * Drag (F_d)
> * Net Force = 0
> * v = 0, v increasing, v = v_t
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This is the most common diagram used to explain the concept of terminal velocity. Students must be able to draw and label the forces at each stage.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — FVF-TV-02: Velocity-Time Graph for Terminal Velocity**
>
> **English Prompt:**
> A graph of velocity (y-axis, m/s) vs. time (x-axis, s). The curve starts at the origin (0,0) with a steep positive slope (high acceleration). The slope gradually decreases (curves over) and becomes horizontal (zero slope) at a value labeled "Terminal Velocity (v_t)". The curve is smooth and asymptotic. The axes are clearly labeled with units. A small inset diagram shows a sphere with force arrows at three points on the curve: at the start (large net force), in the middle (smaller net force), and at the end (net force = 0). Clean white background, black lines, blue curve.
>
> **中文描述:**
> 一个速度 (y轴, m/s) 对时间 (x轴, s) 的图表。曲线从原点 (0,0) 开始，具有陡峭的正斜率（高加速度）。斜率逐渐减小（曲线变平缓），并在标有“终端速度 (v_t)”的值处变为水平（零斜率）。曲线平滑且渐近。坐标轴清晰标注了单位。一个小插图在曲线上的三个点显示了带有力箭头的球体：起点（合力大）、中间（合力较小）和终点（合力为零）。干净的白色背景，黑色线条，蓝色曲线。
>
> **Labels Required / 需要标注:**
> * Velocity / m s$^{-1}$
> * Time / s
> * Terminal Velocity (v_t)
> * Acceleration decreasing
> * Constant velocity
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This graph is a very common exam question. Students must be able to sketch it, explain its shape, and identify the terminal velocity region.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A small steel ball bearing of radius 0.50 mm is dropped into a large tank of glycerine. The density of steel is 7800 kg m$^{-3}$, the density of glycerine is 1260 kg m$^{-3}$, and the viscosity of glycerine is 1.5 Pa s. Calculate the terminal velocity of the ball bearing. (Assume Stokes' Law applies.)

**中文:**
将一颗半径为 0.50 mm 的小钢珠丢入一个盛满甘油的大槽中。钢的密度为 7800 kg m$^{-3}$，甘油的密度为 1260 kg m$^{-3}$，甘油的粘度为 1.5 Pa s。计算该钢珠的终端速度。（假设适用斯托克斯定律。）

### Solution / 解答
1.  **Identify knowns:**
    $r = 0.50 \text{ mm} = 0.50 \times 10^{-3} \text{ m} = 5.0 \times 10^{-4} \text{ m}$
    $\rho_{sphere} = 7800 \text{ kg m}^{-3}$
    $\rho_{fluid} = 1260 \text{ kg m}^{-3}$
    $\eta = 1.5 \text{ Pa s}$
    $g = 9.81 \text{ m s}^{-2}$

2.  **Apply the formula for terminal velocity (Stokes' Law):**
    $$ v_t = \frac{2r^2 g (\rho_{sphere} - \rho_{fluid})}{9\eta} $$

3.  **Substitute values:**
    $$ v_t = \frac{2 \times (5.0 \times 10^{-4})^2 \times 9.81 \times (7800 - 1260)}{9 \times 1.5} $$

4.  **Calculate step-by-step:**
    $$ r^2 = (5.0 \times 10^{-4})^2 = 2.5 \times 10^{-7} \text{ m}^2 $$
    $$ \rho_{sphere} - \rho_{fluid} = 7800 - 1260 = 6540 \text{ kg m}^{-3} $$
    $$ \text{Numerator} = 2 \times 2.5 \times 10^{-7} \times 9.81 \times 6540 $$
    $$ \text{Numerator} = 2 \times 2.5 \times 10^{-7} \times 9.81 \times 6540 = 3.207 \times 10^{-2} $$
    $$ \text{Denominator} = 9 \times 1.5 = 13.5 $$
    $$ v_t = \frac{3.207 \times 10^{-2}}{13.5} = 2.38 \times 10^{-3} \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** $2.4 \times 10^{-3} \text{ m s}^{-1}$ (to 2 significant figures)
**答案:** $2.4 \times 10^{-3} \text{ m s}^{-1}$

### Quick Tip / 提示
Always convert all lengths to meters (m) before substituting into the formula. A common mistake is to use mm or cm directly. Also, check the units of viscosity; if it's in mPa s, you must convert to Pa s.

---

# 7. Flashcards / 闪卡

**Q (EN):** What is terminal velocity?
**Q (CN):** 什么是终端速度？
**A (EN):** The constant maximum velocity reached by an object falling through a fluid when the net force acting on it is zero.
**A (CN):** 物体在流体中下落时，当作用在其上的合力为零时所达到的恒定最大速度。

**Q (EN):** What are the three forces acting on a sphere falling through a fluid?
**Q (CN):** 作用在流体中下落的球体上的三个力是什么？
**A (EN):** Weight (downwards), Upthrust (upwards), and Viscous Drag (upwards).
**A (CN):** 重力（向下）、浮力（向上）和粘性阻力（向上）。

**Q (EN):** What is the condition for an object to be at terminal velocity?
**Q (CN):** 物体达到终端速度的条件是什么？
**A (EN):** The net force is zero. Weight = Upthrust + Drag.
**A (CN):** 合力为零。重力 = 浮力 + 阻力。

**Q (EN):** How does the acceleration of a falling object change as it approaches terminal velocity?
**Q (CN):** 下落物体的加速度在接近终端速度时如何变化？
**A (EN):** The acceleration decreases from its initial value (g) and becomes zero at terminal velocity.
**A (CN):** 加速度从其初始值 (g) 减小，并在终端速度时变为零。

**Q (EN):** State one factor that affects the terminal velocity of a sphere.
**Q (CN):** 说出一个影响球体终端速度的因素。
**A (EN):** The radius of the sphere (larger radius = higher terminal velocity), or the density difference (larger difference = higher terminal velocity), or the viscosity of the fluid (higher viscosity = lower terminal velocity).
**A (CN):** 球体的半径（半径越大，终端速度越高），或密度差（密度差越大，终端速度越高），或流体的粘度（粘度越高，终端速度越低）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Terminal Velocity in Fluids
  cn: 流体中的终端速度
parent_topic: Forces in Fluids (Upthrust and Viscous Force)
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
  - "[[Viscous Drag and Stokes' Law]]"
  - "[[Types of Force]]"
language: bilingual_en_cn