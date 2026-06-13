# 1. Overview / 概述

**English:**
External Beam Radiotherapy (EBRT) is the most common form of radiotherapy, where a beam of high-energy radiation is directed from outside the body onto a tumour. This sub-topic covers the principles, techniques, and physics behind EBRT, including how radiation is generated, collimated, and delivered to destroy cancerous cells while minimising damage to surrounding healthy tissue. It is a critical application of [[Alpha, Beta and Gamma Radiation]] and [[X-rays and Medical Imaging]] in modern medicine.

EBRT relies on the fact that rapidly dividing cancer cells are more sensitive to radiation damage than normal cells. The key challenge is to deliver a lethal dose to the tumour while keeping the dose to organs at risk (OARs) within safe limits. This requires precise targeting, dose calculation, and treatment planning. Understanding EBRT is essential for appreciating the broader topic of [[Radiotherapy and Nuclear Medicine Treatment]] and its role in cancer management.

**中文:**
外照射放疗（EBRT）是最常见的放疗形式，将高能辐射束从体外直接照射到肿瘤上。本子知识点涵盖EBRT的原理、技术和物理基础，包括如何产生、准直和传递辐射以摧毁癌细胞，同时最大限度地减少对周围健康组织的损伤。它是[[Alpha, Beta and Gamma Radiation]]和[[X-rays and Medical Imaging]]在现代医学中的关键应用。

EBRT依赖于快速分裂的癌细胞比正常细胞对辐射损伤更敏感这一事实。关键挑战在于向肿瘤传递致死剂量，同时将危及器官（OARs）的剂量控制在安全范围内。这需要精确的靶向、剂量计算和治疗计划。理解EBRT对于理解[[Radiotherapy and Nuclear Medicine Treatment]]及其在癌症管理中的作用至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 26.4(a) Describe the principles of external beam radiotherapy | 11.19 Understand the principles of external beam radiotherapy |
| 26.4(b) Explain the use of linear accelerators (linacs) in radiotherapy | 11.20 Understand the operation of a linear accelerator (linac) |
| 26.4(c) Describe the use of collimators and beam shaping | 11.21 Understand the use of collimators and multileaf collimators (MLCs) |
| 26.4(d) Explain the concept of dose fractionation | 11.22 Understand the concept of dose fractionation |
| 26.4(e) Describe the use of treatment planning and simulation | 11.23 Understand the use of CT simulation and treatment planning |
| - | 11.24 Understand the concept of dose-volume histograms (DVHs) |

**Examiner Expectations / 考官期望:**
- **CAIE:** Focus on principles, linac operation, collimation, fractionation, and planning. No detailed DVH analysis required.
- **Edexcel:** Includes DVHs and more detailed treatment planning concepts. Expect to interpret DVH curves.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **External Beam Radiotherapy (EBRT)** / 外照射放疗 | A radiotherapy technique where radiation is delivered from outside the body using a machine such as a linear accelerator. | 使用直线加速器等设备从体外传递辐射的放疗技术。 | Confusing with brachytherapy (internal source). |
| **Linear Accelerator (Linac)** / 直线加速器 | A device that accelerates electrons to high energies, which then strike a target to produce high-energy X-rays for radiotherapy. | 将电子加速到高能量，然后撞击靶材产生高能X射线用于放疗的设备。 | Thinking linacs produce radiation directly; they produce electrons that generate X-rays. |
| **Multileaf Collimator (MLC)** / 多叶准直器 | A device consisting of many movable leaves that shape the radiation beam to match the tumour contour. | 由多个可移动叶片组成的装置，用于将辐射束塑形以匹配肿瘤轮廓。 | Forgetting MLCs are dynamic and can change shape during treatment. |
| **Dose Fractionation** / 剂量分次 | The practice of dividing the total radiation dose into smaller daily doses (fractions) over several weeks. | 将总辐射剂量分成数周内每天给予的较小剂量（分次）的做法。 | Confusing fractionation with total dose; fractionation is about schedule. |
| **Planning Target Volume (PTV)** / 计划靶区 | The volume that includes the tumour plus a margin for setup errors and organ motion. | 包含肿瘤以及为摆位误差和器官运动预留边界的体积。 | Thinking PTV is the same as the visible tumour; it includes margins. |
| **Dose-Volume Histogram (DVH)** / 剂量体积直方图 | A graph showing the relationship between radiation dose and the volume of a structure receiving that dose. | 显示辐射剂量与接受该剂量的结构体积之间关系的图表。 | Misinterpreting the y-axis as number of patients; it's volume percentage. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Linear Accelerator (Linac) Operation / 直线加速器工作原理

