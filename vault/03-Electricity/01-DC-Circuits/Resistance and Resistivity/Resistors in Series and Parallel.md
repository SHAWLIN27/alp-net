---
# 1. Overview / 概述

**English:**
This sub-topic covers the rules for combining resistors in series and parallel circuits. It is a fundamental skill in circuit analysis, allowing you to calculate the total or equivalent resistance of a network. Understanding these rules is essential for predicting current, voltage, and power distribution in any electrical circuit, from simple battery-resistor setups to complex electronic devices. This knowledge directly builds on [[Potential Difference and EMF]] and is a prerequisite for understanding [[I-V Characteristics]] and [[Kirchhoff's Laws]].

**中文:**
本子知识点涵盖串联和并联电路中电阻的组合规则。这是电路分析中的一项基本技能，可用于计算网络的总电阻或等效电阻。理解这些规则对于预测任何电路（从简单的电池-电阻装置到复杂的电子设备）中的电流、电压和功率分配至关重要。该知识直接建立在[[Potential Difference and EMF]]的基础上，也是理解[[I-V Characteristics]]和[[Kirchhoff's Laws]]的先决条件。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (9.3 a-f) | Edexcel IAL (WPH11 U2: 3.9-3.12) |
|-----------|-------------|
| Derive and use the formula for the combined resistance of two or more resistors in series. | Derive and use the formula for the combined resistance of resistors in series. |
| Derive and use the formula for the combined resistance of two or more resistors in parallel. | Derive and use the formula for the combined resistance of resistors in parallel. |
| Solve problems involving series and parallel circuits. | Solve problems involving series and parallel circuits. |
| Show an understanding of the use of a potential divider circuit as a source of variable p.d. | Show an understanding of the use of a potential divider circuit as a source of variable p.d. |
| Explain the use of thermistors and light-dependent resistors (LDRs) in potential divider circuits. | Explain the use of thermistors and light-dependent resistors (LDRs) in potential divider circuits. |
| Recall and use the conditions for the maximum power transfer. | (Not explicitly stated, but implied in problem solving) |

**Examiner Expectations / 考官期望:**
- **EN:** You must be able to derive the formulas from first principles (using conservation of charge/current and energy/p.d.). You must be able to apply them to circuits with up to three resistors. You must be able to explain the function of a potential divider and how it can be used with a sensor (LDR or thermistor).
- **CN:** 你必须能够从基本原理（电荷/电流守恒和能量/电势差守恒）推导出公式。你必须能够将其应用于最多三个电阻的电路。你必须能够解释分压器的功能以及如何将其与传感器（LDR或热敏电阻）一起使用。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Series Circuit** / 串联电路 | A circuit where components are connected end-to-end, providing a single path for current flow. | 元件首尾相连，为电流提供单一路径的电路。 | Confusing series with parallel. |
| **Parallel Circuit** / 并联电路 | A circuit where components are connected across the same two points, providing multiple paths for current flow. | 元件连接在相同的两点之间，为电流提供多条路径的电路。 | Confusing parallel with series. |
| **Equivalent Resistance ($R_{eq}$)** / 等效电阻 | The single resistance that could replace a combination of resistors without changing the total current or voltage in the circuit. | 可以替代一组电阻组合而不改变电路中总电流或电压的单个电阻值。 | Thinking $R_{eq}$ is always the sum of individual resistances. |
| **Potential Divider** / 分压器 | A circuit that uses two or more resistors in series to produce a fraction of the input voltage across one of the resistors. | 使用两个或多个串联电阻，在其中一个电阻上产生输入电压的一部分的电路。 | Forgetting that the output voltage depends on the ratio of resistances. |
| **Thermistor** / 热敏电阻 | A temperature-dependent resistor; its resistance decreases as temperature increases (NTC type). | 一种温度依赖性电阻；其电阻值随温度升高而降低（NTC型）。 | Confusing its behavior with an LDR. |
| **Light-Dependent Resistor (LDR)** / 光敏电阻 | A light-dependent resistor; its resistance decreases as light intensity increases. | 一种光依赖性电阻；其电阻值随光强度增加而降低。 | Confusing its behavior with a thermistor. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Resistors in Series / 串联电阻

### Explanation / 解释
**English:** When resistors are connected in series, the same current $I$ flows through each resistor. According to [[Ohm's Law]], the potential difference (p.d.) across each resistor is $V = IR$. The total p.d. across the combination is the sum of the individual p.d.s: $V_{total} = V_1 + V_2 + V_3 + ...$. By substituting $V = IR$, we get $I R_{eq} = I R_1 + I R_2 + I R_3 + ...$. Since the current $I$ is common, it cancels out, leaving the formula for equivalent resistance in series: $$R_{eq} = R_1 + R_2 + R_3 + ...$$
**中文:** 当电阻串联时，通过每个电阻的电流 $I$ 相同。根据[[Ohm's Law]]，每个电阻两端的电势差为 $V = IR$。组合两端的总电势差是各个电势差之和：$V_{total} = V_1 + V_2 + V_3 + ...$。代入 $V = IR$，我们得到 $I R_{eq} = I R_1 + I R_2 + I R_3 + ...$。由于电流 $I$ 是公共的，可以约去，从而得到串联等效电阻的公式：$$R_{eq} = R_1 + R_2 + R_3 + ...$$

### Physical Meaning / 物理意义
**English:** Adding more resistors in series increases the total opposition to current flow. The equivalent resistance is always greater than the largest individual resistance in the chain.
**中文:** 串联更多电阻会增加对电流的总阻碍。等效电阻总是大于链中最大的单个电阻。

### Common Misconceptions / 常见误区
- **EN:** Thinking the current is different in different resistors. (It's the same!)
- **CN:** 认为不同电阻中的电流不同。（实际上是一样的！）
- **EN:** Forgetting that the total p.d. is shared between the resistors.
- **CN:** 忘记总电势差是在电阻之间分配的。

### Exam Tips / 考试提示
- **EN:** Use the formula $R_{eq} = R_1 + R_2 + ...$ directly. For two resistors, it's simply the sum.
- **CN:** 直接使用公式 $R_{eq} = R_1 + R_2 + ...$。对于两个电阻，就是简单的求和。

> 📷 **IMAGE PROMPT — SR01: Series Resistor Circuit**
> A simple circuit diagram showing a battery connected to three resistors (R1, R2, R3) in a single loop. Arrows indicate the same current 'I' flowing through each resistor. Labels show the voltage drops V1, V2, and V3 across each resistor, summing to the total battery voltage V_total. Clean, educational style, suitable for an A-Level physics textbook.

## 4.2 Resistors in Parallel / 并联电阻

### Explanation / 解释
**English:** When resistors are connected in parallel, the potential difference (p.d.) across each resistor is the same and equal to the total p.d. across the combination. The total current $I_{total}$ entering the junction splits, so $I_{total} = I_1 + I_2 + I_3 + ...$. Using [[Ohm's Law]], $I = V/R$, we get $\frac{V}{R_{eq}} = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} + ...$. Since the p.d. $V$ is common, it cancels out, leaving the formula for equivalent resistance in parallel: $$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ...$$
**中文:** 当电阻并联时，每个电阻两端的电势差相同，并且等于组合两端的总电势差。进入节点的总电流 $I_{total}$ 会分流，因此 $I_{total} = I_1 + I_2 + I_3 + ...$。使用[[Ohm's Law]]，$I = V/R$，我们得到 $\frac{V}{R_{eq}} = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} + ...$。由于电势差 $V$ 是公共的，可以约去，从而得到并联等效电阻的公式：$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ...$$

### Physical Meaning / 物理意义
**English:** Adding more resistors in parallel provides more paths for current to flow, thus *reducing* the total opposition to current. The equivalent resistance is always less than the smallest individual resistance in the network.
**中文:** 并联更多电阻为电流提供了更多路径，从而*减少*了对电流的总阻碍。等效电阻总是小于网络中最小的单个电阻。

### Common Misconceptions / 常见误区
- **EN:** Forgetting to take the reciprocal of the final answer. The formula gives $1/R_{eq}$, so you must calculate $R_{eq} = 1 / (1/R_1 + 1/R_2 + ...)$.
- **CN:** 忘记对最终答案取倒数。公式给出的是 $1/R_{eq}$，所以你必须计算 $R_{eq} = 1 / (1/R_1 + 1/R_2 + ...)$。
- **EN:** Thinking the p.d. is different across different parallel branches. (It's the same!)
- **CN:** 认为不同并联支路两端的电势差不同。（实际上是一样的！）

### Exam Tips / 考试提示
- **EN:** For **two resistors only**, use the product-over-sum formula: $R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$. This is faster and avoids reciprocal errors.
- **CN:** 对于**仅有两个电阻**的情况，使用积和公式：$R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$。这更快，并且可以避免倒数错误。
- **EN:** If all $n$ resistors in parallel are identical ($R$), then $R_{eq} = R/n$.
- **CN:** 如果并联的所有 $n$ 个电阻都相同（$R$），那么 $R_{eq} = R/n$。

> 📷 **IMAGE PROMPT — PR01: Parallel Resistor Circuit**
> A circuit diagram showing a battery connected to three resistors (R1, R2, R3) in parallel branches. Arrows show the total current 'I_total' splitting into 'I1', 'I2', and 'I3' through each branch. Labels show the same voltage 'V' across each resistor and the battery. Clean, educational style, suitable for an A-Level physics textbook.

## 4.3 The Potential Divider / 分压器

### Explanation / 解释
**English:** A potential divider is a simple circuit that uses two resistors in series to "divide" the input voltage $V_{in}$ into a smaller output voltage $V_{out}$. The output voltage is taken across one of the resistors (e.g., $R_2$). Since the current $I$ is the same through both resistors, $V_{out} = I R_2$. The total current is $I = V_{in} / (R_1 + R_2)$. Substituting gives the potential divider equation: $$V_{out} = \frac{R_2}{R_1 + R_2} \times V_{in}$$
**中文:** 分压器是一个简单的电路，它使用两个串联电阻将输入电压 $V_{in}$ "分"成一个较小的输出电压 $V_{out}$。输出电压取自其中一个电阻（例如 $R_2$）两端。由于通过两个电阻的电流 $I$ 相同，$V_{out} = I R_2$。总电流为 $I = V_{in} / (R_1 + R_2)$。代入得到分压器方程：$$V_{out} = \frac{R_2}{R_1 + R_2} \times V_{in}$$

### Physical Meaning / 物理意义
**English:** The output voltage is a fraction of the input voltage, determined by the ratio of the two resistances. By changing one of the resistors (e.g., with a thermistor or LDR), you can create a sensor circuit that produces a varying output voltage in response to a physical change (temperature or light).
**中文:** 输出电压是输入电压的一部分，由两个电阻的比值决定。通过改变其中一个电阻（例如使用热敏电阻或光敏电阻），您可以创建一个传感器电路，该电路会根据物理变化（温度或光）产生变化的输出电压。

### Common Misconceptions / 常见误区
- **EN:** Using the wrong resistor in the numerator. $V_{out}$ is across the resistor in the denominator of the ratio.
- **CN:** 在分子中使用错误的电阻。$V_{out}$ 取自比值中分母位置的电阻两端。
- **EN:** Forgetting that the circuit is a series circuit, so the same current flows through both resistors.
- **CN:** 忘记该电路是串联电路，因此相同的电流流过两个电阻。

### Exam Tips / 考试提示
- **EN:** For sensor circuits (LDR/Thermistor), always think about how the sensor's resistance changes (e.g., light increases → LDR resistance decreases → $V_{out}$ changes).
- **CN:** 对于传感器电路（LDR/热敏电阻），始终考虑传感器的电阻如何变化（例如，光强增加 → LDR电阻减小 → $V_{out}$ 变化）。

> 📋 **Edexcel Only:** The potential divider is a key application in the Edexcel syllabus, often tested with LDRs and thermistors in "light/dark" and "temperature" sensing circuits.

> 📷 **IMAGE PROMPT — PD01: Potential Divider Circuit**
> A circuit diagram showing a 9V battery connected to two resistors R1 and R2 in series. The output voltage V_out is measured across R2. An arrow points to V_out with the label "V_out = (R2/(R1+R2)) * V_in". Clean, educational style.

## 4.4 Sensor Circuits (LDR & Thermistor) / 传感器电路（LDR 和 热敏电阻）

### Explanation / 解释
**English:** A potential divider can be turned into a sensor circuit by replacing one of the fixed resistors with a sensor (LDR or thermistor).
- **Light Sensor (LDR):** Replace $R_2$ with an LDR. As light intensity increases, LDR resistance decreases. Therefore, $V_{out}$ (across the LDR) decreases. This can be used to switch on a light when it gets dark.
- **Temperature Sensor (Thermistor):** Replace $R_2$ with a thermistor (NTC type). As temperature increases, thermistor resistance decreases. Therefore, $V_{out}$ (across the thermistor) decreases. This can be used to switch on a fan when it gets hot.
**中文:** 通过将其中一个固定电阻替换为传感器（LDR或热敏电阻），可以将分压器转变为传感器电路。
- **光传感器 (LDR):** 将 $R_2$ 替换为 LDR。随着光强度增加，LDR电阻减小。因此，$V_{out}$（LDR两端）减小。这可用于在天黑时打开灯。
- **温度传感器 (热敏电阻):** 将 $R_2$ 替换为热敏电阻（NTC型）。随着温度升高，热敏电阻电阻减小。因此，$V_{out}$（热敏电阻两端）减小。这可用于在天热时打开风扇。

### Common Misconceptions / 常见误区
- **EN:** Confusing the behavior of LDR and thermistor. Remember: LDR = Light, Thermistor = Temperature.
- **CN:** 混淆LDR和热敏电阻的行为。记住：LDR = 光，热敏电阻 = 温度。
- **EN:** Forgetting that the output voltage is taken across the sensor. If the sensor is in the top position ($R_1$), the relationship is inverted.
- **CN:** 忘记输出电压取自传感器两端。如果传感器在顶部位置（$R_1$），则关系是相反的。

### Exam Tips / 考试提示
- **EN:** Always state the direction of change: "As light/temperature increases, resistance decreases, so $V_{out}$ decreases."
- **CN:** 始终说明变化方向：“随着光/温度增加，电阻减小，因此 $V_{out}$ 减小。”

> 📷 **IMAGE PROMPT — SC01: LDR Potential Divider Circuit**
> A circuit diagram showing a 9V battery connected to a fixed resistor R1 and an LDR in series. The output voltage V_out is measured across the LDR. An arrow points to the LDR with the label "LDR (Light Dependent Resistor)". Clean, educational style.

---

# 5. Essential Equations / 核心公式

## 5.1 Series Resistance / 串联电阻

$$ R_{eq} = R_1 + R_2 + R_3 + ... $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $R_{eq}$ | Equivalent total resistance | 等效总电阻 | $\Omega$ (Ohm) |
| $R_1, R_2, ...$ | Individual resistances | 各个电阻 | $\Omega$ (Ohm) |

**Derivation / 推导:** From conservation of energy ($V_{total} = V_1 + V_2 + ...$) and [[Ohm's Law]] ($V=IR$).
**Conditions / 适用条件:** Components are connected end-to-end in a single loop.
**Limitations / 局限性:** Only valid for purely resistive circuits.

## 5.2 Parallel Resistance / 并联电阻

$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ... $$

**For two resistors only:** $$ R_{eq} = \frac{R_1 R_2}{R_1 + R_2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $R_{eq}$ | Equivalent total resistance | 等效总电阻 | $\Omega$ (Ohm) |
| $R_1, R_2, ...$ | Individual resistances | 各个电阻 | $\Omega$ (Ohm) |

**Derivation / 推导:** From conservation of charge ($I_{total} = I_1 + I_2 + ...$) and [[Ohm's Law]] ($I=V/R$).
**Conditions / 适用条件:** Components are connected across the same two points.
**Limitations / 局限性:** Only valid for purely resistive circuits.

## 5.3 Potential Divider / 分压器

$$ V_{out} = \frac{R_2}{R_1 + R_2} \times V_{in} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $V_{out}$ | Output voltage (across $R_2$) | 输出电压（$R_2$两端） | V (Volt) |
| $V_{in}$ | Input voltage (across the whole divider) | 输入电压（整个分压器两端） | V (Volt) |
| $R_1, R_2$ | The two series resistors | 两个串联电阻 | $\Omega$ (Ohm) |

**Derivation / 推导:** From series current $I = V_{in}/(R_1+R_2)$ and $V_{out} = I R_2$.
**Conditions / 适用条件:** The output is unloaded (no current is drawn from $V_{out}$).
**Limitations / 局限性:** If a load is connected to $V_{out}$, the equation changes.

> 📷 **IMAGE PROMPT — EQ01: Formula Summary Card**
> A clean, visually appealing summary card showing the three key formulas: Series Resistance (R_eq = R1 + R2 + ...), Parallel Resistance (1/R_eq = 1/R1 + 1/R2 + ...), and Potential Divider (V_out = (R2/(R1+R2)) * V_in). Each formula is in a separate box with a small circuit diagram next to it. Suitable for a revision poster.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Equivalent Resistance vs. Number of Resistors / 等效电阻 vs. 电阻数量

### Axes / 坐标轴
- **X-axis:** Number of resistors ($n$)
- **Y-axis:** Equivalent resistance ($R_{eq}$)
- **X轴:** 电阻数量 ($n$)
- **Y轴:** 等效电阻 ($R_{eq}$)

### Shape / 形状
- **Series:** A straight line with a positive slope ($R_{eq} \propto n$).
- **Parallel:** A curve that approaches zero as $n$ increases ($R_{eq} \propto 1/n$).
- **串联:** 一条斜率为正的直线 ($R_{eq} \propto n$)。
- **并联:** 一条随着 $n$ 增加而趋近于零的曲线 ($R_{eq} \propto 1/n$)。

### Gradient Meaning / 斜率含义
- **Series:** The gradient is the value of each individual resistor (if all are equal).
- **Parallel:** The gradient is negative and decreasing in magnitude.
- **串联:** 斜率为每个单个电阻的值（如果所有电阻都相等）。
- **并联:** 斜率为负，且绝对值递减。

### Area Meaning / 面积含义
- **N/A** for this graph.

### Exam Interpretation / 考试解读
- **EN:** Be able to sketch these graphs. Understand that adding resistors in series always increases $R_{eq}$, while adding them in parallel always decreases $R_{eq}$.
- **CN:** 能够画出这些草图。理解串联电阻总是增加 $R_{eq}$，而并联电阻总是减小 $R_{eq}$。

> 📷 **IMAGE PROMPT — GR01: R_eq vs n Graph**
> A graph with two curves. One is a straight line going up (labeled "Series"), the other is a curve going down and approaching zero (labeled "Parallel"). The x-axis is labeled "Number of Resistors (n)" and the y-axis is labeled "Equivalent Resistance (R_eq)". Clean, educational style.

---

# 7. Required Diagrams / 必备图表

## 7.1 Series and Parallel Circuit Diagrams / 串联和并联电路图

### Description / 描述
**English:** Standard circuit diagrams showing three resistors in series (a single loop) and three resistors in parallel (three branches connected to the same two points). Include a battery and an ammeter/voltmeter to show measurements.
**中文:** 标准电路图，显示三个电阻串联（单个回路）和三个电阻并联（三个支路连接到相同的两点）。包括电池和电流表/电压表以显示测量值。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DG01: Series vs Parallel Circuits**
> Two side-by-side circuit diagrams. Left: A 9V battery connected to three resistors (R1, R2, R3) in a single loop. An ammeter is in series, and a voltmeter is across R2. Right: A 9V battery connected to three resistors (R1, R2, R3) in parallel. An ammeter is in the main line, and a voltmeter is across one branch. Clean, educational style, suitable for an A-Level physics textbook.

### Labels Required / 需要标注
- **EN:** Battery, Resistor (R1, R2, R3), Ammeter (A), Voltmeter (V), Current (I), Voltage (V).
- **CN:** 电池、电阻（R1, R2, R3）、电流表（A）、电压表（V）、电流（I）、电压（V）。

### Exam Importance / 考试重要性
- **EN:** High. You must be able to draw and interpret these diagrams. They are the foundation of all circuit analysis.
- **CN:** 高。你必须能够绘制和解读这些图表。它们是所有电路分析的基础。

## 7.2 Potential Divider with LDR / 带LDR的分压器

### Description / 描述
**English:** A circuit diagram showing a potential divider where one of the resistors is replaced by an LDR. The output voltage is taken across the LDR.
**中文:** 一个电路图，显示一个分压器，其中一个电阻被LDR取代。输出电压取自LDR两端。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DG02: Potential Divider with LDR**
> A circuit diagram showing a 9V battery connected to a fixed resistor R1 and an LDR in series. The output voltage V_out is measured across the LDR. An arrow points to the LDR with the label "LDR (Light Dependent Resistor)". A light bulb icon is shown near the LDR to indicate light intensity. Clean, educational style.

### Labels Required / 需要标注
- **EN:** Battery, Fixed Resistor (R1), LDR, Output Voltage ($V_{out}$), Input Voltage ($V_{in}$).
- **CN:** 电池、固定电阻（R1）、LDR、输出电压（$V_{out}$）、输入电压（$V_{in}$）。

### Exam Importance / 考试重要性
- **EN:** High. This is a common exam question. You must be able to explain how $V_{out}$ changes with light intensity.
- **CN:** 高。这是一个常见的考试题目。你必须能够解释 $V_{out}$ 如何随光强度变化。

---

# 8. Worked Examples / 典型例题

## Example 1: Series and Parallel Combination / 串联和并联组合

### Question / 题目
**English:** Three resistors, $R_1 = 4 \Omega$, $R_2 = 6 \Omega$, and $R_3 = 12 \Omega$, are connected to a 12V battery as shown in the diagram. $R_2$ and $R_3$ are in parallel, and this combination is in series with $R_1$. Calculate:
a) The total equivalent resistance of the circuit.
b) The total current supplied by the battery.
c) The current through $R_2$.
**中文:** 三个电阻 $R_1 = 4 \Omega$，$R_2 = 6 \Omega$ 和 $R_3 = 12 \Omega$ 按图示连接到12V电池。$R_2$ 和 $R_3$ 并联，该组合与 $R_1$ 串联。计算：
a) 电路的总等效电阻。
b) 电池提供的总电流。
c) 通过 $R_2$ 的电流。

### Solution / 解答
**Step 1: Calculate the parallel combination ($R_{23}$).**
$$ \frac{1}{R_{23}} = \frac{1}{R_2} + \frac{1}{R_3} = \frac{1}{6} + \frac{1}{12} = \frac{2}{12} + \frac{1}{12} = \frac{3}{12} = \frac{1}{4} $$
$$ R_{23} = 4 \Omega $$

**Step 2: Calculate the total equivalent resistance ($R_{eq}$).**
$R_{23}$ is in series with $R_1$.
$$ R_{eq} = R_1 + R_{23} = 4 + 4 = 8 \Omega $$

**Step 3: Calculate the total current ($I_{total}$).**
Using [[Ohm's Law]]:
$$ I_{total} = \frac{V}{R_{eq}} = \frac{12}{8} = 1.5 A $$

**Step 4: Calculate the voltage across the parallel combination ($V_{23}$).**
The current through $R_1$ is $1.5 A$. The voltage across $R_1$ is $V_1 = I_{total} \times R_1 = 1.5 \times 4 = 6 V$.
Since the total voltage is 12V, the voltage across the parallel combination is:
$$ V_{23} = V_{total} - V_1 = 12 - 6 = 6 V $$

**Step 5: Calculate the current through $R_2$.**
Since $R_2$ and $R_3$ are in parallel, the voltage across each is $V_{23} = 6 V$.
$$ I_2 = \frac{V_{23}}{R_2} = \frac{6}{6} = 1 A $$

### Final Answer / 最终答案
**Answer:** a) $8 \Omega$ b) $1.5 A$ c) $1 A$ | **答案：** a) $8 \Omega$ b) $1.5 A$ c) $1 A$

### Quick Tip / 提示
- **EN:** Always simplify the circuit step-by-step, starting with the innermost parallel or series combinations.
- **CN:** 始终逐步简化电路，从最内层的并联或串联组合开始。

## Example 2: Potential Divider with Thermistor / 带热敏电阻的分压器

### Question / 题目
**English:** A potential divider circuit consists of a fixed resistor $R_1 = 10 k\Omega$ and a thermistor $R_2$ connected in series to a 5V supply. The output voltage $V_{out}$ is taken across the thermistor. At room temperature, the thermistor has a resistance of $5 k\Omega$.
a) Calculate $V_{out}$ at room temperature.
b) The temperature increases, and the thermistor's resistance drops to $2 k\Omega$. Calculate the new $V_{out}$.
c) State and explain how $V_{out}$ changes as temperature increases.
**中文:** 一个分压器电路由一个固定电阻 $R_1 = 10 k\Omega$ 和一个热敏电阻 $R_2$ 串联连接到5V电源组成。输出电压 $V_{out}$ 取自热敏电阻两端。在室温下，热敏电阻的电阻为 $5 k\Omega$。
a) 计算室温下的 $V_{out}$。
b) 温度升高，热敏电阻的电阻降至 $2 k\Omega$。计算新的 $V_{out}$。
c) 说明并解释 $V_{out}$ 如何随温度升高而变化。

### Solution / 解答
**Step 1: Calculate $V_{out}$ at room temperature.**
Using the potential divider equation:
$$ V_{out} = \frac{R_2}{R_1 + R_2} \times V_{in} = \frac{5}{10 + 5} \times 5 = \frac{5}{15} \times 5 = \frac{25}{15} = 1.67 V $$

**Step 2: Calculate $V_{out}$ at higher temperature.**
$$ V_{out} = \frac{R_2}{R_1 + R_2} \times V_{in} = \frac{2}{10 + 2} \times 5 = \frac{2}{12} \times 5 = \frac{10}{12} = 0.83 V $$

**Step 3: Explain the change.**
As temperature increases, the thermistor's resistance decreases. Since $V_{out}$ is proportional to $R_2$ (the thermistor's resistance), $V_{out}$ also decreases.

### Final Answer / 最终答案
**Answer:** a) $1.67 V$ b) $0.83 V$ c) $V_{out}$ decreases because the thermistor's resistance decreases. | **答案：** a) $1.67 V$ b) $0.83 V$ c) $V_{out}$ 减小，因为热敏电阻的电阻减小。

