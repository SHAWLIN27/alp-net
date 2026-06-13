---
# Using the H-R Diagram to Determine Stellar Properties / 利用赫罗图确定恒星性质

---

# 1. Overview / 概述

**English:**
This sub-topic explores how the Hertzsprung-Russell (H-R) diagram, a plot of stellar luminosity against surface temperature, can be used as a powerful diagnostic tool to determine fundamental stellar properties. By locating a star on the H-R diagram, we can deduce its radius, mass, and evolutionary stage. This sub-topic focuses on the quantitative relationships derived from the diagram, particularly the Stefan-Boltzmann law for radius determination and the mass-luminosity relation for main sequence stars. Understanding these techniques is crucial for interpreting stellar observations and linking them to theoretical models of [[Stellar Evolution]].

**中文:**
本子知识点探讨如何利用赫罗图（H-R图，即恒星光度与表面温度的关系图）作为强大的诊断工具来确定恒星的基本性质。通过在赫罗图上定位一颗恒星，我们可以推断出其半径、质量以及演化阶段。本子知识点侧重于从该图推导出的定量关系，特别是用于确定半径的斯特藩-玻尔兹曼定律，以及用于主序星的质量-光度关系。理解这些技术对于解释恒星观测结果并将其与[[恒星演化]]的理论模型联系起来至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 25.3(a) Show an understanding that the Hertzsprung-Russell (H-R) diagram is a plot of luminosity against temperature. | 10.13 Understand the use of the Hertzsprung-Russell (H-R) diagram to determine stellar properties. |
| 25.3(b) Use the H-R diagram to determine the radius of a star from its luminosity and temperature. | 10.14 Use the Stefan-Boltzmann law to determine the radius of a star from its luminosity and temperature. |
| 25.3(c) Use the H-R diagram to determine the mass of a main sequence star from its luminosity. | 10.15 Understand the mass-luminosity relation for main sequence stars. |
| 25.3(d) Use the H-R diagram to determine the evolutionary stage of a star. | 10.16 Use the H-R diagram to determine the evolutionary stage of a star. |
| 25.3(e) Show an understanding that the H-R diagram can be used to estimate stellar distances using spectroscopic parallax. | 10.17 Understand the concept of spectroscopic parallax to estimate stellar distances. |
| 25.3(f) Use the H-R diagram to determine the distance to a star using spectroscopic parallax. | 10.18 Use the H-R diagram to determine the distance to a star using spectroscopic parallax. |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to apply the Stefan-Boltzmann law ($L = 4\pi r^2 \sigma T^4$) to compare stars on the H-R diagram. They should be able to read values from a given H-R diagram and use them in calculations. For main sequence stars, the mass-luminosity relation ($L \propto M^{3.5}$) is a key tool. Students must also understand the logic of spectroscopic parallax: using the H-R diagram to estimate a star's absolute magnitude from its spectral class, then applying the distance modulus equation to find its distance.
- **中文:** 学生必须能够应用斯特藩-玻尔兹曼定律 ($L = 4\pi r^2 \sigma T^4$) 来比较赫罗图上的恒星。他们应能从给定的赫罗图中读取数值并用于计算。对于主序星，质量-光度关系 ($L \propto M^{3.5}$) 是一个关键工具。学生还必须理解分光视差的逻辑：利用赫罗图从恒星的光谱型估计其绝对星等，然后应用距离模数方程求出其距离。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Luminosity** / 光度 | The total power (energy per second) radiated by a star. | 恒星每秒辐射的总能量（功率）。 | Confusing luminosity with apparent brightness. Luminosity is an intrinsic property, not dependent on distance. |
| **Stefan-Boltzmann Law** / 斯特藩-玻尔兹曼定律 | The law stating that the power radiated per unit area of a black body is proportional to the fourth power of its absolute temperature: $L = 4\pi r^2 \sigma T^4$. | 该定律指出黑体单位面积辐射的功率与其绝对温度的四次方成正比：$L = 4\pi r^2 \sigma T^4$。 | Forgetting the $4\pi r^2$ factor (surface area of a sphere). |
| **Mass-Luminosity Relation** / 质量-光度关系 | An empirical relationship for main sequence stars stating that luminosity is proportional to mass raised to the power of approximately 3.5: $L \propto M^{3.5}$. | 主序星的经验关系，指出光度与质量的约3.5次方成正比：$L \propto M^{3.5}$。 | Applying this relation to non-main-sequence stars (giants, white dwarfs). |
| **Spectroscopic Parallax** / 分光视差 | A method for estimating the distance to a star by comparing its apparent magnitude with its absolute magnitude, where the absolute magnitude is estimated from its spectral class using the H-R diagram. | 一种通过比较恒星的视星等和绝对星等来估计其距离的方法，其中绝对星等是利用赫罗图从其光谱型估计出来的。 | Thinking it involves actual parallax measurements. It is a *spectroscopic* method, not a geometric one. |
| **Distance Modulus** / 距离模数 | The difference between a star's apparent magnitude ($m$) and its absolute magnitude ($M$), related to its distance ($d$) by $m - M = 5 \log_{10}(d/10)$. | 恒星的视星等 ($m$) 与其绝对星等 ($M$) 之差，通过 $m - M = 5 \log_{10}(d/10)$ 与其距离 ($d$) 相关联。 | Forgetting the units of distance (parsecs) in the formula. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Determining Radius from the H-R Diagram / 从赫罗图确定半径

