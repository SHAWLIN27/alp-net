# 1. Overview / 概述

**English:**
This sub-topic focuses on the **graphical analysis** of capacitor charging and discharging circuits. It is a critical skill in A-Level Physics, as it allows you to determine key circuit parameters — such as the time constant (τ), initial current (I₀), and maximum charge (Q₀) — directly from experimental data without complex calculations. You will learn to interpret the characteristic exponential curves for charge (Q), current (I), and voltage (V) against time (t), and crucially, how to linearise these curves using a **logarithmic plot** (ln Q vs t) to extract the time constant from the gradient. This graphical approach is the foundation for many practical experiments (Paper 3/5) and is directly linked to the [[RC Time Constant]] and the [[Charging Curve (Exponential Growth)]] / [[Discharging Curve (Exponential Decay)]] sub-topics. Mastery of this analysis is essential for understanding [[Applications (Flash Photography, Smoothing, Timing)]] and for solving complex past-paper questions.

**中文:**
本子知识点专注于**电容器充放电电路的图形分析**。这是A-Level物理中的一项关键技能，因为它允许你直接从实验数据中确定关键电路参数——如时间常数 (τ)、初始电流 (I₀) 和最大电荷 (Q₀)，而无需复杂计算。你将学习解释电荷 (Q)、电流 (I) 和电压 (V) 随时间 (t) 变化的特征指数曲线，并且至关重要的是，学习如何使用**对数图** (ln Q vs t) 将这些曲线线性化，从而从梯度中提取时间常数。这种图形方法是许多实验考试（Paper 3/5）的基础，并与 [[RC Time Constant]] 和 [[Charging Curve (Exponential Growth)]] / [[Discharging Curve (Exponential Decay)]] 子知识点直接相关。掌握这种分析对于理解 [[Applications (Flash Photography, Smoothing, Timing)]] 和解决复杂的历年真题至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 19.3(a): Show an understanding of and use the term *time constant* (τ = RC). | 4.9: Understand the behaviour of capacitors charging and discharging through a resistor. |
| 19.3(b): Derive and use the equations for the discharging of a capacitor: Q = Q₀e^(-t/RC), I = I₀e^(-t/RC), V = V₀e^(-t/RC). | 4.10: Derive and use the equations for the discharging of a capacitor. |
| 19.3(c): Derive and use the equations for the charging of a capacitor: Q = Q₀(1 - e^(-t/RC)), I = I₀e^(-t/RC), V = V₀(1 - e^(-t/RC)). | 4.11: Derive and use the equations for the charging of a capacitor. |
| 19.3(d): Use the time constant (τ = RC) in calculations. | 4.12: Use the time constant (τ = RC) in calculations. |
| 19.3(e): Analyse graphs of charge, current, and voltage for charging and discharging. | 4.13: Analyse graphs of charge, current, and voltage for charging and discharging. |
| 19.3(f): Determine the time constant from a graph of charge/discharge. | 4.14: Determine the time constant from a graph of charge/discharge. |
| 19.3(g): Use the logarithmic form of the discharging equation to plot a straight-line graph. | (Implicit in 4.14: using ln Q vs t to find τ). |

**Examiner Expectations / 考官期望:**
- **EN:** You must be able to sketch, label, and interpret the exponential curves for Q, I, and V. The most common high-mark question involves plotting ln Q against t for a discharging capacitor and using the gradient to find τ. You must also be able to determine τ from the original exponential curve (e.g., the time for Q to fall to 0.368 Q₀).
- **CN:** 你必须能够绘制、标注和解释 Q、I 和 V 的指数曲线。最常见的高分题涉及绘制放电电容器的 ln Q 对 t 的图，并使用梯度求 τ。你还必须能够从原始指数曲线中确定 τ（例如，Q 下降到 0.368 Q₀ 所需的时间）。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Time Constant (τ)** / 时间常数 | The time taken for the charge (or current or voltage) to fall to 1/e (≈ 0.368) of its initial value during discharge, or to rise to (1 - 1/e) ≈ 0.632 of its final value during charge. | 在放电过程中，电荷（或电流、电压）下降到其初始值的 1/e (≈ 0.368) 所需的时间；或在充电过程中，上升到其最终值的 (1 - 1/e) ≈ 0.632 所需的时间。 | Confusing the 0.368 (discharge) and 0.632 (charge) values. |
| **Exponential Decay** / 指数衰减 | A process where a quantity decreases at a rate proportional to its current value, following the form y = y₀e^(-t/τ). | 一个量以与其当前值成正比的速率减少的过程，遵循形式 y = y₀e^(-t/τ)。 | Thinking the graph is linear; forgetting the 'e' base. |
| **Exponential Growth (to a limit)** / 指数增长（趋于极限） | A process where a quantity increases towards a maximum value, with the rate of increase decreasing over time, following y = y₀(1 - e^(-t/τ)). | 一个量向最大值增加的过程，增加速率随时间减小，遵循 y = y₀(1 - e^(-t/τ))。 | Confusing this with linear growth or simple exponential growth (e.g., population). |
| **Logarithmic Linearisation** / 对数线性化 | The process of taking the natural logarithm of an exponential equation (e.g., Q = Q₀e^(-t/τ)) to produce a straight-line graph (ln Q = -t/τ + ln Q₀). | 对指数方程（例如 Q = Q₀e^(-t/τ)）取自然对数以产生直线图（ln Q = -t/τ + ln Q₀）的过程。 | Forgetting to use ln (natural log), not log₁₀; misinterpreting the gradient. |
| **Initial Current (I₀)** / 初始电流 | The maximum current flowing in the circuit at the instant the switch is closed (t=0). For a discharging capacitor, I₀ = V₀/R. | 在开关闭合的瞬间（t=0）电路中流过的最大电流。对于放电电容器，I₀ = V₀/R。 | Confusing I₀ with the steady-state current (which is zero). |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Exponential Curves / 指数曲线

