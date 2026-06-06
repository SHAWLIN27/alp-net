# 1. Overview / 概述

**English:** Simple Harmonic Motion (SHM) is a fundamental type of oscillatory motion where the restoring force is directly proportional to the displacement from equilibrium and acts in the opposite direction. This topic is central to understanding waves, vibrations, and many natural phenomena from pendulums to molecular vibrations. In both CAIE 9702 and Edexcel IAL, SHM forms the mathematical foundation for wave theory and is heavily tested in both multiple-choice and structured questions. Real-world applications include clock mechanisms, suspension systems, seismometers, and alternating current circuits.

**中文:** 简谐运动（SHM）是一种基本的振荡运动类型，其中恢复力与偏离平衡位置的位移成正比，且方向相反。本主题是理解波、振动以及从摆锤到分子振动等许多自然现象的核心。在CAIE 9702和Edexcel IAL中，SHM构成了波动理论的数学基础，在选择题和结构化问题中都有大量考察。实际应用包括钟表机构、悬挂系统、地震仪和交流电路。

> 📷 **IMAGE PROMPT — [SHM-OVERVIEW-01]: Real-World SHM Examples** (Collage showing: pendulum clock, mass on spring, swinging child on swing, vibrating guitar string. Labels in English and Chinese. Style: clean educational diagram with real-world photos and simplified physics overlays. Exam importance: HIGH - helps students connect theory to applications)

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (17.1) | Edexcel IAL (WPH14 U4: 7.1-7.5) |
|-------------------|----------------------------------|
| 17.1(a) Describe SHM as motion where acceleration ∝ -displacement | 7.1 Define SHM and derive a = -ω²x |
| 17.1(b) Define and use displacement, amplitude, period, frequency, angular frequency | 7.2 Use x = A cos(ωt) and x = A sin(ωt) |
| 17.1(c) Use a = -ω²x and x = A cos(ωt) | 7.3 Derive v = ±ω√(A² - x²) |
| 17.1(d) Describe energy changes in SHM | 7.4 Energy in SHM (kinetic + potential) |
| - | 7.5 Simple pendulum and mass-spring system |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to derive the defining equation a = -ω²x from the definition of SHM. Graphical analysis of displacement, velocity, and acceleration vs time is essential. Energy conversion graphs are frequently tested.
- **中文:** 学生必须能够从SHM的定义推导出定义方程a = -ω²x。位移、速度和加速度随时间变化的图形分析至关重要。能量转换图经常被考察。

