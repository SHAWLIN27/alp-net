# 1. Overview / 概述

**English:**
Dimensional Analysis is a powerful mathematical technique used to check the consistency of physical equations and derive relationships between physical quantities. This sub-topic introduces the concept of dimensions (represented by square brackets [ ]) as the fundamental building blocks of physical quantities, based on the seven [[SI Base Units and Derived Units]]. By expressing any physical quantity in terms of its base dimensions — mass [M], length [L], time [T], current [I], temperature [Θ], amount of substance [N], and luminous intensity [J] — we can verify whether an equation is dimensionally consistent (homogeneous) and even predict the form of unknown relationships. This skill is essential for [[Homogeneity of Physical Equations]] and forms the mathematical foundation for all subsequent physics problem-solving.

**中文:**
量纲分析是一种强大的数学工具，用于检查物理方程的一致性并推导物理量之间的关系。本子知识点介绍量纲的概念（用方括号 [ ] 表示），它是基于七个[[SI基本单位和导出单位]]的物理量基本构建模块。通过将任何物理量用其基本量纲表示——质量[M]、长度[L]、时间[T]、电流[I]、温度[Θ]、物质的量[N]和发光强度[J]——我们可以验证方程是否量纲一致（齐次），甚至可以预测未知关系的形式。这项技能对于[[物理方程的齐次性]]至关重要，并构成所有后续物理问题解决的数学基础。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 1.1 Understand the concept of dimensions and use dimensional analysis to check the homogeneity of physical equations | WPH11 U1: 1.1-1.6 Use dimensional analysis to verify equations and derive relationships |
| 1.2 Derive the dimensions of derived quantities from base quantities | WPH11 U1: 1.3 Determine dimensions of physical quantities |
| 1.3 Apply dimensional analysis to determine the form of an equation | WPH11 U1: 1.5 Apply dimensional analysis to derive relationships |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to write dimensions correctly using square brackets, derive dimensions of any derived quantity from its definition, check if an equation is homogeneous, and use dimensional analysis to find the form of an unknown relationship. You are NOT expected to handle dimensionless constants in dimensional analysis.
- **中文:** 你必须能够正确使用方括号书写量纲，从定义推导任何导出量的量纲，检查方程是否齐次，并使用量纲分析找出未知关系的形式。在量纲分析中不需要处理无量纲常数。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Dimension** / 量纲 | The fundamental nature of a physical quantity, expressed in terms of base quantities (M, L, T, I, Θ, N, J) using square brackets [ ] | 物理量的基本性质，用基本量（M、L、T、I、Θ、N、J）表示，使用方括号[ ] | ❌ Confusing dimensions with units (e.g., [velocity] = LT⁻¹, NOT m/s) |
| **Dimensional Analysis** / 量纲分析 | A method to check the consistency of equations and derive relationships by comparing dimensions on both sides | 通过比较方程两边的量纲来检查方程一致性和推导关系的方法 | ❌ Forgetting that dimensionless constants have no dimensions |
| **Homogeneous Equation** / 齐次方程 | An equation where every term has the same dimensions | 每一项都具有相同量纲的方程 | ❌ Assuming homogeneity guarantees correctness (it only checks consistency) |
| **Base Dimension** / 基本量纲 | One of the seven fundamental dimensions (M, L, T, I, Θ, N, J) from which all others are derived | 七个基本量纲之一（M、L、T、I、Θ、N、J），所有其他量纲由此导出 | ❌ Using units instead of dimensions |
| **Dimensionless Quantity** / 无量纲量 | A quantity with no physical dimensions, represented as [1] or dimensionless | 没有物理量纲的量，表示为[1]或无因次 | ❌ Assigning dimensions to constants like π, e, or ratios |
| **Derived Dimension** / 导出量纲 | The dimension of a quantity expressed as a combination of base dimensions | 用基本量纲组合表示的量的量纲 | ❌ Incorrectly deriving dimensions from formulas |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Concept of Dimensions / 量纲的概念

### Explanation / 解释
**English:**
Every physical quantity has a fundamental nature called its **dimension**. For example, velocity, speed, and the speed of light all have the same dimension: length per time, written as [LT⁻¹]. The dimension tells us what kind of quantity it is, regardless of the units used to measure it. The seven base dimensions correspond to the seven [[SI Base Units and Derived Units]]:

