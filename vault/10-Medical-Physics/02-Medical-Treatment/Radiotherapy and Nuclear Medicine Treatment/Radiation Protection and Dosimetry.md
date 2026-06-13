# 1. Overview / 概述

**English:**
Radiation Protection and Dosimetry is a critical sub-topic within [[Radiotherapy and Nuclear Medicine Treatment]] that focuses on the principles and practices of measuring radiation dose and protecting patients, staff, and the public from harmful effects of ionizing radiation. This sub-topic covers the fundamental concepts of absorbed dose, equivalent dose, and effective dose, as well as the practical measures used to minimize radiation exposure in medical settings. Understanding these principles is essential for ensuring the safe and effective use of radiation in [[External Beam Radiotherapy]], [[Brachytherapy (Internal Radiotherapy)]], and [[Targeted Alpha Therapy and Nuclear Medicine]].

The importance of this sub-topic extends beyond clinical practice to regulatory compliance and ethical considerations. Students must grasp how dosimetry quantifies radiation exposure and how protection measures—such as time, distance, and shielding—are applied to maintain exposure levels As Low As Reasonably Achievable (ALARA). This knowledge directly informs the [[Benefits vs Risks of Medical Radiation]] debate and connects to prerequisite concepts from [[Alpha, Beta and Gamma Radiation]] and [[PET Scans and Nuclear Medicine]].

**中文:**
辐射防护与剂量学是[[Radiotherapy and Nuclear Medicine Treatment]]中的一个关键子知识点，专注于测量辐射剂量以及保护患者、工作人员和公众免受电离辐射有害影响的原则与实践。本子知识点涵盖吸收剂量、当量剂量和有效剂量的基本概念，以及在医疗环境中最小化辐射暴露的实用措施。理解这些原则对于确保[[External Beam Radiotherapy]]、[[Brachytherapy (Internal Radiotherapy)]]和[[Targeted Alpha Therapy and Nuclear Medicine]]中辐射的安全有效使用至关重要。

本子知识点的重要性不仅限于临床实践，还涉及法规遵从和伦理考量。学生必须掌握剂量学如何量化辐射暴露，以及如何应用时间、距离和屏蔽等防护措施，将暴露水平保持在"合理可行尽量低"（ALARA）原则范围内。这些知识直接为[[Benefits vs Risks of Medical Radiation]]的讨论提供依据，并与[[Alpha, Beta and Gamma Radiation]]和[[PET Scans and Nuclear Medicine]]的先决概念相联系。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 26.4(a): Define absorbed dose, equivalent dose, and effective dose | 11.19: Understand the concept of absorbed dose and its measurement in grays (Gy) |
| 26.4(b): Understand the concept of dose equivalent and the sievert (Sv) | 11.20: Understand the concept of equivalent dose and the sievert (Sv) |
| 26.4(c): Understand the concept of effective dose and its use in risk assessment | 11.21: Understand the concept of effective dose and its application |
| 26.4(d): Describe methods of radiation protection including time, distance, and shielding | 11.22: Describe methods of radiation protection (time, distance, shielding) |
| 26.4(e): Understand the ALARA principle | 11.23: Understand the ALARA principle |
| — | 11.24: Understand the concept of half-value thickness (HVT) |

**Examiner Expectations / 考官期望:**
- **CAIE:** Students must be able to calculate absorbed dose, equivalent dose, and effective dose using given data. They should understand the weighting factors for different radiation types and tissues. Questions often involve interpreting dose limits and justifying protection measures.
- **Edexcel:** Students must be able to calculate half-value thickness from experimental data and apply the exponential attenuation equation. They should understand the practical application of protection methods in medical settings.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Absorbed Dose** / 吸收剂量 | The energy absorbed per unit mass of tissue from ionizing radiation. Unit: gray (Gy) = J kg⁻¹ | 电离辐射在单位质量组织中吸收的能量。单位：戈瑞 (Gy) = J kg⁻¹ | Confusing with equivalent dose; forgetting it's energy per unit mass |
| **Equivalent Dose** / 当量剂量 | The absorbed dose multiplied by a radiation weighting factor (w_R) to account for biological effectiveness of different radiation types. Unit: sievert (Sv) | 吸收剂量乘以辐射权重因子 (w_R)，以考虑不同辐射类型的生物效应。单位：希沃特 (Sv) | Using Sv for absorbed dose; forgetting the weighting factor |
| **Effective Dose** / 有效剂量 | The sum of equivalent doses to each tissue multiplied by tissue weighting factors (w_T), giving a whole-body risk measure. Unit: sievert (Sv) | 各组织当量剂量乘以组织权重因子 (w_T) 的总和，提供全身风险度量。单位：希沃特 (Sv) | Confusing with equivalent dose; forgetting tissue weighting |
| **ALARA Principle** / ALARA原则 | As Low As Reasonably Achievable — the principle of minimizing radiation exposure considering economic and social factors | 合理可行尽量低——在考虑经济和社会因素的情况下，最小化辐射暴露的原则 | Thinking it means zero exposure; ignoring the "reasonably achievable" part |
| **Half-Value Thickness (HVT)** / 半值厚度 | The thickness of a shielding material required to reduce the intensity of a radiation beam by half | 将辐射束强度降低一半所需的屏蔽材料厚度 | Confusing with half-life; forgetting it depends on material and radiation type |
| **Radiation Weighting Factor (w_R)** / 辐射权重因子 | A dimensionless factor that accounts for the relative biological effectiveness of different types of radiation (e.g., α = 20, β = 1, γ = 1) | 无量纲因子，用于说明不同类型辐射的相对生物效应（例如，α = 20, β = 1, γ = 1） | Forgetting α has much higher factor; using wrong values |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Absorbed Dose vs Equivalent Dose vs Effective Dose / 吸收剂量 vs 当量剂量 vs 有效剂量