### Explanation / 解释
**English:** A [[Linear Accelerator (Linac)]] uses high-frequency electromagnetic waves to accelerate electrons along a waveguide. The electrons gain kinetic energy as they travel through a series of accelerating cavities. At the end of the waveguide, the high-energy electrons strike a tungsten target, producing bremsstrahlung X-rays. These X-rays are then collimated and shaped before being directed at the patient's tumour. The energy of the X-rays is typically in the range of 6-20 MV (megavoltage), which allows deep penetration into the body.

**中文:** 直线加速器利用高频电磁波沿波导管加速电子。电子在通过一系列加速腔时获得动能。在波导管末端，高能电子撞击钨靶，产生轫致辐射X射线。这些X射线在准直和塑形后，被导向患者的肿瘤。X射线的能量通常在6-20 MV（兆伏）范围内，能够深入穿透人体。

### Physical Meaning / 物理意义
**English:** The high energy of the X-rays (megavoltage) is crucial because it provides a "skin-sparing" effect: the maximum dose is deposited several centimetres below the skin surface, reducing damage to the skin. This is due to the build-up effect, where secondary electrons from Compton scattering reach equilibrium at depth.

**中文:** X射线的高能量（兆伏级）至关重要，因为它提供了"皮肤保护"效应：最大剂量沉积在皮肤表面下几厘米处，减少了对皮肤的损伤。这是由于累积效应，康普顿散射产生的次级电子在深处达到平衡。

### Common Misconceptions / 常见误区
- **Misconception:** Linacs produce radiation directly. → **Correction:** They accelerate electrons; X-rays are produced when electrons hit the target.
- **Misconception:** Higher energy always means better treatment. → **Correction:** Higher energy gives deeper penetration but may increase neutron contamination.
- **Misconception:** The beam is perfectly uniform. → **Correction:** Beam flattening filters are used to make the beam uniform across the field.

### Exam Tips / 考试提示
- **CAIE:** Be able to describe the basic linac components: electron gun, waveguide, bending magnet, target, collimator.
- **Edexcel:** Understand the role of the bending magnet (to direct the electron beam to the target) and the difference between electron and photon modes.

> 📷 **IMAGE PROMPT — EBRT-01: Linear Accelerator Schematic**
> A labelled cross-sectional diagram of a medical linear accelerator showing: electron gun, accelerating waveguide, bending magnet, tungsten target, primary collimator, flattening filter, monitor ionization chamber, and multileaf collimator. Arrows show electron path (blue) and X-ray path (red). Clean, educational style with clear labels.

## 4.2 Beam Shaping and Collimation / 光束塑形与准直

### Explanation / 解释
**English:** The radiation beam must be shaped to conform to the tumour while avoiding critical structures. This is achieved using a [[Multileaf Collimator (MLC)]], which consists of 60-160 pairs of tungsten leaves that can move independently. The MLC creates an irregular field shape that matches the tumour's projection from the beam's eye view. Modern IMRT (Intensity Modulated Radiotherapy) uses dynamic MLC motion to modulate the beam intensity across the field.

**中文:** 辐射束必须塑形以贴合肿瘤，同时避开关键结构。这是通过多叶准直器（MLC）实现的，它由60-160对可独立移动的钨叶片组成。MLC创建出不规则射野形状，从射束视角匹配肿瘤的投影。现代IMRT（调强放疗）使用动态MLC运动来调制整个射野的束流强度。

