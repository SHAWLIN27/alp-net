---
# 1. Overview / 概述

**English:**
This sub-topic introduces the fundamental concept of **electrical resistance** and its SI unit, the **ohm (Ω)**. Resistance is a measure of how much a component opposes the flow of electric current. We will define resistance using the ratio of potential difference ($V$) to current ($I$), explore the factors that determine the resistance of a conductor, and understand the conditions under which Ohm's law is obeyed. This forms the bedrock for analyzing circuits and understanding energy dissipation in components, linking directly to [[Ohm's Law]] and [[Resistivity and the Resistivity Equation]].

**中文:**
本子知识点介绍**电阻**的基本概念及其国际单位**欧姆 (Ω)**。电阻是衡量元件阻碍电流流动程度的物理量。我们将通过电势差 ($V$) 与电流 ($I$) 的比值来定义电阻，探讨决定导体电阻的因素，并理解欧姆定律的适用条件。这是分析电路和理解元件中能量耗散的基础，直接与[[欧姆定律]]和[[电阻率与电阻率方程]]相关联。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (9.3 a-f) | Edexcel IAL (WPH11 U2: 3.9-3.12) |
|-----------|-------------|
| Define resistance and the ohm. | Define resistance. |
| Recall and use $R = V/I$. | Use the equation $R = V/I$. |
| Describe how the resistance of a metallic conductor changes with temperature. | Explain how the resistance of a metallic conductor varies with temperature. |
| Describe how the resistance of a light-dependent resistor (LDR) changes with light intensity. | Describe the characteristics of an LDR. |
| Describe how the resistance of a thermistor changes with temperature. | Describe the characteristics of a thermistor. |
| Sketch the I-V characteristic of a metallic conductor at constant temperature. | Sketch and interpret I-V characteristics for ohmic conductors. |

**Examiner Expectations / 考官期望:**
- **EN:** You must be able to define resistance from $R=V/I$, not $R = \frac{\rho L}{A}$ (which is resistivity). You must know the ohm in base SI units ($\text{kg m}^2 \text{s}^{-3} \text{A}^{-2}$). You must be able to sketch and interpret I-V graphs for ohmic and non-ohmic components.
- **CN:** 必须能够从 $R=V/I$ 定义电阻，而非 $R = \frac{\rho L}{A}$（那是电阻率）。必须知道欧姆的基本SI单位 ($\text{kg m}^2 \text{s}^{-3} \text{A}^{-2}$)。必须能够绘制并解释欧姆和非欧姆元件的 I-V 图。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Resistance** / 电阻 | The opposition to the flow of electric current in a conductor. Defined as the ratio of potential difference across a component to the current flowing through it: $R = V/I$. | 导体对电流流动的阻碍作用。定义为元件两端的电势差与通过它的电流之比：$R = V/I$。 | Confusing resistance with [[Resistivity and the Resistivity Equation\|resistivity]]. Resistance is a property of a *component*; resistivity is a property of a *material*. |
| **Ohm (Ω)** / 欧姆 | The SI unit of resistance. A component has a resistance of 1 Ω if a potential difference of 1 V across it causes a current of 1 A to flow through it. | 电阻的国际单位。如果元件两端的电势差为 1 V 时，通过它的电流为 1 A，则该元件的电阻为 1 Ω。 | Forgetting the base units: $1 \Omega = 1 \text{ kg m}^2 \text{s}^{-3} \text{A}^{-2}$. |
| **Ohmic Conductor** / 欧姆导体 | A conductor that obeys Ohm's law; its resistance remains constant (at constant temperature) and its I-V characteristic is a straight line through the origin. | 遵循欧姆定律的导体；其电阻（在恒定温度下）保持不变，其 I-V 特性曲线是一条通过原点的直线。 | Assuming all conductors are ohmic. Semiconductors and components like diodes are non-ohmic. |
| **Non-Ohmic Conductor** / 非欧姆导体 | A conductor that does not obey Ohm's law; its resistance changes with the applied voltage or current. Its I-V characteristic is not a straight line. | 不遵循欧姆定律的导体；其电阻随外加电压或电流的变化而变化。其 I-V 特性曲线不是直线。 | Thinking non-ohmic means the graph is not linear. It specifically means the gradient ($\Delta I / \Delta V$) is not constant. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Definition of Resistance / 电阻的定义