### Quick Tip / 提示
- **EN:** For sensor circuits, always identify which resistor is the sensor and whether $V_{out}$ is taken across it.
- **CN:** 对于传感器电路，始终识别哪个电阻是传感器，以及 $V_{out}$ 是否取自其两端。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate equivalent resistance of a series/parallel network | High | Easy | 📝 *待填入* |
| Calculate current, voltage, or power in a series/parallel circuit | High | Medium | 📝 *待填入* |
| Explain the behavior of a potential divider with an LDR or thermistor | High | Medium | 📝 *待填入* |
| Derive the formula for series or parallel resistance | Low | Medium | 📝 *待填入* |
| Design a potential divider circuit for a specific output voltage | Medium | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Calculate, Determine, Show, Explain, State, Derive, Sketch.
- **CN:** 计算、确定、展示、解释、陈述、推导、画出草图。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
- **Measurements:** Using an ohmmeter to measure the resistance of individual resistors and combinations. Using a voltmeter and ammeter to verify the formulas.
- **Uncertainties:** Calculating the uncertainty in $R_{eq}$ from the uncertainties in individual resistor values (using error propagation rules).
- **Graph Plotting:** Plotting a graph of $V_{out}$ vs. temperature (for a thermistor) or light intensity (for an LDR) to characterize a sensor circuit.
- **Experimental Design:** Designing an experiment to determine the resistance of an unknown resistor by placing it in a series or parallel circuit with a known resistor.