### Physical Meaning / 物理意义
**English:** The MLC replaces traditional lead blocks, allowing for more precise and efficient treatment. The leaves are typically 5-10 mm wide at the isocentre, providing high spatial resolution. The penumbra (the region of rapid dose fall-off at the field edge) is minimized by using focused leaf ends and rounded leaf tips.

**中文:** MLC取代了传统的铅块，实现了更精确、更高效的治疗。叶片在等中心处通常宽5-10毫米，提供高空间分辨率。通过使用聚焦叶片端和圆形叶片尖端，最小化了半影（射野边缘剂量快速下降的区域）。

### Common Misconceptions / 常见误区
- **Misconception:** MLC leaves are perfectly straight. → **Correction:** They are slightly divergent to match the beam geometry.
- **Misconception:** MLCs only create static fields. → **Correction:** They can move during treatment (dynamic MLC) for IMRT.

### Exam Tips / 考试提示
- **CAIE:** Describe how collimators reduce the field size and shape the beam.
- **Edexcel:** Understand the difference between conventional collimators and MLCs, and the concept of "step-and-shoot" vs "dynamic" MLC.

> 📷 **IMAGE PROMPT — EBRT-02: Multileaf Collimator**
> A 3D rendering of a multileaf collimator showing 60 pairs of tungsten leaves in different positions. The leaves are arranged in two banks (left and right) with a central opening shaped like an irregular tumour. Labels indicate leaf width, leaf travel direction, and the isocentre. The background shows a patient outline with the tumour in red.

## 4.3 Dose Fractionation / 剂量分次

### Explanation / 解释
**English:** [[Dose Fractionation]] is the practice of delivering the total radiation dose in multiple smaller doses (fractions) over several weeks. For example, a typical course might be 60 Gy delivered in 30 fractions of 2 Gy each, given daily from Monday to Friday. The biological rationale is based on the "4 Rs" of radiobiology: Repair, Repopulation, Redistribution, and Reoxygenation. Fractionation allows normal cells to repair sublethal damage between fractions, while cancer cells are more vulnerable due to their reduced repair capacity.

**中文:** 剂量分次是将总辐射剂量分成数周内多次给予的较小剂量（分次）的做法。例如，典型疗程可能是60 Gy，分30次给予，每次2 Gy，周一至周五每天一次。其生物学原理基于放射生物学的"4个R"：修复、再增殖、再分布和再氧合。分次允许正常细胞在分次之间修复亚致死损伤，而癌细胞由于修复能力降低而更易受损。

### Physical Meaning / 物理意义
**English:** The linear-quadratic (LQ) model describes the cell survival curve: $S = e^{-(\alpha D + \beta D^2)}$, where $\alpha$ and $\beta$ are tissue-specific parameters. The $\alpha/\beta$ ratio indicates the tissue's sensitivity to fractionation. Late-responding tissues (e.g., spinal cord) have low $\alpha/\beta$ (~2-3 Gy) and are more sensitive to fraction size, while early-responding tissues (e.g., skin) have high $\alpha/\beta$ (~10 Gy).

**中文:** 线性-二次（LQ）模型描述了细胞存活曲线：$S = e^{-(\alpha D + \beta D^2)}$，其中$\alpha$和$\beta$是组织特异性参数。$\alpha/\beta$比值表示组织对分次的敏感性。晚反应组织（如脊髓）具有低$\alpha/\beta$（约2-3 Gy），对分次大小更敏感，而早反应组织（如皮肤）具有高$\alpha/\beta$（约10 Gy）。

### Common Misconceptions / 常见误区
- **Misconception:** Fractionation reduces the total dose needed. → **Correction:** Fractionation allows a higher total dose to be given safely.
- **Misconception:** All tumours respond the same to fractionation. → **Correction:** Different tumours have different $\alpha/\beta$ ratios.

### Exam Tips / 考试提示
- **CAIE:** Explain why fractionation is used (spares normal tissue, damages tumour).
- **Edexcel:** Be able to use the LQ model conceptually and interpret $\alpha/\beta$ ratios.

---

# 5. Essential Equations / 核心公式

## 5.1 Linear-Quadratic (LQ) Model / 线性-二次模型

