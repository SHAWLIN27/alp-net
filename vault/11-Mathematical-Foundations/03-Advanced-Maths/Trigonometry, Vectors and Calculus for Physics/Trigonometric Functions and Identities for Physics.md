---
# Trigonometric Functions and Identities for Physics
# 物理中的三角函数与恒等式

---

# 1. Overview / 概述

**English:**
Trigonometric functions (sine, cosine, tangent) are fundamental tools in physics for describing oscillations, waves, circular motion, and resolving vectors. This sub-topic covers the definitions, key identities, and graphical properties of these functions, with a focus on their application in A-Level Physics contexts. You will learn how to use radians, understand the relationships between sine and cosine, and apply identities like $\sin^2\theta + \cos^2\theta = 1$ to simplify physical problems. This knowledge is essential for topics such as [[Simple Harmonic Motion]], [[Wave Behaviour]], and [[Scalars and Vectors]].

**中文:**
三角函数（正弦、余弦、正切）是物理学中描述振动、波动、圆周运动和矢量分解的基本工具。本子知识点涵盖这些函数的定义、关键恒等式和图形性质，重点在于它们在A-Level物理情境中的应用。你将学习如何使用弧度制，理解正弦和余弦之间的关系，并应用如 $\sin^2\theta + \cos^2\theta = 1$ 这样的恒等式来简化物理问题。这些知识对于[[简谐运动]]、[[波动行为]]和[[标量与矢量]]等主题至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| Understand the relationship between degrees and radians, and convert between them. | Understand the definition of sine, cosine, and tangent for angles of any size. |
| Know and use the identities $\sin^2\theta + \cos^2\theta = 1$ and $\tan\theta = \frac{\sin\theta}{\cos\theta}$. | Use trigonometric functions to model periodic phenomena (e.g., SHM). |
| Use trigonometric functions to resolve vectors into components. | Understand the graphs of $\sin\theta$, $\cos\theta$, and $\tan\theta$, including amplitude and period. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to apply trigonometric functions in physical contexts, not just recall definitions. For example, resolving forces on an inclined plane or describing the displacement of an oscillator. Radians are the default unit in calculus-based physics.
- **中文:** 你必须在物理情境中应用三角函数，而不仅仅是回忆定义。例如，在斜面上分解力或描述振荡器的位移。在基于微积分的物理中，弧度是默认单位。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Radian** / 弧度 | The angle subtended at the centre of a circle by an arc equal in length to the radius. | 在圆中，长度等于半径的弧所对的圆心角。 | Confusing radians with degrees; forgetting that $2\pi \text{ rad} = 360^\circ$. |
| **Sine ($\sin\theta$)** / 正弦 | For a right-angled triangle, $\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}$. For any angle, it is the y-coordinate of a point on the unit circle. | 在直角三角形中，$\sin\theta = \frac{\text{对边}}{\text{斜边}}$。对于任意角，它是单位圆上点的y坐标。 | Thinking $\sin\theta$ is only for acute angles; forgetting it can be negative. |
| **Cosine ($\cos\theta$)** / 余弦 | For a right-angled triangle, $\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}$. For any angle, it is the x-coordinate of a point on the unit circle. | 在直角三角形中，$\cos\theta = \frac{\text{邻边}}{\text{斜边}}$。对于任意角，它是单位圆上点的x坐标。 | Confusing adjacent and opposite sides. |
| **Tangent ($\tan\theta$)** / 正切 | $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\text{opposite}}{\text{adjacent}}$. | $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\text{对边}}{\text{邻边}}$。 | Forgetting $\tan\theta$ is undefined when $\cos\theta = 0$ (e.g., $\theta = 90^\circ$). |
| **Period** / 周期 | The time (or angle) taken for one complete cycle of a trigonometric function. For $\sin\theta$ and $\cos\theta$, the period is $2\pi$ radians. | 三角函数完成一个完整周期所需的时间（或角度）。对于 $\sin\theta$ 和 $\cos\theta$，周期为 $2\pi$ 弧度。 | Confusing period with frequency. |
| **Amplitude** / 振幅 | The maximum displacement from the equilibrium position. For $\sin\theta$ and $\cos\theta$, the amplitude is 1. | 从平衡位置的最大位移。对于 $\sin\theta$ 和 $\cos\theta$，振幅为1。 | Thinking amplitude is always positive; it is a magnitude. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Radians vs Degrees / 弧度与角度