### Explanation / 解释
**English:**
These three quantities form a hierarchy of radiation measurement. **Absorbed dose** ($D$) is the fundamental physical quantity—the energy deposited per unit mass. However, different types of radiation cause different amounts of biological damage for the same absorbed dose. Therefore, **equivalent dose** ($H_T$) multiplies absorbed dose by a radiation weighting factor ($w_R$): $H_T = D \times w_R$. For example, alpha particles ($w_R = 20$) cause 20 times more biological damage than gamma rays ($w_R = 1$) for the same absorbed dose.

**Effective dose** ($E$) goes further by considering that different tissues have different sensitivities to radiation. It sums the equivalent doses to each tissue multiplied by tissue weighting factors ($w_T$): $E = \sum (H_T \times w_T)$. This gives a whole-body risk measure that allows comparison of different exposure scenarios. For example, a chest X-ray gives an effective dose of about 0.1 mSv, while a CT scan might give 10 mSv.

**中文:**
这三个量构成了辐射测量的层级结构。**吸收剂量** ($D$) 是基本的物理量——单位质量沉积的能量。然而，对于相同的吸收剂量，不同类型的辐射会造成不同程度的生物损伤。因此，**当量剂量** ($H_T$) 将吸收剂量乘以辐射权重因子 ($w_R$)：$H_T = D \times w_R$。例如，对于相同的吸收剂量，α粒子 ($w_R = 20$) 造成的生物损伤是γ射线 ($w_R = 1$) 的20倍。

**有效剂量** ($E$) 更进一步，考虑了不同组织对辐射的敏感性不同。它将各组织的当量剂量乘以组织权重因子 ($w_T$) 后求和：$E = \sum (H_T \times w_T)$。这提供了一个全身风险度量，允许比较不同的暴露情景。例如，胸部X光检查的有效剂量约为0.1 mSv，而CT扫描可能为10 mSv。

### Physical Meaning / 物理意义
**English:**
- **Absorbed dose** tells us how much energy is deposited in tissue (physical effect)
- **Equivalent dose** tells us how much biological damage is expected (biological effect)
- **Effective dose** tells us the overall health risk to the whole body (risk assessment)

**中文:**
- **吸收剂量**告诉我们组织中有多少能量沉积（物理效应）
- **当量剂量**告诉我们预期有多少生物损伤（生物效应）
- **有效剂量**告诉我们全身的整体健康风险（风险评估）

### Common Misconceptions / 常见误区
- **EN:** Thinking absorbed dose and equivalent dose are the same thing. They are only equal when $w_R = 1$ (for β, γ, X-rays).
- **CN:** 认为吸收剂量和当量剂量是同一回事。它们仅在 $w_R = 1$ 时相等（对于β、γ、X射线）。
- **EN:** Forgetting that effective dose requires summing over all exposed tissues.
- **CN:** 忘记有效剂量需要对所有暴露组织求和。
- **EN:** Using sieverts (Sv) for absorbed dose instead of grays (Gy).
- **CN:** 对吸收剂量使用希沃特 (Sv) 而不是戈瑞 (Gy)。

### Exam Tips / 考试提示
- **EN:** Always check the units: Gy for absorbed dose, Sv for equivalent and effective dose. Remember the weighting factors: $w_R$ for radiation type, $w_T$ for tissue type.
- **CN:** 始终检查单位：吸收剂量用Gy，当量剂量和有效剂量用Sv。记住权重因子：$w_R$ 用于辐射类型，$w_T$ 用于组织类型。

