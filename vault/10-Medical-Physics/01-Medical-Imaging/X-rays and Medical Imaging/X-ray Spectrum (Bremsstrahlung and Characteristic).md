# 1. Overview / 概述

**English:**
This sub-topic explores the **X-ray spectrum** — the distribution of photon energies produced by an X-ray tube. When high-speed electrons strike a metal target (typically tungsten), they generate X-rays through two distinct mechanisms: **Bremsstrahlung** (braking radiation) and **Characteristic X-rays**. Understanding the spectrum is crucial for medical imaging because it determines image quality, patient dose, and the effectiveness of [[Attenuation of X-rays]] in different tissues. The spectrum's shape — a continuous background with sharp peaks — is a direct consequence of quantum physics and atomic structure, linking this topic to [[The Photoelectric Effect]] and [[Alpha, Beta and Gamma Radiation]].

**中文:**
本子知识点探讨 **X射线谱** —— X射线管产生的光子能量分布。当高速电子撞击金属靶（通常是钨）时，通过两种不同的机制产生X射线：**轫致辐射**（制动辐射）和**特征X射线**。理解X射线谱对医学成像至关重要，因为它决定了图像质量、患者剂量以及[[X射线的衰减]]在不同组织中的效果。X射线谱的形状——连续背景上叠加尖锐峰值——是量子物理和原子结构的直接结果，将本主题与[[光电效应]]和[[α、β和γ辐射]]联系起来。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 26.1(a) Describe the nature of X-rays as electromagnetic radiation of short wavelength | 11.1 Understand the production of X-rays from an X-ray tube |
| 26.1(b) Explain the production of X-rays by the processes of Bremsstrahlung and characteristic radiation | 11.2 Understand the continuous nature of the X-ray spectrum and the minimum wavelength |
| 26.1(c) Describe the features of the X-ray spectrum | 11.3 Understand the origin of characteristic X-ray peaks |
| 26.1(d) Explain the effect of changing tube voltage on the spectrum | 11.4 Understand the effect of tube voltage on the spectrum |
| 26.1(e) Explain the effect of changing target material on the spectrum | 11.5 Understand the effect of target material on the spectrum |
| 26.1(f) Explain the effect of filtration on the X-ray spectrum | 11.6 Understand the use of filtration to remove low-energy X-rays |
| 26.1(g) Understand the concept of half-value thickness (HVT) | — |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to sketch and label the X-ray spectrum, explain the origin of both continuous and characteristic components, and predict how changes in tube voltage, target material, and filtration affect the spectrum. Calculations of minimum wavelength using $λ_{min} = hc/eV$ are common.
- **中文:** 你必须能够绘制并标注X射线谱，解释连续谱和特征谱的起源，并预测管电压、靶材料和过滤如何影响谱线。使用 $λ_{min} = hc/eV$ 计算最小波长是常见题型。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Bremsstrahlung** / 轫致辐射 | Electromagnetic radiation produced when a charged particle (electron) is decelerated by the electric field of an atomic nucleus | 带电粒子（电子）在原子核电场中减速时产生的电磁辐射 | Confusing with characteristic radiation; thinking it's from electron-electron interactions |
| **Characteristic X-rays** / 特征X射线 | X-rays emitted when an electron from an outer shell fills a vacancy in an inner shell of an atom, releasing energy equal to the difference in binding energies | 当外层电子填补内层空位时发射的X射线，释放的能量等于结合能之差 | Forgetting that the vacancy must first be created by an incident electron |
| **Minimum Wavelength ($λ_{min}$)** / 最小波长 | The shortest wavelength in the X-ray spectrum, corresponding to an electron losing all its kinetic energy in a single Bremsstrahlung event | X射线谱中最短的波长，对应电子在一次轫致辐射事件中损失全部动能 | Thinking $λ_{min}$ depends on target material (it only depends on tube voltage) |
| **Cut-off Wavelength** / 截止波长 | Same as minimum wavelength; the wavelength below which no X-rays are produced | 与最小波长相同；低于此波长不产生X射线 | Confusing with absorption edges |
| **Filtration** / 过滤 | The process of removing low-energy X-rays from the beam using an absorbing material (typically aluminium) | 使用吸收材料（通常是铝）从射线束中去除低能X射线的过程 | Thinking filtration increases intensity (it actually reduces it but hardens the beam) |
| **Half-Value Thickness (HVT)** / 半值厚度 | The thickness of a material required to reduce the intensity of an X-ray beam to half its original value | 将X射线束强度降低到原始值一半所需的材料厚度 | Confusing with attenuation coefficient; HVT = ln2/μ |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Bremsstrahlung Radiation / 轫致辐射