$$ S = e^{-(\alpha D + \beta D^2)} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $S$ | Surviving fraction of cells | 细胞存活分数 | dimensionless |
| $D$ | Radiation dose | 辐射剂量 | Gy |
| $\alpha$ | Linear coefficient (single-hit killing) | 线性系数（单次击中杀伤） | Gy$^{-1}$ |
| $\beta$ | Quadratic coefficient (two-hit killing) | 二次系数（两次击中杀伤） | Gy$^{-2}$ |

**Derivation / 推导:** The LQ model assumes cell killing occurs via two mechanisms: single-track events (proportional to $\alpha D$) and two-track events (proportional to $\beta D^2$). The equation is empirical but well-supported by radiobiological data.

**Conditions / 适用条件:**
- **English:** Valid for doses up to ~8-10 Gy per fraction. For higher doses (e.g., stereotactic radiosurgery), modified models are used.
- **中文:** 适用于每分次剂量高达约8-10 Gy。对于更高剂量（如立体定向放射外科），使用修正模型。

**Limitations / 局限性:**
- **English:** Does not account for repair kinetics, cell cycle effects, or tumour heterogeneity.
- **中文:** 未考虑修复动力学、细胞周期效应或肿瘤异质性。

## 5.2 Biologically Effective Dose (BED) / 生物有效剂量

$$ \text{BED} = n d \left(1 + \frac{d}{\alpha/\beta}\right) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| BED | Biologically Effective Dose | 生物有效剂量 | Gy |
| $n$ | Number of fractions | 分次数 | dimensionless |
| $d$ | Dose per fraction | 每分次剂量 | Gy |
| $\alpha/\beta$ | Alpha/beta ratio for the tissue | 组织的α/β比值 | Gy |

**Derivation / 推导:** Derived from the LQ model by equating the log cell kill for different fractionation schemes.

**Conditions / 适用条件:**
- **English:** Used to compare different fractionation schedules. Assumes complete repair between fractions.
- **中文:** 用于比较不同分次方案。假设分次之间完全修复。

**Limitations / 局限性:**
- **English:** Does not account for repopulation during treatment.
- **中文:** 未考虑治疗期间的再增殖。

## 5.3 Percentage Depth Dose (PDD) / 百分深度剂量

$$ \text{PDD}(d) = \frac{D_d}{D_{d_{\text{max}}}} \times 100\% $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| PDD($d$) | Percentage depth dose at depth $d$ | 深度$d$处的百分深度剂量 | % |
| $D_d$ | Dose at depth $d$ | 深度$d$处的剂量 | Gy |
| $D_{d_{\text{max}}}$ | Dose at depth of maximum dose ($d_{\text{max}}$) | 最大剂量深度($d_{\text{max}}$)处的剂量 | Gy |

**Conditions / 适用条件:**
- **English:** Depends on beam energy, field size, and source-to-surface distance (SSD).
- **中文:** 取决于射束能量、射野大小和源皮距（SSD）。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Percentage Depth Dose (PDD) Curves / 百分深度剂量曲线

### Axes / 坐标轴
- **X-axis:** Depth in tissue (cm) / 组织深度 (cm)
- **Y-axis:** Percentage depth dose (%) / 百分深度剂量 (%)

### Shape / 形状
**English:** For megavoltage X-rays, the PDD curve shows a characteristic build-up region: dose increases from the surface to a maximum at depth $d_{\text{max}}$, then decreases approximately exponentially. For 6 MV X-rays, $d_{\text{max}}$ is about 1.5 cm; for 18 MV, about 3.5 cm. The surface dose is typically 30-50% of the maximum.

**中文:** 对于兆伏级X射线，PDD曲线显示特征性的累积区域：剂量从表面增加到深度$d_{\text{max}}$处的最大值，然后近似指数下降。对于6 MV X射线，$d_{\text{max}}$约为1.5 cm；对于18 MV，约为3.5 cm。表面剂量通常为最大值的30-50%。

### Gradient Meaning / 斜率含义
**English:** The gradient in the build-up region indicates the rate of dose increase due to secondary electron equilibrium. The gradient in the fall-off region indicates the attenuation of the primary beam.