- [M] = mass (kilogram)
- [L] = length (metre)
- [T] = time (second)
- [I] = electric current (ampere)
- [Θ] = temperature (kelvin)
- [N] = amount of substance (mole)
- [J] = luminous intensity (candela)

For A-Level Physics, we primarily use [M], [L], and [T] for mechanics, and occasionally [I] for electricity.

**中文:**
每个物理量都有其基本性质，称为**量纲**。例如，速度、速率和光速都具有相同的量纲：长度除以时间，写作[LT⁻¹]。量纲告诉我们这是什么类型的量，无论使用什么单位来测量。七个基本量纲对应于七个[[SI基本单位和导出单位]]：

- [M] = 质量（千克）
- [L] = 长度（米）
- [T] = 时间（秒）
- [I] = 电流（安培）
- [Θ] = 温度（开尔文）
- [N] = 物质的量（摩尔）
- [J] = 发光强度（坎德拉）

在A-Level物理中，我们主要在力学中使用[M]、[L]和[T]，偶尔在电学中使用[I]。

### Physical Meaning / 物理意义
**English:**
Dimensions represent the "type" of physical quantity. Two quantities can only be added, subtracted, or equated if they have the same dimensions. This is the **principle of dimensional homogeneity** — the foundation of [[Homogeneity of Physical Equations]].

**中文:**
量纲代表物理量的"类型"。两个量只有在具有相同量纲时才能相加、相减或相等。这就是**量纲齐次原理**——[[物理方程的齐次性]]的基础。

### Common Misconceptions / 常见误区
- ❌ **"Dimensions are the same as units"** — No! Dimensions are abstract; units are concrete. [L] can be metres, feet, or light-years.
- ❌ **"All constants are dimensionless"** — Some constants (like G, the gravitational constant) have dimensions.
- ❌ **"If an equation is homogeneous, it must be correct"** — No! Homogeneity is necessary but not sufficient. You can have a homogeneous equation that is physically wrong.

### Exam Tips / 考试提示
- **English:** Always write dimensions in square brackets [ ]. For derived quantities, start from the defining equation.
- **中文:** 始终用方括号[ ]书写量纲。对于导出量，从定义方程开始推导。

> 📷 **IMAGE PROMPT — DA-01: Dimension Ladder**
> A visual ladder showing how base dimensions [M], [L], [T] combine to form derived dimensions like [MLT⁻²] for force, [ML²T⁻³] for power, with arrows showing the mathematical operations (multiplication, division, exponentiation) that create each derived dimension. Include a comparison with SI units on the right side.

## 4.2 Deriving Dimensions of Derived Quantities / 推导导出量的量纲

### Explanation / 解释
**English:**
To find the dimension of any derived quantity, use its defining equation. For example:

- **Velocity:** $v = \frac{\text{displacement}}{\text{time}} \Rightarrow [v] = \frac{[L]}{[T]} = [LT^{-1}]$
- **Acceleration:** $a = \frac{\text{velocity}}{\text{time}} \Rightarrow [a] = \frac{[LT^{-1}]}{[T]} = [LT^{-2}]$
- **Force:** $F = ma \Rightarrow [F] = [M][LT^{-2}] = [MLT^{-2}]$
- **Work/Energy:** $W = Fd \Rightarrow [W] = [MLT^{-2}][L] = [ML^{2}T^{-2}]$
- **Power:** $P = \frac{W}{t} \Rightarrow [P] = \frac{[ML^{2}T^{-2}]}{[T]} = [ML^{2}T^{-3}]$

**中文:**
要找到任何导出量的量纲，使用其定义方程。例如：

- **速度：** $v = \frac{\text{位移}}{\text{时间}} \Rightarrow [v] = \frac{[L]}{[T]} = [LT^{-1}]$
- **加速度：** $a = \frac{\text{速度}}{\text{时间}} \Rightarrow [a] = \frac{[LT^{-1}]}{[T]} = [LT^{-2}]$
- **力：** $F = ma \Rightarrow [F] = [M][LT^{-2}] = [MLT^{-2}]$
- **功/能量：** $W = Fd \Rightarrow [W] = [MLT^{-2}][L] = [ML^{2}T^{-2}]$
- **功率：** $P = \frac{W}{t} \Rightarrow [P] = \frac{[ML^{2}T^{-2}]}{[T]} = [ML^{2}T^{-3}]$