### Explanation / 解释
**English:** The H-R diagram plots luminosity ($L$) against temperature ($T$). The Stefan-Boltzmann law links these two quantities to a star's radius ($r$): $L = 4\pi r^2 \sigma T^4$. This means that lines of constant radius (isoradius lines) can be drawn on the H-R diagram. These are diagonal lines running from the top-left (high $L$, high $T$) to the bottom-right (low $L$, low $T$). A star's position relative to these lines tells us its radius. For example, a star with the same temperature as the Sun but a much higher luminosity must have a larger radius (a giant). Conversely, a star with the same temperature but a much lower luminosity must have a smaller radius (a white dwarf). This is the key to understanding the different regions of the [[H-R Diagram Axes and Regions]].

**中文:** 赫罗图绘制了光度 ($L$) 与温度 ($T$) 的关系。斯特藩-玻尔兹曼定律将这两个量与恒星的半径 ($r$) 联系起来：$L = 4\pi r^2 \sigma T^4$。这意味着可以在赫罗图上画出等半径线。这些是对角线，从左上角（高 $L$，高 $T$）延伸到右下角（低 $L$，低 $T$）。恒星相对于这些线的位置告诉我们它的半径。例如，一颗与太阳温度相同但光度高得多的恒星，其半径一定更大（一颗巨星）。相反，一颗温度相同但光度低得多的恒星，其半径一定更小（一颗白矮星）。这是理解[[赫罗图坐标轴与区域]]不同区域的关键。

### Physical Meaning / 物理意义
**English:** The radius determines the surface area available for radiating energy. A larger star has more surface area, so it can emit more total power (luminosity) even if its surface temperature is lower. The H-R diagram visually separates stars by their size.
**中文:** 半径决定了可用于辐射能量的表面积。更大的恒星拥有更大的表面积，因此即使其表面温度较低，也能辐射出更多的总功率（光度）。赫罗图直观地根据恒星的大小将其区分开来。

### Common Misconceptions / 常见误区
- **English:** Thinking that a hotter star is always more luminous. A cool supergiant can be far more luminous than a hot white dwarf because of its enormous size.
- **中文:** 认为更热的恒星总是更亮。一颗冷的超巨星可能比一颗热的白矮星亮得多，因为它巨大的体积。
- **English:** Confusing the Stefan-Boltzmann constant ($\sigma$) with the Stefan-Boltzmann *law*.
- **中文:** 混淆斯特藩-玻尔兹曼常数 ($\sigma$) 与斯特藩-玻尔兹曼*定律*。

### Exam Tips / 考试提示
- **English:** When comparing two stars, use the ratio form of the Stefan-Boltzmann law: $\frac{L_1}{L_2} = \left(\frac{r_1}{r_2}\right)^2 \left(\frac{T_1}{T_2}\right)^4$. This avoids needing the constant.
- **中文:** 比较两颗恒星时，使用斯特藩-玻尔兹曼定律的比例形式：$\frac{L_1}{L_2} = \left(\frac{r_1}{r_2}\right)^2 \left(\frac{T_1}{T_2}\right)^4$。这样可以避免使用常数。

