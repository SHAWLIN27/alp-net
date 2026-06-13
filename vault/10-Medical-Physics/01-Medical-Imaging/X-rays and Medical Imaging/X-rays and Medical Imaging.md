# X-rays and Medical Imaging / X射线与医学成像

---

# 1. Overview / 概述

**English:**
X-rays are a form of high-energy electromagnetic radiation with wavelengths in the range of approximately $10^{-11}$ m to $10^{-8}$ m (photon energies from about 100 eV to 100 keV). This topic explores the production, properties, and medical applications of X-rays, forming a cornerstone of modern diagnostic medicine. We will study how X-rays are generated in an [[X-ray Tube]], the nature of the [[X-ray Spectrum (Bremsstrahlung and Characteristic)]], how they interact with matter through [[Attenuation of X-rays]], and how these principles enable [[X-ray Imaging and Contrast]] techniques. The topic extends to advanced imaging modalities like [[CT Scans and Their Principles]] and concludes with essential considerations of [[Radiation Dose and Safety]].

In the Cambridge 9702 and Edexcel IAL A-Level Physics syllabuses, this topic is assessed through a combination of theoretical understanding, graphical analysis (particularly the X-ray spectrum), calculations involving attenuation and half-value thickness, and explanations of imaging principles. It connects deeply with [[The Photoelectric Effect]] (which explains X-ray absorption) and [[Alpha, Beta and Gamma Radiation]] (for understanding radiation hazards and safety). It also links forward to [[Ultrasound Imaging]] and [[PET Scans and Nuclear Medicine]] as alternative medical imaging modalities.

Real-world applications are vast: from simple chest X-rays for diagnosing pneumonia and fractures, to mammography for breast cancer screening, fluoroscopy for real-time imaging during surgery, and CT scans for detailed 3D anatomical reconstruction. Understanding X-ray physics is also critical for radiation therapy in oncology and for ensuring patient and staff safety through proper shielding and dose management.

**中文：**
X射线是一种高能电磁辐射，波长范围约为 $10^{-11}$ m 到 $10^{-8}$ m（光子能量约100 eV到100 keV）。本主题探讨X射线的产生、性质及其在医学中的应用，是现代诊断医学的基石。我们将研究X射线如何在[[X射线管]]中产生、[[X射线谱（轫致辐射和特征辐射）]]的性质、它们如何通过[[X射线的衰减]]与物质相互作用，以及这些原理如何实现[[X射线成像与对比度]]技术。本主题还扩展到[[CT扫描及其原理]]等先进成像方式，并以[[辐射剂量与安全]]的基本考虑作为结尾。

在剑桥9702和爱德思IAL A-Level物理考纲中，本主题通过理论理解、图形分析（特别是X射线谱）、涉及衰减和半值厚度的计算以及成像原理解释来评估。它与[[光电效应]]（解释X射线吸收）和[[α、β和γ辐射]]（理解辐射危害和安全）密切相关，并向前链接到[[超声成像]]和[[PET扫描与核医学]]作为替代医学成像方式。

实际应用非常广泛：从用于诊断肺炎和骨折的简单胸部X光片，到用于乳腺癌筛查的乳腺摄影、手术中实时成像的透视检查，以及用于详细3D解剖重建的CT扫描。理解X射线物理学对于肿瘤学中的放射治疗以及通过适当屏蔽和剂量管理确保患者和工作人员安全也至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (26.1) | Edexcel IAL (WPH14 U4: 11.1-11.6) |
|------------------|-----------------------------------|
| 26.1(a) Describe the nature and properties of X-rays | 11.1 Understand the nature and production of X-rays, including the role of the X-ray tube |
| 26.1(b) Explain how X-rays are produced in an X-ray tube | 11.2 Understand the X-ray spectrum, including continuous (bremsstrahlung) and characteristic components |
| 26.1(c) Describe the X-ray spectrum and distinguish between continuous and characteristic X-rays | 11.3 Understand the attenuation of X-rays, including the exponential attenuation law and half-value thickness (HVT) |
| 26.1(d) Understand the attenuation of X-rays and the exponential attenuation law $I = I_0 e^{-\mu x}$ | 11.4 Understand how X-rays are used in medical imaging, including contrast media |
| 26.1(e) Define and use half-value thickness (HVT) | 11.5 Understand the principles of CT scanning, including image reconstruction |
| 26.1(f) Explain the use of X-rays in medical imaging, including contrast media | 11.6 Understand the principles of radiation dose and safety, including absorbed dose, equivalent dose, and effective dose |
| 26.1(g) Describe the principles of CT scanning | |

> 📋 **CIE Only:** CIE specifically requires description of the nature and properties of X-rays (26.1a) and expects students to distinguish between continuous and characteristic X-rays in the spectrum (26.1c). The definition and use of half-value thickness (HVT) is explicitly listed (26.1e). CIE also expects students to describe the principles of CT scanning (26.1g).

> 📋 **Edexcel Only:** Edexcel explicitly includes the role of the X-ray tube in production (11.1), requires understanding of both continuous and characteristic components of the spectrum (11.2), and has a dedicated section on radiation dose and safety (11.6) which includes absorbed dose, equivalent dose, and effective dose. Edexcel also expects understanding of CT image reconstruction (11.5).

**Examiner Expectations / 考官期望：**
- **English:** Students must be able to recall and apply the exponential attenuation law $I = I_0 e^{-\mu x}$ in calculations. They should be able to interpret the X-ray spectrum graph, identifying the minimum wavelength (duality cutoff) and characteristic peaks. Understanding of half-value thickness (HVT) and its relationship with the attenuation coefficient ($\mu$) is essential. For CT scans, students should understand the principle of taking multiple projections from different angles and reconstructing a 3D image.
- **中文：** 学生必须能够回忆并应用指数衰减定律 $I = I_0 e^{-\mu x}$ 进行计算。他们应该能够解释X射线谱图，识别最小波长（对偶截止）和特征峰。理解半值厚度（HVT）及其与衰减系数（$\mu$）的关系至关重要。对于CT扫描，学生应理解从不同角度获取多个投影并重建3D图像的原理。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **X-rays / X射线** | High-energy electromagnetic radiation with wavelengths in the range $10^{-11}$ m to $10^{-8}$ m, produced when high-speed electrons are decelerated by a metal target | 高能电磁辐射，波长范围 $10^{-11}$ m 到 $10^{-8}$ m，当高速电子被金属靶减速时产生 | Confusing X-rays with gamma rays (X-rays are produced by electron interactions, gamma rays by nuclear decay) |
| **[[X-ray Tube]] / X射线管** | A vacuum tube containing a heated cathode and a metal anode (target), used to produce X-rays by accelerating electrons through a high potential difference | 一种真空管，包含加热阴极和金属阳极（靶），通过高电势差加速电子来产生X射线 | Forgetting that the tube must be evacuated to prevent electron collisions with air molecules |
| **[[Bremsstrahlung]] / 轫致辐射** | "Braking radiation" — continuous X-ray spectrum produced when electrons are decelerated by the electric field of target nuclei | "刹车辐射" — 当电子被靶核电场减速时产生的连续X射线谱 | Thinking bremsstrahlung is the only mechanism; forgetting characteristic X-rays |
| **[[Characteristic X-rays]] / 特征X射线** | Discrete X-ray wavelengths produced when an incident electron ejects an inner-shell electron from a target atom, and an outer-shell electron fills the vacancy | 当入射电子从靶原子中击出一个内层电子，外层电子填补空位时产生的离散X射线波长 | Confusing with atomic emission spectra in the visible range |
| **[[Attenuation of X-rays]] / X射线的衰减** | The reduction in intensity of an X-ray beam as it passes through matter, due to absorption and scattering | X射线束穿过物质时由于吸收和散射导致的强度降低 | Thinking attenuation is only due to absorption (scattering also contributes) |
| **Half-Value Thickness (HVT) / 半值厚度** | The thickness of a material that reduces the intensity of an X-ray beam to half its initial value | 将X射线束强度降低到初始值一半所需的材料厚度 | Confusing HVT with the attenuation coefficient $\mu$ (they are inversely related: $HVT = \ln 2 / \mu$) |
| **[[Attenuation Coefficient]] ($\mu$) / 衰减系数** | The probability per unit thickness that an X-ray photon will be absorbed or scattered, with units m$^{-1}$ | 单位厚度内X射线光子被吸收或散射的概率，单位为 m$^{-1}$ | Forgetting that $\mu$ depends on both the material and the X-ray energy |
| **[[Contrast Medium]] / 造影剂** | A substance (e.g., barium sulfate or iodine) introduced into the body to enhance the contrast between different tissues in an X-ray image | 引入体内的物质（如硫酸钡或碘），用于增强X射线图像中不同组织之间的对比度 | Thinking contrast media are radioactive (they are not; they are high atomic number materials that absorb X-rays strongly) |
| **[[CT Scan]] / CT扫描** | Computed Tomography — a medical imaging technique that uses X-ray measurements from multiple angles to produce cross-sectional (tomographic) images of the body | 计算机断层扫描 — 一种使用从多个角度进行的X射线测量来产生身体横截面（断层）图像的医学成像技术 | Confusing CT with simple X-ray radiography (CT uses multiple projections and computer reconstruction) |
| **[[Absorbed Dose]] / 吸收剂量** | The energy absorbed per unit mass of tissue, measured in grays (Gy), where 1 Gy = 1 J kg$^{-1}$ | 单位质量组织吸收的能量，以戈瑞（Gy）为单位，1 Gy = 1 J kg$^{-1}$ | Confusing absorbed dose with equivalent dose (equivalent dose accounts for radiation type) |
| **[[Equivalent Dose]] / 等效剂量** | The absorbed dose multiplied by a radiation weighting factor ($w_R$) to account for the biological effectiveness of different radiation types, measured in sieverts (Sv) | 吸收剂量乘以辐射权重因子（$w_R$），以考虑不同辐射类型的生物效应，单位为希沃特（Sv） | Forgetting that for X-rays, $w_R = 1$, so equivalent dose in Sv equals absorbed dose in Gy |
| **[[Effective Dose]] / 有效剂量** | The sum of equivalent doses to different tissues, each multiplied by a tissue weighting factor ($w_T$), measured in sieverts (Sv) | 不同组织的等效剂量之和，每个乘以组织权重因子（$w_T$），单位为希沃特（Sv） | Thinking effective dose is the same as equivalent dose (effective dose accounts for tissue sensitivity) |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Production of X-rays / X射线的产生

### Explanation / 解释
**English:**
X-rays are produced in an [[X-ray Tube]] when high-speed electrons are rapidly decelerated upon striking a metal target (usually tungsten or molybdenum). The tube consists of a heated cathode (filament) that emits electrons via thermionic emission, and a metal anode (target) maintained at a high positive potential (typically 30-150 kV). The electrons are accelerated across the vacuum gap and strike the target, where two main processes generate X-rays:

1. **Bremsstrahlung (braking radiation):** When an electron passes near the nucleus of a target atom, it is deflected and decelerated by the strong electric field. The lost kinetic energy is emitted as an X-ray photon. Since electrons can lose varying amounts of energy, this produces a continuous spectrum of X-ray wavelengths.

2. **Characteristic X-rays:** If an incident electron has sufficient energy to eject an inner-shell electron (e.g., from the K-shell) from a target atom, an outer-shell electron drops down to fill the vacancy. The energy difference is emitted as an X-ray photon with a specific wavelength characteristic of the target material.

Only about 1% of the electron kinetic energy is converted to X-rays; the remaining 99% is converted to heat in the target. This is why the anode must be cooled (often by rotating it or using water cooling).

**中文：**
当高速电子撞击金属靶（通常是钨或钼）时，在[[X射线管]]中产生X射线。该管由一个加热阴极（灯丝）通过热电子发射发射电子，以及一个保持高正电势（通常30-150 kV）的金属阳极（靶）组成。电子在真空间隙中被加速并撞击靶，其中两个主要过程产生X射线：

