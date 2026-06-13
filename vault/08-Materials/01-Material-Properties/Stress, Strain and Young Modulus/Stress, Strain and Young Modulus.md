# 1. Overview / 概述

**English:**
This topic introduces the fundamental mechanical properties of materials under tensile (stretching) forces. **Stress** describes the internal resistance per unit area within a material when an external force is applied, while **Strain** quantifies the resulting fractional deformation. The **Young Modulus** is a material-specific constant that measures stiffness — the ratio of stress to strain within the elastic limit. Understanding these concepts is essential for predicting how materials behave under load, from bridge cables to dental braces. In both Cambridge 9702 and Edexcel IAL syllabuses, this topic forms the foundation for [[Stress-Strain Graphs and Material Behaviour]] and connects directly to [[Density, Hooke's Law and Springs]]. Real-world applications include selecting materials for aircraft wings, designing suspension bridges, and understanding why rubber bands stretch differently from steel wires. Examiners frequently test the experimental determination of Young Modulus, graph interpretation, and calculations involving [[Tensile Stress and Strain]].

**中文：**
本主题介绍材料在拉伸力作用下的基本力学性质。**应力**描述材料在外力作用下单位面积上的内部阻力，而**应变**量化由此产生的相对形变。**杨氏模量**是衡量材料刚度的材料特性常数——弹性极限内应力与应变的比值。理解这些概念对于预测材料在载荷下的行为至关重要，从桥梁缆索到牙套都适用。在剑桥9702和爱德思IAL考纲中，本主题构成[[应力-应变图与材料行为]]的基础，并直接联系到[[密度、胡克定律与弹簧]]。实际应用包括选择飞机机翼材料、设计悬索桥以及理解橡皮筋为何与钢丝拉伸方式不同。考官经常测试杨氏模量的实验测定、图表解读以及涉及[[拉伸应力与应变]]的计算。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (6.2 a-g) | Edexcel IAL (WPH11 U1: 2.7-2.12) |
|---------------------|----------------------------------|
| (a) Define and use stress, strain, and Young Modulus | 2.7 Define and use tensile stress and tensile strain |
| (b) Describe force-extension graphs for different materials | 2.8 Describe force-extension/compression graphs for ductile, brittle, and polymeric materials |
| (c) Describe stress-strain graphs for different materials | 2.9 Define and use Young Modulus |
| (d) Distinguish between elastic and plastic deformation | 2.10 Describe elastic and plastic behaviour |
| (e) Define and use elastic limit, limit of proportionality, yield point | 2.11 Define and use elastic limit, limit of proportionality, yield point, ultimate tensile stress |
| (f) Define and use ultimate tensile stress (UTS) | 2.12 Describe the behaviour of materials under tensile and compressive forces |
| (g) Describe the behaviour of materials under tensile and compressive forces | — |

**Examiner Expectations / 考官期望:**

**English:**
- Candidates must use correct SI units: stress in Pa (or N m⁻²), strain dimensionless, Young Modulus in Pa.
- Definitions must be precise: "stress = force per unit cross-sectional area" not "force over area".
- Graph interpretation is critical — identify key points (limit of proportionality, elastic limit, yield point, UTS) on stress-strain curves.
- Experimental methods (e.g., Searle's apparatus, wire stretching) are frequently tested in Paper 3/5 (CAIE) and Unit 3/6 (Edexcel).
- Calculations must show working with correct significant figures.

**中文：**
- 考生必须使用正确的SI单位：应力用Pa（或N m⁻²），应变无量纲，杨氏模量用Pa。
- 定义必须精确："应力 = 单位横截面积上的力"，而非"力除以面积"。
- 图表解读至关重要——在应力-应变曲线上识别关键点（比例极限、弹性极限、屈服点、极限抗拉强度）。
- 实验方法（如Searle装置、金属丝拉伸）在Paper 3/5（CAIE）和Unit 3/6（Edexcel）中经常考查。
- 计算必须展示过程，并保留正确的有效数字。

> 📋 **CIE Only:** CAIE specifically requires describing force-extension graphs (6.2b) and stress-strain graphs (6.2c) for different materials including ductile, brittle, and polymeric materials. The distinction between elastic and plastic deformation (6.2d) is explicitly tested.
>
> 📋 **Edexcel Only:** Edexcel explicitly includes compression graphs (2.8) and requires defining ultimate tensile stress (2.11). The behaviour under compressive forces (2.12) is a separate objective.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Stress** / 应力 | The force applied per unit cross-sectional area of a material, given by $\sigma = \frac{F}{A}$ | 材料单位横截面积上所承受的力，公式为 $\sigma = \frac{F}{A}$ | Using diameter instead of radius in area calculation; confusing stress with force |
| **Strain** / 应变 | The ratio of extension (change in length) to original length, given by $\varepsilon = \frac{\Delta L}{L_0}$ | 伸长量（长度变化）与原始长度的比值，公式为 $\varepsilon = \frac{\Delta L}{L_0}$ | Forgetting strain is dimensionless; using final length instead of extension |
| **Young Modulus** / 杨氏模量 | The ratio of tensile stress to tensile strain within the elastic limit, given by $E = \frac{\sigma}{\varepsilon} = \frac{FL_0}{A\Delta L}$ | 弹性极限内拉伸应力与拉伸应变的比值，公式为 $E = \frac{\sigma}{\varepsilon} = \frac{FL_0}{A\Delta L}$ | Confusing with stiffness (spring constant); using force-extension gradient directly |
| **Elastic Limit** / 弹性极限 | The maximum stress a material can withstand without permanent (plastic) deformation | 材料能承受而不发生永久（塑性）变形的最大应力 | Confusing with limit of proportionality |
| **Limit of Proportionality** / 比例极限 | The maximum stress at which stress is directly proportional to strain (Hooke's law holds) | 应力与应变成正比（胡克定律成立）的最大应力 | Assuming elastic limit and limit of proportionality are always the same point |
| **Yield Point** / 屈服点 | The stress at which a material begins to deform plastically without a significant increase in load | 材料在载荷无明显增加的情况下开始发生塑性变形的应力点 | Confusing with UTS; thinking all materials have a clear yield point |
| **Ultimate Tensile Stress (UTS)** / 极限抗拉强度 | The maximum stress a material can withstand before fracture | 材料在断裂前能承受的最大应力 | Confusing with breaking stress; thinking UTS is the stress at fracture |
| **Breaking Stress** / 断裂应力 | The stress at which a material actually fractures | 材料实际断裂时的应力 | Confusing with UTS (UTS is higher than breaking stress for ductile materials) |
| **Elastic Deformation** / 弹性形变 | Deformation that is reversible — the material returns to its original shape when the load is removed | 可逆的形变——卸载后材料恢复原始形状 | Thinking all deformation is elastic until fracture |
| **Plastic Deformation** / 塑性形变 | Permanent deformation that remains after the load is removed | 卸载后仍然存在的永久形变 | Confusing with elastic deformation; not understanding it occurs beyond elastic limit |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Stress / 应力

### Explanation / 解释
**English:**
Stress ($\sigma$) is defined as the force applied per unit cross-sectional area. It is a measure of the internal forces within a material that resist deformation. For a wire under tension, stress is calculated using the original cross-sectional area (engineering stress), not the reduced area after stretching. Stress has units of pascals (Pa) or N m⁻². The symbol $\sigma$ (sigma) is standard. Stress is a scalar quantity in this context, though it has directional components in more advanced treatments. Understanding stress is essential for [[Tensile Stress and Strain]] calculations and connects to [[Density, Hooke's Law and Springs]] through the concept of restoring forces.

**中文：**
应力（$\sigma$）定义为施加在单位横截面积上的力。它是衡量材料内部抵抗形变的力的指标。对于受拉伸的金属丝，应力使用原始横截面积（工程应力）计算，而非拉伸后的减小面积。应力的单位为帕斯卡（Pa）或N m⁻²。符号$\sigma$（西格玛）为标准符号。在此上下文中，应力是标量，尽管在更高级的处理中具有方向分量。理解应力对于[[拉伸应力与应变]]计算至关重要，并通过恢复力的概念与[[密度、胡克定律与弹簧]]相联系。

### Physical Meaning / 物理意义
**English:**
Stress tells us how "intensely" a force is applied. A 100 N force on a thin wire creates much higher stress than the same force on a thick rod. This explains why thin wires snap more easily — the stress is higher for the same force. In real life, high heels create high stress on floors (damaging wooden floors), while flat shoes distribute the force over a larger area, reducing stress.

**中文：**
应力告诉我们力施加的"强度"。一根细金属丝上施加100 N的力比同样力施加在粗棒上产生的应力大得多。这解释了为什么细金属丝更容易断裂——相同力下应力更高。在现实生活中，高跟鞋在地板上产生高应力（损坏木地板），而平底鞋将力分布在更大面积上，降低应力。

### Common Misconceptions / 常见误区
1. **Confusing stress with force:** Stress is force per area, not force alone. A small force on a tiny area can produce enormous stress.
2. **Using wrong area:** For a wire, use cross-sectional area ($\pi r^2$), not surface area.
3. **Ignoring units:** Stress is in Pa, not N. Always convert mm² to m² ($1 \text{ mm}^2 = 10^{-6} \text{ m}^2$).
4. **Assuming stress is constant:** Stress varies if the cross-sectional area changes along the material.

### Exam Tips / 考试提示
**English:**
- Always show the formula $\sigma = F/A$ before substituting numbers.
- Convert all areas to m² before calculation.
- For wires, remember $A = \pi r^2 = \pi (d/2)^2$ where $d$ is diameter.
- CAIE often gives diameter in mm — convert to m first.

**中文：**
- 代入数字前始终写出公式 $\sigma = F/A$。
- 计算前将所有面积转换为m²。
- 对于金属丝，记住 $A = \pi r^2 = \pi (d/2)^2$，其中$d$为直径。
- CAIE常给出直径单位为mm——先转换为m。

---

## 4.2 Strain / 应变

### Explanation / 解释
**English:**
Strain ($\varepsilon$) is the ratio of the change in length ($\Delta L$) to the original length ($L_0$). It is dimensionless — it has no units. Strain is often expressed as a percentage or in decimal form. For a wire stretched from 2.000 m to 2.004 m, the strain is $\varepsilon = \frac{0.004}{2.000} = 0.002$ or 0.2%. Strain is a measure of relative deformation, not absolute extension. This makes it useful for comparing materials of different sizes. Strain connects directly to [[Tensile Stress and Strain]] and is used in the [[Young Modulus Definition and Formula]].

**中文：**
应变（$\varepsilon$）是长度变化量（$\Delta L$）与原始长度（$L_0$）的比值。它是无量纲的——没有单位。应变通常以百分比或小数形式表示。对于从2.000 m拉伸到2.004 m的金属丝，应变为 $\varepsilon = \frac{0.004}{2.000} = 0.002$ 或0.2%。应变是相对形变的度量，而非绝对伸长量。这使得它适用于比较不同尺寸的材料。应变直接联系到[[拉伸应力与应变]]，并用于[[杨氏模量定义与公式]]。

### Physical Meaning / 物理意义
**English:**
Strain tells us how much a material deforms relative to its original size. A strain of 0.001 means the material has stretched by 0.1% of its original length. Rubber bands can have strains of several hundred percent before breaking, while steel typically fractures at strains less than 1%. Strain is a normalized measure — a 1 m rod stretching 1 mm has the same strain as a 10 m rod stretching 10 mm.

**中文：**
应变告诉我们材料相对于其原始尺寸形变了多少。应变为0.001意味着材料拉伸了原始长度的0.1%。橡皮筋在断裂前可以达到百分之几百的应变，而钢通常在小于1%的应变下断裂。应变是一种归一化度量——1 m的棒伸长1 mm与10 m的棒伸长10 mm具有相同的应变。

### Common Misconceptions / 常见误区
1. **Giving strain units:** Strain is dimensionless — do not write "m" or "mm".
2. **Using final length instead of extension:** $\varepsilon = \Delta L / L_0$, not $L_{final} / L_0$.
3. **Confusing strain with extension:** Extension is absolute ($\Delta L$), strain is relative ($\Delta L / L_0$).
4. **Forgetting original length:** Always use the unstretched original length.

### Exam Tips / 考试提示
**English:**
- Strain is always a small number for most materials (except elastomers).
- If asked for percentage strain, multiply by 100%.
- In calculations, keep strain as a decimal (e.g., 0.002) not a fraction.
- Edexcel often asks for strain in graph questions — read values carefully from axes.

**中文：**
- 对于大多数材料（弹性体除外），应变总是小数字。
- 如果要求百分比应变，乘以100%。
- 计算中，应变保留为小数（如0.002）而非分数。
- 爱德思常在图表题中要求应变——仔细从坐标轴读取数值。

---

## 4.3 Young Modulus / 杨氏模量

### Explanation / 解释
**English:**
The Young Modulus ($E$) is a material property that measures stiffness — how resistant a material is to stretching. It is defined as the ratio of tensile stress to tensile strain within the elastic limit: $E = \frac{\sigma}{\varepsilon} = \frac{F/A}{\Delta L / L_0} = \frac{FL_0}{A\Delta L}$. The Young Modulus has the same units as stress (Pa or N m⁻²) because strain is dimensionless. A high Young Modulus means the material is stiff (e.g., steel ~200 GPa), while a low Young Modulus means it is flexible (e.g., rubber ~0.01 GPa). The Young Modulus is temperature-dependent and is only valid within the elastic region. This concept is central to [[Young Modulus Definition and Formula]] and is experimentally determined in [[Experimental Determination of Young Modulus]].

**中文：**
杨氏模量（$E$）是衡量刚度的材料属性——材料抵抗拉伸的能力。它定义为弹性极限内拉伸应力与拉伸应变的比值：$E = \frac{\sigma}{\varepsilon} = \frac{F/A}{\Delta L / L_0} = \frac{FL_0}{A\Delta L}$。杨氏模量与应力具有相同单位（Pa或N m⁻²），因为应变无量纲。高杨氏模量意味着材料刚度大（如钢约200 GPa），低杨氏模量意味着材料柔韧（如橡胶约0.01 GPa）。杨氏模量具有温度依赖性，且仅在弹性区域内有效。这个概念是[[杨氏模量定义与公式]]的核心，并通过[[杨氏模量的实验测定]]进行实验确定。

### Physical Meaning / 物理意义
**English:**
The Young Modulus tells us how much a material stretches under a given stress. A material with a high Young Modulus (like diamond ~1200 GPa) barely stretches at all, while a material with a low Young Modulus (like rubber) stretches easily. This is why steel is used for structural beams and rubber for elastic bands. The Young Modulus is an intrinsic property — it does not depend on the size or shape of the sample, only on the material itself.

**中文：**
杨氏模量告诉我们材料在给定应力下拉伸多少。高杨氏模量的材料（如钻石约1200 GPa）几乎不拉伸，而低杨氏模量的材料（如橡胶）容易拉伸。这就是为什么钢用于结构梁，橡胶用于橡皮筋。杨氏模量是固有属性——它不依赖于样品的尺寸或形状，只取决于材料本身。

### Common Misconceptions / 常见误区
1. **Confusing Young Modulus with stiffness:** Stiffness ($k = F/\Delta L$) depends on dimensions; Young Modulus is material-specific.
2. **Using force-extension gradient directly:** The gradient of a force-extension graph is $k$, not $E$. You must multiply by $L_0/A$ to get $E$.
3. **Applying beyond elastic limit:** Young Modulus is only defined within the elastic region.
4. **Assuming constant for all temperatures:** Young Modulus decreases with increasing temperature for most materials.

### Exam Tips / 考试提示
**English:**
- Remember the three forms: $E = \sigma/\varepsilon = FL_0/(A\Delta L) = (F/\Delta L)(L_0/A)$.
- For graph questions: gradient of stress-strain graph = Young Modulus (within elastic limit).
- CAIE often asks to calculate $E$ from experimental data — check units carefully.
- Edexcel may ask to compare Young Moduli of different materials from graph gradients.

**中文：**
- 记住三种形式：$E = \sigma/\varepsilon = FL_0/(A\Delta L) = (F/\Delta L)(L_0/A)$。
- 对于图表题：应力-应变图的斜率 = 杨氏模量（弹性极限内）。
- CAIE常要求从实验数据计算$E$——仔细检查单位。
- 爱德思可能要求从图表斜率比较不同材料的杨氏模量。

---

## 4.4 Elastic and Plastic Deformation / 弹性形变与塑性形变

### Explanation / 解释
**English:**
**Elastic deformation** is reversible — when the load is removed, the material returns to its original shape and size. This occurs because atoms are displaced from their equilibrium positions but return when the force is removed. **Plastic deformation** is permanent — the material does not return to its original shape when the load is removed. This occurs because atoms slide past each other (dislocation motion) and do not return to their original positions. The transition from elastic to plastic behaviour occurs at the **elastic limit**. For ductile materials like copper, significant plastic deformation occurs before fracture. For brittle materials like glass, there is very little plastic deformation before fracture. This distinction is crucial for [[Stress-Strain Graphs and Material Behaviour]].

**中文：**
**弹性形变**是可逆的——卸载后，材料恢复原始形状和尺寸。这是因为原子从平衡位置位移，但力移除后返回。**塑性形变**是永久的——卸载后材料不恢复原始形状。这是因为原子彼此滑过（位错运动）且不返回原始位置。从弹性到塑性行为的转变发生在**弹性极限**处。对于铜等延性材料，断裂前发生显著的塑性形变。对于玻璃等脆性材料，断裂前几乎没有塑性形变。这种区别对于[[应力-应变图与材料行为]]至关重要。

### Physical Meaning / 物理意义
**English:**
Think of a paperclip: bending it slightly (elastic) allows it to spring back, but bending it too far (plastic) leaves it permanently bent. Elastic deformation is like stretching a spring within its limit — it returns. Plastic deformation is like bending a spoon — it stays bent. Engineers must design structures to operate within the elastic region to avoid permanent damage.

**中文：**
想想回形针：轻微弯曲（弹性）可以弹回，但过度弯曲（塑性）会永久弯曲。弹性形变就像在极限内拉伸弹簧——它会恢复。塑性形变就像弯曲勺子——它会保持弯曲。工程师必须设计结构在弹性区域内运行以避免永久损坏。

### Common Misconceptions / 常见误区
1. **Thinking all materials have clear elastic limits:** Some materials (like polymers) show gradual transition.
2. **Confusing elastic limit with limit of proportionality:** They are often close but not identical.
3. **Believing elastic deformation is always linear:** Elastic deformation can be non-linear (e.g., rubber).
4. **Assuming plastic deformation means immediate failure:** Ductile materials can undergo significant plastic deformation before fracture.

### Exam Tips / 考试提示
**English:**
- Be able to identify elastic and plastic regions on a stress-strain graph.
- Know that the area under the elastic region represents elastic strain energy.
- CAIE often asks to explain the difference using atomic/molecular models.
- Edexcel may ask to describe the behaviour of specific materials (ductile, brittle, polymeric).

**中文：**
- 能够在应力-应变图上识别弹性和塑性区域。
- 知道弹性区域下的面积代表弹性应变能。
- CAIE常要求使用原子/分子模型解释差异。
- 爱德思可能要求描述特定材料（延性、脆性、聚合物）的行为。

---

## 4.5 Ultimate Tensile Stress and Breaking Stress / 极限抗拉强度与断裂应力

### Explanation / 解释
**English:**
**Ultimate Tensile Stress (UTS)** is the maximum stress a material can withstand before it begins to fail. On a stress-strain graph, this is the highest point on the curve. **Breaking Stress** (or fracture stress) is the stress at which the material actually breaks. For ductile materials, the breaking stress is lower than the UTS because necking (local reduction in cross-sectional area) occurs after the UTS, causing the material to weaken. For brittle materials, the UTS and breaking stress are essentially the same because there is no plastic deformation. These concepts are explored in [[Ultimate Tensile Strength]] and [[Breaking Stress]].

**中文：**
**极限抗拉强度（UTS）**是材料在开始失效前能承受的最大应力。在应力-应变图上，这是曲线上的最高点。**断裂应力**是材料实际断裂时的应力。对于延性材料，断裂应力低于UTS，因为UTS后发生颈缩（横截面积局部减小），导致材料弱化。对于脆性材料，UTS和断裂应力基本相同，因为没有塑性形变。这些概念在[[极限抗拉强度]]和[[断裂应力]]中探讨。

### Physical Meaning / 物理意义
**English:**
UTS tells engineers the maximum load a material can handle. For example, a steel cable with UTS of 500 MPa and cross-sectional area of 1 cm² can support a maximum force of 50,000 N (about 5 tonnes). Safety factors are always applied — structures are designed to operate well below the UTS. Breaking stress is the point of actual failure — the stress at which the material separates.

**中文：**
UTS告诉工程师材料能承受的最大载荷。例如，UTS为500 MPa、横截面积为1 cm²的钢缆可支撑最大50,000 N（约5吨）的力。始终应用安全系数——结构设计在远低于UTS的条件下运行。断裂应力是实际失效点——材料分离时的应力。

### Common Misconceptions / 常见误区
1. **Confusing UTS with breaking stress:** For ductile materials, UTS > breaking stress.
2. **Thinking UTS is the stress at fracture:** UTS is the maximum stress, which occurs before fracture for ductile materials.
3. **Assuming UTS is constant for all samples of the same material:** UTS is material-specific but can vary with temperature, impurities, and manufacturing process.
4. **Ignoring necking:** Necking reduces the cross-sectional area, so the engineering stress (using original area) decreases after UTS.

### Exam Tips / 考试提示
**English:**
- On a stress-strain graph, UTS is the peak of the curve.
- Breaking stress is where the curve ends (fracture point).
- CAIE may ask to label UTS and breaking stress on a graph.
- Edexcel may ask to compare UTS values for different materials.

**中文：**
- 在应力-应变图上，UTS是曲线的峰值。
- 断裂应力是曲线结束处（断裂点）。
- CAIE可能要求在图上标注UTS和断裂应力。
- 爱德思可能要求比较不同材料的UTS值。

---

## 4.6 Force-Extension vs Stress-Strain Graphs / 力-伸长图与应力-应变图对比

### Explanation / 解释
**English:**
**Force-extension graphs** show the actual force applied versus the actual extension of a specific sample. The gradient gives the stiffness ($k = F/\Delta L$), which depends on the material's dimensions. **Stress-strain graphs** normalize for sample dimensions — stress uses cross-sectional area, strain uses original length. The gradient of the linear region gives the Young Modulus ($E$), which is material-specific and independent of sample dimensions. Force-extension graphs are useful for practical experiments, while stress-strain graphs allow comparison between different materials. This distinction is critical for [[Stress-Strain Graphs and Material Behaviour]].

**中文：**
**力-伸长图**显示施加的实际力与特定样品的实际伸长量。斜率给出刚度（$k = F/\Delta L$），取决于材料尺寸。**应力-应变图**对样品尺寸进行归一化——应力使用横截面积，应变使用原始长度。线性区域的斜率给出杨氏模量（$E$），这是材料特有的，与样品尺寸无关。力-伸长图对实际实验有用，而应力-应变图允许比较不同材料。这种区别对于[[应力-应变图与材料行为]]至关重要。

### Physical Meaning / 物理意义
**English:**
If you test two steel wires of different lengths and thicknesses, their force-extension graphs will be different (different stiffness). But their stress-strain graphs will be identical (same Young Modulus). This is why stress-strain graphs are used in material science — they reveal the intrinsic properties of the material, not the sample.

**中文：**
如果你测试两根不同长度和粗细的钢丝，它们的力-伸长图会不同（不同刚度）。但它们的应力-应变图会相同（相同杨氏模量）。这就是为什么材料科学中使用应力-应变图——它们揭示材料的固有属性，而非样品的属性。

### Common Misconceptions / 常见误区
1. **Confusing stiffness with Young Modulus:** Stiffness ($k$) depends on dimensions; Young Modulus ($E$) does not.
2. **Thinking force-extension gradient = Young Modulus:** You must multiply by $L_0/A$ to convert.
3. **Assuming stress-strain graphs are always linear:** Only within the elastic limit for many materials.
4. **Forgetting to normalize:** Always use stress and strain when comparing materials.

### Exam Tips / 考试提示
**English:**
- Know how to convert between force-extension and stress-strain data.
- CAIE often asks to calculate Young Modulus from a force-extension graph.
- Edexcel may ask to sketch both types of graphs for the same material.
- Remember: gradient of stress-strain graph = $E$; gradient of force-extension graph = $k$.

**中文：**
- 知道如何在力-伸长数据和应力-应变数据之间转换。
- CAIE常要求从力-伸长图计算杨氏模量。
- 爱德思可能要求为同一材料绘制两种类型的图。
- 记住：应力-应变图斜率 = $E$；力-伸长图斜率 = $k$。

---

# 5. Essential Equations / 核心公式

## 5.1 Stress / 应力

**Equation / 公式:**
$$ \sigma = \frac{F}{A} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\sigma$ | Stress | 应力 | Pa (N m⁻²) |
| $F$ | Force applied perpendicular to cross-section | 垂直于横截面施加的力 | N |
| $A$ | Cross-sectional area (original) | 横截面积（原始） | m² |

**Derivation / 推导:**
**English:** Stress is defined as force per unit area. It is a direct definition, not derived from other equations. The concept comes from the need to compare forces on objects of different sizes.

**中文：** 应力定义为力除以单位面积。这是一个直接定义，而非从其他方程推导而来。这个概念源于比较不同大小物体上力的需要。

**Conditions / 适用条件:**
**English:** Force must be perpendicular to the cross-sectional area. For tensile stress, the force pulls the material apart. For compressive stress, the force pushes the material together.

**中文：** 力必须垂直于横截面积。对于拉伸应力，力将材料拉开。对于压缩应力，力将材料压在一起。

**Limitations / 局限性:**
**English:** Engineering stress (using original area) becomes inaccurate at large strains because the cross-sectional area changes. True stress (using instantaneous area) is more accurate but not required at A-Level.

**中文：** 工程应力（使用原始面积）在大应变下变得不准确，因为横截面积发生变化。真应力（使用瞬时面积）更准确，但A-Level不要求。

**Rearrangements / 变形:**
$$ F = \sigma A $$
$$ A = \frac{F}{\sigma} $$

---

## 5.2 Strain / 应变

**Equation / 公式:**
$$ \varepsilon = \frac{\Delta L}{L_0} = \frac{L - L_0}{L_0} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\varepsilon$ | Strain | 应变 | Dimensionless (无量纲) |
| $\Delta L$ | Extension (change in length) | 伸长量（长度变化） | m |
| $L_0$ | Original (unstretched) length | 原始（未拉伸）长度 | m |
| $L$ | Final length | 最终长度 | m |

**Derivation / 推导:**
**English:** Strain is defined as the ratio of extension to original length. It is a direct definition. The extension $\Delta L = L - L_0$ where $L$ is the final length after stretching.

**中文：** 应变定义为伸长量与原始长度的比值。这是一个直接定义。伸长量 $\Delta L = L - L_0$，其中$L$是拉伸后的最终长度。

**Conditions / 适用条件:**
**English:** The original length $L_0$ must be measured when the material is unstretched (no load applied). For very small strains, the difference between engineering and true strain is negligible.

**中文：** 原始长度$L_0$必须在材料未拉伸（无载荷）时测量。对于非常小的应变，工程应变与真应变之间的差异可忽略。

**Limitations / 局限性:**
**English:** Engineering strain (using original length) is only accurate for small strains (< 1%). For large strains (e.g., rubber), true strain ($\ln(L/L_0)$) is more appropriate but not required at A-Level.

**中文：** 工程应变（使用原始长度）仅对小应变（< 1%）准确。对于大应变（如橡胶），真应变（$\ln(L/L_0)$）更合适，但A-Level不要求。

**Rearrangements / 变形:**
$$ \Delta L = \varepsilon L_0 $$
$$ L_0 = \frac{\Delta L}{\varepsilon} $$
$$ L = L_0(1 + \varepsilon) $$

---

## 5.3 Young Modulus / 杨氏模量

**Equation / 公式:**
$$ E = \frac{\sigma}{\varepsilon} = \frac{F/A}{\Delta L / L_0} = \frac{FL_0}{A\Delta L} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Young Modulus | 杨氏模量 | Pa (N m⁻²) |
| $\sigma$ | Tensile stress | 拉伸应力 | Pa |
| $\varepsilon$ | Tensile strain | 拉伸应变 | Dimensionless |
| $F$ | Force | 力 | N |
| $A$ | Cross-sectional area | 横截面积 | m² |
| $L_0$ | Original length | 原始长度 | m |
| $\Delta L$ | Extension | 伸长量 | m |

**Derivation / 推导:**
**English:**
The Young Modulus is defined as the ratio of tensile stress to tensile strain within the elastic limit.

Starting from:
$$ \sigma = \frac{F}{A} \quad \text{and} \quad \varepsilon = \frac{\Delta L}{L_0} $$

By definition:
$$ E = \frac{\sigma}{\varepsilon} = \frac{F/A}{\Delta L / L_0} = \frac{F}{A} \times \frac{L_0}{\Delta L} = \frac{FL_0}{A\Delta L} $$

**中文：**
杨氏模量定义为弹性极限内拉伸应力与拉伸应变的比值。

从以下公式开始：
$$ \sigma = \frac{F}{A} \quad \text{和} \quad \varepsilon = \frac{\Delta L}{L_0} $$

根据定义：
$$ E = \frac{\sigma}{\varepsilon} = \frac{F/A}{\Delta L / L_0} = \frac{F}{A} \times \frac{L_0}{\Delta L} = \frac{FL_0}{A\Delta L} $$

**Conditions / 适用条件:**
**English:**
- Material must be within its elastic limit (no permanent deformation).
- Stress must be tensile (stretching) — compressive Young Modulus can be different.
- Material must be homogeneous and isotropic (same properties in all directions).
- Temperature must be constant.

**中文：**
- 材料必须在弹性极限内（无永久形变）。
- 应力必须是拉伸的（伸长）——压缩杨氏模量可能不同。
- 材料必须均匀且各向同性（所有方向性质相同）。
- 温度必须恒定。

**Limitations / 局限性:**
**English:**
- Not valid beyond the elastic limit (plastic deformation region).
- Does not apply to non-linear elastic materials (e.g., rubber) in the same way.
- Assumes uniform cross-sectional area (not valid after necking).
- Temperature-dependent — values change with temperature.

**中文：**
- 超出弹性极限（塑性形变区域）无效。
- 不适用于非线性弹性材料（如橡胶）。
- 假设横截面积均匀（颈缩后无效）。
- 温度依赖性——数值随温度变化。

**Rearrangements / 变形:**
$$ F = \frac{EA\Delta L}{L_0} $$
$$ \Delta L = \frac{FL_0}{EA} $$
$$ A = \frac{FL_0}{E\Delta L} $$
$$ L_0 = \frac{EA\Delta L}{F} $$

---

## 5.4 Stiffness (Spring Constant) / 刚度（弹簧常数）

**Equation / 公式:**
$$ k = \frac{F}{\Delta L} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $k$ | Stiffness (spring constant) | 刚度（弹簧常数） | N m⁻¹ |
| $F$ | Force | 力 | N |
| $\Delta L$ | Extension | 伸长量 | m |

**Derivation / 推导:**
**English:**
Stiffness is defined from Hooke's Law: $F = k\Delta L$. It is the force required per unit extension. For a wire, stiffness is related to Young Modulus by:
$$ k = \frac{F}{\Delta L} = \frac{EA}{L_0} $$
This shows that stiffness depends on both material properties ($E$) and dimensions ($A$ and $L_0$).

**中文：**
刚度由胡克定律定义：$F = k\Delta L$。它是单位伸长所需的力。对于金属丝，刚度与杨氏模量的关系为：
$$ k = \frac{F}{\Delta L} = \frac{EA}{L_0} $$
这表明刚度取决于材料属性（$E$）和尺寸（$A$和$L_0$）。

**Conditions / 适用条件:**
**English:**
- Only valid within the elastic limit (Hooke's law region).
- For a specific sample, not a material property.

**中文：**
- 仅在弹性极限内有效（胡克定律区域）。
- 针对特定样品，非材料属性。

**Limitations / 局限性:**
**English:**
- Not a material constant — changes with sample dimensions.
- Only valid for linear elastic behaviour.

**中文：**
- 非材料常数——随样品尺寸变化。
- 仅对线性弹性行为有效。

**Rearrangements / 变形:**
$$ F = k\Delta L $$
$$ \Delta L = \frac{F}{k} $$

---

## 5.5 Relationship between Young Modulus and Stiffness / 杨氏模量与刚度的关系

**Equation / 公式:**
$$ E = \frac{kL_0}{A} $$
$$ k = \frac{EA}{L_0} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Young Modulus | 杨氏模量 | Pa |
| $k$ | Stiffness | 刚度 | N m⁻¹ |
| $L_0$ | Original length | 原始长度 | m |
| $A$ | Cross-sectional area | 横截面积 | m² |

**Derivation / 推导:**
**English:**
Starting from $E = \frac{FL_0}{A\Delta L}$ and $k = \frac{F}{\Delta L}$:
$$ E = \frac{FL_0}{A\Delta L} = \frac{L_0}{A} \times \frac{F}{\Delta L} = \frac{kL_0}{A} $$
Therefore:
$$ k = \frac{EA}{L_0} $$

**中文：**
从 $E = \frac{FL_0}{A\Delta L}$ 和 $k = \frac{F}{\Delta L}$ 开始：
$$ E = \frac{FL_0}{A\Delta L} = \frac{L_0}{A} \times \frac{F}{\Delta L} = \frac{kL_0}{A} $$
因此：
$$ k = \frac{EA}{L_0} $$

**Conditions / 适用条件:**
**English:**
- Valid only within the elastic limit.
- Assumes uniform cross-sectional area.

**中文：**
- 仅在弹性极限内有效。
- 假设横截面积均匀。

**Limitations / 局限性:**
**English:**
- $k$ depends on sample dimensions; $E$ does not.
- This relationship breaks down if the material is not homogeneous.

**中文：**
- $k$取决于样品尺寸；$E$不依赖。
- 如果材料不均匀，此关系不成立。

**Rearrangements / 变形:**
$$ L_0 = \frac{EA}{k} $$
$$ A = \frac{kL_0}{E} $$

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Force-Extension Graph / 力-伸长图

### Axes / 坐标轴
**English:** x-axis: Extension ($\Delta L$ / m); y-axis: Force ($F$ / N)
**中文：** x轴：伸长量（$\Delta L$ / m）；y轴：力（$F$ / N）

### Shape / 形状
**English:** Initially a straight line through the origin (Hooke's law region), then curves as the material approaches elastic limit. For ductile materials, the curve may plateau (yield) before rising again and eventually dropping after UTS.
**中文：** 初始为通过原点的直线（胡克定律区域），然后随材料接近弹性极限而弯曲。对于延性材料，曲线可能先出现平台（屈服），然后再次上升，最终在UTS后下降。

### Gradient Meaning / 斜率含义
**English:** Gradient = $\frac{F}{\Delta L} = k$ (stiffness or spring constant). A steeper gradient means a stiffer sample.
**中文：** 斜率 = $\frac{F}{\Delta L} = k$（刚度或弹簧常数）。斜率越陡，样品越硬。

### Area Meaning / 面积含义
**English:** Area under the graph = work done = elastic strain energy (within elastic limit). Units: J (joules).
**中文：** 图下面积 = 做功 = 弹性应变能（弹性极限内）。单位：J（焦耳）。

### Exam Interpretation / 考试解读
**English:**
- Identify the linear region (Hooke's law obeyed).
- Identify the limit of proportionality (end of linear region).
- Identify the elastic limit (where permanent deformation begins).
- For a wire, the graph is linear initially, then curves.
- CAIE often asks to calculate $k$ from the gradient.
- Edexcel may ask to compare graphs for different materials.

**中文：**
- 识别线性区域（胡克定律成立）。
- 识别比例极限（线性区域结束）。
- 识别弹性极限（永久形变开始处）。
- 对于金属丝，图形初始为线性，然后弯曲。
- CAIE常要求从斜率计算$k$。
- 爱德思可能要求比较不同材料的图形。

### Common Questions / 常见问题
**English:**
1. Calculate the spring constant from the gradient.
2. Calculate the work done from the area under the graph.
3. Determine the limit of proportionality from the graph.
4. Explain why the graph deviates from linearity.

**中文：**
1. 从斜率计算弹簧常数。
2. 从图下面积计算做功。
3. 从图形确定比例极限。
4. 解释图形为何偏离线性。

> 📷 **IMAGE PROMPT — GRAPH-01: Force-Extension Graph for a Ductile Metal Wire**
>
> A clear graph with Force (N) on y-axis and Extension (m) on x-axis. Show a straight line from origin (Hooke's law region), then a gradual curve (non-linear elastic), then a plateau (yield point), then rising again (work hardening), then a peak (UTS), then dropping to fracture point. Label all key points. Use gridlines. Professional scientific graph style.

---

## 6.2 Stress-Strain Graph / 应力-应变图

### Axes / 坐标轴
**English:** x-axis: Strain ($\varepsilon$, dimensionless); y-axis: Stress ($\sigma$ / Pa)
**中文：** x轴：应变（$\varepsilon$，无量纲）；y轴：应力（$\sigma$ / Pa）

### Shape / 形状
**English:** Similar shape to force-extension but normalized. Linear region (Hooke's law), then non-linear elastic, yield point, work hardening, UTS (peak), then necking and fracture. Shape varies significantly for different material types (ductile, brittle, polymeric).
**中文：** 形状与力-伸长图相似但已归一化。线性区域（胡克定律），然后非线性弹性、屈服点、加工硬化、UTS（峰值），然后颈缩和断裂。不同材料类型（延性、脆性、聚合物）的形状差异显著。

### Gradient Meaning / 斜率含义
**English:** Gradient of linear region = $\frac{\sigma}{\varepsilon} = E$ (Young Modulus). A steeper gradient means a stiffer material.
**中文：** 线性区域斜率 = $\frac{\sigma}{\varepsilon} = E$（杨氏模量）。斜率越陡，材料越硬。

### Area Meaning / 面积含义
**English:** Area under the graph = energy per unit volume (strain energy density). Units: J m⁻³.
**中文：** 图下面积 = 单位体积能量（应变能密度）。单位：J m⁻³。

### Exam Interpretation / 考试解读
**English:**
- Gradient gives Young Modulus directly (unlike force-extension).
- UTS is the maximum stress (peak of curve).
- Breaking stress is where the curve ends.
- Area under curve = toughness (energy absorbed before fracture).
- Compare materials: steel (high $E$, high UTS), copper (lower $E$, ductile), glass (high $E$, brittle, no plastic region).

**中文：**
- 斜率直接给出杨氏模量（与力-伸长图不同）。
- UTS是最大应力（曲线峰值）。
- 断裂应力是曲线结束处。
- 曲线下面积 = 韧性（断裂前吸收的能量）。
- 比较材料：钢（高$E$，高UTS）、铜（较低$E$，延性）、玻璃（高$E$，脆性，无塑性区域）。

### Common Questions / 常见问题
**English:**
1. Calculate Young Modulus from the gradient.
2. Determine UTS from the graph.
3. Compare ductility of different materials.
4. Explain why the graph shape differs for brittle vs ductile materials.

**中文：**
1. 从斜率计算杨氏模量。
2. 从图形确定UTS。
3. 比较不同材料的延性。
4. 解释为何脆性材料与延性材料的图形形状不同。

> 📷 **IMAGE PROMPT — GRAPH-02: Stress-Strain Graphs for Different Materials**
>
> Three overlaid stress-strain curves on the same axes: (1) Mild steel — linear, yield plateau, work hardening, UTS, necking; (2) Glass — straight line to sudden fracture, no plastic region; (3) Copper — linear, gradual curve, no clear yield point, UTS, necking. Label axes (Stress/Pa, Strain), label key points (elastic limit, UTS, fracture). Use different colors for each material. Professional scientific graph style.

---

## 6.3 Force-Extension Graph for Different Materials / 不同材料的力-伸长图

### Axes / 坐标轴
**English:** x-axis: Extension ($\Delta L$); y-axis: Force ($F$)
**中文：** x轴：伸长量（$\Delta L$）；y轴：力（$F$）

### Shape / 形状
**English:**
- **Ductile (e.g., copper):** Linear, then curve, yield, work hardening, UTS, necking, fracture.
- **Brittle (e.g., glass):** Linear to sudden fracture — very little extension.
- **Polymeric (e.g., rubber):** Non-linear from start — "J-shaped" curve, very large extension before fracture.
- **Elastomeric (e.g., rubber band):** Hysteresis — different loading and unloading paths.

**中文：**
- **延性（如铜）：** 线性，然后曲线、屈服、加工硬化、UTS、颈缩、断裂。
- **脆性（如玻璃）：** 线性到突然断裂——伸长量非常小。
- **聚合物（如橡胶）：** 从开始即非线性——"J形"曲线，断裂前伸长量非常大。
- **弹性体（如橡皮筋）：** 滞后——加载和卸载路径不同。

### Gradient Meaning / 斜率含义
**English:** Gradient = stiffness ($k$). Different for each sample even of same material if dimensions differ.
**中文：** 斜率 = 刚度（$k$）。即使相同材料，如果尺寸不同，也不同。

### Area Meaning / 面积含义
**English:** Area under loading curve = work done on material. Area under unloading curve = work recovered. Difference = energy dissipated (hysteresis loss).
**中文：** 加载曲线下面积 = 对材料做的功。卸载曲线下面积 = 恢复的功。差值 = 耗散的能量（滞后损耗）。

### Exam Interpretation / 考试解读
**English:**
- CAIE often asks to sketch force-extension graphs for different materials.
- Edexcel may ask to describe the behaviour of specific materials.
- Rubber shows hysteresis — important for energy absorption applications.
- Brittle materials fail with little warning (no plastic deformation).

**中文：**
- CAIE常要求绘制不同材料的力-伸长图。
- 爱德思可能要求描述特定材料的行为。
- 橡胶显示滞后——对能量吸收应用很重要。
- 脆性材料几乎没有预警地失效（无塑性形变）。

### Common Questions / 常见问题
**English:**
1. Sketch the force-extension graph for a brittle material.
2. Explain why rubber shows hysteresis.
3. Compare the force-extension graphs for copper and glass.
4. Describe the loading and unloading curves for an elastomer.

**中文：**
1. 绘制脆性材料的力-伸长图。
2. 解释橡胶为何显示滞后。
3. 比较铜和玻璃的力-伸长图。
4. 描述弹性体的加载和卸载曲线。

> 📷 **IMAGE PROMPT — GRAPH-03: Force-Extension Graphs for Ductile, Brittle, and Polymeric Materials**
>
> Three separate graphs side by side: (Left) Ductile material — linear region, yield, work hardening, UTS, necking; (Middle) Brittle material — straight line to sudden fracture; (Right) Polymeric material — J-shaped curve with large extension. Label axes (Force/N, Extension/m). Label key points. Clean, professional style.

---

# 7. Required Diagrams / 必备图表

## 7.1 Stress-Strain Curve with Key Points Labeled / 标注关键点的应力-应变曲线

### Description / 描述
**English:** A stress-strain graph for a typical ductile material (e.g., mild steel) showing all key points: limit of proportionality, elastic limit, yield point, UTS, and fracture point. The graph should show the linear elastic region, non-linear elastic region, yield plateau, work hardening region, necking region, and fracture. Axes should be labeled with units.

**中文：** 典型延性材料（如低碳钢）的应力-应变图，显示所有关键点：比例极限、弹性极限、屈服点、UTS和断裂点。图形应显示线性弹性区域、非线性弹性区域、屈服平台、加工硬化区域、颈缩区域和断裂。坐标轴应标注单位。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-01: Stress-Strain Curve for Ductile Material with All Key Points**
>
> A detailed stress-strain graph for mild steel. x-axis: Strain (dimensionless, 0 to 0.25). y-axis: Stress (Pa, 0 to 500e6). Show a straight line from origin (0,0) to point A (limit of proportionality). Slight curve from A to B (elastic limit). Sharp drop to C (upper yield point), then plateau to D (lower yield point). Rising curve from D to E (work hardening). Peak at F (UTS). Dropping curve from F to G (necking). End at H (fracture). Label all points A-H with text. Use gridlines. Professional scientific graph style. Color: blue line on white background.

### Labels Required / 需要标注
| Label (EN) | Label (CN) |
|------------|------------|
| Limit of Proportionality | 比例极限 |
| Elastic Limit | 弹性极限 |
| Upper Yield Point | 上屈服点 |
| Lower Yield Point | 下屈服点 |
| Ultimate Tensile Stress (UTS) | 极限抗拉强度 |
| Fracture Point | 断裂点 |
| Elastic Region | 弹性区域 |
| Plastic Region | 塑性区域 |
| Work Hardening | 加工硬化 |
| Necking | 颈缩 |

### Exam Importance / 考试重要性
**English:** This is the most important diagram in this topic. Both CAIE and Edexcel frequently ask students to label key points, identify regions, and explain the physical processes occurring at each stage. Understanding this diagram is essential for [[Stress-Strain Graphs and Material Behaviour]].

**中文：** 这是本主题中最重要的图表。CAIE和爱德思都经常要求学生标注关键点、识别区域并解释每个阶段发生的物理过程。理解此图对于[[应力-应变图与材料行为]]至关重要。

---

## 7.2 Experimental Setup for Determining Young Modulus / 测定杨氏模量的实验装置

### Description / 描述
**English:** A diagram showing the experimental setup to determine the Young Modulus of a metal wire. The setup includes: a long thin wire clamped at the top, hanging vertically with a weight hanger at the bottom. A reference marker (e.g., a piece of tape or a pointer) is attached to the wire, and a ruler or vernier scale is used to measure extension. A control wire (identical but unloaded) is used to compensate for temperature changes. The diagram should show the arrangement of pulleys, weights, and measurement devices.

**中文：** 显示测定金属丝杨氏模量的实验装置图。装置包括：顶部夹紧的长细金属丝，底部悬挂砝码钩。金属丝上附有参考标记（如胶带或指针），使用尺子或游标尺测量伸长量。使用控制金属丝（相同但未加载）补偿温度变化。图示应显示滑轮、砝码和测量装置的布置。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-02: Experimental Setup for Young Modulus Determination (Searle's Method)**
>
> A clear laboratory diagram showing: Two identical long thin wires (test wire and control wire) hanging vertically from a rigid support at the top. Test wire has a weight hanger with slotted masses at bottom. Control wire has a fixed weight to keep it taut. Both wires have reference markers (small pieces of tape) at the same height. A vernier scale or traveling microscope is positioned to measure the movement of the test wire's marker relative to the control wire's marker. A ruler shows the original length of the wire. Labels: "Test Wire", "Control Wire", "Weight Hanger", "Slotted Masses", "Reference Markers", "Vernier Scale", "Rigid Support". Clean, schematic style with clear labels. No background clutter.

### Labels Required / 需要标注
| Label (EN) | Label (CN) |
|------------|------------|
| Test Wire | 测试金属丝 |
| Control Wire | 控制金属丝 |
| Rigid Support | 刚性支架 |
| Weight Hanger | 砝码钩 |
| Slotted Masses | 槽码 |
| Reference Markers | 参考标记 |
| Vernier Scale / Traveling Microscope | 游标尺/移动显微镜 |
| Original Length ($L_0$) | 原始长度（$L_0$） |
| Extension ($\Delta L$) | 伸长量（$\Delta L$） |

### Exam Importance / 考试重要性
**English:** This experimental setup is frequently tested in CAIE Paper 3 (AS) and Paper 5 (A2), and Edexcel Unit 3 (AS) and Unit 6 (A2). Students must be able to describe the procedure, identify sources of error, and explain how to improve accuracy. This is directly linked to [[Experimental Determination of Young Modulus]].

**中文：** 该实验装置在CAIE Paper 3（AS）和Paper 5（A2）以及爱德思Unit 3（AS）和Unit 6（A2）中经常考查。学生必须能够描述实验步骤、识别误差来源并解释如何提高精度。这与[[杨氏模量的实验测定]]直接相关。

---

## 7.3 Force-Extension Graphs for Different Material Types / 不同材料类型的力-伸长图

### Description / 描述
**English:** Three force-extension graphs side by side showing the characteristic shapes for: (a) a ductile material (e.g., copper), (b) a brittle material (e.g., glass), and (c) a polymeric material (e.g., rubber). Each graph should have labeled axes and key features. The ductile graph shows linear region, yield, work hardening, UTS, and necking. The brittle graph shows linear region then sudden fracture. The polymeric graph shows a J-shaped curve with large extension.

**中文：** 三个并排的力-伸长图，显示以下特征形状：(a) 延性材料（如铜），(b) 脆性材料（如玻璃），(c) 聚合物材料（如橡胶）。每个图应有标注的坐标轴和关键特征。延性图显示线性区域、屈服、加工硬化、UTS和颈缩。脆性图显示线性区域然后突然断裂。聚合物图显示J形曲线，伸长量大。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-03: Comparison of Force-Extension Graphs for Three Material Types**
>
> Three separate force-extension graphs arranged horizontally. Graph A (Ductile): Force on y-axis, Extension on x-axis. Linear region from origin, then curve, yield plateau, rising curve (work hardening), peak (UTS), dropping curve (necking), fracture point. Graph B (Brittle): Straight line from origin to sudden fracture point — very small extension. Graph C (Polymeric): J-shaped curve starting with shallow slope, becoming steeper, then very large extension to fracture. All graphs have labeled axes: "Force / N" and "Extension / m". Key points labeled: "Limit of Proportionality", "Yield Point", "UTS", "Fracture". Clean, schematic style. Different colors for each graph.

### Labels Required / 需要标注
| Label (EN) | Label (CN) |
|------------|------------|
| Ductile Material | 延性材料 |
| Brittle Material | 脆性材料 |
| Polymeric Material | 聚合物材料 |
| Limit of Proportionality | 比例极限 |
| Yield Point | 屈服点 |
| Ultimate Tensile Stress (UTS) | 极限抗拉强度 |
| Fracture Point | 断裂点 |
| Elastic Region | 弹性区域 |
| Plastic Region | 塑性区域 |
| Necking | 颈缩 |

### Exam Importance / 考试重要性
**English:** Both CAIE and Edexcel require students to describe and compare the behaviour of different material types. This diagram helps students visualize the differences and is essential for understanding [[Ultimate Tensile Strength]] and [[Breaking Stress]].

**中文：** CAIE和爱德思都要求学生描述和比较不同材料类型的行为。此图帮助学生可视化差异，对于理解[[极限抗拉强度]]和[[断裂应力]]至关重要。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Young Modulus from Experimental Data / 从实验数据计算杨氏模量

### Question / 题目
**English:**
A student investigates the stretching of a steel wire. The wire has original length $L_0 = 2.50 \text{ m}$ and diameter $d = 0.50 \text{ mm}$. When a mass of $m = 5.0 \text{ kg}$ is hung from the wire, the extension is $\Delta L = 1.2 \text{ mm}$.

(a) Calculate the stress in the wire.
(b) Calculate the strain in the wire.
(c) Calculate the Young Modulus of steel.
(d) Calculate the stiffness of this wire.

**中文：**
一名学生研究钢丝的拉伸。钢丝原始长度 $L_0 = 2.50 \text{ m}$，直径 $d = 0.50 \text{ mm}$。当悬挂质量 $m = 5.0 \text{ kg}$ 时，伸长量为 $\Delta L = 1.2 \text{ mm}$。

(a) 计算钢丝中的应力。
(b) 计算钢丝中的应变。
(c) 计算钢的杨氏模量。
(d) 计算该钢丝的刚度。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — EX-01: Diagram for Young Modulus Calculation Problem**
>
> Simple schematic showing a vertical wire of length 2.50 m, diameter 0.50 mm, with a 5.0 kg mass hanging from the bottom. The wire is clamped at the top. Show the extension of 1.2 mm (exaggerated for visibility). Label: "L₀ = 2.50 m", "d = 0.50 mm", "m = 5.0 kg", "ΔL = 1.2 mm". Clean, simple style.

### Solution / 解答

**Step 1: Calculate cross-sectional area**
$$ A = \pi r^2 = \pi \left(\frac{d}{2}\right)^2 = \pi \left(\frac{0.50 \times 10^{-3}}{2}\right)^2 = \pi (0.25 \times 10^{-3})^2 $$
$$ A = \pi \times 6.25 \times 10^{-8} = 1.9635 \times 10^{-7} \text{ m}^2 $$

**Step 2: Calculate force**
$$ F = mg = 5.0 \times 9.81 = 49.05 \text{ N} $$

**Step 3: Calculate stress (a)**
$$ \sigma = \frac{F}{A} = \frac{49.05}{1.9635 \times 10^{-7}} = 2.498 \times 10^8 \text{ Pa} $$
$$ \sigma \approx 2.5 \times 10^8 \text{ Pa} \text{ (or } 250 \text{ MPa)} $$

**Step 4: Calculate strain (b)**
$$ \varepsilon = \frac{\Delta L}{L_0} = \frac{1.2 \times 10^{-3}}{2.50} = 4.8 \times 10^{-4} $$
$$ \varepsilon = 4.8 \times 10^{-4} \text{ (dimensionless)} $$

**Step 5: Calculate Young Modulus (c)**
$$ E = \frac{\sigma}{\varepsilon} = \frac{2.498 \times 10^8}{4.8 \times 10^{-4}} = 5.204 \times 10^{11} \text{ Pa} $$
$$ E \approx 5.2 \times 10^{11} \text{ Pa} \text{ (or } 520 \text{ GPa)} $$

**Step 6: Calculate stiffness (d)**
$$ k = \frac{F}{\Delta L} = \frac{49.05}{1.2 \times 10^{-3}} = 4.0875 \times 10^4 \text{ N m}^{-1} $$
$$ k \approx 4.1 \times 10^4 \text{ N m}^{-1} $$

**Alternative method for (d):**
$$ k = \frac{EA}{L_0} = \frac{(5.204 \times 10^{11})(1.9635 \times 10^{-7})}{2.50} = 4.087 \times 10^4 \text{ N m}^{-1} $$

### Final Answer / 最终答案
**Answer:**
(a) $\sigma = 2.5 \times 10^8 \text{ Pa}$ (250 MPa)
(b) $\varepsilon = 4.8 \times 10^{-4}$
(c) $E = 5.2 \times 10^{11} \text{ Pa}$ (520 GPa)
(d) $k = 4.1 \times 10^4 \text{ N m}^{-1}$

**答案：**
(a) $\sigma = 2.5 \times 10^8 \text{ Pa}$（250 MPa）
(b) $\varepsilon = 4.8 \times 10^{-4}$
(c) $E = 5.2 \times 10^{11} \text{ Pa}$（520 GPa）
(d) $k = 4.1 \times 10^4 \text{ N m}^{-1}$

### Examiner Notes / 考官点评
**English:**
- Common mistake: using diameter instead of radius in area calculation. Always use $A = \pi r^2 = \pi (d/2)^2$.
- Common mistake: forgetting to convert mm to m. $0.50 \text{ mm} = 0.50 \times 10^{-3} \text{ m}$.
- The calculated Young Modulus (520 GPa) is higher than typical steel (~200 GPa). This suggests an experimental error or the wire is a different material. Students should comment on plausibility.
- Always include units in final answers.
- Use appropriate significant figures (2 s.f. given input data).

**中文：**
- 常见错误：面积计算中使用直径而非半径。始终使用 $A = \pi r^2 = \pi (d/2)^2$。
- 常见错误：忘记将mm转换为m。$0.50 \text{ mm} = 0.50 \times 10^{-3} \text{ m}$。
- 计算出的杨氏模量（520 GPa）高于典型钢（约200 GPa）。这表明存在实验误差或金属丝是不同材料。学生应评论合理性。
- 最终答案中始终包含单位。
- 使用适当的有效数字（输入数据为2位有效数字）。

### Alternative Method / 替代方法
**English:**
For part (c), use the combined formula directly:
$$ E = \frac{FL_0}{A\Delta L} = \frac{(49.05)(2.50)}{(1.9635 \times 10^{-7})(1.2 \times 10^{-3})} = 5.204 \times 10^{11} \text{ Pa} $$

**中文：**
对于(c)部分，直接使用组合公式：
$$ E = \frac{FL_0}{A\Delta L} = \frac{(49.05)(2.50)}{(1.9635 \times 10^{-7})(1.2 \times 10^{-3})} = 5.204 \times 10^{11} \text{ Pa} $$

---

## Example 2: Interpreting a Stress-Strain Graph / 解读应力-应变图

### Question / 题目
**English:**
The stress-strain graph for a sample of aluminium is shown below. Use the graph to determine:

(a) The Young Modulus of aluminium.
(b) The 0.1% proof stress.
(c) The ultimate tensile stress.
(d) The approximate strain at fracture.
(e) The energy absorbed per unit volume up to the elastic limit.

[Assume the graph shows: linear region from (0,0) to (0.002, 140 MPa), then curves to UTS at (0.10, 300 MPa), then fractures at (0.15, 280 MPa)]

**中文：**
铝样品的应力-应变图如下所示。使用图形确定：

(a) 铝的杨氏模量。
(b) 0.1% 条件屈服应力。
(c) 极限抗拉强度。
(d) 断裂时的近似应变。
(e) 弹性极限前每单位体积吸收的能量。

[假设图形显示：线性区域从(0,0)到(0.002, 140 MPa)，然后曲线到UTS在(0.10, 300 MPa)，然后在(0.15, 280 MPa)断裂]

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — EX-02: Stress-Strain Graph for Aluminium**
>
> A stress-strain graph for aluminium. x-axis: Strain (0 to 0.18). y-axis: Stress (MPa, 0 to 350). Show a straight line from origin to point (0.002, 140 MPa). Then a gradual curve rising to a peak at (0.10, 300 MPa) — label "UTS". Then a slight drop to fracture at (0.15, 280 MPa) — label "Fracture". Draw a dashed line parallel to the linear region starting at strain = 0.001 to show the 0.1% proof stress. Label axes with units. Professional style.

### Solution / 解答

**Step 1: Calculate Young Modulus (a)**
The linear region extends from (0,0) to (0.002, 140 × 10⁶ Pa).

$$ E = \frac{\sigma}{\varepsilon} = \frac{140 \times 10^6}{0.002} = 7.0 \times 10^{10} \text{ Pa} $$
$$ E = 70 \text{ GPa} $$

**Step 2: Determine 0.1% proof stress (b)**
0.1% strain = 0.001. Draw a line parallel to the linear region starting at $\varepsilon = 0.001$. Where this line intersects the stress-strain curve, read the stress value.

From the graph, at $\varepsilon = 0.001$ offset, the intersection occurs at approximately $\sigma \approx 150 \text{ MPa}$.

**Step 3: Determine UTS (c)**
The UTS is the maximum stress on the graph.
$$ \text{UTS} = 300 \text{ MPa} = 3.0 \times 10^8 \text{ Pa} $$

**Step 4: Determine strain at fracture (d)**
The fracture point is at the end of the curve.
$$ \varepsilon_{\text{fracture}} \approx 0.15 $$

**Step 5: Calculate energy per unit volume up to elastic limit (e)**
The energy per unit volume (strain energy density) is the area under the stress-strain graph up to the elastic limit. Assuming the elastic limit is at the end of the linear region ($\varepsilon = 0.002$):

$$ \text{Energy per unit volume} = \frac{1}{2} \times \sigma \times \varepsilon = \frac{1}{2} \times (140 \times 10^6) \times 0.002 $$
$$ = \frac{1}{2} \times 280,000 = 140,000 \text{ J m}^{-3} $$
$$ = 1.4 \times 10^5 \text{ J m}^{-3} $$

### Final Answer / 最终答案
**Answer:**
(a) $E = 70 \text{ GPa}$
(b) 0.1% proof stress $\approx 150 \text{ MPa}$
(c) UTS $= 300 \text{ MPa}$
(d) Strain at fracture $\approx 0.15$
(e) Energy per unit volume $= 1.4 \times 10^5 \text{ J m}^{-3}$

**答案：**
(a) $E = 70 \text{ GPa}$
(b) 0.1% 条件屈服应力 $\approx 150 \text{ MPa}$
(c) UTS $= 300 \text{ MPa}$
(d) 断裂应变 $\approx 0.15$
(e) 单位体积能量 $= 1.4 \times 10^5 \text{ J m}^{-3}$

### Examiner Notes / 考官点评
**English:**
- For the Young Modulus, always use the linear (elastic) region of the graph.
- The 0.1% proof stress is used for materials without a clear yield point (like aluminium).
- The area under the elastic region is a triangle: $\frac{1}{2} \times \text{base} \times \text{height}$.
- For the total area under the entire curve (toughness), you would need to count squares or integrate.
- CAIE often asks to estimate values from graphs — read carefully and interpolate.

**中文：**
- 对于杨氏模量，始终使用图形的线性（弹性）区域。
- 0.1% 条件屈服应力用于没有明显屈服点的材料（如铝）。
- 弹性区域下的面积是三角形：$\frac{1}{2} \times \text{底} \times \text{高}$。
- 对于整个曲线下的总面积（韧性），需要数方格或积分。
- CAIE常要求从图形估计数值——仔细读取并插值。

### Alternative Method / 替代方法
**English:**
For part (e), the area could also be calculated by counting squares if the graph has gridlines. Each square represents a certain energy density value.

**中文：**
对于(e)部分，如果图形有网格线，也可以通过数方格计算面积。每个方格代表一定的能量密度值。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation / 计算 | High | Medium | 📝 *待填入* |
| Explanation / 解释 | High | Medium-High | 📝 *待填入* |
| Graph Analysis / 图表分析 | High | Medium-High | 📝 *待填入* |
| Practical / 实验 | Medium | High | 📝 *待填入* |
| Derivation / 推导 | Low | Medium | 📝 *待填入* |
| Definition / 定义 | Medium | Low | 📝 *待填入* |
| Comparison / 比较 | Medium | Medium | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| Command Word (EN) | Command Word (CN) | Typical Usage / 典型用法 |
|-------------------|-------------------|------------------------|
| State | 陈述 | State the definition of stress. |
| Define | 定义 | Define the Young Modulus. |
| Calculate | 计算 | Calculate the stress in the wire. |
| Determine | 确定 | Determine the Young Modulus from the graph. |
| Explain | 解释 | Explain why the wire does not return to its original length. |
| Describe | 描述 | Describe the shape of the stress-strain graph for a brittle material. |
| Sketch | 绘制 | Sketch a force-extension graph for rubber. |
| Compare | 比较 | Compare the behaviour of ductile and brittle materials. |
| Suggest | 建议 | Suggest how the experiment could be improved. |
| Show that | 证明 | Show that the Young Modulus is 200 GPa. |

**English:**
- Calculation questions typically involve finding stress, strain, Young Modulus, or stiffness.
- Explanation questions often ask about elastic vs plastic deformation, or why materials behave differently.
- Graph analysis questions require reading values, calculating gradients, and identifying key points.
- Practical questions test knowledge of experimental setup, error analysis, and improvements.
- Definitions are frequently tested in the first part of multi-part questions.

**中文：**
- 计算题通常涉及求应力、应变、杨氏模量或刚度。
- 解释题常问弹性与塑性形变，或材料为何行为不同。
- 图表分析题要求读取数值、计算斜率和识别关键点。
- 实验题考查实验装置、误差分析和改进方法的知识。
- 定义常在多部分问题的第一部分考查。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This topic has strong practical components in both CAIE and Edexcel specifications.

**CAIE Practical Connections:**
- **Paper 3 (AS):** Students may be asked to determine the Young Modulus of a wire using an experimental setup. Skills tested include: measuring diameter with a micrometer, measuring length with a ruler, measuring extension with a vernier scale or traveling microscope, plotting force-extension graphs, calculating gradients, and determining uncertainties.
- **Paper 5 (A2):** Students may be asked to design an experiment to determine the Young Modulus of a material, including identifying variables, controlling conditions, and analyzing errors.

**Edexcel Practical Connections:**
- **Unit 3 (AS):** Core Practical 4: Determine the Young Modulus of a material. Skills include: using a micrometer to measure wire diameter, setting up the apparatus, taking measurements of force and extension, plotting graphs, and calculating the Young Modulus.
- **Unit 6 (A2):** More advanced practical work involving stress-strain analysis and material characterization.

**Key Practical Skills / 关键实验技能:**

1. **Measuring diameter / 测量直径:**
   - Use a micrometer screw gauge (resolution 0.01 mm).
   - Measure at several points along the wire and average.
   - Avoid applying too much pressure (can squash the wire).

2. **Measuring length / 测量长度:**
   - Use a meter ruler or tape measure.
   - Measure the original length from clamp to marker.
   - Ensure the wire is straight but not stretched.

3. **Measuring extension / 测量伸长量:**
   - Use a vernier scale or traveling microscope for precision.
   - Use a control wire to compensate for temperature changes.
   - Take readings for increasing and decreasing loads to check for hysteresis.

4. **Graph plotting / 图表绘制:**
   - Plot force-extension or stress-strain graphs.
   - Draw the best-fit line through the linear region.
   - Calculate gradient to find stiffness or Young Modulus.

5. **Uncertainties / 不确定度:**
   - Calculate percentage uncertainties in $F$, $A$, $L_0$, and $\Delta L$.
   - Combine uncertainties to find the uncertainty in $E$.
   - Identify the largest source of uncertainty (usually area measurement).

6. **Error analysis / 误差分析:**
   - Systematic errors: zero error on micrometer, parallax error in length measurement.
   - Random errors: variations in wire diameter, temperature fluctuations.
   - Improvements: use longer wire (larger extension), use thinner wire (larger stress), use more sensitive measurement devices.

**中文：**
本主题在CAIE和爱德思考纲中都有很强的实验成分。

**CAIE实验链接：**
- **Paper 3 (AS)：** 学生可能被要求使用实验装置测定金属丝的杨氏模量。考查的技能包括：使用千分尺测量直径、使用尺子测量长度、使用游标尺或移动显微镜测量伸长量、绘制力-伸长图、计算斜率和确定不确定度。
- **Paper 5 (A2)：** 学生可能被要求设计测定材料杨氏模量的实验，包括识别变量、控制条件和分析误差。

**爱德思实验链接：**
- **Unit 3 (AS)：** 核心实践4：测定材料的杨氏模量。技能包括：使用千分尺测量金属丝直径、设置装置、测量力和伸长量、绘制图表和计算杨氏模量。
- **Unit 6 (A2)：** 涉及应力-应变分析和材料表征的更高级实验工作。

**关键实验技能：**

1. **测量直径：**
   - 使用千分尺（分辨率0.01 mm）。
   - 沿金属丝在多个点测量并取平均。
   - 避免施加过大压力（可能压扁金属丝）。

2. **测量长度：**
   - 使用米尺或卷尺。
   - 测量从夹子到标记的原始长度。
   - 确保金属丝伸直但未拉伸。

3. **测量伸长量：**
   - 使用游标尺或移动显微镜以提高精度。
   - 使用控制金属丝补偿温度变化。
   - 对增加和减少载荷进行读数以检查滞后。

4. **图表绘制：**
   - 绘制力-伸长图或应力-应变图。
   - 通过线性区域绘制最佳拟合线。
   - 计算斜率以找到刚度或杨氏模量。

5. **不确定度：**
   - 计算$F$、$A$、$L_0$和$\Delta L$的百分比不确定度。
   - 组合不确定度以找到$E$的不确定度。
   - 识别最大的不确定度来源（通常是面积测量）。

6. **误差分析：**
   - 系统误差：千分尺零误差、长度测量中的视差误差。
   - 随机误差：金属丝直径变化、温度波动。
   - 改进：使用更长的金属丝（更大伸长量）、使用更细的金属丝（更大应力）、使用更灵敏的测量装置。

> 📋 **CIE Only:** CAIE Paper 3 often includes a question where students must determine the Young Modulus from experimental data. The control wire method is specifically tested.
>
> 📋 **Edexcel Only:** Edexcel Unit 3 Core Practical 4 is explicitly titled "Determine the Young Modulus of a material." Students must be familiar with the specific apparatus and procedure described in the specification.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    SSY[Stress, Strain and Young Modulus] --> TS[Tensile Stress and Strain]
    SSY --> YM[Young Modulus Definition and Formula]
    SSY --> EY[Experimental Determination of Young Modulus]
    SSY --> UTS[Ultimate Tensile Strength]
    SSY --> BS[Breaking Stress]
    
    %% Prerequisites
    DENSITY[Density, Hooke's Law and Springs] --> SSY
    HOOKE[Hooke's Law: F = kΔL] --> SSY
    FORCE[Force and Newton's Laws] --> SSY
    
    %% Sub-topics details
    TS --> STRESS[Stress σ = F/A]
    TS --> STRAIN[Strain ε = ΔL/L₀]
    
    YM --> FORMULA[E = σ/ε = FL₀/AΔL]
    YM --> STIFFNESS[Stiffness k = EA/L₀]
    
    EY --> SEARLE[Searle's Apparatus]
    EY --> CONTROL[Control Wire Method]
    EY --> MICROMETER[Micrometer Measurement]
    EY --> UNCERTAINTY[Uncertainty Analysis]
    
    UTS --> MAX_STRESS[Maximum Stress on Graph]
    UTS --> NECKING[Necking Region]
    
    BS --> FRACTURE[Fracture Point]
    BS --> DUCTILE[Ductile vs Brittle Fracture]
    
    %% Related Topics
    SSY --> SSG[Stress-Strain Graphs and Material Behaviour]
    SSG --> DUCTILE_BEH[Ductile Behaviour]
    SSG --> BRITTLE_BEH[Brittle Behaviour]
    SSG --> POLYMER_BEH[Polymeric Behaviour]
    SSG --> ELASTIC[Elastic Deformation]
    SSG --> PLASTIC[Plastic Deformation]
    SSG --> HYSTERESIS[Hysteresis in Rubber]
    
    %% Key Points
    STRESS --> UNITS[Units: Pa or N m⁻²]
    STRAIN --> DIMENSIONLESS[Dimensionless]
    YM --> MATERIAL_PROP[Material Property - Intrinsic]
    STIFFNESS --> SAMPLE_DEP[Sample Dependent]
    
    %% Graph Connections
    SSG --> FE_GRAPH[Force-Extension Graph]
    SSG --> SS_GRAPH[Stress-Strain Graph]
    FE_GRAPH --> GRADIENT_FE[Gradient = k]
    SS_GRAPH --> GRADIENT_SS[Gradient = E]
    FE_GRAPH --> AREA_FE[Area = Work Done]
    SS_GRAPH --> AREA_SS[Area = Energy/Volume]
    
    %% Practical Connections
    EY --> PAPER3[CAIE Paper 3 / Edexcel Unit 3]
    PAPER3 --> MEASUREMENT[Measurement Techniques]
    MEASUREMENT --> ERROR[Error Analysis]
    
    %% Styling
    classDef main fill:#4a90d9,color:#fff,stroke:#2c5f8a
    classDef sub fill:#5cb85c,color:#fff,stroke:#3d8b3d
    classDef practical fill:#f0ad4e,color:#fff,stroke:#cc8800
    classDef graph fill:#d9534f,color:#fff,stroke:#b52e2e
    classDef related fill:#5bc0de,color:#fff,stroke:#3a8a9e
    
    class SSY main
    class TS,STRESS,STRAIN,YM,FORMULA,STIFFNESS,UTS,MAX_STRESS,NECKING,BS,FRACTURE sub
    class EY,SEARLE,CONTROL,MICROMETER,UNCERTAINTY,PAPER3,MEASUREMENT,ERROR practical
    class SSG,FE_GRAPH,SS_GRAPH,GRADIENT_FE,GRADIENT_SS,AREA_FE,AREA_SS graph
    class DENSITY,HOOKE,FORCE,DUCTILE_BEH,BRITTLE_BEH,POLYMER_BEH,ELASTIC,PLASTIC,HYSTERESIS related
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | **Stress / 应力:** $\sigma = F/A$ (Pa or N m⁻²) — force per unit cross-sectional area<br>**Strain / 应变:** $\varepsilon = \Delta L / L_0$ (dimensionless) — fractional change in length<br>**Young Modulus / 杨氏模量:** $E = \sigma/\varepsilon = FL_0/(A\Delta L)$ (Pa) — measure of stiffness<br>**Elastic Limit / 弹性极限:** Maximum stress without permanent deformation<br>**Limit of Proportionality / 比例极限:** Maximum stress where Hooke's law holds<br>**UTS / 极限抗拉强度:** Maximum stress before failure<br>**Breaking Stress / 断裂应力:** Stress at fracture |
| **Equations / 公式** | $\sigma = F/A$ — Stress<br>$\varepsilon = \Delta L/L_0$ — Strain<br>$E = \sigma/\varepsilon = FL_0/(A\Delta L)$ — Young Modulus<br>$k = F/\Delta L = EA/L_0$ — Stiffness<br>$F = k\Delta L$ — Hooke's Law<br>$A = \pi r^2 = \pi(d/2)^2$ — Area of wire |
| **Graphs / 图表** | **Force-Extension:** Gradient = $k$ (stiffness), Area = work done<br>**Stress-Strain:** Gradient (linear) = $E$ (Young Modulus), Area = energy/volume<br>**Key points on stress-strain:** Limit of proportionality → Elastic limit → Yield point → UTS → Fracture<br>**Ductile:** Large plastic region, necking before fracture<br>**Brittle:** No plastic region, sudden fracture<br>**Polymeric:** J-shaped curve, large extension, hysteresis |
| **Key Facts / 关键事实** | • Young Modulus is a material property (intrinsic); stiffness depends on dimensions<br>• Strain is dimensionless — no units<br>• Always convert mm to m: $1 \text{ mm} = 10^{-3} \text{ m}$, $1 \text{ mm}^2 = 10^{-6} \text{ m}^2$<br>• Area uses radius, not diameter: $A = \pi r^2 = \pi(d/2)^2$<br>• For ductile materials: UTS > Breaking Stress (due to necking)<br>• For brittle materials: UTS ≈ Breaking Stress<br>• Elastic deformation is reversible; plastic deformation is permanent<br>• Rubber shows hysteresis — energy is dissipated as heat |
| **Exam Reminders / 考试提醒** | • Show all formulas before substitution<br>• Include units in every step<br>• Use correct significant figures (match input data)<br>• For graph questions: read values carefully, use gradient triangle<br>• For definitions: use precise wording ("force per unit cross-sectional area")<br>• For explanations: mention atomic/molecular level (atoms displaced, return, or slide past)<br>• For practical: describe control wire, micrometer, vernier scale, error sources<br>• Common calculation errors: area from diameter, mm to m conversion, strain units |