### Common Misconceptions / 常见误区
- ❌ Using the wrong defining equation (e.g., using $F = \frac{mv^2}{r}$ for force instead of $F = ma$)
- ❌ Forgetting that trigonometric functions, logarithms, and exponentials must have dimensionless arguments

### Exam Tips / 考试提示
- **English:** Always start from the simplest defining equation. For pressure, use $P = F/A$ not $P = \rho gh$.
- **中文:** 始终从最简单的定义方程开始。对于压强，使用$P = F/A$而不是$P = \rho gh$。

## 4.3 Checking Homogeneity of Equations / 检查方程的齐次性

### Explanation / 解释
**English:**
To check if an equation is dimensionally homogeneous:
1. Write the dimensions of every term in the equation
2. Compare the dimensions of all terms
3. If all terms have the same dimensions, the equation is homogeneous

**Example:** Check $v^2 = u^2 + 2as$
- $[v^2] = [LT^{-1}]^2 = [L^2T^{-2}]$
- $[u^2] = [LT^{-1}]^2 = [L^2T^{-2}]$
- $[2as] = [1][LT^{-2}][L] = [L^2T^{-2}]$ (the constant 2 is dimensionless)
- All terms have $[L^2T^{-2}]$ → homogeneous ✓

**中文:**
检查方程是否量纲齐次：
1. 写出方程中每一项的量纲
2. 比较所有项的量纲
3. 如果所有项具有相同的量纲，则方程是齐次的

**示例：** 检查 $v^2 = u^2 + 2as$
- $[v^2] = [LT^{-1}]^2 = [L^2T^{-2}]$
- $[u^2] = [LT^{-1}]^2 = [L^2T^{-2}]$
- $[2as] = [1][LT^{-2}][L] = [L^2T^{-2}]$（常数2是无量纲的）
- 所有项都具有 $[L^2T^{-2}]$ → 齐次 ✓

### Common Misconceptions / 常见误区
- ❌ Forgetting to square the dimensions when squaring a quantity
- ❌ Assigning dimensions to pure numbers (constants like 2, π, ½)
- ❌ Only checking two terms instead of all terms

### Exam Tips / 考试提示
- **English:** Show all working clearly. Write the dimension of each term separately before comparing.
- **中文:** 清晰展示所有步骤。在比较之前分别写出每一项的量纲。

## 4.4 Using Dimensional Analysis to Derive Relationships / 用量纲分析推导关系

### Explanation / 解释
**English:**
Dimensional analysis can predict the form of an equation when you know which quantities are involved. The method:
1. Identify the dependent variable and independent variables
2. Assume a relationship of the form: $A = k \cdot B^a \cdot C^b \cdot D^c$ (where k is dimensionless)
3. Write the dimensions of all quantities
4. Equate the exponents of each base dimension
5. Solve the simultaneous equations for a, b, c
6. Write the final relationship

**Example:** Find the period T of a simple pendulum in terms of length L and gravitational acceleration g.
- Assume: $T = k \cdot L^a \cdot g^b$
- $[T] = [T]$, $[L] = [L]$, $[g] = [LT^{-2}]$
- $[T] = [L]^a \cdot [LT^{-2}]^b = [L^{a+b}][T^{-2b}]$
- Equate: For [L]: $0 = a + b$; For [T]: $1 = -2b$
- Solve: $b = -\frac{1}{2}$, $a = \frac{1}{2}$
- Result: $T = k \cdot L^{1/2} \cdot g^{-1/2} = k\sqrt{\frac{L}{g}}$

**中文:**
当你知道涉及哪些量时，量纲分析可以预测方程的形式。方法：
1. 确定因变量和自变量
2. 假设关系形式：$A = k \cdot B^a \cdot C^b \cdot D^c$（其中k是无量纲的）
3. 写出所有量的量纲
4. 使每个基本量纲的指数相等
5. 解联立方程求a、b、c
6. 写出最终关系