> 📷 **IMAGE PROMPT — DIAGRAM-01: H-R Diagram with Isoradius Lines**
> A standard Hertzsprung-Russell diagram with luminosity on the y-axis (in solar units) and temperature on the x-axis (decreasing to the right). Three diagonal dashed lines are drawn, labeled "10 R☉", "1 R☉", and "0.1 R☉". The Sun is marked on the "1 R☉" line. A red giant star is shown in the top-right, lying on the "10 R☉" line. A white dwarf is shown in the bottom-left, lying on the "0.1 R☉" line. Arrows indicate the direction of increasing radius.

## 4.2 Determining Mass from the H-R Diagram / 从赫罗图确定质量

### Explanation / 解释
**English:** For [[Main Sequence Stars]], there is a strong empirical relationship between their mass and their luminosity. This is the mass-luminosity relation: $L \propto M^{3.5}$. This means that a main sequence star's position on the H-R diagram (specifically its luminosity) directly tells us its mass. More massive main sequence stars are much more luminous and are found at the top-left of the main sequence. Less massive stars are much fainter and are found at the bottom-right. This relation does *not* apply to giants, supergiants, or white dwarfs, as their luminosity is determined more by their radius than their mass.

**中文:** 对于[[主序星]]，其质量与光度之间存在一个很强的经验关系。这就是质量-光度关系：$L \propto M^{3.5}$。这意味着主序星在赫罗图上的位置（特别是其光度）直接告诉我们它的质量。质量更大的主序星光度更高，位于主序带的左上角。质量较小的恒星光度更暗，位于主序带的右下角。这个关系*不*适用于巨星、超巨星或白矮星，因为这些恒星的光度更多地取决于它们的半径而非质量。

### Physical Meaning / 物理意义
**English:** The mass of a main sequence star determines its core pressure and temperature, which in turn dictates the rate of nuclear fusion. Higher mass leads to higher core temperature and a much faster fusion rate, hence a much higher luminosity.
**中文:** 主序星的质量决定了其核心的压力和温度，这反过来又决定了核聚变的速率。更高的质量导致更高的核心温度和更快的聚变速率，从而产生更高的光度。

### Common Misconceptions / 常见误区
- **English:** Applying the $L \propto M^{3.5}$ relation to all stars. It is only valid for main sequence stars.
- **中文:** 将 $L \propto M^{3.5}$ 关系应用于所有恒星。它仅对主序星有效。
- **English:** Forgetting that the exponent is approximately 3.5, not 1 or 2.
- **中文:** 忘记指数大约是3.5，而不是1或2。

### Exam Tips / 考试提示
- **English:** If a question asks for the mass ratio of two main sequence stars, use the ratio form: $\frac{L_1}{L_2} = \left(\frac{M_1}{M_2}\right)^{3.5}$.
- **中文:** 如果问题要求两个主序星的质量比，使用比例形式：$\frac{L_1}{L_2} = \left(\frac{M_1}{M_2}\right)^{3.5}$。

## 4.3 Determining Distance: Spectroscopic Parallax / 确定距离：分光视差

### Explanation / 解释
**English:** Spectroscopic parallax is a method to estimate the distance to a star. It does *not* involve measuring a geometric parallax angle. The steps are:
1.  **Obtain the spectrum** of the star to determine its spectral class (e.g., G2).
2.  **Use the H-R diagram** to find the absolute magnitude ($M$) for a main sequence star of that spectral class. This assumes the star is on the main sequence.
3.  **Measure the apparent magnitude** ($m$) of the star.
4.  **Apply the distance modulus equation:** $m - M = 5 \log_{10}(d/10)$, where $d$ is the distance in parsecs. Solve for $d$.

This method is crucial for stars too far away for geometric parallax to be effective. It links [[Spectral Classes (OBAFGKM)]] directly to [[Stellar Distances]].

