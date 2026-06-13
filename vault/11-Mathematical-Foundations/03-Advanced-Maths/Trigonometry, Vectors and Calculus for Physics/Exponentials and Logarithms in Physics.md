# 1. Overview / 概述

**English:**
Exponentials and logarithms are fundamental mathematical tools in physics, appearing in phenomena ranging from radioactive decay and capacitor discharge to sound intensity and population growth. This sub-topic covers the properties of exponential functions ($e^x$, $a^x$) and their inverse logarithmic functions ($\ln x$, $\log_{10} x$), with a focus on their physical applications. Understanding these concepts is crucial for modeling processes where rates of change are proportional to the quantity itself — a pattern that recurs across mechanics, electricity, nuclear physics, and waves. This leaf node connects to the broader [[Trigonometry, Vectors and Calculus for Physics]] hub and builds on [[Orders of Magnitude Estimation]] while preparing for [[Simple Harmonic Motion]] and [[Differentiation for Kinematics and Rates of Change]].

**中文:**
指数和对数是物理学中的基础数学工具，出现在从放射性衰变和电容器放电到声音强度和人口增长等各种现象中。本子知识点涵盖指数函数（$e^x$，$a^x$）及其反函数对数函数（$\ln x$，$\log_{10} x$）的性质，重点是其物理应用。理解这些概念对于建模变化率与数量本身成正比的过程至关重要——这种模式在力学、电学、核物理和波动学中反复出现。本叶节点连接到更广泛的 [[Trigonometry, Vectors and Calculus for Physics]] 枢纽，建立在 [[Orders of Magnitude Estimation]] 的基础上，并为 [[Simple Harmonic Motion]] 和 [[Differentiation for Kinematics and Rates of Change]] 做准备。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| Understand and use exponential and logarithmic functions in physical contexts | Use exponential and logarithmic functions in physical contexts |
| Solve equations involving exponentials and logarithms | Manipulate exponential and logarithmic expressions |
| Interpret graphs of exponential growth and decay | Interpret exponential and logarithmic graphs |
| Apply natural logarithms to linearize exponential relationships | Use logarithms to linearize data for analysis |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to recognize when a physical process follows exponential behavior, manipulate exponential and logarithmic equations, and use logarithms to transform exponential relationships into linear forms for graph analysis. The natural logarithm ($\ln$) is preferred for physical applications involving $e$, while $\log_{10}$ is used for decibel scales and pH.
- **中文:** 学生必须能够识别物理过程何时遵循指数行为，处理指数和对数方程，并使用对数将指数关系转化为线性形式以进行图形分析。自然对数（$\ln$）优先用于涉及 $e$ 的物理应用，而 $\log_{10}$ 用于分贝标度和 pH 值。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Exponential Function** / 指数函数 | A function of the form $f(x) = a^x$ where $a > 0$ and $a \neq 1$, or $f(x) = e^{kx}$ where $e$ is Euler's number | 形式为 $f(x) = a^x$（其中 $a > 0$ 且 $a \neq 1$）或 $f(x) = e^{kx}$（其中 $e$ 是欧拉数）的函数 | Confusing $a^x$ with $x^a$ — the variable is in the exponent |
| **Natural Exponential** / 自然指数 | The exponential function with base $e \approx 2.718$, written as $e^x$ or $\exp(x)$ | 以 $e \approx 2.718$ 为底的指数函数，写作 $e^x$ 或 $\exp(x)$ | Forgetting that $e$ is a constant, not a variable |
| **Logarithm** / 对数 | The inverse of an exponential: if $y = a^x$, then $\log_a y = x$ | 指数的逆运算：如果 $y = a^x$，则 $\log_a y = x$ | Thinking $\log(a+b) = \log a + \log b$ (wrong — it's $\log(ab) = \log a + \log b$) |
| **Natural Logarithm** / 自然对数 | Logarithm with base $e$, written as $\ln x$ | 以 $e$ 为底的对数，写作 $\ln x$ | Confusing $\ln x$ with $\log_{10} x$ |
| **Exponential Decay** / 指数衰减 | A process where quantity decreases at a rate proportional to its current value: $N = N_0 e^{-\lambda t}$ | 数量以与其当前值成正比的速率减少的过程：$N = N_0 e^{-\lambda t}$ | Forgetting that the exponent must be dimensionless |
| **Half-life** / 半衰期 | The time taken for a quantity to reduce to half its initial value in exponential decay | 在指数衰减中，数量减少到初始值一半所需的时间 | Confusing half-life with mean lifetime ($\tau = 1/\lambda$) |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Exponential Growth and Decay / 指数增长与衰减

### Explanation / 解释
**English:** In physics, many processes follow the differential equation $\frac{dN}{dt} = \pm \lambda N$, where the rate of change is proportional to the quantity itself. The solution is $N(t) = N_0 e^{\pm \lambda t}$, where $N_0$ is the initial value and $\lambda$ is the decay/growth constant. Positive exponent gives growth (e.g., population, chain reactions), negative gives decay (e.g., radioactive decay, capacitor discharge). The constant $\lambda$ has units of $s^{-1}$ (inverse time). This concept is essential for [[Simple Harmonic Motion]] and [[Differentiation for Kinematics and Rates of Change]].

**中文:** 在物理学中，许多过程遵循微分方程 $\frac{dN}{dt} = \pm \lambda N$，其中变化率与数量本身成正比。解为 $N(t) = N_0 e^{\pm \lambda t}$，其中 $N_0$ 是初始值，$\lambda$ 是衰减/增长常数。正指数表示增长（如人口、链式反应），负指数表示衰减（如放射性衰变、电容器放电）。常数 $\lambda$ 的单位为 $s^{-1}$（时间的倒数）。这个概念对于 [[Simple Harmonic Motion]] 和 [[Differentiation for Kinematics and Rates of Change]] 至关重要。

### Physical Meaning / 物理意义
**English:** The exponential function describes processes where the rate of change is always proportional to the current amount. This means the quantity never reaches zero in finite time (theoretically) but approaches it asymptotically. The time constant $\tau = 1/\lambda$ represents the time for the quantity to fall to $1/e \approx 37\%$ of its initial value.

**中文:** 指数函数描述了变化率始终与当前量成正比的过程。这意味着数量在有限时间内永远不会达到零（理论上），而是渐近地趋近于零。时间常数 $\tau = 1/\lambda$ 表示数量下降到初始值的 $1/e \approx 37\%$ 所需的时间。

### Common Misconceptions / 常见误区
- **English:** Students often think exponential decay reaches zero — it only approaches zero asymptotically.
- **English:** Confusing the decay constant $\lambda$ with half-life $t_{1/2}$ — they are related by $t_{1/2} = \ln 2 / \lambda$.
- **中文:** 学生常认为指数衰减会达到零——它只是渐近地趋近于零。
- **中文:** 混淆衰减常数 $\lambda$ 和半衰期 $t_{1/2}$——它们的关系为 $t_{1/2} = \ln 2 / \lambda$。

### Exam Tips / 考试提示
- **English:** Always check units: $\lambda$ must be in $s^{-1}$ for time in seconds. The exponent $\lambda t$ must be dimensionless.
- **English:** For graph linearization, take natural logs: $\ln N = \ln N_0 - \lambda t$ gives a straight line with gradient $-\lambda$.
- **中文:** 始终检查单位：时间以秒为单位时，$\lambda$ 必须为 $s^{-1}$。指数 $\lambda t$ 必须无量纲。
- **中文:** 对于图形线性化，取自然对数：$\ln N = \ln N_0 - \lambda t$ 得到斜率为 $-\lambda$ 的直线。

> 📷 **IMAGE PROMPT — EXP-01: Exponential Decay Curve**
> A graph showing exponential decay: y-axis labeled "N (quantity)" from 0 to N₀, x-axis labeled "t (time)" from 0 to 5τ. The curve starts at N₀ and decays smoothly toward zero. Mark points at t=τ (N=N₀/e ≈ 0.37N₀) and t=t₁/₂ (N=N₀/2). Include a dashed horizontal line at N₀/2 and N₀/e. Clean, textbook-style with grid lines.

## 4.2 Logarithmic Linearization / 对数线性化

### Explanation / 解释
**English:** A powerful technique in physics is using logarithms to transform exponential relationships into linear ones. For $y = Ae^{kx}$, taking natural logs gives $\ln y = \ln A + kx$, which is linear in $x$ with gradient $k$ and intercept $\ln A$. For $y = Ax^n$, taking logs of both sides gives $\log y = \log A + n \log x$, also linear. This is crucial for analyzing experimental data in [[Orders of Magnitude Estimation]] and [[Integration for Area Under Curves]].

**中文:** 物理学中一个强大的技巧是使用对数将指数关系转化为线性关系。对于 $y = Ae^{kx}$，取自然对数得到 $\ln y = \ln A + kx$，这是关于 $x$ 的线性方程，斜率为 $k$，截距为 $\ln A$。对于 $y = Ax^n$，两边取对数得到 $\log y = \log A + n \log x$，也是线性的。这对于分析 [[Orders of Magnitude Estimation]] 和 [[Integration for Area Under Curves]] 中的实验数据至关重要。

### Physical Meaning / 物理意义
**English:** Linearization allows us to verify exponential behavior experimentally and extract physical constants (decay constant, growth rate, exponent) from the gradient of a straight-line graph. This is standard practice in radioactive decay experiments, capacitor discharge investigations, and cooling curve analysis.

**中文:** 线性化使我们能够通过实验验证指数行为，并从直线图的斜率中提取物理常数（衰减常数、增长率、指数）。这是放射性衰变实验、电容器放电研究和冷却曲线分析中的标准做法。

### Common Misconceptions / 常见误区
- **English:** Using $\log_{10}$ when $\ln$ is required (or vice versa) — check the base of the exponential.
- **English:** Forgetting that $\ln(AB) = \ln A + \ln B$ and $\ln(A/B) = \ln A - \ln B$.
- **中文:** 在需要 $\ln$ 时使用 $\log_{10}$（反之亦然）——检查指数的底数。
- **中文:** 忘记 $\ln(AB) = \ln A + \ln B$ 和 $\ln(A/B) = \ln A - \ln B$。

### Exam Tips / 考试提示
- **English:** When linearizing $y = Ae^{kx}$, plot $\ln y$ against $x$ — gradient is $k$, intercept is $\ln A$.
- **English:** When linearizing $y = Ax^n$, plot $\log y$ against $\log x$ — gradient is $n$, intercept is $\log A$.
- **中文:** 线性化 $y = Ae^{kx}$ 时，绘制 $\ln y$ 对 $x$ 的图——斜率为 $k$，截距为 $\ln A$。
- **中文:** 线性化 $y = Ax^n$ 时，绘制 $\log y$ 对 $\log x$ 的图——斜率为 $n$，截距为 $\log A$。

> 📷 **IMAGE PROMPT — EXP-02: Logarithmic Linearization**
> Two graphs side by side. Left: exponential decay curve N = N₀e^(-λt) with curved shape. Right: same data plotted as ln(N) vs t, showing a straight line with negative slope -λ. Labels: "Original exponential data" and "Linearized using natural log". Arrows connecting corresponding points. Clean, educational style.

---

# 5. Essential Equations / 核心公式

## 5.1 Exponential Function Definition / 指数函数定义

$$ e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $e$ | Euler's number, ~2.71828 | 欧拉数，约2.71828 | dimensionless |
| $x$ | Exponent | 指数 | dimensionless |
| $n!$ | n factorial | n的阶乘 | dimensionless |

**Derivation / 推导:** This is the Taylor series expansion of $e^x$ around $x=0$.

## 5.2 Exponential Growth/Decay / 指数增长/衰减

$$ N(t) = N_0 e^{\pm \lambda t} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $N(t)$ | Quantity at time t | t时刻的数量 | varies |
| $N_0$ | Initial quantity | 初始数量 | varies |
| $\lambda$ | Decay/growth constant | 衰减/增长常数 | $s^{-1}$ |
| $t$ | Time | 时间 | s |

**Conditions / 适用条件:** Rate of change proportional to quantity; $\lambda > 0$ for decay, $\lambda < 0$ for growth.
**Limitations / 局限性:** Assumes continuous process; breaks down at very small numbers (quantum effects).

## 5.3 Half-life Relationship / 半衰期关系

$$ t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $t_{1/2}$ | Half-life | 半衰期 | s |
| $\lambda$ | Decay constant | 衰减常数 | $s^{-1}$ |
| $\ln 2$ | Natural log of 2 (~0.693) | 2的自然对数（约0.693） | dimensionless |

**Derivation / 推导:** Set $N = N_0/2$, solve $N_0/2 = N_0 e^{-\lambda t_{1/2}}$, giving $1/2 = e^{-\lambda t_{1/2}}$, so $\ln(1/2) = -\lambda t_{1/2}$, thus $t_{1/2} = \ln 2 / \lambda$.

## 5.4 Logarithm Properties / 对数性质

$$ \ln(ab) = \ln a + \ln b $$
$$ \ln\left(\frac{a}{b}\right) = \ln a - \ln b $$
$$ \ln(a^n) = n \ln a $$
$$ \ln(e^x) = x $$
$$ e^{\ln x} = x $$

**Conditions / 适用条件:** $a > 0$, $b > 0$ for real logarithms.
**Limitations / 局限性:** Cannot take log of zero or negative numbers in real analysis.

## 5.5 Linearization Forms / 线性化形式

$$ \ln y = \ln A + kx \quad \text{(for } y = Ae^{kx} \text{)} $$
$$ \log y = \log A + n \log x \quad \text{(for } y = Ax^n \text{)} $$

> 📋 **CIE Only:** CIE expects students to use natural logs ($\ln$) for exponential relationships and $\log_{10}$ for power law relationships.
> 📋 **Edexcel Only:** Edexcel emphasizes both $\ln$ and $\log_{10}$ linearization, with particular focus on radioactive decay and capacitor discharge contexts.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Exponential Decay Graph / 指数衰减图

### Axes / 坐标轴
- **X-axis:** Time $t$ (s) / 时间 $t$（秒）
- **Y-axis:** Quantity $N$ (varies) / 数量 $N$（可变）

### Shape / 形状
**English:** A smooth curve starting at $N_0$ on the y-axis, decreasing rapidly at first then more slowly, approaching zero asymptotically. The curve never crosses the x-axis.
**中文:** 从 y 轴上的 $N_0$ 开始的平滑曲线，先快速下降然后变慢，渐近趋近于零。曲线永远不会穿过 x 轴。

### Gradient Meaning / 斜率含义
**English:** The gradient at any point equals $-\lambda N$, representing the instantaneous rate of decay. It is always negative and its magnitude decreases over time.
**中文:** 任意点的斜率等于 $-\lambda N$，表示瞬时衰减率。它始终为负，其大小随时间减小。

### Area Meaning / 面积含义
**English:** The area under the curve from $t=0$ to $t=\infty$ equals $N_0/\lambda$, representing the total "exposure" or integrated quantity.
**中文:** 从 $t=0$ 到 $t=\infty$ 的曲线下面积等于 $N_0/\lambda$，表示总"暴露量"或积分量。

### Exam Interpretation / 考试解读
**English:** Be able to read off half-life from the graph (time for N to halve). The curve should show that each successive half-life reduces the quantity by half.
**中文:** 能够从图中读出半衰期（N 减半所需的时间）。曲线应显示每个连续的半衰期使数量减半。

## 6.2 Logarithmic Linearization Graph / 对数线性化图

### Axes / 坐标轴
- **X-axis:** Time $t$ (s) / 时间 $t$（秒）
- **Y-axis:** $\ln N$ (dimensionless) / $\ln N$（无量纲）

### Shape / 形状
**English:** A straight line with negative slope $-\lambda$ and y-intercept $\ln N_0$. The linearity confirms exponential behavior.
**中文:** 斜率为 $-\lambda$、y 截距为 $\ln N_0$ 的直线。线性关系确认了指数行为。

### Gradient Meaning / 斜率含义
**English:** The gradient equals $-\lambda$, the negative of the decay constant. A steeper slope means faster decay.
**中文:** 斜率等于 $-\lambda$，即衰减常数的负值。斜率越陡表示衰减越快。

### Area Meaning / 面积含义
**English:** Not typically used for this graph. Focus on gradient and intercept.
**中文:** 此图通常不使用面积。关注斜率和截距。

### Exam Interpretation / 考试解读
**English:** If the $\ln N$ vs $t$ graph is not a straight line, the process is NOT exponential. Calculate $\lambda$ from gradient: $\lambda = -(\text{gradient})$.
**中文:** 如果 $\ln N$ 对 $t$ 的图不是直线，则该过程不是指数过程。从斜率计算 $\lambda$：$\lambda = -(\text{斜率})$。

> 📷 **IMAGE PROMPT — EXP-03: Log-linear Graph**
> A straight line graph of ln(N) vs time with negative slope. Axes labeled: x-axis "Time / s", y-axis "ln(N)". The line has intercept ln(N₀) on y-axis. Mark two points on the line and show the calculation of gradient = Δ(ln N)/Δt = -λ. Include error bars on data points. Clean, exam-style.

---

# 7. Required Diagrams / 必备图表

## 7.1 Exponential Decay with Half-life Markers / 带半衰期标记的指数衰减图

### Description / 描述
**English:** A graph showing exponential decay with half-life markers at $t_{1/2}$, $2t_{1/2}$, $3t_{1/2}$, etc., demonstrating that the quantity halves each half-life. Include the time constant $\tau = 1/\lambda$ marker.
**中文:** 显示指数衰减的图，在 $t_{1/2}$、$2t_{1/2}$、$3t_{1/2}$ 等处有半衰期标记，显示每个半衰期数量减半。包括时间常数 $\tau = 1/\lambda$ 标记。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — EXP-04: Exponential Decay with Half-lives**
> Graph of exponential decay N = N₀e^(-λt). Y-axis: N from 0 to N₀. X-axis: time from 0 to 5t₁/₂. Mark points at t=0 (N=N₀), t=t₁/₂ (N=N₀/2), t=2t₁/₂ (N=N₀/4), t=3t₁/₂ (N=N₀/8). Draw dashed horizontal lines at N₀/2, N₀/4, N₀/8. Also mark τ = 1/λ where N = N₀/e. Label "Half-life t₁/₂" and "Time constant τ". Clean textbook style with grid.

### Labels Required / 需要标注
- **English:** $N_0$, $N_0/2$, $N_0/4$, $N_0/8$, $t_{1/2}$, $2t_{1/2}$, $3t_{1/2}$, $\tau = 1/\lambda$, $N_0/e$
- **中文:** $N_0$、$N_0/2$、$N_0/4$、$N_0/8$、$t_{1/2}$、$2t_{1/2}$、$3t_{1/2}$、$\tau = 1/\lambda$、$N_0/e$

### Exam Importance / 考试重要性
**English:** Essential for understanding radioactive decay, capacitor discharge, and any process with constant proportional rate. Frequently tested in both CIE and Edexcel.
**中文:** 对于理解放射性衰变、电容器放电以及任何具有恒定比例速率的过程至关重要。在 CIE 和 Edexcel 中经常考到。

## 7.2 Logarithmic Linearization Setup / 对数线性化设置图

### Description / 描述
**English:** A diagram showing how to transform an exponential decay curve into a straight line by plotting $\ln N$ against $t$. Include the original data points and the transformed points.
**中文:** 显示如何通过绘制 $\ln N$ 对 $t$ 的图将指数衰减曲线转化为直线的图。包括原始数据点和变换后的点。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — EXP-05: Linearization Transformation**
> Two-panel diagram. Left panel: curved exponential decay with 6 data points with error bars. Right panel: same data plotted as ln(N) vs t showing straight line with best fit. Arrows connecting corresponding points between panels. Labels: "Original data: N vs t" and "Linearized: ln(N) vs t". Show gradient calculation on right panel. Educational style.

### Labels Required / 需要标注
- **English:** Original data points, transformed data points, best fit line, gradient $= -\lambda$, intercept $= \ln N_0$
- **中文:** 原始数据点、变换后的数据点、最佳拟合线、斜率 $= -\lambda$、截距 $= \ln N_0$

### Exam Importance / 考试重要性
**English:** Critical for practical paper questions where students must analyze exponential data. Common in Paper 3 (CIE) and Unit 6 (Edexcel).
**中文:** 对于学生必须分析指数数据的实验试卷问题至关重要。常见于 CIE Paper 3 和 Edexcel Unit 6。

---

# 8. Worked Examples / 典型例题

## Example 1: Radioactive Decay Half-life / 放射性衰变半衰期

### Question / 题目
**English:** A radioactive sample has an initial activity of 1200 Bq. After 8.0 days, the activity is 150 Bq. Calculate:
(a) The decay constant $\lambda$
(b) The half-life $t_{1/2}$
(c) The activity after 20 days

**中文:** 一个放射性样品的初始活度为 1200 Bq。8.0 天后，活度为 150 Bq。计算：
(a) 衰减常数 $\lambda$
(b) 半衰期 $t_{1/2}$
(c) 20 天后的活度

### Solution / 解答

**Step 1: Identify the exponential decay equation**
$$ A = A_0 e^{-\lambda t} $$
where $A_0 = 1200$ Bq, $A = 150$ Bq, $t = 8.0$ days.

**Step 2: Solve for $\lambda$**
$$ 150 = 1200 e^{-\lambda \times 8.0} $$
$$ \frac{150}{1200} = e^{-8\lambda} $$
$$ 0.125 = e^{-8\lambda} $$
$$ \ln(0.125) = -8\lambda $$
$$ \lambda = -\frac{\ln(0.125)}{8} = -\frac{-2.079}{8} = 0.260 \text{ day}^{-1} $$

**Step 3: Calculate half-life**
$$ t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{0.260} = 2.67 \text{ days} $$

**Step 4: Calculate activity after 20 days**
$$ A = 1200 e^{-0.260 \times 20} = 1200 e^{-5.20} = 1200 \times 0.00552 = 6.62 \text{ Bq} $$

### Final Answer / 最终答案
**Answer:** (a) $\lambda = 0.260 \text{ day}^{-1}$, (b) $t_{1/2} = 2.67 \text{ days}$, (c) $A = 6.62 \text{ Bq}$ | **答案：** (a) $\lambda = 0.260 \text{ 天}^{-1}$，(b) $t_{1/2} = 2.67 \text{ 天}$，(c) $A = 6.62 \text{ Bq}$

### Quick Tip / 提示
**English:** Check that after 3 half-lives ($3 \times 2.67 = 8.01$ days), activity should be $1200/8 = 150$ Bq — confirming our answer.
**中文:** 检查 3 个半衰期后（$3 \times 2.67 = 8.01$ 天），活度应为 $1200/8 = 150$ Bq——确认我们的答案。

## Example 2: Capacitor Discharge / 电容器放电

### Question / 题目
**English:** A capacitor discharges through a resistor. The voltage across the capacitor follows $V = V_0 e^{-t/RC}$. Given $V_0 = 12.0$ V, $R = 100$ k$\Omega$, $C = 50$ $\mu$F:
(a) Calculate the time constant $\tau = RC$
(b) Find the voltage after 15 seconds
(c) How long does it take for voltage to fall to 3.0 V?

**中文:** 一个电容器通过电阻放电。电容器两端的电压遵循 $V = V_0 e^{-t/RC}$。给定 $V_0 = 12.0$ V，$R = 100$ k$\Omega$，$C = 50$ $\mu$F：
(a) 计算时间常数 $\tau = RC$
(b) 求 15 秒后的电压
(c) 电压降到 3.0 V 需要多长时间？

### Solution / 解答

**Step 1: Calculate time constant**
$$ \tau = RC = (100 \times 10^3) \times (50 \times 10^{-6}) = 5.0 \text{ s} $$

**Step 2: Voltage after 15 seconds**
$$ V = 12.0 e^{-15/5.0} = 12.0 e^{-3} = 12.0 \times 0.0498 = 0.598 \text{ V} $$

**Step 3: Time to reach 3.0 V**
$$ 3.0 = 12.0 e^{-t/5.0} $$
$$ \frac{3.0}{12.0} = 0.25 = e^{-t/5.0} $$
$$ \ln(0.25) = -\frac{t}{5.0} $$
$$ t = -5.0 \times \ln(0.25) = -5.0 \times (-1.386) = 6.93 \text{ s} $$

### Final Answer / 最终答案
**Answer:** (a) $\tau = 5.0$ s, (b) $V = 0.598$ V, (c) $t = 6.93$ s | **答案：** (a) $\tau = 5.0$ 秒，(b) $V = 0.598$ 伏特，(c) $t = 6.93$ 秒

### Quick Tip / 提示
**English:** After one time constant ($t = \tau$), voltage falls to $V_0/e \approx 0.368V_0 = 4.42$ V. After 3 time constants ($t = 3\tau$), it's $V_0/e^3 \approx 0.598$ V.
**中文:** 一个时间常数后（$t = \tau$），电压降到 $V_0/e \approx 0.368V_0 = 4.42$ V。三个时间常数后（$t = 3\tau$），为 $V_0/e^3 \approx 0.598$ V。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Radioactive decay half-life calculation | Very High | Medium | 📝 *待填入* |
| Capacitor discharge exponential analysis | High | Medium | 📝 *待填入* |
| Logarithmic linearization graph analysis | High | Medium-Hard | 📝 *待填入* |
| Exponential growth (e.g., population, chain reaction) | Low | Medium | 📝 *待填入* |
| Decibel scale (logarithmic) | Low | Easy | 📝 *待填入* |
| Solving exponential equations with ln | Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, Show that, Plot, Linearize, Find, Hence, Sketch
- **中文:** 计算、确定、证明、绘制、线性化、求、因此、画出

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Exponentials and logarithms are central to several A-Level practical experiments:

1. **Radioactive Decay (Geiger-Müller tube):** Measure count rate over time, plot $\ln(\text{count rate})$ vs time to find decay constant and half-life. Key skills: background radiation subtraction, uncertainty in count rate ($\sqrt{N}$), error bars on log graph.

2. **Capacitor Discharge (RC circuit):** Measure voltage across capacitor during discharge, plot $\ln V$ vs $t$ to find time constant $\tau = RC$. Key skills: timing with stopwatch, voltage measurement, ensuring capacitor is fully charged before discharge.

3. **Cooling Curves (Newton's Law of Cooling):** Measure temperature of hot object cooling, plot $\ln(T - T_{\text{room}})$ vs $t$ to verify exponential cooling. Key skills: temperature measurement, controlling room temperature, identifying when cooling becomes non-exponential.

4. **Data Analysis:** Always linearize exponential data before drawing best-fit lines. Use log-linear graph paper or calculate $\ln$ values. Calculate gradient from best-fit line, not from individual data points.

**Uncertainty Considerations:**
- When taking $\ln$ of a value, the absolute uncertainty transforms: $\Delta(\ln x) \approx \Delta x / x$
- Error bars on $\ln N$ vs $t$ graphs are smaller for larger $N$ values
- Weighted best-fit lines may be needed for uneven uncertainties

**中文:**
指数和对数是几个 A-Level 实验的核心：

1. **放射性衰变（盖革-米勒管）：** 随时间测量计数率，绘制 $\ln(\text{计数率})$ 对时间的图以找到衰减常数和半衰期。关键技能：本底辐射扣除、计数率的不确定度（$\sqrt{N}$）、对数图上的误差棒。

2. **电容器放电（RC 电路）：** 测量放电期间电容器两端的电压，绘制 $\ln V$ 对 $t$ 的图以找到时间常数 $\tau = RC$。关键技能：用秒表计时、电压测量、确保放电前电容器完全充电。

3. **冷却曲线（牛顿冷却定律）：** 测量热物体冷却时的温度，绘制 $\ln(T - T_{\text{室温}})$ 对 $t$ 的图以验证指数冷却。关键技能：温度测量、控制室温、识别何时冷却变为非指数。

4. **数据分析：** 在绘制最佳拟合线之前始终对指数数据进行线性化。使用对数线性坐标纸或计算 $\ln$ 值。从最佳拟合线计算斜率，而不是从单个数据点。

**不确定度考虑：**
- 对值取 $\ln$ 时，绝对不确定度变换为：$\Delta(\ln x) \approx \Delta x / x$
- $\ln N$ 对 $t$ 图上的误差棒在 $N$ 值较大时较小
- 对于不均匀的不确定度，可能需要加权最佳拟合线

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core concepts
    EXP[Exponential Functions<br/>指数函数] --> DECAY[Exponential Decay<br/>指数衰减]
    EXP --> GROWTH[Exponential Growth<br/>指数增长]
    
    %% Logarithm connections
    LOG[Logarithms<br/>对数] --> LN[Natural Log ln<br/>自然对数 ln]
    LOG --> LOG10[Log Base 10<br/>以10为底的对数]
    
    %% Key relationships
    DECAY --> HALF[Half-life t₁/₂<br/>半衰期]
    DECAY --> TAU[Time Constant τ<br/>时间常数]
    DECAY --> LINEAR[Linearization<br/>线性化]
    GROWTH --> LINEAR
    
    %% Linearization methods
    LINEAR --> LNPLOT[ln(N) vs t plot<br/>ln(N)对t图]
    LINEAR --> LOGLOG[log-log plot<br/>双对数图]
    
    %% Physical applications
    DECAY --> RADIO[Radioactive Decay<br/>放射性衰变]
    DECAY --> CAP[Capacitor Discharge<br/>电容器放电]
    DECAY --> COOL[Newton's Cooling<br/>牛顿冷却]
    GROWTH --> POP[Population Growth<br/>人口增长]
    GROWTH --> CHAIN[Chain Reactions<br/>链式反应]
    
    %% Logarithmic scales
    LOG10 --> DECIBEL[Decibel Scale<br/>分贝标度]
    LOG10 --> PH[pH Scale<br/>pH标度]
    
    %% Connections to other topics
    DECAY --> SHM[[Simple Harmonic Motion]]
    LINEAR --> DIFF[[Differentiation for Kinematics and Rates of Change]]
    EXP --> INTEG[[Integration for Area Under Curves]]
    
    %% Mathematical foundations
    EXP --> EULER[Euler's Number e<br/>欧拉数e]
    LOG --> LOGPROP[Log Properties<br/>对数性质]
    
    %% Styling
    classDef core fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef app fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef math fill:#f3e5f5,stroke:#4a148c,stroke-width:1px
    classDef link fill:#e8f5e9,stroke:#1b5e20,stroke-width:1px
    
    class EXP,LOG core
    class DECAY,GROWTH,HALF,TAU,LINEAR app
    class LN,LOG10,EULER,LOGPROP math
    class RADIO,CAP,COOL,POP,CHAIN,DECIBEL,PH link
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Exponential: $f(x) = e^{kx}$ or $a^x$; Logarithm: inverse of exponential, $\ln(e^x) = x$ |
| **Key Formula / 核心公式** | $N = N_0 e^{-\lambda t}$ (decay), $t_{1/2} = \ln 2 / \lambda$, $\tau = 1/\lambda$ |
| **Log Properties / 对数性质** | $\ln(ab) = \ln a + \ln b$, $\ln(a/b) = \ln a - \ln b$, $\ln(a^n) = n\ln a$ |
| **Linearization / 线性化** | $y = Ae^{kx}$ → plot $\ln y$ vs $x$ (gradient $= k$, intercept $= \ln A$) |
| **Key Graph / 核心图表** | Exponential decay: curved; $\ln N$ vs $t$: straight line with slope $-\lambda$ |
| **Half-life / 半衰期** | Time for quantity to halve; constant for exponential decay; $t_{1/2} = 0.693/\lambda$ |
| **Time Constant / 时间常数** | $\tau = 1/\lambda$; time for quantity to fall to $1/e \approx 37\%$ of initial |
| **Common Applications / 常见应用** | Radioactive decay, capacitor discharge ($RC$ circuits), Newton's cooling, sound intensity (dB) |
| **Exam Tip / 考试提示** | Always check exponent is dimensionless; use $\ln$ for $e$-based exponentials; linearize before drawing best-fit |
| **Common Mistake / 常见错误** | $\ln(A+B) \neq \ln A + \ln B$; $\log(a^x) \neq x\log a$ (it IS $x\log a$ — correct!) |
| **Units / 单位** | $\lambda$ in $s^{-1}$, $t_{1/2}$ and $\tau$ in seconds, exponent $\lambda t$ dimensionless |
| **Practical Skill / 实验技能** | Plot $\ln(\text{data})$ vs time; calculate gradient from best-fit line; propagate uncertainties through $\ln$ |

> 📋 **CIE Only:** CIE expects proficiency with natural logs ($\ln$) for exponential decay/growth and $\log_{10}$ for power laws. Be prepared to interpret log-linear graph paper in Paper 3 practicals.
> 
> 📋 **Edexcel Only:** Edexcel emphasizes the relationship between exponential functions and differential equations ($dN/dt = -\lambda N$). Unit 1 (WPH11) includes mathematical skills questions on exponentials and logs.