> 📋 **CIE Only:** CAIE focuses more on graphical interpretation and energy changes. The phase difference between displacement and velocity is explicitly tested.
> 
> 📋 **Edexcel Only:** Edexcel requires derivation of velocity equation v = ±ω√(A² - x²) and more detailed analysis of [[The Simple Pendulum]] and [[Mass-Spring System]].

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Simple Harmonic Motion / 简谐运动** | Motion where the acceleration is directly proportional to the displacement from equilibrium and directed towards the equilibrium position | 加速度与偏离平衡位置的位移成正比，且方向指向平衡位置的运动 | Confusing with any periodic motion - SHM requires a ∝ -x specifically |
| **Amplitude (A) / 振幅** | Maximum displacement from equilibrium position | 从平衡位置到最大位移的距离 | Using amplitude as peak-to-peak distance (it's half that) |
| **Period (T) / 周期** | Time taken for one complete oscillation | 完成一次完整振动所需的时间 | Confusing with frequency; forgetting T = 1/f |
| **Frequency (f) / 频率** | Number of complete oscillations per unit time | 单位时间内完成的完整振动次数 | Units: Hz, not s⁻¹ (though equivalent) |
| **Angular Frequency (ω) / 角频率** | Rate of change of phase, ω = 2πf = 2π/T | 相位变化率，ω = 2πf = 2π/T | Confusing with angular velocity in circular motion |
| **Phase / 相位** | A measure of the position within the oscillation cycle | 描述振动循环中位置的量 | Phase difference of π/2 between displacement and velocity |
| **Equilibrium Position / 平衡位置** | Position where net force on oscillating object is zero | 振荡物体所受合力为零的位置 | Thinking velocity is zero here (it's maximum) |
| **Restoring Force / 恢复力** | Force that acts to return the system to equilibrium | 使系统返回平衡位置的力 | Must be proportional to displacement for SHM |

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Defining Equation of SHM / SHM的定义方程

### Explanation / 解释:
**English:** The fundamental condition for [[Simple Harmonic Motion]] is that the acceleration a is directly proportional to the displacement x from equilibrium and acts in the opposite direction. Mathematically: a ∝ -x, or a = -ω²x where ω is the [[Angular Frequency]]. The negative sign indicates the acceleration always points toward the equilibrium position (restoring nature). This equation is the differential equation of SHM and all other relationships derive from it.

**中文:** 简谐运动的基本条件是加速度a与偏离平衡位置的位移x成正比，且方向相反。数学表达式为：a ∝ -x，或a = -ω²x，其中ω是角频率。负号表示加速度总是指向平衡位置（恢复性质）。这个方程是SHM的微分方程，所有其他关系都由此推导。

### Physical Meaning / 物理意义:
**English:** The equation a = -ω²x tells us that the farther an object is from equilibrium, the greater its acceleration back toward equilibrium. This creates the characteristic sinusoidal motion. The constant ω² determines how "stiff" the restoring force is relative to the mass.

**中文:** 方程a = -ω²x告诉我们，物体离平衡位置越远，其返回平衡位置的加速度就越大。这产生了特征性的正弦运动。常数ω²决定了恢复力相对于质量的"刚度"。

### Common Misconceptions / 常见误区:
- Thinking acceleration is constant (it varies with displacement)
- Forgetting the negative sign (direction matters)
- Confusing ω with angular velocity in circular motion (though mathematically related)

### Exam Tips / 考试提示:
**English:** Always write a = -ω²x, not a = ω²x. The negative sign is worth marks. When deriving, start from F = -kx and use F = ma to get a = -(k/m)x, then identify ω² = k/m.

**中文:** 始终写a = -ω²x，而不是a = ω²x。负号是得分点。推导时，从F = -kx开始，使用F = ma得到a = -(k/m)x，然后确定ω² = k/m。

> 📷 **IMAGE PROMPT — [SHM-DEF-01]: Acceleration vs Displacement Graph for SHM** (Graph with x-axis labeled "Displacement x / 位移" and y-axis labeled "Acceleration a / 加速度". Straight line through origin with negative slope. Labels: gradient = -ω². Style: clear physics graph with gridlines. Exam importance: HIGH - directly tests the defining equation)

## 4.2 Displacement, Velocity and Acceleration in SHM / SHM中的位移、速度和加速度

### Explanation / 解释:
**English:** The solutions to the SHM differential equation give sinusoidal functions for displacement, velocity, and acceleration. For an object starting at maximum displacement:
- Displacement: x = A cos(ωt)
- Velocity: v = -Aω sin(ωt) = ±ω√(A² - x²)
- Acceleration: a = -Aω² cos(ωt) = -ω²x

The velocity leads displacement by π/2 (90°), and acceleration is in anti-phase with displacement (π or 180° out of phase).

**中文:** SHM微分方程的解给出了位移、速度和加速度的正弦函数。对于从最大位移开始的物体：
- 位移：x = A cos(ωt)
- 速度：v = -Aω sin(ωt) = ±ω√(A² - x²)
- 加速度：a = -Aω² cos(ωt) = -ω²x

速度领先位移π/2（90°），加速度与位移反相（相差π或180°）。

### Physical Meaning / 物理意义:
**English:** At equilibrium (x=0): velocity is maximum (v_max = Aω), acceleration is zero. At amplitude (x=±A): velocity is zero, acceleration is maximum (a_max = Aω²). The velocity equation v = ±ω√(A² - x²) shows velocity depends on position.

**中文:** 在平衡位置（x=0）：速度最大（v_max = Aω），加速度为零。在振幅处（x=±A）：速度为零，加速度最大（a_max = Aω²）。速度方程v = ±ω√(A² - x²)显示速度取决于位置。

### Common Misconceptions / 常见误区:
- Thinking velocity and displacement are in phase (they're 90° out)
- Confusing maximum velocity with maximum acceleration
- Forgetting the ± sign in the velocity equation

### Exam Tips / 考试提示:
**English:** Memorize the phase relationships: v leads x by π/2, a lags v by π/2 (or a is π out of phase with x). For graphs, always check which quantity is at zero when the other is at maximum.

**中文:** 记住相位关系：v领先x π/2，a落后v π/2（或a与x反相）。对于图形，始终检查当一个量为零时另一个量是否在最大值。

> 📷 **IMAGE PROMPT — [SHM-GRAPH-01]: Displacement, Velocity, Acceleration vs Time** (Three stacked graphs with same time axis. Top: x = A cos(ωt) - cosine wave. Middle: v = -Aω sin(ωt) - negative sine wave. Bottom: a = -Aω² cos(ωt) - negative cosine wave. Key points marked: x=0 where v is max, x=±A where v=0. Style: clean, color-coded (blue for x, red for v, green for a). Exam importance: VERY HIGH - almost every exam has this)

## 4.3 Energy in SHM / SHM中的能量

### Explanation / 解释:
**English:** In [[Energy in SHM]], total mechanical energy is conserved (for ideal SHM). Energy continuously converts between kinetic energy (KE) and potential energy (PE):
- KE = ½mv² = ½mω²(A² - x²)
- PE = ½kx² = ½mω²x² (for a spring)
- Total Energy (E) = ½kA² = ½mω²A²

At equilibrium: KE is maximum, PE is zero. At amplitude: KE is zero, PE is maximum.

**中文:** 在SHM的能量中，总机械能守恒（对于理想SHM）。能量在动能（KE）和势能（PE）之间连续转换：
- KE = ½mv² = ½mω²(A² - x²)
- PE = ½kx² = ½mω²x²（对于弹簧）
- 总能量（E）= ½kA² = ½mω²A²

在平衡位置：KE最大，PE为零。在振幅处：KE为零，PE最大。

### Physical Meaning / 物理意义:
**English:** The total energy depends only on amplitude and the spring constant (or equivalent). Energy graphs show parabolic PE and inverted parabolic KE, with the sum constant. The period of energy oscillation is half the period of displacement oscillation (energy converts twice per cycle).

**中文:** 总能量仅取决于振幅和弹簧常数（或等效值）。能量图显示抛物线形的PE和倒抛物线形的KE，总和恒定。能量振荡的周期是位移振荡周期的一半（每个循环能量转换两次）。

### Common Misconceptions / 常见误区:
- Thinking total energy changes during oscillation (it's constant in ideal SHM)
- Confusing PE with total energy
- Forgetting that KE and PE are both functions of position

### Exam Tips / 考试提示:
**English:** Draw energy vs displacement graphs carefully. Remember KE + PE = constant. The point where KE = PE occurs at x = ±A/√2. For CAIE, energy-time graphs are common; for Edexcel, energy-displacement graphs are preferred.

**中文:** 仔细绘制能量与位移的关系图。记住KE + PE = 常数。KE = PE的点出现在x = ±A/√2处。对于CAIE，能量-时间图很常见；对于Edexcel，能量-位移图更受青睐。

> 📷 **IMAGE PROMPT — [SHM-ENERGY-01]: Energy vs Displacement in SHM** (Graph with x-axis "Displacement x / 位移" from -A to +A, y-axis "Energy / 能量". Parabolic PE curve (green) opening upward, inverted parabolic KE curve (red) opening downward, horizontal line for total energy (blue). Point where KE=PE marked at x = ±A/√2. Style: clean physics graph with legend. Exam importance: HIGH)

## 4.4 The Simple Pendulum / 单摆

### Explanation / 解释:
**English:** A [[The Simple Pendulum]] approximates SHM for small angular displacements (θ < 10°). The restoring force is the component of weight tangential to the arc: F = -mg sinθ ≈ -mgθ for small θ. The period is T = 2π√(L/g), independent of mass and amplitude (for small amplitudes).

**中文:** 单摆在角位移很小（θ < 10°）时近似为SHM。恢复力是重力沿圆弧切向的分量：F = -mg sinθ ≈ -mgθ（小角度时）。周期为T = 2π√(L/g)，与质量和振幅无关（小振幅时）。

### Physical Meaning / 物理意义:
**English:** The period depends only on pendulum length and gravitational field strength. This makes pendulums useful for measuring g (gravitational acceleration) and for timekeeping. The independence from amplitude is called isochronism.

**中文:** 周期仅取决于摆长和重力场强度。这使得摆可用于测量g（重力加速度）和计时。与振幅无关的特性称为等时性。

### Common Misconceptions / 常见误区:
- Thinking period depends on mass (it doesn't for small angles)
- Using the formula for large amplitudes (approximation breaks down)
- Confusing length L with the string length (it's the distance from pivot to center of mass)

### Exam Tips / 考试提示:
**English:** For pendulum experiments, always mention small angle approximation. To find g, plot T² vs L - gradient = 4π²/g. Remember the pendulum is only approximately SHM - the approximation sinθ ≈ θ is key.

**中文:** 对于摆的实验，始终提到小角度近似。要找到g，绘制T²与L的关系图 - 梯度 = 4π²/g。记住摆只是近似SHM - 近似sinθ ≈ θ是关键。

> 📷 **IMAGE PROMPT — [PENDULUM-01]: Simple Pendulum Diagram** (Diagram showing: pivot point, string of length L, bob of mass m, angle θ from vertical, restoring force component mg sinθ, equilibrium position. Labels in English and Chinese. Style: clear technical diagram with force vectors. Exam importance: HIGH - standard exam diagram)

## 4.5 Mass-Spring System / 弹簧-质量系统

### Explanation / 解释:
**English:** A [[Mass-Spring System]] exhibits perfect SHM (no small angle approximation needed). The restoring force is F = -kx (Hooke's Law). The period is T = 2π√(m/k), independent of amplitude. For vertical springs, the equilibrium position shifts due to weight, but the period formula remains the same.

**中文:** 弹簧-质量系统表现出完美的SHM（不需要小角度近似）。恢复力为F = -kx（胡克定律）。周期为T = 2π√(m/k)，与振幅无关。对于竖直弹簧，平衡位置因重力而偏移，但周期公式保持不变。

### Physical Meaning / 物理意义:
**English:** The period depends on mass and spring constant. Stiffer springs (larger k) give shorter periods. Heavier masses give longer periods. This system is the basis for many mechanical oscillators and is used in shock absorbers and vibration isolation.

**中文:** 周期取决于质量和弹簧常数。更硬的弹簧（更大的k）给出更短的周期。更重的质量给出更长的周期。这个系统是许多机械振荡器的基础，用于减震器和隔振。

### Common Misconceptions / 常见误区:
- Thinking vertical and horizontal springs have different period formulas (they don't)
- Forgetting that k is the spring constant (stiffness), not the spring length
- Confusing extension due to weight with amplitude of oscillation

### Exam Tips / 考试提示:
**English:** For mass-spring experiments, plot T² vs m - gradient = 4π²/k. For vertical springs, the equilibrium extension e = mg/k, but this doesn't affect the period. Both horizontal and vertical mass-spring systems have T = 2π√(m/k).

**中文:** 对于弹簧-质量实验，绘制T²与m的关系图 - 梯度 = 4π²/k。对于竖直弹簧，平衡伸长量e = mg/k，但这不影响周期。水平和竖直弹簧-质量系统都有T = 2π√(m/k)。

> 📷 **IMAGE PROMPT — [MASS-SPRING-01]: Mass-Spring System Diagrams** (Two diagrams side by side: (a) Horizontal mass-spring on frictionless surface showing equilibrium and displaced positions, (b) Vertical mass-spring showing equilibrium extension e = mg/k and oscillation about this point. Force vectors shown. Labels in English and Chinese. Style: clear technical diagrams. Exam importance: HIGH)

# 5. Essential Equations / 核心公式

## 5.1 Defining Equation of SHM / SHM定义方程

$$ a = -\omega^2 x $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| a | Acceleration / 加速度 | m s⁻² |
| ω | Angular frequency / 角频率 | rad s⁻¹ |
| x | Displacement from equilibrium / 偏离平衡位置的位移 | m |

**Derivation:** From F = -kx and F = ma: ma = -kx → a = -(k/m)x → identify ω² = k/m

**Conditions:** Must be SHM (restoring force proportional to displacement)

**Limitations:** Only valid for ideal SHM (no damping)

**Rearrangements:** ω = √(-a/x), x = -a/ω²

## 5.2 Displacement Equation / 位移方程

$$ x = A \cos(\omega t) \quad \text{or} \quad x = A \sin(\omega t) $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| x | Displacement / 位移 | m |
| A | Amplitude / 振幅 | m |
| ω | Angular frequency / 角频率 | rad s⁻¹ |
| t | Time / 时间 | s |

**Derivation:** Solution to differential equation d²x/dt² = -ω²x

**Conditions:** x = A cos(ωt) when starting from maximum displacement; x = A sin(ωt) when starting from equilibrium

**Limitations:** Assumes no damping and starts at t=0 at either max displacement or equilibrium

**Rearrangements:** t = (1/ω) arccos(x/A)

## 5.3 Velocity Equation / 速度方程

$$ v = \pm \omega \sqrt{A^2 - x^2} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| v | Velocity / 速度 | m s⁻¹ |
| ω | Angular frequency / 角频率 | rad s⁻¹ |
| A | Amplitude / 振幅 | m |
| x | Displacement / 位移 | m |

**Derivation:** From energy conservation: ½mv² + ½mω²x² = ½mω²A² → v² = ω²(A² - x²)

**Conditions:** Valid for any SHM system

**Limitations:** ± sign indicates direction; maximum velocity v_max = Aω at x = 0

**Rearrangements:** x = ±√(A² - v²/ω²)

## 5.4 Acceleration in Terms of Displacement / 用位移表示的加速度

$$ a = -\omega^2 x $$

(Same as 5.1 - repeated here for completeness with velocity relationship)

## 5.5 Period of a Simple Pendulum / 单摆周期

$$ T = 2\pi \sqrt{\frac{L}{g}} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| T | Period / 周期 | s |
| L | Length of pendulum / 摆长 | m |
| g | Gravitational field strength / 重力场强度 | m s⁻² or N kg⁻¹ |

**Derivation:** For small θ, restoring torque τ = -mgLθ, I = mL², τ = Iα → α = -(g/L)θ → ω² = g/L

**Conditions:** Small angle approximation (θ < 10°), point mass bob, massless string

**Limitations:** Only approximate SHM; period increases for large amplitudes

**Rearrangements:** g = 4π²L/T², L = gT²/4π²

## 5.6 Period of a Mass-Spring System / 弹簧-质量系统周期

$$ T = 2\pi \sqrt{\frac{m}{k}} $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| T | Period / 周期 | s |
| m | Mass / 质量 | kg |
| k | Spring constant / 弹簧常数 | N m⁻¹ |

**Derivation:** F = -kx, F = ma → a = -(k/m)x → ω² = k/m → T = 2π/ω = 2π√(m/k)

**Conditions:** Ideal spring (Hooke's law obeyed), no damping

**Limitations:** Valid for both horizontal and vertical oscillations (vertical equilibrium shifts but period unchanged)

**Rearrangements:** k = 4π²m/T², m = kT²/4π²

## 5.7 Energy Equations / 能量方程

$$ E_K = \frac{1}{2} m \omega^2 (A^2 - x^2) $$

$$ E_P = \frac{1}{2} m \omega^2 x^2 $$

$$ E_{total} = \frac{1}{2} m \omega^2 A^2 = \frac{1}{2} k A^2 $$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| E_K | Kinetic energy / 动能 | J |
| E_P | Potential energy / 势能 | J |
| E_total | Total mechanical energy / 总机械能 | J |
| m | Mass / 质量 | kg |
| ω | Angular frequency / 角频率 | rad s⁻¹ |
| A | Amplitude / 振幅 | m |
| x | Displacement / 位移 | m |
| k | Spring constant / 弹簧常数 | N m⁻¹ |

**Derivation:** KE = ½mv², substitute v = ±ω√(A² - x²); PE = ½kx² = ½mω²x²; Total = KE + PE

**Conditions:** Ideal SHM (no energy loss)

**Limitations:** Energy conservation only in undamped systems

**Rearrangements:** x when KE = PE: x = ±A/√2

# 6. Graphs and Relationships / 图表与关系

## 6.1 Displacement-Time Graph / 位移-时间图

**Axes:** x-axis: Time (t / 时间) [s]; y-axis: Displacement (x / 位移) [m]

**Shape:** Sinusoidal (cosine or sine wave)

**Gradient Meaning (EN+CN):** Gradient = velocity / 梯度 = 速度

**Area Meaning (EN+CN):** No direct physical meaning / 无直接物理意义

**Exam Interpretation:** Read amplitude from peak value, period from one complete cycle, phase from starting point

**Common Questions:** Find period, amplitude, frequency, phase difference between two oscillators

> 📷 **IMAGE PROMPT — [SHM-GRAPH-02]: Displacement-Time Graph** (Cosine wave x = A cos(ωt) with A and T marked. Points marked: x=A at t=0, x=0 at t=T/4, x=-A at t=T/2, x=0 at t=3T/4, x=A at t=T. Style: clean graph with gridlines. Exam importance: VERY HIGH)

## 6.2 Velocity-Time Graph / 速度-时间图

**Axes:** x-axis: Time (t / 时间) [s]; y-axis: Velocity (v / 速度) [m s⁻¹]

**Shape:** Negative sine wave (v = -Aω sin(ωt))

**Gradient Meaning (EN+CN):** Gradient = acceleration / 梯度 = 加速度

**Area Meaning (EN+CN):** Area = displacement / 面积 = 位移

**Exam Interpretation:** Maximum velocity = Aω at t = T/4, 3T/4; zero velocity at t = 0, T/2, T

**Common Questions:** Find maximum velocity, determine phase relationship with displacement

## 6.3 Acceleration-Time Graph / 加速度-时间图

**Axes:** x-axis: Time (t / 时间) [s]; y-axis: Acceleration (a / 加速度) [m s⁻²]

**Shape:** Negative cosine wave (a = -Aω² cos(ωt))

**Gradient Meaning (EN+CN):** No standard meaning / 无标准意义

**Area Meaning (EN+CN):** Area = change in velocity / 面积 = 速度变化量

**Exam Interpretation:** Maximum acceleration = Aω² at t = 0, T; zero acceleration at t = T/4, 3T/4

**Common Questions:** Find maximum acceleration, verify a = -ω²x relationship

## 6.4 Acceleration-Displacement Graph / 加速度-位移图

**Axes:** x-axis: Displacement (x / 位移) [m]; y-axis: Acceleration (a / 加速度) [m s⁻²]

**Shape:** Straight line through origin with negative slope

**Gradient Meaning (EN+CN):** Gradient = -ω² / 梯度 = -ω²

**Area Meaning (EN+CN):** No direct meaning / 无直接意义

**Exam Interpretation:** This graph directly tests the defining equation a = -ω²x. The steeper the line, the larger ω² (shorter period)

**Common Questions:** Determine ω from gradient, verify SHM condition, compare two oscillators

> 📷 **IMAGE PROMPT — [SHM-GRAPH-03]: Acceleration-Displacement Graph** (Straight line through origin with negative slope. x-axis from -A to +A, y-axis from -Aω² to +Aω². Gradient labeled as -ω². Points at (A, -Aω²) and (-A, Aω²) marked. Style: clean graph with gridlines. Exam importance: VERY HIGH - directly tests defining equation)

## 6.5 Energy-Displacement Graph / 能量-位移图

**Axes:** x-axis: Displacement (x / 位移) [m]; y-axis: Energy (E / 能量) [J]

**Shape:** Parabolic PE (E_P = ½mω²x²), inverted parabolic KE (E_K = ½mω²(A² - x²)), horizontal line for total energy

**Gradient Meaning (EN+CN):** Gradient of PE = restoring force / PE的梯度 = 恢复力

**Area Meaning (EN+CN):** No direct meaning / 无直接意义

**Exam Interpretation:** KE = PE at x = ±A/√2; total energy constant; energy conversion visible

**Common Questions:** Find where KE = PE, determine total energy from amplitude, compare systems

## 6.6 Energy-Time Graph / 能量-时间图

**Axes:** x-axis: Time (t / 时间) [s]; y-axis: Energy (E / 能量) [J]

**Shape:** Squared sinusoidal functions: KE = ½mω²A² sin²(ωt), PE = ½mω²A² cos²(ωt)

**Gradient Meaning (EN+CN):** Gradient = power / 梯度 = 功率

**Area Meaning (EN+CN):** No direct meaning / 无直接意义

**Exam Interpretation:** Energy oscillates at twice the frequency of displacement; KE and PE are complementary

**Common Questions:** Find frequency of energy oscillation, determine when KE is maximum

> 📷 **IMAGE PROMPT — [SHM-GRAPH-04]: Energy-Time Graph** (Two curves: KE (red) = ½mω²A² sin²(ωt) and PE (green) = ½mω²A² cos²(ωt), with horizontal total energy line (blue). Note that energy oscillates at 2f (twice the frequency of displacement). Style: clean graph with legend. Exam importance: HIGH)

# 7. Required Diagrams / 必备图表

## 7.1 Simple Pendulum Setup / 单摆装置图

> 📷 **IMAGE PROMPT — [DIAG-PENDULUM-01]: Simple Pendulum Experimental Setup**
> **English:** Technical diagram of a simple pendulum showing: rigid support (clamp stand), string of length L from pivot to center of bob, spherical bob of mass m, angle θ measured from vertical, equilibrium position (dashed line), restoring force component mg sinθ shown as vector, small angle approximation indicated (θ < 10°). Labels in English and Chinese. Style: clean line drawing with vector arrows, suitable for exam reproduction. Exam importance: VERY HIGH - standard diagram for Paper 3/5 and Unit 3/6 practicals.

## 7.2 Mass-Spring System / 弹簧-质量系统图

> 📷 **IMAGE PROMPT — [DIAG-SPRING-01]: Mass-Spring System Configurations**
> **English:** Two diagrams side by side: (a) Horizontal mass-spring on frictionless surface - spring attached to wall at left, mass m at right, equilibrium position marked, displaced position x shown, restoring force F = -kx vector shown; (b) Vertical mass-spring - spring hanging from support, mass m attached, equilibrium extension e = mg/k marked, oscillation about equilibrium shown with amplitude A. Labels in English and Chinese. Style: clear technical diagrams with force vectors. Exam importance: HIGH - frequently tested in both theory and practical papers.

## 7.3 SHM Phase Relationship Diagram / SHM相位关系图

> 📷 **IMAGE PROMPT — [DIAG-PHASE-01]: Phase Relationships in SHM**
> **English:** Three stacked graphs with aligned time axes showing: (top) displacement x = A cos(ωt) - blue cosine wave; (middle) velocity v = -Aω sin(ωt) - red negative sine wave; (bottom) acceleration a = -Aω² cos(ωt) - green negative cosine wave. Vertical dashed lines at t=0, T/4, T/2, 3T/4, T showing phase relationships: v leads x by π/2, a lags v by π/2, a is π out of phase with x. Key values marked at each point. Style: color-coded, clean, with phase difference annotations. Exam importance: VERY HIGH - almost every exam tests phase relationships.

## 7.4 Energy Conversion Diagram / 能量转换图

> 📷 **IMAGE PROMPT — [DIAG-ENERGY-01]: Energy Conversion in SHM**
> **English:** Combined diagram showing: (a) Mass-spring system at four positions: extreme left (x=-A), equilibrium (x=0), extreme right (x=+A), and one intermediate position; (b) Corresponding bar charts showing KE (red) and PE (green) at each position; (c) Energy-displacement graph with parabolic curves. Labels: at x=±A: KE=0, PE=max; at x=0: KE=max, PE=0; at x=±A/√2: KE=PE. Style: integrated multi-part diagram. Exam importance: HIGH - helps visualize energy conversion.

# 8. Worked Examples / 典型例题

## Example 1: Finding Period and Maximum Velocity / 求周期和最大速度

### Question / 题目:
**English:** A mass of 0.50 kg is attached to a spring of spring constant 80 N m⁻¹ and set into SHM with amplitude 0.12 m. Calculate: (a) the period of oscillation, (b) the maximum velocity, (c) the velocity when the displacement is 0.06 m.

**中文:** 一个0.50 kg的质量块连接到弹簧常数为80 N m⁻¹的弹簧上，以0.12 m的振幅进行SHM。计算：(a) 振荡周期，(b) 最大速度，(c) 位移为0.06 m时的速度。

### Image Prompt / 图片提示:
> 📷 **IMAGE PROMPT — [EX1-DIAG-01]: Mass-Spring System for Example 1** (Simple diagram showing mass m=0.50 kg on spring with k=80 N m⁻¹, amplitude A=0.12 m marked, equilibrium position shown. Labels in English and Chinese. Style: clean technical diagram.)

### Solution / 解答:

**(a) Period / 周期:**
$$ T = 2\pi \sqrt{\frac{m}{k}} = 2\pi \sqrt{\frac{0.50}{80}} $$

$$ T = 2\pi \sqrt{0.00625} = 2\pi \times 0.0791 $$

$$ T = 0.497 \text{ s} \approx 0.50 \text{ s} $$

**(b) Maximum Velocity / 最大速度:**
First find angular frequency:
$$ \omega = \frac{2\pi}{T} = \frac{2\pi}{0.497} = 12.65 \text{ rad s}^{-1} $$

Maximum velocity:
$$ v_{max} = A\omega = 0.12 \times 12.65 = 1.52 \text{ m s}^{-1} $$

**(c) Velocity at x = 0.06 m / 位移0.06 m时的速度:**
$$ v = \pm \omega \sqrt{A^2 - x^2} = \pm 12.65 \sqrt{0.12^2 - 0.06^2} $$

$$ v = \pm 12.65 \sqrt{0.0144 - 0.0036} = \pm 12.65 \sqrt{0.0108} $$

$$ v = \pm 12.65 \times 0.104 = \pm 1.31 \text{ m s}^{-1} $$

### Final Answer / 最终答案:
(a) T = 0.50 s
(b) v_max = 1.52 m s⁻¹
(c) v = ±1.31 m s⁻¹

### Examiner Notes / 考官点评:
**English:** Common mistakes: (1) Using T = 2π√(k/m) instead of T = 2π√(m/k) - check the formula carefully. (2) Forgetting to find ω first before calculating v_max. (3) Omitting the ± sign in part (c) - velocity can be in either direction. Always show working with units.

**中文:** 常见错误：(1) 使用T = 2π√(k/m)而不是T = 2π√(m/k) - 仔细检查公式。(2) 在计算v_max之前忘记先求ω。(3) 在(c)部分省略±号 - 速度可以是两个方向。始终显示带单位的计算过程。

## Example 2: Simple Pendulum - Finding g / 单摆 - 求重力加速度

### Question / 题目:
**English:** In an experiment to determine g using a simple pendulum, a student measures the period T for different lengths L. The following data is obtained:

| L (m) | 0.20 | 0.40 | 0.60 | 0.80 | 1.00 |
|-------|------|------|------|------|------|
| T (s) | 0.90 | 1.27 | 1.55 | 1.79 | 2.01 |

(a) Complete the table by calculating T² for each length.
(b) Plot a graph of T² against L and determine the gradient.
(c) Use the gradient to find the value of g.

**中文:** 在用单摆测定g的实验中，学生测量了不同长度L对应的周期T。得到以下数据：

| L (m) | 0.20 | 0.40 | 0.60 | 0.80 | 1.00 |
|-------|------|------|------|------|------|
| T (s) | 0.90 | 1.27 | 1.55 | 1.79 | 2.01 |

(a) 通过计算每个长度的T²来完善表格。
(b) 绘制T²对L的图并确定梯度。
(c) 使用梯度求g的值。

### Image Prompt / 图片提示:
> 📷 **IMAGE PROMPT — [EX2-GRAPH-01]: T² vs L Graph for Simple Pendulum** (Graph with L on x-axis (0 to 1.0 m) and T² on y-axis (0 to 4.5 s²). Five data points plotted with error bars. Line of best fit through origin. Gradient calculation shown: ΔT²/ΔL = (4.0 - 0)/(1.0 - 0) = 4.0 s²/m. Style: graph paper style with gridlines. Exam importance: HIGH - standard practical analysis)

### Solution / 解答:

**(a) Complete Table / 完善表格:**

| L (m) | 0.20 | 0.40 | 0.60 | 0.80 | 1.00 |
|-------|------|------|------|------|------|
| T (s) | 0.90 | 1.27 | 1.55 | 1.79 | 2.01 |
| T² (s²) | 0.81 | 1.61 | 2.40 | 3.20 | 4.04 |

**(b) Graph and Gradient / 图和梯度:**

From T = 2π√(L/g):
$$ T^2 = \frac{4\pi^2}{g} L $$

This is of the form y = mx, where y = T², x = L, and gradient m = 4π²/g.

From the graph, gradient = (4.04 - 0.81) / (1.00 - 0.20) = 3.23 / 0.80 = 4.04 s²/m

**(c) Finding g / 求g:**

$$ \text{Gradient} = \frac{4\pi^2}{g} $$

$$ g = \frac{4\pi^2}{\text{gradient}} = \frac{4\pi^2}{4.04} $$

$$ g = \frac{39.48}{4.04} = 9.77 \text{ m s}^{-2} $$

### Final Answer / 最终答案:
(a) T² values: 0.81, 1.61, 2.40, 3.20, 4.04 s²
(b) Gradient = 4.04 s²/m
(c) g = 9.77 m s⁻²

### Examiner Notes / 考官点评:
**English:** This is a classic practical question. Key points: (1) The graph must pass through the origin (T=0 when L=0). (2) Use a large triangle for gradient calculation. (3) The formula T² = (4π²/g)L is derived from T = 2π√(L/g). (4) Compare your result with the accepted value of 9.81 m s⁻² - small discrepancies are acceptable due to experimental errors.

**中文:** 这是一个经典的实验题。关键点：(1) 图必须通过原点（L=0时T=0）。(2) 使用大三角形计算梯度。(3) 公式T² = (4π²/g)L由T = 2π√(L/g)推导。(4) 将结果与公认值9.81 m s⁻²比较 - 由于实验误差，小的偏差是可以接受的。

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|-------------------|----------------------------------|
| Define SHM and write defining equation / 定义SHM并写出定义方程 | Very High / 非常高 | Easy / 简单 | 📝 *待填入* |
| Calculate period/frequency from given data / 从给定数据计算周期/频率 | Very High / 非常高 | Medium / 中等 | 📝 *待填入* |
| Phase relationship questions (graphs) / 相位关系问题（图形） | High / 高 | Medium / 中等 | 📝 *待填入* |
| Energy conversion calculations / 能量转换计算 | High / 高 | Medium-Hard / 中难 | 📝 *待填入* |
| Pendulum experiment - find g / 摆实验 - 求g | High / 高 | Medium / 中等 | 📝 *待填入* |
| Mass-spring system analysis / 弹簧-质量系统分析 | High / 高 | Medium / 中等 | 📝 *待填入* |
| Velocity at given displacement / 给定位移处的速度 | Medium / 中等 | Medium / 中等 | 📝 *待填入* |
| Derivation of equations / 方程推导 | Medium / 中等 | Hard / 困难 | 📝 *待填入* |
| Damping effects (qualitative) / 阻尼效应（定性） | Medium / 中等 | Medium / 中等 | 📝 *待填入* |
| Comparison of two oscillators / 两个振荡器的比较 | Low / 低 | Hard / 困难 | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体真题编号和年份正在整理中。建议学生练习所有CAIE 9702 Paper 4和Edexcel IAL Unit 4中关于SHM的题目。常见题型包括：定义题、计算题、图形分析题和实验设计题。

**Common Command Words / 常见指令词:**
- **Define / 定义:** State the precise meaning (e.g., "Define simple harmonic motion")
- **Derive / 推导:** Show the mathematical steps from a starting equation
- **Calculate / 计算:** Use given values in a formula to find a numerical answer
- **Sketch / 草图:** Draw a graph showing the general shape (axes labeled)
- **Explain / 解释:** Give reasons or causes for a phenomenon
- **Determine / 确定:** Find a value using data or a graph

# 10. Practical Skills Connections / 实验技能链接

**English:** SHM practical work is essential in both CAIE and Edexcel specifications.

**CAIE 9702:**
- **Paper 3 (AS Practical):** Simple pendulum experiment to determine g. Skills: measuring period using stopwatch (timing multiple oscillations), measuring length, plotting T² vs L, calculating gradient and g.
- **Paper 5 (A2 Planning):** May require designing an experiment to investigate SHM, e.g., mass-spring system or pendulum with variable parameters.

**Edexcel IAL:**
- **Unit 3 (Practical Skills):** Pendulum experiment for g determination. Skills: uncertainty analysis, error propagation, graph plotting.
- **Unit 6 (Experimental Physics):** More complex investigations, e.g., damped oscillations, forced oscillations, resonance.

**Key Practical Skills / 关键实验技能:**
1. **Timing / 计时:** Measure period by timing 10-20 oscillations and dividing (reduces percentage error)
2. **Small Angle / 小角度:** Ensure θ < 10° for pendulum (maintain SHM approximation)
3. **Amplitude / 振幅:** Keep amplitude small and constant
4. **Graph Plotting / 绘图:** Plot T² vs L (pendulum) or T² vs m (mass-spring) to get straight line
5. **Uncertainties / 不确定度:** Calculate percentage uncertainties in measurements

**Common Errors in Practical / 实验常见错误:**
- Timing from the wrong point in the oscillation
- Not using a fiducial marker (reference point)
- Parallax error when reading length
- Not accounting for the radius of the bob in pendulum length

> 📋 **CIE Only:** Paper 3 specifically tests the pendulum experiment. Students must know how to reduce errors (e.g., using a fiducial marker, timing multiple oscillations).
> 
> 📋 **Edexcel Only:** Unit 6 may require investigation of damping effects or forced oscillations. Students should understand how to vary damping (e.g., changing viscosity of fluid) and measure amplitude decay.

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Simple Harmonic Motion / 简谐运动] --> B[Conditions for SHM / SHM条件]
    A --> C[Displacement, Velocity and Acceleration / 位移、速度和加速度]
    A --> D[Energy in SHM / SHM中的能量]
    A --> E[The Simple Pendulum / 单摆]
    A --> F[Mass-Spring System / 弹簧-质量系统]
    
    B --> B1[Restoring Force ∝ -Displacement / 恢复力∝ -位移]
    B --> B2[a = -ω²x / 定义方程]
    
    C --> C1[x = A cos(ωt) / 位移方程]
    C --> C2[v = ±ω√(A² - x²) / 速度方程]
    C --> C3[a = -ω²x / 加速度方程]
    C --> C4[Phase Relationships / 相位关系]
    
    D --> D1[KE = ½mω²(A² - x²) / 动能]
    D --> D2[PE = ½mω²x² / 势能]
    D --> D3[Total Energy = ½mω²A² / 总能量]
    D --> D4[Energy Conservation / 能量守恒]
    
    E --> E1[T = 2π√(L/g) / 周期公式]
    E --> E2[Small Angle Approximation / 小角度近似]
    E --> E3[Determining g / 测定g]
    
    F --> F1[T = 2π√(m/k) / 周期公式]
    F --> F2[Horizontal vs Vertical / 水平与竖直]
    F --> F3[Hooke's Law / 胡克定律]
    
    G[Prerequisites / 前置知识] --> A
    G --> G1[Equations of Motion (SUVAT) / 运动学方程]
    G --> G2[Angular Measures / 角度测量]
    G --> G3[Forces and Hooke's Law / 力和胡克定律]
    
    A --> H[Related Topics / 相关主题]
    H --> H1[Waves / 波]
    H --> H2[Resonance / 共振]
    H --> H3[Damping / 阻尼]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333
    style C fill:#bbf,stroke:#333
    style D fill:#bbf,stroke:#333
    style E fill:#bbf,stroke:#333
    style F fill:#bbf,stroke:#333
    style G fill:#bfb,stroke:#333
    style H fill:#fbb,stroke:#333
```

# 12. Examiner Insights / 考官洞察

**English:**

**Most Tested Ideas (CAIE 9702):**
1. **Defining equation a = -ω²x** - Almost every Paper 4 has a question asking students to state or use this. The negative sign is crucial.
2. **Phase relationships** - Questions on which quantity leads/lags and by how much. Common: "State the phase difference between displacement and acceleration."
3. **Energy graphs** - Sketching energy vs displacement or energy vs time. Students often confuse KE and PE curves.
4. **Pendulum experiment** - Determining g from T² vs L graph. Calculating percentage uncertainty.
5. **Mass-spring period** - Using T = 2π√(m/k) and understanding what affects period.

**Most Tested Ideas (Edexcel IAL):**
1. **Derivation of v = ±ω√(A² - x²)** - From energy conservation or differentiation.
2. **Simple pendulum analysis** - Including the small angle approximation and its limitations.
3. **Mass-spring system** - Both horizontal and vertical configurations.
4. **Energy calculations** - Finding KE and PE at specific displacements.
5. **Graph interpretation** - Reading values from displacement-time and velocity-time graphs.

**Mark Scheme Wording / 评分方案措辞:**
- "Acceleration is directly proportional to displacement" (must include "directly")
- "Acceleration is directed towards the equilibrium position" (direction matters)
- "ω is the angular frequency" (not just "frequency")
- For energy: "Total energy = ½kA²" or "Total energy = ½mω²A²"

**Common Lost Marks / 常见失分点:**
1. Omitting the negative sign in a = -ω²x
2. Using T = 2π√(k/m) instead of T = 2π√(m/k)
3. Confusing amplitude with peak-to-peak distance
4. Not stating the small angle approximation for pendulums
5. Forgetting units in final answers
6. Not showing working for derivation questions

**High-Scoring Structures / 高分答题结构:**
- **Definition questions:** State the relationship (a ∝ -x) and the equation (a = -ω²x)
- **Calculation questions:** Write the formula, substitute values with units, show intermediate steps, box final answer
- **Graph questions:** Label axes with units, plot points accurately, draw line/best fit, calculate gradient using large triangle
- **Explanation questions:** Use physics terminology, reference equations, give reasons

**中文:**

**最常考内容（CAIE 9702）：**
1. **定义方程 a = -ω²x** - 几乎每份Paper 4都有要求学生陈述或使用此方程的问题。负号至关重要。
2. **相位关系** - 关于哪个量超前/滞后以及超前/滞后多少的问题。常见："陈述位移和加速度之间的相位差。"
3. **能量图** - 绘制能量与位移或能量与时间的关系图。学生经常混淆KE和PE曲线。
4. **摆实验** - 从T²与L的关系图确定g。计算百分比不确定度。
5. **弹簧-质量周期** - 使用T = 2π√(m/k)并理解什么影响周期。

**最常考内容（Edexcel IAL）：**
1. **推导v = ±ω√(A² - x²)** - 从能量守恒或微分推导。
2. **单摆分析** - 包括小角度近似及其局限性。
3. **弹簧-质量系统** - 水平和竖直配置。
4. **能量计算** - 在特定位移处求KE和PE。
5. **图形解读** - 从位移-时间和速度-时间图中读取数值。

# 13. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|-----------------|-------------------|
| **Definition / 定义** | a ∝ -x, a = -ω²x. Acceleration proportional to displacement, opposite direction / 加速度与位移成正比，方向相反 |
| **Key Equations / 关键方程** | x = A cos(ωt), v = ±ω√(A² - x²), a = -ω²x, v_max = Aω, a_max = Aω² |
| **Period Formulas / 周期公式** | Pendulum: T = 2π√(L/g); Mass-Spring: T = 2π√(m/k); ω = 2π/T = 2πf |
| **Phase / 相位** | v leads x by π/2; a lags v by π/2; a is π out of phase with x / v领先x π/2；a落后v π/2；a与x反相 |
| **Energy / 能量** | KE = ½mω²(A² - x²), PE = ½mω²x², Total = ½mω²A² = ½kA². KE=PE at x = ±A/√2 |
| **Pendulum / 单摆** | Small angle θ < 10°; T independent of mass and amplitude (for small θ); g = 4π²L/T² |
| **Mass-Spring / 弹簧-质量** | T independent of amplitude; same formula for horizontal and vertical; k = spring constant |
| **Graphs / 图形** | a-x: straight line through origin (gradient = -ω²); x-t: cosine/sine; v-t: negative sine; a-t: negative cosine |
| **Common Errors / 常见错误** | Forgetting negative sign; wrong period formula; no ± in velocity; no small angle condition |
| **Practical Tips / 实验提示** | Time 10-20 oscillations; use fiducial marker; small amplitude; plot T² vs L for pendulum |

# 14. Metadata / 元数据

```yaml
title:
  en: "Simple Harmonic Motion"
  cn: "简谐运动"
subject: Physics
syllabus: [CAIE 9702, Edexcel IAL]
cie_ref: "17.1 (a-d)"
edexcel_ref: "WPH14 U4: 7.1-7.5"
level: A2
node_type: topic_hub
difficulty: intermediate
prerequisites:
  - "[[Equations of Motion (SUVAT)]]"
  - "[[Angular Measures]]"
related_topics:
  - "[[Energy in SHM]]"
  - "[[Waves]]"
  - "[[Resonance]]"
  - "[[Damping]]"
sub_topics:
  - "[[Conditions for SHM]]"
  - "[[Displacement, Velocity and Acceleration in SHM]]"
  - "[[The Simple Pendulum]]"
  - "[[Mass-Spring System]]"
formula_count: 7
diagram_count: 8
exam_frequency: very_high
language: bilingual_en_cn
last_updated: 2024-01
```

> 📝 **Note / 备注:** This is the HUB file for Simple Harmonic Motion. Each sub-topic has its own leaf node file with detailed derivations, more worked examples, and specific exam questions. Navigate to sub-topics using [[wikilinks]] for deeper study.