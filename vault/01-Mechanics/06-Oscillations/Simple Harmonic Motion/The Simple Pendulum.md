---
# The Simple Pendulum / 单摆

---

# 1. Overview / 概述

**English:**
The simple pendulum is a classic example of a system that undergoes [[Simple Harmonic Motion]] under specific conditions. This sub-topic focuses on deriving and applying the formula for the time period of a simple pendulum, $T = 2\pi \sqrt{\frac{l}{g}}$. We will explore the assumptions that make a pendulum a simple harmonic oscillator, the factors that affect its period, and how to use it as a tool for measuring gravitational field strength. Understanding the simple pendulum builds directly on the [[Conditions for SHM]] and the [[Displacement, Velocity and Acceleration in SHM]] concepts, and is a key practical application of SHM theory.

**中文:**
单摆是在特定条件下进行[[简谐运动]]的经典系统。本子知识点专注于推导和应用单摆的周期公式 $T = 2\pi \sqrt{\frac{l}{g}}$。我们将探讨使单摆成为简谐振子的假设条件、影响其周期的因素，以及如何将其用作测量重力场强度的工具。理解单摆直接建立在[[简谐运动的条件]]和[[简谐运动中的位移、速度和加速度]]概念之上，是SHM理论的关键实际应用。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (17.1) | Edexcel IAL (WPH14 U4: 7.1-7.5) |
|-----------|-------------|
| (a) Describe simple examples of SHM, including the simple pendulum. | 7.1 Understand the conditions for SHM and how the simple pendulum satisfies them. |
| (b) Define and use the terms displacement, amplitude, period, frequency, angular frequency and phase difference. | 7.2 Derive and use the formula $T = 2\pi \sqrt{\frac{l}{g}}$ for the period of a simple pendulum. |
| (c) Derive and use the formula $T = 2\pi \sqrt{\frac{l}{g}}$ for the period of a simple pendulum. | 7.3 Investigate the factors affecting the period of a simple pendulum. |
| (d) Describe an experiment to determine $g$ using a simple pendulum. | 7.4 Use a simple pendulum to determine the value of $g$. |
| | 7.5 Understand the limitations of the simple pendulum model. |

**Examiner Expectations / 考官期望:**
- **CAIE:** Students must be able to derive the period formula from the restoring force and the condition for SHM. They must also be able to describe the experimental procedure to find $g$ and identify sources of error.
- **Edexcel:** Students must be able to derive and use the formula, and understand the assumptions (small angle, inextensible string, point mass). They should be able to analyze experimental data to find $g$.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Simple Pendulum** / 单摆 | An idealized model consisting of a point mass suspended from a fixed point by a massless, inextensible string, swinging under gravity. | 一个理想化模型，由一个质点通过一根无质量、不可伸长的绳子悬挂在固定点上，在重力作用下摆动。 | Confusing the real pendulum with the ideal model. |
| **Restoring Force** / 回复力 | The net force acting on the pendulum bob that always acts towards the equilibrium position. For a simple pendulum, it is the component of weight tangential to the arc: $F = -mg \sin \theta$. | 作用在单摆摆锤上的净力，始终指向平衡位置。对于单摆，它是重力沿圆弧切向的分量：$F = -mg \sin \theta$. | Forgetting the negative sign or using the full weight $mg$ instead of its component. |
| **Small Angle Approximation** / 小角度近似 | The assumption that for small angular displacements ($\theta < 10^\circ$), $\sin \theta \approx \theta$ (in radians). This linearizes the restoring force, making the motion SHM. | 假设对于小角位移 ($\theta < 10^\circ$)，$\sin \theta \approx \theta$ (以弧度为单位)。这使回复力线性化，从而使运动成为简谐运动。 | Using degrees instead of radians when applying the approximation. |
| **Period (T)** / 周期 | The time taken for one complete oscillation (e.g., from one extreme to the other and back). | 完成一次全振动所需的时间（例如，从一个极端到另一个极端再返回）。 | Confusing period with frequency or half-period. |
| **Length (l)** / 摆长 | The distance from the point of suspension to the center of mass of the bob. | 从悬挂点到摆锤质心的距离。 | Measuring to the bottom of the bob instead of its center. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Derivation of the Period Formula / 周期公式的推导