**示例：** 求单摆周期T与摆长L和重力加速度g的关系。
- 假设：$T = k \cdot L^a \cdot g^b$
- $[T] = [T]$，$[L] = [L]$，$[g] = [LT^{-2}]$
- $[T] = [L]^a \cdot [LT^{-2}]^b = [L^{a+b}][T^{-2b}]$
- 相等：对于[L]：$0 = a + b$；对于[T]：$1 = -2b$
- 解：$b = -\frac{1}{2}$，$a = \frac{1}{2}$
- 结果：$T = k \cdot L^{1/2} \cdot g^{-1/2} = k\sqrt{\frac{L}{g}}$

### Common Misconceptions / 常见误区
- ❌ Including too many variables (dimensional analysis cannot determine dimensionless constants)
- ❌ Forgetting that the constant k remains unknown
- ❌ Assuming the relationship is always a product of powers

### Exam Tips / 考试提示
- **English:** Dimensional analysis cannot find the value of dimensionless constants (like k, π, 2). It only gives the functional form.
- **中文：** 量纲分析无法找到无量纲常数的值（如k、π、2）。它只给出函数形式。

---

# 5. Essential Equations / 核心公式

## 5.1 Dimension of a Derived Quantity / 导出量的量纲

$$ [Q] = [M]^a [L]^b [T]^c [I]^d [\Theta]^e [N]^f [J]^g $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| [Q] | Dimension of quantity Q | 量Q的量纲 | dimensionless |
| a, b, c, d, e, f, g | Exponents of base dimensions | 基本量纲的指数 | dimensionless |

**Conditions / 适用条件:** All physical quantities can be expressed this way.
**Limitations / 局限性:** Cannot distinguish between different quantities with same dimensions (e.g., torque and energy both have [ML²T⁻²]).

## 5.2 Principle of Dimensional Homogeneity / 量纲齐次原理

$$ [\text{Term}_1] = [\text{Term}_2] = [\text{Term}_3] = \ldots $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) |
|--------------|-------------|-------------|
| [Term_i] | Dimension of the i-th term | 第i项的量纲 |

**Conditions / 适用条件:** All terms in a valid physical equation must have identical dimensions.
**Limitations / 局限性:** Does not guarantee the equation is physically correct.

## 5.3 Dimensional Analysis for Relationship Derivation / 量纲分析推导关系

$$ A = k \cdot B^a \cdot C^b \cdot D^c \ldots $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) |
|--------------|-------------|-------------|
| A | Dependent variable | 因变量 |
| B, C, D | Independent variables | 自变量 |
| k | Dimensionless constant | 无量纲常数 |
| a, b, c | Exponents to be determined | 待确定的指数 |

**Conditions / 适用条件:** The relationship is assumed to be a product of powers.
**Limitations / 局限性:** Cannot determine the value of k; cannot handle sums of terms.

> 📷 **IMAGE PROMPT — DA-02: Dimensional Analysis Flowchart**
> A step-by-step flowchart showing the process of dimensional analysis: Start → Identify variables → Assume product form → Write dimensions → Equate exponents → Solve equations → Write relationship. Use arrows and decision diamonds. Include a worked example for pendulum period alongside.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Dimension Comparison Graph / 量纲比较图

### Axes / 坐标轴
- **English:** Not a standard graph; instead, a table comparing dimensions of different quantities
- **中文：** 不是标准图表；而是比较不同量量纲的表格

### Shape / 形状
- **English:** Tabular form showing quantities and their dimensions
- **中文：** 表格形式显示量及其量纲

### Gradient Meaning / 斜率含义
- **English:** Not applicable for dimensional analysis
- **中文：** 不适用于量纲分析

### Area Meaning / 面积含义
- **English:** Not applicable for dimensional analysis
- **中文：** 不适用于量纲分析

### Exam Interpretation / 考试解读
- **English:** You may be asked to identify which quantities have the same dimensions (e.g., work and torque both have [ML²T⁻²])
- **中文：** 你可能会被要求识别哪些量具有相同的量纲（例如，功和力矩都具有[ML²T⁻²]）

---

# 7. Required Diagrams / 必备图表

