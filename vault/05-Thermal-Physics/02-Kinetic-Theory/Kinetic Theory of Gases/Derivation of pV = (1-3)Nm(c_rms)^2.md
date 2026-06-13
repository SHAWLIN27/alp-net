# Derivation of pV = (1/3)Nm(c_rms)² / pV = (1/3)Nm(c_rms)² 的推导

---

# 1. Overview / 概述

**English:**
This sub-topic presents the **kinetic derivation** of the fundamental equation linking the macroscopic properties of an ideal gas (pressure $p$ and volume $V$) to its microscopic properties (number of molecules $N$, molecular mass $m$, and the mean square speed $\overline{c^2}$). The result, $pV = \frac{1}{3} N m \overline{c^2}$, is the **central equation of the kinetic theory of gases**. It bridges the gap between the [[Kinetic Theory Assumptions]] and measurable gas behaviour, and leads directly to the relationship between [[Mean Kinetic Energy and Temperature]].

**中文:**
本子知识点介绍理想气体宏观性质（压强 $p$ 和体积 $V$）与微观性质（分子数 $N$、分子质量 $m$ 和均方速度 $\overline{c^2}$）之间基本方程的**动力学推导**。结果 $pV = \frac{1}{3} N m \overline{c^2}$ 是**气体分子动理论的核心方程**。它连接了[[Kinetic Theory Assumptions]]与可测量的气体行为，并直接导出[[Mean Kinetic Energy and Temperature]]之间的关系。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (11.2 a-e) | Edexcel IAL (WPH11 U1: 5.23-5.27) |
|----------------------|-----------------------------------|
| Derive $pV = \frac{1}{3} N m \overline{c^2}$ from kinetic theory assumptions | Derive the kinetic theory equation $pV = \frac{1}{3} N m c_{rms}^2$ |
| Explain the significance of the root-mean-square speed | Understand the derivation of $p = \frac{1}{3} \rho \langle c^2 \rangle$ |
| Relate pressure to molecular motion | Use the equation to solve problems involving gas pressure and molecular speeds |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to reproduce the full derivation step-by-step, explaining each assumption used. You should understand why $\overline{c^2}$ (mean square speed) appears, not $(\overline{c})^2$ (square of mean speed). You must be able to manipulate the equation to find $c_{rms}$.
- **中文:** 必须能够逐步重现完整的推导过程，并解释每一步所使用的假设。应理解为什么出现的是 $\overline{c^2}$（均方速度）而不是 $(\overline{c})^2$（平均速度的平方）。必须能够操作方程求出 $c_{rms}$。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Mean Square Speed** $\overline{c^2}$ / 均方速度 | The average of the squares of the speeds of all molecules in a gas sample. | 气体样品中所有分子速度平方的平均值。 | Confusing with $(\overline{c})^2$ (square of mean speed). $\overline{c^2} \neq (\overline{c})^2$ |
| **Root Mean Square Speed** $c_{rms}$ / 方均根速度 | The square root of the mean square speed: $c_{rms} = \sqrt{\overline{c^2}}$ | 均方速度的平方根：$c_{rms} = \sqrt{\overline{c^2}}$ | Forgetting to take the square root at the end of a calculation. |
| **Pressure** $p$ / 压强 | Force per unit area exerted by gas molecules colliding with container walls. | 气体分子与容器壁碰撞所产生的单位面积上的力。 | Thinking pressure is due to static repulsion between molecules (it is due to collisions). |
| **Number Density** $n = N/V$ / 数密度 | Number of molecules per unit volume. | 单位体积内的分子数。 | Confusing with $n$ (number of moles) in the ideal gas law. |
| **Molecular Mass** $m$ / 分子质量 | Mass of a single molecule of the gas. | 单个气体分子的质量。 | Using molar mass $M$ instead of $m$ without conversion. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Derivation Strategy / 推导策略