**中文:** 分光视差是一种估计恒星距离的方法。它*不*涉及测量几何视差角。步骤如下：
1.  **获取恒星的光谱** 以确定其光谱型（例如，G2）。
2.  **使用赫罗图** 找出该光谱型主序星的绝对星等 ($M$)。这假设该恒星在主序带上。
3.  **测量恒星的视星等** ($m$)。
4.  **应用距离模数方程：** $m - M = 5 \log_{10}(d/10)$，其中 $d$ 是以秒差距为单位的距离。求解 $d$。

这种方法对于几何视差无法有效测量的遥远恒星至关重要。它将[[光谱型 (OBAFGKM)]] 与[[恒星距离]]直接联系起来。

### Physical Meaning / 物理意义
**English:** The method relies on the fact that all main sequence stars of a given spectral class have approximately the same intrinsic luminosity (and hence absolute magnitude). By comparing how bright they appear (apparent magnitude) to how bright they truly are (absolute magnitude), we can calculate how far away they must be.
**中文:** 该方法依赖于这样一个事实：所有给定光谱型的主序星都具有大致相同的内禀光度（因此也具有相同的绝对星等）。通过比较它们看起来有多亮（视星等）和它们实际上有多亮（绝对星等），我们可以计算出它们必须有多远。

### Common Misconceptions / 常见误区
- **English:** Thinking it is a direct measurement of distance. It is an *estimation* based on an assumption (the star is on the main sequence).
- **中文:** 认为这是对距离的直接测量。这是一种基于假设（恒星在主序带上）的*估计*。
- **English:** Confusing it with standard candles (like Cepheid variables). Spectroscopic parallax uses the H-R diagram, not a period-luminosity relation.
- **中文:** 将其与标准烛光（如造父变星）混淆。分光视差使用赫罗图，而不是周期-光度关系。

### Exam Tips / 考试提示
- **English:** You will be given the distance modulus equation. Be careful with logarithms. If $m-M=5$, then $d=100$ pc. If $m-M=0$, then $d=10$ pc.
- **中文:** 你会被给予距离模数方程。注意对数运算。如果 $m-M=5$，则 $d=100$ pc。如果 $m-M=0$，则 $d=10$ pc。

> 📷 **IMAGE PROMPT — DIAGRAM-02: Spectroscopic Parallax Flowchart**
> A flowchart showing the steps of spectroscopic parallax. Step 1: "Star's Spectrum" leads to "Spectral Class (e.g., G2)". Step 2: "Spectral Class" points to an H-R diagram, with an arrow from the main sequence to a label "Absolute Magnitude M = +5". Step 3: "Telescope Observation" leads to "Apparent Magnitude m = +10". Step 4: "m and M" point to the equation "m - M = 5 log(d/10)". Step 5: "Distance d = 100 pc".

---

# 5. Essential Equations / 核心公式

## 5.1 Stefan-Boltzmann Law / 斯特藩-玻尔兹曼定律

$$ L = 4\pi r^2 \sigma T^4 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $L$ | Luminosity of the star | 恒星的光度 | W (Watts) |
| $r$ | Radius of the star | 恒星的半径 | m |
| $\sigma$ | Stefan-Boltzmann constant ($5.67 \times 10^{-8} \text{ W m}^{-2} \text{ K}^{-4}$) | 斯特藩-玻尔兹曼常数 | W m⁻² K⁻⁴ |
| $T$ | Surface temperature of the star | 恒星的表面温度 | K |

**Derivation / 推导:** The power radiated per unit area is $\sigma T^4$ (Stefan-Boltzmann law for a black body). The total surface area of a star (sphere) is $4\pi r^2$. Therefore, total power $L = (4\pi r^2) \times (\sigma T^4)$.

**Conditions / 适用条件:** The star is assumed to be a perfect black body radiator. This is a good approximation for most stars.

**Limitations / 局限性:** Real stars are not perfect black bodies, especially in spectral lines. The law gives the total luminosity across all wavelengths.

## 5.2 Mass-Luminosity Relation / 质量-光度关系

$$ L \propto M^{3.5} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $L$ | Luminosity of the star | 恒星的光度 | W (Watts) |
| $M$ | Mass of the star | 恒星的质量 | kg |

**Derivation / 推导:** This is an empirical relation derived from observations of binary star systems. The exponent can vary slightly (e.g., 3.0 to 4.0) depending on the mass range, but 3.5 is the standard value for A-Level.