### Explanation / 解释
**English:**
The derivation of $T = 2\pi \sqrt{\frac{l}{g}}$ is a core skill. It links the [[Conditions for SHM]] to the geometry of the pendulum.

1.  **Restoring Force:** For a pendulum displaced by an angle $\theta$, the restoring force is the component of weight acting towards the equilibrium position: $F = -mg \sin \theta$.
2.  **Small Angle Approximation:** For SHM, the restoring force must be proportional to displacement ($F \propto -x$). The displacement $x$ along the arc is $x = l\theta$. Using the small angle approximation ($\sin \theta \approx \theta$), we get $F \approx -mg \theta = -mg \left(\frac{x}{l}\right) = -\left(\frac{mg}{l}\right)x$.
3.  **Identifying $k$:** Comparing $F = -kx$ with $F = -\left(\frac{mg}{l}\right)x$, we find the effective spring constant for the pendulum is $k = \frac{mg}{l}$.
4.  **Using the SHM Period Formula:** The general formula for the period of any SHM system is $T = 2\pi \sqrt{\frac{m}{k}}$. Substituting $k = \frac{mg}{l}$ gives $T = 2\pi \sqrt{\frac{m}{mg/l}} = 2\pi \sqrt{\frac{l}{g}}$.

**中文:**
推导 $T = 2\pi \sqrt{\frac{l}{g}}$ 是一项核心技能。它将[[简谐运动的条件]]与单摆的几何形状联系起来。

1.  **回复力：** 对于偏离角度 $\theta$ 的单摆，回复力是重力指向平衡位置的分量：$F = -mg \sin \theta$。
2.  **小角度近似：** 对于SHM，回复力必须与位移成正比 ($F \propto -x$)。沿弧的位移 $x$ 为 $x = l\theta$。使用小角度近似 ($\sin \theta \approx \theta$)，我们得到 $F \approx -mg \theta = -mg \left(\frac{x}{l}\right) = -\left(\frac{mg}{l}\right)x$。
3.  **识别 $k$：** 比较 $F = -kx$ 和 $F = -\left(\frac{mg}{l}\right)x$，我们发现单摆的有效劲度系数为 $k = \frac{mg}{l}$。
4.  **使用SHM周期公式：** 任何SHM系统的通用周期公式是 $T = 2\pi \sqrt{\frac{m}{k}}$。代入 $k = \frac{mg}{l}$ 得到 $T = 2\pi \sqrt{\frac{m}{mg/l}} = 2\pi \sqrt{\frac{l}{g}}$。

### Physical Meaning / 物理意义
**English:** The period of a simple pendulum depends only on its length ($l$) and the local gravitational field strength ($g$). It is independent of the mass of the bob and the amplitude (for small angles). A longer pendulum has a longer period; a stronger gravitational field results in a shorter period.
**中文:** 单摆的周期仅取决于其摆长 ($l$) 和当地的重力场强度 ($g$)。它与摆锤的质量和振幅（在小角度下）无关。摆长越长，周期越长；重力场越强，周期越短。

### Common Misconceptions / 常见误区
- **Mass matters:** Students often think a heavier bob will swing slower. The derivation shows mass cancels out.
- **Large amplitude:** The formula is only valid for small amplitudes ($\theta < 10^\circ$). For larger amplitudes, the motion is not simple harmonic, and the period becomes longer.
- **Angle units:** The small angle approximation $\sin \theta \approx \theta$ is only valid when $\theta$ is in **radians**.

### Exam Tips / 考试提示
- **Derivation:** Be prepared to derive the formula step-by-step in a "show that" question.
- **Variables:** Clearly state which variables are independent and dependent when describing experiments.
- **Units:** Ensure $l$ is in meters and $g$ is in $ms^{-2}$.