### Explanation / 解释
**English:** When a high-speed electron from the cathode approaches the nucleus of a target atom (e.g., tungsten), it experiences a strong electrostatic attraction. This causes the electron to decelerate and change direction. According to classical electromagnetism, an accelerating (or decelerating) charge radiates energy. The energy lost by the electron is emitted as a photon — an X-ray. The process is called "Bremsstrahlung" (German for "braking radiation"). The energy of the emitted photon can range from zero up to the full kinetic energy of the incident electron ($eV$), producing a **continuous spectrum**. Most electrons undergo multiple interactions, losing energy gradually, which is why the spectrum is continuous and peaks at around one-third of the maximum energy.

**中文:** 当来自阴极的高速电子接近靶原子（如钨）的原子核时，会受到强烈的静电吸引。这导致电子减速并改变方向。根据经典电磁学，加速（或减速）的电荷会辐射能量。电子损失的能量以光子形式发射——即X射线。这个过程称为"轫致辐射"（德语"制动辐射"）。发射光子的能量范围从零到入射电子的全部动能（$eV$），产生**连续谱**。大多数电子经历多次相互作用，逐渐损失能量，这就是为什么谱线是连续的，并在最大能量的约三分之一处出现峰值。

### Physical Meaning / 物理意义
**English:** Bremsstrahlung is a direct conversion of kinetic energy into electromagnetic radiation. The continuous nature of the spectrum reflects the statistical distribution of how much energy each electron loses in a single interaction. The minimum wavelength ($λ_{min}$) corresponds to the rare event where an electron loses ALL its kinetic energy in ONE interaction.

**中文:** 轫致辐射是动能直接转化为电磁辐射的过程。谱线的连续性质反映了每个电子在单次相互作用中损失多少能量的统计分布。最小波长（$λ_{min}$）对应于电子在**一次**相互作用中损失**全部**动能的罕见事件。

### Common Misconceptions / 常见误区
- **English:** Students often think Bremsstrahlung is caused by electrons hitting the nucleus directly. In reality, electrons rarely hit the nucleus; they are deflected by the electric field.
- **中文:** 学生常认为轫致辐射是由电子直接撞击原子核引起的。实际上，电子很少撞击原子核；它们是被电场偏转的。
- **English:** Another misconception is that all electrons produce the same photon energy. In fact, the energy varies randomly from zero to $eV$.
- **中文:** 另一个误区是所有电子产生相同的光子能量。实际上，能量从零到$eV$随机变化。

### Exam Tips / 考试提示
- **English:** Be prepared to calculate $λ_{min}$ using $λ_{min} = hc/eV$. Remember that $V$ is the tube voltage in volts, and $e$ is the elementary charge.
- **中文:** 准备好使用 $λ_{min} = hc/eV$ 计算 $λ_{min}$。记住 $V$ 是以伏特为单位的管电压，$e$ 是元电荷。
- **English:** When sketching the spectrum, always label the axes: intensity (y-axis) vs. wavelength (x-axis).
- **中文:** 绘制谱线时，始终标注坐标轴：强度（y轴）vs. 波长（x轴）。

> 📷 **IMAGE PROMPT — BR-01: Bremsstrahlung Process**
> A diagram showing a high-speed electron (with velocity vector) approaching a tungsten nucleus (large positive charge). The electron's path curves as it is deflected by the electric field. An X-ray photon is emitted at the point of maximum curvature. Labels: "Incident electron", "Tungsten nucleus", "X-ray photon (Bremsstrahlung)", "Deflected electron (lower energy)". Use arrows to show direction.

## 4.2 Characteristic X-rays / 特征X射线

### Explanation / 解释
**English:** Characteristic X-rays are produced when an incident electron has enough energy to eject an inner-shell electron from a target atom (e.g., a K-shell electron). This creates a vacancy (hole) in the inner shell. An electron from a higher energy level (e.g., L-shell or M-shell) immediately drops down to fill the vacancy. The energy difference between the two shells is emitted as a photon — a **characteristic X-ray**. Because the energy levels are unique to each element, the wavelengths of these X-rays are characteristic of the target material. For tungsten, the Kα line (L→K transition) has energy ~59.3 keV, and the Kβ line (M→K transition) has energy ~67.2 keV.