**中文:** 累积区域的斜率表示由于次级电子平衡导致的剂量增加速率。下降区域的斜率表示主射束的衰减。

### Area Meaning / 面积含义
**English:** The area under the PDD curve is proportional to the integral dose delivered to the tissue.

**中文:** PDD曲线下的面积与传递给组织的积分剂量成正比。

### Exam Interpretation / 考试解读
- **CAIE:** Compare PDD curves for different energies; explain why higher energy gives better skin sparing.
- **Edexcel:** Use PDD curves to calculate dose at depth; understand the effect of field size on PDD.

> 📷 **IMAGE PROMPT — EBRT-03: PDD Curves for Different Energies**
> A graph showing three PDD curves for 6 MV, 10 MV, and 18 MV X-rays. X-axis: 0-20 cm depth. Y-axis: 0-100% dose. The 6 MV curve peaks at ~1.5 cm with surface dose ~40%, the 18 MV curve peaks at ~3.5 cm with surface dose ~25%. Clear labels showing $d_{\text{max}}$ for each energy. Educational style with gridlines.

## 6.2 Dose-Volume Histogram (DVH) / 剂量体积直方图

### Axes / 坐标轴
- **X-axis:** Dose (Gy) / 剂量 (Gy)
- **Y-axis:** Volume (%) / 体积 (%)

### Shape / 形状
**English:** A cumulative DVH shows the percentage of a structure's volume that receives at least a given dose. For a tumour (PTV), an ideal DVH is a step function: 100% of the volume receives the prescription dose. For organs at risk (OARs), the DVH should show low volumes receiving high doses.

**中文:** 累积DVH显示结构体积中接受至少给定剂量的百分比。对于肿瘤（PTV），理想DVH是阶跃函数：100%体积接受处方剂量。对于危及器官（OARs），DVH应显示接受高剂量的体积较小。

### Gradient Meaning / 斜率含义
**English:** A steep gradient in the DVH indicates a sharp dose fall-off at the edge of the structure, which is desirable for sparing OARs.

**中文:** DVH中的陡峭梯度表示结构边缘剂量急剧下降，这对于保护OARs是可取的。

### Area Meaning / 面积含义
**English:** The area under the DVH curve is related to the mean dose to the structure.

**中文:** DVH曲线下的面积与结构的平均剂量相关。

### Exam Interpretation / 考试解读
- **Edexcel only:** Interpret DVH curves to compare treatment plans. A plan with a lower volume of OAR receiving high dose is better.

> 📷 **IMAGE PROMPT — EBRT-04: Dose-Volume Histogram**
> A cumulative DVH graph showing three curves: PTV (red), spinal cord (blue), and parotid gland (green). The PTV curve shows 95% volume receiving 60 Gy. The spinal cord curve shows 0% volume receiving >45 Gy. The parotid curve shows 50% volume receiving >30 Gy. Clear axes labels and legend.

---

# 7. Required Diagrams / 必备图表

## 7.1 Linear Accelerator Cross-Section / 直线加速器剖面图

### Description / 描述
**English:** A labelled diagram showing the internal components of a medical linear accelerator, including the electron gun, accelerating waveguide, bending magnet, target, flattening filter, monitor chambers, and collimator assembly.

**中文:** 显示医用直线加速器内部组件的标注图，包括电子枪、加速波导管、偏转磁铁、靶、均整过滤器、监测电离室和准直器组件。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — EBRT-05: Linac Internal Components**
> A detailed cross-sectional diagram of a medical linear accelerator. The electron gun is at the top, followed by the accelerating waveguide (shown as a series of cavities). A bending magnet (90-degree) directs the electron beam to the tungsten target. Below the target: primary collimator, flattening filter, monitor ionization chamber (two parallel plates), and the multileaf collimator. All components labelled with arrows. Clean, technical illustration style with blue background.

### Labels Required / 需要标注
- Electron gun / 电子枪
- Accelerating waveguide / 加速波导管
- Bending magnet / 偏转磁铁
- Tungsten target / 钨靶
- Primary collimator / 初级准直器
- Flattening filter / 均整过滤器
- Monitor ionization chamber / 监测电离室
- Multileaf collimator (MLC) / 多叶准直器