> 📷 **IMAGE PROMPT — DOSE_HIERARCHY: Hierarchy of Radiation Dose Quantities**
> A clear diagram showing three levels: bottom level "Absorbed Dose (Gy)" with arrow labeled "× w_R" pointing up to middle level "Equivalent Dose (Sv)", then arrow labeled "× w_T" pointing up to top level "Effective Dose (Sv)". Include example values: 1 Gy of α → 20 Sv equivalent → multiply by tissue factor for effective dose. Use color coding: blue for physical, green for biological, red for risk.

---

## 4.2 ALARA Principle and Protection Methods / ALARA原则与防护方法

### Explanation / 解释
**English:**
The **ALARA principle** (As Low As Reasonably Achievable) is the cornerstone of radiation protection. It requires that all radiation exposures be kept as low as possible, considering economic and social factors. This is achieved through three fundamental protection methods:

1. **Time:** Minimizing the time spent near radiation sources reduces total exposure. Dose ∝ time.
2. **Distance:** Increasing distance from the source reduces exposure. For point sources, dose rate ∝ 1/r² (inverse square law).
3. **Shielding:** Using absorbing materials between the source and personnel reduces exposure. The required thickness depends on the radiation type and energy.

**中文:**
**ALARA原则**（合理可行尽量低）是辐射防护的基石。它要求在考虑经济和社会因素的情况下，将所有辐射暴露保持在尽可能低的水平。这通过三种基本防护方法实现：

1. **时间：** 最小化在辐射源附近的时间可减少总暴露量。剂量 ∝ 时间。
2. **距离：** 增加与辐射源的距离可减少暴露量。对于点源，剂量率 ∝ 1/r²（平方反比定律）。
3. **屏蔽：** 在源和人员之间使用吸收材料可减少暴露量。所需厚度取决于辐射类型和能量。

### Physical Meaning / 物理意义
**English:**
- **Time:** Direct proportionality—double the time, double the dose
- **Distance:** Inverse square law—doubling distance reduces dose rate to 1/4
- **Shielding:** Exponential attenuation—each HVT reduces intensity by half

**中文:**
- **时间：** 直接正比——时间加倍，剂量加倍
- **距离：** 平方反比定律——距离加倍，剂量率降至1/4
- **屏蔽：** 指数衰减——每个HVT使强度减半

### Common Misconceptions / 常见误区
- **EN:** Thinking ALARA means zero exposure. It means "reasonably achievable" considering practical constraints.
- **CN:** 认为ALARA意味着零暴露。它意味着考虑实际限制后的"合理可行"。
- **EN:** Forgetting that distance protection follows inverse square law only for point sources.
- **CN:** 忘记距离防护仅对点源遵循平方反比定律。
- **EN:** Confusing HVT with half-life. HVT is for shielding thickness, half-life is for radioactive decay.
- **CN:** 混淆HVT与半衰期。HVT用于屏蔽厚度，半衰期用于放射性衰变。

### Exam Tips / 考试提示
- **EN:** Be prepared to calculate dose reduction using inverse square law or HVT. For HVT problems, use $I = I_0 (1/2)^{n}$ where $n = \text{thickness} / \text{HVT}$.
- **CN:** 准备好使用平方反比定律或HVT计算剂量减少。对于HVT问题，使用 $I = I_0 (1/2)^{n}$，其中 $n = \text{厚度} / \text{HVT}$。

> 📷 **IMAGE PROMPT — ALARA_PRINCIPLE: Three Methods of Radiation Protection**
> A split diagram showing three panels: (1) "Time" with a stopwatch and person near source, (2) "Distance" with inverse square law graph showing dose rate vs distance, (3) "Shielding" with radiation beam passing through lead blocks showing exponential attenuation. Include ALARA acronym prominently.

---

## 4.3 Half-Value Thickness (HVT) / 半值厚度

### Explanation / 解释
**English:**
**Half-Value Thickness (HVT)** is the thickness of a shielding material required to reduce the intensity of a radiation beam to half its original value. It depends on:
- The type of radiation (α, β, γ, X-rays)
- The energy of the radiation
- The material used for shielding

The intensity after passing through a thickness $x$ of shielding is given by:
$$ I = I_0 \left(\frac{1}{2}\right)^{x / \text{HVT}} $$

Alternatively, using the linear attenuation coefficient $\mu$:
$$ I = I_0 e^{-\mu x} $$
where $\text{HVT} = \frac{\ln 2}{\mu} = \frac{0.693}{\mu}$

**中文:**
**半值厚度 (HVT)** 是将辐射束强度降低到原始值一半所需的屏蔽材料厚度。它取决于：
- 辐射类型（α、β、γ、X射线）
- 辐射的能量
- 用于屏蔽的材料