## 7.1 Dimension Derivation Tree / 量纲推导树

### Description / 描述
**English:** A tree diagram showing how derived dimensions are built from base dimensions, starting from [M], [L], [T] and branching into common derived quantities like velocity, acceleration, force, energy, power, pressure.

**中文：** 一个树状图，展示如何从基本量纲构建导出量纲，从[M]、[L]、[T]开始，分支到常见的导出量，如速度、加速度、力、能量、功率、压强。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DA-03: Dimension Derivation Tree**
> A hierarchical tree diagram with [M], [L], [T] at the top as root nodes. Branches show: [L][T]⁻¹ → velocity; [L][T]⁻² → acceleration; [M][L][T]⁻² → force; [M][L]²[T]⁻² → energy/work; [M][L]²[T]⁻³ → power; [M][L]⁻¹[T]⁻² → pressure. Use different colors for each base dimension. Include SI unit equivalents in parentheses. Clean, educational style suitable for A-Level physics.

### Labels Required / 需要标注
- **English:** Each derived quantity with its dimension in square brackets and SI unit in parentheses
- **中文：** 每个导出量及其方括号中的量纲和括号中的SI单位

### Exam Importance / 考试重要性
- **English:** High — understanding this tree helps derive dimensions quickly in exams
- **中文：** 高——理解这个树有助于在考试中快速推导量纲

## 7.2 Homogeneity Check Worked Example / 齐次性检查示例

### Description / 描述
**English:** A step-by-step visual showing how to check the homogeneity of the equation $s = ut + \frac{1}{2}at^2$, with each term's dimensions written separately and compared.

**中文：** 逐步可视化展示如何检查方程 $s = ut + \frac{1}{2}at^2$ 的齐次性，分别写出每一项的量纲并进行比较。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DA-04: Homogeneity Check Example**
> A clean, step-by-step visual showing the equation s = ut + ½at². Three boxes: Box 1 shows [s] = [L]; Box 2 shows [ut] = [L]; Box 3 shows [½at²] = [L]. Arrows point from each box to a central "All terms have [L] → Homogeneous ✓" conclusion. Use color coding: blue for displacement, green for initial velocity term, orange for acceleration term. Include the note "½ is dimensionless" in a small callout.

### Labels Required / 需要标注
- **English:** Each term's dimension, the conclusion "Homogeneous" or "Not Homogeneous"
- **中文：** 每一项的量纲，结论"齐次"或"不齐次"

### Exam Importance / 考试重要性
- **English:** Very high — this is a common exam question type
- **中文：** 非常高——这是常见的考试题型

---

# 8. Worked Examples / 典型例题

## Example 1: Checking Homogeneity / 检查齐次性

### Question / 题目
**English:**
Check whether the equation $F = \frac{mv^2}{r}$ is dimensionally homogeneous, where F is force, m is mass, v is velocity, and r is radius.

**中文：**
检查方程 $F = \frac{mv^2}{r}$ 是否量纲齐次，其中F是力，m是质量，v是速度，r是半径。

### Solution / 解答

**Step 1: Write dimensions of each quantity / 写出每个量的量纲**
- $[F] = [MLT^{-2}]$ (from $F = ma$)
- $[m] = [M]$
- $[v] = [LT^{-1}]$
- $[r] = [L]$

**Step 2: Find dimension of RHS / 求右边的量纲**
$$ \left[\frac{mv^2}{r}\right] = \frac{[M][LT^{-1}]^2}{[L]} = \frac{[M][L^2T^{-2}]}{[L]} = [MLT^{-2}] $$

**Step 3: Compare / 比较**
- LHS: $[F] = [MLT^{-2}]$
- RHS: $\left[\frac{mv^2}{r}\right] = [MLT^{-2}]$
- Both sides have the same dimensions → **Homogeneous ✓**

### Final Answer / 最终答案
**Answer:** The equation is dimensionally homogeneous. | **答案：** 该方程量纲齐次。

### Quick Tip / 提示
- **English:** Always derive the dimension of force from $F = ma$, not from the equation you are checking.
- **中文：** 始终从 $F = ma$ 推导力的量纲，而不是从你要检查的方程。

---

