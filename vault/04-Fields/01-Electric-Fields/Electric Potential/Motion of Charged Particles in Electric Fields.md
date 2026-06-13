---
# Motion of Charged Particles in Electric Fields / 带电粒子在电场中的运动

---

# 1. Overview / 概述

**English:**
This sub-topic explores the behavior of charged particles (such as electrons, protons, and ions) when placed in uniform or non-uniform electric fields. It bridges the concepts of [[Electric Fields and Coulomb's Law]] with [[Electric Potential (V)]] and [[Electric Potential Energy]], applying Newtonian mechanics to electrostatic scenarios. Understanding this motion is crucial for explaining the operation of devices like cathode ray tubes (CRTs), particle accelerators, and mass spectrometers. The core principle is that an electric field exerts a force $F = qE$ on a charged particle, causing acceleration according to $F = ma$. This sub-topic focuses on calculating trajectories, velocities, and kinetic energy changes, often using energy conservation ($\Delta E_k = - \Delta E_p = qV$) as a powerful alternative to kinematic analysis.

**中文:**
本子知识点探讨带电粒子（如电子、质子和离子）在匀强或非匀强电场中的运动行为。它连接了[[Electric Fields and Coulomb's Law]]与[[Electric Potential (V)]]和[[Electric Potential Energy]]的概念，将牛顿力学应用于静电学场景。理解这种运动对于解释阴极射线管（CRT）、粒子加速器和质谱仪等设备的工作原理至关重要。核心原理是电场对带电粒子施加力 $F = qE$，根据 $F = ma$ 引起加速度。本子知识点侧重于计算轨迹、速度和动能变化，通常使用能量守恒（$\Delta E_k = - \Delta E_p = qV$）作为运动学分析的有力替代方案。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (18.2 a-f) | Edexcel IAL (WPH14 U4: 2.6-2.10) |
|-----------|-------------|
| Describe and analyse the motion of charged particles in uniform electric fields. | Understand the motion of charged particles in uniform electric fields. |
| Calculate the acceleration of a charged particle in an electric field. | Calculate the force on a charged particle in an electric field. |
| Apply the principle of conservation of energy to charged particles moving in electric fields. | Apply the work-energy principle to charged particles in electric fields. |
| Derive and use the equation for the speed of a particle accelerated from rest through a potential difference $V$: $v = \sqrt{\frac{2qV}{m}}$. | Derive and use $v = \sqrt{\frac{2qV}{m}}$ for a particle accelerated from rest. |
| Analyse the deflection of charged particles in electric fields (e.g., in a cathode ray tube). | Analyse the trajectory of a charged particle moving perpendicular to a uniform electric field. |
| Describe the use of electric fields in particle accelerators and other applications. | Understand the principles of a simple mass spectrometer. |

**Examiner Expectations / 考官期望:**
- **EN:** Students must be able to combine kinematics equations with $F = qE$ and $F = ma$. They must also be able to use energy conservation ($\Delta E_k = qV$) to find speeds, especially for particles accelerated through a potential difference. For deflection problems, treat the motion as projectile motion under constant acceleration.
- **CN:** 学生必须能够将运动学方程与 $F = qE$ 和 $F = ma$ 结合。他们还必须能够使用能量守恒（$\Delta E_k = qV$）来求速度，特别是对于通过电势差加速的粒子。对于偏转问题，应将运动视为恒定加速度下的抛体运动。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Electric Force** / 电场力 | The force $F$ experienced by a charge $q$ in an electric field $E$, given by $F = qE$. | 电荷 $q$ 在电场 $E$ 中受到的力 $F$，由 $F = qE$ 给出。 | Confusing $F = qE$ with $F = \frac{kQq}{r^2}$ (Coulomb's law). The former is for a field, the latter is for point charges. |
| **Acceleration** / 加速度 | The rate of change of velocity of a charged particle in an electric field, $a = \frac{F}{m} = \frac{qE}{m}$. | 带电粒子在电场中的速度变化率，$a = \frac{F}{m} = \frac{qE}{m}$。 | Forgetting that the acceleration is constant only in a **uniform** electric field. |
| **Kinetic Energy Gain** / 动能增益 | The increase in kinetic energy of a charged particle accelerated through a potential difference $V$, given by $\Delta E_k = qV$. | 带电粒子通过电势差 $V$ 加速后动能的增加量，由 $\Delta E_k = qV$ 给出。 | Using $\Delta E_k = qV$ only works if the particle starts from rest or if you know the change in potential. |
| **Deflection** / 偏转 | The change in direction of a charged particle's path when it enters an electric field at an angle (usually perpendicular). | 带电粒子以一定角度（通常垂直）进入电场时其路径方向的改变。 | Treating deflection as a simple angle change without considering the parabolic trajectory. |
| **Trajectory** / 轨迹 | The path followed by a charged particle moving in an electric field. In a uniform field, this is a parabola. | 带电粒子在电场中运动所遵循的路径。在匀强电场中，这是一条抛物线。 | Assuming the trajectory is a straight line unless the particle is moving parallel to the field lines. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Acceleration in a Uniform Field / 在匀强电场中的加速度

### Explanation / 解释
**English:** When a charged particle of charge $q$ and mass $m$ is placed in a uniform electric field $E$, it experiences a constant force $F = qE$. According to Newton's second law ($F = ma$), this results in a constant acceleration $a = \frac{qE}{m}$. The direction of the acceleration is the same as the direction of the force. For a positive charge, the acceleration is in the direction of the field ($E$). For a negative charge (like an electron), the acceleration is opposite to the field direction. This constant acceleration allows us to use the standard [[Kinematics]] equations ($s = ut + \frac{1}{2}at^2$, $v = u + at$, $v^2 = u^2 + 2as$) to describe the motion.

**中文:** 当带电量为 $q$、质量为 $m$ 的带电粒子置于匀强电场 $E$ 中时，它会受到恒定的力 $F = qE$。根据牛顿第二定律（$F = ma$），这会产生恒定的加速度 $a = \frac{qE}{m}$。加速度的方向与力的方向相同。对于正电荷，加速度方向与电场方向（$E$）相同。对于负电荷（如电子），加速度方向与电场方向相反。这种恒定加速度使我们能够使用标准的[[Kinematics]]方程（$s = ut + \frac{1}{2}at^2$, $v = u + at$, $v^2 = u^2 + 2as$）来描述运动。

### Physical Meaning / 物理意义
**English:** The electric field does work on the particle, converting [[Electric Potential Energy]] into kinetic energy. The acceleration is a measure of how quickly the particle's velocity changes due to this energy conversion. A stronger field or a smaller mass leads to a larger acceleration.

**中文:** 电场对粒子做功，将[[Electric Potential Energy]]转化为动能。加速度是衡量粒子由于这种能量转换而改变速度快慢的指标。更强的场或更小的质量会导致更大的加速度。

### Common Misconceptions / 常见误区
- **EN:** Thinking the acceleration depends on the particle's velocity. In a uniform field, acceleration is constant and independent of velocity.
- **CN:** 认为加速度取决于粒子的速度。在匀强电场中，加速度是恒定的，与速度无关。
- **EN:** Confusing the direction of force on a positive vs. negative charge. Remember: $F = qE$, so the sign of $q$ matters.
- **CN:** 混淆正电荷和负电荷所受力的方向。记住：$F = qE$，所以 $q$ 的符号很重要。

### Exam Tips / 考试提示
- **EN:** Always draw a free-body diagram showing the electric force. Then resolve forces if the field is not aligned with the motion.
- **CN:** 始终画出显示电场力的受力分析图。如果电场方向与运动方向不一致，则进行力的分解。

> 📷 **IMAGE PROMPT — ACCEL: Positive vs Negative Charge**
> A diagram showing a uniform electric field between two parallel plates (top plate positive, bottom plate negative). A positive charge (red sphere with '+') is shown accelerating downwards (direction of E field). A negative charge (blue sphere with '-') is shown accelerating upwards (opposite to E field). Arrows labeled 'F' and 'a' are drawn on each particle. The field lines are shown as equally spaced vertical arrows pointing from top to bottom.

## 4.2 Energy Conservation Approach / 能量守恒方法

### Explanation / 解释
**English:** A powerful alternative to using kinematics is the principle of conservation of energy. When a charged particle moves through a potential difference $V$, its [[Electric Potential Energy]] changes by $\Delta E_p = qV$. If no other forces (like gravity or friction) do work, this change in potential energy is converted entirely into kinetic energy. For a particle accelerated from rest through a potential difference $V$, we have:
$$ \frac{1}{2}mv^2 = qV $$
This gives the final speed:
$$ v = \sqrt{\frac{2qV}{m}} $$
This equation is extremely useful because it bypasses the need to know the field strength or the distance traveled. It only depends on the charge, mass, and potential difference.

**中文:** 使用能量守恒原理是运动学分析的一个强大替代方案。当带电粒子通过电势差 $V$ 运动时，其[[Electric Potential Energy]]变化量为 $\Delta E_p = qV$。如果没有其他力（如重力或摩擦力）做功，这个势能变化将完全转化为动能。对于从静止开始通过电势差 $V$ 加速的粒子，我们有：
$$ \frac{1}{2}mv^2 = qV $$
这给出了最终速度：
$$ v = \sqrt{\frac{2qV}{m}} $$
这个方程非常有用，因为它绕过了需要知道场强或行进距离的问题。它只取决于电荷、质量和电势差。

### Physical Meaning / 物理意义
**English:** The potential difference $V$ is a measure of the "electrical push" given to the particle. A larger $V$ gives the particle more kinetic energy. The charge $q$ determines how strongly the particle couples to the electric field. The mass $m$ determines how much inertia the particle has.

**中文:** 电势差 $V$ 是给予粒子的“电推力”的量度。更大的 $V$ 给粒子更多的动能。电荷 $q$ 决定了粒子与电场耦合的强度。质量 $m$ 决定了粒子有多少惯性。

### Common Misconceptions / 常见误区
- **EN:** Using $\frac{1}{2}mv^2 = qV$ when the particle does not start from rest. The correct form is $\frac{1}{2}mv^2 - \frac{1}{2}mu^2 = qV$.
- **CN:** 当粒子不是从静止开始时使用 $\frac{1}{2}mv^2 = qV$。正确的形式是 $\frac{1}{2}mv^2 - \frac{1}{2}mu^2 = qV$。
- **EN:** Forgetting the sign of $q$. If a negative charge moves through a positive potential difference, it loses potential energy and gains kinetic energy. The equation $\frac{1}{2}mv^2 = qV$ still works if you use the correct sign for $q$ and $V$.
- **CN:** 忘记 $q$ 的符号。如果负电荷通过正电势差，它会失去势能并获得动能。如果你对 $q$ 和 $V$ 使用正确的符号，方程 $\frac{1}{2}mv^2 = qV$ 仍然有效。

### Exam Tips / 考试提示
- **EN:** This is a very common exam question. Memorize $v = \sqrt{\frac{2qV}{m}}$ and know when to apply it.
- **CN:** 这是一个非常常见的考试问题。记住 $v = \sqrt{\frac{2qV}{m}}$ 并知道何时应用它。

## 4.3 Deflection in a Uniform Field (Projectile Motion) / 在匀强电场中的偏转（抛体运动）

### Explanation / 解释
**English:** When a charged particle enters a uniform electric field with an initial velocity perpendicular to the field lines, it behaves like a projectile in a gravitational field. The electric force provides a constant acceleration perpendicular to the initial velocity. This results in a parabolic trajectory. We can analyze this by resolving the motion into two independent components:
1.  **Parallel to the field (y-direction):** Constant acceleration $a_y = \frac{qE}{m}$. Use $s_y = u_y t + \frac{1}{2}a_y t^2$ and $v_y = u_y + a_y t$.
2.  **Perpendicular to the field (x-direction):** Constant velocity $v_x = u_x$. Use $s_x = v_x t$.

**中文:** 当带电粒子以垂直于电场线的初速度进入匀强电场时，它的行为就像在重力场中的抛体。电场力提供一个垂直于初速度的恒定加速度。这导致抛物线轨迹。我们可以通过将运动分解为两个独立的分量来分析：
1.  **平行于电场方向（y方向）：** 恒定加速度 $a_y = \frac{qE}{m}$。使用 $s_y = u_y t + \frac{1}{2}a_y t^2$ 和 $v_y = u_y + a_y t$。
2.  **垂直于电场方向（x方向）：** 恒定速度 $v_x = u_x$。使用 $s_x = v_x t$。

### Physical Meaning / 物理意义
**English:** The particle's path is curved because the electric force continuously changes its velocity component in the direction of the field. The horizontal component of velocity remains unchanged, while the vertical component increases linearly with time.

**中文:** 粒子的路径是弯曲的，因为电场力不断改变其在电场方向上的速度分量。速度的水平分量保持不变，而垂直分量随时间线性增加。

### Common Misconceptions / 常见误区
- **EN:** Thinking the particle's speed is constant. The speed increases because the particle gains kinetic energy from the field.
- **CN:** 认为粒子的速度是恒定的。速度会增加，因为粒子从电场中获得动能。
- **EN:** Forgetting that the acceleration is only in the direction of the field. The velocity component perpendicular to the field is constant.
- **CN:** 忘记加速度只在电场方向上。垂直于电场的速度分量是恒定的。

### Exam Tips / 考试提示
- **EN:** Treat this exactly like projectile motion. Set up your $x$ and $y$ equations separately. The time of flight is usually determined by the horizontal motion ($t = \frac{L}{v_x}$, where $L$ is the plate length).
- **CN:** 完全像处理抛体运动一样处理。分别建立 $x$ 和 $y$ 方程。飞行时间通常由水平运动决定（$t = \frac{L}{v_x}$，其中 $L$ 是板长）。

> 📷 **IMAGE PROMPT — DEFLECTION: Parabolic Trajectory**
> A diagram showing two parallel plates (top positive, bottom negative). A beam of electrons enters horizontally from the left between the plates. The path of the electrons is shown as a curved line bending upwards (towards the positive plate). The path is labeled as a parabola. The horizontal velocity $v_x$ is shown as a constant arrow. The vertical velocity $v_y$ is shown increasing as the particle moves. The plate length $L$ and vertical deflection $y$ are labeled.

---

# 5. Essential Equations / 核心公式

## Equation 1: Force on a Charged Particle / 带电粒子所受的力

$$ F = qE $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $F$ | Electric force | 电场力 | N (牛顿) |
| $q$ | Charge of the particle | 粒子的电荷 | C (库仑) |
| $E$ | Electric field strength | 电场强度 | N C$^{-1}$ or V m$^{-1}$ |

**Derivation / 推导:** This is the definition of electric field strength: $E = \frac{F}{q}$.
**Conditions / 适用条件:** The field must be uniform, or the force is the instantaneous force at a point in a non-uniform field.
**Limitations / 局限性:** Does not account for relativistic effects at very high speeds.

## Equation 2: Acceleration of a Charged Particle / 带电粒子的加速度

$$ a = \frac{F}{m} = \frac{qE}{m} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $a$ | Acceleration | 加速度 | m s$^{-2}$ |
| $m$ | Mass of the particle | 粒子的质量 | kg |

**Derivation / 推导:** From Newton's second law $F = ma$ and $F = qE$.
**Conditions / 适用条件:** Constant mass, non-relativistic speeds.
**Limitations / 局限性:** $a$ is constant only in a uniform field.

## Equation 3: Kinetic Energy Gain from Potential Difference / 从电势差获得的动能

$$ \Delta E_k = qV $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta E_k$ | Change in kinetic energy | 动能变化 | J (焦耳) |
| $V$ | Potential difference | 电势差 | V (伏特) |

**Derivation / 推导:** Work done by the field $W = Fd = qEd = qV$ (since $V = Ed$ for a uniform field). This work equals the change in kinetic energy.
**Conditions / 适用条件:** No other forces doing work. Particle moves from one point to another with potential difference $V$.
**Limitations / 局限性:** Does not account for energy lost to radiation or other processes.

## Equation 4: Speed of a Particle Accelerated from Rest / 从静止加速的粒子速度

$$ v = \sqrt{\frac{2qV}{m}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v$ | Final speed | 最终速度 | m s$^{-1}$ |
| $q$ | Charge | 电荷 | C |
| $V$ | Potential difference | 电势差 | V |
| $m$ | Mass | 质量 | kg |

**Derivation / 推导:** From $\frac{1}{2}mv^2 = qV$.
**Conditions / 适用条件:** Particle starts from rest.
**Limitations / 局限性:** Non-relativistic speeds only.

> 📋 **CIE Only:** CIE often asks students to derive this equation from energy conservation.
> 📋 **Edexcel Only:** Edexcel frequently uses this in the context of mass spectrometry to find the speed of ions.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Velocity vs. Time for a Particle Accelerated from Rest / 从静止加速的粒子速度-时间图

### Axes / 坐标轴
- **x-axis:** Time / 时间 $t$ (s)
- **y-axis:** Velocity / 速度 $v$ (m s$^{-1}$)

### Shape / 形状
A straight line with a positive slope passing through the origin.

### Gradient Meaning / 斜率含义
The gradient is the acceleration $a = \frac{qE}{m}$.

### Area Meaning / 面积含义
The area under the graph is the distance traveled $s$.

### Exam Interpretation / 考试解读
- **EN:** A steeper line means a larger acceleration (either larger $q$, larger $E$, or smaller $m$).
- **CN:** 更陡的线意味着更大的加速度（要么 $q$ 更大，$E$ 更大，或者 $m$ 更小）。

## 6.2 Kinetic Energy vs. Potential Difference / 动能-电势差图

### Axes / 坐标轴
- **x-axis:** Potential Difference / 电势差 $V$ (V)
- **y-axis:** Kinetic Energy / 动能 $E_k$ (J)

### Shape / 形状
A straight line passing through the origin with a positive slope.

### Gradient Meaning / 斜率含义
The gradient is the charge $q$ of the particle.

### Area Meaning / 面积含义
N/A

### Exam Interpretation / 考试解读
- **EN:** A steeper line means a larger charge. For a given $V$, a particle with a larger $q$ gains more kinetic energy.
- **CN:** 更陡的线意味着更大的电荷。对于给定的 $V$，具有更大 $q$ 的粒子获得更多动能。

---

# 7. Required Diagrams / 必备图表

## 7.1 Parallel Plate Deflection / 平行板偏转

### Description / 描述
**English:** A diagram showing a charged particle (e.g., an electron) entering a uniform electric field between two parallel plates. The particle's parabolic trajectory is shown, with the initial velocity $v_0$ horizontal, the plate length $L$, the plate separation $d$, the potential difference $V$ across the plates, and the vertical deflection $y$ at the point of exit.

**中文:** 一个显示带电粒子（例如电子）进入两个平行板之间的匀强电场的示意图。显示了粒子的抛物线轨迹，标有初速度 $v_0$（水平）、板长 $L$、板间距 $d$、板间电势差 $V$ 以及出口点的垂直偏转 $y$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DEFLECTION_DIAG: Parallel Plate Deflection**
> A clean physics diagram. Two parallel horizontal plates, one above the other. The top plate is labeled '+V' and the bottom plate is labeled '0V' or 'ground'. The space between them is labeled 'Uniform Electric Field E'. An electron (blue circle with '-') enters from the left, moving horizontally with velocity $v_0$. Its path curves upwards in a parabola. The horizontal distance from entry to exit is labeled 'L' (plate length). The vertical distance from the entry point to the exit point is labeled 'y' (deflection). Arrows show the horizontal velocity $v_x$ (constant) and the increasing vertical velocity $v_y$. The field lines are shown as equally spaced vertical arrows pointing from top to bottom.

### Labels Required / 需要标注
- **EN:** $v_0$ (initial velocity), $L$ (plate length), $y$ (deflection), $E$ (field), $+V$ and $0V$ (plate potentials), $v_x$ and $v_y$ (velocity components).
- **CN:** $v_0$（初速度），$L$（板长），$y$（偏转），$E$（电场），$+V$ 和 $0V$（板电势），$v_x$ 和 $v_y$（速度分量）。

### Exam Importance / 考试重要性
- **EN:** This is the most common diagram for this sub-topic. Students must be able to draw it, label it, and use it to derive equations for deflection.
- **CN:** 这是本子知识点最常见的图表。学生必须能够画出它、标注它，并用它来推导偏转方程。

## 7.2 Linear Accelerator (Simple) / 线性加速器（简单）

### Description / 描述
**English:** A diagram showing a series of hollow metal cylinders (drift tubes) connected to an alternating voltage source. A charged particle is accelerated across the gaps between the tubes. The diagram should show the particle gaining speed as it moves through each gap.

**中文:** 一个显示一系列连接到交流电压源的中空金属圆柱体（漂移管）的示意图。带电粒子在管间的间隙中被加速。该图应显示粒子在通过每个间隙时速度增加。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — LINAC: Simple Linear Accelerator**
> A diagram showing a series of 4-5 hollow metal cylinders (drift tubes) arranged in a line. The gaps between the cylinders are labeled 'Acceleration Gap'. An alternating voltage source (AC) is connected to the cylinders. A positive ion (red sphere with '+') is shown entering from the left. Arrows of increasing length between the gaps indicate the particle is speeding up. The cylinders are labeled 'Drift Tube 1', 'Drift Tube 2', etc.

### Labels Required / 需要标注
- **EN:** Drift tubes, acceleration gaps, AC source, particle path, increasing speed.
- **CN:** 漂移管，加速间隙，交流电源，粒子路径，速度增加。

### Exam Importance / 考试重要性
- **EN:** This is a common application question. Students should understand the principle of how the alternating voltage ensures the particle is always accelerated.
- **CN:** 这是一个常见的应用题。学生应该理解交流电压如何确保粒子始终被加速的原理。

---

# 8. Worked Examples / 典型例题

## Example 1: Electron Accelerated from Rest / 从静止加速的电子

### Question / 题目
**English:** An electron is accelerated from rest through a potential difference of 500 V. Calculate the final speed of the electron. (Mass of electron $m_e = 9.11 \times 10^{-31}$ kg, charge of electron $e = 1.60 \times 10^{-19}$ C)

**中文:** 一个电子从静止开始通过 500 V 的电势差加速。计算电子的最终速度。（电子质量 $m_e = 9.11 \times 10^{-31}$ kg，电子电荷 $e = 1.60 \times 10^{-19}$ C）

### Solution / 解答
1.  **Identify the principle / 确定原理:** Energy conservation. The kinetic energy gained equals the electrical potential energy lost.
    $$ \frac{1}{2}mv^2 = eV $$
2.  **Rearrange for $v$ / 解出 $v$:**
    $$ v = \sqrt{\frac{2eV}{m}} $$
3.  **Substitute values / 代入数值:**
    $$ v = \sqrt{\frac{2 \times (1.60 \times 10^{-19}) \times 500}{9.11 \times 10^{-31}}} $$
4.  **Calculate / 计算:**
    $$ v = \sqrt{\frac{1.60 \times 10^{-16}}{9.11 \times 10^{-31}}} $$
    $$ v = \sqrt{1.756 \times 10^{14}} $$
    $$ v = 1.33 \times 10^7 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** $1.33 \times 10^7$ m s$^{-1}$ | **答案：** $1.33 \times 10^7$ 米/秒

### Quick Tip / 提示
- **EN:** Always check if the speed is non-relativistic (<< $3 \times 10^8$ m/s). If it is a significant fraction of the speed of light, relativistic equations are needed (A-Level does not require this).
- **CN:** 始终检查速度是否是非相对论性的（<< $3 \times 10^8$ 米/秒）。如果它是光速的很大一部分，则需要相对论方程（A-Level 不要求这个）。

## Example 2: Deflection of an Electron in a CRT / 电子在阴极射线管中的偏转

### Question / 题目
**English:** An electron enters a uniform electric field between two parallel plates of length $L = 5.0$ cm. The field strength is $E = 2.0 \times 10^4$ N C$^{-1}$ directed upwards. The initial horizontal velocity of the electron is $v_0 = 3.0 \times 10^7$ m s$^{-1}$. Calculate the vertical deflection $y$ of the electron as it exits the plates. (Mass of electron $m_e = 9.11 \times 10^{-31}$ kg, charge of electron $e = 1.60 \times 10^{-19}$ C)

**中文:** 一个电子进入两个长度为 $L = 5.0$ cm 的平行板之间的匀强电场。电场强度为 $E = 2.0 \times 10^4$ N C$^{-1}$，方向向上。电子的水平初速度为 $v_0 = 3.0 \times 10^7$ m s$^{-1}$。计算电子离开板时的垂直偏转 $y$。（电子质量 $m_e = 9.11 \times 10^{-31}$ kg，电子电荷 $e = 1.60 \times 10^{-19}$ C）

### Solution / 解答
1.  **Find the acceleration / 求加速度:**
    The force on the electron is $F = eE = (1.60 \times 10^{-19})(2.0 \times 10^4) = 3.2 \times 10^{-15}$ N.
    The acceleration is $a = \frac{F}{m} = \frac{3.2 \times 10^{-15}}{9.11 \times 10^{-31}} = 3.51 \times 10^{15}$ m s$^{-2}$.
    *Direction:* The field is upwards, but the electron is negative, so the force (and acceleration) is downwards.

2.  **Find the time of flight / 求飞行时间:**
    The horizontal velocity is constant. $t = \frac{L}{v_0} = \frac{0.05}{3.0 \times 10^7} = 1.67 \times 10^{-9}$ s.

3.  **Find the vertical deflection / 求垂直偏转:**
    Use $s = ut + \frac{1}{2}at^2$. The initial vertical velocity $u = 0$.
    $$ y = \frac{1}{2}at^2 = \frac{1}{2} \times (3.51 \times 10^{15}) \times (1.67 \times 10^{-9})^2 $$
    $$ y = \frac{1}{2} \times 3.51 \times 10^{15} \times 2.79 \times 10^{-18} $$
    $$ y = 4.90 \times 10^{-3} \text{ m} = 4.9 \text{ mm} $$

### Final Answer / 最终答案
**Answer:** 4.9 mm | **答案：** 4.9 毫米

### Quick Tip / 提示
- **EN:** The deflection is proportional to $\frac{1}{v_0^2}$. A faster electron is deflected less.
- **CN:** 偏转与 $\frac{1}{v_0^2}$ 成正比。更快的电子偏转更少。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate speed from $V$ / 从 $V$ 计算速度 | Very High / 非常高 | Easy / 简单 | 📝 *待填入* |
| Deflection in parallel plates / 平行板偏转 | High / 高 | Medium / 中等 | 📝 *待填入* |
| Derivation of $v = \sqrt{2qV/m}$ / 推导 $v = \sqrt{2qV/m}$ | Medium / 中 | Medium / 中等 | 📝 *待填入* |
| Applications (CRT, mass spec) / 应用（CRT，质谱） | Medium / 中 | Hard / 困难 | 📝 *待填入* |
| Comparing electron and proton / 比较电子和质子 | Low / 低 | Medium / 中等 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Calculate, Derive, Show that, Determine, Explain, Sketch
- **CN:** 计算，推导，证明，确定，解释，画出草图

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in several ways:
1.  **Cathode Ray Oscilloscope (CRO):** Understanding how electric fields deflect an electron beam is fundamental to using a CRO. Students should be able to explain how changing the voltage on the Y-plates affects the vertical deflection of the spot on the screen.
2.  **Millikan's Oil Drop Experiment:** This classic experiment uses a uniform electric field to balance the gravitational force on charged oil droplets, allowing the measurement of the elementary charge $e$. This connects $F = qE$ with $F = mg$.
3.  **Measurement of $e/m$ for an Electron:** An experiment can be designed where electrons are accelerated through a known $V$ and then deflected by a known $E$ (or $B$) field to measure the charge-to-mass ratio $e/m$.
4.  **Uncertainties:** When calculating the speed of a particle, uncertainties in $V$ and $d$ (for field strength) must be propagated.

**中文:**
本子知识点通过以下几种方式与实验工作相联系：
1.  **阴极射线示波器（CRO）：** 理解电场如何偏转电子束是使用 CRO 的基础。学生应该能够解释改变 Y 板上的电压如何影响屏幕上光点的垂直偏转。
2.  **密立根油滴实验：** 这个经典实验使用匀强电场来平衡带电油滴上的重力，从而能够测量基本电荷 $e$。这连接了 $F = qE$ 和 $F = mg$。
3.  **测量电子的 $e/m$：** 可以设计一个实验，其中电子通过已知的 $V$ 加速，然后被已知的 $E$（或 $B$）场偏转，以测量荷质比 $e/m$。
4.  **不确定度：** 在计算粒子速度时，必须传播 $V$ 和 $d$（对于场强）的不确定度。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    subgraph "Motion of Charged Particles in Electric Fields"
        direction TB
        A[Charged Particle in E-Field] --> B{Force F = qE}
        B --> C[Acceleration a = qE/m]
        C --> D[Kinematics Analysis]
        C --> E[Energy Conservation]
        E --> F[ΔEk = qV]
        F --> G[Speed v = sqrt(2qV/m)]
        D --> H[Projectile Motion in Uniform Field]
        H --> I[Parabolic Trajectory]
        I --> J[Deflection y]
        J --> K[Applications]
        K --> L[Cathode Ray Tube CRT]
        K --> M[Mass Spectrometer]
        K --> N[Particle Accelerator]
    end

    %% Connections to other topics
    A -.-> O[[Electric Fields and Coulomb's Law]]
    B -.-> P[[Electric Potential (V)]]
    F -.-> Q[[Electric Potential Energy]]
    H -.-> R[[Kinematics]]
    L -.-> S[[Capacitance and Capacitors]]
    M -.-> T[[Magnetic Fields]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | A charged particle in an electric field experiences a force $F = qE$, leading to acceleration $a = qE/m$. |
| **Key Formula / 核心公式** | $F = qE$, $a = \frac{qE}{m}$, $\Delta E_k = qV$, $v = \sqrt{\frac{2qV}{m}}$ |
| **Key Graph / 核心图表** | $v$ vs $t$: straight line (constant acceleration). $E_k$ vs $V$: straight line (gradient = $q$). |
| **Key Experiment / 核心实验** | Parallel plate deflection (CRT). Millikan's oil drop experiment. |
| **Common Mistake / 常见错误** | Forgetting the sign of $q$ for force direction. Using $\frac{1}{2}mv^2 = qV$ when the particle doesn't start from rest. |
| **Exam Tip / 考试提示** | For deflection problems, treat $x$ and $y$ motion separately. Time of flight is usually from $x$-motion. Use energy conservation to find speed. |