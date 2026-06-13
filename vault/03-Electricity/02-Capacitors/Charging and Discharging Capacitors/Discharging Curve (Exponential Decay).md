# 1. Overview / 概述

**English:**
This sub-topic focuses on the **discharging curve** of a capacitor through a resistor, which follows an **exponential decay** pattern. When a charged capacitor is connected across a resistor, the stored charge decreases exponentially with time, meaning the rate of discharge is proportional to the remaining charge. This is a fundamental concept in A2 Physics, forming the basis for understanding timing circuits, flash photography, and signal smoothing. The exponential decay model is mathematically described by the equation $Q = Q_0 e^{-t/RC}$, where $RC$ is the [[RC Time Constant]]. This sub-topic is part of the broader [[Charging and Discharging Capacitors]] topic and builds directly on [[Capacitance and Capacitors]] and [[Energy Stored in a Capacitor]].

**中文:**
本子知识点聚焦电容器通过电阻的**放电曲线**，该曲线遵循**指数衰减**模式。当已充电的电容器连接到电阻两端时，储存的电荷随时间呈指数减少，这意味着放电速率与剩余电荷成正比。这是A2物理中的一个基本概念，为理解定时电路、闪光摄影和信号平滑奠定了基础。指数衰减模型由方程 $Q = Q_0 e^{-t/RC}$ 数学描述，其中 $RC$ 是[[RC Time Constant]]。本子知识点属于更广泛的[[Charging and Discharging Capacitors]]主题的一部分，并直接建立在[[Capacitance and Capacitors]]和[[Energy Stored in a Capacitor]]之上。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 19.3(a): Describe the discharge of a capacitor through a resistor | 4.9: Understand the exponential nature of capacitor discharge |
| 19.3(b): Sketch and interpret the exponential decay graph of charge, current, and p.d. against time | 4.10: Derive and use the equation $Q = Q_0 e^{-t/RC}$ |
| 19.3(c): Derive and use the equation $Q = Q_0 e^{-t/RC}$ | 4.11: Understand the significance of the time constant $RC$ |
| 19.3(d): Define and use the time constant $\tau = RC$ | 4.12: Use the equation $V = V_0 e^{-t/RC}$ and $I = I_0 e^{-t/RC}$ |
| 19.3(e): Use the equation $V = V_0 e^{-t/RC}$ and $I = I_0 e^{-t/RC}$ | 4.13: Determine the time constant from experimental data |
| 19.3(f): Determine the time constant from experimental data | 4.14: Understand applications of capacitor discharge |
| 19.3(g): Understand applications of capacitor discharge | |

**Examiner Expectations / 考官期望:**
- **CAIE:** Students must be able to derive the exponential decay equation from the differential equation $dQ/dt = -Q/RC$, sketch and interpret graphs, and calculate the time constant from experimental data.
- **Edexcel:** Students must understand the exponential nature, derive and apply the equations, and determine the time constant from graphs.
- **Both:** Students should be able to explain why the discharge is exponential (rate proportional to remaining quantity) and apply the concept to real-world applications.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Exponential Decay** / 指数衰减 | A process where a quantity decreases at a rate proportional to its current value, following $y = y_0 e^{-kt}$ | 一个量以与其当前值成正比的速率减少的过程，遵循 $y = y_0 e^{-kt}$ | Confusing with linear decay; thinking the rate is constant |
| **Discharge Curve** / 放电曲线 | A graph showing how charge, current, or p.d. decreases exponentially with time during capacitor discharge | 显示电容器放电过程中电荷、电流或电势差随时间呈指数减少的图表 | Thinking the curve is a straight line on linear axes |
| **Time Constant ($\tau$)** / 时间常数 | The product $RC$; the time taken for the charge, current, or p.d. to fall to $1/e$ (approximately 37%) of its initial value | 乘积 $RC$；电荷、电流或电势差降至初始值的 $1/e$（约37%）所需的时间 | Confusing with half-life; forgetting units (seconds) |
| **Initial Current ($I_0$)** / 初始电流 | The maximum current at the start of discharge, given by $I_0 = V_0/R$ | 放电开始时的最大电流，由 $I_0 = V_0/R$ 给出 | Forgetting that $I_0$ depends on initial p.d. and resistance |
| **Half-life ($t_{1/2}$)** / 半衰期 | The time taken for the charge, current, or p.d. to fall to half its initial value; $t_{1/2} = \tau \ln 2 \approx 0.693\tau$ | 电荷、电流或电势差降至初始值一半所需的时间；$t_{1/2} = \tau \ln 2 \approx 0.693\tau$ | Confusing with time constant; using wrong formula |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Exponential Decay Mechanism / 指数衰减机制