**中文:** 当入射电子有足够能量从靶原子中击出一个内层电子（如K层电子）时，就会产生特征X射线。这在内层产生一个空位。来自更高能级（如L层或M层）的电子立即下降填补空位。两个能级之间的能量差以光子形式发射——即**特征X射线**。由于能级对每种元素是唯一的，这些X射线的波长是靶材料的特征。对于钨，Kα线（L→K跃迁）能量约为59.3 keV，Kβ线（M→K跃迁）能量约为67.2 keV。

### Physical Meaning / 物理意义
**English:** Characteristic X-rays are a manifestation of atomic structure and quantum mechanics. They provide a "fingerprint" of the target element. The minimum tube voltage required to produce a characteristic X-ray is the binding energy of the inner-shell electron (e.g., ~69.5 keV for tungsten K-shell). Below this voltage, no characteristic X-rays of that series are produced.

**中文:** 特征X射线是原子结构和量子力学的体现。它们提供了靶元素的"指纹"。产生特征X射线所需的最小管电压是内层电子的结合能（例如钨K层约为69.5 keV）。低于此电压，不会产生该系列的特征X射线。

### Common Misconceptions / 常见误区
- **English:** Students often think characteristic X-rays are produced by the incident electron itself. They are actually produced by the target atom's electrons rearranging.
- **中文:** 学生常认为特征X射线是由入射电子本身产生的。实际上它们是由靶原子的电子重新排列产生的。
- **English:** Another mistake is thinking that increasing tube voltage increases the energy of characteristic X-rays. The energy is fixed by atomic energy levels; only the intensity increases.
- **中文:** 另一个错误是认为增加管电压会增加特征X射线的能量。能量由原子能级固定；只有强度增加。

### Exam Tips / 考试提示
- **English:** Remember that characteristic peaks appear as sharp spikes on top of the continuous Bremsstrahlung background. They only appear if the tube voltage exceeds the binding energy of the inner shell.
- **中文:** 记住特征峰在连续轫致辐射背景上表现为尖锐的尖峰。只有当管电压超过内壳层结合能时才会出现。

> 📷 **IMAGE PROMPT — CH-01: Characteristic X-ray Production**
> A diagram showing an atom with K, L, and M shells. An incident electron (arrow) strikes a K-shell electron, ejecting it. A vacancy is created in the K-shell. An L-shell electron drops down to fill the vacancy, emitting a characteristic X-ray photon. Labels: "Incident electron", "Ejected K-shell electron", "K-shell vacancy", "L→K transition", "Characteristic X-ray (Kα)". Use different colours for shells.

## 4.3 The Complete X-ray Spectrum / 完整的X射线谱

### Explanation / 解释
**English:** The complete X-ray spectrum is a plot of X-ray intensity (number of photons per unit energy interval) against wavelength (or energy). It consists of two components:
1. **Continuous spectrum (Bremsstrahlung):** A smooth curve starting at $λ_{min}$, rising to a peak at about $1.5λ_{min}$, then gradually falling to zero at long wavelengths.
2. **Characteristic peaks:** Sharp spikes superimposed on the continuous background at specific wavelengths determined by the target material.

The shape of the continuous spectrum is determined by:
- **Tube voltage ($V$):** Higher voltage shifts $λ_{min}$ to shorter wavelengths and increases overall intensity.
- **Target material:** Higher atomic number (Z) increases Bremsstrahlung efficiency (intensity ∝ Z).
- **Filtration:** Removes low-energy (long wavelength) X-rays, shifting the peak to shorter wavelengths (hardening the beam).

**中文:** 完整的X射线谱是X射线强度（每单位能量间隔的光子数）对波长（或能量）的图。它由两部分组成：
1. **连续谱（轫致辐射）：** 从 $λ_{min}$ 开始的平滑曲线，上升到约 $1.5λ_{min}$ 处的峰值，然后逐渐下降到长波长处的零。
2. **特征峰：** 在特定波长处叠加在连续背景上的尖锐尖峰，由靶材料决定。

连续谱的形状由以下因素决定：
- **管电压（$V$）：** 更高的电压将 $λ_{min}$ 移至更短波长并增加整体强度。
- **靶材料：** 更高的原子序数（Z）增加轫致辐射效率（强度 ∝ Z）。
- **过滤：** 去除低能（长波长）X射线，将峰值移至更短波长（硬化射线束）。