### Explanation / 解释
**English:** Radians are the standard unit of angular measure in physics, especially when dealing with calculus (e.g., differentiating $\sin\theta$). One radian is defined as the angle where the arc length equals the radius. The conversion is: $360^\circ = 2\pi \text{ rad}$. Therefore, $1 \text{ rad} \approx 57.3^\circ$. In A-Level physics, you must be comfortable working in radians for topics like [[Simple Harmonic Motion]] and [[Angular Motion]].

**中文:** 弧度是物理学中角度的标准单位，特别是在处理微积分时（例如，对 $\sin\theta$ 求导）。一弧度定义为弧长等于半径时的角度。换算关系为：$360^\circ = 2\pi \text{ rad}$。因此，$1 \text{ rad} \approx 57.3^\circ$。在A-Level物理中，你必须习惯在[[简谐运动]]和[[角运动]]等主题中使用弧度。

### Physical Meaning / 物理意义
**English:** Radians provide a natural link between linear and angular quantities. For example, arc length $s = r\theta$ (where $\theta$ is in radians) and angular velocity $\omega = \frac{\Delta\theta}{\Delta t}$.

**中文:** 弧度在线性和角度量之间提供了自然的联系。例如，弧长 $s = r\theta$（其中 $\theta$ 以弧度为单位）和角速度 $\omega = \frac{\Delta\theta}{\Delta t}$。

### Common Misconceptions / 常见误区
- **English:** Using degrees in calculus formulas (e.g., differentiating $\sin\theta$ gives $\cos\theta$ only if $\theta$ is in radians).
- **中文:** 在微积分公式中使用角度制（例如，只有当 $\theta$ 以弧度为单位时，$\sin\theta$ 的导数才是 $\cos\theta$）。
- **English:** Forgetting to set calculator to radian mode when solving physics problems.
- **中文:** 在解决物理问题时忘记将计算器设置为弧度模式。

### Exam Tips / 考试提示
- **English:** Always check the question for units. If the answer involves $\pi$, it's likely in radians. If you see $\omega t$ in an equation, $\omega$ is in rad/s, so $t$ must be in seconds.
- **中文:** 始终检查题目中的单位。如果答案涉及 $\pi$，很可能使用弧度。如果在方程中看到 $\omega t$，$\omega$ 的单位是 rad/s，因此 $t$ 必须是以秒为单位。

> 📷 **IMAGE PROMPT — TRIG-01: Radian Definition Diagram**
> A clear diagram showing a circle with radius r, an arc of length r, and the angle θ = 1 radian labelled. Include labels for radius, arc length, and angle. Use a clean, educational style suitable for a physics textbook.

## 4.2 Sine and Cosine Functions / 正弦和余弦函数

### Explanation / 解释
**English:** The sine and cosine functions describe periodic oscillations. In physics, they are used to model displacement in [[Simple Harmonic Motion]]: $x(t) = A \sin(\omega t + \phi)$ or $x(t) = A \cos(\omega t + \phi)$. The key difference is the phase: $\sin(\theta) = \cos(\theta - \frac{\pi}{2})$. This means a sine wave is a cosine wave shifted by $\frac{\pi}{2}$ radians (90°) to the right.

**中文:** 正弦和余弦函数描述周期性振荡。在物理学中，它们用于模拟[[简谐运动]]中的位移：$x(t) = A \sin(\omega t + \phi)$ 或 $x(t) = A \cos(\omega t + \phi)$。关键区别在于相位：$\sin(\theta) = \cos(\theta - \frac{\pi}{2})$。这意味着正弦波是余弦波向右平移 $\frac{\pi}{2}$ 弧度（90°）。

### Physical Meaning / 物理意义
**English:** The amplitude $A$ represents the maximum displacement. The angular frequency $\omega$ determines how fast the oscillation occurs. The phase constant $\phi$ determines the initial position at $t=0$.

**中文:** 振幅 $A$ 代表最大位移。角频率 $\omega$ 决定振荡发生的速度。相位常数 $\phi$ 决定 $t=0$ 时的初始位置。

### Common Misconceptions / 常见误区
- **English:** Thinking $\sin$ and $\cos$ are the same function. They are phase-shifted versions of each other.
- **中文:** 认为 $\sin$ 和 $\cos$ 是相同的函数。它们是彼此相位偏移的版本。
- **English:** Forgetting that the argument of $\sin$ or $\cos$ must be in radians when used in calculus or with $\omega t$.
- **中文:** 忘记在微积分或与 $\omega t$ 一起使用时，$\sin$ 或 $\cos$ 的参数必须以弧度为单位。