### Explanation / 解释
**English:**
When a charged capacitor (initial charge $Q_0$, initial p.d. $V_0$) is connected across a resistor $R$, electrons flow from the negative plate through the resistor to the positive plate, neutralizing the charge. The discharge current $I$ is given by $I = V/R = Q/(RC)$. Since $I = -dQ/dt$ (current is the rate of loss of charge), we get the differential equation:

$$ \frac{dQ}{dt} = -\frac{Q}{RC} $$

This equation states that the rate of charge loss is proportional to the remaining charge. Solving this gives the exponential decay equation:

$$ Q = Q_0 e^{-t/RC} $$

Similarly, since $V \propto Q$ and $I \propto V$, we have:

$$ V = V_0 e^{-t/RC} \quad \text{and} \quad I = I_0 e^{-t/RC} $$

where $I_0 = V_0/R = Q_0/(RC)$.

**中文:**
当已充电的电容器（初始电荷 $Q_0$，初始电势差 $V_0$）连接到电阻 $R$ 两端时，电子从负极板通过电阻流向正极板，中和电荷。放电电流 $I$ 由 $I = V/R = Q/(RC)$ 给出。由于 $I = -dQ/dt$（电流是电荷损失率），我们得到微分方程：

$$ \frac{dQ}{dt} = -\frac{Q}{RC} $$

该方程表明电荷损失率与剩余电荷成正比。解此方程得到指数衰减方程：

$$ Q = Q_0 e^{-t/RC} $$

类似地，由于 $V \propto Q$ 且 $I \propto V$，我们有：

$$ V = V_0 e^{-t/RC} \quad \text{和} \quad I = I_0 e^{-t/RC} $$

其中 $I_0 = V_0/R = Q_0/(RC)$。

### Physical Meaning / 物理意义
**English:**
The exponential decay means that in each equal time interval (equal to the time constant $\tau = RC$), the remaining charge decreases by the same factor ($1/e$). This is analogous to radioactive decay. The larger the resistance $R$ or capacitance $C$, the slower the discharge because the time constant $\tau = RC$ is larger. Physically, a larger $R$ reduces the current, and a larger $C$ means more charge to remove.

**中文:**
指数衰减意味着在每个相等的时间间隔（等于时间常数 $\tau = RC$）内，剩余电荷减少相同的倍数（$1/e$）。这类似于放射性衰变。电阻 $R$ 或电容 $C$ 越大，放电越慢，因为时间常数 $\tau = RC$ 越大。物理上，更大的 $R$ 减小电流，更大的 $C$ 意味着需要移除更多电荷。

### Common Misconceptions / 常见误区
- **Misconception 1:** The discharge current is constant. → **Correction:** The current decreases exponentially because it depends on the remaining p.d.
- **Misconception 2:** After one time constant, the capacitor is fully discharged. → **Correction:** After one time constant, 63% has discharged, leaving 37% remaining.
- **Misconception 3:** The discharge curve is a straight line on a linear graph. → **Correction:** It is a curve; only on a semi-log graph does it become a straight line.
- **Misconception 4:** The time constant is the same as half-life. → **Correction:** $\tau = RC$ is the time to fall to $1/e$; half-life $t_{1/2} = \tau \ln 2 \approx 0.693\tau$.

### Exam Tips / 考试提示
- **Tip 1:** Always check whether the question asks for charge, p.d., or current — they all decay exponentially but with different initial values.
- **Tip 2:** When calculating the time constant from a graph, use the time for the quantity to fall to 37% of its initial value, or use the gradient of a semi-log plot.
- **Tip 3:** Remember that $I_0 = V_0/R = Q_0/(RC)$ — this links the three exponential equations.
- **Tip 4:** For "show that" questions, start from the differential equation $dQ/dt = -Q/RC$ and integrate.

