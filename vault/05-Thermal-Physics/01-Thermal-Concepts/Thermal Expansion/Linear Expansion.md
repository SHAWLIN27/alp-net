# 1. Overview / 概述

**English:**
Linear expansion describes how the length of a solid material changes when its temperature changes. This sub-topic is fundamental to understanding [[Thermal Expansion]] because most engineering structures and precision instruments must account for length changes due to temperature variations. When a solid is heated, its atoms vibrate more vigorously, increasing the average separation between them, which manifests as an increase in length. The key parameter is the coefficient of linear expansion ($\alpha$), which quantifies how much a material expands per degree temperature change per unit length.

This concept connects directly to [[Temperature and Thermal Equilibrium]] as the driving mechanism, and leads naturally to [[Area and Volume Expansion]] for two-dimensional and three-dimensional cases. Understanding linear expansion is essential for real-world applications like railway tracks, bridges, and thermostats, which are explored in [[Applications and Consequences of Thermal Expansion]] and [[Bimetallic Strips and Thermostats]].

**中文:**
线性膨胀描述的是固体材料的长度如何随温度变化而改变。这个子知识点是理解[[Thermal Expansion]]的基础，因为大多数工程结构和精密仪器都必须考虑温度变化引起的长度变化。当固体被加热时，其原子振动更加剧烈，增加了它们之间的平均间距，表现为长度的增加。关键参数是线膨胀系数（$\alpha$），它量化了材料每单位长度每度温度变化时的膨胀量。

这个概念直接连接到[[Temperature and Thermal Equilibrium]]作为驱动机制，并自然地引向[[Area and Volume Expansion]]的二维和三维情况。理解线性膨胀对于铁路轨道、桥梁和恒温器等实际应用至关重要，这些在[[Applications and Consequences of Thermal Expansion]]和[[Bimetallic Strips and Thermostats]]中有所探讨。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 10.2(a) Define and use the coefficient of linear expansion | 5.5 Understand that materials expand when heated and contract when cooled |
| 10.2(b) Apply the linear expansion equation $\Delta L = \alpha L_0 \Delta T$ | 5.6 Use the equation $\Delta L = \alpha L_0 \Delta T$ |
| 10.2(c) Solve problems involving linear expansion in practical contexts | 5.7 Solve problems involving thermal expansion in everyday contexts |
| 10.2(d) Distinguish between linear, area, and volume expansion | — |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to define $\alpha$ precisely, apply the formula correctly with consistent units, and interpret real-world scenarios involving expansion gaps, thermal stress, and material selection.
- **中文:** 学生必须能够精确定义$\alpha$，使用一致的单位正确应用公式，并解释涉及膨胀间隙、热应力和材料选择的实际场景。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Linear Expansion** / 线性膨胀 | The increase in length of a solid material when its temperature increases | 固体材料温度升高时长度的增加 | Confusing with area/volume expansion / 与面积/体积膨胀混淆 |
| **Coefficient of Linear Expansion ($\alpha$)** / 线膨胀系数 | The fractional change in length per unit temperature change: $\alpha = \frac{\Delta L}{L_0 \Delta T}$ | 单位温度变化引起的长度相对变化率 | Forgetting units ($K^{-1}$ or $^\circ C^{-1}$) / 忘记单位 |
| **Original Length ($L_0$)** / 原始长度 | The length of the material at the reference temperature | 材料在参考温度下的长度 | Using final length instead of original / 使用最终长度而非原始长度 |
| **Temperature Change ($\Delta T$)** / 温度变化 | The difference between final and initial temperature | 最终温度与初始温度的差值 | Using Celsius and Kelvin inconsistently / 摄氏度和开尔文使用不一致 |
| **Thermal Stress** / 热应力 | The stress developed in a material when thermal expansion is constrained | 当热膨胀受到约束时材料内部产生的应力 | Confusing with thermal strain / 与热应变混淆 |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Mechanism of Linear Expansion / 线性膨胀的机制