### Explanation / 解释
**English:**
The derivation follows a logical sequence based on the [[Kinetic Theory Assumptions]]:
1. **Consider one molecule** moving in a cubical box of side length $L$.
2. **Calculate the change in momentum** when it collides elastically with one wall.
3. **Calculate the time between collisions** with that same wall.
4. **Calculate the force** exerted by that one molecule on the wall (rate of change of momentum).
5. **Sum over all molecules** in all three dimensions.
6. **Relate force to pressure** ($p = F/A$) and volume ($V = L^3$).

**中文:**
推导基于[[Kinetic Theory Assumptions]]，遵循以下逻辑顺序：
1. **考虑一个分子**在边长为 $L$ 的立方体容器中运动。
2. **计算与一面墙弹性碰撞时的动量变化**。
3. **计算与同一面墙两次碰撞之间的时间间隔**。
4. **计算该分子对墙施加的力**（动量变化率）。
5. **对所有分子和三个维度求和**。
6. **将力与压强** ($p = F/A$) **和体积** ($V = L^3$) **联系起来**。

### Physical Meaning / 物理意义
**English:**
The equation $pV = \frac{1}{3} N m \overline{c^2}$ shows that gas pressure arises from the **collective effect of countless molecular collisions** with the container walls. The factor $\frac{1}{3}$ arises because, on average, only one-third of the molecules' velocity components are directed towards any given wall at any instant.

**中文:**
方程 $pV = \frac{1}{3} N m \overline{c^2}$ 表明气体压强源于**无数分子与容器壁碰撞的集体效应**。因子 $\frac{1}{3}$ 的出现是因为，在任意时刻，平均只有三分之一的分子速度分量指向某一特定墙面。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking the $\frac{1}{3}$ comes from the three dimensions of space (it does, but specifically from averaging velocity components).
  - Believing all molecules move at the same speed (they have a distribution; we use $\overline{c^2}$).
  - Forgetting that the collision is elastic (kinetic energy is conserved).
- **中文:**
  - 认为 $\frac{1}{3}$ 来自三维空间（确实如此，但具体来自速度分量的平均）。
  - 认为所有分子以相同速度运动（它们有分布；我们使用 $\overline{c^2}$）。
  - 忘记碰撞是弹性的（动能守恒）。

### Exam Tips / 考试提示
- **English:** Memorise the derivation steps. Examiners often ask "State the assumptions used in the derivation of $pV = \frac{1}{3} N m \overline{c^2}$" — list all [[Kinetic Theory Assumptions]].
- **中文:** 记住推导步骤。考官常问"陈述推导 $pV = \frac{1}{3} N m \overline{c^2}$ 时使用的假设"——列出所有[[Kinetic Theory Assumptions]]。

> 📷 **IMAGE PROMPT — DERIV-01: Single Molecule in a Cubical Box**
> A 3D diagram showing a single molecule moving inside a cube of side length L. The molecule has velocity components v_x, v_y, v_z. One wall (shaded) is labelled as the wall being considered. Arrows show the molecule approaching and rebounding from the wall. Labels: "Elastic collision", "Change in momentum = 2mv_x".

---

## 4.2 Why Mean Square Speed? / 为什么是均方速度？

### Explanation / 解释
**English:**
When summing the contributions from all molecules, we need the average of the squares of the $x$-components of velocity: $\overline{v_x^2}$. Since the motion is random, $\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2} = \frac{1}{3} \overline{c^2}$, where $\overline{c^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2}$. The **square** is essential because momentum change depends on $v_x$ (not $v_x^2$), but the force depends on $v_x$ multiplied by the collision frequency (which also depends on $v_x$), giving $v_x^2$.

**中文:**
当对所有分子的贡献求和时，我们需要速度 $x$ 分量平方的平均值：$\overline{v_x^2}$。由于运动是随机的，$\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2} = \frac{1}{3} \overline{c^2}$，其中 $\overline{c^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2}$。**平方**是必要的，因为动量变化取决于 $v_x$（而不是 $v_x^2$），但力取决于 $v_x$ 乘以碰撞频率（也取决于 $v_x$），得到 $v_x^2$。