> 📷 **IMAGE PROMPT — DC01: Exponential Decay Curve**
> A clear graph showing charge Q (y-axis) against time t (x-axis) for capacitor discharge. The curve starts at Q₀ on the y-axis and decays exponentially, approaching zero asymptotically. Mark the time constant τ = RC on the x-axis, showing that at t = τ, Q = Q₀/e ≈ 0.37Q₀. Also mark t₁/₂ where Q = Q₀/2. Include labels: "Exponential Decay: Q = Q₀e^(-t/RC)", "Time Constant τ", "Half-life t₁/₂". Use a clean, educational style suitable for A-Level physics.

---

# 5. Essential Equations / 核心公式

## Equation 1: Charge Decay / 电荷衰减

$$ Q = Q_0 e^{-t/RC} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $Q$ | Charge at time $t$ | 时间 $t$ 时的电荷 | C (coulomb) |
| $Q_0$ | Initial charge at $t=0$ | $t=0$ 时的初始电荷 | C (coulomb) |
| $t$ | Time elapsed | 经过的时间 | s (second) |
| $R$ | Resistance | 电阻 | $\Omega$ (ohm) |
| $C$ | Capacitance | 电容 | F (farad) |
| $RC$ | Time constant $\tau$ | 时间常数 $\tau$ | s (second) |

**Derivation / 推导:**
Starting from $dQ/dt = -Q/RC$, separate variables: $dQ/Q = -dt/RC$. Integrate: $\int_{Q_0}^Q dQ/Q = -\int_0^t dt/RC$. This gives $\ln(Q/Q_0) = -t/RC$, so $Q = Q_0 e^{-t/RC}$.

**Conditions / 适用条件:**
- The capacitor discharges through a fixed resistor $R$.
- The capacitor has constant capacitance $C$.
- No other sources of e.m.f. in the discharge circuit.

**Limitations / 局限性:**
- Assumes ideal components (no internal resistance in capacitor, no leakage).
- Real capacitors may have leakage current, causing faster discharge.
- At very low voltages, the exponential model may deviate due to dielectric absorption.

## Equation 2: Potential Difference Decay / 电势差衰减

$$ V = V_0 e^{-t/RC} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $V$ | p.d. at time $t$ | 时间 $t$ 时的电势差 | V (volt) |
| $V_0$ | Initial p.d. at $t=0$ | $t=0$ 时的初始电势差 | V (volt) |

**Derivation / 推导:**
Since $Q = CV$ and $Q_0 = CV_0$, substituting into $Q = Q_0 e^{-t/RC}$ gives $CV = CV_0 e^{-t/RC}$, so $V = V_0 e^{-t/RC}$.

## Equation 3: Current Decay / 电流衰减

$$ I = I_0 e^{-t/RC} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $I$ | Current at time $t$ | 时间 $t$ 时的电流 | A (ampere) |
| $I_0$ | Initial current at $t=0$ | $t=0$ 时的初始电流 | A (ampere) |

**Derivation / 推导:**
Since $I = V/R = (V_0/R)e^{-t/RC} = I_0 e^{-t/RC}$, where $I_0 = V_0/R$.

## Equation 4: Half-life Relationship / 半衰期关系

$$ t_{1/2} = \tau \ln 2 = RC \ln 2 \approx 0.693 RC $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $t_{1/2}$ | Half-life | 半衰期 | s (second) |
| $\tau$ | Time constant $RC$ | 时间常数 $RC$ | s (second) |

**Derivation / 推导:**
Set $Q = Q_0/2$ in $Q = Q_0 e^{-t/RC}$: $Q_0/2 = Q_0 e^{-t_{1/2}/RC}$. Cancel $Q_0$: $1/2 = e^{-t_{1/2}/RC}$. Take ln: $\ln(1/2) = -t_{1/2}/RC$. So $-\ln 2 = -t_{1/2}/RC$, giving $t_{1/2} = RC \ln 2$.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Discharge Curve on Linear Axes / 线性坐标上的放电曲线

### Axes / 坐标轴
- **x-axis:** Time $t$ (s) / 时间 $t$ (秒)
- **y-axis:** Charge $Q$ (C), p.d. $V$ (V), or current $I$ (A) / 电荷 $Q$ (库仑)、电势差 $V$ (伏特) 或电流 $I$ (安培)