> 📋 **CIE Only:** You need to understand half-value thickness (HVT) and its relationship to attenuation coefficient: $HVT = \ln 2 / \mu$.
> 📋 **Edexcel Only:** You need to understand the effect of filtration on the spectrum in more detail, including the concept of beam hardening.

---

# 5. Essential Equations / 核心公式

## 5.1 Minimum Wavelength / 最小波长

$$ λ_{min} = \frac{hc}{eV} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $λ_{min}$ | Minimum wavelength of X-rays | X射线的最小波长 | m (metres) |
| $h$ | Planck's constant | 普朗克常数 | J·s |
| $c$ | Speed of light | 光速 | m·s⁻¹ |
| $e$ | Elementary charge | 元电荷 | C |
| $V$ | Tube voltage (accelerating potential) | 管电压（加速电势） | V (volts) |

**Derivation / 推导:**
An electron accelerated through a potential difference $V$ gains kinetic energy $eV$. If all this energy is converted into a single X-ray photon: $eV = hf = hc/λ$. Rearranging: $λ = hc/eV$. The minimum wavelength occurs when $eV$ is maximum, so $λ_{min} = hc/eV$.

**Conditions / 适用条件:**
- **English:** Assumes all kinetic energy of the electron is converted into one photon (ideal case). In reality, this is rare.
- **中文:** 假设电子的全部动能转化为一个光子（理想情况）。实际上，这种情况很少见。

**Limitations / 局限性:**
- **English:** Does not account for energy losses due to heat or multiple interactions.
- **中文:** 不考虑由于热量或多次相互作用造成的能量损失。

## 5.2 Photon Energy / 光子能量

$$ E = hf = \frac{hc}{λ} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Photon energy | 光子能量 | J or eV |
| $f$ | Frequency | 频率 | Hz |
| $λ$ | Wavelength | 波长 | m |

## 5.3 Half-Value Thickness (HVT) / 半值厚度

$$ I = I_0 e^{-μx} $$

$$ HVT = \frac{\ln 2}{μ} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $I$ | Transmitted intensity | 透射强度 | W·m⁻² |
| $I_0$ | Incident intensity | 入射强度 | W·m⁻² |
| $μ$ | Linear attenuation coefficient | 线性衰减系数 | m⁻¹ |
| $x$ | Thickness of material | 材料厚度 | m |
| $HVT$ | Half-value thickness | 半值厚度 | m |

> 📋 **CIE Only:** This equation is required for CAIE 9702 but not for Edexcel IAL.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 X-ray Spectrum Graph / X射线谱图

### Axes / 坐标轴
- **X-axis:** Wavelength (λ) / 波长 (λ) — decreasing to the right (or energy increasing to the right)
- **Y-axis:** Intensity (I) / 强度 (I)

### Shape / 形状
**English:** The graph shows:
- A sharp cut-off at $λ_{min}$ (shortest wavelength)
- A rapid rise to a peak at approximately $1.5λ_{min}$
- A gradual decrease at longer wavelengths
- Sharp characteristic peaks (if tube voltage is high enough) superimposed on the continuous curve

**中文:** 图形显示：
- 在 $λ_{min}$ 处有尖锐截止（最短波长）
- 快速上升到约 $1.5λ_{min}$ 处的峰值
- 在较长波长处逐渐下降
- 尖锐的特征峰（如果管电压足够高）叠加在连续曲线上

### Gradient Meaning / 斜率含义
**English:** The gradient at any point represents the rate of change of intensity with wavelength. Not typically examined directly.

**中文:** 任意点的斜率表示强度随波长的变化率。通常不直接考查。

### Area Meaning / 面积含义
**English:** The area under the curve represents the total X-ray intensity (total power emitted).

**中文:** 曲线下的面积代表总X射线强度（总发射功率）。

### Exam Interpretation / 考试解读
**English:** You must be able to:
1. Sketch the spectrum for different tube voltages
2. Identify the effect of changing target material
3. Show the effect of filtration
4. Label characteristic peaks

**中文:** 你必须能够：
1. 绘制不同管电压下的谱线
2. 识别改变靶材料的影响
3. 显示过滤的效果
4. 标注特征峰

