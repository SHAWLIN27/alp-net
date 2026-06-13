---
tags:
  - A-Level
  - Physics
  - Capacitance
  - LeafNode
  - Bilingual
  - 9702
  - WPH14
---

# 1. Overview / 概述

**English:**
This leaf node defines the fundamental concept of **capacitance**. Capacitance is the ability of a conductor or a system of conductors (like a capacitor) to store electric charge. It is a measure of how much charge a device can hold per unit of potential difference applied across it. This definition is the cornerstone for understanding all other topics within [[Capacitance and Capacitors]], including how capacitors are constructed ([[Parallel Plate Capacitor]]), how materials affect their storage ([[Dielectrics and Permittivity]]), and how they are combined in circuits ([[Capacitors in Series and Parallel]]). A strong grasp of [[Potential Difference and EMF]] is a prerequisite, as capacitance directly links charge and voltage.

**中文:**
本子知识点定义了**电容**的基本概念。电容是导体或导体系统（如电容器）储存电荷的能力。它是衡量一个器件在施加单位电势差时能储存多少电荷的度量。这个定义是理解[[Capacitance and Capacitors]]中所有其他主题的基石，包括电容器的构造（[[Parallel Plate Capacitor]]）、材料如何影响其储存能力（[[Dielectrics and Permittivity]]），以及它们在电路中的组合方式（[[Capacitors in Series and Parallel]]）。牢固掌握[[Potential Difference and EMF]]是先决条件，因为电容直接关联了电荷和电压。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (19.1) | Edexcel IAL (WPH14 U4: 4.1-4.5) |
|-----------|-------------|
| (a) Define capacitance as $C = Q/V$. | 4.1 Define capacitance. |
| (b) Use the formula $C = Q/V$. | 4.2 Use the formula $C = Q/V$. |
| (c) Recall and use the unit of capacitance: farad (F). | 4.3 Recall the unit of capacitance: farad (F). |
| (d) Understand that the farad is a large unit and use sub-units (µF, nF, pF). | 4.4 Understand the farad as a large unit and use sub-units. |
| | 4.5 Understand that the charge stored is proportional to the p.d. for a given capacitor. |

**Examiner Expectations / 考官期望:**
- **EN:** You must be able to define capacitance from first principles and apply the formula $C = Q/V$ to simple calculations. You should be comfortable converting between farads (F), microfarads (µF), nanofarads (nF), and picofarads (pF). The key is to understand that $Q \propto V$ for a given capacitor, and $C$ is the constant of proportionality.
- **CN:** 你必须能够从基本原理定义电容，并应用公式 $C = Q/V$ 进行简单计算。你应该能够熟练地在法拉 (F)、微法 (µF)、纳法 (nF) 和皮法 (pF) 之间进行单位换算。关键在于理解对于给定的电容器，$Q \propto V$，而 $C$ 是比例常数。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Capacitance** / 电容 | The charge stored per unit potential difference across the capacitor. | 电容器储存的电荷量与其两端电势差之比。 | **Mistake:** Confusing capacitance with charge. Capacitance is a constant property of the device, not the amount of charge on it. |
| **Farad (F)** / 法拉 | The unit of capacitance. One farad is one coulomb per volt (1 F = 1 C V⁻¹). | 电容的单位。1法拉等于1库仑每伏特 (1 F = 1 C V⁻¹)。 | **Mistake:** Thinking 1 F is a small unit. It is a very large unit; most practical capacitors are in µF, nF, or pF. |
| **Charge (Q)** / 电荷 | The amount of electric charge stored on one plate of the capacitor. | 储存在电容器一个极板上的电荷量。 | **Mistake:** Forgetting that the net charge on a capacitor is zero. The charge stored, $Q$, refers to the magnitude of charge on one plate. |
| **Potential Difference (V)** / 电势差 | The voltage across the terminals of the capacitor. | 电容器两端的电压。 | **Mistake:** Using the EMF of the battery instead of the p.d. across the capacitor, which may be different during charging/discharging. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Definition of Capacitance / 电容的定义

### Explanation / 解释
**English:**
Capacitance ($C$) is defined by the equation $C = \frac{Q}{V}$. This means that for a given capacitor, the amount of charge ($Q$) it can store is directly proportional to the potential difference ($V$) applied across its plates. The constant of proportionality is the capacitance. A capacitor with a larger capacitance can store more charge for the same voltage. This is analogous to the size of a water tank: a larger tank (higher $C$) can hold more water (more $Q$) at the same water pressure ($V$). This concept is built upon the idea of [[Potential Difference and EMF]].