### Shape / 形状
**English:** A smooth curve starting at the initial value ($Q_0$, $V_0$, or $I_0$) on the y-axis and decreasing exponentially, approaching zero asymptotically. The curve is steepest at the start and gradually flattens.

**中文:** 一条平滑曲线，从y轴上的初始值（$Q_0$、$V_0$ 或 $I_0$）开始，呈指数递减，渐近地趋近于零。曲线在开始时最陡，然后逐渐变平。

### Gradient Meaning / 斜率含义
**English:** The gradient of the $Q$-$t$ graph at any point equals $-I$ (negative of the current). The gradient of the $V$-$t$ graph equals $-I/C$. The gradient decreases in magnitude over time.

**中文:** $Q$-$t$ 图上任意点的斜率等于 $-I$（电流的负值）。$V$-$t$ 图的斜率等于 $-I/C$。斜率的大小随时间减小。

### Area Meaning / 面积含义
**English:** The area under the $I$-$t$ graph represents the total charge that has flowed, which equals the initial charge $Q_0$.

**中文:** $I$-$t$ 图下的面积表示已经流过的总电荷，等于初始电荷 $Q_0$。

### Exam Interpretation / 考试解读
- **Finding $\tau$:** Read the time when the quantity has fallen to $0.37Q_0$ (or $0.37V_0$, $0.37I_0$).
- **Finding $t_{1/2}$:** Read the time when the quantity has fallen to $0.5Q_0$.
- **Comparing circuits:** A larger $RC$ gives a shallower curve (slower decay); a smaller $RC$ gives a steeper curve (faster decay).

## 6.2 Semi-log Graph (Natural Log Plot) / 半对数图（自然对数图）

### Axes / 坐标轴
- **x-axis:** Time $t$ (s) / 时间 $t$ (秒)
- **y-axis:** $\ln Q$, $\ln V$, or $\ln I$ / $\ln Q$、$\ln V$ 或 $\ln I$

### Shape / 形状
**English:** A straight line with negative gradient. This is because taking natural logs of $Q = Q_0 e^{-t/RC}$ gives $\ln Q = \ln Q_0 - t/RC$, which is of the form $y = mx + c$ with gradient $m = -1/RC$.

**中文:** 一条具有负斜率的直线。这是因为对 $Q = Q_0 e^{-t/RC}$ 取自然对数得到 $\ln Q = \ln Q_0 - t/RC$，这是 $y = mx + c$ 的形式，斜率为 $m = -1/RC$。

### Gradient Meaning / 斜率含义
**English:** The gradient of the $\ln Q$ vs $t$ graph is $-1/RC$. Therefore, $RC = -1/\text{gradient}$. This is the most accurate way to determine the time constant from experimental data.

**中文:** $\ln Q$ 对 $t$ 图的斜率为 $-1/RC$。因此，$RC = -1/\text{斜率}$。这是从实验数据确定时间常数的最准确方法。

### Area Meaning / 面积含义
**English:** Not applicable for semi-log graphs.

**中文:** 不适用于半对数图。

### Exam Interpretation / 考试解读
- **Finding $\tau$:** Calculate gradient $m$, then $\tau = RC = -1/m$.
- **Finding $Q_0$:** The y-intercept gives $\ln Q_0$, so $Q_0 = e^{\text{intercept}}$.
- **Checking exponential behavior:** If the data points lie on a straight line, the decay is exponential.

> 📷 **IMAGE PROMPT — DC02: Semi-log Plot for Capacitor Discharge**
> A graph showing ln(Q) (y-axis) against time t (x-axis) for capacitor discharge. The data points form a straight line with negative gradient. Label the y-intercept as ln(Q₀). Show the gradient calculation: gradient = Δ(ln Q)/Δt = -1/RC. Include error bars on data points. Title: "Semi-log Plot for Determining Time Constant". Educational style for A-Level physics.

---

# 7. Required Diagrams / 必备图表

## 7.1 Circuit Diagram for Capacitor Discharge / 电容器放电电路图

### Description / 描述
**English:** A circuit showing a charged capacitor $C$ connected in series with a resistor $R$ and a switch. The switch is initially in position A (charging from a battery) and then moved to position B (discharging through the resistor). An ammeter and voltmeter are included to measure current and p.d. during discharge.