**Conditions / 适用条件:** Only applies to [[Main Sequence Stars]].

**Limitations / 局限性:** Does not apply to giants, supergiants, or white dwarfs. It is an approximation.

## 5.3 Distance Modulus Equation / 距离模数方程

$$ m - M = 5 \log_{10} \left( \frac{d}{10} \right) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $m$ | Apparent magnitude | 视星等 | dimensionless |
| $M$ | Absolute magnitude | 绝对星等 | dimensionless |
| $d$ | Distance to the star | 恒星的距离 | pc (parsecs) |

**Derivation / 推导:** Based on the inverse square law for light and the definition of the magnitude scale (a difference of 5 magnitudes corresponds to a factor of 100 in brightness).

**Conditions / 适用条件:** Assumes no significant interstellar extinction (absorption of light by dust).

**Limitations / 局限性:** Interstellar dust can make a star appear fainter (larger $m$), leading to an overestimate of distance.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 The H-R Diagram with Isoradius Lines / 带有等半径线的赫罗图

### Axes / 坐标轴
- **Y-axis:** Luminosity ($L$) in solar units ($L_\odot$), or Absolute Magnitude ($M$). Increasing upwards.
- **X-axis:** Surface Temperature ($T$) in Kelvin, or Spectral Class. Decreasing to the right (hotter on the left).

### Shape / 形状
The main sequence is a diagonal band from top-left to bottom-right. Giants and supergiants are above the main sequence. White dwarfs are below it. Isoradius lines are diagonal lines running parallel to the main sequence.

### Gradient Meaning / 斜率含义
The gradient of an isoradius line is not constant on a log-log plot, but the lines show the relationship $L \propto T^4$ for a fixed radius.

### Area Meaning / 面积含义
The area of the H-R diagram is not directly meaningful, but the position of a star within the diagram tells you its evolutionary stage.

### Exam Interpretation / 考试解读
- **English:** You will be asked to read values of $L$ and $T$ from a given H-R diagram and use the Stefan-Boltzmann law to calculate the radius of a star, often comparing it to the Sun's radius.
- **中文:** 你会被要求从给定的赫罗图中读取 $L$ 和 $T$ 的值，并使用斯特藩-玻尔兹曼定律计算恒星的半径，通常是与太阳半径进行比较。

---

# 7. Required Diagrams / 必备图表

## 7.1 H-R Diagram with Isoradius Lines / 带有等半径线的赫罗图

### Description / 描述
**English:** A standard H-R diagram showing the main sequence, giant, supergiant, and white dwarf regions. Three or four diagonal dashed lines representing constant radii (e.g., $0.1 R_\odot$, $1 R_\odot$, $10 R_\odot$, $100 R_\odot$) are overlaid. The Sun is marked on the $1 R_\odot$ line.
**中文:** 一个标准的赫罗图，显示了主序带、巨星、超巨星和白矮星区域。叠加了三条或四条代表恒定半径的对角虚线（例如，$0.1 R_\odot$, $1 R_\odot$, $10 R_\odot$, $100 R_\odot$）。太阳被标记在 $1 R_\odot$ 线上。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-03: H-R Diagram with Isoradius Lines**
> A detailed Hertzsprung-Russell diagram. The y-axis is labeled "Luminosity (L/L☉)" on a logarithmic scale from 10^-4 to 10^6. The x-axis is labeled "Temperature (K)" decreasing from 30,000 K to 3,000 K. The main sequence is a thick, slightly curved band from top-left to bottom-right. The giant and supergiant branches are above the main sequence. The white dwarf region is below. Four dashed diagonal lines are drawn, labeled "0.1 R☉", "1 R☉", "10 R☉", and "100 R☉". The Sun is a yellow dot on the "1 R☉" line. A red giant is a red dot on the "10 R☉" line. A white dwarf is a small white dot on the "0.1 R☉" line.

### Labels Required / 需要标注
- **English:** Luminosity (L/L☉), Temperature (K), Main Sequence, Giants, Supergiants, White Dwarfs, Isoradius Lines (0.1 R☉, 1 R☉, 10 R☉, 100 R☉), Sun.
- **中文:** 光度 (L/L☉), 温度 (K), 主序带, 巨星, 超巨星, 白矮星, 等半径线 (0.1 R☉, 1 R☉, 10 R☉, 100 R☉), 太阳。