### Exam Tips / 考试提示
- **English:** When given a graph of an oscillation, identify whether it starts at zero (sine) or at maximum (cosine) to choose the correct function.
- **中文:** 当给出振荡图时，识别它是从零开始（正弦）还是从最大值开始（余弦），以选择正确的函数。

## 4.3 Tangent Function / 正切函数

### Explanation / 解释
**English:** The tangent function is less common in A-Level physics but appears in contexts like gradient of a slope or phase difference calculations. It is defined as $\tan\theta = \frac{\sin\theta}{\cos\theta}$. Its graph has vertical asymptotes where $\cos\theta = 0$ (at $\theta = \frac{\pi}{2}, \frac{3\pi}{2}$, etc.).

**中文:** 正切函数在A-Level物理中不太常见，但出现在坡度梯度或相位差计算等情境中。它定义为 $\tan\theta = \frac{\sin\theta}{\cos\theta}$。其图形在 $\cos\theta = 0$ 处有垂直渐近线（在 $\theta = \frac{\pi}{2}, \frac{3\pi}{2}$ 等处）。

### Physical Meaning / 物理意义
**English:** In vector resolution, $\tan\theta = \frac{\text{opposite}}{\text{adjacent}}$ is used to find the direction of a resultant vector from its components.

**中文:** 在矢量分解中，$\tan\theta = \frac{\text{对边}}{\text{邻边}}$ 用于从分量求合矢量的方向。

### Common Misconceptions / 常见误区
- **English:** Forgetting that $\tan\theta$ is undefined at certain angles.
- **中文:** 忘记 $\tan\theta$ 在某些角度未定义。

### Exam Tips / 考试提示
- **English:** Use $\tan^{-1}$ to find an angle from a ratio, but always check the quadrant to ensure the angle is correct.
- **中文:** 使用 $\tan^{-1}$ 从比值求角度，但始终检查象限以确保角度正确。

---

# 5. Essential Equations / 核心公式

## 5.1 Radian Conversion / 弧度转换

$$ \theta (\text{rad}) = \frac{\pi}{180^\circ} \times \theta (\text{degrees}) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Angle | 角度 | rad or ° |

**Derivation / 推导:** Since $360^\circ = 2\pi \text{ rad}$, dividing both sides by 360 gives $1^\circ = \frac{\pi}{180} \text{ rad}$.

**Conditions / 适用条件:** Always use radians in calculus and when using $\omega t$.

**Limitations / 局限性:** None, but be consistent.

## 5.2 Pythagorean Identity / 毕达哥拉斯恒等式

$$ \sin^2\theta + \cos^2\theta = 1 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Angle | 角度 | rad or ° |

**Derivation / 推导:** From the unit circle, where the x-coordinate is $\cos\theta$ and y-coordinate is $\sin\theta$, and the radius is 1, so by Pythagoras: $x^2 + y^2 = 1$.

**Conditions / 适用条件:** True for all $\theta$.

**Limitations / 局限性:** None.

## 5.3 Tangent Identity / 正切恒等式

$$ \tan\theta = \frac{\sin\theta}{\cos\theta} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Angle | 角度 | rad or ° |

**Derivation / 推导:** From right-angled triangle definitions: $\frac{\text{opposite}}{\text{adjacent}} = \frac{\text{opposite/hypotenuse}}{\text{adjacent/hypotenuse}} = \frac{\sin\theta}{\cos\theta}$.

**Conditions / 适用条件:** $\cos\theta \neq 0$.

**Limitations / 局限性:** Undefined at $\theta = \frac{\pi}{2} + n\pi$.

## 5.4 Phase Relationship / 相位关系

$$ \sin\theta = \cos\left(\theta - \frac{\pi}{2}\right) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta$ | Angle | 角度 | rad |

**Derivation / 推导:** Using the cosine subtraction formula: $\cos(\theta - \frac{\pi}{2}) = \cos\theta \cos\frac{\pi}{2} + \sin\theta \sin\frac{\pi}{2} = 0 + \sin\theta \cdot 1 = \sin\theta$.

**Conditions / 适用条件:** $\theta$ in radians.

**Limitations / 局限性:** None.

> 📷 **IMAGE PROMPT — TRIG-02: Sine and Cosine Phase Shift**
> Two graphs on the same axes: one sine wave and one cosine wave, showing that sine leads cosine by 90° (π/2 rad). Label the axes as θ (radians) and amplitude. Use different colors for sine and cosine.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Sine and Cosine Graphs / 正弦和余弦图