> 📷 **IMAGE PROMPT — DIAGRAM: Simple Pendulum Force Diagram**
> A clear diagram of a simple pendulum displaced by an angle θ. Show the string of length l, the bob of mass m, the equilibrium position (dashed line), and the displacement x along the arc. Draw the weight mg acting vertically downwards, and resolve it into two components: mg cosθ along the string and mg sinθ tangential to the arc. Label the restoring force as F = -mg sinθ. Indicate the angle θ.

---

# 5. Essential Equations / 核心公式

## Equation 1: Period of a Simple Pendulum / 单摆周期公式

$$ T = 2\pi \sqrt{\frac{l}{g}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T$ | Period of oscillation | 振动周期 | s (秒) |
| $l$ | Length of the pendulum (from pivot to center of mass) | 摆长（从支点到质心） | m (米) |
| $g$ | Acceleration due to gravity | 重力加速度 | $ms^{-2}$ |

**Derivation / 推导:** See Section 4.1.
**Conditions / 适用条件:**
- **EN:** Small angular displacement ($\theta < 10^\circ$), inextensible string, point mass bob, no air resistance.
- **CN:** 小角位移 ($\theta < 10^\circ$)，不可伸长的绳子，质点摆锤，无空气阻力。
**Limitations / 局限性:**
- **EN:** The formula is an approximation. For larger amplitudes, the period is longer and depends on amplitude. Real pendulums have mass distribution and friction.
- **CN:** 该公式是一个近似值。对于较大的振幅，周期更长且取决于振幅。真实的单摆有质量分布和摩擦。

## Equation 2: Restoring Force / 回复力公式

$$ F = -mg \sin \theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $F$ | Restoring force | 回复力 | N (牛顿) |
| $m$ | Mass of bob | 摆锤质量 | kg (千克) |
| $g$ | Acceleration due to gravity | 重力加速度 | $ms^{-2}$ |
| $\theta$ | Angular displacement from equilibrium | 与平衡位置的角位移 | rad (弧度) |

**Conditions / 适用条件:** Always true for a simple pendulum.
**Limitations / 局限性:** This is the exact expression. It is not proportional to $\theta$ unless the small angle approximation is used.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 $T^2$ vs $l$ Graph / $T^2$ 对 $l$ 关系图

### Axes / 坐标轴
- **X-axis:** Length, $l$ (m) / 摆长 $l$ (米)
- **Y-axis:** Square of Period, $T^2$ ($s^2$) / 周期的平方 $T^2$ (秒²)

### Shape / 形状
A straight line passing through the origin.

### Gradient Meaning / 斜率含义
From $T = 2\pi \sqrt{\frac{l}{g}}$, squaring both sides gives $T^2 = \frac{4\pi^2}{g} l$.
Therefore, the gradient of the $T^2$ vs $l$ graph is $m = \frac{4\pi^2}{g}$.

### Area Meaning / 面积含义
No physical meaning.

### Exam Interpretation / 考试解读
This graph is the standard method for determining $g$ experimentally. By plotting $T^2$ against $l$ and calculating the gradient, you can find $g = \frac{4\pi^2}{\text{gradient}}$. A straight line through the origin confirms the relationship $T^2 \propto l$.

> 📷 **IMAGE PROMPT — GRAPH: T² vs l for a Simple Pendulum**
> A graph with 'Length, l / m' on the x-axis and 'T² / s²' on the y-axis. Show a straight line passing through the origin. Label the gradient as 'm = 4π²/g'. Add a data point with error bars to show experimental uncertainty.

---

# 7. Required Diagrams / 必备图表

## 7.1 Experimental Setup for Determining $g$ / 测定重力加速度 $g$ 的实验装置

### Description / 描述
**English:** A diagram showing the experimental setup used to determine the acceleration due to gravity using a simple pendulum. It includes a clamp stand, a string, a bob, a protractor to measure the initial angle, and a ruler or meter rule to measure the length.
**中文:** 显示使用单摆测定重力加速度的实验装置图。它包括一个铁架台、一根绳子、一个摆锤、一个用于测量初始角度的量角器，以及一把用于测量摆长的尺子或米尺。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM: Pendulum Experiment Setup**
> A clean, labeled diagram of a simple pendulum experiment. A clamp stand holds a string from which a metal bob is suspended. A protractor is shown at the pivot point to indicate the small angle of release (θ < 10°). A meter rule is placed vertically next to the pendulum to measure the length 'l' from the clamp to the center of the bob. A stopwatch is shown nearby.

### Labels Required / 需要标注
- **Clamp and Stand** / 铁架台
- **String (inextensible)** / 绳子（不可伸长）
- **Bob (point mass)** / 摆锤（质点）
- **Length, $l$** / 摆长 $l$
- **Angle of release, $\theta$** / 释放角度 $\theta$
- **Equilibrium position** / 平衡位置

### Exam Importance / 考试重要性
**English:** This is a required practical for both CAIE and Edexcel. You must be able to draw and label this setup, describe the procedure, and identify sources of error (e.g., reaction time in starting/stopping the stopwatch, measuring length to the center of mass, air resistance).
**中文:** 这是CAIE和Edexcel都要求的必做实验。你必须能够绘制并标注此装置，描述实验步骤，并识别误差来源（例如，启动/停止秒表的反应时间，测量到质心的摆长，空气阻力）。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Period / 计算周期

### Question / 题目
**English:** A simple pendulum of length 1.2 m is set into oscillation on Earth, where $g = 9.81 \, ms^{-2}$. Calculate the period of the pendulum.
**中文:** 一个摆长为1.2米的单摆在地球上开始振动，已知 $g = 9.81 \, ms^{-2}$。计算该单摆的周期。

### Solution / 解答
1.  **Identify the formula:** $T = 2\pi \sqrt{\frac{l}{g}}$
2.  **Substitute values:** $T = 2\pi \sqrt{\frac{1.2}{9.81}}$
3.  **Calculate:** $T = 2\pi \sqrt{0.1223} = 2\pi \times 0.3498$
4.  **Final:** $T = 2.20 \, s$

### Final Answer / 最终答案
**Answer:** $T = 2.20 \, s$ | **答案：** $T = 2.20 \, s$

### Quick Tip / 提示
**English:** Always ensure your calculator is in radian mode when dealing with trigonometric functions in SHM, although for this specific formula, it doesn't matter as you are only using arithmetic.
**中文:** 在处理SHM中的三角函数时，务必确保计算器处于弧度模式，尽管对于这个特定公式，由于只用到算术运算，所以无关紧要。

## Example 2: Determining $g$ from Experimental Data / 从实验数据确定 $g$

### Question / 题目
**English:** In an experiment to determine $g$, a student measures the period $T$ for different lengths $l$ of a simple pendulum. The graph of $T^2$ against $l$ has a gradient of $4.02 \, s^2 m^{-1}$. Calculate the value of $g$.
**中文:** 在测定 $g$ 的实验中，一名学生测量了不同摆长 $l$ 下单摆的周期 $T$。$T^2$ 对 $l$ 的图线斜率为 $4.02 \, s^2 m^{-1}$。计算 $g$ 的值。

### Solution / 解答
1.  **Relate gradient to $g$:** From $T^2 = \frac{4\pi^2}{g} l$, the gradient $m = \frac{4\pi^2}{g}$.
2.  **Rearrange for $g$:** $g = \frac{4\pi^2}{m}$.
3.  **Substitute:** $g = \frac{4\pi^2}{4.02} = \frac{39.48}{4.02}$.
4.  **Final:** $g = 9.82 \, ms^{-2}$.

### Final Answer / 最终答案
**Answer:** $g = 9.82 \, ms^{-2}$ | **答案：** $g = 9.82 \, ms^{-2}$

### Quick Tip / 提示
**English:** Plotting $T^2$ vs $l$ is better than plotting $T$ vs $l$ because it linearizes the data, making it easier to find the gradient and hence $g$.
**中文:** 绘制 $T^2$ 对 $l$ 的图线比绘制 $T$ 对 $l$ 的图线更好，因为它使数据线性化，更容易找到斜率，从而求出 $g$。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Derivation of $T = 2\pi \sqrt{l/g}$ | High | Medium | 📝 *待填入* |
| Calculation of period or length | High | Low | 📝 *待填入* |
| Experimental determination of $g$ | High | Medium | 📝 *待填入* |
| Effect of changing parameters (mass, amplitude) | Medium | Low | 📝 *待填入* |
| Pendulum on other planets | Low | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Derive / 推导:** Show the step-by-step mathematical proof.
- **Determine / 测定:** Calculate a value from given data or a graph.
- **Describe / 描述:** Explain the experimental procedure.
- **Explain / 解释:** Give reasons for an observation or result.
- **State / 陈述:** Give a brief answer without explanation.

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
The simple pendulum is a core practical for determining $g$. Key practical skills include:
- **Measurement:** Measuring length $l$ from the pivot to the center of the bob using a meter rule. Measuring the time for a number of oscillations (e.g., 20) to reduce the percentage uncertainty in $T$.
- **Uncertainties:** Calculating the uncertainty in $T$ from the range of repeated measurements. Propagating uncertainties to find the uncertainty in $g$.
- **Graph Plotting:** Plotting $T^2$ against $l$ and drawing a line of best fit. Calculating the gradient and using it to find $g$.
- **Experimental Design:** Controlling variables (e.g., keeping the angle small). Identifying and minimizing sources of error (e.g., parallax error in reading the ruler, reaction time in using the stopwatch).

**中文:**
单摆是测定 $g$ 的核心实验。关键的实验技能包括：
- **测量：** 使用米尺测量从支点到摆锤质心的摆长 $l$。测量多次振动（例如20次）的时间，以减小 $T$ 的百分比不确定度。
- **不确定度：** 根据重复测量的极差计算 $T$ 的不确定度。传递不确定度以求出 $g$ 的不确定度。
- **绘图：** 绘制 $T^2$ 对 $l$ 的图线，并画出最佳拟合直线。计算斜率并用它来求 $g$。
- **实验设计：** 控制变量（例如，保持小角度）。识别并最小化误差来源（例如，读取尺子时的视差误差，使用秒表时的反应时间）。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    subgraph "Prerequisites / 先决条件"
        A[Equations of Motion (SUVAT)] --> B[Angular Measures]
        B --> C[Conditions for SHM]
    end

    subgraph "This Leaf Node / 本子知识点"
        C --> D[Simple Pendulum]
        D --> E[Restoring Force: F = -mg sinθ]
        E --> F[Small Angle Approximation: sinθ ≈ θ]
        F --> G[Derivation of T = 2π√(l/g)]
        G --> H[Factors Affecting Period: l, g]
        G --> I[Factors NOT Affecting Period: m, Amplitude]
    end

    subgraph "Related Topics / 相关主题"
        G --> J[Energy in SHM]
        H --> K[Mass-Spring System]
        I --> L[Displacement, Velocity and Acceleration in SHM]
    end

    subgraph "Practical Application / 实际应用"
        G --> M[Experiment to Determine g]
        M --> N[Graph of T² vs l]
        N --> O[Calculate g from Gradient]
    end
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | A point mass on a massless, inextensible string swinging under gravity. / 一个质点在一根无质量、不可伸长的绳子上，在重力作用下摆动。 |
| **Key Formula / 核心公式** | $T = 2\pi \sqrt{\frac{l}{g}}$ |
| **Key Graph / 核心图表** | $T^2$ vs $l$: Straight line through origin. Gradient $= \frac{4\pi^2}{g}$. / $T^2$ 对 $l$：过原点的直线。斜率 $= \frac{4\pi^2}{g}$. |
| **Conditions for SHM / SHM的条件** | Small angle ($\theta < 10^\circ$), so $\sin \theta \approx \theta$. / 小角度 ($\theta < 10^\circ$)，使得 $\sin \theta \approx \theta$. |
| **Independent of / 无关因素** | Mass of bob ($m$) and amplitude ($A$). / 摆锤质量 ($m$) 和振幅 ($A$). |
| **Exam Tip / 考试提示** | Derive the formula step-by-step. Use the $T^2$ vs $l$ graph to find $g$. Remember the small angle approximation is in radians. / 逐步推导公式。使用 $T^2$ 对 $l$ 的图线求 $g$。记住小角度近似是以弧度为单位的。 |