### Explanation / 解释
**English:** When a solid is heated, the kinetic energy of its atoms increases, causing them to vibrate more vigorously around their equilibrium positions. The interatomic potential energy curve is asymmetric — atoms can move further apart more easily than they can move closer together. This asymmetry means that as temperature rises, the average atomic separation increases, resulting in macroscopic expansion of the material. The coefficient of linear expansion $\alpha$ is a material property that depends on the strength of interatomic bonds: stronger bonds (like in diamond) give smaller $\alpha$ values, while weaker bonds (like in lead) give larger $\alpha$ values.

**中文:** 当固体被加热时，其原子的动能增加，导致它们在平衡位置周围振动更加剧烈。原子间势能曲线是不对称的——原子更容易远离彼此而不是靠近。这种不对称性意味着随着温度升高，平均原子间距增加，导致材料的宏观膨胀。线膨胀系数$\alpha$是一种材料属性，取决于原子间键的强度：更强的键（如金刚石）产生更小的$\alpha$值，而更弱的键（如铅）产生更大的$\alpha$值。

### Physical Meaning / 物理意义
**English:** $\alpha$ represents the fractional change in length per degree temperature change. For example, $\alpha = 2 \times 10^{-5} K^{-1}$ means that a 1 m rod expands by $2 \times 10^{-5}$ m (0.02 mm) for every 1 K temperature increase.

**中文:** $\alpha$表示每度温度变化引起的长度相对变化率。例如，$\alpha = 2 \times 10^{-5} K^{-1}$意味着1米长的杆每升高1 K温度膨胀$2 \times 10^{-5}$米（0.02毫米）。

### Common Misconceptions / 常见误区
- **English:** 
  - Thinking $\alpha$ depends on the length of the object (it doesn't — it's a material property)
  - Using $\Delta T$ in Celsius when the formula requires Kelvin (the numerical value is the same for temperature differences)
  - Confusing $\alpha$ with the coefficient of area expansion ($\beta \approx 2\alpha$) or volume expansion ($\gamma \approx 3\alpha$)
- **中文:**
  - 认为$\alpha$取决于物体的长度（不——它是材料属性）
  - 当公式需要开尔文时使用摄氏度的$\Delta T$（温度差的数值相同）
  - 混淆$\alpha$与面膨胀系数（$\beta \approx 2\alpha$）或体膨胀系数（$\gamma \approx 3\alpha$）

### Exam Tips / 考试提示
- **English:** Always check units — $\alpha$ is typically given in $K^{-1}$ or $^\circ C^{-1}$. For temperature differences, 1 K = 1 $^\circ C$, so you can use either as long as you're consistent. Remember that $\Delta L$ is usually very small compared to $L_0$, so expect answers in millimeters or micrometers.
- **中文:** 始终检查单位——$\alpha$通常以$K^{-1}$或$^\circ C^{-1}$给出。对于温度差，1 K = 1 $^\circ C$，所以只要一致就可以使用任意一种。记住$\Delta L$通常比$L_0$小得多，所以答案通常以毫米或微米为单位。

> 📷 **IMAGE PROMPT — LE-01: Atomic Vibration Model for Linear Expansion**
> A diagram showing atoms in a crystal lattice at low temperature (small vibrations, close spacing) and high temperature (larger vibrations, increased spacing). Include an asymmetric potential energy curve showing the average atomic separation increasing with temperature. Labels: "Low T", "High T", "Interatomic distance", "Potential energy".

---

# 5. Essential Equations / 核心公式

## Equation 1: Linear Expansion Formula / 线性膨胀公式

$$ \Delta L = \alpha L_0 \Delta T $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta L$ | Change in length | 长度变化量 | m (or mm, μm) |
| $\alpha$ | Coefficient of linear expansion | 线膨胀系数 | $K^{-1}$ or $^\circ C^{-1}$ |
| $L_0$ | Original length | 原始长度 | m |
| $\Delta T$ | Change in temperature | 温度变化量 | K or $^\circ C$ |

**Derivation / 推导:**
- **English:** The definition of $\alpha$ is $\alpha = \frac{\Delta L}{L_0 \Delta T}$. Rearranging gives $\Delta L = \alpha L_0 \Delta T$. This is an empirical relationship valid for small temperature changes where $\alpha$ remains approximately constant.
- **中文:** $\alpha$的定义是$\alpha = \frac{\Delta L}{L_0 \Delta T}$。重新排列得到$\Delta L = \alpha L_0 \Delta T$。这是一个经验关系式，适用于$\alpha$近似恒定的小温度变化。