### Explanation / 解释
**English:** For a capacitor discharging through a resistor, the charge Q, current I, and voltage V all follow an **exponential decay** pattern. The equations are:
- $$ Q = Q_0 e^{-t/RC} $$
- $$ I = I_0 e^{-t/RC} $$
- $$ V = V_0 e^{-t/RC} $$
For a capacitor charging through a resistor, the charge and voltage follow an **exponential growth** pattern towards a maximum, while the current follows an exponential decay:
- $$ Q = Q_0 (1 - e^{-t/RC}) $$
- $$ V = V_0 (1 - e^{-t/RC}) $$
- $$ I = I_0 e^{-t/RC} $$
The key parameter in all these curves is the [[RC Time Constant]] (τ = RC). It determines how quickly the capacitor charges or discharges. A larger τ means a slower process.

**中文:** 对于通过电阻放电的电容器，电荷 Q、电流 I 和电压 V 都遵循**指数衰减**模式。其方程为：
- $$ Q = Q_0 e^{-t/RC} $$
- $$ I = I_0 e^{-t/RC} $$
- $$ V = V_0 e^{-t/RC} $$
对于通过电阻充电的电容器，电荷和电压遵循向最大值**指数增长**的模式，而电流则遵循指数衰减：
- $$ Q = Q_0 (1 - e^{-t/RC}) $$
- $$ V = V_0 (1 - e^{-t/RC}) $$
- $$ I = I_0 e^{-t/RC} $$
所有这些曲线的关键参数是 [[RC Time Constant]] (τ = RC)。它决定了电容器充电或放电的速度。τ 越大，过程越慢。

### Physical Meaning / 物理意义
**English:** The exponential shape arises because the **rate of change** of charge (or current or voltage) is proportional to the **amount of charge remaining** (or the current itself). This is a self-limiting process: as the capacitor discharges, the voltage across it drops, which reduces the current, which in turn slows the rate of further discharge. This creates the characteristic 'hockey-stick' curve.

**中文:** 指数形状的出现是因为**变化率**（电荷、电流或电压）与**剩余量**（或电流本身）成正比。这是一个自限过程：随着电容器放电，其两端的电压下降，这导致电流减小，进而减慢了进一步放电的速率。这就产生了特征性的“曲棍球棒”曲线。

### Common Misconceptions / 常见误区
- **EN:** Thinking the capacitor discharges linearly. It does not; it is exponential.
- **CN:** 认为电容器是线性放电的。它不是；它是指数放电。
- **EN:** Confusing the charging curve of Q (which rises to a maximum) with the discharging curve of Q (which falls to zero).
- **CN:** 混淆 Q 的充电曲线（上升到最大值）和 Q 的放电曲线（下降到零）。
- **EN:** Believing that the current is constant during charging/discharging. The current is maximum at t=0 and decays exponentially.
- **CN:** 认为充放电过程中电流是恒定的。电流在 t=0 时最大，然后呈指数衰减。

### Exam Tips / 考试提示
- **EN:** Always label the axes with the correct quantity and unit. For a discharging graph, the curve should asymptotically approach zero but never touch it.
- **CN:** 始终用正确的量和单位标注坐标轴。对于放电图，曲线应渐近地接近零，但永不触及。
- **EN:** When asked to find τ from a graph, you can either: (a) find the time for the value to fall to 0.368 of its initial value, or (b) use the logarithmic plot method.
- **CN:** 当被要求从图中求 τ 时，你可以：(a) 找到值下降到其初始值的 0.368 所需的时间，或 (b) 使用对数图方法。

> 📷 **IMAGE PROMPT — GRAPH-01: Comparison of Charging and Discharging Curves**
> A clear, labelled graph with two curves on the same set of axes (Q vs t). One curve shows exponential decay (discharge) starting from Q₀ and asymptotically approaching 0. The other shows exponential growth (charge) starting from 0 and asymptotically approaching Q₀. The time constant τ is marked on the x-axis for both curves, showing Q = 0.368Q₀ for discharge and Q = 0.632Q₀ for charge. Use a clean, textbook-style diagram with a white background.

