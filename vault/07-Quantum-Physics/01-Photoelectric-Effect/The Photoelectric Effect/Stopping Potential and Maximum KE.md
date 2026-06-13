---
# 1. Overview / 概述

**English:**
This sub-topic focuses on the **stopping potential** ($V_s$) and its direct relationship to the **maximum kinetic energy** ($KE_{max}$) of photoelectrons. When light of a sufficiently high frequency (above the [[Work Function and Threshold Frequency|threshold frequency]]) strikes a metal surface, electrons are emitted with a range of kinetic energies. The stopping potential is the minimum reverse voltage required to prevent even the fastest (most energetic) photoelectrons from reaching the collector, effectively reducing the photocurrent to zero. By measuring $V_s$, we can directly determine $KE_{max}$, providing crucial experimental evidence for [[Einstein's Photon Model]] and the [[The Photoelectric Equation]]. This concept is central to understanding how light behaves as a particle (photon) and is a key step towards [[Wave-Particle Duality]].

**中文:**
本子知识点聚焦于**截止电压** ($V_s$) 及其与光电子**最大动能** ($KE_{max}$) 的直接关系。当频率足够高（高于[[Work Function and Threshold Frequency|截止频率]]）的光照射到金属表面时，会发射出具有一系列动能的光电子。截止电压是阻止最快（能量最高）的光电子到达集电极所需的最小反向电压，从而将光电流降至零。通过测量 $V_s$，我们可以直接确定 $KE_{max}$，这为[[Einstein's Photon Model|爱因斯坦光子模型]]和[[The Photoelectric Equation|光电效应方程]]提供了关键的实验证据。这个概念对于理解光如何表现为粒子（光子）至关重要，也是迈向[[Wave-Particle Duality|波粒二象性]]的关键一步。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 22.1 (d) Explain what is meant by the term stopping potential. | 7.3 Understand the concept of stopping potential. |
| 22.1 (e) Recall and use the equation $eV_s = \frac{1}{2}mv_{max}^2$. | 7.4 Use the equation $eV_s = hf - \phi$ to determine the Planck constant and work function. |
| 22.1 (f) Explain how the value of the Planck constant can be determined from a graph of stopping potential against frequency. | 7.5 Analyse experimental data to determine the Planck constant from the $V_s$ vs $f$ graph. |
| 22.1 (g) Describe and explain the effect of varying the intensity and frequency of incident radiation on the stopping potential. | 7.6 Understand the effect of intensity and frequency on stopping potential. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to define stopping potential precisely, derive the relationship between $V_s$ and $KE_{max}$, and interpret the $V_s$ vs $f$ graph to find the Planck constant ($h$) and work function ($\phi$). A common exam question involves explaining why increasing light intensity does **not** increase $V_s$, but increasing frequency **does**.
- **中文:** 你必须能够精确定义截止电压，推导 $V_s$ 和 $KE_{max}$ 之间的关系，并解释 $V_s$ 与 $f$ 的关系图以求出普朗克常数 ($h$) 和逸出功 ($\phi$)。一个常见的考题是解释为什么增加光强度**不会**增加 $V_s$，但增加频率**会**。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Stopping Potential** / 截止电压 | The minimum reverse potential difference applied between the cathode and anode that is just sufficient to prevent the most energetic photoelectrons from reaching the anode, reducing the photocurrent to zero. | 施加在阴极和阳极之间的最小反向电势差，刚好足以阻止能量最高的光电子到达阳极，使光电流降为零。 | Confusing it with the *accelerating* voltage. It is a *reverse* bias. / 将其与*加速*电压混淆。它是*反向*偏压。 |
| **Maximum Kinetic Energy ($KE_{max}$)** / 最大动能 | The maximum kinetic energy possessed by a photoelectron immediately after it is emitted from the metal surface. It is equal to the work done by the stopping potential in bringing the electron to rest: $KE_{max} = eV_s$. | 光电子从金属表面发射后立即具有的最大动能。它等于截止电压使电子停止所做的功：$KE_{max} = eV_s$。 | Thinking all photoelectrons have this energy. Only the fastest ones do. / 认为所有光电子都具有此能量。只有最快的才有。 |
| **Photocurrent** / 光电流 | The electric current that flows in the photoelectric effect circuit due to the movement of photoelectrons from the cathode to the anode. | 在光电效应电路中，由于光电子从阴极移动到阳极而产生的电流。 | Forgetting that photocurrent is proportional to light *intensity*, not frequency. / 忘记光电流与光*强度*成正比，而非频率。 |
| **Reverse Bias** / 反向偏压 | A voltage applied in the circuit that opposes the flow of photoelectrons from the cathode to the anode. The stopping potential is a specific value of reverse bias. | 在电路中施加的、阻碍光电子从阴极流向阳极的电压。截止电压是反向偏压的一个特定值。 | Confusing with forward bias, which accelerates electrons. / 与加速电子的正向偏压混淆。 |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Relationship Between Stopping Potential and Maximum KE / 截止电压与最大动能的关系

### Explanation / 解释
**English:**
When a photoelectron is emitted with maximum kinetic energy ($KE_{max}$), it moves towards the anode. If we apply a **reverse bias** (anode negative relative to cathode), the electric field does work *against* the electron's motion. The work done by the electric field on the electron is $W = eV_s$, where $e$ is the elementary charge and $V_s$ is the stopping potential. The electron will be stopped when this work done equals its initial kinetic energy. Therefore:

$$ KE_{max} = eV_s $$

This is a fundamental equation linking a measurable electrical quantity ($V_s$) to the microscopic energy of a single electron. It allows us to test [[Einstein's Photon Model]] experimentally.

**中文:**
当一个光电子以最大动能 ($KE_{max}$) 发射时，它会向阳极移动。如果我们施加一个**反向偏压**（阳极相对于阴极为负），电场会对电子的运动做*负功*。电场对电子做的功为 $W = eV_s$，其中 $e$ 是元电荷，$V_s$ 是截止电压。当这个功等于电子的初始动能时，电子将被停止。因此：

$$ KE_{max} = eV_s $$

这是一个基本方程，它将一个可测量的电学量 ($V_s$) 与单个电子的微观能量联系起来。它使我们能够通过实验检验[[Einstein's Photon Model|爱因斯坦光子模型]]。

### Physical Meaning / 物理意义
**English:**
The stopping potential is a direct, quantitative measure of the maximum kinetic energy of the photoelectrons. It transforms an invisible energy value into a visible voltage reading on a voltmeter. If $V_s$ is high, the photoelectrons are very energetic. If $V_s$ is zero, the photoelectrons have no kinetic energy (which only happens at the [[Work Function and Threshold Frequency|threshold frequency]]).

**中文:**
截止电压是光电子最大动能的直接、定量的度量。它将一个不可见的能量值转换为电压表上的可见电压读数。如果 $V_s$ 很高，说明光电子能量很大。如果 $V_s$ 为零，说明光电子没有动能（这仅在[[Work Function and Threshold Frequency|截止频率]]时发生）。

### Common Misconceptions / 常见误区
- **English:** "Increasing light intensity increases the stopping potential." (False. Intensity increases the *number* of photons, hence the *photocurrent*, but not the energy of individual photons or electrons. $V_s$ depends only on frequency.)
- **中文:** "增加光强度会增加截止电压。"（错误。强度增加的是*光子数量*，因此是*光电流*，但不会增加单个光子或电子的能量。$V_s$ 仅取决于频率。）
- **English:** "The stopping potential is the voltage at which the first electron is stopped." (False. It is the voltage at which the *last* (most energetic) electron is stopped.)
- **中文:** "截止电压是第一个电子被停止时的电压。"（错误。它是*最后一个*（能量最高的）电子被停止时的电压。）

### Exam Tips / 考试提示
- **English:** When asked to "explain why stopping potential increases with frequency," always start with Einstein's photoelectric equation: $hf = \phi + KE_{max}$. Then state that $KE_{max} = eV_s$, so $hf = \phi + eV_s$. Therefore, if $f$ increases, $V_s$ must increase.
- **中文:** 当被要求"解释为什么截止电压随频率增加而增加"时，始终从爱因斯坦光电效应方程开始：$hf = \phi + KE_{max}$。然后说明 $KE_{max} = eV_s$，所以 $hf = \phi + eV_s$。因此，如果 $f$ 增加，$V_s$ 必须增加。

> 📷 **IMAGE PROMPT — DIAGRAM-01: Stopping Potential Circuit**
> A clear, labeled diagram of a photoelectric effect circuit. The circuit includes a photocell (evacuated glass tube with a metal cathode and a collecting anode), a variable DC power supply connected in reverse bias (positive terminal to cathode, negative terminal to anode), a sensitive ammeter (microammeter) in series, and a voltmeter connected in parallel across the photocell to measure the stopping potential. Arrows should show the direction of electron flow from cathode to anode being opposed by the electric field. The voltage source should be labeled "Variable Reverse Bias".

---

# 5. Essential Equations / 核心公式

## Equation 1: Stopping Potential and Maximum KE / 截止电压与最大动能

$$ KE_{max} = eV_s $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $KE_{max}$ | Maximum kinetic energy of a photoelectron | 光电子的最大动能 | J (Joules) |
| $e$ | Elementary charge ($1.60 \times 10^{-19} \text{ C}$) | 元电荷 | C (Coulombs) |
| $V_s$ | Stopping potential | 截止电压 | V (Volts) |

**Derivation / 推导:**
The work done by the electric field in stopping the electron is $W = Fd = eEd = eV_s$. By the work-energy theorem, this work equals the change in kinetic energy: $W = \Delta KE = 0 - KE_{max}$. Therefore, $eV_s = KE_{max}$.

**Conditions / 适用条件:**
- **English:** This equation applies only to the *most energetic* photoelectrons. It assumes the electron is brought to rest by the stopping potential.
- **中文:** 该方程仅适用于*能量最高*的光电子。它假设电子被截止电压完全停止。

**Limitations / 局限性:**
- **English:** It does not account for the initial kinetic energy distribution of electrons. It only gives the maximum value.
- **中文:** 它没有考虑电子初始动能的分布。它只给出了最大值。

## Equation 2: Combined Einstein Equation / 组合爱因斯坦方程

$$ eV_s = hf - \phi $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $h$ | Planck constant ($6.63 \times 10^{-34} \text{ J s}$) | 普朗克常数 | J s |
| $f$ | Frequency of incident radiation | 入射辐射的频率 | Hz |
| $\phi$ | Work function of the metal | 金属的逸出功 | J |

**Derivation / 推导:**
Combine [[The Photoelectric Equation]] ($hf = \phi + KE_{max}$) with $KE_{max} = eV_s$.

**Conditions / 适用条件:**
- **English:** $f$ must be greater than the [[Work Function and Threshold Frequency|threshold frequency]] ($f > f_0$).
- **中文:** $f$ 必须大于[[Work Function and Threshold Frequency|截止频率]] ($f > f_0$).

**Limitations / 局限性:**
- **English:** This is a classical equation derived from Einstein's quantum model. It does not explain the time delay or intensity independence of $V_s$ (those are explained by the photon model itself).
- **中文:** 这是从爱因斯坦量子模型推导出的经典方程。它不能解释时间延迟或 $V_s$ 与强度的无关性（这些由光子模型本身解释）。

> 📷 **IMAGE PROMPT — GRAPH-01: Stopping Potential vs Frequency Graph**
> A graph with "Frequency (f) / Hz" on the x-axis and "Stopping Potential (Vs) / V" on the y-axis. A straight line with a positive slope is drawn. The line intercepts the x-axis at the threshold frequency (f0). The y-intercept is negative, representing -φ/e. The gradient of the line is labeled as "h/e". The graph should be clean, with clear axis labels and units.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Stopping Potential vs. Frequency Graph / 截止电压-频率图

### Axes / 坐标轴
- **X-axis:** Frequency of incident radiation, $f$ (Hz) / 入射辐射频率 $f$ (Hz)
- **Y-axis:** Stopping potential, $V_s$ (V) / 截止电压 $V_s$ (V)

### Shape / 形状
- **English:** A straight line with a positive gradient. It does not pass through the origin. It intercepts the x-axis at the threshold frequency ($f_0$).
- **中文:** 一条具有正斜率的直线。它不经过原点。它在 x 轴上的截距为截止频率 ($f_0$)。

### Gradient Meaning / 斜率含义
- **English:** The gradient of the line is $\frac{h}{e}$. This is a key method for experimentally determining the Planck constant ($h$).
- **中文:** 直线的斜率为 $\frac{h}{e}$。这是通过实验确定普朗克常数 ($h$) 的关键方法。

### Area Meaning / 面积含义
- **English:** The area under the graph has no direct physical meaning in this context.
- **中文:** 在此上下文中，图线下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
- **English:** You will be asked to:
    1.  Calculate $h$ from the gradient: $h = e \times \text{gradient}$.
    2.  Find the work function $\phi$ from the y-intercept: $\text{y-intercept} = -\frac{\phi}{e}$, so $\phi = -e \times \text{y-intercept}$.
    3.  Find the threshold frequency $f_0$ from the x-intercept.
    4.  Explain why different metals give different lines (different y-intercepts due to different $\phi$, but same gradient $h/e$).
- **中文:** 你可能会被要求：
    1.  从斜率计算 $h$：$h = e \times \text{斜率}$。
    2.  从 y 轴截距求逸出功 $\phi$：$\text{y-截距} = -\frac{\phi}{e}$，所以 $\phi = -e \times \text{y-截距}$。
    3.  从 x 轴截距求截止频率 $f_0$。
    4.  解释为什么不同的金属给出不同的直线（由于 $\phi$ 不同导致 y 截距不同，但斜率 $h/e$ 相同）。

---

# 7. Required Diagrams / 必备图表

## 7.1 Experimental Setup for Measuring Stopping Potential / 测量截止电压的实验装置

### Description / 描述
- **English:** A circuit diagram showing a photocell (evacuated tube with a photosensitive cathode C and a collecting anode A), a variable DC power supply connected in reverse bias, a sensitive ammeter (microammeter), and a voltmeter. The power supply is adjusted until the ammeter reads zero, and the voltmeter reading at that point is the stopping potential $V_s$.
- **中文:** 电路图显示一个光电管（带有光敏阴极 C 和收集阳极 A 的真空管）、一个以反向偏压连接的直流可调电源、一个灵敏电流计（微安表）和一个电压表。调节电源直到电流计读数为零，此时电压表的读数即为截止电压 $V_s$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-02: Stopping Potential Measurement Setup**
> A detailed, clean circuit diagram. A photocell is represented as a circle with two plates inside: a larger curved plate labeled "C (Cathode)" and a smaller straight plate labeled "A (Anode)". A variable DC power supply is connected with its positive terminal to the cathode and its negative terminal to the anode (reverse bias). A microammeter is in series with the power supply. A voltmeter is connected in parallel across the photocell. Arrows indicate the direction of the electric field opposing electron flow. The text "Adjust V until I = 0" should be near the power supply.

### Labels Required / 需要标注
- **English:** Cathode (C), Anode (A), Photocell, Variable DC Supply (Reverse Bias), Microammeter (A), Voltmeter (V), Incident Light, Photoelectrons.
- **中文:** 阴极 (C), 阳极 (A), 光电管, 可调直流电源 (反向偏压), 微安表 (A), 电压表 (V), 入射光, 光电子.

### Exam Importance / 考试重要性
- **English:** High. You must be able to draw and label this circuit. A common question is: "Explain how you would use this circuit to determine the stopping potential for a given frequency of light."
- **中文:** 高。你必须能够画出并标注此电路。一个常见问题是："解释你将如何使用此电路来确定给定频率光的截止电压。"

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Maximum KE from Stopping Potential / 从截止电压计算最大动能

### Question / 题目
**English:**
Light of frequency $7.5 \times 10^{14} \text{ Hz}$ is incident on a metal surface. The stopping potential is measured to be $1.20 \text{ V}$. Calculate the maximum kinetic energy of the photoelectrons in joules and electronvolts. (Take $e = 1.60 \times 10^{-19} \text{ C}$)

**中文:**
频率为 $7.5 \times 10^{14} \text{ Hz}$ 的光照射到金属表面。测得截止电压为 $1.20 \text{ V}$。计算光电子的最大动能，单位分别为焦耳和电子伏特。（取 $e = 1.60 \times 10^{-19} \text{ C}$）

### Solution / 解答
**Step 1: Use the relationship between $V_s$ and $KE_{max}$.**
$$ KE_{max} = eV_s $$

**Step 2: Substitute values.**
$$ KE_{max} = (1.60 \times 10^{-19}) \times (1.20) $$

**Step 3: Calculate.**
$$ KE_{max} = 1.92 \times 10^{-19} \text{ J} $$

**Step 4: Convert to eV.**
Since $1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$,
$$ KE_{max} = \frac{1.92 \times 10^{-19}}{1.60 \times 10^{-19}} = 1.20 \text{ eV} $$

### Final Answer / 最终答案
**Answer:** $1.92 \times 10^{-19} \text{ J}$ or $1.20 \text{ eV}$ | **答案：** $1.92 \times 10^{-19} \text{ J}$ 或 $1.20 \text{ eV}$

### Quick Tip / 提示
- **English:** Notice that the numerical value of $KE_{max}$ in eV is the same as the stopping potential in volts. This is a useful check!
- **中文:** 注意，以 eV 为单位的 $KE_{max}$ 数值与以伏特为单位的截止电压数值相同。这是一个有用的检查方法！

## Example 2: Determining Planck Constant from Graph / 从图表确定普朗克常数

### Question / 题目
**English:**
In an experiment to determine the Planck constant, the following stopping potentials were measured for different frequencies of light incident on a cesium surface:

| Frequency ($\times 10^{14} \text{ Hz}$) | 5.0 | 6.0 | 7.0 | 8.0 | 9.0 |
|----------------------------------------|-----|-----|-----|-----|-----|
| Stopping Potential (V) | 0.20 | 0.60 | 1.00 | 1.40 | 1.80 |

Plot a graph of stopping potential ($V_s$) against frequency ($f$). Use your graph to determine:
(a) The Planck constant, $h$.
(b) The work function, $\phi$, of cesium.
(c) The threshold frequency, $f_0$.

**中文:**
在确定普朗克常数的实验中，对于入射到铯表面的不同频率的光，测得以下截止电压：

| 频率 ($\times 10^{14} \text{ Hz}$) | 5.0 | 6.0 | 7.0 | 8.0 | 9.0 |
|----------------------------------------|-----|-----|-----|-----|-----|
| 截止电压 (V) | 0.20 | 0.60 | 1.00 | 1.40 | 1.80 |

绘制截止电压 ($V_s$) 对频率 ($f$) 的图表。使用你的图表确定：
(a) 普朗克常数 $h$。
(b) 铯的逸出功 $\phi$。
(c) 截止频率 $f_0$。

### Solution / 解答
**Step 1: Plot the graph.**
The points should form a straight line. Draw the best-fit line.

**Step 2: Calculate the gradient.**
Choose two points far apart on the line (not data points).
e.g., Point 1: $(5.0 \times 10^{14} \text{ Hz}, 0.20 \text{ V})$
Point 2: $(9.0 \times 10^{14} \text{ Hz}, 1.80 \text{ V})$
$$ \text{Gradient} = \frac{\Delta V_s}{\Delta f} = \frac{1.80 - 0.20}{(9.0 - 5.0) \times 10^{14}} = \frac{1.60}{4.0 \times 10^{14}} = 4.0 \times 10^{-15} \text{ V s} $$

**Step 3: Determine $h$.**
Since gradient $= h/e$,
$$ h = e \times \text{gradient} = (1.60 \times 10^{-19}) \times (4.0 \times 10^{-15}) = 6.4 \times 10^{-34} \text{ J s} $$

**Step 4: Determine $\phi$.**
Extend the line to find the y-intercept. From the graph, the y-intercept is approximately $-0.80 \text{ V}$.
Since y-intercept $= -\phi/e$,
$$ \phi = -e \times (\text{y-intercept}) = -(1.60 \times 10^{-19}) \times (-0.80) = 1.28 \times 10^{-19} \text{ J} $$

**Step 5: Determine $f_0$.**
The x-intercept is the threshold frequency. From the graph, the line crosses the x-axis at approximately $f_0 = 4.8 \times 10^{14} \text{ Hz}$.

### Final Answer / 最终答案
**Answer:** (a) $h \approx 6.4 \times 10^{-34} \text{ J s}$ | (b) $\phi \approx 1.28 \times 10^{-19} \text{ J}$ | (c) $f_0 \approx 4.8 \times 10^{14} \text{ Hz}$
**答案：** (a) $h \approx 6.4 \times 10^{-34} \text{ J s}$ | (b) $\phi \approx 1.28 \times 10^{-19} \text{ J}$ | (c) $f_0 \approx 4.8 \times 10^{14} \text{ Hz}$

### Quick Tip / 提示
- **English:** Always use points from the best-fit line, not the original data points, to calculate the gradient. This minimizes experimental error.
- **中文:** 始终使用最佳拟合直线上的点，而不是原始数据点，来计算斜率。这可以最小化实验误差。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Definition of stopping potential / 截止电压的定义 | High | Easy | 📝 *待填入* |
| Calculation of $KE_{max}$ from $V_s$ / 从 $V_s$ 计算 $KE_{max}$ | High | Easy | 📝 *待填入* |
| Explaining effect of intensity/frequency on $V_s$ / 解释强度/频率对 $V_s$ 的影响 | High | Medium | 📝 *待填入* |
| Determining $h$ and $\phi$ from $V_s$ vs $f$ graph / 从 $V_s$-$f$ 图确定 $h$ 和 $\phi$ | High | Medium | 📝 *待填入* |
| Drawing and interpreting the $V_s$ vs $f$ graph / 绘制并解释 $V_s$-$f$ 图 | Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Define, Explain, Calculate, Determine, Plot, Sketch, State
- **中文:** 定义, 解释, 计算, 确定, 绘制, 画出, 陈述

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is heavily linked to practical work. Key skills include:
1.  **Circuit Construction:** Setting up the reverse bias circuit correctly.
2.  **Measurement:** Using a voltmeter and microammeter accurately.
3.  **Data Collection:** Varying the frequency of light (using filters) and measuring the corresponding stopping potential.
4.  **Graph Plotting:** Plotting $V_s$ against $f$ and drawing a best-fit straight line.
5.  **Graph Analysis:** Calculating the gradient and intercepts to determine $h$ and $\phi$.
6.  **Uncertainty:** Estimating the uncertainty in $V_s$ (from the voltmeter) and $f$ (from the filter bandwidth) and propagating these to find the uncertainty in $h$.

**中文:**
本子知识点与实验操作紧密相关。关键技能包括：
1.  **电路搭建：** 正确搭建反向偏压电路。
2.  **测量：** 准确使用电压表和微安表。
3.  **数据收集：** 改变光的频率（使用滤光片）并测量相应的截止电压。
4.  **图表绘制：** 绘制 $V_s$ 对 $f$ 的图表并画出最佳拟合直线。
5.  **图表分析：** 计算斜率和截距以确定 $h$ 和 $\phi$。
6.  **不确定度：** 估算 $V_s$（来自电压表）和 $f$（来自滤光片带宽）的不确定度，并传递这些不确定度以求出 $h$ 的不确定度。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Concept
    A[Stopping Potential (Vs) & Maximum KE] --> B[Definition: Min reverse voltage to stop fastest e-]
    A --> C[Key Equation: KEmax = eVs]
    A --> D[Combined Equation: eVs = hf - φ]

    %% Connections to other sub-topics
    A --> E[Einstein's Photon Model]
    A --> F[The Photoelectric Equation]
    A --> G[Work Function & Threshold Frequency]

    %% Experimental & Graphical Analysis
    A --> H[Experimental Circuit: Reverse Bias]
    A --> I[Vs vs f Graph]
    I --> J[Gradient = h/e → find h]
    I --> K[Y-intercept = -φ/e → find φ]
    I --> L[X-intercept = f0 → find threshold frequency]

    %% Effects of Variables
    A --> M[Effect of Increasing Frequency]
    M --> N[Vs increases (more energy per photon)]
    A --> O[Effect of Increasing Intensity]
    O --> P[Vs unchanged (more photons, same energy)]

    %% Broader Connections
    A --> Q[Wave-Particle Duality]
    A --> R[Energy Levels & Spectra]

    %% Styling
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style I fill:#bbf,stroke:#333,stroke-width:2px
    style J fill:#bfb,stroke:#333,stroke-width:1px
    style K fill:#bfb,stroke:#333,stroke-width:1px
    style L fill:#bfb,stroke:#333,stroke-width:1px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | The minimum reverse voltage to stop the most energetic photoelectrons. / 阻止能量最高光电子所需的最小反向电压。 |
| **Key Formula / 核心公式** | $KE_{max} = eV_s$ and $eV_s = hf - \phi$ |
| **Key Graph / 核心图表** | $V_s$ vs $f$: Straight line, gradient $= h/e$, y-intercept $= -\phi/e$, x-intercept $= f_0$. / $V_s$ 对 $f$ 图：直线，斜率 $= h/e$，y 截距 $= -\phi/e$，x 截距 $= f_0$。 |
| **Effect of Intensity / 强度的影响** | Increasing intensity **does not** change $V_s$ (only increases photocurrent). / 增加强度**不会**改变 $V_s$（只会增加光电流）。 |
| **Effect of Frequency / 频率的影响** | Increasing frequency **increases** $V_s$ (linearly). / 增加频率**会增加** $V_s$（线性关系）。 |
| **Exam Tip / 考试提示** | Always link $V_s$ back to $KE_{max}$ and then to Einstein's equation. Use the graph to find $h$ and $\phi$. / 始终将 $V_s$ 联系回 $KE_{max}$，然后联系到爱因斯坦方程。使用图表求 $h$ 和 $\phi$。 |