### Exam Importance / 考试重要性
- **English:** Essential for understanding how radius is determined from the H-R diagram. A common exam question is to locate a star on the diagram and estimate its radius relative to the Sun.
- **中文:** 对于理解如何从赫罗图确定半径至关重要。一个常见的考试题目是在图上定位一颗恒星并估计其相对于太阳的半径。

---

# 8. Worked Examples / 典型例题

## Example 1: Determining Radius / 例题1：确定半径

### Question / 题目
**English:** A star has a luminosity of $100 L_\odot$ and a surface temperature of $6000 \text{ K}$. The Sun has a luminosity of $L_\odot = 3.8 \times 10^{26} \text{ W}$ and a surface temperature of $5800 \text{ K}$. Calculate the radius of the star in terms of the Sun's radius ($R_\odot$).
**中文:** 一颗恒星的光度为 $100 L_\odot$，表面温度为 $6000 \text{ K}$。太阳的光度为 $L_\odot = 3.8 \times 10^{26} \text{ W}$，表面温度为 $5800 \text{ K}$。计算该恒星以太阳半径 ($R_\odot$) 为单位的半径。

### Solution / 解答
**Step 1:** Use the ratio form of the Stefan-Boltzmann law.
$$\frac{L_{\text{star}}}{L_\odot} = \left(\frac{r_{\text{star}}}{r_\odot}\right)^2 \left(\frac{T_{\text{star}}}{T_\odot}\right)^4$$

**Step 2:** Substitute the known values.
$$\frac{100 L_\odot}{L_\odot} = \left(\frac{r_{\text{star}}}{r_\odot}\right)^2 \left(\frac{6000}{5800}\right)^4$$

**Step 3:** Simplify.
$$100 = \left(\frac{r_{\text{star}}}{r_\odot}\right)^2 \times (1.0345)^4$$
$$100 = \left(\frac{r_{\text{star}}}{r_\odot}\right)^2 \times 1.145$$

**Step 4:** Solve for the radius ratio.
$$\left(\frac{r_{\text{star}}}{r_\odot}\right)^2 = \frac{100}{1.145} = 87.34$$
$$\frac{r_{\text{star}}}{r_\odot} = \sqrt{87.34} = 9.35$$

### Final Answer / 最终答案
**Answer:** $r_{\text{star}} = 9.35 R_\odot$ | **答案：** $r_{\text{star}} = 9.35 R_\odot$

### Quick Tip / 提示
**English:** Always use the ratio form to avoid dealing with large numbers and constants. Remember to take the square root at the end.
**中文:** 始终使用比例形式，以避免处理大数字和常数。记得最后要开平方根。

## Example 2: Spectroscopic Parallax / 例题2：分光视差

### Question / 题目
**English:** A main sequence star has an apparent magnitude of $m = +8.0$. Its spectrum shows it is an A0 star. From the H-R diagram, the absolute magnitude of an A0 main sequence star is $M = +2.0$. Calculate the distance to the star in parsecs.
**中文:** 一颗主序星的视星等为 $m = +8.0$。其光谱显示它是一颗A0型星。从赫罗图可知，A0型主序星的绝对星等为 $M = +2.0$。计算该恒星的距离（以秒差距为单位）。

### Solution / 解答
**Step 1:** Write down the distance modulus equation.
$$m - M = 5 \log_{10} \left( \frac{d}{10} \right)$$

**Step 2:** Substitute the values.
$$8.0 - 2.0 = 5 \log_{10} \left( \frac{d}{10} \right)$$
$$6.0 = 5 \log_{10} \left( \frac{d}{10} \right)$$

**Step 3:** Solve for the logarithm.
$$\log_{10} \left( \frac{d}{10} \right) = \frac{6.0}{5} = 1.2$$

**Step 4:** Remove the logarithm.
$$\frac{d}{10} = 10^{1.2}$$

**Step 5:** Calculate $d$.
$$d = 10 \times 10^{1.2} = 10 \times 15.85 = 158.5 \text{ pc}$$