**Conditions / 适用条件:**
- **English:** Valid for solids only; assumes $\alpha$ is constant over the temperature range; applies to small temperature changes (typically < 100 K for most materials).
- **中文:** 仅适用于固体；假设$\alpha$在温度范围内恒定；适用于小温度变化（大多数材料通常< 100 K）。

**Limitations / 局限性:**
- **English:** $\alpha$ can vary with temperature for large temperature ranges; does not account for phase changes; assumes isotropic expansion (same in all directions).
- **中文:** 对于大温度范围，$\alpha$可能随温度变化；不考虑相变；假设各向同性膨胀（所有方向相同）。

## Equation 2: Final Length / 最终长度

$$ L = L_0 (1 + \alpha \Delta T) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $L$ | Final length after expansion | 膨胀后的最终长度 | m |

**Derivation / 推导:**
- **English:** Since $\Delta L = L - L_0$, substituting into $\Delta L = \alpha L_0 \Delta T$ gives $L - L_0 = \alpha L_0 \Delta T$, so $L = L_0 + \alpha L_0 \Delta T = L_0(1 + \alpha \Delta T)$.
- **中文:** 由于$\Delta L = L - L_0$，代入$\Delta L = \alpha L_0 \Delta T$得到$L - L_0 = \alpha L_0 \Delta T$，所以$L = L_0 + \alpha L_0 \Delta T = L_0(1 + \alpha \Delta T)$。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Length vs Temperature Graph / 长度-温度关系图

### Axes / 坐标轴
- **X-axis:** Temperature ($T$) / 温度 ($T$)
- **Y-axis:** Length ($L$) / 长度 ($L$)

### Shape / 形状
- **English:** A straight line with positive gradient, indicating a linear relationship between length and temperature for small temperature ranges.
- **中文:** 一条具有正斜率的直线，表明在小温度范围内长度与温度呈线性关系。

### Gradient Meaning / 斜率含义
- **English:** The gradient equals $\alpha L_0$, which is the rate of change of length with temperature.
- **中文:** 斜率等于$\alpha L_0$，即长度随温度的变化率。

### Area Meaning / 面积含义
- **English:** Not applicable — the area under this graph has no physical meaning.
- **中文:** 不适用——该图下方的面积没有物理意义。

### Exam Interpretation / 考试解读
- **English:** If given a graph of $L$ vs $T$, you can find $\alpha$ by calculating the gradient and dividing by $L_0$. The y-intercept gives $L_0$ at $T = 0$ (if extrapolated).
- **中文:** 如果给出$L$ vs $T$的图表，可以通过计算斜率并除以$L_0$来找到$\alpha$。y轴截距给出$T = 0$时的$L_0$（如果外推）。

> 📷 **IMAGE PROMPT — LE-02: Length vs Temperature Linear Graph**
> A straight-line graph with Temperature on the x-axis (0 to 100°C) and Length on the y-axis (showing small changes like 1.000 to 1.002 m). Label the gradient as αL₀ and the y-intercept as L₀. Show a data point at (20°C, 1.000 m) and (80°C, 1.0016 m).

---

# 7. Required Diagrams / 必备图表

## 7.1 Linear Expansion of a Metal Rod / 金属棒的线性膨胀

### Description / 描述
- **English:** A diagram showing a metal rod of original length $L_0$ at temperature $T_1$, and the same rod at higher temperature $T_2$ with increased length $L = L_0 + \Delta L$. Arrows indicate the direction of expansion.
- **中文:** 一个显示金属棒在温度$T_1$时的原始长度$L_0$，以及同一根棒在更高温度$T_2$时长度增加为$L = L_0 + \Delta L$的图示。箭头表示膨胀方向。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — LE-03: Linear Expansion of a Metal Rod**
> A clear physics diagram showing a metal rod at two different temperatures. Top: rod at temperature T₁ with length L₀. Bottom: same rod at temperature T₂ > T₁ with length L = L₀ + ΔL. Show expansion arrows pointing outward from the center. Label all quantities. Use a simple, clean style suitable for an A-Level textbook.