---

## 4.2 Logarithmic Linearisation / 对数线性化

### Explanation / 解释
**English:** This is the most powerful graphical technique for this topic. The discharging equation Q = Q₀e^(-t/RC) is non-linear. By taking the natural logarithm of both sides, we get:
$$ \ln Q = \ln Q_0 - \frac{t}{RC} $$
This is in the form of a straight line: y = mx + c, where:
- y = ln Q
- x = t
- m (gradient) = -1/RC = -1/τ
- c (y-intercept) = ln Q₀
Therefore, if you plot a graph of ln Q against t, you get a **straight line** with a **negative gradient**. The time constant τ can be found from the gradient: τ = -1/m. The y-intercept gives the initial charge Q₀ (since Q₀ = e^(c)).

**中文:** 这是本主题中最强大的图形技术。放电方程 Q = Q₀e^(-t/RC) 是非线性的。通过对两边取自然对数，我们得到：
$$ \ln Q = \ln Q_0 - \frac{t}{RC} $$
这符合直线形式：y = mx + c，其中：
- y = ln Q
- x = t
- m (梯度) = -1/RC = -1/τ
- c (y轴截距) = ln Q₀
因此，如果你绘制 ln Q 对 t 的图，你会得到一条**直线**，其**梯度为负**。时间常数 τ 可以从梯度求得：τ = -1/m。y轴截距给出了初始电荷 Q₀（因为 Q₀ = e^(c)）。

### Physical Meaning / 物理意义
**English:** The logarithmic transformation 'undoes' the exponential relationship, revealing the underlying constant rate of decay. The gradient of the ln Q vs t graph is a direct measure of the **decay constant** (1/τ). A steeper gradient means a smaller time constant (faster discharge).

**中文:** 对数变换“解除了”指数关系，揭示了潜在的恒定衰减率。ln Q 对 t 图的梯度是**衰减常数** (1/τ) 的直接度量。梯度越陡，意味着时间常数越小（放电越快）。

### Common Misconceptions / 常见误区
- **EN:** Using log₁₀ instead of ln (natural log). The equation is derived using ln.
- **CN:** 使用 log₁₀ 而不是 ln（自然对数）。方程是用 ln 推导的。
- **EN:** Forgetting the negative sign on the gradient. The gradient must be negative for a discharging process.
- **CN:** 忘记梯度上的负号。对于放电过程，梯度必须为负。
- **EN:** Plotting ln Q on the x-axis and t on the y-axis. The standard is ln Q on the y-axis.
- **CN:** 将 ln Q 绘制在 x 轴上，t 绘制在 y 轴上。标准做法是将 ln Q 放在 y 轴上。

### Exam Tips / 考试提示
- **EN:** This is a very common Paper 5 (CAIE) or practical question. You will be given a table of Q (or V) vs t. You must calculate ln Q (or ln V) and plot the graph. Then calculate the gradient using a large triangle.
- **CN:** 这是 Paper 5 (CAIE) 或实验题中非常常见的题型。你会得到一张 Q（或 V）对 t 的数据表。你必须计算 ln Q（或 ln V）并绘制图表。然后使用大三角形计算梯度。
- **EN:** The y-intercept is ln Q₀. To find Q₀, you must take the exponential: Q₀ = e^(y-intercept).
- **CN:** y轴截距是 ln Q₀。要求 Q₀，你必须取指数：Q₀ = e^(y轴截距)。

> 📷 **IMAGE PROMPT — GRAPH-02: Logarithmic Linearisation of Discharge Data**
> A two-part diagram. Part (a) shows a curved graph of Q vs t (exponential decay). Part (b) shows the corresponding straight-line graph of ln Q vs t. The axes are clearly labelled. On the ln Q vs t graph, a large gradient triangle is drawn, and the y-intercept is marked. The equation of the line (ln Q = -t/τ + ln Q₀) is displayed on the graph. Use a clean, textbook-style diagram.

---

# 5. Essential Equations / 核心公式

## Equation 1: Discharging Equations / 放电方程

$$ Q = Q_0 e^{-t/RC} \quad I = I_0 e^{-t/RC} \quad V = V_0 e^{-t/RC} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| Q, I, V | Charge, Current, Voltage at time t | 时间 t 时的电荷、电流、电压 | C, A, V |
| Q₀, I₀, V₀ | Initial charge, current, voltage (at t=0) | 初始电荷、电流、电压 (t=0 时) | C, A, V |
| t | Time elapsed since discharge began | 自放电开始以来经过的时间 | s |
| R | Resistance in the discharge path | 放电回路中的电阻 | Ω |
| C | Capacitance of the capacitor | 电容器的电容 | F |
| RC | Time constant (τ) | 时间常数 (τ) | s |