### Final Answer / 最终答案
**Answer:** $d = 159 \text{ pc}$ (to 3 significant figures) | **答案：** $d = 159 \text{ pc}$（3位有效数字）

### Quick Tip / 提示
**English:** Remember that $10^{1.2}$ is not 12. Use your calculator carefully. If $m-M=5$, then $d=100$ pc. If $m-M=0$, then $d=10$ pc.
**中文:** 记住 $10^{1.2}$ 不是12。小心使用计算器。如果 $m-M=5$，则 $d=100$ pc。如果 $m-M=0$，则 $d=10$ pc。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate radius from L and T using Stefan-Boltzmann law | High | Medium | 📝 *待填入* |
| Calculate mass of main sequence star using mass-luminosity relation | Medium | Medium | 📝 *待填入* |
| Calculate distance using spectroscopic parallax | High | Medium | 📝 *待填入* |
| Explain why a star is a giant or white dwarf based on its position on H-R diagram | Medium | Easy | 📝 *待填入* |
| Compare two stars on the H-R diagram (radius, mass, evolutionary stage) | High | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, Show that, Explain, State, Suggest, Compare.
- **中文:** 计算，确定，证明，解释，陈述，提出，比较。

---

# 10. Practical Skills Connections / 实验技能链接

**English:** While you won't build an H-R diagram in a school lab, the skills of data analysis and graph interpretation are directly relevant. You should be able to:
- Plot data of luminosity vs. temperature on a logarithmic scale.
- Draw a best-fit line for the main sequence.
- Use the graph to interpolate or extrapolate values.
- Understand the concept of uncertainties: the H-R diagram has intrinsic scatter, meaning the absolute magnitude estimated from a spectral class has an associated uncertainty, which propagates into the distance calculation.
- The mass-luminosity relation is derived from binary star observations, which involve careful measurement of orbital periods and separations (linking to [[Gravitational Fields]]).

**中文:** 虽然你不会在学校实验室里构建赫罗图，但数据分析和图表解读的技能是直接相关的。你应该能够：
- 在对数坐标上绘制光度与温度的关系数据。
- 为主序带绘制最佳拟合线。
- 使用图表进行内插或外推数值。
- 理解不确定性的概念：赫罗图存在固有的弥散，这意味着从光谱型估计出的绝对星等具有相关的不确定性，这会传递到距离计算中。
- 质量-光度关系是从双星观测中推导出来的，这涉及对轨道周期和间距的仔细测量（与[[引力场]]相关）。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    subgraph "Using H-R Diagram"
        A[Star's Spectrum] --> B[Spectral Class]
        B --> C[H-R Diagram]
        C --> D[Absolute Magnitude M]
        C --> E[Luminosity L]
        C --> F[Temperature T]
        
        E --> G[Stefan-Boltzmann Law]
        F --> G
        G --> H[Radius r]
        
        E --> I[Mass-Luminosity Relation]
        I --> J[Mass M (Main Sequence Only)]
        
        D --> K[Distance Modulus]
        K --> L[Distance d]
        
        M[Apparent Magnitude m] --> K
    end

    subgraph "Related Topics"
        N[[Stellar Evolution]]
        O[[Stellar Distances]]
        P[[Luminosity, Radiant Flux and Black Body Radiation]]
    end

    H --> N
    J --> N
    L --> O
    G --> P
    I --> P
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| Definition / 定义 | The H-R diagram is a plot of Luminosity (or Absolute Magnitude) against Temperature (or Spectral Class). It is used to determine stellar radius, mass, and distance. |
| Key Formula / 核心公式 | **Stefan-Boltzmann:** $L = 4\pi r^2 \sigma T^4$ <br> **Mass-Luminosity:** $L \propto M^{3.5}$ (Main Sequence only) <br> **Distance Modulus:** $m - M = 5 \log_{10}(d/10)$ |
| Key Graph / 核心图表 | H-R diagram with isoradius lines. Diagonal lines show constant radius. Top-right = large radius (giants). Bottom-left = small radius (white dwarfs). |
| Exam Tip / 考试提示 | Always use ratio forms of equations to simplify calculations. For spectroscopic parallax, remember the assumption that the star is on the main sequence. If $m-M=5$, $d=100$ pc. |