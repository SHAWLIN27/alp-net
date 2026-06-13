# 1. Overview / 概述

**English:**
This sub-topic explores how engineers and designers use [[Stress-Strain Graphs and Material Behaviour]] to select appropriate materials for real-world applications. Building on the understanding of [[Stress, Strain and Young Modulus]] and the characteristic curves for [[Stress-Strain Graph for a Ductile Material (Copper)]], [[Stress-Strain Graph for a Brittle Material (Glass)]], and [[Stress-Strain Graph for a Polymeric Material (Rubber)]], we now focus on the practical decision-making process. Key material properties derived from stress-strain graphs—such as [[Elastic and Plastic Regions]], [[Necking and Fracture]], yield strength, ultimate tensile strength (UTS), and stiffness—are used to match materials to specific engineering requirements. This sub-topic bridges theoretical material science with practical engineering design, covering safety factors, cost considerations, and performance trade-offs.

**中文:**
本子知识点探讨工程师和设计师如何利用[[应力-应变图与材料行为]]为实际应用选择合适的材料。在理解[[应力、应变与杨氏模量]]以及[[韧性材料（铜）的应力-应变图]]、[[脆性材料（玻璃）的应力-应变图]]和[[聚合物材料（橡胶）的应力-应变图]]的特征曲线基础上，我们现在聚焦于实际的决策过程。从应力-应变图中得出的关键材料属性——如[[弹性区与塑性区]]、[[颈缩与断裂]]、屈服强度、极限抗拉强度（UTS）和刚度——被用来将材料与特定的工程要求相匹配。本子知识点将理论材料科学与实际工程设计联系起来，涵盖安全系数、成本考虑和性能权衡。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 6.3(a): Understand how to select materials for specific applications based on their mechanical properties | WPH11 U1: 2.13: Understand how to select materials for specific applications using stress-strain graphs |
| 6.3(b): Explain the use of safety factors in engineering design | WPH11 U1: 2.14: Explain the concept of safety factor and its application |
| 6.3(c): Compare and contrast materials for different applications (e.g., bridges, aircraft, sports equipment) | WPH11 U1: 2.15: Compare materials for different applications using stress-strain data |
| 6.3(d): Understand the importance of stiffness, strength, and toughness in material selection | WPH11 U1: 2.16: Understand the terms stiffness, strength, and toughness |
| 6.3(e): Evaluate the suitability of materials for given applications | WPH11 U1: 2.17: Evaluate material suitability using stress-strain graphs |
| | WPH11 U1: 2.18: Understand the economic and environmental factors in material selection |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to read stress-strain graphs and extract key values (yield stress, UTS, breaking stress, Young modulus). They should justify material choices using quantitative data and explain the role of safety factors. For higher marks, students must discuss trade-offs (e.g., strength vs. weight, cost vs. performance).
- **中文:** 学生必须能够读取应力-应变图并提取关键数值（屈服应力、极限抗拉强度、断裂应力、杨氏模量）。他们应使用定量数据证明材料选择的合理性，并解释安全系数的作用。对于高分，学生必须讨论权衡（例如，强度与重量、成本与性能）。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Yield Strength** / 屈服强度 | The maximum stress a material can withstand without permanent (plastic) deformation. | 材料在不发生永久（塑性）变形的情况下能承受的最大应力。 | Confusing with UTS; yield strength is for elastic limit, UTS is for maximum load before fracture. |
| **Ultimate Tensile Strength (UTS)** / 极限抗拉强度 | The maximum stress a material can withstand before it fractures or necks. | 材料在断裂或颈缩前能承受的最大应力。 | Thinking UTS is the breaking stress; UTS is the peak, breaking stress is lower. |
| **Stiffness** / 刚度 | The resistance of a material to elastic deformation; measured by Young modulus (gradient of elastic region). | 材料抵抗弹性变形的能力；由杨氏模量（弹性区斜率）衡量。 | Confusing stiffness with strength; a stiff material may be brittle. |
| **Toughness** / 韧性 | The ability of a material to absorb energy before fracturing; area under the stress-strain curve. | 材料在断裂前吸收能量的能力；应力-应变曲线下的面积。 | Confusing with strength; tough materials have large area under curve, not just high stress. |
| **Safety Factor** / 安全系数 | The ratio of the material's ultimate strength to the maximum allowable working stress. | 材料极限强度与最大允许工作应力的比值。 | Forgetting that safety factor > 1; typical values are 2-5. |
| **Ductility** / 延展性 | The ability of a material to undergo large plastic deformation before fracture. | 材料在断裂前发生大量塑性变形的能力。 | Confusing with toughness; ductility is about deformation, toughness is about energy absorption. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Material Selection Criteria / 材料选择标准