### Axes / 坐标轴
- **x-axis:** Angle $\theta$ (radians) / 角度 $\theta$ (弧度)
- **y-axis:** Value of $\sin\theta$ or $\cos\theta$ / $\sin\theta$ 或 $\cos\theta$ 的值

### Shape / 形状
- **English:** Both are smooth, periodic waves. $\sin\theta$ starts at 0, rises to 1 at $\frac{\pi}{2}$, returns to 0 at $\pi$, goes to -1 at $\frac{3\pi}{2}$, and back to 0 at $2\pi$. $\cos\theta$ starts at 1, goes to 0 at $\frac{\pi}{2}$, -1 at $\pi$, 0 at $\frac{3\pi}{2}$, and back to 1 at $2\pi$.
- **中文:** 两者都是平滑的周期性波。$\sin\theta$ 从0开始，在 $\frac{\pi}{2}$ 处上升到1，在 $\pi$ 处回到0，在 $\frac{3\pi}{2}$ 处下降到-1，在 $2\pi$ 处回到0。$\cos\theta$ 从1开始，在 $\frac{\pi}{2}$ 处到0，在 $\pi$ 处到-1，在 $\frac{3\pi}{2}$ 处到0，在 $2\pi$ 处回到1。

### Gradient Meaning / 斜率含义
- **English:** The gradient of $\sin\theta$ at any point is $\cos\theta$. This is crucial in SHM where velocity is the derivative of displacement.
- **中文:** $\sin\theta$ 在任何点的斜率是 $\cos\theta$。这在简谐运动中至关重要，其中速度是位移的导数。

### Area Meaning / 面积含义
- **English:** The area under the curve of $\sin\theta$ or $\cos\theta$ over a full period is zero, as the positive and negative areas cancel.
- **中文:** $\sin\theta$ 或 $\cos\theta$ 在一个完整周期内的曲线下面积为零，因为正面积和负面积相互抵消。

### Exam Interpretation / 考试解读
- **English:** Be able to read amplitude and period from a graph. Identify phase shifts between two waves.
- **中文:** 能够从图中读取振幅和周期。识别两个波之间的相位差。

## 6.2 Tangent Graph / 正切图

### Axes / 坐标轴
- **x-axis:** Angle $\theta$ (radians) / 角度 $\theta$ (弧度)
- **y-axis:** Value of $\tan\theta$ / $\tan\theta$ 的值

### Shape / 形状
- **English:** Periodic with period $\pi$. Has vertical asymptotes at $\theta = \frac{\pi}{2}, \frac{3\pi}{2}$, etc. The function increases from $-\infty$ to $+\infty$ between asymptotes.
- **中文:** 周期为 $\pi$ 的周期性函数。在 $\theta = \frac{\pi}{2}, \frac{3\pi}{2}$ 等处有垂直渐近线。函数在渐近线之间从 $-\infty$ 增加到 $+\infty$。

### Gradient Meaning / 斜率含义
- **English:** The gradient is $\sec^2\theta$, which is always positive.
- **中文:** 斜率为 $\sec^2\theta$，始终为正。

### Area Meaning / 面积含义
- **English:** Not typically examined at A-Level.
- **中文:** 在A-Level中通常不考查。

### Exam Interpretation / 考试解读
- **English:** Recognize the asymptotes and understand that $\tan\theta$ is undefined at those points.
- **中文:** 识别渐近线并理解 $\tan\theta$ 在这些点未定义。

---

# 7. Required Diagrams / 必备图表

## 7.1 Unit Circle Diagram / 单位圆图

### Description / 描述
**English:** A circle of radius 1 centered at the origin. An angle $\theta$ is drawn from the positive x-axis. The x-coordinate of the point on the circle is $\cos\theta$, and the y-coordinate is $\sin\theta$. This diagram visually explains the definitions of sine and cosine for all angles.

**中文:** 一个以原点为圆心、半径为1的圆。从正x轴画出一个角度 $\theta$。圆上点的x坐标是 $\cos\theta$，y坐标是 $\sin\theta$。该图直观地解释了所有角度的正弦和余弦定义。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — TRIG-03: Unit Circle with Sine and Cosine**
> A unit circle diagram with the angle θ marked from the positive x-axis. Show the point on the circle with coordinates (cosθ, sinθ). Draw a vertical line from the point to the x-axis to represent sinθ, and a horizontal line to the y-axis to represent cosθ. Label all parts clearly. Use a clean, educational style.