### Physical Meaning / 物理意义
**English:**
Using $\overline{c^2}$ (mean square speed) rather than $(\overline{c})^2$ (square of mean speed) is crucial because faster molecules hit the walls more frequently AND with greater momentum change per collision. The mean square speed captures this **double weighting** of faster molecules.

**中文:**
使用 $\overline{c^2}$（均方速度）而不是 $(\overline{c})^2$（平均速度的平方）至关重要，因为更快的分子碰撞墙壁更频繁，且每次碰撞的动量变化更大。均方速度捕捉了更快分子的这种**双重加权**。

---

# 5. Essential Equations / 核心公式

## 5.1 The Kinetic Theory Equation / 气体动理论方程

$$ pV = \frac{1}{3} N m \overline{c^2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $p$ | Pressure of the gas | 气体压强 | Pa (N m$^{-2}$) |
| $V$ | Volume of the container | 容器体积 | m$^3$ |
| $N$ | Number of molecules | 分子数目 | dimensionless |
| $m$ | Mass of one molecule | 单个分子质量 | kg |
| $\overline{c^2}$ | Mean square speed of molecules | 分子均方速度 | m$^2$ s$^{-2}$ |

**Alternative Forms / 其他形式:**
$$ p = \frac{1}{3} \rho \overline{c^2} \quad \text{where } \rho = \frac{Nm}{V} \text{ (density)} $$
$$ p = \frac{1}{3} n m \overline{c^2} \quad \text{where } n = \frac{N}{V} \text{ (number density)} $$

**Derivation / 推导:**
1. Consider a cube of side $L$. Volume $V = L^3$.
2. One molecule with velocity components $v_x, v_y, v_z$.
3. Collision with wall perpendicular to $x$: momentum change $\Delta p = 2mv_x$.
4. Time between collisions with same wall: $\Delta t = \frac{2L}{v_x}$.
5. Force from one molecule: $F_1 = \frac{\Delta p}{\Delta t} = \frac{2mv_x}{2L/v_x} = \frac{mv_x^2}{L}$.
6. Total force from $N$ molecules: $F = \frac{m}{L} \sum v_x^2 = \frac{m}{L} N \overline{v_x^2}$.
7. Pressure: $p = \frac{F}{A} = \frac{F}{L^2} = \frac{m N \overline{v_x^2}}{L^3} = \frac{N m \overline{v_x^2}}{V}$.
8. Since $\overline{c^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2} = 3\overline{v_x^2}$, we have $\overline{v_x^2} = \frac{1}{3}\overline{c^2}$.
9. Therefore: $p = \frac{N m}{V} \cdot \frac{1}{3} \overline{c^2}$ → $pV = \frac{1}{3} N m \overline{c^2}$.

**Conditions / 适用条件:**
- **English:** Ideal gas only. Assumes [[Kinetic Theory Assumptions]] hold: negligible molecular size, elastic collisions, no intermolecular forces, random motion.
- **中文:** 仅适用于理想气体。假设[[Kinetic Theory Assumptions]]成立：分子大小可忽略、弹性碰撞、无分子间作用力、随机运动。

**Limitations / 局限性:**
- **English:** Does not account for real gas effects (van der Waals forces, finite molecular volume). Only valid at low pressures and high temperatures.
- **中文:** 不考虑真实气体效应（范德华力、有限分子体积）。仅在低压高温下有效。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Pressure vs. Mean Square Speed / 压强与均方速度的关系

### Axes / 坐标轴
- **x-axis:** $\overline{c^2}$ (mean square speed) / 均方速度 (m$^2$ s$^{-2}$)
- **y-axis:** $p$ (pressure) / 压强 (Pa)

### Shape / 形状
**English:** A straight line through the origin, with gradient $\frac{1}{3} \frac{Nm}{V}$.
**中文:** 一条通过原点的直线，斜率为 $\frac{1}{3} \frac{Nm}{V}$。

### Gradient Meaning / 斜率含义
**English:** The gradient is $\frac{1}{3} \frac{Nm}{V} = \frac{1}{3} \rho$, where $\rho$ is the gas density. A steeper gradient means higher density or lower volume.
**中文:** 斜率为 $\frac{1}{3} \frac{Nm}{V} = \frac{1}{3} \rho$，其中 $\rho$ 是气体密度。斜率越大表示密度越高或体积越小。

### Area Meaning / 面积含义
**English:** No meaningful area under this graph.
**中文:** 该图线下无有意义的面积。

### Exam Interpretation / 考试解读
**English:** If asked to sketch $p$ against $\overline{c^2}$, draw a straight line through origin. If asked about $p$ against $c_{rms}$, the graph is a parabola ($p \propto c_{rms}^2$).
**中文:** 如果要求画出 $p$ 对 $\overline{c^2}$ 的草图，画一条通过原点的直线。如果问 $p$ 对 $c_{rms}$，图形是抛物线 ($p \propto c_{rms}^2$)。

> 📷 **IMAGE PROMPT — GRAPH-01: Pressure vs Mean Square Speed**
> A Cartesian graph with "Mean square speed / m² s⁻²" on the x-axis and "Pressure / Pa" on the y-axis. A straight line passes through the origin with positive gradient. The line is labelled "p = (1/3)(Nm/V) c²". A second, steeper line is shown with a dashed style, labelled "Higher density or smaller volume".

---

# 7. Required Diagrams / 必备图表

## 7.1 Single Molecule Collision Model / 单分子碰撞模型

### Description / 描述
**English:** A diagram showing a single gas molecule moving inside a cubical container of side length $L$. The molecule has velocity components $v_x$, $v_y$, $v_z$. It collides elastically with the right-hand wall, reversing its $x$-component of velocity. The path between collisions is shown.
**中文:** 一个显示单个气体分子在边长为 $L$ 的立方体容器内运动的示意图。分子具有速度分量 $v_x$、$v_y$、$v_z$。它与右侧墙壁发生弹性碰撞，其 $x$ 方向速度分量反向。显示了两次碰撞之间的路径。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-01: Single Molecule Collision Model for Kinetic Theory Derivation**
> A clean physics textbook-style diagram. A cube with side length L. A single spherical molecule is shown moving towards the right wall with velocity component v_x. The molecule has velocity components labelled v_x, v_y, v_z. An arrow shows the molecule approaching the wall, and another arrow shows it rebounding with velocity -v_x. The wall is shaded. Labels: "Elastic collision", "Change in momentum = 2mv_x", "Time between collisions = 2L/v_x". The cube is labelled "Volume V = L³". Minimalist style, black and white with blue accents.

### Labels Required / 需要标注
- **English:** $L$ (side length), $v_x, v_y, v_z$ (velocity components), "Wall", "Elastic collision", $\Delta p = 2mv_x$, $\Delta t = 2L/v_x$
- **中文:** $L$（边长），$v_x, v_y, v_z$（速度分量），"墙壁"，"弹性碰撞"，$\Delta p = 2mv_x$，$\Delta t = 2L/v_x$

### Exam Importance / 考试重要性
**English:** This diagram is essential for the derivation. You may be asked to draw and label it, or to explain each step using the diagram.
**中文:** 此图对推导至关重要。可能会被要求画出并标注，或使用该图解释每一步。

---

## 7.2 Molecular Speed Distribution / 分子速度分布

### Description / 描述
**English:** A Maxwell-Boltzmann distribution curve showing the spread of molecular speeds in a gas. The positions of $\overline{c}$ (mean speed), $c_{mp}$ (most probable speed), and $c_{rms}$ (root mean square speed) are marked.
**中文:** 显示气体中分子速度分布的麦克斯韦-玻尔兹曼分布曲线。标出了 $\overline{c}$（平均速度）、$c_{mp}$（最概然速度）和 $c_{rms}$（方均根速度）的位置。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-02: Maxwell-Boltzmann Speed Distribution with c_rms Marked**
> A graph showing a Maxwell-Boltzmann speed distribution curve. The x-axis is "Molecular speed / m s⁻¹" and the y-axis is "Number of molecules". The curve starts at zero, rises to a peak, then decays. Three vertical lines are drawn: the leftmost labelled "c_mp (most probable)", the middle labelled "c̄ (mean)", and the rightmost labelled "c_rms (root mean square)". The area under the curve is shaded. The relative positions show c_mp < c̄ < c_rms. Clean, textbook style.

### Labels Required / 需要标注
- **English:** $c_{mp}$, $\overline{c}$, $c_{rms}$, "Number of molecules", "Molecular speed"
- **中文:** $c_{mp}$（最概然速度），$\overline{c}$（平均速度），$c_{rms}$（方均根速度），"分子数"，"分子速度"

### Exam Importance / 考试重要性
**English:** Understanding that $c_{rms} > \overline{c}$ is important. The derivation uses $\overline{c^2}$, not $(\overline{c})^2$, because of the distribution of speeds.
**中文:** 理解 $c_{rms} > \overline{c}$ 很重要。由于速度分布的存在，推导使用 $\overline{c^2}$ 而不是 $(\overline{c})^2$。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Pressure from Molecular Data / 从分子数据计算压强

### Question / 题目
**English:**
A container of volume $2.5 \times 10^{-3} \text{ m}^3$ contains $6.0 \times 10^{23}$ molecules of an ideal gas. Each molecule has a mass of $4.65 \times 10^{-26} \text{ kg}$. The root mean square speed of the molecules is $500 \text{ m s}^{-1}$.
Calculate the pressure exerted by the gas.

**中文:**
一个体积为 $2.5 \times 10^{-3} \text{ m}^3$ 的容器中含有 $6.0 \times 10^{23}$ 个理想气体分子。每个分子的质量为 $4.65 \times 10^{-26} \text{ kg}$。分子的方均根速度为 $500 \text{ m s}^{-1}$。
计算气体施加的压强。

### Solution / 解答
**Step 1: Identify the equation / 确定方程**
$$ pV = \frac{1}{3} N m \overline{c^2} $$

**Step 2: Find $\overline{c^2}$ / 求 $\overline{c^2}$**
$$ c_{rms} = \sqrt{\overline{c^2}} \implies \overline{c^2} = (c_{rms})^2 = (500)^2 = 2.5 \times 10^5 \text{ m}^2 \text{ s}^{-2} $$

**Step 3: Substitute values / 代入数值**
$$ p \times (2.5 \times 10^{-3}) = \frac{1}{3} \times (6.0 \times 10^{23}) \times (4.65 \times 10^{-26}) \times (2.5 \times 10^5) $$

**Step 4: Calculate / 计算**
$$ p \times 2.5 \times 10^{-3} = \frac{1}{3} \times 6.0 \times 10^{23} \times 4.65 \times 10^{-26} \times 2.5 \times 10^5 $$
$$ p \times 2.5 \times 10^{-3} = \frac{1}{3} \times 6.0 \times 4.65 \times 2.5 \times 10^{23-26+5} $$
$$ p \times 2.5 \times 10^{-3} = \frac{1}{3} \times 69.75 \times 10^2 $$
$$ p \times 2.5 \times 10^{-3} = 23.25 \times 10^2 = 2325 $$

**Step 5: Solve for $p$ / 解出 $p$**
$$ p = \frac{2325}{2.5 \times 10^{-3}} = 9.3 \times 10^5 \text{ Pa} $$

### Final Answer / 最终答案
**Answer:** $p = 9.3 \times 10^5 \text{ Pa}$ | **答案：** $p = 9.3 \times 10^5 \text{ Pa}$

### Quick Tip / 提示
**English:** Always check whether you are given $c_{rms}$ or $\overline{c^2}$. If given $c_{rms}$, remember to square it first. If given $\overline{c^2}$, take the square root to find $c_{rms}$.
**中文:** 始终检查给的是 $c_{rms}$ 还是 $\overline{c^2}$。如果给的是 $c_{rms}$，记得先平方。如果给的是 $\overline{c^2}$，开平方根得到 $c_{rms}$。

---

## Example 2: Finding Root Mean Square Speed / 求方均根速度

### Question / 题目
**English:**
The pressure of an ideal gas is $1.01 \times 10^5 \text{ Pa}$ and its density is $1.29 \text{ kg m}^{-3}$.
Calculate the root mean square speed of the gas molecules.

**中文:**
理想气体的压强为 $1.01 \times 10^5 \text{ Pa}$，密度为 $1.29 \text{ kg m}^{-3}$。
计算气体分子的方均根速度。

### Solution / 解答
**Step 1: Use the density form / 使用密度形式**
$$ p = \frac{1}{3} \rho \overline{c^2} $$

**Step 2: Rearrange for $\overline{c^2}$ / 解出 $\overline{c^2}$**
$$ \overline{c^2} = \frac{3p}{\rho} = \frac{3 \times 1.01 \times 10^5}{1.29} $$

**Step 3: Calculate / 计算**
$$ \overline{c^2} = \frac{3.03 \times 10^5}{1.29} = 2.349 \times 10^5 \text{ m}^2 \text{ s}^{-2} $$

**Step 4: Find $c_{rms}$ / 求 $c_{rms}$**
$$ c_{rms} = \sqrt{\overline{c^2}} = \sqrt{2.349 \times 10^5} = 484.7 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** $c_{rms} = 485 \text{ m s}^{-1}$ (3 s.f.) | **答案：** $c_{rms} = 485 \text{ m s}^{-1}$（3位有效数字）

### Quick Tip / 提示
**English:** The density form $p = \frac{1}{3} \rho \overline{c^2}$ is very useful when you don't know $N$ or $m$ individually. Remember $\rho = \frac{Nm}{V}$.
**中文:** 当不知道 $N$ 或 $m$ 时，密度形式 $p = \frac{1}{3} \rho \overline{c^2}$ 非常有用。记住 $\rho = \frac{Nm}{V}$。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Derivation of $pV = \frac{1}{3} Nm\overline{c^2}$ | High | Medium | 📝 *待填入* |
| Calculation of $c_{rms}$ from $p$ and $\rho$ | High | Easy | 📝 *待填入* |
| Calculation of pressure from molecular data | Medium | Medium | 📝 *待填入* |
| Stating assumptions used in derivation | High | Easy | 📝 *待填入* |
| Explaining why $\overline{c^2}$ is used instead of $(\overline{c})^2$ | Medium | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Derive, State, Calculate, Explain, Show that, Suggest
- **中文:** 推导、陈述、计算、解释、证明、提出

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
While the derivation itself is theoretical, the equation $pV = \frac{1}{3} N m \overline{c^2}$ connects to practical work in several ways:

1. **Measurement of $c_{rms}$:** Using the equation $c_{rms} = \sqrt{3p/\rho}$, you can calculate $c_{rms}$ from measured pressure and density values. This requires accurate measurement of pressure (using a pressure sensor or manometer) and density (from mass and volume measurements).

2. **Uncertainty Analysis:** When calculating $c_{rms}$, uncertainties in $p$ and $\rho$ propagate. The percentage uncertainty in $c_{rms}$ is half the sum of percentage uncertainties in $p$ and $\rho$ (due to the square root).

3. **Graphical Verification:** Plotting $p$ against $\overline{c^2}$ should give a straight line through the origin, verifying the relationship. This requires measuring $c_{rms}$ at different temperatures.

4. **Experimental Design:** To verify the equation, you would need to measure pressure, volume, temperature, and the mass of gas. The number of molecules $N$ can be found from the mass of gas and the molecular mass.

**中文:**
虽然推导本身是理论性的，但方程 $pV = \frac{1}{3} N m \overline{c^2}$ 通过以下方式与实验工作联系：

1. **测量 $c_{rms}$：** 使用方程 $c_{rms} = \sqrt{3p/\rho}$，可以从测量的压强和密度值计算 $c_{rms}$。这需要精确测量压强（使用压强传感器或压力计）和密度（通过质量和体积测量）。

2. **不确定度分析：** 计算 $c_{rms}$ 时，$p$ 和 $\rho$ 的不确定度会传递。$c_{rms}$ 的百分比不确定度是 $p$ 和 $\rho$ 百分比不确定度之和的一半（由于平方根）。

3. **图形验证：** 绘制 $p$ 对 $\overline{c^2}$ 的图应得到一条通过原点的直线，验证该关系。这需要在不同温度下测量 $c_{rms}$。

4. **实验设计：** 要验证该方程，需要测量压强、体积、温度和气体质量。分子数 $N$ 可以从气体质量和分子质量求出。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Kinetic Theory Assumptions] --> B[Derivation of pV = 1/3 Nm c²]
    B --> C[Equation: pV = 1/3 Nm c²]
    C --> D[Alternative: p = 1/3 ρ c²]
    C --> E[Root Mean Square Speed c_rms]
    E --> F[c_rms = √(3p/ρ)]
    C --> G[Mean Kinetic Energy]
    G --> H[KE_avg = 3/2 kT]
    H --> I[The Boltzmann Constant]
    C --> J[Ideal Gas Law pV = NkT]
    J --> I
    
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:1px
    style H fill:#bfb,stroke:#333,stroke-width:1px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | $pV = \frac{1}{3} N m \overline{c^2}$ — links macroscopic ($p,V$) to microscopic ($N,m,\overline{c^2}$) / 连接宏观量 ($p,V$) 与微观量 ($N,m,\overline{c^2}$) |