## Example 2: Deriving a Relationship / 推导关系

### Question / 题目
**English:**
The viscous drag force F on a sphere moving through a fluid depends on the radius r of the sphere, the speed v of the sphere, and the viscosity η of the fluid. The dimensions of viscosity are $[ML^{-1}T^{-1}]$. Use dimensional analysis to find the relationship between F, r, v, and η.

**中文：**
球体在流体中运动时受到的粘滞阻力F取决于球体的半径r、球体的速度v和流体的粘度η。粘度的量纲是 $[ML^{-1}T^{-1}]$。用量纲分析找出F、r、v和η之间的关系。

### Solution / 解答

**Step 1: Assume relationship / 假设关系**
$$ F = k \cdot r^a \cdot v^b \cdot \eta^c $$
where k is a dimensionless constant.

**Step 2: Write dimensions / 写出量纲**
- $[F] = [MLT^{-2}]$
- $[r] = [L]$
- $[v] = [LT^{-1}]$
- $[\eta] = [ML^{-1}T^{-1}]$

**Step 3: Substitute / 代入**
$$ [MLT^{-2}] = [L]^a \cdot [LT^{-1}]^b \cdot [ML^{-1}T^{-1}]^c $$
$$ [MLT^{-2}] = [M]^c \cdot [L]^{a+b-c} \cdot [T]^{-b-c} $$

**Step 4: Equate exponents / 使指数相等**
- For [M]: $1 = c$
- For [L]: $1 = a + b - c$
- For [T]: $-2 = -b - c$

**Step 5: Solve / 解**
- From [M]: $c = 1$
- From [T]: $-2 = -b - 1 \Rightarrow b = 1$
- From [L]: $1 = a + 1 - 1 \Rightarrow a = 1$

**Step 6: Write relationship / 写出关系**
$$ F = k \cdot r^1 \cdot v^1 \cdot \eta^1 = k \cdot r \cdot v \cdot \eta $$