**Derivation / 推导:** From the differential equation: I = -dQ/dt = Q/RC. Solving gives Q = Q₀e^(-t/RC).

**Conditions / 适用条件:**
- **EN:** The capacitor is initially fully charged (Q₀). The circuit contains only a resistor and capacitor in series.
- **CN:** 电容器初始时已充满电 (Q₀)。电路中仅串联一个电阻和一个电容器。

**Limitations / 局限性:**
- **EN:** Assumes ideal components (no internal resistance of the capacitor or battery).
- **CN:** 假设元件是理想的（电容器或电池无内阻）。

---

## Equation 2: Charging Equations / 充电方程

$$ Q = Q_0 (1 - e^{-t/RC}) \quad V = V_0 (1 - e^{-t/RC}) \quad I = I_0 e^{-t/RC} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| Q, V | Charge, Voltage at time t | 时间 t 时的电荷、电压 | C, V |
| Q₀, V₀ | Maximum charge, voltage (final value) | 最大电荷、电压（最终值） | C, V |
| I | Current at time t | 时间 t 时的电流 | A |
| I₀ | Initial current (at t=0) | 初始电流 (t=0 时) | A |
| t, R, C, RC | Same as above | 同上 | s, Ω, F, s |

**Derivation / 推导:** From the differential equation: I = dQ/dt = (V₀ - V)/R. Solving gives Q = Q₀(1 - e^(-t/RC)).

**Conditions / 适用条件:**
- **EN:** The capacitor is initially uncharged. The circuit contains a battery, resistor, and capacitor in series.
- **CN:** 电容器初始时未充电。电路中串联一个电池、一个电阻和一个电容器。

**Limitations / 局限性:**
- **EN:** Assumes the battery has zero internal resistance and provides a constant EMF.
- **CN:** 假设电池内阻为零并提供恒定电动势。

---

## Equation 3: Logarithmic Form / 对数形式

$$ \ln Q = \ln Q_0 - \frac{t}{RC} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| ln Q | Natural logarithm of charge | 电荷的自然对数 | (dimensionless) |
| ln Q₀ | Natural logarithm of initial charge | 初始电荷的自然对数 | (dimensionless) |
| t/RC | t/τ | t/τ | (dimensionless) |

**Derivation / 推导:** Take ln of both sides of Q = Q₀e^(-t/RC).

**Conditions / 适用条件:**
- **EN:** Only valid for the **discharging** process. For charging, the equation is more complex and not linear.
- **CN:** 仅对**放电**过程有效。对于充电，方程更复杂且不是线性的。

**Limitations / 局限性:**
- **EN:** Requires accurate data points, especially at long times when Q is small (ln Q becomes very negative and noisy).
- **CN:** 需要准确的数据点，尤其是在长时间后 Q 很小时（ln Q 变得非常负且有噪声）。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Discharge: Q vs t / 放电：Q 对 t

### Axes / 坐标轴
- **EN:** x-axis: Time (t / s); y-axis: Charge (Q / C)
- **CN:** x轴：时间 (t / s)；y轴：电荷 (Q / C)

### Shape / 形状
- **EN:** Exponential decay curve. Starts at Q₀ (t=0), decreases rapidly, then asymptotically approaches 0.
- **CN:** 指数衰减曲线。从 Q₀ (t=0) 开始，快速下降，然后渐近地接近 0。

### Gradient Meaning / 斜率含义
- **EN:** The gradient (dQ/dt) is the **current** (I). It is negative and its magnitude decreases over time.
- **CN:** 梯度 (dQ/dt) 是**电流** (I)。它为负，其大小随时间减小。

### Area Meaning / 面积含义
- **EN:** Not directly meaningful for this graph.
- **CN:** 此图无直接意义。

### Exam Interpretation / 考试解读
- **EN:** To find τ, find the time when Q = 0.368 Q₀. Draw a horizontal line from 0.368 Q₀ to the curve, then drop a vertical line to the time axis. The time read is τ.
- **CN:** 要求 τ，找到 Q = 0.368 Q₀ 的时间。从 0.368 Q₀ 画一条水平线与曲线相交，然后向时间轴画一条垂直线。读出的时间就是 τ。

---

## 6.2 Discharge: ln Q vs t / 放电：ln Q 对 t

### Axes / 坐标轴
- **EN:** x-axis: Time (t / s); y-axis: ln(Q / C) (or ln Q)
- **CN:** x轴：时间 (t / s)；y轴：ln(Q / C) (或 ln Q)

### Shape / 形状
- **EN:** Straight line with a negative gradient.
- **CN:** 具有负梯度的直线。

### Gradient Meaning / 斜率含义
- **EN:** Gradient = -1/RC = -1/τ. A steeper gradient means a smaller time constant (faster discharge).
- **CN:** 梯度 = -1/RC = -1/τ。梯度越陡，时间常数越小（放电越快）。