### Explanation / 解释
**English:** When selecting a material for an engineering application, engineers consider several mechanical properties derived from the [[Stress-Strain Graphs and Material Behaviour]]:
1. **Stiffness** (Young modulus): How much does the material deflect under load? For a bridge girder, high stiffness (steel) is needed to prevent excessive sagging.
2. **Strength** (Yield strength and UTS): What is the maximum load the material can withstand? For a pressure vessel, high UTS is critical.
3. **Toughness** (Area under curve): Can the material absorb impact energy without fracturing? For car bumpers, high toughness (polymers) is desirable.
4. **Ductility** (Strain at fracture): Can the material be formed or bent? For electrical wiring, high ductility (copper) is essential.
5. **Brittleness**: Does the material fracture without warning? For safety-critical applications, brittle materials (glass) are avoided unless reinforced.

**中文:** 在为工程应用选择材料时，工程师会考虑从[[应力-应变图与材料行为]]中得出的几个力学性能：
1. **刚度**（杨氏模量）：材料在载荷下变形多少？对于桥梁大梁，需要高刚度（钢）以防止过度下垂。
2. **强度**（屈服强度和极限抗拉强度）：材料能承受的最大载荷是多少？对于压力容器，高极限抗拉强度至关重要。
3. **韧性**（曲线下面积）：材料能否吸收冲击能量而不断裂？对于汽车保险杠，高韧性（聚合物）是可取的。
4. **延展性**（断裂应变）：材料能否被成型或弯曲？对于电线，高延展性（铜）是必需的。
5. **脆性**：材料是否会在没有预警的情况下断裂？对于安全关键应用，除非经过增强，否则避免使用脆性材料（玻璃）。

### Physical Meaning / 物理意义
**English:** The stress-strain graph is a "fingerprint" of a material's mechanical behavior. The shape tells engineers everything they need to know: the slope of the elastic region gives stiffness, the height of the curve gives strength, and the area under the curve gives toughness. By comparing these features for different materials, engineers can make informed choices.

**中文:** 应力-应变图是材料力学行为的"指纹"。其形状告诉工程师他们需要知道的一切：弹性区的斜率给出刚度，曲线的高度给出强度，曲线下的面积给出韧性。通过比较不同材料的这些特征，工程师可以做出明智的选择。

### Common Misconceptions / 常见误区
- **English:**
  - "Stronger material is always better." → Not true; a strong but brittle material (e.g., glass) can fail catastrophically.
  - "Stiff material is the same as strong material." → No; stiffness is about elastic deformation, strength is about plastic deformation/fracture.
  - "Toughness is the same as strength." → No; toughness is energy absorption (area under curve), strength is maximum stress.
- **中文:**
  - "更强的材料总是更好。" → 不对；强但脆的材料（如玻璃）可能灾难性地失效。
  - "刚的材料就是强的材料。" → 不对；刚度是关于弹性变形，强度是关于塑性变形/断裂。
  - "韧性就是强度。" → 不对；韧性是能量吸收（曲线下面积），强度是最大应力。

### Exam Tips / 考试提示
- **English:** When asked to "select a material for X application," always justify your choice with at least two quantitative properties from the stress-strain graph. Use phrases like "high Young modulus for stiffness" or "large area under curve for toughness."
- **中文:** 当被要求"为X应用选择材料"时，始终用应力-应变图中至少两个定量属性来证明你的选择。使用"高杨氏模量以获得刚度"或"曲线下面积大以获得韧性"等短语。

---

## 4.2 Safety Factor / 安全系数

### Explanation / 解释
**English:** The safety factor (also called factor of safety) is a critical concept in engineering design. It accounts for uncertainties in material properties, loading conditions, manufacturing defects, and environmental factors. The safety factor is defined as:

$$ \text{Safety Factor} = \frac{\text{Ultimate Tensile Strength (UTS)}}{\text{Maximum Allowable Working Stress}} $$

For example, if a steel cable has UTS = 500 MPa and the maximum load it will experience is 100 MPa, the safety factor is 5. This means the cable can safely carry 5 times the expected maximum load.

Typical safety factors:
- Aircraft components: 1.5–2.0 (weight-critical, minimal safety margin)
- Bridges: 2.0–4.0 (public safety, moderate weight)
- Elevator cables: 10–12 (human life critical, high safety margin)