1. **轫致辐射（刹车辐射）：** 当电子经过靶原子核附近时，它被强电场偏转和减速。损失的动能以X射线光子的形式发射。由于电子可以损失不同数量的能量，这产生了连续波长的X射线谱。

2. **特征X射线：** 如果入射电子有足够的能量从靶原子中击出一个内层电子（例如，从K层），外层电子会下降填补空位。能量差以特定波长的X射线光子形式发射，该波长是靶材料的特征。

只有约1%的电子动能转化为X射线；剩余的99%在靶中转化为热量。这就是为什么阳极必须冷却（通常通过旋转或水冷）。

### Physical Meaning / 物理意义
**English:**
The production of X-rays is a conversion of electrical energy into electromagnetic radiation. The minimum wavelength of the X-ray spectrum corresponds to the maximum energy conversion — when an electron loses all its kinetic energy in a single interaction, producing a photon with energy equal to the accelerating voltage times the electron charge ($eV = hf_{max}$). This is the Duane-Hunt law.

**中文：**
X射线的产生是将电能转化为电磁辐射。X射线谱的最小波长对应于最大能量转换——当一个电子在单次相互作用中损失其全部动能时，产生一个能量等于加速电压乘以电子电荷的光子（$eV = hf_{max}$）。这就是杜安-亨特定律。

### Common Misconceptions / 常见误区
- **English:** Students often think X-rays are produced by the electrons themselves emitting radiation continuously. In reality, bremsstrahlung is produced by the *deceleration* of electrons, not by the electrons in their normal state.
- **中文：** 学生常认为X射线是由电子本身连续发射辐射产生的。实际上，轫致辐射是由电子的*减速*产生的，而不是由正常状态下的电子产生的。
- **English:** Another misconception is that characteristic X-rays are produced by the incident electron itself. They are produced by the target atom's electron transitions after the incident electron has ejected an inner-shell electron.
- **中文：** 另一个误解是特征X射线是由入射电子本身产生的。它们是在入射电子击出一个内层电子后，由靶原子的电子跃迁产生的。

### Exam Tips / 考试提示
**English:**
- Be able to label a diagram of an X-ray tube (cathode, anode, target, cooling system, lead shielding).
- Know that the minimum wavelength $\lambda_{min} = \frac{hc}{eV}$ where $V$ is the accelerating voltage.
- Understand why the anode is rotated (to distribute heat and prevent melting).
- Distinguish between the continuous (bremsstrahlung) and discrete (characteristic) components of the X-ray spectrum.

**中文：**
- 能够标注X射线管图（阴极、阳极、靶、冷却系统、铅屏蔽）。
- 知道最小波长 $\lambda_{min} = \frac{hc}{eV}$，其中 $V$ 是加速电压。
- 理解为什么阳极旋转（分散热量，防止熔化）。
- 区分X射线谱的连续（轫致辐射）和离散（特征）分量。

> 📷 **IMAGE PROMPT — [XRT-01]: Cross-section of an X-ray Tube**
>
> A detailed cross-sectional diagram of an X-ray tube showing: a heated tungsten filament (cathode) at the top, a focusing cup directing electrons downward, a rotating tungsten anode (target) at the bottom angled at about 20 degrees, a beryllium window on the side for X-ray output, lead shielding around the tube except at the window, and cooling oil channels around the anode. Labels in English and Chinese. Clean technical illustration style with color coding: red for high voltage, blue for cooling system, yellow for X-ray beam.

---

## 4.2 X-ray Spectrum / X射线谱

### Explanation / 解释
**English:**
The X-ray spectrum is a graph of X-ray intensity (or number of photons) versus wavelength (or photon energy). It has two distinct components:

1. **Continuous spectrum (Bremsstrahlung):** This forms the background of the spectrum. It has a sharp cutoff at the minimum wavelength $\lambda_{min}$ (corresponding to the maximum photon energy $E_{max} = eV$), rises to a peak intensity at about $1.5\lambda_{min}$, and then gradually decreases to zero at longer wavelengths. The shape arises because electrons can lose any fraction of their kinetic energy in a single bremsstrahlung event.

2. **Characteristic spectrum:** Superimposed on the continuous background are sharp peaks at specific wavelengths. These correspond to the characteristic X-rays of the target material. For tungsten, the $K_\alpha$ and $K_\beta$ lines are prominent, corresponding to electron transitions from the L-shell to K-shell ($K_\alpha$) and M-shell to K-shell ($K_\beta$).

The spectrum is affected by:
- **Increasing accelerating voltage:** Shifts $\lambda_{min}$ to shorter wavelengths (higher energies), increases overall intensity, and may excite additional characteristic lines if the voltage exceeds the excitation potential for inner shells.
- **Changing target material:** Changes the positions of characteristic peaks (different atomic numbers have different energy levels). The continuous spectrum shape is similar for all materials but the intensity scales with atomic number.

**中文：**
X射线谱是X射线强度（或光子数）与波长（或光子能量）的关系图。它有两个不同的分量：

1. **连续谱（轫致辐射）：** 这构成了谱的背景。它在最小波长 $\lambda_{min}$（对应于最大光子能量 $E_{max} = eV$）处有尖锐截止，在大约 $1.5\lambda_{min}$ 处上升到峰值强度，然后在较长波长处逐渐减小到零。这种形状的产生是因为电子可以在单次轫致辐射事件中损失其动能的任何部分。

2. **特征谱：** 在连续背景上叠加了特定波长处的尖锐峰值。这些对应于靶材料的特征X射线。对于钨，$K_\alpha$ 和 $K_\beta$ 线很突出，分别对应于从L层到K层（$K_\alpha$）和从M层到K层（$K_\beta$）的电子跃迁。

谱受以下因素影响：
- **增加加速电压：** 将 $\lambda_{min}$ 移至更短波长（更高能量），增加整体强度，如果电压超过内层的激发电位，可能激发额外的特征线。
- **改变靶材料：** 改变特征峰的位置（不同原子序数有不同的能级）。连续谱形状对所有材料相似，但强度随原子序数缩放。

### Physical Meaning / 物理意义
**English:**
The X-ray spectrum tells us about the energy distribution of X-ray photons produced. This is crucial for medical imaging because different photon energies have different penetration abilities. The continuous spectrum provides a range of energies, which is useful for imaging different tissue thicknesses. The characteristic peaks provide high-intensity X-rays at specific energies, which can be useful for specific applications (e.g., mammography uses molybdenum characteristic X-rays at about 20 keV).

**中文：**
X射线谱告诉我们产生的X射线光子的能量分布。这对医学成像至关重要，因为不同能量的光子具有不同的穿透能力。连续谱提供了一系列能量，这对于成像不同组织厚度很有用。特征峰在特定能量处提供高强度X射线，可用于特定应用（例如，乳腺摄影使用约20 keV的钼特征X射线）。

### Common Misconceptions / 常见误区
- **English:** Students often think the minimum wavelength $\lambda_{min}$ is the wavelength of the most intense X-rays. In fact, the most intense X-rays occur at about $1.5\lambda_{min}$.
- **中文：** 学生常认为最小波长 $\lambda_{min}$ 是最强X射线的波长。实际上，最强X射线出现在约 $1.5\lambda_{min}$ 处。
- **English:** Another misconception is that characteristic X-rays are always present. They only appear when the accelerating voltage exceeds the excitation potential of the target's inner shells (e.g., for tungsten K-shell, about 69.5 kV).
- **中文：** 另一个误解是特征X射线总是存在。它们只在加速电压超过靶内层的激发电位时才出现（例如，对于钨K层，约69.5 kV）。