### Labels Required / 需要标注
- **English:** Origin (0,0), radius = 1, angle $\theta$, point $(\cos\theta, \sin\theta)$, x-axis, y-axis.
- **中文:** 原点 (0,0)，半径 = 1，角度 $\theta$，点 $(\cos\theta, \sin\theta)$，x轴，y轴。

### Exam Importance / 考试重要性
- **English:** High. Understanding the unit circle helps with understanding phase, amplitude, and the signs of trigonometric functions in different quadrants.
- **中文:** 高。理解单位圆有助于理解相位、振幅以及三角函数在不同象限的符号。

## 7.2 Sine and Cosine Wave Graphs / 正弦和余弦波图

### Description / 描述
**English:** Two graphs showing $\sin\theta$ and $\cos\theta$ over the range $0$ to $2\pi$ radians. The graphs should be on the same axes to show the phase difference.

**中文:** 两个显示 $\sin\theta$ 和 $\cos\theta$ 在 $0$ 到 $2\pi$ 弧度范围内的图。这两个图应在同一坐标轴上以显示相位差。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — TRIG-04: Sine and Cosine Waves**
> Two smooth periodic waves on the same axes. One wave (sine) starts at (0,0), rises to a peak of 1 at π/2, crosses zero at π, reaches a trough of -1 at 3π/2, and returns to zero at 2π. The other wave (cosine) starts at (0,1), crosses zero at π/2, reaches a trough of -1 at π, crosses zero at 3π/2, and returns to 1 at 2π. Label the axes as θ (radians) and amplitude. Use different colors for sine and cosine. Include a legend.

### Labels Required / 需要标注
- **English:** Amplitude = 1, Period = $2\pi$, $\sin\theta$, $\cos\theta$, key points: $0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi$.
- **中文:** 振幅 = 1，周期 = $2\pi$，$\sin\theta$，$\cos\theta$，关键点：$0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi$。

### Exam Importance / 考试重要性
- **English:** Very high. You must be able to sketch these graphs from memory and interpret them in physics contexts.
- **中文:** 非常高。你必须能够凭记忆画出这些图并在物理情境中解释它们。

---

# 8. Worked Examples / 典型例题

## Example 1: Resolving a Force / 例1：分解力

### Question / 题目
**English:** A force of 50 N is applied at an angle of 30° to the horizontal. Calculate the horizontal and vertical components of the force.

**中文:** 一个50 N的力与水平方向成30°角。计算该力的水平和垂直分量。

### Solution / 解答
**Step 1:** Identify the components.
- Horizontal: $F_x = F \cos\theta$
- Vertical: $F_y = F \sin\theta$

**Step 2:** Substitute values. Ensure calculator is in degree mode.
- $F_x = 50 \times \cos(30^\circ) = 50 \times 0.8660 = 43.3 \text{ N}$
- $F_y = 50 \times \sin(30^\circ) = 50 \times 0.5 = 25.0 \text{ N}$

### Final Answer / 最终答案
**Answer:** Horizontal component = 43.3 N, Vertical component = 25.0 N | **答案：** 水平分量 = 43.3 N，垂直分量 = 25.0 N

### Quick Tip / 提示
**English:** Always draw a right-angled triangle to visualize the components. The force is the hypotenuse. | **中文:** 始终画一个直角三角形来可视化分量。力是斜边。

## Example 2: SHM Displacement / 例2：简谐运动位移

### Question / 题目
**English:** An object oscillates with SHM according to $x(t) = 0.05 \sin(10t)$, where $x$ is in meters and $t$ in seconds. Find the displacement at $t = 0.2 \text{ s}$.

**中文:** 一个物体根据 $x(t) = 0.05 \sin(10t)$ 做简谐运动，其中 $x$ 以米为单位，$t$ 以秒为单位。求 $t = 0.2 \text{ s}$ 时的位移。

### Solution / 解答
**Step 1:** Ensure calculator is in radian mode (since $\omega = 10 \text{ rad/s}$).
**Step 2:** Substitute $t = 0.2$:
$$ x(0.2) = 0.05 \times \sin(10 \times 0.2) = 0.05 \times \sin(2) $$
**Step 3:** Calculate $\sin(2 \text{ rad})$:
$$ \sin(2) \approx 0.9093 $$
**Step 4:** Multiply:
$$ x = 0.05 \times 0.9093 = 0.0455 \text{ m} $$

### Final Answer / 最终答案
**Answer:** $x = 0.0455 \text{ m}$ | **答案：** $x = 0.0455 \text{ m}$