**中文:**
电容 ($C$) 由公式 $C = \frac{Q}{V}$ 定义。这意味着对于一个给定的电容器，它能储存的电荷量 ($Q$) 与其两极板间施加的电势差 ($V$) 成正比。这个比例常数就是电容。电容越大的电容器，在相同电压下能储存更多的电荷。这类似于水箱的大小：更大的水箱（更高的 $C$）在相同水压（$V$）下能容纳更多的水（更多的 $Q$）。这个概念建立在[[Potential Difference and EMF]]的基础上。

### Physical Meaning / 物理意义
**English:**
Physically, capacitance is a measure of a capacitor's ability to store electrical energy in an electric field. A higher capacitance means the device can create a stronger electric field for a given voltage, or store more charge for the same field strength. It is a geometric and material property of the capacitor, not dependent on $Q$ or $V$.

**中文:**
从物理意义上讲，电容是衡量电容器在电场中储存电能能力的指标。更高的电容意味着该器件在给定电压下能产生更强的电场，或者在相同场强下储存更多的电荷。它是电容器的几何和材料属性，不依赖于 $Q$ 或 $V$。

### Common Misconceptions / 常见误区
- **EN:** "Capacitance is the charge stored." (Incorrect. Capacitance is the *ratio* of charge to voltage.)
- **CN:** "电容就是储存的电荷。" (错误。电容是电荷与电压的*比值*。)
- **EN:** "If I double the voltage, the capacitance doubles." (Incorrect. For a given capacitor, $C$ is constant. Doubling $V$ doubles $Q$, but $C$ remains the same.)
- **CN:** "如果我把电压加倍，电容也会加倍。" (错误。对于给定的电容器，$C$ 是常数。电压加倍会使 $Q$ 加倍，但 $C$ 保持不变。)

### Exam Tips / 考试提示
- **EN:** Always define capacitance using the formula $C = Q/V$. Be prepared to rearrange it to find $Q$ or $V$.
- **CN:** 始终使用公式 $C = Q/V$ 来定义电容。准备好重新排列公式以求出 $Q$ 或 $V$。

> 📷 **IMAGE PROMPT — DEF-01: Water Tank Analogy for Capacitance**
> A side-by-side comparison diagram. On the left, a tall, narrow water tank labeled "Small Capacitance (C)". A water level is marked, and the volume of water is labeled "Charge (Q)". The height of the water column is labeled "Potential (V)". On the right, a short, wide water tank labeled "Large Capacitance (C)". The same water level height (same V) is shown, but the volume of water (Q) is much larger. Arrows indicate that for the same V, a larger C stores more Q.

---

# 5. Essential Equations / 核心公式

## 5.1 The Defining Equation / 定义方程

$$ C = \frac{Q}{V} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $C$ | Capacitance | 电容 | Farad (F) |
| $Q$ | Charge stored on one plate | 一个极板上储存的电荷 | Coulomb (C) |
| $V$ | Potential difference across plates | 两极板间的电势差 | Volt (V) |

**Derivation / 推导:**
This is an empirical definition derived from the observation that for a given capacitor, the charge stored is directly proportional to the applied voltage ($Q \propto V$). The constant of proportionality is defined as the capacitance.

**Conditions / 适用条件:**
- **EN:** This equation applies to any capacitor, regardless of its geometry or dielectric material, as long as the capacitor is not operating beyond its voltage rating (dielectric breakdown).
- **CN:** 该方程适用于任何电容器，无论其几何形状或介电材料如何，只要电容器不在其额定电压（介电击穿）之外工作。

**Limitations / 局限性:**
- **EN:** The equation defines an ideal, linear capacitor. In reality, capacitance can be slightly voltage-dependent, especially for certain types of electrolytic capacitors.
- **CN:** 该方程定义了一个理想的线性电容器。实际上，电容可能会有轻微的电压依赖性，特别是对于某些类型的电解电容器。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Charge vs. Potential Difference (Q-V) Graph / 电荷-电势差 (Q-V) 图

### Axes / 坐标轴
- **X-axis:** Potential Difference, $V$ / V (电势差, $V$ / 伏特)
- **Y-axis:** Charge, $Q$ / C (电荷, $Q$ / 库仑)

### Shape / 形状
- **EN:** A straight line passing through the origin.
- **CN:** 一条通过原点的直线。

### Gradient Meaning / 斜率含义
- **EN:** The gradient of the $Q$-$V$ graph is equal to the capacitance, $C$.
- **CN:** $Q$-$V$ 图的斜率等于电容 $C$。