**中文:** 安全系数（也称为安全因子）是工程设计中的一个关键概念。它考虑了材料属性、载荷条件、制造缺陷和环境因素的不确定性。安全系数定义为：

$$ \text{安全系数} = \frac{\text{极限抗拉强度 (UTS)}}{\text{最大允许工作应力}} $$

例如，如果一根钢缆的极限抗拉强度为500 MPa，而它将承受的最大载荷为100 MPa，则安全系数为5。这意味着该钢缆可以安全地承受预期最大载荷的5倍。

典型安全系数：
- 飞机部件：1.5–2.0（重量关键，安全裕度最小）
- 桥梁：2.0–4.0（公共安全，中等重量）
- 电梯缆绳：10–12（人命关键，高安全裕度）

### Physical Meaning / 物理意义
**English:** The safety factor ensures that the working stress stays well within the [[Elastic and Plastic Regions|elastic region]] of the material, preventing any plastic deformation or fracture under normal operating conditions. It also provides a buffer for unexpected overloads.

**中文:** 安全系数确保工作应力保持在材料的[[弹性区与塑性区|弹性区]]内，防止在正常操作条件下发生任何塑性变形或断裂。它还为意外的过载提供了缓冲。

### Common Misconceptions / 常见误区
- **English:**
  - "Higher safety factor is always better." → Not true; excessive safety factor adds weight, cost, and material waste.
  - "Safety factor applies only to ultimate strength." → It can also be applied to yield strength for designs that must remain elastic.
- **中文:**
  - "安全系数越高越好。" → 不对；过高的安全系数会增加重量、成本和材料浪费。
  - "安全系数只适用于极限强度。" → 对于必须保持弹性的设计，它也可以应用于屈服强度。

### Exam Tips / 考试提示
- **English:** When calculating safety factor, always use UTS (or yield strength if specified) divided by working stress. State whether the design is safe (safety factor > 1) and comment on the margin.
- **中文:** 计算安全系数时，始终使用极限抗拉强度（或如果指定则使用屈服强度）除以工作应力。说明设计是否安全（安全系数 > 1）并评论裕度。

---

## 4.3 Trade-offs in Material Selection / 材料选择中的权衡

### Explanation / 解释
**English:** Real-world material selection involves balancing competing requirements. Common trade-offs include:
1. **Strength vs. Weight:** For aerospace applications, materials with high strength-to-weight ratio (e.g., titanium alloys, carbon fiber composites) are preferred, even if they are expensive.
2. **Stiffness vs. Ductility:** Ceramics are very stiff but brittle; polymers are ductile but flexible. Steel offers a good balance.
3. **Cost vs. Performance:** High-performance materials (e.g., carbon fiber) are expensive; for mass-produced items, cheaper materials (e.g., steel, aluminum) are used.
4. **Toughness vs. Hardness:** Hard materials (e.g., tool steel) resist wear but may be brittle; tough materials (e.g., rubber) absorb impact but wear easily.

**中文:** 现实世界中的材料选择涉及平衡相互竞争的要求。常见的权衡包括：
1. **强度与重量：** 对于航空航天应用，优先选择具有高强度重量比的材料（如钛合金、碳纤维复合材料），即使它们很昂贵。
2. **刚度与延展性：** 陶瓷非常刚但脆；聚合物有延展性但柔韧。钢提供了良好的平衡。
3. **成本与性能：** 高性能材料（如碳纤维）昂贵；对于大规模生产的产品，使用更便宜的材料（如钢、铝）。
4. **韧性与硬度：** 硬材料（如工具钢）耐磨但可能脆；韧性材料（如橡胶）吸收冲击但易磨损。

### Physical Meaning / 物理意义
**English:** The stress-strain graph visually represents these trade-offs. For example, comparing [[Stress-Strain Graph for a Ductile Material (Copper)]] and [[Stress-Strain Graph for a Brittle Material (Glass)]] shows that copper has lower strength but much higher ductility and toughness, while glass has high strength but zero ductility.

**中文:** 应力-应变图直观地表示了这些权衡。例如，比较[[韧性材料（铜）的应力-应变图]]和[[脆性材料（玻璃）的应力-应变图]]显示，铜的强度较低但延展性和韧性高得多，而玻璃强度高但延展性为零。

### Common Misconceptions / 常见误区
- **English:**
  - "The best material is the one with the highest strength." → Not true; application context matters (e.g., rubber for seals, not steel).
  - "Composite materials are always better than metals." → Not true; composites are expensive and difficult to repair.