**中文:** 一个电路图，显示已充电的电容器 $C$ 与电阻 $R$ 和开关串联。开关最初在位置A（从电池充电），然后移动到位置B（通过电阻放电）。包括电流表和电压表以测量放电过程中的电流和电势差。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DC03: Capacitor Discharge Circuit**
> A clear circuit diagram showing: a battery (6V), a two-way switch, a capacitor (1000 μF) labeled C, a resistor (10 kΩ) labeled R, an ammeter in series, and a voltmeter in parallel across the capacitor. Switch position A connects the battery to the capacitor for charging. Switch position B connects the capacitor to the resistor for discharging. Include labels: "Charging (A)", "Discharging (B)", "C", "R", "A", "V". Clean, educational style for A-Level physics.

### Labels Required / 需要标注
- Capacitor $C$ / 电容器 $C$
- Resistor $R$ / 电阻 $R$
- Switch positions A (charge) and B (discharge) / 开关位置A（充电）和B（放电）
- Ammeter $A$ / 电流表 $A$
- Voltmeter $V$ / 电压表 $V$
- Battery / 电池

### Exam Importance / 考试重要性
**English:** This circuit is essential for understanding how to set up experiments to measure the discharge curve. Students must be able to draw and explain the circuit, including the role of the switch.

**中文:** 该电路对于理解如何设置实验以测量放电曲线至关重要。学生必须能够绘制和解释电路，包括开关的作用。

## 7.2 Discharge Curve with Time Constant Marked / 标注时间常数的放电曲线

### Description / 描述
**English:** An exponential decay graph of $Q$ vs $t$ with key points marked: initial charge $Q_0$, the point at $t = \tau$ where $Q = Q_0/e \approx 0.37Q_0$, and the point at $t = t_{1/2}$ where $Q = Q_0/2$. The time constant $\tau$ and half-life $t_{1/2}$ are indicated on the time axis.

**中文:** $Q$ 对 $t$ 的指数衰减图，标注了关键点：初始电荷 $Q_0$，$t = \tau$ 处 $Q = Q_0/e \approx 0.37Q_0$ 的点，以及 $t = t_{1/2}$ 处 $Q = Q_0/2$ 的点。时间常数 $\tau$ 和半衰期 $t_{1/2}$ 在时间轴上标出。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DC04: Discharge Curve with Time Constant**
> A graph of charge Q (y-axis) against time t (x-axis) for capacitor discharge. The curve starts at Q₀ on the y-axis. Mark point A at (τ, Q₀/e) with dashed lines to axes. Mark point B at (t₁/₂, Q₀/2) with dashed lines. Label τ and t₁/₂ on the x-axis. Add annotations: "At t = τ, Q = Q₀/e ≈ 0.37Q₀" and "At t = t₁/₂, Q = Q₀/2". Include equation Q = Q₀e^(-t/RC). Clean educational style.

### Labels Required / 需要标注
- $Q_0$ (initial charge) / $Q_0$（初始电荷）
- $Q_0/e$ at $t = \tau$ / $t = \tau$ 处的 $Q_0/e$
- $Q_0/2$ at $t = t_{1/2}$ / $t = t_{1/2}$ 处的 $Q_0/2$
- Time constant $\tau = RC$ / 时间常数 $\tau = RC$
- Half-life $t_{1/2} = \tau \ln 2$ / 半衰期 $t_{1/2} = \tau \ln 2$

### Exam Importance / 考试重要性
**English:** Students must be able to read values from the graph, calculate the time constant, and understand the relationship between $\tau$ and $t_{1/2}$.

**中文:** 学生必须能够从图中读取数值，计算时间常数，并理解 $\tau$ 和 $t_{1/2}$ 之间的关系。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Charge After a Given Time / 例1：计算给定时间后的电荷

### Question / 题目
**English:**
A 470 μF capacitor is charged to 12 V and then discharged through a 10 kΩ resistor. Calculate:
(a) The initial charge stored on the capacitor.
(b) The time constant of the discharge circuit.
(c) The charge remaining on the capacitor after 5.0 s.
(d) The time taken for the charge to fall to 25% of its initial value.