### Area Meaning / 面积含义
- **EN:** Not applicable.
- **CN:** 不适用。

### Exam Interpretation / 考试解读
- **EN:** Calculate the gradient using a large triangle. Then τ = -1/gradient. The y-intercept is ln Q₀. Find Q₀ = e^(y-intercept).
- **CN:** 使用大三角形计算梯度。然后 τ = -1/梯度。y轴截距是 ln Q₀。求 Q₀ = e^(y轴截距)。

---

## 6.3 Charge: Q vs t / 充电：Q 对 t

### Axes / 坐标轴
- **EN:** x-axis: Time (t / s); y-axis: Charge (Q / C)
- **CN:** x轴：时间 (t / s)；y轴：电荷 (Q / C)

### Shape / 形状
- **EN:** Exponential growth curve. Starts at 0 (t=0), increases rapidly, then asymptotically approaches Q₀.
- **CN:** 指数增长曲线。从 0 (t=0) 开始，快速增加，然后渐近地接近 Q₀。

### Gradient Meaning / 斜率含义
- **EN:** The gradient (dQ/dt) is the **current** (I). It is positive and its magnitude decreases over time.
- **CN:** 梯度 (dQ/dt) 是**电流** (I)。它为正，其大小随时间减小。

### Area Meaning / 面积含义
- **EN:** Not directly meaningful.
- **CN:** 无直接意义。

### Exam Interpretation / 考试解读
- **EN:** To find τ, find the time when Q = 0.632 Q₀. Draw a horizontal line from 0.632 Q₀ to the curve, then drop a vertical line to the time axis. The time read is τ.
- **CN:** 要求 τ，找到 Q = 0.632 Q₀ 的时间。从 0.632 Q₀ 画一条水平线与曲线相交，然后向时间轴画一条垂直线。读出的时间就是 τ。

---

## 6.4 Current vs Time (Both Processes) / 电流对时间（两种过程）

### Axes / 坐标轴
- **EN:** x-axis: Time (t / s); y-axis: Current (I / A)
- **CN:** x轴：时间 (t / s)；y轴：电流 (I / A)

### Shape / 形状
- **EN:** For **both** charging and discharging, the current follows an **exponential decay** curve. It starts at I₀ (t=0) and asymptotically approaches 0. The only difference is the direction of current (positive for charging, negative for discharging).
- **CN:** 对于**充电和放电**，电流都遵循**指数衰减**曲线。它从 I₀ (t=0) 开始，渐近地接近 0。唯一的区别是电流方向（充电为正，放电为负）。

### Gradient Meaning / 斜率含义
- **EN:** The gradient (dI/dt) is the rate of change of current. It is negative.
- **CN:** 梯度 (dI/dt) 是电流的变化率。它为负。

### Area Meaning / 面积含义
- **EN:** The area under the I-t graph represents the **total charge** that has flowed (Q = ∫ I dt). For discharge, this equals Q₀. For charge, this equals Q₀.
- **CN:** I-t 图下的面积代表流过的**总电荷** (Q = ∫ I dt)。对于放电，这等于 Q₀。对于充电，这也等于 Q₀。

### Exam Interpretation / 考试解读
- **EN:** You can find I₀ from the y-intercept of the I-t graph. Then, if you know R, you can find V₀ = I₀R. The area under the graph can be estimated by counting squares.
- **CN:** 你可以从 I-t 图的 y轴截距找到 I₀。然后，如果你知道 R，你可以找到 V₀ = I₀R。图下的面积可以通过数方格来估算。

---

# 7. Required Diagrams / 必备图表

## 7.1 Circuit Diagram for Charging and Discharging / 充放电电路图

### Description / 描述
- **EN:** A circuit diagram showing a capacitor (C), resistor (R), battery (E), and a two-way switch (S). In one position, the switch connects the battery to the RC circuit (charging). In the other position, it disconnects the battery and connects the RC circuit in a loop (discharging).
- **CN:** 一个电路图，显示电容器 (C)、电阻器 (R)、电池 (E) 和一个双向开关 (S)。在一个位置，开关将电池连接到 RC 电路（充电）。在另一个位置，它断开电池并将 RC 电路连接成一个回路（放电）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-01: Charging and Discharging Circuit**
> A clean, textbook-style circuit diagram. A 6V battery (E) is connected to a two-way switch (S). The switch has two positions: position 'A' connects the battery to a series combination of a 10 kΩ resistor (R) and a 100 μF capacitor (C). Position 'B' connects only the resistor and capacitor in a closed loop (discharging path). A voltmeter is connected in parallel across the capacitor. All components are clearly labelled with their symbols and values. Use a white background.

### Labels Required / 需要标注
- **EN:** Battery (E), Switch (S), Resistor (R), Capacitor (C), Voltmeter (V). Arrows indicating 'Charge' and 'Discharge' paths.
- **CN:** 电池 (E)、开关 (S)、电阻器 (R)、电容器 (C)、电压表 (V)。指示“充电”和“放电”路径的箭头。