通过厚度 $x$ 的屏蔽后的强度由下式给出：
$$ I = I_0 \left(\frac{1}{2}\right)^{x / \text{HVT}} $$

或者使用线性衰减系数 $\mu$：
$$ I = I_0 e^{-\mu x} $$
其中 $\text{HVT} = \frac{\ln 2}{\mu} = \frac{0.693}{\mu}$

### Physical Meaning / 物理意义
**English:**
- HVT is a measure of how effective a material is at attenuating radiation
- Smaller HVT = more effective shielding (e.g., lead has small HVT for γ-rays)
- HVT is analogous to half-life in radioactive decay, but for spatial attenuation

**中文:**
- HVT是衡量材料衰减辐射有效性的指标
- HVT越小 = 屏蔽越有效（例如，铅对γ射线的HVT很小）
- HVT类似于放射性衰变中的半衰期，但用于空间衰减

### Common Misconceptions / 常见误区
- **EN:** Confusing HVT with half-life. HVT is about distance through material, half-life is about time.
- **CN:** 混淆HVT与半衰期。HVT是关于材料中的距离，半衰期是关于时间。
- **EN:** Thinking HVT is the same for all materials and radiation types.
- **CN:** 认为HVT对所有材料和辐射类型都相同。
- **EN:** Forgetting that HVT applies to narrow beam geometry (good geometry).
- **CN:** 忘记HVT适用于窄束几何（良好几何）。

### Exam Tips / 考试提示
- **EN:** For Edexcel, be prepared to calculate HVT from experimental data using the exponential equation. For CAIE, understand the concept but focus more on dose calculations.
- **CN:** 对于Edexcel，准备好使用指数方程从实验数据计算HVT。对于CAIE，理解概念但更关注剂量计算。

> 📋 **Edexcel Only:** HVT calculations are specifically required in Edexcel IAL syllabus (11.24). Practice using both forms of the attenuation equation.

---

# 5. Essential Equations / 核心公式

## 5.1 Absorbed Dose / 吸收剂量

$$ D = \frac{E}{m} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $D$ | Absorbed dose | 吸收剂量 | Gy (J kg⁻¹) |
| $E$ | Energy absorbed | 吸收的能量 | J |
| $m$ | Mass of tissue | 组织质量 | kg |

**Derivation / 推导:** Definitional equation.
**Conditions / 适用条件:** Any type of ionizing radiation.
**Limitations / 局限性:** Does not account for biological effectiveness of different radiation types.

## 5.2 Equivalent Dose / 当量剂量

$$ H_T = D \times w_R $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $H_T$ | Equivalent dose to tissue T | 组织T的当量剂量 | Sv |
| $D$ | Absorbed dose | 吸收剂量 | Gy |
| $w_R$ | Radiation weighting factor | 辐射权重因子 | dimensionless |

**Derivation / 推导:** Definitional equation.
**Conditions / 适用条件:** All types of ionizing radiation.
**Limitations / 局限性:** Does not account for tissue sensitivity differences.

## 5.3 Effective Dose / 有效剂量

$$ E = \sum (H_T \times w_T) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Effective dose | 有效剂量 | Sv |
| $H_T$ | Equivalent dose to tissue T | 组织T的当量剂量 | Sv |
| $w_T$ | Tissue weighting factor | 组织权重因子 | dimensionless |

**Derivation / 推导:** Definitional equation.
**Conditions / 适用条件:** Whole-body or partial-body exposure.
**Limitations / 局限性:** Tissue weighting factors are population averages, not individual-specific.

## 5.4 Half-Value Thickness Attenuation / 半值厚度衰减

$$ I = I_0 \left(\frac{1}{2}\right)^{x / \text{HVT}} $$

$$ I = I_0 e^{-\mu x} $$

$$ \text{HVT} = \frac{\ln 2}{\mu} = \frac{0.693}{\mu} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $I$ | Transmitted intensity | 透射强度 | W m⁻² or count rate |
| $I_0$ | Initial intensity | 初始强度 | W m⁻² or count rate |
| $x$ | Thickness of shielding | 屏蔽厚度 | m or cm |
| HVT | Half-value thickness | 半值厚度 | m or cm |
| $\mu$ | Linear attenuation coefficient | 线性衰减系数 | m⁻¹ or cm⁻¹ |

**Derivation / 推导:** From exponential decay law.
**Conditions / 适用条件:** Narrow beam geometry (good geometry), monoenergetic radiation.
**Limitations / 局限性:** Does not apply to broad beam geometry without correction for scatter.

## 5.5 Inverse Square Law for Distance / 距离的平方反比定律