### Labels Required / 需要标注
- **English:** $L_0$ (original length), $\Delta L$ (change in length), $T_1$ (initial temperature), $T_2$ (final temperature), expansion arrows
- **中文:** $L_0$（原始长度），$\Delta L$（长度变化量），$T_1$（初始温度），$T_2$（最终温度），膨胀箭头

### Exam Importance / 考试重要性
- **English:** High — this diagram is frequently used in exam questions to set up the problem and identify known and unknown quantities.
- **中文:** 高——这个图表经常在考试题中用于设置问题并识别已知和未知量。

## 7.2 Expansion Gap in Railway Tracks / 铁路轨道的膨胀间隙

### Description / 描述
- **English:** A diagram showing two railway track sections with a small gap between them at low temperature, and the gap closing at high temperature due to expansion.
- **中文:** 一个显示两段铁路轨道在低温时之间有微小间隙，以及高温时由于膨胀间隙闭合的图示。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — LE-04: Railway Track Expansion Gap**
> A side-view diagram of two railway track sections. Top: at low temperature (winter) showing a clear gap labeled "Expansion gap". Bottom: at high temperature (summer) showing the gap reduced or closed. Label the track sections, gap width, and indicate expansion direction with arrows. Include temperature labels T_cold and T_hot.

### Labels Required / 需要标注
- **English:** Expansion gap, track section, gap width, temperature labels, expansion arrows
- **中文:** 膨胀间隙，轨道段，间隙宽度，温度标签，膨胀箭头

### Exam Importance / 考试重要性
- **English:** High — this is a classic application question that appears frequently in exams.
- **中文:** 高——这是一个经典的应用题，经常出现在考试中。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Expansion of a Steel Bridge / 计算钢桥的膨胀

### Question / 题目
**English:**
A steel bridge has a length of 50.0 m at 15°C. The coefficient of linear expansion for steel is $\alpha = 1.2 \times 10^{-5} K^{-1}$. Calculate:
(a) The expansion of the bridge when the temperature rises to 35°C.
(b) The length of the bridge at 35°C.

**中文:**
一座钢桥在15°C时的长度为50.0米。钢的线膨胀系数为$\alpha = 1.2 \times 10^{-5} K^{-1}$。计算：
(a) 当温度升至35°C时桥梁的膨胀量。
(b) 桥梁在35°C时的长度。

### Solution / 解答

**Step 1: Identify known quantities / 步骤1：确定已知量**
- $L_0 = 50.0$ m
- $T_1 = 15^\circ C$
- $T_2 = 35^\circ C$
- $\alpha = 1.2 \times 10^{-5} K^{-1}$

**Step 2: Calculate temperature change / 步骤2：计算温度变化**
$$\Delta T = T_2 - T_1 = 35 - 15 = 20^\circ C = 20 \text{ K}$$

**Step 3: Apply the linear expansion formula / 步骤3：应用线性膨胀公式**
$$\Delta L = \alpha L_0 \Delta T$$
$$\Delta L = (1.2 \times 10^{-5})(50.0)(20)$$
$$\Delta L = 1.2 \times 10^{-5} \times 1000$$
$$\Delta L = 0.012 \text{ m} = 12 \text{ mm}$$

**Step 4: Calculate final length / 步骤4：计算最终长度**
$$L = L_0 + \Delta L = 50.0 + 0.012 = 50.012 \text{ m}$$

### Final Answer / 最终答案
**Answer:** (a) $\Delta L = 12$ mm | **答案：** (a) $\Delta L = 12$ 毫米
**Answer:** (b) $L = 50.012$ m | **答案：** (b) $L = 50.012$ 米

### Quick Tip / 提示
- **English:** Always convert temperature differences to Kelvin — although numerically the same as Celsius, it's good practice for more advanced topics.
- **中文:** 始终将温度差转换为开尔文——虽然数值上与摄氏度相同，但这是为更高级主题做的好习惯。

---

## Example 2: Expansion Gap Problem / 膨胀间隙问题