- **中文:**
  - "最好的材料是强度最高的材料。" → 不对；应用背景很重要（例如，密封件用橡胶，不用钢）。
  - "复合材料总是比金属好。" → 不对；复合材料昂贵且难以修复。

### Exam Tips / 考试提示
- **English:** When discussing trade-offs, use comparative language: "Material A has higher stiffness but lower toughness than Material B, making it suitable for X but not Y."
- **中文:** 讨论权衡时，使用比较性语言："材料A比材料B具有更高的刚度但更低的韧性，使其适用于X但不适用于Y。"

---

# 5. Essential Equations / 核心公式

## 5.1 Safety Factor / 安全系数

$$ \text{Safety Factor} = \frac{\sigma_{\text{UTS}}}{\sigma_{\text{working}}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\sigma_{\text{UTS}}$ | Ultimate tensile strength | 极限抗拉强度 | Pa (or MPa) |
| $\sigma_{\text{working}}$ | Maximum allowable working stress | 最大允许工作应力 | Pa (or MPa) |

**Derivation / 推导:** The safety factor is a design ratio, not derived from first principles. It is chosen based on engineering standards and risk assessment.

**Conditions / 适用条件:**
- **English:** Safety factor > 1 for safe design. Typical values: 1.5–12 depending on application criticality.
- **中文:** 安全系数 > 1 为安全设计。典型值：1.5–12，取决于应用的关键性。

**Limitations / 局限性:**
- **English:** Does not account for fatigue, corrosion, or temperature effects. A separate safety factor may be needed for these.
- **中文:** 不考虑疲劳、腐蚀或温度效应。可能需要为这些因素单独设置安全系数。

---

## 5.2 Strength-to-Weight Ratio / 强度重量比

$$ \text{Specific Strength} = \frac{\sigma_{\text{UTS}}}{\rho} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\sigma_{\text{UTS}}$ | Ultimate tensile strength | 极限抗拉强度 | Pa (or MPa) |
| $\rho$ | Density | 密度 | kg/m³ |

**Derivation / 推导:** This is a figure of merit, not a derived equation. It allows comparison of materials on a per-unit-mass basis.

**Conditions / 适用条件:**
- **English:** Used for weight-critical applications (aerospace, automotive, sports equipment).
- **中文:** 用于重量关键的应用（航空航天、汽车、运动器材）。

**Limitations / 局限性:**
- **English:** Does not consider stiffness, toughness, or cost. A material with high specific strength may still be unsuitable if it is brittle or expensive.
- **中文:** 不考虑刚度、韧性或成本。具有高比强度的材料如果脆或昂贵，可能仍然不适合。

---

## 5.3 Stiffness-to-Weight Ratio / 刚度重量比

$$ \text{Specific Stiffness} = \frac{E}{\rho} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Young modulus | 杨氏模量 | Pa (or GPa) |
| $\rho$ | Density | 密度 | kg/m³ |

**Derivation / 推导:** Similar to specific strength, this compares stiffness per unit mass.

**Conditions / 适用条件:**
- **English:** Used for applications where deflection under self-weight is critical (e.g., long-span bridges, aircraft wings).
- **中文:** 用于自重下变形关键的应用（如大跨度桥梁、飞机机翼）。

**Limitations / 局限性:**
- **English:** Does not consider strength or toughness. A material with high specific stiffness may fracture under load.
- **中文:** 不考虑强度或韧性。具有高比刚度的材料可能在载荷下断裂。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Comparison of Stress-Strain Curves for Different Materials / 不同材料应力-应变曲线比较

### Axes / 坐标轴
- **X-axis:** Strain (ε) / 应变 (ε) — dimensionless
- **Y-axis:** Stress (σ) / 应力 (σ) — Pa or MPa

### Shape / 形状
**English:** The graph overlays the stress-strain curves for three material types:
- **Steel (ductile):** Linear elastic region, clear yield point, plastic region with strain hardening, necking, then fracture.
- **Glass (brittle):** Linear elastic region only, fracture at low strain with no plastic deformation.
- **Rubber (polymeric):** Non-linear elastic region, large strain before fracture, no clear yield point.

**中文:** 该图叠加了三种材料类型的应力-应变曲线：
- **钢（韧性）：** 线性弹性区，明显的屈服点，带有应变硬化的塑性区，颈缩，然后断裂。
- **玻璃（脆性）：** 仅有线性弹性区，在低应变下断裂，无塑性变形。
- **橡胶（聚合物）：** 非线性弹性区，断裂前应变大，无明显屈服点。

### Gradient Meaning / 斜率含义
**English:** The initial gradient of each curve gives the Young modulus (stiffness). Steel has the steepest gradient (highest stiffness), glass has a steep gradient but low strain range, rubber has a shallow gradient (low stiffness).

**中文:** 每条曲线的初始斜率给出杨氏模量（刚度）。钢的斜率最陡（刚度最高），玻璃斜率陡但应变范围小，橡胶斜率平缓（刚度低）。

### Area Meaning / 面积含义
**English:** The area under each curve up to fracture gives toughness. Steel has a large area (high toughness), glass has a very small area (low toughness), rubber has a moderate area (moderate toughness).

**中文:** 每条曲线到断裂为止的面积给出韧性。钢的面积大（韧性高），玻璃的面积非常小（韧性低），橡胶的面积中等（韧性中等）。

### Exam Interpretation / 考试解读
**English:** When comparing materials, always comment on:
1. Which material is stiffest (steepest initial gradient).
2. Which material is strongest (highest peak stress).
3. Which material is toughest (largest area under curve).
4. Which material is most ductile (largest strain at fracture).

**中文:** 比较材料时，始终评论：
1. 哪种材料最刚（初始斜率最陡）。
2. 哪种材料最强（峰值应力最高）。
3. 哪种材料最韧（曲线下面积最大）。
4. 哪种材料延展性最好（断裂应变最大）。

> 📷 **IMAGE PROMPT — GRAPH-01: Comparison of Stress-Strain Curves for Steel, Glass, and Rubber**
> A graph with three overlaid stress-strain curves. Steel: steep linear region, clear yield point, long plastic region, peak at ~400 MPa, fracture at ~0.2 strain. Glass: steep linear region, fracture at ~100 MPa, ~0.002 strain. Rubber: shallow non-linear curve, fracture at ~10 MPa, ~5 strain. Axes labeled "Stress (MPa)" and "Strain". Legend showing "Steel (Ductile)", "Glass (Brittle)", "Rubber (Polymeric)". Area under steel curve shaded to show toughness.

---

# 7. Required Diagrams / 必备图表

## 7.1 Material Selection Flowchart / 材料选择流程图

### Description / 描述
**English:** A flowchart showing the decision-making process for selecting a material for a given application. It starts with the application requirements (load, environment, cost), then considers mechanical properties (stiffness, strength, toughness), then evaluates trade-offs, and finally selects the material.

**中文:** 一个流程图，显示为给定应用选择材料的决策过程。它从应用要求（载荷、环境、成本）开始，然后考虑力学性能（刚度、强度、韧性），然后评估权衡，最后选择材料。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-01: Material Selection Flowchart**
> A flowchart with boxes and arrows. Start box: "Application Requirements (Load, Environment, Cost)". Arrow to "Identify Required Properties (Stiffness, Strength, Toughness)". Arrow to "List Candidate Materials (Steel, Aluminum, Titanium, Composites)". Arrow to "Evaluate Trade-offs (Weight, Cost, Durability)". Arrow to "Select Material". Decision diamond: "Does material meet all requirements?" with "Yes" arrow to "Final Selection" and "No" arrow back to "List Candidate Materials". Clean, professional style with blue and gray colors.

### Labels Required / 需要标注
- **English:** Application Requirements, Required Properties, Candidate Materials, Trade-offs, Final Selection
- **中文:** 应用要求、所需属性、候选材料、权衡、最终选择

### Exam Importance / 考试重要性
- **English:** High. Students are often asked to "describe the process of selecting a material for X application." This flowchart provides a structured answer.
- **中文:** 高。学生经常被要求"描述为X应用选择材料的过程。"这个流程图提供了一个结构化的答案。

---

## 7.2 Safety Factor Diagram / 安全系数示意图

### Description / 描述
**English:** A diagram showing a stress-strain curve with the working stress marked well below the yield strength and UTS. The safety factor is shown as the ratio between UTS and working stress.

**中文:** 一个显示应力-应变曲线的示意图，工作应力标记在屈服强度和极限抗拉强度以下很远的位置。安全系数显示为极限抗拉强度与工作应力之间的比值。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-02: Safety Factor on Stress-Strain Curve**
> A stress-strain curve for a ductile material (steel). Three horizontal dashed lines: "Working Stress (100 MPa)" near bottom, "Yield Strength (250 MPa)" in middle, "Ultimate Tensile Strength (500 MPa)" at top. Arrows showing "Safety Factor = 5" between working stress and UTS. Labels: "Elastic Region" and "Plastic Region". Clean engineering diagram style.

### Labels Required / 需要标注
- **English:** Working Stress, Yield Strength, Ultimate Tensile Strength, Safety Factor, Elastic Region, Plastic Region
- **中文:** 工作应力、屈服强度、极限抗拉强度、安全系数、弹性区、塑性区

### Exam Importance / 考试重要性
- **English:** High. Understanding the safety factor is essential for exam questions on engineering design and material selection.
- **中文:** 高。理解安全系数对于工程设计 and 材料选择的考试问题至关重要。

---

# 8. Worked Examples / 典型例题

## Example 1: Selecting Material for a Bicycle Frame / 为自行车车架选择材料

### Question / 题目
**English:** A bicycle frame must be lightweight, stiff, and strong. Three candidate materials are:
- **Steel:** Young modulus = 210 GPa, UTS = 500 MPa, Density = 7800 kg/m³, Cost = Low
- **Aluminum:** Young modulus = 70 GPa, UTS = 300 MPa, Density = 2700 kg/m³, Cost = Medium
- **Carbon Fiber:** Young modulus = 230 GPa, UTS = 600 MPa, Density = 1600 kg/m³, Cost = High

(a) Calculate the specific stiffness ($E/\rho$) for each material.
(b) Calculate the specific strength ($\sigma_{\text{UTS}}/\rho$) for each material.
(c) Which material would you recommend for a high-performance racing bicycle? Justify your answer.

**中文:** 一个自行车车架必须轻、刚且强。三种候选材料是：
- **钢：** 杨氏模量 = 210 GPa，极限抗拉强度 = 500 MPa，密度 = 7800 kg/m³，成本 = 低
- **铝：** 杨氏模量 = 70 GPa，极限抗拉强度 = 300 MPa，密度 = 2700 kg/m³，成本 = 中
- **碳纤维：** 杨氏模量 = 230 GPa，极限抗拉强度 = 600 MPa，密度 = 1600 kg/m³，成本 = 高

(a) 计算每种材料的比刚度（$E/\rho$）。
(b) 计算每种材料的比强度（$\sigma_{\text{UTS}}/\rho$）。
(c) 你会推荐哪种材料用于高性能赛车自行车？证明你的答案。

### Solution / 解答

**Part (a): Specific Stiffness / 比刚度**

$$ \text{Steel: } \frac{210 \times 10^9}{7800} = 2.69 \times 10^7 \, \text{m}^2/\text{s}^2 $$

$$ \text{Aluminum: } \frac{70 \times 10^9}{2700} = 2.59 \times 10^7 \, \text{m}^2/\text{s}^2 $$

$$ \text{Carbon Fiber: } \frac{230 \times 10^9}{1600} = 1.44 \times 10^8 \, \text{m}^2/\text{s}^2 $$

**Part (b): Specific Strength / 比强度**

$$ \text{Steel: } \frac{500 \times 10^6}{7800} = 6.41 \times 10^4 \, \text{m}^2/\text{s}^2 $$

$$ \text{Aluminum: } \frac{300 \times 10^6}{2700} = 1.11 \times 10^5 \, \text{m}^2/\text{s}^2 $$

$$ \text{Carbon Fiber: } \frac{600 \times 10^6}{1600} = 3.75 \times 10^5 \, \text{m}^2/\text{s}^2 $$

**Part (c): Recommendation / 推荐**

**English:** Carbon fiber is the best choice for a high-performance racing bicycle. It has the highest specific stiffness ($1.44 \times 10^8 \, \text{m}^2/\text{s}^2$) and the highest specific strength ($3.75 \times 10^5 \, \text{m}^2/\text{s}^2$), meaning it is both stiffest and strongest per unit mass. This allows for a lightweight frame that does not flex under load and can withstand high stresses. Although carbon fiber is expensive, for a racing bicycle, performance outweighs cost. Steel and aluminum have much lower specific properties, making them heavier for the same stiffness and strength.

**中文:** 碳纤维是高性能赛车自行车的最佳选择。它具有最高的比刚度（$1.44 \times 10^8 \, \text{m}^2/\text{s}^2$）和最高的比强度（$3.75 \times 10^5 \, \text{m}^2/\text{s}^2$），意味着每单位质量它既最刚又最强。这使得车架轻便，在载荷下不会弯曲，并能承受高应力。虽然碳纤维昂贵，但对于赛车自行车来说，性能胜过成本。钢和铝的比属性低得多，使得它们在相同刚度和强度下更重。

### Final Answer / 最终答案
**Answer:** Carbon fiber is recommended. | **答案：** 推荐碳纤维。

### Quick Tip / 提示
- **English:** Always calculate specific properties when weight is a factor. Use units consistently (convert GPa to Pa: 1 GPa = $10^9$ Pa).
- **中文:** 当重量是一个因素时，始终计算比属性。一致使用单位（将GPa转换为Pa：1 GPa = $10^9$ Pa）。

---

## Example 2: Safety Factor Calculation / 安全系数计算

### Question / 题目
**English:** A steel cable used in a suspension bridge has an ultimate tensile strength of 500 MPa. The maximum tension in the cable is 80 kN, and the cable has a cross-sectional area of $2.0 \times 10^{-4} \, \text{m}^2$.

(a) Calculate the working stress in the cable.
(b) Calculate the safety factor.
(c) Comment on whether this safety factor is appropriate for a bridge.

**中文:** 一座悬索桥中使用的钢缆极限抗拉强度为500 MPa。钢缆中的最大张力为80 kN，钢缆的横截面积为$2.0 \times 10^{-4} \, \text{m}^2$。

(a) 计算钢缆中的工作应力。
(b) 计算安全系数。
(c) 评论这个安全系数是否适合桥梁。

### Solution / 解答

**Part (a): Working Stress / 工作应力**

$$ \sigma_{\text{working}} = \frac{F}{A} = \frac{80 \times 10^3}{2.0 \times 10^{-4}} = 4.0 \times 10^8 \, \text{Pa} = 400 \, \text{MPa} $$

**Part (b): Safety Factor / 安全系数**

$$ \text{Safety Factor} = \frac{\sigma_{\text{UTS}}}{\sigma_{\text{working}}} = \frac{500}{400} = 1.25 $$

**Part (c): Comment / 评论**

**English:** A safety factor of 1.25 is too low for a bridge. Bridges are public safety structures and typically require a safety factor of 2.0–4.0. A factor of 1.25 means the cable would fail if the load increased by only 25%. This does not account for wind loads, corrosion, fatigue, or manufacturing defects. The design should use a thicker cable (larger cross-sectional area) to reduce working stress and increase the safety factor to at least 2.0.

**中文:** 1.25的安全系数对于桥梁来说太低了。桥梁是公共安全结构，通常需要2.0–4.0的安全系数。1.25的系数意味着如果载荷仅增加25%，钢缆就会失效。这没有考虑风载荷、腐蚀、疲劳或制造缺陷。设计应使用更粗的钢缆（更大的横截面积）以降低工作应力并将安全系数提高到至少2.0。

### Final Answer / 最终答案
**Answer:** (a) 400 MPa, (b) 1.25, (c) Too low for a bridge. | **答案：** (a) 400 MPa，(b) 1.25，(c) 对于桥梁来说太低。

### Quick Tip / 提示
- **English:** Always check units: convert kN to N, mm² to m². A safety factor below 2 is generally unacceptable for public structures.
- **中文:** 始终检查单位：将kN转换为N，将mm²转换为m²。对于公共结构，安全系数低于2通常不可接受。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Select material for application using stress-strain data | High | Medium | 📝 *待填入* |
| Calculate and comment on safety factor | High | Low-Medium | 📝 *待填入* |
| Compare materials using specific properties | Medium | Medium | 📝 *待填入* |
| Explain trade-offs in material selection | Medium | Medium-High | 📝 *待填入* |
| Evaluate suitability of material for given application | Low-Medium | High | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Select", "Justify", "Calculate", "Comment on", "Compare", "Evaluate", "Explain why"
- **中文:** "选择"、"证明"、"计算"、"评论"、"比较"、"评估"、"解释为什么"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in the following ways:
1. **Tensile Testing:** Students may perform a tensile test on different materials (e.g., copper wire, nylon thread, rubber band) to obtain stress-strain data. This directly provides the curves used for material selection.
2. **Data Analysis:** From the stress-strain graph, students must extract:
   - Young modulus (gradient of elastic region)
   - Yield strength (deviation from linearity)
   - UTS (peak stress)
   - Breaking stress (final point)
   - Toughness (area under curve — may require counting squares or integration)
3. **Uncertainties:** When calculating specific properties, students must propagate uncertainties from measurements of force, extension, and cross-sectional area.
4. **Graph Plotting:** Students should be able to plot stress-strain graphs from raw data and use them to compare materials.
5. **Experimental Design:** Students may be asked to design an experiment to determine which material is best for a given application, including control of variables and safety considerations.

**中文:**
本子知识点通过以下方式与实验工作联系：
1. **拉伸测试：** 学生可以对不同材料（如铜线、尼龙线、橡皮筋）进行拉伸测试以获得应力-应变数据。这直接提供了用于材料选择的曲线。
2. **数据分析：** 从应力-应变图中，学生必须提取：
   - 杨氏模量（弹性区的斜率）
   - 屈服强度（偏离线性）
   - 极限抗拉强度（峰值应力）
   - 断裂应力（最终点）
   - 韧性（曲线下面积——可能需要数方格或积分）
3. **不确定度：** 计算比属性时，学生必须传播来自力、伸长量和横截面积测量的不确定度。
4. **图表绘制：** 学生应能够从原始数据绘制应力-应变图，并用它们来比较材料。
5. **实验设计：** 学生可能被要求设计一个实验来确定哪种材料最适合给定的应用，包括变量控制和安全考虑。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core concept
    MS[Material Selection for Engineering Applications] --> SC[Selection Criteria]
    MS --> SF[Safety Factor]
    MS --> TO[Trade-offs]

    %% Selection Criteria
    SC --> ST[Stiffness - Young Modulus]
    SC --> STR[Strength - Yield/UTS]
    SC --> TOU[Toughness - Area under curve]
    SC --> DUC[Ductility - Strain at fracture]
    SC --> BRI[Brittleness]

    %% Safety Factor
    SF --> DEF[Definition: UTS / Working Stress]
    SF --> TYP[Typical Values: 1.5-12]
    SF --> APP[Applications: Bridges, Aircraft, Elevators]

    %% Trade-offs
    TO --> SW[Strength vs Weight]
    TO --> SD[Stiffness vs Ductility]
    TO --> CP[Cost vs Performance]
    TO --> TH[Hardness vs Toughness]

    %% Connections to other topics
    MS -->|Uses data from| SSG[Stress-Strain Graphs and Material Behaviour]
    MS -->|Requires knowledge of| YM[Stress, Strain and Young Modulus]
    MS -->|Compares| DUC_M[Stress-Strain Graph for a Ductile Material (Copper)]
    MS -->|Compares| BRI_M[Stress-Strain Graph for a Brittle Material (Glass)]
    MS -->|Compares| POL_M[Stress-Strain Graph for a Polymeric Material (Rubber)]
    MS -->|Involves| EP[Elastic and Plastic Regions]
    MS -->|Involves| NF[Necking and Fracture]

    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef sub fill:#bbf,stroke:#333,stroke-width:1px
    classDef link fill:#dfd,stroke:#333,stroke-width:1px
    class MS core
    class SC,SF,TO sub
    class ST,STR,TOU,DUC,BRI,DEF,TYP,APP,SW,SD,CP,TH link
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Material selection uses stress-strain data to choose materials for applications. Safety factor = UTS / working stress. |
| **Key Formula / 核心公式** | Safety Factor = $\frac{\sigma_{\text{UTS}}}{\sigma_{\text{working}}}$; Specific Strength = $\frac{\sigma_{\text{UTS}}}{\rho}$; Specific Stiffness = $\frac{E}{\rho}$ |
| **Key Graph / 核心图表** | Overlay of stress-strain curves for steel (ductile), glass (brittle), rubber (polymeric). Compare stiffness (gradient), strength (peak), toughness (area), ductility (strain). |
| **Key Properties / 关键属性** | Stiffness (E), Strength (yield/UTS), Toughness (area), Ductility (strain), Brittleness (no plastic region) |
| **Safety Factor / 安全系数** | Aircraft: 1.5-2.0; Bridges: 2.0-4.0; Elevators: 10-12. Higher factor = safer but heavier/more expensive. |
| **Trade-offs / 权衡** | Strength vs Weight (aerospace), Stiffness vs Ductility (ceramics vs polymers), Cost vs Performance (steel vs carbon fiber) |
| **Exam Tip / 考试提示** | Always justify material choices with quantitative data from stress-strain graphs. Use specific properties when weight is critical. Comment on safety factor appropriateness. |
| **Common Mistakes / 常见错误** | Confusing stiffness with strength; confusing toughness with strength; thinking higher safety factor is always better; ignoring cost in real-world applications. |