> 📷 **IMAGE PROMPT — SP-01: X-ray Spectrum**
> A graph with wavelength on the x-axis (increasing to the right) and intensity on the y-axis. The curve starts at λ_min (marked with a vertical dashed line), rises sharply to a peak at about 1.5λ_min, then gradually decreases. Two sharp characteristic peaks (Kα and Kβ) are shown as spikes on the continuous background. Labels: "λ_min", "Bremsstrahlung continuum", "Kα characteristic peak", "Kβ characteristic peak". Use different colours for continuous and characteristic components.

## 6.2 Effect of Tube Voltage / 管电压的影响

### Description / 描述
**English:** Increasing the tube voltage ($V$):
- Decreases $λ_{min}$ (shifts to shorter wavelengths)
- Increases overall intensity (area under curve increases)
- Shifts the peak to shorter wavelengths
- May introduce new characteristic peaks if voltage exceeds binding energies of inner shells

**中文:** 增加管电压（$V$）：
- 减小 $λ_{min}$（移至更短波长）
- 增加整体强度（曲线下面积增加）
- 将峰值移至更短波长
- 如果电压超过内壳层结合能，可能引入新的特征峰

> 📷 **IMAGE PROMPT — SP-02: Effect of Tube Voltage**
> Two X-ray spectra on the same axes. One at 50 kV (lower intensity, longer λ_min) and one at 100 kV (higher intensity, shorter λ_min). The 100 kV curve is entirely above and to the left of the 50 kV curve. Labels: "50 kV", "100 kV", "λ_min (50 kV)", "λ_min (100 kV)".

## 6.3 Effect of Filtration / 过滤的影响