### Area Meaning / 面积含义
- **EN:** The area under the $Q$-$V$ graph represents the energy stored in the capacitor ($E = \frac{1}{2} QV$). This is covered in [[Energy Stored in a Capacitor]].
- **CN:** $Q$-$V$ 图下的面积代表电容器中储存的能量 ($E = \frac{1}{2} QV$)。这在[[Energy Stored in a Capacitor]]中介绍。

### Exam Interpretation / 考试解读
- **EN:** A steeper line means a larger capacitance. A shallower line means a smaller capacitance. The graph is a direct visual representation of the definition $C = Q/V$.
- **CN:** 更陡的线意味着更大的电容。更平的线意味着更小的电容。该图是定义 $C = Q/V$ 的直接视觉表示。

```mermaid
graph TD
    subgraph Q-V Graph
        A[Start: Origin (0,0)] --> B[Point (V, Q)];
    end
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
```

> 📷 **IMAGE PROMPT — GRAPH-01: Q-V Graph for Capacitors**
> A standard Cartesian graph. The x-axis is labeled "V / V" and the y-axis is labeled "Q / C". Two straight lines are drawn from the origin. One line is steeper and labeled "C₁ (Large Capacitance)". The other line is shallower and labeled "C₂ (Small Capacitance)". A point on the steeper line is marked, showing coordinates (V, Q). An arrow points to the gradient of the line, labeled "Gradient = C = Q/V".

---

# 7. Required Diagrams / 必备图表

## 7.1 Circuit Symbol for a Capacitor / 电容器的电路符号

### Description / 描述
- **EN:** The standard circuit symbol for a fixed-value capacitor consists of two parallel lines of equal length, representing the two plates.
- **CN:** 固定值电容器的标准电路符号由两条等长的平行线组成，代表两个极板。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-01: Capacitor Circuit Symbol**
> A simple, clean diagram showing the standard circuit symbol for a fixed capacitor. It consists of two parallel, straight, vertical lines of equal length, separated by a small gap. The lines are thick and black on a white background. A label points to the symbol and reads "Capacitor (C)".

### Labels Required / 需要标注
- **EN:** The symbol itself, often labeled with the letter 'C'.
- **CN:** 符号本身，通常标有字母 'C'。

### Exam Importance / 考试重要性
- **EN:** You must be able to recognize and draw this symbol in circuit diagrams.
- **CN:** 你必须能够在电路图中识别并画出这个符号。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Capacitance / 例题1：计算电容

### Question / 题目
**English:**
A capacitor stores a charge of 60 µC when a potential difference of 12 V is applied across its plates. Calculate the capacitance of the capacitor.

**中文:**
当一个电容器两极板间施加 12 V 的电势差时，它储存了 60 µC 的电荷。计算该电容器的电容。

### Solution / 解答
1.  **Identify knowns / 确定已知量:**
    $Q = 60 \text{ µC} = 60 \times 10^{-6} \text{ C}$
    $V = 12 \text{ V}$

2.  **Choose the correct formula / 选择正确的公式:**
    $C = \frac{Q}{V}$

3.  **Substitute and solve / 代入并求解:**
    $C = \frac{60 \times 10^{-6}}{12}$
    $C = 5 \times 10^{-6} \text{ F}$

4.  **Convert to a sensible unit / 转换为合适的单位:**
    $C = 5 \text{ µF}$

### Final Answer / 最终答案
**Answer:** 5 µF | **答案：** 5 µF

### Quick Tip / 提示
- **EN:** Always convert charge to coulombs (C) and voltage to volts (V) before calculating capacitance in farads (F).
- **CN:** 在用法拉 (F) 计算电容之前，务必将电荷转换为库仑 (C)，将电压转换为伏特 (V)。

---

## Example 2: Finding Charge from Capacitance / 例题2：从电容求电荷

### Question / 题目
**English:**
A 470 nF capacitor is connected to a 9.0 V battery. Calculate the charge stored on the capacitor.

**中文:**
一个 470 nF 的电容器连接到 9.0 V 的电池上。计算电容器上储存的电荷。

### Solution / 解答
1.  **Identify knowns / 确定已知量:**
    $C = 470 \text{ nF} = 470 \times 10^{-9} \text{ F}$
    $V = 9.0 \text{ V}$

2.  **Choose the correct formula / 选择正确的公式:**
    $Q = CV$