### Exam Tips / 考试提示
**English:**
- Be able to sketch and label the X-ray spectrum, showing both continuous and characteristic components.
- Know how to calculate $\lambda_{min}$ from the accelerating voltage.
- Understand the effect of changing voltage and target material on the spectrum.
- Be able to explain why the intensity drops to zero at $\lambda_{min}$ (no photon can have energy greater than the electron's kinetic energy).

**中文：**
- 能够绘制和标注X射线谱，显示连续和特征分量。
- 知道如何从加速电压计算 $\lambda_{min}$。
- 理解改变电压和靶材料对谱的影响。
- 能够解释为什么强度在 $\lambda_{min}$ 处降至零（没有光子可以具有大于电子动能的能量）。

> 📷 **IMAGE PROMPT — [XRS-01]: X-ray Spectrum Graph**
>
> A graph of X-ray intensity (y-axis) versus wavelength (x-axis) showing: a continuous bremsstrahlung spectrum rising from zero at $\lambda_{min}$ to a peak at about $1.5\lambda_{min}$, then gradually decreasing; two sharp characteristic peaks ($K_\alpha$ and $K_\beta$) superimposed on the continuous background; labeled axes with units; a second curve (dashed) showing the effect of higher accelerating voltage (shifted to shorter wavelengths, higher intensity). Clean scientific graph style with grid lines.

---

## 4.3 Attenuation of X-rays / X射线的衰减

### Explanation / 解释
**English:**
When an X-ray beam passes through matter, its intensity decreases due to absorption and scattering. This process is called [[Attenuation of X-rays]]. The attenuation follows an exponential law:

$$ I = I_0 e^{-\mu x} $$

where:
- $I$ is the transmitted intensity
- $I_0$ is the initial intensity
- $\mu$ is the linear attenuation coefficient (m$^{-1}$)
- $x$ is the thickness of the material (m)

The linear attenuation coefficient $\mu$ depends on:
- **Atomic number ($Z$) of the material:** Higher $Z$ materials absorb X-rays more strongly (e.g., bone, with calcium, $Z=20$, absorbs more than soft tissue, mainly carbon, hydrogen, oxygen).
- **Density ($\rho$) of the material:** Denser materials attenuate more.
- **Energy of the X-ray photons:** Higher energy X-rays penetrate more (lower $\mu$).

The **mass attenuation coefficient** $\mu_m = \mu / \rho$ (units m$^2$ kg$^{-1}$) is often used because it is independent of the physical density of the material.

The **Half-Value Thickness (HVT)** is the thickness required to reduce the intensity to half:

$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{\mu} $$

**中文：**
当X射线束穿过物质时，其强度因吸收和散射而降低。这个过程称为[[X射线的衰减]]。衰减遵循指数定律：

$$ I = I_0 e^{-\mu x} $$

其中：
- $I$ 是透射强度
- $I_0$ 是初始强度
- $\mu$ 是线性衰减系数（m$^{-1}$）
- $x$ 是材料的厚度（m）

线性衰减系数 $\mu$ 取决于：
- **材料的原子序数（$Z$）：** 高$Z$材料吸收X射线更强（例如，骨骼含钙，$Z=20$，比主要含碳、氢、氧的软组织吸收更多）。
- **材料的密度（$\rho$）：** 密度更大的材料衰减更多。
- **X射线光子的能量：** 更高能量的X射线穿透力更强（$\mu$ 更小）。

**质量衰减系数** $\mu_m = \mu / \rho$（单位 m$^2$ kg$^{-1}$）经常使用，因为它与材料的物理密度无关。

**半值厚度（HVT）** 是将强度降低到一半所需的厚度：

$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{\mu} $$

### Physical Meaning / 物理意义
**English:**
The exponential attenuation law explains why X-rays can image different tissues. Bone has a higher $\mu$ than soft tissue, so it attenuates X-rays more, appearing white on a radiograph. Air (in lungs) has a very low $\mu$, appearing black. The HVT is a practical measure used in radiation shielding design — for example, lead has a small HVT for X-rays, making it an effective shielding material.

**中文：**
指数衰减定律解释了为什么X射线可以对不同组织成像。骨骼的 $\mu$ 高于软组织，因此它衰减X射线更多，在X光片上呈现白色。空气（在肺中）的 $\mu$ 非常低，呈现黑色。HVT是辐射屏蔽设计中使用的实用度量——例如，铅对X射线的HVT很小，使其成为有效的屏蔽材料。

### Common Misconceptions / 常见误区
- **English:** Students often think $\mu$ is a constant for a given material. In fact, $\mu$ depends strongly on X-ray energy — it decreases as energy increases (except at absorption edges).
- **中文：** 学生常认为 $\mu$ 对给定材料是常数。实际上，$\mu$ 强烈依赖于X射线能量——它随能量增加而减小（吸收边除外）。
- **English:** Another misconception is that after one HVT, the intensity is zero. After one HVT, the intensity is $I_0/2$; after two HVTs, it is $I_0/4$, etc. It never reaches zero theoretically.
- **中文：** 另一个误解是经过一个HVT后，强度为零。经过一个HVT后，强度为 $I_0/2$；经过两个HVT后，为 $I_0/4$，等等。理论上它永远不会达到零。

### Exam Tips / 考试提示
**English:**
- Be able to use the exponential attenuation law in calculations.
- Know how to calculate HVT from $\mu$ and vice versa.
- Understand that the HVT depends on both the material and the X-ray energy.
- Be able to explain why different tissues appear with different contrast on an X-ray image.
- For CIE: Be prepared to describe an experiment to measure the HVT of a material.

**中文：**
- 能够在计算中使用指数衰减定律。
- 知道如何从 $\mu$ 计算HVT，反之亦然。
- 理解HVT取决于材料和X射线能量。
- 能够解释为什么不同组织在X射线图像上呈现不同对比度。
- 对于CIE：准备描述测量材料HVT的实验。

> 📷 **IMAGE PROMPT — [ATT-01]: Exponential Attenuation of X-rays**
>
> A graph showing exponential decay: X-ray intensity (y-axis) versus thickness of material (x-axis). The curve starts at $I_0$ and decays exponentially. Marked points at $x = HVT$ showing $I = I_0/2$, at $x = 2HVT$ showing $I = I_0/4$, and at $x = 3HVT$ showing $I = I_0/8$. A second curve (dashed) shows a material with higher $\mu$ (steeper decay). Clean scientific graph with labeled axes and grid lines.

---

## 4.4 X-ray Imaging and Contrast / X射线成像与对比度

### Explanation / 解释
**English:**
In conventional X-ray radiography, X-rays from a source pass through the patient and are detected on the other side (by film or a digital detector). Different tissues attenuate X-rays by different amounts, creating a shadow image:

- **Bone:** High attenuation → appears white (radiopaque)
- **Soft tissue (muscle, organs):** Moderate attenuation → appears gray
- **Air (lungs, bowel):** Low attenuation → appears black (radiolucent)

**Contrast media** are substances introduced into the body to enhance the visibility of specific structures:
- **Barium sulfate ($BaSO_4$):** A high-Z compound (barium, $Z=56$) that is insoluble and safe for ingestion. Used for imaging the gastrointestinal tract (barium meal for esophagus/stomach, barium enema for colon).
- **Iodine compounds:** Water-soluble iodine ($Z=53$) compounds injected intravenously. Used for angiography (imaging blood vessels), CT contrast enhancement, and urography (imaging the urinary tract).

The principle is that these high-Z materials have a much higher attenuation coefficient than surrounding tissues, so they appear bright white on the image, clearly delineating the structure of interest.

**Image quality** is affected by:
- **Contrast:** The difference in intensity between adjacent areas. Higher contrast makes structures more distinguishable.
- **Spatial resolution:** The ability to distinguish small, closely spaced objects.
- **Noise:** Random fluctuations in image brightness that reduce clarity.

**中文：**
在常规X射线放射摄影中，来自源的X射线穿过患者并在另一侧被检测到（通过胶片或数字探测器）。不同组织衰减X射线的量不同，产生阴影图像：

- **骨骼：** 高衰减 → 呈现白色（不透射线）
- **软组织（肌肉、器官）：** 中等衰减 → 呈现灰色
- **空气（肺、肠道）：** 低衰减 → 呈现黑色（透射线）

**造影剂** 是引入体内的物质，用于增强特定结构的可见性：
- **硫酸钡（$BaSO_4$）：** 一种高Z化合物（钡，$Z=56$），不溶于水，可安全摄入。用于胃肠道成像（食管/胃的钡餐，结肠的钡灌肠）。
- **碘化合物：** 水溶性碘（$Z=53$）化合物静脉注射。用于血管造影（血管成像）、CT对比增强和尿路造影（尿路成像）。

原理是这些高Z材料的衰减系数远高于周围组织，因此在图像上呈现亮白色，清晰勾勒出感兴趣的结构。

**图像质量** 受以下因素影响：
- **对比度：** 相邻区域之间的强度差异。更高的对比度使结构更易区分。
- **空间分辨率：** 区分小而紧密间隔物体的能力。
- **噪声：** 图像亮度的随机波动，降低清晰度。

### Physical Meaning / 物理意义
**English:**
The ability to distinguish different tissues depends on the difference in their attenuation coefficients. For soft tissues with similar composition (e.g., liver and kidney), the natural contrast is poor. Contrast media artificially increase the attenuation difference, making these structures visible. This is why contrast-enhanced CT scans are so valuable in diagnosing tumors and vascular abnormalities.

**中文：**
区分不同组织的能力取决于它们衰减系数的差异。对于成分相似的软组织（如肝脏和肾脏），自然对比度很差。造影剂人为地增加了衰减差异，使这些结构可见。这就是为什么对比增强CT扫描在诊断肿瘤和血管异常方面如此有价值。

### Common Misconceptions / 常见误区
- **English:** Students often think contrast media are radioactive. They are not — they are simply high atomic number materials that absorb X-rays strongly.
- **中文：** 学生常认为造影剂具有放射性。它们不是——它们只是吸收X射线强烈的高原子序数材料。
- **English:** Another misconception is that higher X-ray energy always gives better images. In fact, there is a trade-off: higher energy X-rays penetrate more (reducing dose) but also reduce contrast because the attenuation coefficients of different tissues become more similar.
- **中文：** 另一个误解是更高的X射线能量总是产生更好的图像。实际上，存在权衡：更高能量的X射线穿透力更强（减少剂量），但也降低对比度，因为不同组织的衰减系数变得更相似。

### Exam Tips / 考试提示
**English:**
- Be able to explain why bone appears white and air appears black on an X-ray.
- Know the two main contrast media (barium and iodine) and their applications.
- Understand the principle of contrast enhancement.
- Be able to discuss factors affecting image quality (contrast, resolution, noise).

**中文：**
- 能够解释为什么骨骼在X射线上呈现白色，空气呈现黑色。
- 知道两种主要造影剂（钡和碘）及其应用。
- 理解对比增强的原理。
- 能够讨论影响图像质量的因素（对比度、分辨率、噪声）。

> 📷 **IMAGE PROMPT — [IMG-01]: X-ray Image of Chest with Contrast**
>
> A chest X-ray image showing: the heart as a white shadow in the center, ribs as curved white lines, lungs as dark areas, the diaphragm as a curved white line at the bottom. Inset shows a contrast-enhanced image of the esophagus (barium swallow) where the esophagus appears as a bright white tube. Medical imaging style with annotations in English and Chinese.

---

## 4.5 CT Scans and Their Principles / CT扫描及其原理

### Explanation / 解释
**English:**
Computed Tomography (CT) is a medical imaging technique that produces cross-sectional (tomographic) images of the body. Unlike conventional X-ray radiography, which projects a 3D structure onto a 2D image (superimposing all tissues along the beam path), CT creates true 3D images by taking multiple projections from different angles.

**Principle of operation:**
1. An X-ray tube and detector array rotate around the patient, taking many projections (typically hundreds) from different angles.
2. Each projection measures the attenuation of X-rays along a specific path through the body.
3. A computer uses mathematical algorithms (typically filtered back projection or iterative reconstruction) to reconstruct the 3D distribution of attenuation coefficients.
4. The result is a series of cross-sectional images (slices) that can be viewed individually or combined to form a 3D volume.

**Key advantages over conventional radiography:**
- Eliminates superimposition of structures (overlapping tissues are separated)
- Provides true 3D anatomical information
- Much better contrast resolution (can distinguish tissues with very similar attenuation coefficients)
- Enables quantitative measurements (e.g., Hounsfield units for tissue characterization)

**Hounsfield scale:** CT images are displayed in Hounsfield units (HU), where:
- Water = 0 HU
- Air = -1000 HU
- Bone = +400 to +1000 HU (depending on density)
- Soft tissue = +40 to +80 HU

**中文：**
计算机断层扫描（CT）是一种产生身体横截面（断层）图像的医学成像技术。与将3D结构投影到2D图像上（沿光束路径叠加所有组织）的常规X射线放射摄影不同，CT通过从不同角度获取多个投影来创建真正的3D图像。

**工作原理：**
1. X射线管和探测器阵列围绕患者旋转，从不同角度获取许多投影（通常数百个）。
2. 每个投影测量X射线沿穿过身体的特定路径的衰减。
3. 计算机使用数学算法（通常是滤波反投影或迭代重建）来重建衰减系数的3D分布。
4. 结果是一系列横截面图像（切片），可以单独查看或组合形成3D体积。

**与常规放射摄影相比的主要优势：**
- 消除结构叠加（重叠组织被分离）
- 提供真正的3D解剖信息
- 更好的对比度分辨率（可以区分衰减系数非常相似的组织）
- 实现定量测量（例如，用于组织表征的亨氏单位）

**亨氏标度：** CT图像以亨氏单位（HU）显示，其中：
- 水 = 0 HU
- 空气 = -1000 HU
- 骨骼 = +400 到 +1000 HU（取决于密度）
- 软组织 = +40 到 +80 HU

### Physical Meaning / 物理意义
**English:**
CT scanning revolutionized medical imaging by providing true 3D anatomical information. Before CT, surgeons had to rely on 2D X-rays that superimposed all structures. CT allows precise localization of tumors, assessment of trauma, and guidance for surgical planning. The Hounsfield scale provides a quantitative measure of tissue density, enabling tissue characterization (e.g., distinguishing a cyst from a solid tumor).

**中文：**
CT扫描通过提供真正的3D解剖信息彻底改变了医学成像。在CT之前，外科医生必须依赖叠加所有结构的2D X射线。CT允许精确定位肿瘤、评估创伤和指导手术规划。亨氏标度提供了组织密度的定量测量，实现了组织表征（例如，区分囊肿和实体瘤）。

### Common Misconceptions / 常见误区
- **English:** Students often think CT uses a different type of radiation than conventional X-rays. CT uses the same X-rays — the difference is in how the data is acquired and processed.
- **中文：** 学生常认为CT使用与常规X射线不同类型的辐射。CT使用相同的X射线——区别在于数据的获取和处理方式。
- **English:** Another misconception is that CT gives a lower radiation dose than a single X-ray. In fact, a CT scan typically gives a much higher dose (e.g., a chest CT gives about 7 mSv compared to 0.1 mSv for a chest X-ray).
- **中文：** 另一个误解是CT比单次X射线辐射剂量更低。实际上，CT扫描通常给出更高的剂量（例如，胸部CT约7 mSv，而胸部X射线约0.1 mSv）。

### Exam Tips / 考试提示
**English:**
- Be able to describe the principle of CT scanning: multiple projections from different angles, computer reconstruction.
- Understand why CT provides better contrast resolution than conventional X-rays.
- Know the Hounsfield scale and what different values represent.
- Be able to discuss the advantages and disadvantages of CT compared to conventional X-rays.
- For Edexcel: Understand the concept of image reconstruction (filtered back projection).

**中文：**
- 能够描述CT扫描的原理：从不同角度获取多个投影，计算机重建。
- 理解为什么CT提供比常规X射线更好的对比度分辨率。
- 知道亨氏标度以及不同值代表什么。
- 能够讨论CT与常规X射线相比的优缺点。
- 对于爱德思：理解图像重建的概念（滤波反投影）。

> 📷 **IMAGE PROMPT — [CT-01]: CT Scanner Diagram**
>
> A cross-sectional diagram of a CT scanner showing: a patient lying on a table, an X-ray tube on one side of the patient, a curved detector array on the opposite side, the rotation path of the tube-detector assembly (shown as a dashed circle), and a computer monitor displaying a reconstructed cross-sectional image of the brain. Labels in English and Chinese. Clean technical illustration style.

---

## 4.6 Radiation Dose and Safety / 辐射剂量与安全

### Explanation / 解释
**English:**
Radiation dose is a measure of the energy deposited by ionizing radiation in tissue. Three key quantities are used:

1. **Absorbed Dose ($D$):** The energy absorbed per unit mass.
   $$ D = \frac{E}{m} $$
   Unit: gray (Gy), where 1 Gy = 1 J kg$^{-1}$.

2. **Equivalent Dose ($H_T$):** The absorbed dose multiplied by a radiation weighting factor ($w_R$) that accounts for the biological effectiveness of different radiation types.
   $$ H_T = D \times w_R $$
   Unit: sievert (Sv).
   For X-rays and gamma rays, $w_R = 1$, so $H_T$ (in Sv) = $D$ (in Gy).

3. **Effective Dose ($E$):** The sum of equivalent doses to different tissues, each multiplied by a tissue weighting factor ($w_T$) that accounts for the radiosensitivity of different organs.
   $$ E = \sum_T H_T \times w_T = \sum_T D \times w_R \times w_T $$
   Unit: sievert (Sv).

**Radiation safety principles (ALARA):**
- **Time:** Minimize exposure time.
- **Distance:** Maximize distance from the source (inverse square law).
- **Shielding:** Use appropriate shielding (lead aprons, lead glass, concrete walls).

**Typical effective doses:**
- Chest X-ray: ~0.02 mSv
- Dental X-ray: ~0.005 mSv
- Mammogram: ~0.4 mSv
- CT scan (head): ~2 mSv
- CT scan (abdomen): ~8 mSv
- Annual background radiation: ~2-3 mSv

**Biological effects:**
- **Deterministic effects:** Have a threshold dose (e.g., skin erythema at ~2 Sv, cataracts at ~5 Sv). Severity increases with dose.
- **Stochastic effects:** No threshold (e.g., cancer, genetic mutations). Probability increases with dose, but severity is independent of dose.

**中文：**
辐射剂量是电离辐射在组织中沉积能量的度量。使用三个关键量：

1. **吸收剂量（$D$）：** 单位质量吸收的能量。
   $$ D = \frac{E}{m} $$
   单位：戈瑞（Gy），其中 1 Gy = 1 J kg$^{-1}$。

2. **等效剂量（$H_T$）：** 吸收剂量乘以辐射权重因子（$w_R$），该因子考虑了不同辐射类型的生物效应。
   $$ H_T = D \times w_R $$
   单位：希沃特（Sv）。
   对于X射线和伽马射线，$w_R = 1$，因此 $H_T$（以Sv为单位）= $D$（以Gy为单位）。

3. **有效剂量（$E$）：** 不同组织等效剂量之和，每个乘以组织权重因子（$w_T$），该因子考虑了不同器官的辐射敏感性。
   $$ E = \sum_T H_T \times w_T = \sum_T D \times w_R \times w_T $$
   单位：希沃特（Sv）。

**辐射安全原则（ALARA）：**
- **时间：** 最小化暴露时间。
- **距离：** 最大化与源的距离（平方反比定律）。
- **屏蔽：** 使用适当的屏蔽（铅围裙、铅玻璃、混凝土墙）。

**典型有效剂量：**
- 胸部X射线：~0.02 mSv
- 牙科X射线：~0.005 mSv
- 乳腺摄影：~0.4 mSv
- CT扫描（头部）：~2 mSv
- CT扫描（腹部）：~8 mSv
- 年背景辐射：~2-3 mSv

**生物效应：**
- **确定性效应：** 有阈值剂量（例如，皮肤红斑约2 Sv，白内障约5 Sv）。严重程度随剂量增加。
- **随机性效应：** 无阈值（例如，癌症、基因突变）。概率随剂量增加，但严重程度与剂量无关。

### Physical Meaning / 物理意义
**English:**
Radiation dose is a critical concept in medical physics because it balances the diagnostic benefit of an X-ray examination against the potential harm of radiation exposure. The effective dose allows comparison of different imaging procedures and helps clinicians make informed decisions. The ALARA principle (As Low As Reasonably Achievable) guides all medical radiation practices.

**中文：**
辐射剂量是医学物理学中的一个关键概念，因为它平衡了X射线检查的诊断益处与辐射暴露的潜在危害。有效剂量允许比较不同的成像程序，帮助临床医生做出明智的决定。ALARA原则（合理可行尽量低）指导所有医学辐射实践。

### Common Misconceptions / 常见误区
- **English:** Students often confuse absorbed dose (Gy) with equivalent dose (Sv). Remember: Gy measures energy deposited; Sv measures biological effect.
- **中文：** 学生常混淆吸收剂量（Gy）和等效剂量（Sv）。记住：Gy测量沉积的能量；Sv测量生物效应。
- **English:** Another misconception is that all radiation is equally harmful. The radiation weighting factor $w_R$ accounts for different biological effectiveness (e.g., alpha particles have $w_R = 20$, meaning they are 20 times more damaging than X-rays for the same absorbed dose).
- **中文：** 另一个误解是所有辐射同样有害。辐射权重因子 $w_R$ 考虑了不同的生物效应（例如，α粒子的 $w_R = 20$，意味着对于相同的吸收剂量，它们的危害是X射线的20倍）。

### Exam Tips / 考试提示
**English:**
- Be able to calculate absorbed dose, equivalent dose, and effective dose.
- Know the units (Gy for absorbed dose, Sv for equivalent and effective dose).
- Understand the ALARA principles and how they are applied in practice.
- Be able to compare the radiation doses from different imaging procedures.
- Understand the difference between deterministic and stochastic effects.

**中文：**
- 能够计算吸收剂量、等效剂量和有效剂量。
- 知道单位（Gy用于吸收剂量，Sv用于等效和有效剂量）。
- 理解ALARA原则及其在实践中的应用。
- 能够比较不同成像程序的辐射剂量。
- 理解确定性效应和随机性效应之间的区别。

> 📷 **IMAGE PROMPT — [DOS-01]: Radiation Dose Comparison Chart**
>
> A bar chart comparing effective doses of different medical imaging procedures: chest X-ray (0.02 mSv), dental X-ray (0.005 mSv), mammogram (0.4 mSv), head CT (2 mSv), abdomen CT (8 mSv), and annual background radiation (2-3 mSv). Bars are color-coded from green (low dose) to red (high dose). Labels in English and Chinese. Clean infographic style.

---

# 5. Essential Equations / 核心公式

## 5.1 Minimum Wavelength of X-rays / X射线的最小波长

**Equation / 公式:**
$$ \lambda_{min} = \frac{hc}{eV} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\lambda_{min}$ | Minimum wavelength of X-rays | X射线的最小波长 | m |
| $h$ | Planck's constant | 普朗克常数 | J s |
| $c$ | Speed of light in vacuum | 真空中的光速 | m s$^{-1}$ |
| $e$ | Elementary charge | 元电荷 | C |
| $V$ | Accelerating voltage | 加速电压 | V |

**Derivation / 推导:**
**English:**
When an electron is accelerated through a potential difference $V$, it gains kinetic energy $eV$. If this entire kinetic energy is converted into a single X-ray photon, the photon has maximum energy $E_{max} = eV$. Using the photon energy equation $E = hf = \frac{hc}{\lambda}$, we get:
$$ eV = \frac{hc}{\lambda_{min}} $$
Rearranging:
$$ \lambda_{min} = \frac{hc}{eV} $$

**中文：**
当电子通过电势差 $V$ 加速时，它获得动能 $eV$。如果这整个动能转化为单个X射线光子，则光子具有最大能量 $E_{max} = eV$。使用光子能量方程 $E = hf = \frac{hc}{\lambda}$，我们得到：
$$ eV = \frac{hc}{\lambda_{min}} $$
整理：
$$ \lambda_{min} = \frac{hc}{eV} $$

**Conditions / 适用条件:**
**English:** This equation applies when all the kinetic energy of a single electron is converted into a single X-ray photon in a single bremsstrahlung event. This gives the shortest possible wavelength (highest energy) in the X-ray spectrum.
**中文：** 该方程适用于单个电子的全部动能在一个轫致辐射事件中转化为单个X射线光子时。这给出了X射线谱中最短的波长（最高能量）。

**Limitations / 局限性:**
**English:** This is the theoretical minimum wavelength. In practice, most electrons undergo multiple interactions and lose energy in stages, producing longer wavelengths. The minimum wavelength is a sharp cutoff in the spectrum.
**中文：** 这是理论最小波长。实际上，大多数电子经历多次相互作用并分阶段损失能量，产生更长的波长。最小波长是谱中的尖锐截止。

**Rearrangements / 变形:**
$$ V = \frac{hc}{e\lambda_{min}} $$
$$ h = \frac{eV\lambda_{min}}{c} $$

---

## 5.2 Exponential Attenuation Law / 指数衰减定律

**Equation / 公式:**
$$ I = I_0 e^{-\mu x} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $I$ | Transmitted intensity | 透射强度 | W m$^{-2}$ or counts s$^{-1}$ |
| $I_0$ | Initial intensity | 初始强度 | W m$^{-2}$ or counts s$^{-1}$ |
| $\mu$ | Linear attenuation coefficient | 线性衰减系数 | m$^{-1}$ |
| $x$ | Thickness of material | 材料厚度 | m |

**Derivation / 推导:**
**English:**
Consider a thin slab of material of thickness $\Delta x$. The fraction of X-rays absorbed is proportional to the thickness:
$$ \frac{\Delta I}{I} = -\mu \Delta x $$
In the limit $\Delta x \to 0$:
$$ \frac{dI}{dx} = -\mu I $$
This is a first-order differential equation. Separating variables:
$$ \frac{dI}{I} = -\mu dx $$
Integrating:
$$ \int_{I_0}^{I} \frac{dI}{I} = -\mu \int_{0}^{x} dx $$
$$ \ln I - \ln I_0 = -\mu x $$
$$ \ln \left(\frac{I}{I_0}\right) = -\mu x $$
$$ \frac{I}{I_0} = e^{-\mu x} $$
$$ I = I_0 e^{-\mu x} $$

**中文：**
考虑厚度为 $\Delta x$ 的薄材料片。吸收的X射线比例与厚度成正比：
$$ \frac{\Delta I}{I} = -\mu \Delta x $$
在极限 $\Delta x \to 0$ 时：
$$ \frac{dI}{dx} = -\mu I $$
这是一阶微分方程。分离变量：
$$ \frac{dI}{I} = -\mu dx $$
积分：
$$ \int_{I_0}^{I} \frac{dI}{I} = -\mu \int_{0}^{x} dx $$
$$ \ln I - \ln I_0 = -\mu x $$
$$ \ln \left(\frac{I}{I_0}\right) = -\mu x $$
$$ \frac{I}{I_0} = e^{-\mu x} $$
$$ I = I_0 e^{-\mu x} $$

**Conditions / 适用条件:**
**English:** This equation applies for narrow-beam (good geometry) conditions where scattered radiation is not detected. It assumes a homogeneous material and monoenergetic X-rays. In practice, it is a good approximation for most medical imaging situations.
**中文：** 该方程适用于窄束（良好几何）条件，其中散射辐射不被检测。它假设均匀材料和单能X射线。在实践中，它对大多数医学成像情况是一个很好的近似。

**Limitations / 局限性:**
**English:** For broad-beam geometry (where scattered radiation is detected), the attenuation is less than predicted because scattered photons can still reach the detector. For polyenergetic X-rays (as in real X-ray tubes), the effective attenuation coefficient changes with thickness because lower energy photons are preferentially absorbed (beam hardening).
**中文：** 对于宽束几何（其中检测到散射辐射），衰减小于预测，因为散射光子仍可到达探测器。对于多能X射线（如在实际X射线管中），有效衰减系数随厚度变化，因为较低能量的光子被优先吸收（束硬化）。

**Rearrangements / 变形:**
$$ \mu = -\frac{1}{x} \ln\left(\frac{I}{I_0}\right) $$
$$ x = -\frac{1}{\mu} \ln\left(\frac{I}{I_0}\right) $$
$$ \frac{I}{I_0} = e^{-\mu x} $$

---

## 5.3 Half-Value Thickness (HVT) / 半值厚度

**Equation / 公式:**
$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{\mu} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $HVT$ | Half-value thickness | 半值厚度 | m |
| $\mu$ | Linear attenuation coefficient | 线性衰减系数 | m$^{-1}$ |
| $\ln 2$ | Natural logarithm of 2 | 2的自然对数 | dimensionless |

**Derivation / 推导:**
**English:**
By definition, when $x = HVT$, $I = I_0/2$. Substituting into the exponential attenuation law:
$$ \frac{I_0}{2} = I_0 e^{-\mu \cdot HVT} $$
$$ \frac{1}{2} = e^{-\mu \cdot HVT} $$
Taking natural logarithms:
$$ \ln\left(\frac{1}{2}\right) = -\mu \cdot HVT $$
$$ -\ln 2 = -\mu \cdot HVT $$
$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{\mu} $$

**中文：**
根据定义，当 $x = HVT$ 时，$I = I_0/2$。代入指数衰减定律：
$$ \frac{I_0}{2} = I_0 e^{-\mu \cdot HVT} $$
$$ \frac{1}{2} = e^{-\mu \cdot HVT} $$
取自然对数：
$$ \ln\left(\frac{1}{2}\right) = -\mu \cdot HVT $$
$$ -\ln 2 = -\mu \cdot HVT $$
$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{\mu} $$

**Conditions / 适用条件:**
**English:** Same as for the exponential attenuation law. The HVT is a convenient way to express the penetrating power of X-rays in a given material.
**中文：** 与指数衰减定律相同。HVT是表达X射线在给定材料中穿透力的便捷方式。

**Limitations / 局限性:**
**English:** For polyenergetic beams, the HVT is not constant — it increases with thickness because the beam becomes harder (higher average energy) as lower energy photons are preferentially absorbed. This is called beam hardening.
**中文：** 对于多能束，HVT不是常数——它随厚度增加而增加，因为随着较低能量光子被优先吸收，束变得更硬（平均能量更高）。这称为束硬化。

**Rearrangements / 变形:**
$$ \mu = \frac{\ln 2}{HVT} = \frac{0.693}{HVT} $$

---

## 5.4 Absorbed Dose / 吸收剂量

**Equation / 公式:**
$$ D = \frac{E}{m} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $D$ | Absorbed dose | 吸收剂量 | Gy (J kg$^{-1}$) |
| $E$ | Energy absorbed | 吸收的能量 | J |
| $m$ | Mass of tissue | 组织质量 | kg |

**Derivation / 推导:**
**English:**
This is a definition, not a derived equation. The absorbed dose is the fundamental quantity for radiation dosimetry. It measures how much energy is deposited per unit mass of tissue.
**中文：**
这是一个定义，不是推导方程。吸收剂量是辐射剂量学的基本量。它测量单位质量组织沉积了多少能量。

**Conditions / 适用条件:**
**English:** Applies to any type of ionizing radiation and any material. It is the starting point for calculating equivalent and effective doses.
**中文：** 适用于任何类型的电离辐射和任何材料。它是计算等效和有效剂量的起点。

**Limitations / 局限性:**
**English:** Absorbed dose alone does not account for the different biological effectiveness of different radiation types (e.g., alpha particles cause more damage per unit energy deposited than X-rays). This is addressed by the equivalent dose.
**中文：** 吸收剂量单独不说明不同辐射类型的不同生物效应（例如，α粒子每单位沉积能量造成的损害比X射线更大）。这由等效剂量解决。

**Rearrangements / 变形:**
$$ E = D \times m $$
$$ m = \frac{E}{D} $$

---

## 5.5 Equivalent Dose / 等效剂量

**Equation / 公式:**
$$ H_T = D \times w_R $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $H_T$ | Equivalent dose to tissue T | 组织T的等效剂量 | Sv |
| $D$ | Absorbed dose | 吸收剂量 | Gy |
| $w_R$ | Radiation weighting factor | 辐射权重因子 | dimensionless |

**Derivation / 推导:**
**English:**
This is a definition. The radiation weighting factor $w_R$ accounts for the relative biological effectiveness (RBE) of different radiation types. For X-rays, gamma rays, and beta particles, $w_R = 1$. For alpha particles, $w_R = 20$. For neutrons, $w_R$ varies with energy (typically 5-20).
**中文：**
这是一个定义。辐射权重因子 $w_R$ 考虑了不同辐射类型的相对生物效应（RBE）。对于X射线、伽马射线和β粒子，$w_R = 1$。对于α粒子，$w_R = 20$。对于中子，$w_R$ 随能量变化（通常5-20）。

**Conditions / 适用条件:**
**English:** Applies to any tissue and any radiation type. The equivalent dose allows comparison of biological risk from different radiation types.
**中文：** 适用于任何组织和任何辐射类型。等效剂量允许比较不同辐射类型的生物风险。

**Limitations / 局限性:**
**English:** Equivalent dose does not account for the different radiosensitivity of different tissues. This is addressed by the effective dose.
**中文：** 等效剂量不说明不同组织的不同辐射敏感性。这由有效剂量解决。

**Rearrangements / 变形:**
$$ D = \frac{H_T}{w_R} $$

---

## 5.6 Effective Dose / 有效剂量

**Equation / 公式:**
$$ E = \sum_T H_T \times w_T = \sum_T D \times w_R \times w_T $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Effective dose | 有效剂量 | Sv |
| $H_T$ | Equivalent dose to tissue T | 组织T的等效剂量 | Sv |
| $w_T$ | Tissue weighting factor | 组织权重因子 | dimensionless |
| $D$ | Absorbed dose | 吸收剂量 | Gy |
| $w_R$ | Radiation weighting factor | 辐射权重因子 | dimensionless |

**Derivation / 推导:**
**English:**
This is a definition. The tissue weighting factors $w_T$ represent the fraction of total health risk contributed by each tissue when the whole body is uniformly irradiated. The sum of all $w_T$ equals 1. Examples: gonads $w_T = 0.20$, bone marrow $w_T = 0.12$, lung $w_T = 0.12$, thyroid $w_T = 0.05$, skin $w_T = 0.01$.
**中文：**
这是一个定义。组织权重因子 $w_T$ 代表当全身均匀照射时每个组织对总健康风险的贡献比例。所有 $w_T$ 之和等于1。示例：性腺 $w_T = 0.20$，骨髓 $w_T = 0.12$，肺 $w_T = 0.12$，甲状腺 $w_T = 0.05$，皮肤 $w_T = 0.01$。

**Conditions / 适用条件:**
**English:** Applies to any exposure scenario. The effective dose allows comparison of overall risk from different types of exposure (e.g., comparing a chest X-ray to a CT scan).
**中文：** 适用于任何暴露场景。有效剂量允许比较不同类型暴露的整体风险（例如，比较胸部X射线与CT扫描）。

**Limitations / 局限性:**
**English:** Effective dose is a population-averaged quantity and should not be used for individual risk assessment. It is most useful for comparing different imaging procedures and for regulatory purposes.
**中文：** 有效剂量是人口平均量，不应用于个体风险评估。它最适用于比较不同成像程序和监管目的。

**Rearrangements / 变形:**
For a single tissue: $E = H_T \times w_T = D \times w_R \times w_T$

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 X-ray Spectrum / X射线谱

### Axes / 坐标轴
**English:** X-axis: Wavelength ($\lambda$) in nm or pm, or Photon Energy ($E$) in keV. Y-axis: X-ray Intensity (arbitrary units) or Number of Photons.
**中文：** X轴：波长（$\lambda$）以nm或pm为单位，或光子能量（$E$）以keV为单位。Y轴：X射线强度（任意单位）或光子数。

### Shape / 形状
**English:** The spectrum has a continuous background (bremsstrahlung) with a sharp cutoff at $\lambda_{min}$, rising to a peak at about $1.5\lambda_{min}$, then gradually decreasing. Superimposed on this are sharp peaks (characteristic X-rays) at specific wavelengths.
**中文：** 谱具有连续背景（轫致辐射），在 $\lambda_{min}$ 处有尖锐截止，在大约 $1.5\lambda_{min}$ 处上升到峰值，然后逐渐减小。在此之上叠加了特定波长处的尖锐峰值（特征X射线）。

### Gradient Meaning / 斜率含义
**English:** The gradient of the spectrum at any point represents the rate of change of intensity with wavelength. The gradient is zero at the peak intensity and at the cutoff. The gradient is positive from $\lambda_{min}$ to the peak, and negative from the peak to longer wavelengths.
**中文：** 谱在任何点的斜率代表强度随波长的变化率。在峰值强度和截止处斜率为零。从 $\lambda_{min}$ 到峰值斜率为正，从峰值到较长波长斜率为负。

### Area Meaning / 面积含义
**English:** The area under the spectrum curve represents the total X-ray intensity (total power) emitted. The area under the continuous part represents bremsstrahlung intensity; the area under the characteristic peaks represents characteristic X-ray intensity.
**中文：** 谱曲线下的面积代表发射的总X射线强度（总功率）。连续部分下的面积代表轫致辐射强度；特征峰下的面积代表特征X射线强度。

### Exam Interpretation / 考试解读
**English:**
- A higher accelerating voltage shifts the entire spectrum to shorter wavelengths (higher energies) and increases the total intensity.
- Changing the target material changes the positions of characteristic peaks but does not significantly affect the continuous spectrum shape.
- The minimum wavelength $\lambda_{min}$ is determined solely by the accelerating voltage, not by the target material.

**中文：**
- 更高的加速电压将整个谱移至更短波长（更高能量）并增加总强度。
- 改变靶材料改变特征峰的位置，但不显著影响连续谱形状。
- 最小波长 $\lambda_{min}$ 仅由加速电压决定，不由靶材料决定。

### Common Questions / 常见问题
**English:**
- Calculate $\lambda_{min}$ given the accelerating voltage.
- Explain why the intensity drops to zero at $\lambda_{min}$.
- Explain why characteristic peaks appear at specific wavelengths.
- Describe the effect of increasing the accelerating voltage on the spectrum.

**中文：**
- 给定加速电压计算 $\lambda_{min}$。
- 解释为什么强度在 $\lambda_{min}$ 处降至零。
- 解释为什么特征峰出现在特定波长。
- 描述增加加速电压对谱的影响。

> 📷 **IMAGE PROMPT — [GRP-01]: X-ray Spectrum with Annotations**
>
> A graph of X-ray intensity vs. wavelength showing: the continuous bremsstrahlung spectrum with $\lambda_{min}$ marked, the peak intensity at $1.5\lambda_{min}$, two characteristic peaks ($K_\alpha$ and $K_\beta$) labeled, and a second curve (dashed) showing the effect of higher voltage. Annotations in English and Chinese. Clean scientific graph style.

---

## 6.2 Exponential Attenuation Curve / 指数衰减曲线

### Axes / 坐标轴
**English:** X-axis: Thickness of material ($x$) in mm or cm. Y-axis: X-ray Intensity ($I$) in W m$^{-2}$ or relative intensity ($I/I_0$).
**中文：** X轴：材料厚度（$x$）以mm或cm为单位。Y轴：X射线强度（$I$）以W m$^{-2}$或相对强度（$I/I_0$）为单位。

### Shape / 形状
**English:** The curve is an exponential decay: it starts at $I_0$ at $x=0$, decreases rapidly at first, then more slowly, asymptotically approaching zero but never reaching it.
**中文：** 曲线是指数衰减：在 $x=0$ 处从 $I_0$ 开始，最初快速下降，然后更慢，渐近接近零但从未达到。

### Gradient Meaning / 斜率含义
**English:** The gradient at any point is $dI/dx = -\mu I$, which is proportional to the intensity at that point. The gradient is steepest at $x=0$ and becomes shallower as $x$ increases. The gradient is always negative.
**中文：** 任何点的斜率为 $dI/dx = -\mu I$，与该点的强度成正比。斜率在 $x=0$ 处最陡，随 $x$ 增加而变浅。斜率始终为负。

### Area Meaning / 面积含义
**English:** The area under the curve from $x=0$ to $x=\infty$ represents the total energy absorbed by the material (if intensity is in power per unit area). More practically, the area under a semi-log plot ($\ln I$ vs $x$) is not typically used.
**中文：** 从 $x=0$ 到 $x=\infty$ 的曲线下面积代表材料吸收的总能量（如果强度是单位面积功率）。更实际地，半对数图（$\ln I$ 与 $x$）下的面积通常不使用。

### Exam Interpretation / 考试解读
**English:**
- A steeper curve indicates a higher attenuation coefficient $\mu$ (less penetrating radiation).
- The HVT can be read directly from the graph: find the thickness where $I = I_0/2$.
- On a semi-log plot ($\ln I$ vs $x$), the data should form a straight line with gradient $-\mu$.
- A non-linear semi-log plot indicates a polyenergetic beam (beam hardening).

**中文：**
- 更陡的曲线表示更高的衰减系数 $\mu$（穿透力更弱的辐射）。
- 可以直接从图中读取HVT：找到 $I = I_0/2$ 处的厚度。
- 在半对数图（$\ln I$ 与 $x$）上，数据应形成斜率为 $-\mu$ 的直线。
- 非线性的半对数图表示多能束（束硬化）。

### Common Questions / 常见问题
**English:**
- Determine $\mu$ from a graph of $I$ vs $x$.
- Determine HVT from a graph.
- Explain why the curve is exponential.
- Compare the attenuation of different materials from their curves.

**中文：**
- 从 $I$ 与 $x$ 的图中确定 $\mu$。
- 从图中确定HVT。
- 解释为什么曲线是指数的。
- 从曲线比较不同材料的衰减。

> 📷 **IMAGE PROMPT — [GRP-02]: Exponential Attenuation Graph**
>
> A graph of relative X-ray intensity ($I/I_0$) vs. thickness showing: an exponential decay curve starting at 1.0, with HVT marked at $I/I_0 = 0.5$, 2HVT at 0.25, 3HVT at 0.125. A second curve (dashed) shows a material with higher $\mu$ (steeper decay). Inset shows the same data on a semi-log plot ($\ln(I/I_0)$ vs. thickness) forming a straight line. Clean scientific graph style.

---

# 7. Required Diagrams / 必备图表

## 7.1 X-ray Tube Diagram / X射线管图

### Description / 描述
**English:**
A cross-sectional diagram of an X-ray tube showing all key components: the glass vacuum envelope, the heated tungsten filament (cathode) with a focusing cup, the rotating tungsten anode (target) angled at about 20 degrees, the beryllium window for X-ray output, lead shielding around the tube, and the cooling system (oil or water). The electron beam from cathode to anode should be shown, as well as the X-ray beam emerging through the window.

**中文：**
X射线管的横截面图，显示所有关键组件：玻璃真空外壳、带聚焦杯的加热钨丝（阴极）、以约20度角倾斜的旋转钨阳极（靶）、用于X射线输出的铍窗、管周围的铅屏蔽以及冷却系统（油或水）。应显示从阴极到阳极的电子束，以及通过窗口射出的X射线束。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [DIA-01]: X-ray Tube Cross-section**
>
> A detailed cross-sectional diagram of an X-ray tube. The glass vacuum envelope is shown as a transparent cylinder. Inside: a coiled tungsten filament (cathode) at the top, surrounded by a metal focusing cup. Below it, a rotating tungsten anode (target) is shown as a disc angled at 20 degrees to the horizontal. A beryllium window is on the side of the tube. Lead shielding surrounds the tube except at the window. Cooling oil channels are shown around the anode. The electron beam is shown as a dashed line from cathode to anode. The X-ray beam is shown as a cone emerging through the window. All components labeled in English and Chinese. Clean technical illustration style with color coding: red for high voltage components, blue for cooling, yellow for X-ray beam.

### Labels Required / 需要标注
- Cathode (filament) / 阴极（灯丝）
- Focusing cup / 聚焦杯
- Anode (target) / 阳极（靶）
- Rotating anode / 旋转阳极
- Beryllium window / 铍窗
- Lead shielding / 铅屏蔽
- Cooling system / 冷却系统
- Electron beam / 电子束
- X-ray beam / X射线束
- Vacuum envelope / 真空外壳

### Exam Importance / 考试重要性
**English:** This is a standard diagram that students must be able to draw and label. Questions often ask about the function of each component, why the anode is rotated, why the tube is evacuated, and why beryllium is used for the window.
**中文：** 这是学生必须能够绘制和标注的标准图。问题常问每个组件的功能、为什么阳极旋转、为什么管是真空的以及为什么使用铍做窗口。

---

## 7.2 X-ray Spectrum Graph / X射线谱图

### Description / 描述
**English:**
A graph showing X-ray intensity (y-axis) versus wavelength (x-axis). The continuous bremsstrahlung spectrum rises from zero at $\lambda_{min}$ to a peak at about $1.5\lambda_{min}$, then gradually decreases. Two sharp characteristic peaks ($K_\alpha$ and $K_\beta$) are superimposed on the continuous background. A second curve (dashed) shows the effect of higher accelerating voltage.

**中文：**
显示X射线强度（y轴）与波长（x轴）的关系图。连续轫致辐射谱从 $\lambda_{min}$ 处的零上升到约 $1.5\lambda_{min}$ 处的峰值，然后逐渐减小。两个尖锐的特征峰（$K_\alpha$ 和 $K_\beta$）叠加在连续背景上。第二条曲线（虚线）显示更高加速电压的效果。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [DIA-02]: X-ray Spectrum**
>
> A graph of X-ray intensity (arbitrary units) vs. wavelength (pm). The main curve shows: a sharp rise from zero at $\lambda_{min}$ (labeled), a peak at $1.5\lambda_{min}$, then a gradual decrease. Two sharp peaks labeled $K_\alpha$ and $K_\beta$ are shown at specific wavelengths. A dashed curve shows the spectrum at a higher accelerating voltage (shifted left and higher). Axes labeled with units. Clean scientific graph style with grid lines. Annotations in English and Chinese.

### Labels Required / 需要标注
- $\lambda_{min}$ (minimum wavelength) / 最小波长
- Peak intensity / 峰值强度
- $K_\alpha$ characteristic peak / $K_\alpha$ 特征峰
- $K_\beta$ characteristic peak / $K_\beta$ 特征峰
- Continuous spectrum (bremsstrahlung) / 连续谱（轫致辐射）
- Characteristic spectrum / 特征谱
- Higher voltage curve / 更高电压曲线

### Exam Importance / 考试重要性
**English:** Students must be able to sketch and interpret this graph. Questions often ask to identify the continuous and characteristic components, explain the shape, calculate $\lambda_{min}$, and describe the effect of changing voltage or target material.
**中文：** 学生必须能够绘制和解释此图。问题常要求识别连续和特征分量，解释形状，计算 $\lambda_{min}$，并描述改变电压或靶材料的效果。

---

## 7.3 CT Scanner Diagram / CT扫描仪图

### Description / 描述
**English:**
A cross-sectional diagram of a CT scanner showing the patient lying on a table, the X-ray tube on one side, the detector array on the opposite side, and the rotation path of the tube-detector assembly. An inset shows a reconstructed cross-sectional image of the brain or abdomen.

**中文：**
CT扫描仪的横截面图，显示患者躺在桌子上，X射线管在一侧，探测器阵列在另一侧，以及管-探测器组件的旋转路径。插图示出大脑或腹部的重建横截面图像。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [DIA-03]: CT Scanner Cross-section**
>
> A cross-sectional diagram of a CT scanner. A patient is shown lying supine on a table. An X-ray tube is shown on the left side of the patient, emitting a fan-shaped X-ray beam. A curved detector array is shown on the right side. A dashed circle shows the rotation path of the tube-detector assembly. Arrows indicate rotation direction. An inset in the top-right corner shows a reconstructed CT image of a brain cross-section with gray matter, white matter, and ventricles visible. All components labeled in English and Chinese. Clean technical illustration style.

### Labels Required / 需要标注
- X-ray tube / X射线管
- Detector array / 探测器阵列
- Fan beam / 扇形束
- Rotation path / 旋转路径
- Patient table / 患者床
- Reconstructed image / 重建图像
- CT slice / CT切片

### Exam Importance / 考试重要性
**English:** Students must understand the principle of CT scanning: multiple projections from different angles, computer reconstruction, and the advantages over conventional X-rays. Questions often ask to explain how CT produces cross-sectional images and why it has better contrast resolution.
**中文：** 学生必须理解CT扫描的原理：从不同角度获取多个投影、计算机重建以及相对于常规X射线的优势。问题常要求解释CT如何产生横截面图像以及为什么它具有更好的对比度分辨率。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Minimum Wavelength / 计算最小波长

### Question / 题目
**English:**
An X-ray tube operates at an accelerating voltage of 80 kV. Calculate:
(a) The minimum wavelength of the X-rays produced.
(b) The maximum energy of the X-ray photons in eV and in J.
(c) The frequency of the X-ray photons with the minimum wavelength.

(Use $h = 6.63 \times 10^{-34}$ J s, $c = 3.00 \times 10^8$ m s$^{-1}$, $e = 1.60 \times 10^{-19}$ C)

**中文：**
一个X射线管在80 kV的加速电压下工作。计算：
(a) 产生的X射线的最小波长。
(b) X射线光子的最大能量，以eV和J为单位。
(c) 具有最小波长的X射线光子的频率。

（使用 $h = 6.63 \times 10^{-34}$ J s，$c = 3.00 \times 10^8$ m s$^{-1}$，$e = 1.60 \times 10^{-19}$ C）

### Solution / 解答

**Step 1: Calculate the minimum wavelength**
**English:**
Using the Duane-Hunt law:
$$ \lambda_{min} = \frac{hc}{eV} $$

Substitute values:
$$ \lambda_{min} = \frac{(6.63 \times 10^{-34})(3.00 \times 10^8)}{(1.60 \times 10^{-19})(80 \times 10^3)} $$

$$ \lambda_{min} = \frac{1.989 \times 10^{-25}}{1.28 \times 10^{-14}} $$

$$ \lambda_{min} = 1.55 \times 10^{-11} \text{ m} = 0.0155 \text{ nm} = 15.5 \text{ pm} $$

**中文：**
使用杜安-亨特定律：
$$ \lambda_{min} = \frac{hc}{eV} $$

代入数值：
$$ \lambda_{min} = \frac{(6.63 \times 10^{-34})(3.00 \times 10^8)}{(1.60 \times 10^{-19})(80 \times 10^3)} $$

$$ \lambda_{min} = \frac{1.989 \times 10^{-25}}{1.28 \times 10^{-14}} $$

$$ \lambda_{min} = 1.55 \times 10^{-11} \text{ m} = 0.0155 \text{ nm} = 15.5 \text{ pm} $$

**Step 2: Calculate the maximum energy**
**English:**
The maximum energy of an X-ray photon equals the kinetic energy of the electron:
$$ E_{max} = eV = (1.60 \times 10^{-19})(80 \times 10^3) = 1.28 \times 10^{-14} \text{ J} $$

In electron volts:
$$ E_{max} = 80 \text{ keV} = 80,000 \text{ eV} $$

**中文：**
X射线光子的最大能量等于电子的动能：
$$ E_{max} = eV = (1.60 \times 10^{-19})(80 \times 10^3) = 1.28 \times 10^{-14} \text{ J} $$

以电子伏特为单位：
$$ E_{max} = 80 \text{ keV} = 80,000 \text{ eV} $$

**Step 3: Calculate the frequency**
**English:**
Using $E = hf$:
$$ f = \frac{E}{h} = \frac{1.28 \times 10^{-14}}{6.63 \times 10^{-34}} = 1.93 \times 10^{19} \text{ Hz} $$

Alternatively, using $c = f\lambda$:
$$ f = \frac{c}{\lambda_{min}} = \frac{3.00 \times 10^8}{1.55 \times 10^{-11}} = 1.94 \times 10^{19} \text{ Hz} $$

**中文：**
使用 $E = hf$：
$$ f = \frac{E}{h} = \frac{1.28 \times 10^{-14}}{6.63 \times 10^{-34}} = 1.93 \times 10^{19} \text{ Hz} $$

或者，使用 $c = f\lambda$：
$$ f = \frac{c}{\lambda_{min}} = \frac{3.00 \times 10^8}{1.55 \times 10^{-11}} = 1.94 \times 10^{19} \text{ Hz} $$

### Final Answer / 最终答案
**Answer:**
(a) $\lambda_{min} = 1.55 \times 10^{-11}$ m (15.5 pm)
(b) $E_{max} = 1.28 \times 10^{-14}$ J = 80 keV
(c) $f = 1.93 \times 10^{19}$ Hz

**答案：**
(a) $\lambda_{min} = 1.55 \times 10^{-11}$ m (15.5 pm)
(b) $E_{max} = 1.28 \times 10^{-14}$ J = 80 keV
(c) $f = 1.93 \times 10^{19}$ Hz

### Examiner Notes / 考官点评
**English:**
- Common mistake: forgetting to convert kV to V (80 kV = 80,000 V = $8 \times 10^4$ V).
- Common mistake: using the wrong formula — some students try to use $E = hf$ directly without relating it to the accelerating voltage.
- Always check units: $\lambda_{min}$ should be in meters (typically $10^{-11}$ to $10^{-10}$ m).
- The answer in pm (picometers) is also acceptable: 15.5 pm.

**中文：**
- 常见错误：忘记将kV转换为V（80 kV = 80,000 V = $8 \times 10^4$ V）。
- 常见错误：使用错误的公式——有些学生试图直接使用 $E = hf$ 而不将其与加速电压联系起来。
- 始终检查单位：$\lambda_{min}$ 应以米为单位（通常 $10^{-11}$ 到 $10^{-10}$ m）。
- 以pm（皮米）为单位的答案也可接受：15.5 pm。

---

## Example 2: Attenuation and Half-Value Thickness / 衰减与半值厚度

### Question / 题目
**English:**
A narrow beam of monoenergetic X-rays passes through a 5.0 mm thick sheet of lead. The intensity of the transmitted beam is 12% of the incident intensity.

(a) Calculate the linear attenuation coefficient $\mu$ for lead at this X-ray energy.
(b) Calculate the half-value thickness (HVT) of lead for these X-rays.
(c) What thickness of lead would be required to reduce the intensity to 1% of its initial value?

**中文：**
一束单能X射线的窄束穿过5.0 mm厚的铅板。透射束的强度是入射强度的12%。

(a) 计算在此X射线能量下铅的线性衰减系数 $\mu$。
(b) 计算这些X射线的铅半值厚度（HVT）。
(c) 需要多厚的铅才能将强度降低到初始值的1%？

### Solution / 解答

**Step 1: Calculate the attenuation coefficient**
**English:**
Using the exponential attenuation law:
$$ I = I_0 e^{-\mu x} $$

Given $I/I_0 = 0.12$ and $x = 5.0 \text{ mm} = 5.0 \times 10^{-3} \text{ m}$:

$$ 0.12 = e^{-\mu \times 5.0 \times 10^{-3}} $$

Taking natural logarithms:
$$ \ln(0.12) = -\mu \times 5.0 \times 10^{-3} $$

$$ -2.12 = -\mu \times 5.0 \times 10^{-3} $$

$$ \mu = \frac{2.12}{5.0 \times 10^{-3}} = 424 \text{ m}^{-1} $$

**中文：**
使用指数衰减定律：
$$ I = I_0 e^{-\mu x} $$

给定 $I/I_0 = 0.12$ 和 $x = 5.0 \text{ mm} = 5.0 \times 10^{-3} \text{ m}$：

$$ 0.12 = e^{-\mu \times 5.0 \times 10^{-3}} $$

取自然对数：
$$ \ln(0.12) = -\mu \times 5.0 \times 10^{-3} $$

$$ -2.12 = -\mu \times 5.0 \times 10^{-3} $$

$$ \mu = \frac{2.12}{5.0 \times 10^{-3}} = 424 \text{ m}^{-1} $$

**Step 2: Calculate the half-value thickness**
**English:**
$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{424} = 1.63 \times 10^{-3} \text{ m} = 1.63 \text{ mm} $$

**中文：**
$$ HVT = \frac{\ln 2}{\mu} = \frac{0.693}{424} = 1.63 \times 10^{-3} \text{ m} = 1.63 \text{ mm} $$

**Step 3: Calculate thickness for 1% transmission**
**English:**
We want $I/I_0 = 0.01$:
$$ 0.01 = e^{-\mu x} $$

$$ \ln(0.01) = -\mu x $$

$$ -4.605 = -424x $$

$$ x = \frac{4.605}{424} = 0.0109 \text{ m} = 10.9 \text{ mm} $$

Alternatively, using the HVT:
Number of HVTs needed: $0.5^n = 0.01$, so $n = \frac{\ln(0.01)}{\ln(0.5)} = \frac{-4.605}{-0.693} = 6.65$ HVTs.
Thickness = $6.65 \times 1.63 = 10.8 \text{ mm}$ (slight difference due to rounding).

**中文：**
我们想要 $I/I_0 = 0.01$：
$$ 0.01 = e^{-\mu x} $$

$$ \ln(0.01) = -\mu x $$

$$ -4.605 = -424x $$

$$ x = \frac{4.605}{424} = 0.0109 \text{ m} = 10.9 \text{ mm} $$

或者，使用HVT：
所需HVT数量：$0.5^n = 0.01$，所以 $n = \frac{\ln(0.01)}{\ln(0.5)} = \frac{-4.605}{-0.693} = 6.65$ 个HVT。
厚度 = $6.65 \times 1.63 = 10.8 \text{ mm}$（由于四舍五入略有差异）。

### Final Answer / 最终答案
**Answer:**
(a) $\mu = 424 \text{ m}^{-1}$
(b) $HVT = 1.63 \text{ mm}$
(c) $x = 10.9 \text{ mm}$

**答案：**
(a) $\mu = 424 \text{ m}^{-1}$
(b) $HVT = 1.63 \text{ mm}$
(c) $x = 10.9 \text{ mm}$

### Examiner Notes / 考官点评
**English:**
- Common mistake: forgetting to convert mm to m for the calculation of $\mu$ (but HVT can be given in mm).
- Common mistake: using $\ln$ instead of $\log_{10}$ or vice versa. Always use natural log ($\ln$) for exponential decay.
- The HVT method in part (c) is a useful check: $0.5^{6.65} = 0.01$, confirming the answer.
- Always include units in the final answer.

**中文：**
- 常见错误：忘记将mm转换为m来计算 $\mu$（但HVT可以以mm为单位给出）。
- 常见错误：使用 $\ln$ 而不是 $\log_{10}$，反之亦然。对于指数衰减始终使用自然对数（$\ln$）。
- 部分(c)中的HVT方法是一个有用的检查：$0.5^{6.65} = 0.01$，确认答案。
- 始终在最终答案中包含单位。

---

## Example 3: Radiation Dose Calculation / 辐射剂量计算

### Question / 题目
**English:**
A patient receives a chest X-ray. The mass of tissue exposed is 25 kg. The total energy absorbed by the tissue is $5.0 \times 10^{-4}$ J.

(a) Calculate the absorbed dose in Gy.
(b) Calculate the equivalent dose in Sv (for X-rays, $w_R = 1$).
(c) If the chest has a tissue weighting factor $w_T = 0.12$, calculate the effective dose.
(d) Compare this effective dose to the annual background radiation of 2.5 mSv.

**中文：**
一名患者接受胸部X射线检查。暴露的组织质量为25 kg。组织吸收的总能量为 $5.0 \times 10^{-4}$ J。

(a) 计算以Gy为单位的吸收剂量。
(b) 计算以Sv为单位的等效剂量（对于X射线，$w_R = 1$）。
(c) 如果胸部的组织权重因子 $w_T = 0.12$，计算有效剂量。
(d) 将此有效剂量与2.5 mSv的年背景辐射进行比较。

### Solution / 解答

**Step 1: Calculate the absorbed dose**
**English:**
$$ D = \frac{E}{m} = \frac{5.0 \times 10^{-4}}{25} = 2.0 \times 10^{-5} \text{ Gy} = 20 \text{ μGy} $$

**中文：**
$$ D = \frac{E}{m} = \frac{5.0 \times 10^{-4}}{25} = 2.0 \times 10^{-5} \text{ Gy} = 20 \text{ μGy} $$

**Step 2: Calculate the equivalent dose**
**English:**
For X-rays, $w_R = 1$:
$$ H_T = D \times w_R = 2.0 \times 10^{-5} \times 1 = 2.0 \times 10^{-5} \text{ Sv} = 20 \text{ μSv} $$

**中文：**
对于X射线，$w_R = 1$：
$$ H_T = D \times w_R = 2.0 \times 10^{-5} \times 1 = 2.0 \times 10^{-5} \text{ Sv} = 20 \text{ μSv} $$

**Step 3: Calculate the effective dose**
**English:**
$$ E = H_T \times w_T = 2.0 \times 10^{-5} \times 0.12 = 2.4 \times 10^{-6} \text{ Sv} = 2.4 \text{ μSv} $$

**中文：**
$$ E = H_T \times w_T = 2.0 \times 10^{-5} \times 0.12 = 2.4 \times 10^{-6} \text{ Sv} = 2.4 \text{ μSv} $$

**Step 4: Compare with background radiation**
**English:**
Annual background = 2.5 mSv = 2500 μSv.
The chest X-ray effective dose (2.4 μSv) is about 0.1% of the annual background radiation. This is equivalent to about 3.5 hours of natural background exposure.

**中文：**
年背景 = 2.5 mSv = 2500 μSv。
胸部X射线有效剂量（2.4 μSv）约为年背景辐射的0.1%。这相当于约3.5小时的自然背景暴露。

### Final Answer / 最终答案
**Answer:**
(a) $D = 2.0 \times 10^{-5}$ Gy (20 μGy)
(b) $H_T = 2.0 \times 10^{-5}$ Sv (20 μSv)
(c) $E = 2.4 \times 10^{-6}$ Sv (2.4 μSv)
(d) The chest X-ray effective dose is about 0.1% of annual background radiation.

**答案：**
(a) $D = 2.0 \times 10^{-5}$ Gy (20 μGy)
(b) $H_T = 2.0 \times 10^{-5}$ Sv (20 μSv)
(c) $E = 2.4 \times 10^{-6}$ Sv (2.4 μSv)
(d) 胸部X射线有效剂量约为年背景辐射的0.1%。

### Examiner Notes / 考官点评
**English:**
- Common mistake: confusing Gy and Sv. Remember: Gy measures energy absorbed; Sv measures biological effect.
- Common mistake: forgetting to multiply by $w_T$ for effective dose.
- The effective dose is always less than or equal to the equivalent dose (since $w_T \leq 1$).
- For whole-body exposure, the sum of all $w_T$ values equals 1, so effective dose equals equivalent dose.

**中文：**
- 常见错误：混淆Gy和Sv。记住：Gy测量吸收的能量；Sv测量生物效应。
- 常见错误：忘记乘以 $w_T$ 来计算有效剂量。
- 有效剂量总是小于或等于等效剂量（因为 $w_T \leq 1$）。
- 对于全身暴露，所有 $w_T$ 值之和等于1，因此有效剂量等于等效剂量。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of $\lambda_{min}$ / 计算 $\lambda_{min}$ | High | Medium | 📝 *待填入* |
| X-ray spectrum interpretation / X射线谱解释 | High | Medium | 📝 *待填入* |
| Exponential attenuation calculation / 指数衰减计算 | High | Medium | 📝 *待填入* |
| HVT calculation / HVT计算 | High | Medium | 📝 *待填入* |
| X-ray tube diagram labeling / X射线管图标注 | Medium | Low | 📝 *待填入* |
| Contrast media explanation / 造影剂解释 | Medium | Medium | 📝 *待填入* |
| CT scan principles / CT扫描原理 | Medium | High | 📝 *待填入* |
| Radiation dose calculation / 辐射剂量计算 | Medium | Medium | 📝 *待填入* |
| ALARA principles / ALARA原则 | Low | Low | 📝 *待填入* |
| Comparison of imaging modalities / 成像方式比较 | Low | High | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词：**

| Command Word (EN) | Command Word (CN) | What is Required / 要求 |
|-------------------|-------------------|------------------------|
| State / 陈述 | 陈述 | A brief, concise answer without explanation |
| Define / 定义 | 定义 | A precise statement of the meaning of a term |
| Explain / 解释 | 解释 | Give reasons or causes, showing understanding |
| Describe / 描述 | 描述 | Give a detailed account of features or characteristics |
| Calculate / 计算 | 计算 | Use mathematical methods to find a numerical answer |
| Determine / 确定 | 确定 | Find a value using given data or a graph |
| Suggest / 建议 | 建议 | Apply knowledge to a new situation |
| Sketch / 绘制 | 绘制 | Draw a freehand graph or diagram |
| Compare / 比较 | 比较 | Describe similarities and differences |
| Discuss / 讨论 | 讨论 | Present arguments for and against |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This topic connects to practical skills in several ways:

**CAIE Paper 3 (AS) / Paper 5 (A2):**
- **Measurement of HVT:** Students may be asked to design an experiment to measure the half-value thickness of a material. This involves setting up an X-ray source (or gamma source as a substitute), a detector (Geiger-Müller tube), and absorbers of different thicknesses. The intensity is measured for each thickness, and a graph of $\ln I$ vs thickness is plotted to determine $\mu$ and HVT.
- **Uncertainties:** When measuring intensity, students must consider counting statistics (Poisson distribution) — the uncertainty in count rate is $\sqrt{N}$ where $N$ is the number of counts. This affects the accuracy of $\mu$ determination.
- **Graph plotting:** The semi-log plot ($\ln I$ vs thickness) should yield a straight line. Students must be able to draw a line of best fit, calculate the gradient, and determine $\mu$ from the gradient.
- **Experimental design:** Students should consider: narrow beam geometry (to minimize scattered radiation reaching the detector), use of collimators, background radiation subtraction, and choice of absorber thicknesses.

**Edexcel Unit 3 (AS) / Unit 6 (A2):**
- Similar practical skills are assessed, with emphasis on experimental design, data analysis, and evaluation of methods.
- Students may be asked to compare the attenuation of different materials (e.g., lead, aluminum, Perspex) and explain the results in terms of atomic number and density.
- The inverse square law for radiation may be combined with attenuation experiments.

**Common practical considerations:**
- **Safety:** X-ray sources are hazardous. In school labs, gamma sources (e.g., Cs-137) are often used as substitutes for X-rays. Students must follow safety protocols: minimize exposure time, maximize distance, use shielding.
- **Background radiation:** Always measure and subtract background count rate.
- **Beam geometry:** Narrow beam (good geometry) is essential for accurate measurement of $\mu$. Broad beam geometry includes scattered radiation, giving an apparent lower $\mu$.

**中文：**
本主题以多种方式与实验技能相关联：

**CAIE Paper 3 (AS) / Paper 5 (A2)：**
- **HVT的测量：** 学生可能被要求设计实验来测量材料的半值厚度。这涉及设置X射线源（或伽马源作为替代）、探测器（盖革-米勒管）和不同厚度的吸收体。测量每个厚度的强度，绘制 $\ln I$ 与厚度的关系图以确定 $\mu$ 和 HVT。
- **不确定度：** 测量强度时，学生必须考虑计数统计（泊松分布）——计数率的不确定度为 $\sqrt{N}$，其中 $N$ 是计数数。这影响 $\mu$ 确定的准确性。
- **图表绘制：** 半对数图（$\ln I$ 与厚度）应产生直线。学生必须能够绘制最佳拟合线，计算斜率，并从斜率确定 $\mu$。
- **实验设计：** 学生应考虑：窄束几何（以最小化到达探测器的散射辐射）、准直器的使用、背景辐射扣除以及吸收体厚度的选择。

**Edexcel Unit 3 (AS) / Unit 6 (A2)：**
- 评估类似的实验技能，重点在实验设计、数据分析和方法评估。
- 学生可能被要求比较不同材料（如铅、铝、有机玻璃）的衰减，并从原子序数和密度角度解释结果。
- 辐射的平方反比定律可能与衰减实验结合。

**常见实验考虑：**
- **安全：** X射线源有危险。在学校实验室中，通常使用伽马源（如Cs-137）作为X射线的替代品。学生必须遵守安全协议：最小化暴露时间，最大化距离，使用屏蔽。
- **背景辐射：** 始终测量并扣除背景计数率。
- **束几何：** 窄束（良好几何）对于准确测量 $\mu$ 至关重要。宽束几何包括散射辐射，给出表观较低的 $\mu$。

> 📋 **CIE Only:** CIE Paper 5 often includes questions on experimental design for measuring HVT. Students should be familiar with the setup, procedure, and analysis.

> 📋 **Edexcel Only:** Edexcel Unit 6 may include questions on the practical determination of attenuation coefficients, including the use of semi-log graphs and error analysis.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    XR[X-rays and Medical Imaging]
    
    %% Prerequisites
    PE[The Photoelectric Effect] -->|Explains absorption| XR
    ABG[Alpha, Beta and Gamma Radiation] -->|Radiation safety context| XR
    
    %% Sub-topics (Leaf Nodes)
    XR --> PROD[Production of X-rays<br>X-ray Tube]
    XR --> SPEC[X-ray Spectrum<br>Bremsstrahlung and Characteristic]
    XR --> ATT[Attenuation of X-rays]
    XR --> IMG[X-ray Imaging and Contrast]
    XR --> CT[CT Scans and Their Principles]
    XR --> DOS[Radiation Dose and Safety]
    
    %% Connections between sub-topics
    PROD -->|Produces| SPEC
    SPEC -->|Determines| ATT
    ATT -->|Enables| IMG
    IMG -->|Extended by| CT
    ATT -->|Quantified by| DOS
    CT -->|Higher dose than| DOS
    
    %% Related Topics
    XR --> US[Ultrasound Imaging]
    XR --> PET[PET Scans and Nuclear Medicine]
    
    %% Key equations
    ATT -->|Uses| EQ1[I = I₀e^(-μx)]
    ATT -->|Uses| EQ2[HVT = ln2/μ]
    PROD -->|Uses| EQ3[λ_min = hc/eV]
    DOS -->|Uses| EQ4[D = E/m]
    DOS -->|Uses| EQ5[H = D × w_R]
    DOS -->|Uses| EQ6[E = Σ H_T × w_T]
    
    %% Practical skills
    ATT -->|Measured by| PRAC[Practical: HVT measurement]
    DOS -->|Requires| SAFE[Safety: ALARA principles]
    
    %% Styling
    classDef main fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef sub fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef eq fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    classDef related fill:#e8f5e9,stroke:#1b5e20,stroke-width:1px
    classDef practical fill:#fce4ec,stroke:#b71c1c,stroke-width:1px
    
    class XR main
    class PROD,SPEC,ATT,IMG,CT,DOS sub
    class EQ1,EQ2,EQ3,EQ4,EQ5,EQ6 eq
    class PE,ABG,US,PET related
    class PRAC,SAFE practical
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | **X-rays:** EM radiation, $\lambda \approx 10^{-11}$ to $10^{-8}$ m, produced by electron deceleration. **Bremsstrahlung:** Continuous spectrum from electron braking. **Characteristic X-rays:** Discrete wavelengths from electron transitions in target atoms. **HVT:** Thickness to reduce intensity by half. **Attenuation coefficient ($\mu$):** Probability per unit length of absorption/scattering. **Absorbed dose:** Energy per unit mass (Gy). **Equivalent dose:** Absorbed dose × $w_R$ (Sv). **Effective dose:** Sum of equivalent doses × $w_T$ (Sv). |
| **Equations / 公式** | $\lambda_{min} = \frac{hc}{eV}$ (Duane-Hunt law) <br> $I = I_0 e^{-\mu x}$ (Exponential attenuation) <br> $HVT = \frac{\ln 2}{\mu} = \frac{0.693}{\mu}$ <br> $D = \frac{E}{m}$ (Absorbed dose) <br> $H_T = D \times w_R$ (Equivalent dose) <br> $E = \sum H_T \times w_T$ (Effective dose) |
| **Graphs / 图表** | **X-ray spectrum:** Intensity vs wavelength. Continuous bremsstrahlung with sharp cutoff at $\lambda_{min}$, peak at $1.5\lambda_{min}$, characteristic peaks superimposed. Higher voltage → shorter $\lambda_{min}$, higher intensity. **Attenuation curve:** $I$ vs $x$ — exponential decay. Semi-log plot ($\ln I$ vs $x$) → straight line, gradient $= -\mu$. |
| **Key Facts / 关键事实** | 1. Only ~1% of electron KE converts to X-rays; 99% becomes heat. <br> 2. Anode must be rotated to dissipate heat. <br> 3. Beryllium window used because it has low attenuation. <br> 4. Bone appears white (high $\mu$), air appears black (low $\mu$). <br> 5. Contrast media (barium, iodine) have high $Z$ → high $\mu$. <br> 6. CT uses multiple projections from different angles + computer reconstruction. <br> 7. CT gives higher dose than conventional X-rays. <br> 8. For X-rays: $w_R = 1$, so $H_T$ (Sv) = $D$ (Gy). <br> 9. ALARA: Time, Distance, Shielding. <br> 10. Deterministic effects have threshold; stochastic effects have no threshold. |
| **Exam Reminders / 考试提醒** | **Calculations:** Always convert units (kV → V, mm → m). Use $\ln$ (not $\log_{10}$) for exponential decay. Check that $\lambda_{min}$ is in the range $10^{-11}$ to $10^{-10}$ m. <br> **Explanations:** Use correct terminology (attenuation, not absorption alone). Distinguish between continuous and characteristic X-rays. Explain why CT has better contrast resolution. <br> **Diagrams:** Practice drawing and labeling the X-ray tube and X-ray spectrum. <br> **Safety:** Know the three dose quantities and their units. Understand ALARA. <br> **Common pitfalls:** Confusing Gy and Sv. Forgetting $w_T$ for effective dose. Thinking HVT is constant for polyenergetic beams. |

---

> 📝 **Document Version:** v1.0 | **Last Updated:** 2025 | **Next Review:** 2026
>
> This knowledge graph node is part of the **Medical Physics** chapter. For related topics, see [[Ultrasound Imaging]] and [[PET Scans and Nuclear Medicine]]. For prerequisites, see [[The Photoelectric Effect]] and [[Alpha, Beta and Gamma Radiation]].