**中文:**
- **测量:** 使用欧姆表测量单个电阻和组合的电阻。使用电压表和电流表验证公式。
- **不确定度:** 根据单个电阻值的不确定度计算 $R_{eq}$ 的不确定度（使用误差传播规则）。
- **图表绘制:** 绘制 $V_{out}$ 与温度（对于热敏电阻）或光强度（对于LDR）的关系图，以表征传感器电路。
- **实验设计:** 设计一个实验，通过将未知电阻与已知电阻串联或并联来测定其电阻值。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Concept
    A[Resistors in Series and Parallel] --> B[Series Circuits]
    A --> C[Parallel Circuits]
    A --> D[Potential Divider]

    %% Series
    B --> B1[Same Current]
    B --> B2[Voltage Divides]
    B --> B3[Req = R1 + R2 + ...]

    %% Parallel
    C --> C1[Same Voltage]
    C --> C2[Current Divides]
    C --> C3[1/Req = 1/R1 + 1/R2 + ...]

    %% Potential Divider
    D --> D1[Vout = (R2/(R1+R2)) * Vin]
    D --> D2[Sensor Circuits]
    D2 --> D3[LDR]
    D2 --> D4[Thermistor]

    %% Connections to other topics
    A --> E[Ohm's Law]
    A --> F[Kirchhoff's Laws]
    A --> G[I-V Characteristics]
    A --> H[Resistance and the Ohm]
    A --> I[Potential Difference and EMF]

    %% Styling
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#cfc,stroke:#333,stroke-width:2px
    style F fill:#cfc,stroke:#333,stroke-width:2px
    style G fill:#cfc,stroke:#333,stroke-width:2px
    style H fill:#cfc,stroke:#333,stroke-width:2px
    style I fill:#cfc,stroke:#333,stroke-width:2px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Series: single path, same current. Parallel: multiple paths, same voltage. |
| **Key Formula / 核心公式** | Series: $R_{eq} = R_1 + R_2 + ...$ <br> Parallel: $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + ...$ <br> Two in parallel: $R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$ <br> Potential Divider: $V_{out} = \frac{R_2}{R_1 + R_2} \times V_{in}$ |
| **Key Graph / 核心图表** | $R_{eq}$ vs. $n$: Series is linear, Parallel is a decreasing curve. |
| **Exam Tip / 考试提示** | Always simplify circuits step-by-step. For potential dividers, identify the sensor and where $V_{out}$ is taken. Use the product-over-sum formula for two parallel resistors to save time. |