**中文:**
一个470 μF的电容器充电至12 V，然后通过一个10 kΩ的电阻放电。计算：
(a) 电容器上储存的初始电荷。
(b) 放电电路的时间常数。
(c) 5.0秒后电容器上剩余的电荷。
(d) 电荷降至初始值25%所需的时间。

### Solution / 解答

**(a) Initial charge / 初始电荷:**
$$ Q_0 = CV_0 = (470 \times 10^{-6})(12) = 5.64 \times 10^{-3} \text{ C} = 5.64 \text{ mC} $$

**(b) Time constant / 时间常数:**
$$ \tau = RC = (10 \times 10^3)(470 \times 10^{-6}) = 4.7 \text{ s} $$

**(c) Charge after 5.0 s / 5.0秒后的电荷:**
$$ Q = Q_0 e^{-t/RC} = (5.64 \times 10^{-3}) e^{-5.0/4.7} $$
$$ Q = (5.64 \times 10^{-3}) e^{-1.064} = (5.64 \times 10^{-3})(0.345) $$
$$ Q = 1.95 \times 10^{-3} \text{ C} = 1.95 \text{ mC} $$

**(d) Time to fall to 25% / 降至25%所需时间:**
$$ Q = 0.25 Q_0 $$
$$ 0.25 Q_0 = Q_0 e^{-t/RC} $$
$$ 0.25 = e^{-t/4.7} $$
$$ \ln(0.25) = -t/4.7 $$
$$ t = -4.7 \ln(0.25) = -4.7(-1.386) = 6.51 \text{ s} $$

### Final Answer / 最终答案
**Answer:** (a) 5.64 mC, (b) 4.7 s, (c) 1.95 mC, (d) 6.51 s
**答案：** (a) 5.64 mC, (b) 4.7 s, (c) 1.95 mC, (d) 6.51 s

### Quick Tip / 提示
**English:** Always convert units to base SI units (F, Ω, V) before calculating. Remember that $e^{-1} \approx 0.37$, so after one time constant, 37% remains.
**中文:** 计算前始终将单位转换为基本SI单位（F、Ω、V）。记住 $e^{-1} \approx 0.37$，所以一个时间常数后，剩余37%。

## Example 2: Determining Time Constant from Experimental Data / 例2：从实验数据确定时间常数

### Question / 题目
**English:**
In an experiment to investigate capacitor discharge, the following data were obtained for the p.d. across a capacitor as it discharges through a resistor:

| Time / s | 0 | 2 | 4 | 6 | 8 | 10 |
|----------|---|---|---|---|---|---|
| V / V | 10.0 | 6.3 | 4.0 | 2.5 | 1.6 | 1.0 |

(a) Show that the discharge follows an exponential decay.
(b) Determine the time constant of the circuit.
(c) Calculate the resistance if the capacitance is 200 μF.

**中文:**
在探究电容器放电的实验中，得到了电容器通过电阻放电时其两端电势差的以下数据：

| 时间 / s | 0 | 2 | 4 | 6 | 8 | 10 |
|----------|---|---|---|---|---|---|
| V / V | 10.0 | 6.3 | 4.0 | 2.5 | 1.6 | 1.0 |

(a) 证明放电遵循指数衰减。
(b) 确定电路的时间常数。
(c) 如果电容为200 μF，计算电阻。

### Solution / 解答

**(a) Show exponential decay / 证明指数衰减:**
Calculate $\ln V$ for each data point:

| t / s | 0 | 2 | 4 | 6 | 8 | 10 |
|-------|---|---|---|---|---|---|
| V / V | 10.0 | 6.3 | 4.0 | 2.5 | 1.6 | 1.0 |
| ln V | 2.30 | 1.84 | 1.39 | 0.92 | 0.47 | 0.00 |

Plot $\ln V$ against $t$. The points lie approximately on a straight line, confirming exponential decay.

**(b) Determine time constant / 确定时间常数:**
From the $\ln V$ vs $t$ graph, gradient $m = \frac{\Delta(\ln V)}{\Delta t}$.

Using first and last points:
$$ m = \frac{0.00 - 2.30}{10 - 0} = \frac{-2.30}{10} = -0.230 \text{ s}^{-1} $$

Since $m = -1/RC$:
$$ RC = -\frac{1}{m} = -\frac{1}{-0.230} = 4.35 \text{ s} $$