### Exam Importance / 考试重要性
- **CAIE:** High — be able to describe the function of each component.
- **Edexcel:** High — understand the electron-to-photon conversion process.

## 7.2 Treatment Planning Geometry / 治疗计划几何

### Description / 描述
**English:** A diagram showing the relationship between the Gross Tumour Volume (GTV), Clinical Target Volume (CTV), Planning Target Volume (PTV), and Organs at Risk (OARs). Also shows the beam arrangement (e.g., 3-field or 5-field IMRT).

**中文:** 显示大体肿瘤体积（GTV）、临床靶体积（CTV）、计划靶体积（PTV）和危及器官（OARs）之间关系的图。还显示射束排列（例如，3野或5野IMRT）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — EBRT-06: Target Volume Definitions**
> A cross-sectional CT image of a pelvis showing a prostate tumour. Overlaid contours: GTV (red, solid), CTV (orange, dashed), PTV (yellow, dotted). A margin of 5-10 mm is visible between each contour. Nearby OARs: bladder (blue), rectum (green). Five beam directions (arrows) are shown entering from different angles. Labels: GTV, CTV, PTV, bladder, rectum, beam directions.

### Labels Required / 需要标注
- GTV (Gross Tumour Volume) / 大体肿瘤体积
- CTV (Clinical Target Volume) / 临床靶体积
- PTV (Planning Target Volume) / 计划靶体积
- OAR (Organ at Risk) / 危及器官
- Beam directions / 射束方向

### Exam Importance / 考试重要性
- **CAIE:** Medium — understand the concept of margins.
- **Edexcel:** High — understand the relationship between volumes and how they affect treatment planning.

---

# 8. Worked Examples / 典型例题

## Example 1: PDD Calculation / PDD计算

### Question / 题目
**English:** A 6 MV X-ray beam has a PDD of 67% at a depth of 10 cm for a 10×10 cm field. If the dose at $d_{\text{max}}$ (1.5 cm) is 1.0 Gy, calculate the dose at 10 cm depth.

**中文:** 一个6 MV X射线束在10×10 cm射野下，10 cm深度处的PDD为67%。如果$d_{\text{max}}$（1.5 cm）处的剂量为1.0 Gy，计算10 cm深度处的剂量。

### Solution / 解答
**Step 1:** Recall the PDD formula:
$$ \text{PDD}(d) = \frac{D_d}{D_{d_{\text{max}}}} \times 100\% $$

**Step 2:** Rearrange to find $D_d$:
$$ D_d = \frac{\text{PDD}(d)}{100\%} \times D_{d_{\text{max}}} $$

**Step 3:** Substitute values:
$$ D_d = \frac{67\%}{100\%} \times 1.0 \text{ Gy} = 0.67 \text{ Gy} $$

### Final Answer / 最终答案
**Answer:** 0.67 Gy | **答案：** 0.67 Gy

### Quick Tip / 提示
**English:** Always check that the PDD is given as a percentage. Convert to decimal before multiplying.
**中文:** 始终检查PDD是否以百分比给出。在相乘前转换为小数。

## Example 2: BED Calculation / BED计算

### Question / 题目
**English:** A prostate tumour (α/β = 1.5 Gy) is treated with 74 Gy in 37 fractions. Calculate the BED. If the same BED is to be delivered using 3 Gy per fraction, how many fractions are needed?

**中文:** 一个前列腺肿瘤（α/β = 1.5 Gy）接受74 Gy分37次治疗。计算BED。如果使用每分次3 Gy传递相同的BED，需要多少次？

### Solution / 解答
**Step 1:** Calculate BED for the standard schedule:
$$ \text{BED} = n d \left(1 + \frac{d}{\alpha/\beta}\right) $$
$$ \text{BED} = 37 \times 2 \left(1 + \frac{2}{1.5}\right) = 74 \times (1 + 1.333) = 74 \times 2.333 = 172.6 \text{ Gy} $$