### Quick Tip / 提示
**English:** Always check the mode of your calculator (degrees vs radians) before solving. | **中文:** 在解题前始终检查计算器的模式（角度制 vs 弧度制）。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Resolving forces using $\sin$ and $\cos$ | Very High | Easy | 📝 *待填入* |
| SHM displacement/velocity equations | High | Medium | 📝 *待填入* |
| Phase difference between waves | Medium | Medium | 📝 *待填入* |
| Using $\sin^2\theta + \cos^2\theta = 1$ | Low | Medium | 📝 *待填入* |
| Radian conversion | Medium | Easy | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, Show that, Sketch, State
- **中文:** 计算，确定，证明，画出，写出

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Trigonometric functions are used in practical work for:
- **Resolving forces:** In experiments involving inclined planes or equilibrium of forces, you will use $\sin$ and $\cos$ to resolve forces into components.
- **Wave experiments:** In experiments with a ripple tank or oscilloscope, you will analyze wave patterns that are sinusoidal.
- **Uncertainties:** When calculating a component force, the uncertainty in the angle propagates through the trigonometric function. For example, if $F_x = F \cos\theta$, the uncertainty in $F_x$ depends on the uncertainty in $\theta$ and the derivative $\frac{d}{d\theta}(\cos\theta) = -\sin\theta$.
- **Graph plotting:** When plotting displacement vs time for an oscillator, the graph should be sinusoidal. You may need to determine the amplitude and period from the graph.

**中文:**
三角函数在实验工作中用于：
- **分解力：** 在涉及斜面或力平衡的实验中，你将使用 $\sin$ 和 $\cos$ 将力分解为分量。
- **波动实验：** 在纹影槽或示波器实验中，你将分析呈正弦波形的图案。
- **不确定度：** 当计算分力时，角度的不确定度会通过三角函数传播。例如，如果 $F_x = F \cos\theta$，则 $F_x$ 的不确定度取决于 $\theta$ 的不确定度和导数 $\frac{d}{d\theta}(\cos\theta) = -\sin\theta$。
- **绘图：** 当绘制振荡器的位移与时间的关系图时，图形应为正弦波。你可能需要从图中确定振幅和周期。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Trigonometric Functions and Identities] --> B[Radians vs Degrees]
    A --> C[Sine Function]
    A --> D[Cosine Function]
    A --> E[Tangent Function]
    A --> F[Key Identities]
    
    B --> B1[Conversion: π rad = 180°]
    B --> B2[Arc Length: s = rθ]
    
    C --> C1[Definition: opposite/hypotenuse]
    C --> C2[Graph: Periodic, period 2π]
    C --> C3[Application: SHM, Waves]
    
    D --> D1[Definition: adjacent/hypotenuse]
    D --> D2[Graph: Periodic, period 2π]
    D --> D3[Application: Vector Resolution]
    
    E --> E1[Definition: sin/cos]
    E --> E2[Graph: Asymptotes]
    E --> E3[Application: Gradient, Direction]
    
    F --> F1[sin²θ + cos²θ = 1]
    F --> F2[tanθ = sinθ/cosθ]
    F --> F3[sinθ = cos(θ - π/2)]
    
    C2 --> G[Amplitude and Period]
    D2 --> G
    
    G --> H[Physics Applications]
    H --> I[[Simple Harmonic Motion]]
    H --> J[[Wave Behaviour]]
    H --> K[[Scalars and Vectors]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Radian: angle where arc length = radius. $2\pi \text{ rad} = 360^\circ$. |
| **Key Formula / 核心公式** | $\sin^2\theta + \cos^2\theta = 1$; $\tan\theta = \frac{\sin\theta}{\cos\theta}$; $\sin\theta = \cos(\theta - \frac{\pi}{2})$ |
| **Key Graph / 核心图表** | Sine: starts at 0, peaks at $\frac{\pi}{2}$. Cosine: starts at 1, crosses 0 at $\frac{\pi}{2}$. Both have period $2\pi$, amplitude 1. |
| **Exam Tip / 考试提示** | Always check calculator mode (degrees vs radians). In physics, radians are default for calculus and SHM. Use SOH CAH TOA for right-angled triangles. |
| **Common Mistake / 常见错误** | Using degrees in $\omega t$ formulas. Forgetting $\tan\theta$ is undefined at $\frac{\pi}{2}$. Confusing sine and cosine phase. |
| **Application / 应用** | Resolving forces: $F_x = F\cos\theta$, $F_y = F\sin\theta$. SHM: $x(t) = A\sin(\omega t + \phi)$. |