### Question / 题目
**English:**
Two concrete sections of a bridge are placed end-to-end with a small gap between them. Each section is 25.0 m long at 10°C. The coefficient of linear expansion for concrete is $\alpha = 1.0 \times 10^{-5} K^{-1}$. What minimum gap must be left between the sections so they don't touch when the temperature reaches 40°C?

**中文:**
一座桥的两段混凝土部分首尾相接，之间留有微小间隙。每段在10°C时长度为25.0米。混凝土的线膨胀系数为$\alpha = 1.0 \times 10^{-5} K^{-1}$。当温度达到40°C时，两段之间必须留有多大的最小间隙才能避免接触？

### Solution / 解答

**Step 1: Understand the problem / 步骤1：理解问题**
- **English:** Each section expands toward the gap. The total expansion of both sections must be accommodated by the gap.
- **中文:** 每段都向间隙方向膨胀。两段的总膨胀量必须由间隙容纳。

**Step 2: Calculate expansion of one section / 步骤2：计算一段的膨胀量**
$$\Delta T = 40 - 10 = 30^\circ C = 30 \text{ K}$$
$$\Delta L_{one} = \alpha L_0 \Delta T = (1.0 \times 10^{-5})(25.0)(30)$$
$$\Delta L_{one} = 7.5 \times 10^{-3} \text{ m} = 7.5 \text{ mm}$$

**Step 3: Calculate total expansion / 步骤3：计算总膨胀量**
- **English:** Both sections expand toward the gap, so total expansion = $2 \times \Delta L_{one}$
- **中文:** 两段都向间隙方向膨胀，所以总膨胀量 = $2 \times \Delta L_{one}$
$$\Delta L_{total} = 2 \times 7.5 = 15 \text{ mm}$$

### Final Answer / 最终答案
**Answer:** Minimum gap = 15 mm | **答案：** 最小间隙 = 15 毫米

### Quick Tip / 提示
- **English:** In gap problems, always consider which parts expand toward the gap. If both sides expand toward the gap, add their expansions.
- **中文:** 在间隙问题中，始终考虑哪些部分向间隙方向膨胀。如果两侧都向间隙膨胀，则相加它们的膨胀量。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Direct calculation of $\Delta L$ or $L$ | High / 高 | Easy / 简单 | 📝 *待填入* |
| Expansion gap problems | High / 高 | Medium / 中等 | 📝 *待填入* |
| Thermal stress problems | Medium / 中 | Medium-Hard / 中难 | 📝 *待填入* |
| Graph interpretation ($L$ vs $T$) | Low-Medium / 低-中 | Medium / 中等 | 📝 *待填入* |
| Material selection based on $\alpha$ | Low / 低 | Easy-Medium / 简单-中等 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, determine, find, state, explain, suggest, show that
- **中文:** 计算，确定，求出，说明，解释，建议，证明

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Linear expansion provides excellent opportunities for practical work in Papers 3 (CAIE) and Unit 1 (Edexcel):

1. **Measurement Techniques:** Use a micrometer screw gauge or travelling microscope to measure small changes in length ($\Delta L$ typically in mm or μm). A dial gauge is ideal for detecting tiny expansions.

2. **Temperature Measurement:** Use a thermometer or thermocouple to measure temperature changes accurately. Ensure the rod reaches thermal equilibrium before taking measurements.

3. **Experimental Design:** 
   - Heat a metal rod using steam or an electric heater
   - Measure expansion using a lever system to amplify small movements
   - Record temperature at regular intervals
   - Plot a graph of $\Delta L$ vs $\Delta T$ — the gradient gives $\alpha L_0$

4. **Uncertainties:** 
   - Length measurements: ±0.01 mm with micrometer
   - Temperature measurements: ±0.5°C with thermometer
   - Calculate percentage uncertainty in $\alpha$ from the gradient

5. **Error Analysis:**
   - Heat loss to surroundings (systematic error)
   - Non-uniform heating of the rod
   - Friction in the expansion measurement apparatus

**中文:**
线性膨胀为Paper 3（CAIE）和Unit 1（Edexcel）的实验工作提供了极好的机会：

1. **测量技术：** 使用千分尺或移动显微镜测量长度的微小变化（$\Delta L$通常以毫米或微米为单位）。千分表非常适合检测微小的膨胀。