### Final Answer / 最终答案
**Answer:** $F = k \cdot r \cdot v \cdot \eta$ (Stokes' law gives $k = 6\pi$) | **答案：** $F = k \cdot r \cdot v \cdot \eta$（斯托克斯定律给出 $k = 6\pi$）

### Quick Tip / 提示
- **English:** The dimensionless constant k cannot be found by dimensional analysis. It must be determined experimentally or from theory.
- **中文：** 无量纲常数k无法通过量纲分析找到，必须通过实验或理论确定。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Check homogeneity of given equation | ★★★★★ Very High | ★★ Easy | 📝 *待填入* |
| Derive dimensions of a quantity from its definition | ★★★★ High | ★★ Easy | 📝 *待填入* |
| Use dimensional analysis to find relationship form | ★★★ Medium | ★★★ Medium | 📝 *待填入* |
| Identify which quantities have same dimensions | ★★ Low | ★★ Easy | 📝 *待填入* |
| Explain why an equation cannot be correct | ★★ Low | ★★★ Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Show that", "Determine", "Use dimensional analysis to", "Check whether", "Verify"
- **中文：** "证明"、"确定"、"用量纲分析"、"检查是否"、"验证"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Dimensional analysis connects to practical work in several ways:

1. **Experimental Design:** Before conducting an experiment, use dimensional analysis to predict the relationship between variables. For example, in the pendulum experiment, dimensional analysis predicts $T \propto \sqrt{L/g}$, guiding your choice of variables to measure.

2. **Graph Plotting:** Dimensional analysis helps determine what to plot on each axis. If you expect $T \propto \sqrt{L}$, plot $T$ against $\sqrt{L}$ to get a straight line. See [[Graph Plotting Skills]].

3. **Error Analysis:** Understanding dimensions helps identify when units are inconsistent in calculations, reducing [[Uncertainties and Errors]].

4. **Verification of Results:** After collecting data, check if the experimental relationship matches the dimensionally predicted form.

**中文：**
量纲分析在多个方面与实验工作相关：

1. **实验设计：** 在进行实验之前，用量纲分析预测变量之间的关系。例如，在单摆实验中，量纲分析预测 $T \propto \sqrt{L/g}$，指导你选择要测量的变量。

2. **图表绘制：** 量纲分析有助于确定每个坐标轴上绘制什么。如果你预期 $T \propto \sqrt{L}$，则绘制T对$\sqrt{L}$的图以获得直线。参见[[图表绘制技能]]。

3. **误差分析：** 理解量纲有助于识别计算中单位不一致的情况，减少[[不确定性和误差]]。

4. **结果验证：** 收集数据后，检查实验关系是否与量纲预测的形式匹配。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    DA[Dimensional Analysis] --> Base[Base Dimensions]
    DA --> Derived[Derived Dimensions]
    DA --> Homogeneity[Checking Homogeneity]
    DA --> Derivation[Deriving Relationships]
    
    Base --> M[[M] Mass]
    Base --> L[[L] Length]
    Base --> T[[T] Time]
    Base --> I[[I] Current]
    
    Derived --> Velocity[[LT⁻¹] Velocity]
    Derived --> Acceleration[[LT⁻²] Acceleration]
    Derived --> Force[[MLT⁻²] Force]
    Derived --> Energy[[ML²T⁻²] Energy/Work]
    Derived --> Power[[ML²T⁻³] Power]
    Derived --> Pressure[[ML⁻¹T⁻²] Pressure]
    
    Homogeneity --> Compare[Compare dimensions of all terms]
    Compare --> Same[Same? → Homogeneous]
    Compare --> Different[Different? → Not Homogeneous]
    
    Derivation --> Identify[Identify variables]
    Derivation --> Assume[Assume product form]
    Derivation --> Solve[Solve exponent equations]
    Derivation --> Result[Write relationship with unknown constant k]
    
    DA --> SI[[SI Base Units and Derived Units]]
    DA --> HomogEq[[Homogeneity of Physical Equations]]
    DA --> Graph[[Graph Plotting Skills]]
    DA --> Errors[[Uncertainties and Errors]]
    
    style DA fill:#4a90d9,color:#fff
    style Base fill:#f0a030,color:#fff
    style Derived fill:#50b080,color:#fff
    style Homogeneity fill:#d94a4a,color:#fff
    style Derivation fill:#8b5cf6,color:#fff
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Dimensions represent the fundamental nature of physical quantities using [M], [L], [T], [I], [Θ], [N], [J] |
| **Key Formula / 核心公式** | $[Q] = [M]^a[L]^b[T]^c$; Homogeneity: all terms must have same dimensions |
| **Key Graph / 核心图表** | Dimension derivation tree (see Section 7.1) |
| **Common Dimensions / 常见量纲** | Velocity: [LT⁻¹]; Force: [MLT⁻²]; Energy: [ML²T⁻²]; Power: [ML²T⁻³]; Pressure: [ML⁻¹T⁻²] |
| **Exam Tip 1 / 考试提示1** | Always derive dimensions from defining equations, not from the equation being checked |
| **Exam Tip 2 / 考试提示2** | Pure numbers (2, π, ½) are dimensionless — ignore them in dimensional analysis |
| **Exam Tip 3 / 考试提示3** | Dimensional analysis cannot find dimensionless constants — they must be found experimentally |
| **Common Mistake / 常见错误** | Confusing dimensions with units (e.g., writing [m/s] instead of [LT⁻¹]) |
| **Must Know / 必须掌握** | How to check homogeneity AND how to derive relationships using dimensional analysis |
| **Equation Form / 方程形式** | Always assume $A = k \cdot B^a \cdot C^b \cdot D^c$ for dimensional analysis derivation |

> 📋 **CIE Only:** CAIE 9702 focuses more on checking homogeneity than deriving relationships. Ensure you can clearly show the dimension of each term.
> 
> 📋 **Edexcel Only:** Edexcel IAL WPH11 includes more emphasis on using dimensional analysis to derive the form of relationships, especially in mechanics contexts.

---

**Related Leaf Nodes:** [[SI Base Units and Derived Units]], [[Homogeneity of Physical Equations]], [[SI Prefixes (pico to tera)]], [[Converting Between Units]]
**Parent Hub:** [[SI Units, Prefixes and Homogeneity of Equations]]
**Related Topics:** [[Uncertainties and Errors]], [[Graph Plotting Skills]]