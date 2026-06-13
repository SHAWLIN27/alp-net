# 1. Overview / 概述

**English:**
The Boltzmann constant ($k_B$) is a fundamental physical constant that bridges the macroscopic world of ideal gases with the microscopic world of individual molecules. It appears in the [[Kinetic Theory of Gases]] as the proportionality constant linking the [[Mean Kinetic Energy and Temperature]] relationship. Specifically, $k_B$ relates the average translational kinetic energy of a single molecule to the absolute temperature: $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$. This constant is essential for understanding how temperature, a macroscopic property, emerges from the random motion of particles at the molecular level. In the context of [[Ideal Gases]], $k_B$ allows us to express the ideal gas law in terms of the number of molecules rather than moles: $pV = Nk_B T$, where $N$ is the total number of molecules.

**中文:**
玻尔兹曼常数 ($k_B$) 是一个基本物理常数，它连接了理想气体的宏观世界与单个分子的微观世界。在[[气体动理论]]中，它作为[[平均动能与温度]]关系中的比例常数出现。具体来说，$k_B$ 将单个分子的平均平动动能与绝对温度联系起来：$\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$。这个常数对于理解温度（一种宏观性质）如何从粒子在分子层面的随机运动中产生至关重要。在[[理想气体]]的背景下，$k_B$ 使我们能够用分子数而不是摩尔数来表达理想气体定律：$pV = Nk_B T$，其中 $N$ 是分子总数。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 11.2(a) Understand the concept of the Boltzmann constant | 5.23 Know that the Boltzmann constant is the gas constant per molecule |
| 11.2(b) Recall and use $pV = NkT$ | 5.24 Use the equation $pV = NkT$ |
| 11.2(c) Derive and use $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ | 5.25 Derive and use $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ |
| 11.2(d) Understand the relationship between Boltzmann constant and molar gas constant | 5.26 Understand that $k = R/N_A$ |
| 11.2(e) Use the Boltzmann constant in kinetic theory calculations | 5.27 Solve problems involving the Boltzmann constant |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to distinguish between $k_B$ (per molecule) and $R$ (per mole). They should be able to derive the relationship $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$ from the kinetic theory equation $pV = \frac{1}{3}Nm\langle c^2 \rangle$ and the ideal gas equation $pV = Nk_B T$. Common exam questions involve calculating the average kinetic energy of molecules at a given temperature or finding the temperature from kinetic energy data.
- **中文:** 学生必须能够区分 $k_B$（每个分子）和 $R$（每摩尔）。他们应该能够从气体动理论方程 $pV = \frac{1}{3}Nm\langle c^2 \rangle$ 和理想气体方程 $pV = Nk_B T$ 推导出关系式 $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$。常见的考试问题包括计算给定温度下分子的平均动能或从动能数据中找出温度。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Boltzmann Constant** / 玻尔兹曼常数 | The fundamental constant that relates the average kinetic energy of a molecule to its absolute temperature; $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$ | 将分子的平均动能与其绝对温度联系起来的基本常数；$k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$ | Confusing $k_B$ with $R$ (molar gas constant). Remember: $k_B$ is per molecule, $R$ is per mole. |
| **Molar Gas Constant** / 摩尔气体常数 | The gas constant per mole of gas; $R = 8.31 \text{ J mol}^{-1} \text{ K}^{-1}$ | 每摩尔气体的气体常数；$R = 8.31 \text{ J mol}^{-1} \text{ K}^{-1}$ | Forgetting the relationship $R = N_A k_B$ where $N_A$ is [[Avogadro's Number]]. |
| **Mean Translational Kinetic Energy** / 平均平动动能 | The average kinetic energy of a molecule due to its random translational motion; $\langle E_K \rangle = \frac{3}{2}k_B T$ | 分子由于其随机平动运动而具有的平均动能；$\langle E_K \rangle = \frac{3}{2}k_B T$ | Thinking this includes rotational or vibrational energy — it only accounts for translational motion in a monatomic ideal gas. |
| **Absolute Temperature** / 绝对温度 | Temperature measured on the Kelvin scale, proportional to the mean kinetic energy of molecules | 以开尔文温标测量的温度，与分子的平均动能成正比 | Using Celsius instead of Kelvin in calculations involving $k_B$. |
| **Number of Molecules** / 分子数 | The total number of individual molecules in a gas sample; $N = nN_A$ | 气体样品中单个分子的总数；$N = nN_A$ | Confusing $N$ (number of molecules) with $n$ (number of moles). |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Boltzmann Constant as a Bridge / 玻尔兹曼常数作为桥梁

### Explanation / 解释
**English:** The Boltzmann constant $k_B$ serves as a conversion factor between the macroscopic world (temperature) and the microscopic world (molecular kinetic energy). When we say a gas is at temperature $T$, we are really describing the average kinetic energy of its molecules. The constant $k_B$ tells us exactly how much energy corresponds to each degree of temperature. For a monatomic ideal gas, each molecule has, on average, $\frac{3}{2}k_B T$ of translational kinetic energy. This means that at room temperature (about 300 K), each molecule has approximately $6.21 \times 10^{-21} \text{ J}$ of kinetic energy — an incredibly small amount, which explains why we don't feel individual molecular impacts.

The relationship between $k_B$ and the molar gas constant $R$ is: $k_B = \frac{R}{N_A}$, where $N_A = 6.02 \times 10^{23} \text{ mol}^{-1}$ is [[Avogadro's Number]]. This makes sense because $R$ is the energy per mole per Kelvin, and dividing by the number of molecules per mole gives the energy per molecule per Kelvin.

**中文:** 玻尔兹曼常数 $k_B$ 作为宏观世界（温度）和微观世界（分子动能）之间的转换因子。当我们说气体处于温度 $T$ 时，我们实际上是在描述其分子的平均动能。常数 $k_B$ 告诉我们每个温度单位对应多少能量。对于单原子理想气体，每个分子平均具有 $\frac{3}{2}k_B T$ 的平动动能。这意味着在室温（约 300 K）下，每个分子具有大约 $6.21 \times 10^{-21} \text{ J}$ 的动能——这是一个极其微小的量，这解释了为什么我们感觉不到单个分子的撞击。

$k_B$ 与摩尔气体常数 $R$ 之间的关系是：$k_B = \frac{R}{N_A}$，其中 $N_A = 6.02 \times 10^{23} \text{ mol}^{-1}$ 是[[阿伏伽德罗常数]]。这是合理的，因为 $R$ 是每摩尔每开尔文的能量，除以每摩尔的分子数就得到每个分子每开尔文的能量。

### Physical Meaning / 物理意义
**English:** The Boltzmann constant quantifies the fundamental relationship between energy and temperature at the molecular level. It tells us that temperature is not just a number on a thermometer — it is a direct measure of the average random kinetic energy of particles. A temperature of 0 K (absolute zero) corresponds to the state where particles have minimum possible kinetic energy.

**中文:** 玻尔兹曼常数量化了分子水平上能量与温度之间的基本关系。它告诉我们，温度不仅仅是温度计上的一个数字——它是粒子平均随机动能的直接度量。0 K（绝对零度）对应于粒子具有最小可能动能的状态。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking $k_B$ is only for gases — it applies to any system in thermal equilibrium
  - Confusing $k_B$ with Boltzmann's constant in the Stefan-Boltzmann law (different constant)
  - Believing that $\frac{3}{2}k_B T$ represents total internal energy — it only represents translational kinetic energy for monatomic gases
- **中文:**
  - 认为 $k_B$ 只适用于气体——它适用于任何处于热平衡的系统
  - 将 $k_B$ 与斯特藩-玻尔兹曼定律中的玻尔兹曼常数混淆（不同的常数）
  - 认为 $\frac{3}{2}k_B T$ 代表总内能——它只代表单原子气体的平动动能

### Exam Tips / 考试提示
- **English:** Always convert Celsius to Kelvin before using $k_B$. Remember the value $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$ — you may need to recall it or use it from a data booklet. When calculating the number of molecules, use $N = nN_A$ where $n$ is the number of moles.
- **中文:** 在使用 $k_B$ 之前，务必将摄氏度转换为开尔文。记住 $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$ 的值——你可能需要回忆它或从数据手册中使用它。计算分子数时，使用 $N = nN_A$，其中 $n$ 是摩尔数。

> 📷 **IMAGE PROMPT — KB01: Boltzmann Constant as a Bridge**
> A visual diagram showing a bridge connecting two worlds: on the left, a macroscopic thermometer showing temperature T (K); on the right, microscopic molecules with arrows showing motion. In the center, a large "k_B" symbol with arrows pointing both ways. Labels: "Macroscopic: Temperature T" on left, "Microscopic: Kinetic Energy ½mv²" on right. The bridge is labeled "k_B = 1.38 × 10⁻²³ J/K". Clean, educational style with blue and orange color scheme.

---

# 5. Essential Equations / 核心公式

## Equation 1: Ideal Gas Law with Boltzmann Constant

$$ pV = Nk_B T $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $p$ | Pressure of the gas | 气体的压强 | Pa |
| $V$ | Volume of the gas | 气体的体积 | m³ |
| $N$ | Number of molecules | 分子数 | dimensionless |
| $k_B$ | Boltzmann constant ($1.38 \times 10^{-23}$) | 玻尔兹曼常数 | J K⁻¹ |
| $T$ | Absolute temperature | 绝对温度 | K |

**Derivation / 推导:** From $pV = nRT$ and $n = \frac{N}{N_A}$, we get $pV = \frac{N}{N_A}RT = N\left(\frac{R}{N_A}\right)T = Nk_B T$.

**Conditions / 适用条件:** Ideal gases only; low pressure, high temperature relative to critical point.

**Limitations / 局限性:** Does not account for intermolecular forces or molecular volume; fails at high pressures and low temperatures.

## Equation 2: Mean Kinetic Energy

$$ \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $m$ | Mass of one molecule | 一个分子的质量 | kg |
| $\langle c^2 \rangle$ | Mean square speed | 均方速度 | m² s⁻² |
| $k_B$ | Boltzmann constant | 玻尔兹曼常数 | J K⁻¹ |
| $T$ | Absolute temperature | 绝对温度 | K |

**Derivation / 推导:** From [[Derivation of pV = (1/3)Nm(c_rms)^2]]: $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Substituting $pV = Nk_B T$ gives $\frac{1}{3}Nm\langle c^2 \rangle = Nk_B T$. Cancelling $N$: $\frac{1}{3}m\langle c^2 \rangle = k_B T$. Multiplying both sides by $\frac{3}{2}$: $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$.

**Conditions / 适用条件:** Monatomic ideal gases; assumes only translational kinetic energy.

**Limitations / 局限性:** For diatomic or polyatomic gases, additional energy is stored in rotational and vibrational modes.

## Equation 3: Relationship between $k_B$ and $R$

$$ k_B = \frac{R}{N_A} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $k_B$ | Boltzmann constant | 玻尔兹曼常数 | J K⁻¹ |
| $R$ | Molar gas constant ($8.31$) | 摩尔气体常数 | J mol⁻¹ K⁻¹ |
| $N_A$ | Avogadro's number ($6.02 \times 10^{23}$) | 阿伏伽德罗常数 | mol⁻¹ |

**Derivation / 推导:** $R$ is the gas constant per mole; $k_B$ is the gas constant per molecule. Since there are $N_A$ molecules in one mole, $R = N_A k_B$.

**Conditions / 适用条件:** Universal relationship, always true.

> 📷 **IMAGE PROMPT — KB02: Key Equations Summary**
> A clean formula card showing three equations: (1) pV = NkT, (2) ½m⟨c²⟩ = ³⁄₂kT, (3) k = R/N_A. Each equation in a separate box with color coding. Arrows showing derivation flow from equation 1 to equation 2. Include the value k_B = 1.38 × 10⁻²³ J/K prominently. Educational infographic style with white background and blue/black text.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Mean Kinetic Energy vs Temperature / 平均动能与温度的关系

### Axes / 坐标轴
- **X-axis:** Temperature $T$ (K) / 温度 $T$ (K)
- **Y-axis:** Mean kinetic energy $\langle E_K \rangle$ (J) / 平均动能 $\langle E_K \rangle$ (J)

### Shape / 形状
A straight line through the origin with gradient $\frac{3}{2}k_B$.

### Gradient Meaning / 斜率含义
The gradient $\frac{3}{2}k_B$ represents the increase in mean kinetic energy per unit increase in temperature for each molecule.

### Area Meaning / 面积含义
No meaningful area under this graph.

### Exam Interpretation / 考试解读
- **English:** A linear relationship confirms that temperature is proportional to mean kinetic energy. The graph passes through the origin, showing that at 0 K, molecules have zero kinetic energy (classical view). The steeper the gradient, the larger the Boltzmann constant.
- **中文:** 线性关系证实了温度与平均动能成正比。图形通过原点，表明在 0 K 时，分子具有零动能（经典观点）。斜率越陡，玻尔兹曼常数越大。

## 6.2 $pV$ vs $N$ for Constant Temperature / 恒定温度下 $pV$ 与 $N$ 的关系

### Axes / 坐标轴
- **X-axis:** Number of molecules $N$ / 分子数 $N$
- **Y-axis:** $pV$ (J) / $pV$ (J)

### Shape / 形状
A straight line through the origin with gradient $k_B T$.

### Gradient Meaning / 斜率含义
The gradient $k_B T$ represents the product of Boltzmann constant and temperature. For a fixed temperature, this gradient is constant.

### Exam Interpretation / 考试解读
- **English:** This graph demonstrates that $pV$ is directly proportional to the number of molecules at constant temperature. The gradient can be used to determine $k_B$ if $T$ is known, or $T$ if $k_B$ is known.
- **中文:** 该图表明，在恒定温度下，$pV$ 与分子数成正比。如果已知 $T$，可以用斜率确定 $k_B$；如果已知 $k_B$，可以用斜率确定 $T$。

---

# 7. Required Diagrams / 必备图表

## 7.1 Derivation Flowchart / 推导流程图

### Description / 描述
**English:** A flowchart showing the step-by-step derivation of $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$ from the kinetic theory equation and the ideal gas law.
**中文:** 一个流程图，展示从气体动理论方程和理想气体定律逐步推导 $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$ 的过程。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — KB03: Derivation Flowchart**
> A clean flowchart with 4 boxes connected by arrows. Box 1: "pV = ⅓Nm⟨c²⟩" (Kinetic Theory). Box 2: "pV = NkT" (Ideal Gas Law). Arrow from both boxes pointing to Box 3: "⅓Nm⟨c²⟩ = NkT". Box 4: "Cancel N → ⅓m⟨c²⟩ = kT". Box 5: "Multiply by ³⁄₂ → ½m⟨c²⟩ = ³⁄₂kT". Each box has a brief explanation below it. Educational style, blue boxes with white text, arrows in orange.

### Labels Required / 需要标注
- Kinetic theory equation / 气体动理论方程
- Ideal gas law with Boltzmann constant / 含玻尔兹曼常数的理想气体定律
- Cancellation of $N$ / 消去 $N$
- Final result / 最终结果

### Exam Importance / 考试重要性
- **English:** This derivation is frequently tested in both CAIE and Edexcel exams. Students must be able to reproduce it step by step.
- **中文:** 这个推导在 CAIE 和 Edexcel 考试中经常被考到。学生必须能够逐步重现它。

## 7.2 Energy Distribution at Different Temperatures / 不同温度下的能量分布

### Description / 描述
**English:** A graph showing the Maxwell-Boltzmann distribution of molecular speeds at two different temperatures, illustrating how higher temperature increases the proportion of molecules with higher kinetic energy.
**中文:** 一个显示两种不同温度下分子速度的麦克斯韦-玻尔兹曼分布的图表，说明较高温度如何增加具有较高动能的分子比例。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — KB04: Maxwell-Boltzmann Distribution**
> A graph with two curves: one at lower temperature T₁ (blue, taller and narrower) and one at higher temperature T₂ > T₁ (red, shorter and wider). X-axis labeled "Molecular Speed / m s⁻¹", Y-axis labeled "Number of Molecules". Both curves start at origin, rise to a peak, then decay asymptotically to zero. The area under both curves is equal. Labels: "T₁" and "T₂" on respective curves. A vertical dashed line shows the most probable speed shifting right at higher temperature.

### Labels Required / 需要标注
- Temperature $T_1$ (lower) / 温度 $T_1$（较低）
- Temperature $T_2$ (higher) / 温度 $T_2$（较高）
- Most probable speed / 最概然速度
- Mean speed / 平均速度
- [[Root Mean Square Speed]] / 均方根速度

### Exam Importance / 考试重要性
- **English:** Understanding this distribution helps explain why the Boltzmann constant relates average energy to temperature — not all molecules have the same energy, but the average follows $\frac{3}{2}k_B T$.
- **中文:** 理解这个分布有助于解释为什么玻尔兹曼常数将平均能量与温度联系起来——并非所有分子都具有相同的能量，但平均值遵循 $\frac{3}{2}k_B T$。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Mean Kinetic Energy / 计算平均动能

### Question / 题目
**English:**
A sample of helium gas is at a temperature of 27°C. Calculate:
(a) The mean translational kinetic energy of a helium atom.
(b) The total translational kinetic energy of all atoms in 0.5 moles of helium.
(Given: $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$, $N_A = 6.02 \times 10^{23} \text{ mol}^{-1}$)

**中文:**
一氦气样品温度为 27°C。计算：
(a) 一个氦原子的平均平动动能。
(b) 0.5 摩尔氦中所有原子的总平动动能。
（已知：$k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$，$N_A = 6.02 \times 10^{23} \text{ mol}^{-1}$）

### Solution / 解答

**Part (a):**
1. Convert temperature to Kelvin: $T = 27 + 273 = 300 \text{ K}$
2. Use $\langle E_K \rangle = \frac{3}{2}k_B T$
3. $\langle E_K \rangle = \frac{3}{2} \times (1.38 \times 10^{-23}) \times 300$
4. $\langle E_K \rangle = \frac{3}{2} \times 4.14 \times 10^{-21}$
5. $\langle E_K \rangle = 6.21 \times 10^{-21} \text{ J}$

**Part (b):**
1. Number of atoms: $N = nN_A = 0.5 \times 6.02 \times 10^{23} = 3.01 \times 10^{23}$
2. Total kinetic energy: $E_{\text{total}} = N \times \langle E_K \rangle$
3. $E_{\text{total}} = (3.01 \times 10^{23}) \times (6.21 \times 10^{-21})$
4. $E_{\text{total}} = 1.87 \times 10^3 \text{ J}$

### Final Answer / 最终答案
**Answer:** (a) $6.21 \times 10^{-21} \text{ J}$ | **答案：** (a) $6.21 \times 10^{-21} \text{ J}$
**Answer:** (b) $1.87 \times 10^3 \text{ J}$ | **答案：** (b) $1.87 \times 10^3 \text{ J}$

### Quick Tip / 提示
**English:** Always convert Celsius to Kelvin first! The Boltzmann constant has units of J K⁻¹, so temperature must be in Kelvin. For part (b), remember that total energy = number of molecules × average energy per molecule.
**中文:** 始终先将摄氏度转换为开尔文！玻尔兹曼常数的单位是 J K⁻¹，所以温度必须是开尔文。对于 (b) 部分，记住总能量 = 分子数 × 每个分子的平均能量。

## Example 2: Finding Temperature from Kinetic Energy / 从动能求温度

### Question / 题目
**English:**
The mean translational kinetic energy of molecules in a gas is $8.28 \times 10^{-21} \text{ J}$. Calculate the temperature of the gas.
(Given: $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$)

**中文:**
气体中分子的平均平动动能为 $8.28 \times 10^{-21} \text{ J}$。计算气体的温度。
（已知：$k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$）

### Solution / 解答
1. Use $\langle E_K \rangle = \frac{3}{2}k_B T$
2. Rearrange for $T$: $T = \frac{2\langle E_K \rangle}{3k_B}$
3. $T = \frac{2 \times (8.28 \times 10^{-21})}{3 \times (1.38 \times 10^{-23})}$
4. $T = \frac{1.656 \times 10^{-20}}{4.14 \times 10^{-23}}$
5. $T = 400 \text{ K}$

### Final Answer / 最终答案
**Answer:** $400 \text{ K}$ | **答案：** $400 \text{ K}$

### Quick Tip / 提示
**English:** Notice that the answer is in Kelvin. If the question asks for temperature in Celsius, subtract 273. The relationship $\langle E_K \rangle \propto T$ means that doubling the kinetic energy doubles the absolute temperature.
**中文:** 注意答案是以开尔文为单位的。如果问题要求以摄氏度为单位的温度，减去 273。关系 $\langle E_K \rangle \propto T$ 意味着动能加倍，绝对温度也加倍。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate mean kinetic energy from temperature | High | Easy | 📝 *待填入* |
| Derive $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$ | High | Medium | 📝 *待填入* |
| Calculate temperature from kinetic energy data | Medium | Easy | 📝 *待填入* |
| Use $pV = Nk_B T$ with number of molecules | Medium | Medium | 📝 *待填入* |
| Relate $k_B$ to $R$ and $N_A$ | Low | Easy | 📝 *待填入* |
| Combined problems with [[Root Mean Square Speed]] | Medium | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Derive, Show that, Determine, State, Explain
- **中文:** 计算，推导，证明，确定，写出，解释

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
The Boltzmann constant connects to practical work in several ways:

1. **Measurement of $k_B$:** In advanced practical setups, students can determine $k_B$ by measuring the pressure, volume, and temperature of a known number of gas molecules using $pV = Nk_B T$.

2. **Uncertainty Analysis:** When calculating mean kinetic energy, uncertainties in temperature measurement propagate. For example, if $T = 300 \pm 1 \text{ K}$, the uncertainty in $\langle E_K \rangle$ is $\frac{3}{2}k_B \times \Delta T = 2.07 \times 10^{-23} \text{ J}$.

3. **Graphical Methods:** Plotting $pV$ against $N$ for constant $T$ gives a straight line with gradient $k_B T$, allowing experimental determination of $k_B$.

4. **Brownian Motion Observation:** While not directly measuring $k_B$, observing Brownian motion provides visual evidence of the molecular motion that $k_B$ quantifies.

**中文:**
玻尔兹曼常数通过以下几种方式与实验工作相关联：

1. **测量 $k_B$：** 在高级实验设置中，学生可以通过使用 $pV = Nk_B T$ 测量已知分子数的气体的压强、体积和温度来确定 $k_B$。

2. **不确定度分析：** 计算平均动能时，温度测量的不确定度会传播。例如，如果 $T = 300 \pm 1 \text{ K}$，则 $\langle E_K \rangle$ 的不确定度为 $\frac{3}{2}k_B \times \Delta T = 2.07 \times 10^{-23} \text{ J}$。

3. **图形方法：** 在恒定 $T$ 下绘制 $pV$ 与 $N$ 的关系图，得到一条斜率为 $k_B T$ 的直线，从而可以通过实验确定 $k_B$。

4. **布朗运动观察：** 虽然不能直接测量 $k_B$，但观察布朗运动为 $k_B$ 量化的分子运动提供了视觉证据。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main node
    KB["Boltzmann Constant (k_B)
    玻尔兹曼常数
    k_B = 1.38 × 10⁻²³ J/K"]

    %% Connections to parent hub
    KTG["[[Kinetic Theory of Gases]]
    气体动理论"]
    
    %% Connections to sibling sub-topics
    MKE["[[Mean Kinetic Energy and Temperature]]
    平均动能与温度"]
    RMS["[[Root Mean Square Speed]]
    均方根速度"]
    DERIV["[[Derivation of pV = (1/3)Nm(c_rms)^2]]
    pV = (1/3)Nm(c_rms)² 推导"]
    ASSUM["[[Kinetic Theory Assumptions]]
    气体动理论假设"]

    %% Connections to prerequisites
    IG["[[Ideal Gases]]
    理想气体"]
    AVO["[[Avogadro's Number]]
    阿伏伽德罗常数"]

    %% Connections to related topics
    IE["[[Internal Energy and the First Law]]
    内能与热力学第一定律"]

    %% Relationships
    KTG --> KB
    KB --> MKE
    KB --> RMS
    DERIV --> KB
    ASSUM --> DERIV
    IG --> KB
    AVO --> KB
    KB --> IE
    
    %% Equation relationships
    MKE ---|"⟨E_K⟩ = ³⁄₂k_B T"| RMS
    DERIV ---|"pV = ⅓Nm⟨c²⟩"| IG
    KB ---|"k_B = R/N_A"| AVO
    
    %% Styling
    classDef main fill:#e74c3c,stroke:#c0392b,color:white
    classDef hub fill:#2980b9,stroke:#2471a3,color:white
    classDef sibling fill:#27ae60,stroke:#229954,color:white
    classDef prereq fill:#f39c12,stroke:#d68910,color:white
    classDef related fill:#8e44ad,stroke:#7d3c98,color:white
    
    class KB main
    class KTG hub
    class MKE,RMS,DERIV,ASSUM sibling
    class IG,AVO prereq
    class IE related
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$ — energy per molecule per Kelvin / 每个分子每开尔文的能量 |
| **Key Formula / 核心公式** | $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$ — mean translational KE per molecule / 每个分子的平均平动动能 |
| **Key Formula / 核心公式** | $pV = Nk_B T$ — ideal gas law with number of molecules / 含分子数的理想气体定律 |
| **Key Formula / 核心公式** | $k_B = \frac{R}{N_A}$ — relationship to molar gas constant / 与摩尔气体常数的关系 |
| **Key Graph / 核心图表** | $\langle E_K \rangle$ vs $T$: straight line through origin, gradient $\frac{3}{2}k_B$ / 通过原点的直线，斜率 $\frac{3}{2}k_B$ |
| **Key Graph / 核心图表** | $pV$ vs $N$: straight line through origin, gradient $k_B T$ / 通过原点的直线，斜率 $k_B T$ |
| **Exam Tip / 考试提示** | Always convert °C to K before using $k_B$ / 使用 $k_B$ 前务必将 °C 转换为 K |
| **Exam Tip / 考试提示** | Derivation: $pV = \frac{1}{3}Nm\langle c^2 \rangle$ + $pV = Nk_B T$ → $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}k_B T$ / 推导过程 |
| **Common Mistake / 常见错误** | Confusing $k_B$ (per molecule) with $R$ (per mole) / 混淆 $k_B$（每个分子）和 $R$（每摩尔） |
| **Common Mistake / 常见错误** | Using $\frac{3}{2}k_B T$ for total internal energy of diatomic gases / 对双原子气体使用 $\frac{3}{2}k_B T$ 作为总内能 |
| **Numerical Value / 数值** | $k_B = 1.38 \times 10^{-23} \text{ J K}^{-1}$ (memorize for CAIE) / 记住此值（CAIE 需要） |
| **Numerical Value / 数值** | $R = 8.31 \text{ J mol}^{-1} \text{ K}^{-1}$, $N_A = 6.02 \times 10^{23} \text{ mol}^{-1}$ / 相关常数 |