2. **温度测量：** 使用温度计或热电偶准确测量温度变化。在进行测量前确保棒达到热平衡。

3. **实验设计：**
   - 使用蒸汽或电加热器加热金属棒
   - 使用杠杆系统放大微小运动来测量膨胀
   - 定期记录温度
   - 绘制$\Delta L$ vs $\Delta T$的图表——斜率给出$\alpha L_0$

4. **不确定度：**
   - 长度测量：千分尺±0.01毫米
   - 温度测量：温度计±0.5°C
   - 从斜率计算$\alpha$的百分比不确定度

5. **误差分析：**
   - 向周围环境的热损失（系统误差）
   - 棒的不均匀加热
   - 膨胀测量装置中的摩擦

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Concept
    LE[Linear Expansion] --> DEF[Definition: ΔL = αL₀ΔT]
    LE --> ALPHA[Coefficient α]
    LE --> FORMULA[Key Equations]
    
    %% Connections to prerequisites
    TEMP[[Temperature and Thermal Equilibrium]] --> LE
    
    %% Formula details
    FORMULA --> EQ1[ΔL = αL₀ΔT]
    FORMULA --> EQ2[L = L₀(1 + αΔT)]
    
    %% Alpha details
    ALPHA --> MAT[Material Property]
    ALPHA --> UNIT[Unit: K⁻¹ or °C⁻¹]
    ALPHA --> BOND[Depends on bond strength]
    
    %% Applications
    LE --> GAP[Expansion Gaps]
    LE --> STRESS[Thermal Stress]
    LE --> BIMET[[Bimetallic Strips and Thermostats]]
    
    %% Related topics
    LE --> AREA[[Area and Volume Expansion]]
    LE --> APPL[[Applications and Consequences of Thermal Expansion]]
    
    %% Practical
    LE --> PRACT[Practical Skills]
    PRACT --> MEAS[Measure ΔL with micrometer]
    PRACT --> GRAPH[Plot ΔL vs ΔT]
    
    %% Styling
    classDef core fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef related fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef practical fill:#e8f5e9,stroke:#1b5e20,stroke-width:1px
    
    class LE core
    class AREA,APPL,BIMET related
    class PRACT practical
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Linear expansion: length increase when temperature rises / 线性膨胀：温度升高时长度增加 |
| **Key Formula / 核心公式** | $\Delta L = \alpha L_0 \Delta T$; $L = L_0(1 + \alpha \Delta T)$ |
| **Coefficient $\alpha$ / 系数$\alpha$** | Material property; unit $K^{-1}$ or $^\circ C^{-1}$; typical values $10^{-6}$ to $10^{-5} K^{-1}$ / 材料属性；单位$K^{-1}$或$^\circ C^{-1}$；典型值$10^{-6}$到$10^{-5} K^{-1}$ |
| **Key Graph / 核心图表** | $L$ vs $T$: straight line, gradient = $\alpha L_0$, y-intercept = $L_0$ at $T=0$ / $L$ vs $T$：直线，斜率 = $\alpha L_0$，y轴截距 = $T=0$时的$L_0$ |
| **Common Application / 常见应用** | Expansion gaps in bridges/railways; bimetallic strips; thermostats / 桥梁/铁路的膨胀间隙；双金属片；恒温器 |
| **Exam Tip / 考试提示** | Use consistent units; $\Delta T$ in K or °C (same numerical value); $\Delta L$ usually in mm or μm / 使用一致的单位；$\Delta T$用K或°C（数值相同）；$\Delta L$通常以mm或μm为单位 |
| **Common Mistake / 常见错误** | Using $L$ instead of $L_0$ in formula; forgetting to multiply by $\alpha$; confusing $\alpha$ with $\beta$ or $\gamma$ / 公式中使用$L$而非$L_0$；忘记乘以$\alpha$；混淆$\alpha$与$\beta$或$\gamma$ |
| **Practical Skill / 实验技能** | Measure $\Delta L$ with micrometer/dial gauge; plot $\Delta L$ vs $\Delta T$; gradient gives $\alpha L_0$ / 用千分尺/千分表测量$\Delta L$；绘制$\Delta L$ vs $\Delta T$；斜率给出$\alpha L_0$ |