### Exam Importance / 考试重要性
- **EN:** Essential for understanding the experimental setup. You must be able to draw and explain this circuit.
- **CN:** 对于理解实验设置至关重要。你必须能够绘制和解释此电路。

---

## 7.2 Combined Graph: Q, I, V vs t for Discharge / 组合图：放电时 Q、I、V 对 t

### Description / 描述
- **EN:** Three separate graphs on the same time axis, showing the exponential decay of Q, I, and V for a discharging capacitor. All three curves have the same time constant τ.
- **CN:** 在同一时间轴上的三个独立图表，显示放电电容器的 Q、I 和 V 的指数衰减。所有三条曲线具有相同的时间常数 τ。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-02: Discharge Graphs for Q, I, and V**
> Three graphs stacked vertically, sharing the same x-axis (Time / s). The top graph shows Q vs t (exponential decay from Q₀ to 0). The middle graph shows V vs t (exponential decay from V₀ to 0). The bottom graph shows I vs t (exponential decay from I₀ to 0). On each graph, the time constant τ is marked on the x-axis, and the corresponding value (0.368 Q₀, 0.368 V₀, 0.368 I₀) is marked on the y-axis. Use a clean, textbook-style diagram with a white background.

### Labels Required / 需要标注
- **EN:** Q₀, V₀, I₀, 0.368Q₀, 0.368V₀, 0.368I₀, τ, axes labels with units.
- **CN:** Q₀, V₀, I₀, 0.368Q₀, 0.368V₀, 0.368I₀, τ, 带单位的坐标轴标签。

### Exam Importance / 考试重要性
- **EN:** High. You must be able to sketch these graphs and explain why they all have the same shape and time constant.
- **CN:** 高。你必须能够绘制这些图表并解释为什么它们都具有相同的形状和时间常数。

---

# 8. Worked Examples / 典型例题

## Example 1: Finding τ from a Discharge Graph / 从放电图中求 τ

### Question / 题目
**English:**
A 100 μF capacitor is discharged through a 50 kΩ resistor. The graph below shows how the charge Q on the capacitor varies with time t. Determine the time constant τ of the circuit.

(Imagine a graph of Q vs t is provided, showing Q₀ = 500 μC at t=0, and Q = 184 μC at t = 5.0 s).

**中文:**
一个 100 μF 的电容器通过一个 50 kΩ 的电阻放电。下图显示了电容器上的电荷 Q 如何随时间 t 变化。确定电路的时间常数 τ。

（假设提供了一个 Q 对 t 的图，显示在 t=0 时 Q₀ = 500 μC，在 t = 5.0 s 时 Q = 184 μC）。

### Solution / 解答
**Step 1: Identify the method.**
- **EN:** We can use the definition of τ: it is the time for Q to fall to 0.368 Q₀.
- **CN:** 我们可以使用 τ 的定义：它是 Q 下降到 0.368 Q₀ 所需的时间。

**Step 2: Calculate 0.368 Q₀.**
- **EN:** 0.368 × 500 μC = 184 μC.
- **CN:** 0.368 × 500 μC = 184 μC。

**Step 3: Read the time from the graph.**
- **EN:** The graph shows that Q = 184 μC at t = 5.0 s. Therefore, τ = 5.0 s.
- **CN:** 图表显示在 t = 5.0 s 时 Q = 184 μC。因此，τ = 5.0 s。

**Step 4: Verification (optional).**
- **EN:** Using the formula τ = RC: τ = (50 × 10³ Ω) × (100 × 10⁻⁶ F) = 5.0 s. This confirms our answer.
- **CN:** 使用公式 τ = RC：τ = (50 × 10³ Ω) × (100 × 10⁻⁶ F) = 5.0 s。这证实了我们的答案。

### Final Answer / 最终答案
**Answer:** τ = 5.0 s | **答案：** τ = 5.0 秒

### Quick Tip / 提示
- **EN:** Always check if the graph provides enough data to use the 0.368 method. If not, you may need to use the logarithmic method.
- **CN:** 始终检查图表是否提供了足够的数据来使用 0.368 方法。如果没有，你可能需要使用对数方法。

---

## Example 2: Using Logarithmic Linearisation / 使用对数线性化

### Question / 题目
**English:**
A student investigates the discharge of a capacitor. She measures the voltage V across the capacitor at different times t. The results are shown in the table.

| t / s | 0 | 10 | 20 | 30 | 40 | 50 |
|-------|---|---|---|---|---|---|
| V / V | 6.0 | 3.3 | 1.8 | 1.0 | 0.55 | 0.30 |

(a) Complete the table by calculating ln(V) for each time.
(b) Plot a graph of ln(V) against t.
(c) Use your graph to determine the time constant τ of the circuit.

**中文:**
一名学生研究电容器的放电。她测量了不同时间 t 时电容器两端的电压 V。结果如下表所示。