### Description / 描述
**English:** Adding an aluminium filter:
- Removes low-energy (long wavelength) X-rays preferentially
- Shifts the peak to shorter wavelengths (beam hardening)
- Reduces overall intensity
- Does NOT affect $λ_{min}$ (high-energy photons pass through)
- Reduces patient dose (low-energy X-rays are absorbed by skin and don't contribute to image)

**中文:** 添加铝过滤器：
- 优先去除低能（长波长）X射线
- 将峰值移至更短波长（射线束硬化）
- 降低整体强度
- 不影响 $λ_{min}$（高能光子通过）
- 降低患者剂量（低能X射线被皮肤吸收，不贡献于图像）

> 📷 **IMAGE PROMPT — SP-03: Effect of Filtration**
> Two X-ray spectra on the same axes. One without filtration (higher intensity at long wavelengths) and one with aluminium filtration (lower intensity, peak shifted to shorter wavelengths). The λ_min is the same for both. Labels: "Unfiltered", "Filtered", "λ_min", "Low-energy X-rays removed".

---

# 7. Required Diagrams / 必备图表

## 7.1 X-ray Tube Diagram / X射线管图

### Description / 描述
**English:** A labelled diagram of an X-ray tube showing the cathode (filament), anode (target), focusing cup, and the path of electrons. The diagram should indicate where Bremsstrahlung and characteristic X-rays are produced.

**中文:** X射线管的标注图，显示阴极（灯丝）、阳极（靶）、聚焦杯和电子路径。图表应指示轫致辐射和特征X射线产生的位置。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — XT-01: X-ray Tube**
> A cross-sectional diagram of a modern X-ray tube. Left side: cathode with a coiled tungsten filament inside a focusing cup. Right side: rotating anode made of tungsten (beveled face). Electrons (dashed arrows) travel from cathode to anode. X-rays (wavy arrows) emerge from the anode at an angle. Labels: "Cathode (-)", "Filament", "Focusing cup", "Electron beam", "Anode (+)", "Tungsten target", "X-ray beam", "Glass envelope". Use a cutaway view to show internal structure.

### Labels Required / 需要标注
- Cathode / 阴极
- Filament / 灯丝
- Focusing cup / 聚焦杯
- Electron beam / 电子束
- Anode / 阳极
- Tungsten target / 钨靶
- X-ray beam / X射线束
- Glass envelope / 玻璃外壳

### Exam Importance / 考试重要性
**English:** This diagram is essential for understanding how the X-ray spectrum is produced. You may be asked to label it or explain the function of each part.

**中文:** 此图对于理解X射线谱如何产生至关重要。你可能会被要求标注或解释每个部分的功能。

## 7.2 X-ray Spectrum Diagram / X射线谱图

### Description / 描述
**English:** A fully labelled X-ray spectrum showing the continuous Bremsstrahlung background and characteristic peaks. The diagram should indicate $λ_{min}$, the peak of the continuous spectrum, and the Kα and Kβ characteristic lines.

**中文:** 完全标注的X射线谱，显示连续轫致辐射背景和特征峰。图表应指示 $λ_{min}$、连续谱的峰值以及Kα和Kβ特征线。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — SP-04: Complete X-ray Spectrum**
> A graph with wavelength (λ) on the x-axis (increasing to the right) and intensity (I) on the y-axis. The continuous Bremsstrahlung curve starts at λ_min (marked with a vertical dashed line and label), rises to a peak at approximately 1.5λ_min, then gradually decreases. Two sharp characteristic peaks are shown: Kα (larger) and Kβ (smaller) at specific wavelengths. The area under the curve is shaded. Labels: "λ_min", "Bremsstrahlung continuum", "Kα (L→K)", "Kβ (M→K)", "Peak of continuous spectrum". Use a clean, textbook-style graph.

### Labels Required / 需要标注
- λ_min / 最小波长
- Bremsstrahlung continuum / 轫致辐射连续谱
- Kα characteristic peak / Kα特征峰
- Kβ characteristic peak / Kβ特征峰
- Peak of continuous spectrum / 连续谱峰值

### Exam Importance / 考试重要性
**English:** This is one of the most commonly examined diagrams in medical physics. You must be able to sketch it from memory and explain its features.

**中文:** 这是医学物理中最常考查的图表之一。你必须能够凭记忆绘制并解释其特征。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Minimum Wavelength / 计算最小波长

### Question / 题目
**English:** An X-ray tube operates at a tube voltage of 80 kV. Calculate the minimum wavelength of the X-rays produced. (Given: $h = 6.63 \times 10^{-34}$ J·s, $c = 3.00 \times 10^8$ m·s⁻¹, $e = 1.60 \times 10^{-19}$ C)

**中文:** 一个X射线管在80 kV的管电压下工作。计算产生的X射线的最小波长。（已知：$h = 6.63 \times 10^{-34}$ J·s，$c = 3.00 \times 10^8$ m·s⁻¹，$e = 1.60 \times 10^{-19}$ C）

### Solution / 解答

**Step 1:** Write the formula.
$$ λ_{min} = \frac{hc}{eV} $$

**Step 2:** Substitute values. Note: 80 kV = $80 \times 10^3$ V.
$$ λ_{min} = \frac{(6.63 \times 10^{-34})(3.00 \times 10^8)}{(1.60 \times 10^{-19})(80 \times 10^3)} $$

**Step 3:** Calculate numerator.
$$ (6.63 \times 10^{-34})(3.00 \times 10^8) = 1.989 \times 10^{-25} $$

**Step 4:** Calculate denominator.
$$ (1.60 \times 10^{-19})(80 \times 10^3) = 1.28 \times 10^{-14} $$

**Step 5:** Divide.
$$ λ_{min} = \frac{1.989 \times 10^{-25}}{1.28 \times 10^{-14}} = 1.55 \times 10^{-11} \text{ m} $$

**Step 6:** Convert to picometres (optional).
$$ λ_{min} = 1.55 \times 10^{-11} \text{ m} = 0.0155 \text{ nm} = 15.5 \text{ pm} $$

### Final Answer / 最终答案
**Answer:** $λ_{min} = 1.55 \times 10^{-11}$ m (or 15.5 pm) | **答案：** $λ_{min} = 1.55 \times 10^{-11}$ 米（或15.5皮米）

### Quick Tip / 提示
**English:** Always convert kV to V (multiply by 1000) before substituting. A common mistake is forgetting this conversion.
**中文:** 代入前始终将kV转换为V（乘以1000）。常见的错误是忘记这个转换。

---

## Example 2: Effect of Changing Tube Voltage / 管电压变化的影响

### Question / 题目
**English:** An X-ray tube is operated at 60 kV and then at 120 kV. Describe and explain the differences in the X-ray spectrum produced.

**中文:** 一个X射线管分别在60 kV和120 kV下工作。描述并解释产生的X射线谱的差异。

### Solution / 解答

**Step 1:** Calculate $λ_{min}$ for both voltages.
At 60 kV: $λ_{min} = \frac{hc}{e \times 60 \times 10^3} = 2.07 \times 10^{-11}$ m
At 120 kV: $λ_{min} = \frac{hc}{e \times 120 \times 10^3} = 1.035 \times 10^{-11}$ m

**Step 2:** Describe the differences.
- **Minimum wavelength:** $λ_{min}$ at 120 kV is half that at 60 kV (shorter wavelength = higher energy).
- **Intensity:** The overall intensity (area under curve) is greater at 120 kV because more electrons are accelerated to higher energy.
- **Peak position:** The peak of the continuous spectrum shifts to shorter wavelengths at higher voltage.
- **Characteristic peaks:** At 60 kV, if the voltage is below the K-shell binding energy of tungsten (~69.5 keV), no K-characteristic peaks appear. At 120 kV, Kα and Kβ peaks will be present.

**Step 3:** Explain using physics.
- $λ_{min} = hc/eV$ shows that $λ_{min}$ is inversely proportional to $V$.
- Higher voltage means electrons have more kinetic energy, so they can produce more X-ray photons and higher energy photons.
- Characteristic X-rays require the incident electron to have enough energy to eject an inner-shell electron. This only happens if $eV$ > binding energy of the inner shell.

### Final Answer / 最终答案
**Answer:** At 120 kV, the spectrum has a shorter $λ_{min}$, higher overall intensity, the peak shifts to shorter wavelengths, and characteristic K-peaks appear (if above ~69.5 keV). | **答案：** 在120 kV下，谱线具有更短的 $λ_{min}$、更高的整体强度、峰值移至更短波长，并且出现特征K峰（如果高于约69.5 keV）。

### Quick Tip / 提示
**English:** When comparing spectra, always mention: $λ_{min}$, intensity, peak position, and characteristic peaks.
**中文:** 比较谱线时，始终提及：$λ_{min}$、强度、峰值位置和特征峰。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate $λ_{min}$ from tube voltage | ★★★★★ | Easy | 📝 *待填入* |
| Sketch and label X-ray spectrum | ★★★★★ | Medium | 📝 *待填入* |
| Explain origin of Bremsstrahlung | ★★★★☆ | Medium | 📝 *待填入* |
| Explain origin of characteristic X-rays | ★★★★☆ | Medium | 📝 *待填入* |
| Effect of changing tube voltage on spectrum | ★★★★☆ | Medium | 📝 *待填入* |
| Effect of filtration on spectrum | ★★★☆☆ | Medium | 📝 *待填入* |
| Compare spectra for different target materials | ★★★☆☆ | Hard | 📝 *待填入* |
| Calculate HVT from attenuation coefficient | ★★☆☆☆ | Easy | 📝 *待填入* (CIE only) |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Sketch, Explain, Describe, Compare, State
- **中文:** 计算、绘制、解释、描述、比较、陈述

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in several ways:

1. **Measurement of X-ray spectrum:** In a lab setting, a Geiger-Müller tube or scintillation detector can be used with a crystal spectrometer to measure the X-ray spectrum. Students would plot intensity against wavelength and identify characteristic peaks.

2. **Determination of $λ_{min}$:** By measuring the minimum wavelength at different tube voltages, students can verify the relationship $λ_{min} = hc/eV$ and determine Planck's constant ($h$) from the gradient of a $λ_{min}$ vs. $1/V$ graph.

3. **Filtration experiments:** Using aluminium absorbers of different thicknesses, students can measure the attenuation of X-rays and determine the half-value thickness (HVT). This links to [[Attenuation of X-rays]].

4. **Uncertainties:** Key uncertainties include:
   - Voltage measurement (±1% typical)
   - Wavelength determination from spectrometer (±0.5%)
   - Intensity measurements (statistical fluctuations in photon count)

5. **Graph plotting:** Students should be able to plot intensity vs. wavelength, identify the peak, and determine $λ_{min}$ from the cut-off point.

**中文:**
本子知识点在多个方面与实验工作相关：

1. **测量X射线谱：** 在实验室环境中，可以使用盖革-米勒管或闪烁探测器配合晶体谱仪测量X射线谱。学生绘制强度对波长的图并识别特征峰。

2. **确定 $λ_{min}$：** 通过在不同管电压下测量最小波长，学生可以验证 $λ_{min} = hc/eV$ 关系，并从 $λ_{min}$ 对 $1/V$ 图的斜率确定普朗克常数（$h$）。

3. **过滤实验：** 使用不同厚度的铝吸收体，学生可以测量X射线的衰减并确定半值厚度（HVT）。这与[[X射线的衰减]]相关。

4. **不确定度：** 关键不确定度包括：
   - 电压测量（典型±1%）
   - 谱仪波长确定（±0.5%）
   - 强度测量（光子计数的统计波动）

5. **绘图：** 学生应能够绘制强度对波长的图，识别峰值，并从截止点确定 $λ_{min}$。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main node
    XS[X-ray Spectrum] --> BR[Bremsstrahlung]
    XS --> CH[Characteristic X-rays]
    
    %% Bremsstrahlung connections
    BR --> |"Electron decelerated by nucleus"| KE[Kinetic Energy → Photon]
    BR --> |"Produces"| CS[Continuous Spectrum]
    CS --> |"Has"| LM[λ_min = hc/eV]
    CS --> |"Peak at"| PP[~1.5λ_min]
    
    %% Characteristic connections
    CH --> |"Requires"| IE[Inner-shell Electron Ejection]
    IE --> |"Creates"| VAC[Vacancy]
    VAC --> |"Filled by"| ET[Electron Transition]
    ET --> |"Emits"| CP[Characteristic Peaks]
    CP --> |"Kα"| KAL[L→K Transition]
    CP --> |"Kβ"| KBL[M→K Transition]
    
    %% External factors
    TV[Tube Voltage] --> |"Affects"| LM
    TV --> |"Affects"| CS
    TV --> |"Determines if"| IE
    TM[Target Material] --> |"Determines"| CP
    FL[Filtration] --> |"Removes"| LW[Low-energy X-rays]
    FL --> |"Causes"| BH[Beam Hardening]
    
    %% Connections to parent and siblings
    XS --> |"Part of"| XR[[X-rays and Medical Imaging]]
    XS --> |"Related to"| XT[[Production of X-rays (X-ray Tube)]]
    XS --> |"Related to"| AT[[Attenuation of X-rays]]
    XS --> |"Related to"| PE[[The Photoelectric Effect]]
    
    %% Styling
    classDef main fill:#f9f,stroke:#333,stroke-width:2px
    classDef process fill:#bbf,stroke:#333,stroke-width:1px
    classDef concept fill:#bfb,stroke:#333,stroke-width:1px
    classDef external fill:#fbb,stroke:#333,stroke-width:1px
    
    class XS main
    class BR,CH,CS,CP process
    class LM,PP,KAL,KBL concept
    class TV,TM,FL external
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | X-ray spectrum = intensity vs. wavelength plot showing continuous Bremsstrahlung + characteristic peaks / X射线谱 = 强度对波长图，显示连续轫致辐射 + 特征峰 |
| **Key Formula / 核心公式** | $λ_{min} = hc/eV$ — minimum wavelength depends ONLY on tube voltage / 最小波长仅取决于管电压 |
| **Key Graph / 核心图表** | Spectrum: sharp cut-off at $λ_{min}$, peak at ~1.5$λ_{min}$, gradual decrease, characteristic spikes / 谱线：在 $λ_{min}$ 处尖锐截止，峰值在 ~1.5$λ_{min}$，逐渐下降，特征尖峰 |
| **Bremsstrahlung / 轫致辐射** | Electron decelerated by nucleus → continuous spectrum; intensity ∝ Z of target / 电子被原子核减速 → 连续谱；强度 ∝ 靶的Z |
| **Characteristic / 特征X射线** | Inner-shell electron ejected → outer electron fills vacancy → photon with fixed energy (element-specific) / 内层电子被击出 → 外层电子填补空位 → 固定能量光子（元素特异性） |
| **Effect of Voltage / 电压影响** | Higher V → shorter $λ_{min}$, higher intensity, peak shifts left, may add characteristic peaks / 更高V → 更短 $λ_{min}$，更高强度，峰值左移，可能添加特征峰 |
| **Effect of Filtration / 过滤影响** | Removes low-energy X-rays → beam hardening, reduced intensity, reduced patient dose / 去除低能X射线 → 射线束硬化，强度降低，患者剂量降低 |
| **Effect of Target / 靶影响** | Higher Z → higher Bremsstrahlung intensity; different Z → different characteristic peak energies / 更高Z → 更高轫致辐射强度；不同Z → 不同特征峰能量 |
| **Exam Tip / 考试提示** | Always sketch spectrum with labelled axes; mention both continuous and characteristic components / 始终绘制带标注坐标轴的谱线；提及连续和特征两部分 |
| **Common Mistake / 常见错误** | Thinking $λ_{min}$ depends on target material (it doesn't — only on V) / 认为 $λ_{min}$ 取决于靶材料（不——仅取决于V） |