### Explanation / 解释
**English:** Resistance ($R$) is defined by the equation $R = \frac{V}{I}$. This is a *definition*, not a law. It tells us how to calculate the resistance of any component at a given operating point. For an [[Ohm's Law|ohmic conductor]] at constant temperature, this value is constant. For a non-ohmic conductor, the value of $R$ changes with $V$ and $I$. The unit of resistance, the ohm (Ω), can be expressed in base SI units. From $V = IR$ and $P = IV$, we can derive: $1 \Omega = \frac{1 \text{ V}}{1 \text{ A}} = \frac{1 \text{ J/C}}{1 \text{ C/s}} = \frac{1 \text{ J s}}{1 \text{ C}^2} = 1 \text{ kg m}^2 \text{s}^{-3} \text{A}^{-2}$.

**中文:** 电阻 ($R$) 由方程 $R = \frac{V}{I}$ 定义。这是一个*定义*，而非定律。它告诉我们如何计算任何元件在给定工作点的电阻。对于恒定温度下的[[欧姆定律|欧姆导体]]，该值为常数。对于非欧姆导体，$R$ 的值随 $V$ 和 $I$ 变化。电阻的单位欧姆 (Ω) 可以用基本 SI 单位表示。由 $V = IR$ 和 $P = IV$ 可推导出：$1 \Omega = \frac{1 \text{ V}}{1 \text{ A}} = \frac{1 \text{ J/C}}{1 \text{ C/s}} = \frac{1 \text{ J s}}{1 \text{ C}^2} = 1 \text{ kg m}^2 \text{s}^{-3} \text{A}^{-2}$。

### Physical Meaning / 物理意义
**English:** Physically, resistance arises from collisions between charge carriers (usually electrons) and the fixed positive ions in the lattice of the conductor. These collisions convert the kinetic energy of the charge carriers into thermal energy (heat), which is why resistors get hot. A higher resistance means more collisions per unit time for a given current.

**中文:** 从物理上讲，电阻源于电荷载流子（通常是电子）与导体晶格中固定的正离子之间的碰撞。这些碰撞将电荷载流子的动能转化为热能（热量），这就是电阻器会发热的原因。对于给定的电流，更高的电阻意味着单位时间内发生更多的碰撞。

### Common Misconceptions / 常见误区
- **EN:** Thinking that $R = V/I$ means resistance depends on voltage. **Correction:** For an ohmic conductor, $R$ is constant. $V$ and $I$ change proportionally, so their ratio stays the same.
- **CN:** 认为 $R = V/I$ 意味着电阻取决于电压。**纠正：** 对于欧姆导体，$R$ 是常数。$V$ 和 $I$ 成比例变化，因此它们的比值保持不变。
- **EN:** Confusing the gradient of an I-V graph with resistance. **Correction:** The gradient of an I-V graph is $1/R$. The gradient of a V-I graph is $R$.
- **CN:** 混淆 I-V 图的斜率与电阻。**纠正：** I-V 图的斜率是 $1/R$。V-I 图的斜率是 $R$。

### Exam Tips / 考试提示
- **EN:** Always state the condition "at constant temperature" when discussing Ohm's law or the resistance of a metallic conductor.
- **CN:** 在讨论欧姆定律或金属导体的电阻时，务必说明“在恒定温度下”这一条件。
- **EN:** When asked to define resistance, write $R = V/I$ and explain that it is the ratio of p.d. to current.
- **CN:** 当被要求定义电阻时，写出 $R = V/I$ 并解释它是电势差与电流的比值。

> 📷 **IMAGE PROMPT — R01: Microscopic View of Resistance**
> A 2D cross-section diagram of a metallic wire. Show a lattice of positive metal ions (blue circles) in a regular grid. Several free electrons (small red dots) are moving from left to right. One electron is shown colliding with an ion, with a small "heat" symbol (a wavy arrow) emanating from the collision point. The direction of the electric field (E) is shown from left to right. The diagram should clearly illustrate the scattering process that causes resistance.

---

# 5. Essential Equations / 核心公式

## Equation 1: Definition of Resistance / 电阻的定义

$$ R = \frac{V}{I} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $R$ | Resistance | 电阻 | Ω (ohm) |
| $V$ | Potential Difference | 电势差 | V (volt) |
| $I$ | Current | 电流 | A (ampere) |

**Derivation / 推导:** This is a definition, not derived from other laws. It is the fundamental relationship between voltage, current, and resistance.

**Conditions / 适用条件:**
- **EN:** This equation is always true for calculating resistance at a specific point. For an ohmic conductor, $R$ is constant. For a non-ohmic conductor, $R$ is the ratio at a specific $V$ and $I$.
- **CN:** 该方程始终适用于计算特定点的电阻。对于欧姆导体，$R$ 是常数。对于非欧姆导体，$R$ 是在特定 $V$ 和 $I$ 下的比值。

**Limitations / 局限性:**
- **EN:** The equation does not explain *why* resistance exists. It is a macroscopic definition. It does not apply to components like a perfect insulator ($I=0$ leads to undefined $R$).
- **CN:** 该方程不解释*为什么*存在电阻。它是一个宏观定义。它不适用于像理想绝缘体这样的元件（$I=0$ 导致 $R$ 未定义）。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 I-V Characteristic for an Ohmic Conductor / 欧姆导体的 I-V 特性曲线

### Axes / 坐标轴
- **X-axis:** Potential Difference, $V$ / 电势差, $V$
- **Y-axis:** Current, $I$ / 电流, $I$

### Shape / 形状
- **EN:** A straight line passing through the origin. The gradient is constant.
- **CN:** 一条通过原点的直线。斜率为常数。

### Gradient Meaning / 斜率含义
- **EN:** The gradient of the I-V graph is $1/R$. A steeper gradient means a lower resistance.
- **CN:** I-V 图的斜率是 $1/R$。斜率越大，电阻越小。

### Area Meaning / 面积含义
- **EN:** The area under the I-V graph is not a standard quantity with a simple physical meaning in this context.
- **CN:** I-V 图下的面积在此上下文中不是一个具有简单物理意义的标准量。

### Exam Interpretation / 考试解读
- **EN:** If the graph is a straight line through the origin, the component is ohmic and obeys Ohm's law. The resistance can be calculated from the gradient ($R = 1/\text{gradient}$) or from any single point ($R = V/I$).
- **CN:** 如果图形是通过原点的直线，则该元件是欧姆的，遵循欧姆定律。电阻可以从斜率 ($R = 1/\text{斜率}$) 或从任何单个点 ($R = V/I$) 计算得出。

> 📷 **IMAGE PROMPT — R02: I-V Graph for Ohmic Conductor**
> A clear graph with labeled axes: "Current I / A" on the y-axis and "Potential Difference V / V" on the x-axis. A straight line passes through the origin (0,0) and extends into the first quadrant. The line has a constant positive gradient. A point on the line is marked with coordinates (V1, I1). An annotation reads: "Gradient = I1/V1 = 1/R".

---

# 7. Required Diagrams / 必备图表

## 7.1 Circuit for Measuring Resistance / 测量电阻的电路

### Description / 描述
- **EN:** A simple circuit used to determine the resistance of a component. It consists of a cell/battery, an ammeter in series with the component, and a voltmeter in parallel with the component. A variable resistor (rheostat) is often included to vary the voltage.
- **CN:** 用于确定元件电阻的简单电路。它由一个电池、一个与元件串联的电流表和一个与元件并联的电压表组成。通常包含一个可变电阻器（变阻器）来改变电压。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — R03: Circuit for Measuring Resistance**
> A clear circuit diagram drawn with standard symbols. A battery (two parallel lines, one longer than the other) is connected to a switch, a variable resistor (a resistor with an arrow through it), an ammeter (A in a circle), and the unknown resistor (R in a rectangle), all in series. A voltmeter (V in a circle) is connected in parallel across the unknown resistor. Arrows show the direction of conventional current flow from the positive terminal of the battery.

### Labels Required / 需要标注
- **EN:** Battery, Switch, Variable Resistor (Rheostat), Ammeter (A), Voltmeter (V), Unknown Resistor (R).
- **CN:** 电池、开关、可变电阻器（变阻器）、电流表 (A)、电压表 (V)、未知电阻 (R)。

### Exam Importance / 考试重要性
- **EN:** High. You must be able to draw this circuit and explain how to use it to measure resistance. You should also be aware of the systematic error caused by the ammeter and voltmeter having their own resistance (see [[Potential Difference and EMF]]).
- **CN:** 高。必须能够绘制此电路并解释如何使用它来测量电阻。还应注意电流表和电压表自身电阻引起的系统误差（参见[[电势差与电动势]]）。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Resistance from I-V Data / 从 I-V 数据计算电阻

### Question / 题目
**English:** A potential difference of 12.0 V is applied across a resistor, and a current of 0.50 A flows through it. Calculate the resistance of the resistor.
**中文:** 在一个电阻器两端施加 12.0 V 的电势差，通过它的电流为 0.50 A。计算该电阻器的电阻。

### Solution / 解答
1.  **Identify knowns / 确定已知量:**
    $V = 12.0 \text{ V}$
    $I = 0.50 \text{ A}$

2.  **Choose the correct equation / 选择正确的方程:**
    $R = \frac{V}{I}$

3.  **Substitute and solve / 代入并求解:**
    $R = \frac{12.0 \text{ V}}{0.50 \text{ A}}$
    $R = 24 \text{ } \Omega$

### Final Answer / 最终答案
**Answer:** 24 Ω | **答案：** 24 Ω

### Quick Tip / 提示
- **EN:** Always ensure your units are consistent (Volts and Amperes to get Ohms).
- **CN:** 始终确保单位一致（伏特和安培得到欧姆）。

## Example 2: Using the Gradient of an I-V Graph / 使用 I-V 图的斜率

### Question / 题目
**English:** The I-V characteristic of a component is a straight line through the origin. The gradient of the line is 0.25 A/V. What is the resistance of the component?
**中文:** 某元件的 I-V 特性曲线是一条通过原点的直线。该直线的斜率为 0.25 A/V。该元件的电阻是多少？

### Solution / 解答
1.  **Recall the relationship / 回忆关系:**
    For an I-V graph, $\text{Gradient} = \frac{\Delta I}{\Delta V} = \frac{1}{R}$.

2.  **Rearrange and solve / 重新排列并求解:**
    $R = \frac{1}{\text{Gradient}} = \frac{1}{0.25 \text{ A/V}}$
    $R = 4 \text{ } \Omega$

### Final Answer / 最终答案
**Answer:** 4 Ω | **答案：** 4 Ω

### Quick Tip / 提示
- **EN:** Be careful! The gradient of an I-V graph is $1/R$, not $R$. If the graph was V-I (V on y-axis, I on x-axis), the gradient would be $R$.
- **CN:** 小心！I-V 图的斜率是 $1/R$，而不是 $R$。如果图形是 V-I（V 在 y 轴，I 在 x 轴），那么斜率就是 $R$。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Definition of resistance and the ohm | Medium | Easy | 📝 *待填入* |
| Calculation of $R = V/I$ | High | Easy | 📝 *待填入* |
| Interpreting I-V graphs (ohmic vs non-ohmic) | High | Medium | 📝 *待填入* |
| Explaining the effect of temperature on resistance | Medium | Medium | 📝 *待填入* |
| Describing the characteristics of LDRs and thermistors | Medium | Easy | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Define / 定义:** Give the precise meaning of a term (e.g., "Define resistance").
- **Calculate / 计算:** Use a formula to find a numerical value (e.g., "Calculate the resistance").
- **Sketch / 绘制:** Draw a graph with labeled axes, showing the general shape (e.g., "Sketch the I-V characteristic of an ohmic conductor").
- **Explain / 解释:** Give reasons for a phenomenon (e.g., "Explain why the resistance of a metal increases with temperature").

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is central to practical Paper 3 (CAIE) and Unit 2 (Edexcel). You will be expected to:
1.  **Set up circuits** to measure resistance using an ammeter and voltmeter.
2.  **Plot I-V graphs** from experimental data and determine resistance from the gradient.
3.  **Identify and reduce errors:** The ammeter should be in series, the voltmeter in parallel. Be aware of the loading effect of the voltmeter (if it has low resistance, it draws current, affecting the ammeter reading).
4.  **Investigate the effect of temperature:** Use a filament lamp and observe how its resistance changes as it heats up.
5.  **Investigate LDRs and thermistors:** Measure resistance under different light intensities (using a lamp) or temperatures (using a water bath).

**中文:**
本子知识点是实验 Paper 3 (CAIE) 和 Unit 2 (Edexcel) 的核心。你需要能够：
1.  **搭建电路**，使用电流表和电压表测量电阻。
2.  **绘制 I-V 图**，并根据实验数据从斜率确定电阻。
3.  **识别并减少误差：** 电流表应串联，电压表应并联。注意电压表的负载效应（如果其电阻较低，它会分流电流，影响电流表读数）。
4.  **研究温度的影响：** 使用白炽灯，观察其电阻随温度升高如何变化。
5.  **研究 LDR 和热敏电阻：** 在不同光照强度（使用灯）或温度（使用水浴）下测量电阻。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    subgraph "Core Concept"
        R[Resistance & the Ohm] --> Def[Definition: R = V/I]
        Def --> Unit[Unit: Ohm (Ω)]
        Unit --> Base[Base SI Units: kg m² s⁻³ A⁻²]
    end

    subgraph "Related Concepts"
        R --> Ohmic[Ohmic Conductor]
        R --> NonOhmic[Non-Ohmic Conductor]
        R --> Temp[Effect of Temperature]
        R --> LDR[Light-Dependent Resistor]
        R --> Therm[Thermistor]
    end

    subgraph "Graphical Representation"
        R --> IVGraph[I-V Characteristic Graph]
        IVGraph --> Grad[Gradient = 1/R]
        IVGraph --> Line[Straight Line = Ohmic]
        IVGraph --> Curve[Curve = Non-Ohmic]
    end

    subgraph "Prerequisites & Links"
        R --> PD[Potential Difference & EMF]
        R --> Current[Electric Current]
        R --> OhmsLaw[Ohm's Law]
        R --> Resistivity[Resistivity & Resistivity Equation]
    end

    subgraph "Applications"
        R --> Circuits[Resistors in Series & Parallel]
        R --> Power[Electrical Power]
    end
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Resistance is opposition to current flow. $R = V/I$. Unit: Ohm (Ω). |
| **Key Formula / 核心公式** | $R = \frac{V}{I}$ |
| **Key Graph / 核心图表** | **I-V Graph:** Gradient = $1/R$. Straight line through origin = ohmic conductor. |
| **Ohmic Conductor / 欧姆导体** | Constant $R$ (at constant temp). Obeys Ohm's law. E.g., metallic wire at constant temp. |
| **Non-Ohmic Conductor / 非欧姆导体** | $R$ changes with $V$ or $I$. Does not obey Ohm's law. E.g., filament lamp, diode, LDR, thermistor. |
| **Temperature Effect (Metal) / 温度效应（金属）** | As temp increases, ions vibrate more → more collisions → **resistance increases**. |
| **LDR / 光敏电阻** | Resistance **decreases** as light intensity **increases**. |
| **Thermistor / 热敏电阻** | Resistance **decreases** as temperature **increases** (for NTC type). |
| **Exam Tip / 考试提示** | Always state "at constant temperature" for Ohm's law. Gradient of I-V graph is $1/R$, not $R$. |