**Step 2:** For the new schedule with $d = 3$ Gy:
$$ 172.6 = n \times 3 \left(1 + \frac{3}{1.5}\right) = n \times 3 \times (1 + 2) = n \times 9 $$
$$ n = \frac{172.6}{9} = 19.2 \approx 19 \text{ fractions} $$

### Final Answer / 最终答案
**Answer:** BED = 172.6 Gy; 19 fractions needed | **答案：** BED = 172.6 Gy；需要19次

### Quick Tip / 提示
**English:** For low α/β tumours (like prostate), larger fraction sizes are more damaging. Always round fractions to the nearest whole number.
**中文:** 对于低α/β肿瘤（如前列腺），较大的分次剂量更具损伤性。始终将分次数四舍五入到最接近的整数。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Describe linac operation / 描述直线加速器工作原理 | High | Medium | 📝 *待填入* |
| Explain fractionation rationale / 解释分次原理 | High | Medium | 📝 *待填入* |
| Interpret PDD curves / 解读PDD曲线 | Medium | Medium | 📝 *待填入* |
| Calculate BED / 计算BED | Medium | Hard | 📝 *待填入* |
| Compare treatment plans using DVH (Edexcel) / 使用DVH比较治疗计划 | Low (Edexcel) | Hard | 📝 *待填入* |
| Explain MLC function / 解释MLC功能 | Medium | Easy | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Describe / 描述:** Give a detailed account of the features or operation.
- **Explain / 解释:** Give reasons for why something happens.
- **Calculate / 计算:** Use mathematical methods to find a numerical answer.
- **Compare / 比较:** Describe similarities and differences.
- **State / 陈述:** Give a brief answer without explanation.

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
External Beam Radiotherapy connects to practical physics in several ways:

1. **Dosimetry Measurements:** Using ionization chambers and phantoms to measure PDD curves and beam profiles. This involves setting up equipment, taking readings at different depths, and plotting graphs.

2. **Uncertainty Analysis:** Dose delivery must be accurate to within ±5%. Students should understand how uncertainties in calibration, positioning, and machine output affect the delivered dose.

3. **Graph Plotting:** Plotting PDD curves from measured data, determining $d_{\text{max}}$, and calculating beam quality indices.

4. **Treatment Plan Verification:** Using film or diode arrays to verify that the delivered dose matches the planned dose.

5. **Quality Assurance (QA):** Daily, monthly, and annual QA checks on linac output, beam flatness, and MLC positioning.

**中文:**
外照射放疗通过以下方式与实验物理联系：

1. **剂量测量：** 使用电离室和体模测量PDD曲线和射束剖面。涉及设备设置、不同深度读数记录和图表绘制。

2. **不确定度分析：** 剂量传递必须精确到±5%以内。学生应理解校准、定位和机器输出中的不确定度如何影响传递剂量。

3. **图表绘制：** 根据测量数据绘制PDD曲线，确定$d_{\text{max}}$，计算射束质量指数。

4. **治疗计划验证：** 使用胶片或二极管阵列验证传递剂量与计划剂量是否匹配。