Alternatively, using the 37% method: $0.37 \times 10.0 = 3.7$ V. From the data, V ≈ 3.7 V at t ≈ 4.5 s, so $\tau \approx 4.5$ s. The semi-log method gives a more accurate value.

**(c) Calculate resistance / 计算电阻:**
$$ R = \frac{\tau}{C} = \frac{4.35}{200 \times 10^{-6}} = 2.18 \times 10^4 \text{ Ω} = 21.8 \text{ kΩ} $$

### Final Answer / 最终答案
**Answer:** (a) ln V vs t is linear, (b) τ ≈ 4.35 s, (c) R ≈ 21.8 kΩ
**答案：** (a) ln V 对 t 呈线性，(b) τ ≈ 4.35 s，(c) R ≈ 21.8 kΩ

### Quick Tip / 提示
**English:** The semi-log method (plotting ln V against t) is the most accurate way to determine the time constant because it uses all data points and gives a straight line for exponential decay.
**中文:** 半对数方法（绘制 ln V 对 t 的图）是确定时间常数的最准确方法，因为它使用了所有数据点，并且对于指数衰减给出了一条直线。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate charge/p.d./current after a given time | High | Medium | 📝 *待填入* |
| Determine time constant from graph or data | High | Medium-Hard | 📝 *待填入* |
| Derive exponential decay equation | Medium | Hard | 📝 *待填入* |
| Sketch and interpret discharge curves | Medium | Medium | 📝 *待填入* |
| Compare discharge for different RC values | Low-Medium | Medium | 📝 *待填入* |
| Semi-log graph analysis | Medium | Hard | 📝 *待填入* |
| Applications (flash, timing, smoothing) | Low-Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Calculate / 计算:** Use the exponential decay equations with given values.
- **Derive / 推导:** Start from the differential equation and integrate.
- **Sketch / 绘制:** Draw the shape of the curve, labeling key values.
- **Determine / 确定:** Find the time constant from data or a graph.
- **Explain / 解释:** Describe why the discharge is exponential.
- **Show that / 证明:** Demonstrate a relationship using given data.

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
The discharging capacitor experiment is a core practical for both CAIE and Edexcel. Key practical skills include:

1. **Circuit Setup:** Connect the capacitor, resistor, switch, and meters correctly. Use a two-way switch to charge then discharge.
2. **Data Collection:** Use a stopwatch and voltmeter to record p.d. at regular time intervals. For faster discharges, use a data logger.
3. **Graph Plotting:** Plot $V$ vs $t$ (exponential curve) and $\ln V$ vs $t$ (straight line). Determine the time constant from both graphs.
4. **Uncertainty Analysis:** Estimate uncertainties in time (reaction time ~0.1 s) and voltage readings. Use error bars on the semi-log plot.
5. **Experimental Design:** Choose appropriate component values so that the discharge takes a measurable time (e.g., $\tau$ between 5-30 s).
6. **Safety:** Ensure capacitors are discharged before handling (use a shorting wire).

**Common Practical Questions:**
- Why is a data logger better than a stopwatch? (Faster, more accurate, reduces human error)
- How would you improve accuracy? (Use larger $RC$ for slower decay, repeat readings, use digital meters)
- What happens if the capacitor has leakage? (Faster discharge, non-exponential behavior)

**中文:**
电容器放电实验是CAIE和Edexcel的核心实验。关键实验技能包括：

1. **电路搭建：** 正确连接电容器、电阻、开关和仪表。使用双路开关先充电后放电。
2. **数据采集：** 使用秒表和电压表按固定时间间隔记录电势差。对于快速放电，使用数据记录器。
3. **图表绘制：** 绘制 $V$ 对 $t$ 图（指数曲线）和 $\ln V$ 对 $t$ 图（直线）。从两个图中确定时间常数。
4. **不确定度分析：** 估计时间（反应时间约0.1秒）和电压读数的不确定度。在半对数图上使用误差棒。
5. **实验设计：** 选择合适的元件值，使放电时间可测量（例如，$\tau$ 在5-30秒之间）。
6. **安全：** 确保在处理前电容器已放电（使用短路线）。