3.  **Substitute and solve / 代入并求解:**
    $Q = (470 \times 10^{-9}) \times 9.0$
    $Q = 4230 \times 10^{-9} \text{ C}$
    $Q = 4.23 \times 10^{-6} \text{ C}$

4.  **Convert to a sensible unit / 转换为合适的单位:**
    $Q = 4.23 \text{ µC}$

### Final Answer / 最终答案
**Answer:** 4.23 µC | **答案：** 4.23 µC

### Quick Tip / 提示
- **EN:** Be careful with powers of ten when using nano (10⁻⁹), micro (10⁻⁶), and pico (10⁻¹²) prefixes.
- **CN:** 在使用纳 (10⁻⁹)、微 (10⁻⁶) 和皮 (10⁻¹²) 前缀时，要小心十的幂次。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Direct calculation of $C$, $Q$, or $V$ using $C=Q/V$ | High | Easy | 📝 *待填入* |
| Definition of capacitance (short answer) | Medium | Easy | 📝 *待填入* |
| Interpreting a $Q$-$V$ graph to find $C$ | Medium | Medium | 📝 *待填入* |
| Unit conversion (F, µF, nF, pF) | High | Easy | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Define, Calculate, Determine, State, Show that.
- **CN:** 定义，计算，确定，陈述，证明。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is foundational for practical work on capacitors. In a typical experiment to determine the capacitance of an unknown capacitor, you would:
1.  **Measurements:** Use a coulombmeter to measure charge ($Q$) and a voltmeter to measure potential difference ($V$).
2.  **Graph Plotting:** Plot a graph of $Q$ against $V$. The gradient of the best-fit line gives the capacitance ($C$).
3.  **Uncertainties:** The uncertainty in $C$ can be found from the maximum and minimum possible gradients of the error bars on the $Q$-$V$ graph.
4.  **Experimental Design:** You must ensure the capacitor is fully charged before taking a reading and that it is not allowed to discharge through the voltmeter (using a high-impedance voltmeter or a digital multimeter).

**中文:**
本子知识点是电容器实验工作的基础。在一个典型的测定未知电容器电容的实验中，你需要：
1.  **测量：** 使用库仑计测量电荷 ($Q$)，使用电压表测量电势差 ($V$)。
2.  **绘制图表：** 绘制 $Q$ 对 $V$ 的图表。最佳拟合线的斜率即为电容 ($C$)。
3.  **不确定度：** $C$ 的不确定度可以通过 $Q$-$V$ 图上误差棒的最大和最小可能斜率来求得。
4.  **实验设计：** 你必须确保电容器在读数前已完全充电，并且不允许通过电压表放电（使用高阻抗电压表或数字万用表）。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    subgraph "Leaf Node: Definition of Capacitance"
        A[Definition of Capacitance] --> B{Formula: C = Q/V};
        B --> C[Charge (Q)];
        B --> D[Potential Difference (V)];
        A --> E[Unit: Farad (F)];
        E --> F[Sub-units: µF, nF, pF];
        A --> G[Q-V Graph];
        G --> H[Gradient = C];
        G --> I[Area = Energy Stored];
    end

    subgraph "Parent Hub"
        J[[Capacitance and Capacitors]];
    end

    subgraph "Prerequisites"
        K[[Potential Difference and EMF]];
    end

    subgraph "Sibling Sub-topics"
        L[[Parallel Plate Capacitor]];
        M[[Dielectrics and Permittivity]];
        N[[Capacitors in Series and Parallel]];
    end

    subgraph "Related Topics"
        O[[Energy Stored in a Capacitor]];
        P[[Charging and Discharging Capacitors]];
    end

    A --> J;
    A --> K;
    A --> L;
    A --> M;
    A --> N;
    I --> O;
    B --> P;
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Capacitance is the charge stored per unit potential difference. $C = Q/V$. |
| **Key Formula / 核心公式** | $C = \frac{Q}{V}$; $Q = CV$; $V = \frac{Q}{C}$ |
| **Key Graph / 核心图表** | $Q$ vs $V$ graph: A straight line through origin. Gradient = $C$. |
| **Unit / 单位** | Farad (F). 1 F = 1 C V⁻¹. Common sub-units: µF (10⁻⁶), nF (10⁻⁹), pF (10⁻¹²). |
| **Key Concept / 关键概念** | $C$ is a constant for a given capacitor. $Q \propto V$. |
| **Exam Tip / 考试提示** | Always convert to base units (C, V) before calculating $C$ in F. The gradient of a $Q$-$V$ graph is the capacitance. |