| **Key Formula / 核心公式** | $pV = \frac{1}{3} N m \overline{c^2}$; $p = \frac{1}{3} \rho \overline{c^2}$; $c_{rms} = \sqrt{\overline{c^2}}$ |
| **Key Graph / 核心图表** | $p$ vs $\overline{c^2}$: straight line through origin, gradient $= \frac{1}{3} \frac{Nm}{V}$ / $p$ 对 $\overline{c^2}$：通过原点的直线，斜率 $= \frac{1}{3} \frac{Nm}{V}$ |
| **Key Assumptions / 关键假设** | 1. Negligible molecular size / 分子大小可忽略 2. Elastic collisions / 弹性碰撞 3. No intermolecular forces / 无分子间作用力 4. Random motion / 随机运动 5. Large number of molecules / 大量分子 6. Container walls are rigid / 容器壁刚性 |
| **Why $\overline{c^2}$? / 为什么用 $\overline{c^2}$？** | Force depends on $v_x$ × collision frequency (also ∝ $v_x$) → $v_x^2$ → need $\overline{v_x^2}$ → $\frac{1}{3}\overline{c^2}$ / 力取决于 $v_x$ × 碰撞频率（也∝ $v_x$）→ $v_x^2$ → 需要 $\overline{v_x^2}$ → $\frac{1}{3}\overline{c^2}$ |
| **Exam Tip / 考试提示** | Memorise the 6-step derivation. Know the density form. Distinguish $c_{rms}$ from $\overline{c^2}$. / 记住6步推导。掌握密度形式。区分 $c_{rms}$ 和 $\overline{c^2}$。 |
| **Common Mistake / 常见错误** | Confusing $\overline{c^2}$ with $(\overline{c})^2$; forgetting to square $c_{rms}$; omitting the $\frac{1}{3}$ factor / 混淆 $\overline{c^2}$ 和 $(\overline{c})^2$；忘记平方 $c_{rms}$；遗漏 $\frac{1}{3}$ 因子 |