**常见实验问题：**
- 为什么数据记录器比秒表更好？（更快、更准确、减少人为误差）
- 如何提高准确性？（使用更大的 $RC$ 以获得更慢的衰减、重复读数、使用数字仪表）
- 如果电容器有漏电会发生什么？（放电更快、非指数行为）

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core concept
    DC[Discharging Curve<br/>Exponential Decay] --> EQ1[Q = Q₀e^(-t/RC)]
    DC --> EQ2[V = V₀e^(-t/RC)]
    DC --> EQ3[I = I₀e^(-t/RC)]
    
    %% Key parameters
    DC --> TC[Time Constant τ = RC]
    DC --> HL[Half-life t₁/₂ = τ ln 2]
    
    %% Graphs
    DC --> LG[Linear Graph<br/>Q vs t - Curve]
    DC --> SG[Semi-log Graph<br/>ln Q vs t - Straight Line]
    
    %% Connections to parent topic
    DC -->|Part of| PCC[Charging and Discharging<br/>Capacitors]
    
    %% Connections to siblings
    TC -->|Related to| CC[Charging Curve<br/>Exponential Growth]
    DC -->|Analyzed in| GA[Graphical Analysis]
    DC -->|Applied in| APP[Applications<br/>Flash, Timing, Smoothing]
    
    %% Prerequisites
    PCC -->|Requires| CAP[Capacitance and<br/>Capacitors]
    PCC -->|Requires| ESC[Energy Stored in<br/>a Capacitor]
    
    %% Practical connections
    DC --> PRAC[Practical Skills<br/>Data Collection, Graph Plotting]
    
    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef equation fill:#bbf,stroke:#333,stroke-width:1px
    classDef graph fill:#bfb,stroke:#333,stroke-width:1px
    classDef parent fill:#ff9,stroke:#333,stroke-width:2px
    classDef sibling fill:#9cf,stroke:#333,stroke-width:1px
    classDef prereq fill:#fbb,stroke:#333,stroke-width:1px
    classDef practical fill:#ddd,stroke:#333,stroke-width:1px
    
    class DC core
    class EQ1,EQ2,EQ3,TC,HL equation
    class LG,SG graph
    class PCC parent
    class CC,GA,APP sibling
    class CAP,ESC prereq
    class PRAC practical
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Exponential decay: quantity decreases at a rate proportional to its current value / 指数衰减：量以与其当前值成正比的速率减少 |
| **Key Formula / 核心公式** | $Q = Q_0 e^{-t/RC}$, $V = V_0 e^{-t/RC}$, $I = I_0 e^{-t/RC}$ |
| **Time Constant / 时间常数** | $\tau = RC$; time for quantity to fall to $1/e \approx 37\%$ of initial value / 量降至初始值 $1/e \approx 37\%$ 所需的时间 |
| **Half-life / 半衰期** | $t_{1/2} = \tau \ln 2 \approx 0.693\tau$; time to fall to 50% / 降至50%所需的时间 |
| **Key Graph / 核心图表** | Linear: exponential curve; Semi-log: straight line with gradient $-1/RC$ / 线性：指数曲线；半对数：斜率为 $-1/RC$ 的直线 |
| **Initial Current / 初始电流** | $I_0 = V_0/R = Q_0/(RC)$ |
| **Differential Equation / 微分方程** | $dQ/dt = -Q/RC$ (rate of charge loss ∝ remaining charge) / 电荷损失率 ∝ 剩余电荷 |
| **Semi-log Method / 半对数方法** | Plot $\ln Q$ vs $t$; gradient $= -1/RC$; intercept $= \ln Q_0$ / 绘制 $\ln Q$ 对 $t$ 图；斜率 $= -1/RC$；截距 $= \ln Q_0$ |
| **Common Mistake / 常见错误** | Confusing time constant with half-life; $\tau \neq t_{1/2}$ / 混淆时间常数和半衰期；$\tau \neq t_{1/2}$ |
| **Exam Tip / 考试提示** | Always convert to base SI units; use semi-log for accurate $\tau$ determination / 始终转换为基本SI单位；使用半对数法准确确定 $\tau$ |
| **Practical / 实验** | Use data logger for accuracy; choose $RC$ so discharge takes 5-30 s / 使用数据记录器提高准确性；选择 $RC$ 使放电持续5-30秒 |
| **Application / 应用** | Flash photography (rapid discharge), timing circuits, signal smoothing / 闪光摄影（快速放电）、定时电路、信号平滑 |