$$ \frac{I_1}{I_2} = \frac{r_2^2}{r_1^2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $I_1, I_2$ | Dose rates at distances $r_1, r_2$ | 距离 $r_1, r_2$ 处的剂量率 | Sv s⁻¹ or Gy s⁻¹ |
| $r_1, r_2$ | Distances from source | 距源的距离 | m |

**Derivation / 推导:** From conservation of energy over spherical surface area ($4\pi r^2$).
**Conditions / 适用条件:** Point source, no absorption or scattering in medium.
**Limitations / 局限性:** Only approximate for extended sources; ignores air attenuation.

> 📷 **IMAGE PROMPT — HVT_GRAPH: Exponential Attenuation and Half-Value Thickness**
> A graph showing intensity I on y-axis vs thickness x on x-axis. The curve starts at I₀ and decays exponentially. Mark the points where I = I₀/2, I₀/4, I₀/8, showing HVT, 2×HVT, 3×HVT. Include the equation I = I₀(1/2)^(x/HVT). Use clear labels and a grid.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Exponential Attenuation Graph / 指数衰减图

### Axes / 坐标轴
- **X-axis:** Thickness of shielding material (x) / 屏蔽材料厚度 (x)
- **Y-axis:** Transmitted intensity (I) or dose rate / 透射强度 (I) 或剂量率

### Shape / 形状
**English:** Exponential decay curve starting at $I_0$ and asymptotically approaching zero. The curve decreases by half for each HVT of thickness.

**中文:** 从 $I_0$ 开始并渐近趋近于零的指数衰减曲线。每增加一个HVT的厚度，曲线减半。

### Gradient Meaning / 斜率含义
**English:** The gradient (slope) at any point is proportional to the negative of the intensity at that point: $\frac{dI}{dx} = -\mu I$. The gradient becomes less steep as thickness increases.

**中文:** 任意点的梯度（斜率）与该点的强度成正比：$\frac{dI}{dx} = -\mu I$。随着厚度增加，梯度变缓。

### Area Meaning / 面积含义
**English:** The area under the curve has no direct physical meaning in this context.

**中文:** 曲线下的面积在此上下文中没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** 
- Use the graph to find HVT: find thickness where $I = I_0/2$
- Use semi-log graph (log I vs x) to get a straight line with gradient $-\mu$
- Compare shielding effectiveness: steeper decay = smaller HVT = better shielding

**中文:**
- 使用图表找到HVT：找到 $I = I_0/2$ 时的厚度
- 使用半对数图（log I vs x）得到斜率为 $-\mu$ 的直线
- 比较屏蔽效果：衰减越陡 = HVT越小 = 屏蔽效果越好

> 📷 **IMAGE PROMPT — ATTENUATION_GRAPH: Exponential Attenuation with HVT Marked**
> A clear graph with labeled axes. Show exponential decay curve with three HVT points marked. Include a second panel showing the same data on a semi-log plot (log I vs x) showing a straight line. Label gradient as -μ.

---

## 6.2 Inverse Square Law Graph / 平方反比定律图

### Axes / 坐标轴
- **X-axis:** Distance from source (r) / 距源距离 (r)
- **Y-axis:** Dose rate (I) / 剂量率 (I)

### Shape / 形状
**English:** Hyperbolic decay: $I \propto 1/r^2$. The curve decreases rapidly near the source and more slowly at larger distances.

**中文:** 双曲线衰减：$I \propto 1/r^2$。曲线在靠近源处迅速下降，在较远距离处下降较慢。

### Gradient Meaning / 斜率含义
**English:** The gradient is negative and proportional to $-2/r^3$. The gradient is steepest near the source.

**中文:** 梯度为负，与 $-2/r^3$ 成正比。梯度在靠近源处最陡。

### Area Meaning / 面积含义
**English:** No direct physical meaning.

**中文:** 没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:**
- Plot $I$ vs $1/r^2$ to get a straight line through origin
- Use to calculate dose rate at different distances
- Important for planning safe working distances in radiotherapy

**中文:**
- 绘制 $I$ vs $1/r^2$ 得到通过原点的直线
- 用于计算不同距离处的剂量率
- 对规划放疗中的安全工作距离很重要

> 📷 **IMAGE PROMPT — INVERSE_SQUARE_GRAPH: Inverse Square Law for Radiation**
> Two-panel graph: Left panel shows I vs r with hyperbolic decay curve. Right panel shows I vs 1/r² with straight line through origin. Label both axes clearly. Include example: at 1m dose rate = 100 μSv/h, at 2m = 25 μSv/h.

---

# 7. Required Diagrams / 必备图表

## 7.1 Radiation Protection Methods Diagram / 辐射防护方法图

### Description / 描述
**English:** A diagram showing the three fundamental methods of radiation protection: time, distance, and shielding. Include a radiation source, a person, and illustrate how each method reduces exposure.

**中文:** 显示三种基本辐射防护方法的图表：时间、距离和屏蔽。包括辐射源、人员，并说明每种方法如何减少暴露。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — PROTECTION_METHODS: Three Methods of Radiation Protection**
> A professional medical physics diagram with three panels. Panel 1 "Time": Show a person near a radiation source with a stopwatch, arrow indicating "Reduce time → Reduce dose". Panel 2 "Distance": Show inverse square law illustration with distances 1m, 2m, 4m and corresponding dose rates 100%, 25%, 6.25%. Panel 3 "Shielding": Show radiation source emitting rays through different thicknesses of lead (1 HVT, 2 HVT, 3 HVT) with intensity halving each time. Use clear labels, color coding (red for high dose, green for low dose), and include the ALARA acronym at the top.

### Labels Required / 需要标注
- **EN:** Radiation source, Person, Time (t), Distance (r), Shielding material (lead), HVT, ALARA
- **CN:** 辐射源、人员、时间 (t)、距离 (r)、屏蔽材料（铅）、HVT、ALARA

### Exam Importance / 考试重要性
**English:** High. This diagram is frequently used in exam questions asking students to explain how protection methods work. Students may be asked to draw or label such a diagram.

**中文:** 高。此图常用于考试题中，要求学生解释防护方法的工作原理。学生可能被要求绘制或标注此类图表。

---

## 7.2 Absorbed vs Equivalent vs Effective Dose Diagram / 吸收剂量 vs 当量剂量 vs 有效剂量图

### Description / 描述
**English:** A hierarchical diagram showing the relationship between absorbed dose, equivalent dose, and effective dose, including the weighting factors applied at each step.

**中文:** 显示吸收剂量、当量剂量和有效剂量之间关系的层级图，包括每一步应用的权重因子。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DOSE_HIERARCHY_DIAGRAM: Hierarchy of Radiation Dose Quantities**
> A three-level pyramid diagram. Bottom level: "Absorbed Dose (D)" with unit Gy, formula D = E/m. Arrow pointing up labeled "× w_R (radiation weighting factor)" leading to middle level: "Equivalent Dose (H_T)" with unit Sv, formula H_T = D × w_R. Arrow pointing up labeled "× w_T (tissue weighting factor)" leading to top level: "Effective Dose (E)" with unit Sv, formula E = Σ(H_T × w_T). Include example values: 1 Gy of alpha radiation → 20 Sv equivalent → multiply by lung tissue factor 0.12 → 2.4 Sv effective. Use color coding: blue (physical), green (biological), red (risk).

### Labels Required / 需要标注
- **EN:** Absorbed dose (Gy), Equivalent dose (Sv), Effective dose (Sv), w_R, w_T, Tissue types
- **CN:** 吸收剂量 (Gy)、当量剂量 (Sv)、有效剂量 (Sv)、w_R、w_T、组织类型

### Exam Importance / 考试重要性
**English:** Very high. Understanding the distinction between these three quantities is essential for all exam boards. Students must be able to explain the purpose of each and perform calculations.

**中文:** 非常高。理解这三个量之间的区别对所有考试委员会都至关重要。学生必须能够解释每个量的目的并进行计算。

---

# 8. Worked Examples / 典型例题

## Example 1: Dose Calculation / 例题1：剂量计算

### Question / 题目
**English:**
A patient receives an absorbed dose of 0.5 Gy from alpha radiation ($w_R = 20$) to their lungs ($w_T = 0.12$) and 0.3 Gy from gamma radiation ($w_R = 1$) to their thyroid ($w_T = 0.05$). Calculate:
(a) The equivalent dose to the lungs
(b) The equivalent dose to the thyroid
(c) The total effective dose to the patient

**中文:**
一名患者肺部接受0.5 Gy的α辐射吸收剂量（$w_R = 20$），甲状腺接受0.3 Gy的γ辐射吸收剂量（$w_R = 1$）。已知肺组织权重因子 $w_T = 0.12$，甲状腺组织权重因子 $w_T = 0.05$。计算：
(a) 肺部的当量剂量
(b) 甲状腺的当量剂量
(c) 患者的总有效剂量

### Solution / 解答

**Step 1: Calculate equivalent dose to lungs / 计算肺部当量剂量**
$$ H_{\text{lungs}} = D \times w_R = 0.5 \times 20 = 10 \text{ Sv} $$

**Step 2: Calculate equivalent dose to thyroid / 计算甲状腺当量剂量**
$$ H_{\text{thyroid}} = D \times w_R = 0.3 \times 1 = 0.3 \text{ Sv} $$

**Step 3: Calculate effective dose / 计算有效剂量**
$$ E = (H_{\text{lungs}} \times w_{T,\text{lungs}}) + (H_{\text{thyroid}} \times w_{T,\text{thyroid}}) $$
$$ E = (10 \times 0.12) + (0.3 \times 0.05) $$
$$ E = 1.2 + 0.015 = 1.215 \text{ Sv} $$

### Final Answer / 最终答案
**Answer:** (a) 10 Sv, (b) 0.3 Sv, (c) 1.215 Sv | **答案：** (a) 10 Sv, (b) 0.3 Sv, (c) 1.215 Sv

### Quick Tip / 提示
**EN:** Always check which weighting factor to use: $w_R$ for radiation type, $w_T$ for tissue type. Remember that effective dose requires summing over ALL exposed tissues.

**CN:** 始终检查使用哪个权重因子：$w_R$ 用于辐射类型，$w_T$ 用于组织类型。记住有效剂量需要对所有暴露组织求和。

---

## Example 2: Half-Value Thickness / 例题2：半值厚度

### Question / 题目
**English:**
A beam of gamma radiation has an initial intensity of 800 counts per second. After passing through 4.0 cm of lead shielding, the intensity is reduced to 50 counts per second. Calculate:
(a) The half-value thickness (HVT) of lead for this radiation
(b) The linear attenuation coefficient ($\mu$)
(c) The thickness required to reduce the intensity to 12.5 counts per second

**中文:**
一束γ辐射的初始强度为每秒800计数。通过4.0 cm铅屏蔽后，强度降至每秒50计数。计算：
(a) 铅对此辐射的半值厚度 (HVT)
(b) 线性衰减系数 ($\mu$)
(c) 将强度降至每秒12.5计数所需的厚度

### Solution / 解答

**Step 1: Find number of HVTs / 求HVT的数量**
$$ I = I_0 \left(\frac{1}{2}\right)^n $$
$$ 50 = 800 \left(\frac{1}{2}\right)^n $$
$$ \frac{50}{800} = \frac{1}{16} = \left(\frac{1}{2}\right)^n $$
$$ n = 4 \text{ HVTs} $$

**Step 2: Calculate HVT / 计算HVT**
$$ \text{HVT} = \frac{x}{n} = \frac{4.0}{4} = 1.0 \text{ cm} $$

**Step 3: Calculate linear attenuation coefficient / 计算线性衰减系数**
$$ \mu = \frac{\ln 2}{\text{HVT}} = \frac{0.693}{1.0} = 0.693 \text{ cm}^{-1} $$

**Step 4: Calculate thickness for 12.5 counts/s / 计算12.5计数/s所需厚度**
$$ 12.5 = 800 \left(\frac{1}{2}\right)^n $$
$$ \frac{12.5}{800} = \frac{1}{64} = \left(\frac{1}{2}\right)^n $$
$$ n = 6 \text{ HVTs} $$
$$ x = n \times \text{HVT} = 6 \times 1.0 = 6.0 \text{ cm} $$

### Final Answer / 最终答案
**Answer:** (a) 1.0 cm, (b) 0.693 cm⁻¹, (c) 6.0 cm | **答案：** (a) 1.0 cm, (b) 0.693 cm⁻¹, (c) 6.0 cm

### Quick Tip / 提示
**EN:** For HVT problems, first find how many HVTs correspond to the given reduction, then divide total thickness by that number. Remember: each HVT halves the intensity.

**CN:** 对于HVT问题，首先找出给定衰减对应多少个HVT，然后将总厚度除以该数字。记住：每个HVT使强度减半。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate absorbed dose, equivalent dose, effective dose | High | Medium | 📝 *待填入* |
| Explain ALARA principle and protection methods | High | Low-Medium | 📝 *待填入* |
| Calculate HVT from experimental data (Edexcel) | Medium | Medium-High | 📝 *待填入* |
| Interpret dose limits and justify protection measures | Medium | Medium | 📝 *待填入* |
| Inverse square law calculations for distance protection | Medium | Medium | 📝 *待填入* |
| Compare shielding effectiveness of different materials | Low | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Define, Calculate, Explain, Describe, Determine, Justify, Compare
- **CN:** 定义、计算、解释、描述、确定、论证、比较

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical skills in several ways:

1. **Measurement of Radiation Intensity:** Using Geiger-Müller tubes or ionization chambers to measure count rates or dose rates at different distances and through different shielding thicknesses.

2. **Determination of Half-Value Thickness:** Experimental setup where students place increasing thicknesses of shielding material between a source and detector, recording intensity at each thickness. Plotting log(I) vs thickness gives a straight line from which HVT and μ can be determined.

3. **Inverse Square Law Verification:** Measuring dose rate at various distances from a point source and plotting I vs 1/r² to verify the inverse square relationship.

4. **Uncertainty Analysis:** Calculating uncertainties in dose measurements, considering counting statistics (Poisson distribution) and systematic errors from geometry.

5. **Risk Assessment:** Evaluating the ALARA principle in practical settings, justifying the use of lead aprons, distance, and time limits.

**中文:**
本子知识点通过以下几种方式与实验技能相联系：

1. **辐射强度测量：** 使用盖革-米勒管或电离室测量不同距离和不同屏蔽厚度下的计数率或剂量率。

2. **半值厚度的测定：** 实验设置中，学生在源和探测器之间放置递增厚度的屏蔽材料，记录每个厚度下的强度。绘制log(I) vs 厚度得到直线，从中可以确定HVT和μ。

3. **平方反比定律验证：** 测量距点源不同距离处的剂量率，绘制I vs 1/r²以验证平方反比关系。

4. **不确定度分析：** 计算剂量测量中的不确定度，考虑计数统计（泊松分布）和几何因素的系统误差。

5. **风险评估：** 在实际环境中评估ALARA原则，论证使用铅围裙、距离和时间限制的合理性。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main topic
    RP[Radiation Protection and Dosimetry] --> AD[Absorbed Dose D]
    RP --> EQ[Equivalent Dose H_T]
    RP --> EF[Effective Dose E]
    RP --> ALARA[ALARA Principle]
    RP --> HVT[Half-Value Thickness]
    
    %% Dose relationships
    AD -->|× w_R| EQ
    EQ -->|× w_T| EF
    
    %% Protection methods
    ALARA --> TIME[Time: D ∝ t]
    ALARA --> DIST[Distance: I ∝ 1/r²]
    ALARA --> SHIELD[Shielding: I = I₀(½)^(x/HVT)]
    
    %% HVT connections
    HVT --> MU[Linear Attenuation Coefficient μ]
    HVT --> EXP[Exponential Attenuation]
    
    %% External links
    AD -.->|Prerequisite| RAD[Alpha, Beta and Gamma Radiation]
    EF -.->|Risk assessment| BEN[Benefits vs Risks of Medical Radiation]
    ALARA -.->|Applied in| EBRT[External Beam Radiotherapy]
    ALARA -.->|Applied in| BRACHY[Brachytherapy]
    HVT -.->|Shielding design| XRAY[X-rays and Medical Imaging]
    
    %% Styling
    classDef main fill:#f9f,stroke:#333,stroke-width:2px
    classDef dose fill:#bbf,stroke:#333,stroke-width:1px
    classDef protect fill:#bfb,stroke:#333,stroke-width:1px
    classDef external fill:#ddd,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
    
    class RP main
    class AD,EQ,EF dose
    class ALARA,TIME,DIST,SHIELD,HVT,MU,EXP protect
    class RAD,BEN,EBRT,BRACHY,XRAY external
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Absorbed dose:** Energy absorbed per unit mass (Gy) / 吸收剂量：单位质量吸收的能量 (Gy) |
| | **Equivalent dose:** Absorbed dose × w_R (Sv) / 当量剂量：吸收剂量 × w_R (Sv) |
| | **Effective dose:** Sum of equivalent doses × w_T (Sv) / 有效剂量：当量剂量 × w_T 之和 (Sv) |
| **Key Formula / 核心公式** | $D = E/m$ (Gy) |
| | $H_T = D \times w_R$ (Sv) |
| | $E = \sum (H_T \times w_T)$ (Sv) |
| | $I = I_0 (1/2)^{x/\text{HVT}}$ |
| | $I = I_0 e^{-\mu x}$, $\text{HVT} = 0.693/\mu$ |
| | $I_1/I_2 = r_2^2/r_1^2$ (inverse square law) |
| **Key Graph / 核心图表** | Exponential attenuation: I vs x (decay curve) / 指数衰减：I vs x（衰减曲线） |
| | Semi-log: log I vs x (straight line, gradient = -μ) / 半对数：log I vs x（直线，斜率 = -μ） |
| | Inverse square: I vs 1/r² (straight line through origin) / 平方反比：I vs 1/r²（通过原点的直线） |
| **Exam Tip / 考试提示** | **CAIE:** Focus on dose calculations and ALARA principle. Know w_R values: α=20, β=1, γ=1, n≈5-20. |
| | **Edexcel:** Also practice HVT calculations using both forms of attenuation equation. |
| | **Both:** Always check units (Gy vs Sv) and which weighting factor to use. |
| | **Both:** For protection questions, always mention all three methods: time, distance, shielding. |