5. **质量保证（QA）：** 对直线加速器输出、射束平坦度和MLC定位进行每日、每月和年度QA检查。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    EBRT[External Beam Radiotherapy] --> Linac[Linear Accelerator]
    EBRT --> Collimation[Beam Collimation]
    EBRT --> Fractionation[Dose Fractionation]
    EBRT --> Planning[Treatment Planning]
    
    Linac --> ElectronGun[Electron Gun]
    Linac --> Waveguide[Accelerating Waveguide]
    Linac --> Target[Tungsten Target]
    Linac --> BendingMagnet[Bending Magnet]
    
    Collimation --> MLC[Multileaf Collimator]
    Collimation --> Penumbra[Penumbra Effect]
    
    Fractionation --> LQModel[Linear-Quadratic Model]
    Fractionation --> BED[Biologically Effective Dose]
    Fractionation --> AlphaBeta[Alpha/Beta Ratio]
    
    Planning --> GTV[Gross Tumour Volume]
    Planning --> CTV[Clinical Target Volume]
    Planning --> PTV[Planning Target Volume]
    Planning --> OAR[Organs at Risk]
    Planning --> DVH[Dose-Volume Histogram]
    
    LQModel --> CellSurvival[Cell Survival Curve]
    
    EBRT --> PDD[Percentage Depth Dose]
    PDD --> BuildUp[Build-up Region]
    PDD --> SkinSparing[Skin Sparing Effect]
    
    EBRT --> IMRT[Intensity Modulated Radiotherapy]
    IMRT --> DynamicMLC[Dynamic MLC Motion]
    
    EBRT --> QA[Quality Assurance]
    QA --> Dosimetry[Dosimetry Measurements]
    
    %% Links to parent and siblings
    EBRT -->|Parent| Radiotherapy[Radiotherapy and Nuclear Medicine Treatment]
    Radiotherapy --> Brachytherapy[Brachytherapy (Internal Radiotherapy)]
    Radiotherapy --> TAT[Targeted Alpha Therapy and Nuclear Medicine]
    Radiotherapy --> Protection[Radiation Protection and Dosimetry]
    Radiotherapy --> Risks[Benefits vs Risks of Medical Radiation]
    
    %% Prerequisites
    EBRT -->|Prerequisite| Radiation[Alpha, Beta and Gamma Radiation]
    EBRT -->|Prerequisite| PET[PET Scans and Nuclear Medicine]
    EBRT -->|Related| Xrays[X-rays and Medical Imaging]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | EBRT delivers radiation from outside the body using a linac. / 外照射放疗使用直线加速器从体外传递辐射。 |
| **Key Formula / 核心公式** | LQ Model: $S = e^{-(\alpha D + \beta D^2)}$; BED: $\text{BED} = n d (1 + d/(\alpha/\beta))$; PDD: $\text{PDD}(d) = (D_d / D_{d_{\text{max}}}) \times 100\%$ |
| **Key Graph / 核心图表** | PDD curve: build-up to $d_{\text{max}}$, then exponential fall-off. Higher energy → deeper $d_{\text{max}}$ and better skin sparing. / PDD曲线：累积到$d_{\text{max}}$，然后指数下降。更高能量→更深的$d_{\text{max}}$和更好的皮肤保护。 |
| **Key Diagram / 核心图表** | Linac cross-section: electron gun → waveguide → bending magnet → target → collimator → MLC. / 直线加速器剖面：电子枪→波导管→偏转磁铁→靶→准直器→MLC。 |
| **Fractionation / 分次** | Divides total dose into smaller fractions to spare normal tissue. Based on 4 Rs: Repair, Repopulation, Redistribution, Reoxygenation. / 将总剂量分成小分次以保护正常组织。基于4个R：修复、再增殖、再分布、再氧合。 |
| **MLC / 多叶准直器** | 60-160 pairs of tungsten leaves that shape the beam to match tumour contour. Used in IMRT for intensity modulation. / 60-160对钨叶片，将射束塑形以匹配肿瘤轮廓。用于IMRT进行强度调制。 |
| **Treatment Volumes / 治疗体积** | GTV (visible tumour) → CTV (GTV + microscopic spread) → PTV (CTV + margins for motion/setup errors). / GTV（可见肿瘤）→ CTV（GTV + 微观扩散）→ PTV（CTV + 运动和摆位误差边界）。 |
| **DVH (Edexcel) / 剂量体积直方图** | Cumulative graph showing volume receiving ≥ given dose. Ideal: PTV step function, OAR low volume at high dose. / 累积图显示接受≥给定剂量的体积。理想：PTV阶跃函数，OAR在高剂量处体积小。 |
| **Exam Tip / 考试提示** | For CAIE: focus on principles and fractionation. For Edexcel: include DVH interpretation and BED calculations. / CAIE：关注原理和分次。Edexcel：包括DVH解读和BED计算。 |
| **Common Mistake / 常见错误** | Confusing EBRT with brachytherapy; thinking linacs produce radiation directly; forgetting PDD is a percentage. / 混淆EBRT和近距离治疗；认为直线加速器直接产生辐射；忘记PDD是百分比。 |