| t / s | 0 | 10 | 20 | 30 | 40 | 50 |
|-------|---|---|---|---|---|---|
| V / V | 6.0 | 3.3 | 1.8 | 1.0 | 0.55 | 0.30 |

(a) 通过计算每个时间的 ln(V) 来完成表格。
(b) 绘制 ln(V) 对 t 的图。
(c) 使用你的图表确定电路的时间常数 τ。

### Solution / 解答
**Step 1: Calculate ln(V).**
- **EN:** Using a calculator:
  - t=0: ln(6.0) = 1.79
  - t=10: ln(3.3) = 1.19
  - t=20: ln(1.8) = 0.59
  - t=30: ln(1.0) = 0.00
  - t=40: ln(0.55) = -0.60
  - t=50: ln(0.30) = -1.20
- **CN:** 使用计算器：
  - t=0: ln(6.0) = 1.79
  - t=10: ln(3.3) = 1.19
  - t=20: ln(1.8) = 0.59
  - t=30: ln(1.0) = 0.00
  - t=40: ln(0.55) = -0.60
  - t=50: ln(0.30) = -1.20

**Step 2: Plot the graph.**
- **EN:** Plot ln(V) on the y-axis and t on the x-axis. Draw a best-fit straight line.
- **CN:** 在 y 轴上绘制 ln(V)，在 x 轴上绘制 t。绘制一条最佳拟合直线。

**Step 3: Calculate the gradient.**
- **EN:** Choose two points far apart on the best-fit line. For example:
  - Point 1: (t₁ = 0 s, ln(V)₁ = 1.79)
  - Point 2: (t₂ = 50 s, ln(V)₂ = -1.20)
  - Gradient = ( -1.20 - 1.79 ) / (50 - 0) = -2.99 / 50 = -0.0598 s⁻¹
- **CN:** 在最佳拟合线上选择两个相距较远的点。例如：
  - 点 1: (t₁ = 0 s, ln(V)₁ = 1.79)
  - 点 2: (t₂ = 50 s, ln(V)₂ = -1.20)
  - 梯度 = ( -1.20 - 1.79 ) / (50 - 0) = -2.99 / 50 = -0.0598 s⁻¹

**Step 4: Find τ.**
- **EN:** The gradient = -1/τ. Therefore, τ = -1 / gradient = -1 / (-0.0598) = 16.7 s.
- **CN:** 梯度 = -1/τ。因此，τ = -1 / 梯度 = -1 / (-0.0598) = 16.7 秒。

### Final Answer / 最终答案
**Answer:** τ = 16.7 s | **答案：** τ = 16.7 秒

### Quick Tip / 提示
- **EN:** Always use a large triangle to calculate the gradient. The y-intercept of the graph gives ln(V₀). Here, ln(V₀) = 1.79, so V₀ = e^(1.79) = 6.0 V, which matches the initial voltage.
- **CN:** 始终使用大三角形来计算梯度。图的 y轴截距给出 ln(V₀)。这里，ln(V₀) = 1.79，所以 V₀ = e^(1.79) = 6.0 V，这与初始电压相符。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Sketching and interpreting Q/I/V vs t graphs / 绘制和解读 Q/I/V 对 t 图 | Very High / 非常高 | Medium / 中等 | 📝 *待填入* |
| Determining τ from an exponential graph (0.368 method) / 从指数图中确定 τ (0.368 方法) | High / 高 | Easy / 简单 | 📝 *待填入* |
| Logarithmic linearisation (ln Q vs t) to find τ and Q₀ / 对数线性化 (ln Q 对 t) 求 τ 和 Q₀ | Very High / 非常高 | Hard / 困难 | 📝 *待填入* |
| Calculating area under I-t graph to find total charge / 计算 I-t 图下面积求总电荷 | Medium / 中等 | Medium / 中等 | 📝 *待填入* |
| Comparing charging and discharging curves / 比较充电和放电曲线 | Medium / 中等 | Medium / 中等 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Sketch, Plot, Determine, Calculate, Show, Explain, State.
- **CN:** 绘制、标绘、确定、计算、证明、解释、陈述。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is heavily tested in practical exams (CAIE Paper 3/5, Edexcel IAL Unit 6). Key skills include:
1. **Data Collection:** Using a datalogger or stopwatch to record V or Q at regular time intervals during discharge.
2. **Graph Plotting:** Plotting the raw data (Q vs t) and the linearised data (ln Q vs t). You must choose appropriate scales, label axes, and draw a best-fit line.
3. **Uncertainty Analysis:** Error bars should be plotted on the ln Q vs t graph. The uncertainty in ln Q is calculated as Δ(ln Q) = ΔQ / Q. The gradient uncertainty is found using 'max/min' gradient lines.
4. **Experimental Design:** Choosing appropriate values of R and C to get a measurable time constant (e.g., τ between 10 s and 60 s for manual timing).
5. **Sources of Error:** Leakage current in the capacitor, internal resistance of the voltmeter, and timing errors.

**中文:**
本子知识点在实验考试中（CAIE Paper 3/5, Edexcel IAL Unit 6）被大量测试。关键技能包括：
1. **数据收集：** 使用数据记录器或秒表在放电过程中以规则的时间间隔记录 V 或 Q。
2. **图表绘制：** 绘制原始数据 (Q 对 t) 和线性化数据 (ln Q 对 t)。你必须选择合适的比例尺、标注坐标轴并绘制最佳拟合线。
3. **不确定度分析：** 应在 ln Q 对 t 图上绘制误差棒。ln Q 的不确定度计算为 Δ(ln Q) = ΔQ / Q。梯度不确定度通过“最大/最小”梯度线求得。
4. **实验设计：** 选择合适的 R 和 C 值以获得可测量的时间常数（例如，手动计时 τ 在 10 秒到 60 秒之间）。
5. **误差来源：** 电容器的漏电流、电压表的内阻和计时误差。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Leaf Node: Graphical Analysis of Charging/Discharging
    %% Parent Hub
    GACD[Graphical Analysis of Charging/Discharging] -->|is part of| P[Charging and Discharging Capacitors]
    
    %% Prerequisites
    GACD -->|requires| CAC[Capacitance and Capacitors]
    GACD -->|requires| ESC[Energy Stored in a Capacitor]
    
    %% Sibling Sub-topics
    GACD -->|uses| RCT[RC Time Constant]
    GACD -->|analyses| CCEG[Charging Curve: Exponential Growth]
    GACD -->|analyses| DCED[Discharging Curve: Exponential Decay]
    GACD -->|applied in| APP[Applications: Flash, Smoothing, Timing]
    
    %% Core Concepts within this Leaf
    GACD -->|produces| EXP_CURVES[Exponential Curves: Q, I, V vs t]
    GACD -->|uses| LOG_LIN[Logarithmic Linearisation: ln Q vs t]
    GACD -->|determines| TAU[Time Constant τ from Gradient]
    
    %% Key Equations
    EXP_CURVES -->|described by| EQ_DIS[Q = Q₀e^(-t/RC)]
    EXP_CURVES -->|described by| EQ_CHA[Q = Q₀(1 - e^(-t/RC))]
    LOG_LIN -->|derived from| EQ_LOG[ln Q = ln Q₀ - t/RC]
    
    %% Practical Skills
    GACD -->|requires| PRAC[Practical Skills: Data Collection, Plotting, Uncertainty]
    
    %% Styling
    style GACD fill:#f9f,stroke:#333,stroke-width:4px
    style P fill:#bbf,stroke:#333,stroke-width:2px
    style CAC fill:#dfd,stroke:#333,stroke-width:1px
    style ESC fill:#dfd,stroke:#333,stroke-width:1px
    style RCT fill:#ffd,stroke:#333,stroke-width:1px
    style CCEG fill:#ffd,stroke:#333,stroke-width:1px
    style DCED fill:#ffd,stroke:#333,stroke-width:1px
    style APP fill:#ffd,stroke:#333,stroke-width:1px
    style EXP_CURVES fill:#eef,stroke:#333,stroke-width:1px
    style LOG_LIN fill:#eef,stroke:#333,stroke-width:1px
    style TAU fill:#eef,stroke:#333,stroke-width:1px
    style EQ_DIS fill:#efe,stroke:#333,stroke-width:1px
    style EQ_CHA fill:#efe,stroke:#333,stroke-width:1px
    style EQ_LOG fill:#efe,stroke:#333,stroke-width:1px
    style PRAC fill:#fee,stroke:#333,stroke-width:1px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Time Constant (τ):** Time for Q to fall to 0.368 Q₀ (discharge) or rise to 0.632 Q₀ (charge). τ = RC. |
| **Key Formula / 核心公式** | **Discharge:** Q = Q₀e^(-t/τ), I = I₀e^(-t/τ), V = V₀e^(-t/τ) <br> **Charge:** Q = Q₀(1 - e^(-t/τ)), V = V₀(1 - e^(-t/τ)), I = I₀e^(-t/τ) <br> **Log Form:** ln Q = ln Q₀ - t/τ |
| **Key Graph / 核心图表** | **Discharge (Q vs t):** Exponential decay from Q₀ to 0. <br> **Charge (Q vs t):** Exponential growth from 0 to Q₀. <br> **ln Q vs t:** Straight line with gradient = -1/τ. |
| **Exam Tip / 考试提示** | **Finding τ:** (1) From Q vs t: find time for Q = 0.368Q₀. (2) From ln Q vs t: τ = -1/gradient. <br> **Common Mistake:** Using log₁₀ instead of ln. Always use natural log. <br> **Practical:** Plot ln Q vs t, draw best-fit line, use large triangle for gradient. |