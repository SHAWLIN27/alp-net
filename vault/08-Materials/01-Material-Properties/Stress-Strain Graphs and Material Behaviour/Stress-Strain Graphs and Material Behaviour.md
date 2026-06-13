# 1. Overview / 概述

**English:**
This topic, **Stress-Strain Graphs and Material Behaviour**, is a cornerstone of materials physics in both the Cambridge 9702 and Edexcel IAL A-Level syllabuses. It builds directly upon the foundational concepts of [[Stress, Strain and Young Modulus]] by exploring how materials respond to applied forces beyond the elastic limit. The central tool is the stress-strain graph, a plot that reveals a material's unique mechanical "fingerprint"—its stiffness, strength, ductility, brittleness, and toughness.

Understanding these graphs is crucial for engineers and physicists who must select appropriate materials for real-world applications, from building skyscrapers and aircraft wings to designing medical implants and sports equipment. The graph allows us to identify key points such as the limit of proportionality, elastic limit, yield point, ultimate tensile strength (UTS), and the breaking point. The shape of the curve—whether it shows a long plastic region (ductile), a sudden fracture (brittle), or a large extension with little force (polymeric)—dictates the material's suitability for a given task.

In examinations, this topic is assessed through graph interpretation, calculation of [[Young Modulus]] from the linear region, calculation of energy stored (area under the graph), and qualitative explanations of material behaviour. Both Cambridge and Edexcel require students to compare and contrast the stress-strain curves for ductile, brittle, and polymeric materials, and to link these properties to their atomic or molecular structure.

**中文：**
本主题“应力-应变图与材料行为”是剑桥9702和爱德思IAL A-Level物理课程中材料物理学的基石。它直接建立在[[应力、应变和杨氏模量]]的基础概念之上，探讨材料在超过弹性极限后对外加力的响应。核心工具是应力-应变图，该图揭示了材料独特的力学“指纹”——其刚度、强度、延展性、脆性和韧性。

理解这些图表对于必须为实际应用（从建造摩天大楼和飞机机翼到设计医疗植入物和运动器材）选择合适的材料的工程师和物理学家至关重要。该图使我们能够识别关键点，如比例极限、弹性极限、屈服点、极限抗拉强度（UTS）和断裂点。曲线的形状——无论是显示长塑性区域（延性）、突然断裂（脆性）还是小力大伸长（聚合物）——决定了材料对特定任务的适用性。

在考试中，本主题通过图表解读、从线性区域计算[[杨氏模量]]、计算储存的能量（图表下方面积）以及对材料行为的定性解释来评估。剑桥和爱德思都要求学生比较和对比延性、脆性和聚合物材料的应力-应变曲线，并将这些特性与其原子或分子结构联系起来。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

**English:**
The following table maps the specific learning objectives from both exam boards. Students must be able to describe, interpret, and calculate from stress-strain graphs for different material types.

**中文：**
下表列出了两个考试委员会的具体学习目标。学生必须能够描述、解读和计算不同类型材料的应力-应变图。

| CAIE 9702 (6.3 a-e) | Edexcel IAL (WPH11 U1: 2.13-2.18) |
|-----------|-------------|
| 6.3(a) Describe the behaviour of materials in terms of extension/compression, elastic and plastic deformation, and the concept of breaking stress. | 2.13 Understand the terms elastic deformation and plastic deformation. |
| 6.3(b) Define and use the terms elastic limit, limit of proportionality, yield point, and ultimate tensile stress. | 2.14 Understand the terms limit of proportionality, elastic limit, yield point, and ultimate tensile strength. |
| 6.3(c) Describe and interpret stress-strain graphs for typical ductile, brittle, and polymeric materials. | 2.15 Describe and interpret stress-strain graphs for typical ductile, brittle, and polymeric materials. |
| 6.3(d) Calculate the Young modulus from the linear section of a stress-strain graph. | 2.16 Use the Young modulus to determine the stiffness of a material. |
| 6.3(e) Calculate the energy stored per unit volume from the area under the stress-strain graph. | 2.17 Calculate the energy stored per unit volume from the area under the stress-strain graph. |
| (Implicit) Relate material properties to atomic/molecular structure. | 2.18 Explain the behaviour of materials in terms of their atomic/molecular structure. |

> 📋 **CIE Only:** The syllabus explicitly requires students to "describe the behaviour of materials in terms of extension/compression" and to "define and use" the terms. The term "breaking stress" is used instead of "fracture stress".
> 📋 **Edexcel Only:** The syllabus explicitly requires students to "explain the behaviour of materials in terms of their atomic/molecular structure" (2.18), which is a more detailed requirement than CIE's implicit coverage.

**Examiner Expectations / 考官期望:**
- **English:** Candidates must be able to sketch and label stress-strain graphs from memory. They must correctly identify the key points on the curve and explain the physical processes occurring at each stage. Calculations must include correct units and significant figures. Qualitative explanations must link macroscopic behaviour to microscopic (atomic/molecular) structure.
- **中文：** 考生必须能够凭记忆绘制并标注应力-应变图。他们必须正确识别曲线上的关键点，并解释每个阶段发生的物理过程。计算必须包括正确的单位和有效数字。定性解释必须将宏观行为与微观（原子/分子）结构联系起来。

---

# 3. Core Definitions / 核心定义

**English:**
The following table provides the official definitions for key terms, along with common student mistakes.

**中文：**
下表提供了关键术语的官方定义以及学生常见错误。

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Elastic Deformation** / 弹性形变 | Deformation that is reversible; the material returns to its original shape when the load is removed. | 可逆的形变；当载荷移除时，材料恢复到其原始形状。 | Confusing with plastic deformation. Thinking it only applies to small strains. |
| **Plastic Deformation** / 塑性形变 | Deformation that is permanent; the material does not return to its original shape when the load is removed. | 永久性的形变；当载荷移除时，材料不会恢复到其原始形状。 | Thinking it occurs immediately after the elastic limit. It begins at the yield point. |
| **Limit of Proportionality** / 比例极限 | The point on a stress-strain graph beyond which stress is no longer directly proportional to strain. | 应力-应变图上，超过该点后应力不再与应变成正比。 | Confusing with the elastic limit. The limit of proportionality is the end of the straight-line region. |
| **Elastic Limit** / 弹性极限 | The point beyond which the material will not return to its original shape when the load is removed. | 超过该点后，当载荷移除时，材料将不会恢复到其原始形状。 | Thinking it is the same as the limit of proportionality. The elastic limit is usually slightly beyond the limit of proportionality. |
| **Yield Point** / 屈服点 | The point at which there is a large increase in strain with little or no increase in stress. | 应力几乎没有或没有增加，而应变却大幅增加的点。 | Confusing with the ultimate tensile strength. The yield point is where plastic deformation begins. |
| **Ultimate Tensile Strength (UTS)** / 极限抗拉强度 | The maximum stress a material can withstand before it fractures. | 材料在断裂前能承受的最大应力。 | Confusing with breaking stress. UTS is the peak of the graph; breaking stress is at the fracture point. |
| **Breaking Stress** / 断裂应力 | The stress at which the material actually fractures or breaks. | 材料实际断裂或破坏时的应力。 | Confusing with UTS. For ductile materials, breaking stress is lower than UTS. |
| **Ductile Material** / 延性材料 | A material that can undergo significant plastic deformation before fracturing. | 在断裂前能经历显著塑性形变的材料。 | Thinking all metals are ductile. Some metals (e.g., cast iron) are brittle. |
| **Brittle Material** / 脆性材料 | A material that fractures with little or no plastic deformation. | 几乎没有或没有塑性形变就断裂的材料。 | Thinking brittle materials are weak. Glass has high compressive strength. |
| **Polymeric Material** / 聚合物材料 | A material made of long-chain molecules that can undergo large elastic strains. | 由长链分子组成，能经历大弹性应变的材料。 | Thinking polymers are always elastic. Rubber is elastic; polythene can be plastic. |
| **Toughness** / 韧性 | The ability of a material to absorb energy before fracturing, measured by the area under the stress-strain graph. | 材料在断裂前吸收能量的能力，由应力-应变图下的面积衡量。 | Confusing with strength. A strong material has high UTS; a tough material absorbs lots of energy. |
| **Stiffness** / 刚度 | The resistance of a material to elastic deformation, measured by the [[Young Modulus]]. | 材料抵抗弹性形变的能力，由[[杨氏模量]]衡量。 | Confusing with strength. Stiffness is about elastic deformation; strength is about failure. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Elastic and Plastic Deformation / 弹性形变与塑性形变

### Explanation / 解释
**English:**
When a force is applied to a material, it deforms. If the deformation is **elastic**, the material returns to its original shape and size when the force is removed. This is because the atoms or molecules are displaced from their equilibrium positions but do not move past each other. The bonds between atoms are stretched but not broken. This region is governed by [[Hooke's Law]] and the [[Young Modulus]].

If the deformation is **plastic**, the material does not return to its original shape. This occurs when the stress exceeds the elastic limit. In a crystalline material like a metal, plastic deformation involves the movement of **dislocations**—line defects in the crystal lattice. Layers of atoms slide past each other, breaking and reforming bonds. This is permanent.

**中文：**
当对材料施加力时，它会形变。如果形变是**弹性的**，当力移除时，材料会恢复到其原始形状和大小。这是因为原子或分子从其平衡位置发生位移，但并未相互移动过去。原子间的键被拉伸但未断裂。该区域由[[胡克定律]]和[[杨氏模量]]控制。

如果形变是**塑性的**，材料不会恢复到其原始形状。当应力超过弹性极限时，就会发生这种情况。在像金属这样的晶体材料中，塑性形变涉及**位错**（晶格中的线缺陷）的运动。原子层相互滑过，断裂并重新形成键。这是永久性的。

### Physical Meaning / 物理意义
**English:**
- **Elastic deformation:** Like a rubber band stretching and snapping back. The energy is stored as elastic potential energy.
- **Plastic deformation:** Like bending a paperclip. It stays bent. The energy is dissipated as heat (internal energy).

**中文：**
- **弹性形变：** 就像橡皮筋拉伸并弹回。能量以弹性势能的形式储存。
- **塑性形变：** 就像弯曲回形针。它会保持弯曲。能量以热量（内能）的形式耗散。

### Common Misconceptions / 常见误区
1. **Misconception:** Elastic deformation is always linear.
   **Correction:** Elastic deformation can be non-linear (e.g., rubber). The limit of proportionality marks the end of linear elastic behaviour.
2. **Misconception:** Plastic deformation is immediate after the elastic limit.
   **Correction:** The yield point marks the onset of plastic deformation. There is a small region between the elastic limit and the yield point where behaviour is complex.
3. **Misconception:** All materials have a clear yield point.
   **Correction:** Some materials (e.g., glass, some polymers) do not have a distinct yield point. They fracture before yielding.

### Exam Tips / 考试提示
**English:**
- Cambridge and Edexcel often ask you to "explain the difference between elastic and plastic deformation" (2-3 marks). Use the key words: reversible/permanent, return to original shape/does not return, bonds stretch/bonds break and reform.
- For higher marks, mention the atomic/molecular level: "In elastic deformation, atoms are displaced from equilibrium but return. In plastic deformation, layers of atoms slide past each other (dislocation movement)."
- Be prepared to sketch a loading-unloading cycle for a material that has been plastically deformed. The unloading line is parallel to the initial linear region.

**中文：**
- 剑桥和爱德思经常要求你“解释弹性形变和塑性形变之间的区别”（2-3分）。使用关键词：可逆/永久、恢复到原始形状/不恢复、键拉伸/键断裂并重新形成。
- 为了获得更高分数，提及原子/分子层面：“在弹性形变中，原子从平衡位置位移但会返回。在塑性形变中，原子层相互滑过（位错运动）。”
- 准备好为已发生塑性形变的材料绘制加载-卸载循环图。卸载线平行于初始线性区域。

---

## 4.2 The Stress-Strain Graph / 应力-应变图

### Explanation / 解释
**English:**
The stress-strain graph is the most important tool for analysing material behaviour. Stress ($\sigma = F/A$) is plotted on the y-axis, and strain ($\epsilon = \Delta L/L$) is plotted on the x-axis. The graph is independent of the sample's dimensions, allowing direct comparison of different materials.

The graph has several distinct regions:
1. **Linear (Hookean) Region:** Stress is proportional to strain. The gradient is the [[Young Modulus]] ($E = \sigma / \epsilon$). This ends at the **limit of proportionality**.
2. **Elastic Region:** The material is still elastic, but the relationship is no longer linear. This ends at the **elastic limit**.
3. **Yield Point:** A sudden increase in strain with little or no increase in stress. Plastic deformation begins.
4. **Plastic Region:** The material deforms permanently. The curve rises to a maximum stress called the **ultimate tensile strength (UTS)**.
5. **Necking:** After the UTS, the material's cross-sectional area decreases locally (necking), causing the stress to drop even though the material is still supporting a load.
6. **Fracture:** The material breaks at the **breaking stress**.

**中文：**
应力-应变图是分析材料行为最重要的工具。应力（$\sigma = F/A$）绘制在y轴上，应变（$\epsilon = \Delta L/L$）绘制在x轴上。该图与样品的尺寸无关，允许直接比较不同材料。

该图有几个不同的区域：
1. **线性（胡克）区域：** 应力与应变成正比。梯度是[[杨氏模量]]（$E = \sigma / \epsilon$）。这结束于**比例极限**。
2. **弹性区域：** 材料仍然是弹性的，但关系不再是线性的。这结束于**弹性极限**。
3. **屈服点：** 应力几乎没有或没有增加，应变突然增加。塑性形变开始。
4. **塑性区域：** 材料发生永久形变。曲线上升到最大应力，称为**极限抗拉强度（UTS）**。
5. **颈缩：** 在UTS之后，材料的横截面积局部减小（颈缩），导致应力下降，即使材料仍在承受载荷。
6. **断裂：** 材料在**断裂应力**处断裂。

### Physical Meaning / 物理意义
**English:**
- The graph tells an engineer: "How much force can I apply before it permanently deforms?" (yield point), "What is the maximum load it can hold?" (UTS), and "How much energy can it absorb before breaking?" (area under graph).
- A steep initial gradient means a stiff material (high [[Young Modulus]]).
- A long, flat region after the yield point means a ductile material.
- A short curve ending abruptly means a brittle material.

**中文：**
- 该图告诉工程师：“在永久形变之前我能施加多大的力？”（屈服点），“它能承受的最大载荷是多少？”（UTS），以及“它在断裂前能吸收多少能量？”（图下方面积）。
- 陡峭的初始梯度意味着刚性材料（高[[杨氏模量]]）。
- 屈服点后长而平坦的区域意味着延性材料。
- 短而突然结束的曲线意味着脆性材料。

### Common Misconceptions / 常见误区
1. **Misconception:** The stress-strain graph is the same as the load-extension graph.
   **Correction:** They have the same shape, but the axes are different. Stress-strain is material-specific; load-extension is sample-specific.
2. **Misconception:** The breaking stress is always the highest point on the graph.
   **Correction:** For ductile materials, the breaking stress is lower than the UTS due to necking.
3. **Misconception:** The area under the graph is the total energy stored.
   **Correction:** The area under the graph is the **energy stored per unit volume** (energy density). Total energy = area × volume.

### Exam Tips / 考试提示
**English:**
- You must be able to sketch the stress-strain graphs for ductile, brittle, and polymeric materials from memory.
- Label ALL key points: limit of proportionality, elastic limit, yield point, UTS, breaking stress.
- When asked to "compare" two materials, use comparative language: "Material A has a higher Young modulus than Material B," "Material A is more ductile than Material B."
- For calculation questions, always check the units. Stress is in Pa (N/m²), strain is dimensionless.

**中文：**
- 你必须能够凭记忆绘制延性、脆性和聚合物材料的应力-应变图。
- 标注所有关键点：比例极限、弹性极限、屈服点、UTS、断裂应力。
- 当被要求“比较”两种材料时，使用比较性语言：“材料A的杨氏模量高于材料B”，“材料A比材料B更具延性。”
- 对于计算题，始终检查单位。应力单位为Pa（N/m²），应变无量纲。

---

## 4.3 Ductile Materials (e.g., Copper, Mild Steel) / 延性材料（例如铜、低碳钢）

### Explanation / 解释
**English:**
A **ductile material** can undergo significant plastic deformation before fracturing. This is due to the ability of dislocations to move easily through the crystal lattice. The stress-strain graph for a ductile material shows:
- A steep linear region (high [[Young Modulus]]).
- A clear yield point where the curve flattens.
- A long plastic region where the material "work hardens" (the stress increases again as dislocations become tangled).
- A peak at the UTS, followed by necking and a drop to the breaking stress.

Examples: Copper, aluminium, mild steel, gold.

**中文：**
**延性材料**在断裂前能经历显著的塑性形变。这是由于位错能够在晶格中轻松移动。延性材料的应力-应变图显示：
- 陡峭的线性区域（高[[杨氏模量]]）。
- 曲线变平的明显屈服点。
- 长的塑性区域，材料在此“加工硬化”（随着位错变得缠结，应力再次增加）。
- 在UTS处达到峰值，随后是颈缩并下降到断裂应力。

例子：铜、铝、低碳钢、金。

### Physical Meaning / 物理意义
**English:**
Ductile materials are used where large deformations are acceptable or desirable before failure. They give warning before breaking (e.g., a bent metal beam). They are also easy to form into wires or sheets.

**中文：**
延性材料用于在失效前可以接受或需要大变形的场合。它们在断裂前会发出警告（例如，弯曲的金属梁）。它们也易于加工成线材或板材。

### Common Misconceptions / 常见误区
1. **Misconception:** All metals are ductile.
   **Correction:** Cast iron is brittle. The ductility of a metal depends on its crystal structure and temperature.
2. **Misconception:** The yield point is always a sharp drop.
   **Correction:** Some ductile materials (e.g., aluminium) have a gradual yield point, not a sharp one.

### Exam Tips / 考试提示
**English:**
- Be able to describe the process of **necking**: after the UTS, the cross-sectional area decreases locally, so the engineering stress (force/original area) decreases, but the true stress (force/actual area) continues to increase.
- Know that the plastic region is associated with **dislocation movement**. Work hardening occurs because dislocations become entangled.

**中文：**
- 能够描述**颈缩**过程：在UTS之后，横截面积局部减小，因此工程应力（力/原始面积）减小，但真实应力（力/实际面积）继续增加。
- 知道塑性区域与**位错运动**有关。加工硬化发生是因为位错变得缠结。

---

## 4.4 Brittle Materials (e.g., Glass, Cast Iron) / 脆性材料（例如玻璃、铸铁）

### Explanation / 解释
**English:**
A **brittle material** fractures with little or no plastic deformation. This is because dislocations cannot move easily; cracks propagate rapidly through the material. The stress-strain graph for a brittle material shows:
- A steep linear region (high [[Young Modulus]]).
- No yield point.
- No plastic region.
- Fracture occurs suddenly at the breaking stress, which is also the UTS.

Examples: Glass, cast iron, ceramics, concrete (in tension).

**中文：**
**脆性材料**几乎没有或没有塑性形变就断裂。这是因为位错不能轻易移动；裂纹迅速在材料中扩展。脆性材料的应力-应变图显示：
- 陡峭的线性区域（高[[杨氏模量]]）。
- 没有屈服点。
- 没有塑性区域。
- 断裂在断裂应力处突然发生，该应力也是UTS。

例子：玻璃、铸铁、陶瓷、混凝土（受拉时）。

### Physical Meaning / 物理意义
**English:**
Brittle materials are strong in compression but weak in tension. They fail without warning, which can be dangerous. They are used where high compressive strength is needed (e.g., concrete pillars) but not where tensile or bending forces are present.

**中文：**
脆性材料抗压强度高，但抗拉强度低。它们在没有预警的情况下失效，这可能很危险。它们用于需要高抗压强度的场合（例如，混凝土柱），但不用于存在拉力或弯曲力的场合。

### Common Misconceptions / 常见误区
1. **Misconception:** Brittle materials are weak.
   **Correction:** Glass has a high compressive strength. It is weak in tension due to surface flaws.
2. **Misconception:** Brittle materials have a low Young modulus.
   **Correction:** Glass has a high Young modulus (~70 GPa). It is stiff but not tough.

### Exam Tips / 考试提示
**English:**
- The key phrase for brittle materials is "fractures with little or no plastic deformation."
- Explain that cracks propagate from surface flaws (Griffith's theory is not required at A-Level, but the concept is useful).
- Compare with ductile materials: "Brittle materials absorb less energy before fracturing, as shown by the smaller area under the stress-strain graph."

**中文：**
- 脆性材料的关键短语是“几乎没有或没有塑性形变就断裂。”
- 解释裂纹从表面缺陷扩展（A-Level不要求格里菲斯理论，但概念有用）。
- 与延性材料比较：“脆性材料在断裂前吸收的能量更少，如应力-应变图下较小的面积所示。”

---

## 4.5 Polymeric Materials (e.g., Rubber) / 聚合物材料（例如橡胶）

### Explanation / 解释
**English:**
A **polymeric material** is made of long-chain molecules that are tangled together. The stress-strain graph for a polymer like rubber is very different from metals:
- **Low Young Modulus:** The initial gradient is shallow.
- **Non-linear Elasticity:** The graph is curved, not straight. Rubber can undergo very large elastic strains (up to 500-800%).
- **Hysteresis:** The loading and unloading curves are different. The area between them represents energy dissipated as heat.
- **No clear yield point or plastic region:** Rubber is elastic until it breaks.
- **Stiffening at high strain:** The chains become aligned and the material becomes stiffer just before breaking.

Examples: Rubber, polythene, nylon.

**中文：**
**聚合物材料**由缠结在一起的长链分子组成。像橡胶这样的聚合物的应力-应变图与金属非常不同：
- **低杨氏模量：** 初始梯度较浅。
- **非线性弹性：** 图是弯曲的，不是直的。橡胶可以经历非常大的弹性应变（高达500-800%）。
- **滞后现象：** 加载和卸载曲线不同。它们之间的面积代表以热量形式耗散的能量。
- **没有明显的屈服点或塑性区域：** 橡胶在断裂前一直是弹性的。
- **高应变下变硬：** 链变得对齐，材料在断裂前变得更硬。

例子：橡胶、聚乙烯、尼龙。

### Physical Meaning / 物理意义
**English:**
Polymers are used where large elastic deformations are needed (e.g., rubber bands, tires, shock absorbers). The hysteresis loop means they are good at absorbing energy (damping).

**中文：**
聚合物用于需要大弹性形变的场合（例如，橡皮筋、轮胎、减震器）。滞后回线意味着它们善于吸收能量（阻尼）。

### Common Misconceptions / 常见误区
1. **Misconception:** Rubber obeys Hooke's Law.
   **Correction:** Rubber does not obey Hooke's Law. The stress-strain relationship is non-linear.
2. **Misconception:** All polymers are elastic.
   **Correction:** Some polymers (e.g., polythene) can undergo plastic deformation. The behaviour depends on the temperature and the polymer structure.
3. **Misconception:** The area under the loading curve equals the energy stored.
   **Correction:** The area under the loading curve is the energy put in. The area under the unloading curve is the energy returned. The difference is the energy dissipated.

### Exam Tips / 考试提示
**English:**
- Edexcel specifically requires you to "explain the behaviour of materials in terms of their atomic/molecular structure" (2.18). For polymers, explain that the long chains are tangled and uncoil when stretched, then recoil when released.
- Cambridge may ask you to "describe the stress-strain graph for a polymeric material." Mention the non-linear shape, the large strain, and the hysteresis loop.
- Be able to calculate the energy dissipated per cycle from the area of the hysteresis loop.

**中文：**
- 爱德思特别要求你“根据材料的原子/分子结构解释其行为”（2.18）。对于聚合物，解释长链是缠结的，拉伸时解开，释放时重新卷曲。
- 剑桥可能要求你“描述聚合物材料的应力-应变图。”提及非线性形状、大应变和滞后回线。
- 能够从滞后回线的面积计算每个循环耗散的能量。

---

## 4.6 Energy Stored per Unit Volume / 单位体积储存的能量

### Explanation / 解释
**English:**
The area under the stress-strain graph represents the **energy stored per unit volume** (also called the strain energy density). This is because:
- Work done = Force × displacement
- Stress = Force / Area
- Strain = displacement / Length
- Work done per unit volume = (Force × displacement) / (Area × Length) = Stress × Strain

For the linear elastic region, the area is a triangle:
$$ \text{Energy per unit volume} = \frac{1}{2} \sigma \epsilon $$

For a non-linear region, the energy is found by integration or by counting squares under the graph.

**中文：**
应力-应变图下的面积代表**单位体积储存的能量**（也称为应变能密度）。这是因为：
- 做功 = 力 × 位移
- 应力 = 力 / 面积
- 应变 = 位移 / 长度
- 单位体积做功 = (力 × 位移) / (面积 × 长度) = 应力 × 应变

对于线性弹性区域，面积是一个三角形：
$$ \text{单位体积能量} = \frac{1}{2} \sigma \epsilon $$

对于非线性区域，能量通过积分或计算图下的方格数来求得。

### Physical Meaning / 物理意义
**English:**
This concept tells us how much energy a material can absorb per unit volume before it breaks. This is a measure of **toughness**. A material with a large area under the graph (e.g., mild steel) is tough. A material with a small area (e.g., glass) is brittle.

**中文：**
这个概念告诉我们材料在断裂前每单位体积能吸收多少能量。这是**韧性**的量度。图下方面积大的材料（例如，低碳钢）是韧性的。面积小的材料（例如，玻璃）是脆性的。

### Common Misconceptions / 常见误区
1. **Misconception:** The area under the graph is the total energy stored.
   **Correction:** The area is the energy per unit volume. Total energy = area × volume of the sample.
2. **Misconception:** The area under the load-extension graph is the same as the area under the stress-strain graph.
   **Correction:** They are related but not the same. Area under load-extension = total energy. Area under stress-strain = energy per unit volume.

### Exam Tips / 考试提示
**English:**
- For the linear region, use the formula $E = \frac{1}{2} F \Delta L$ for total energy, or $\frac{1}{2} \sigma \epsilon$ for energy per unit volume.
- For non-linear regions, you may be asked to estimate the area by counting squares or using the trapezium rule.
- Edexcel and Cambridge both ask: "Use the stress-strain graph to determine the energy stored per unit volume." Show your working clearly.

**中文：**
- 对于线性区域，使用公式 $E = \frac{1}{2} F \Delta L$ 计算总能量，或 $\frac{1}{2} \sigma \epsilon$ 计算单位体积能量。
- 对于非线性区域，你可能被要求通过数方格或使用梯形法则来估算面积。
- 爱德思和剑桥都问：“使用应力-应变图确定单位体积储存的能量。”清晰地展示你的计算过程。

---

# 5. Essential Equations / 核心公式

## 5.1 Young Modulus / 杨氏模量

**Equation / 公式:**
$$ E = \frac{\sigma}{\epsilon} = \frac{F/A}{\Delta L / L} = \frac{FL}{A\Delta L} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Young Modulus | 杨氏模量 | Pa (N/m²) |
| $\sigma$ | Tensile Stress | 拉应力 | Pa (N/m²) |
| $\epsilon$ | Tensile Strain | 拉应变 | dimensionless (无量纲) |
| $F$ | Force | 力 | N |
| $A$ | Cross-sectional Area | 横截面积 | m² |
| $L$ | Original Length | 原始长度 | m |
| $\Delta L$ | Extension | 伸长量 | m |

**Derivation / 推导:**
**English:**
The Young Modulus is defined as the ratio of tensile stress to tensile strain within the limit of proportionality. It is a measure of the stiffness of a material. The derivation comes from combining the definitions of stress ($\sigma = F/A$) and strain ($\epsilon = \Delta L/L$):
$$ E = \frac{\sigma}{\epsilon} = \frac{F/A}{\Delta L/L} = \frac{FL}{A\Delta L} $$

**中文：**
杨氏模量定义为比例极限内拉应力与拉应变之比。它是材料刚度的量度。推导来自结合应力（$\sigma = F/A$）和应变（$\epsilon = \Delta L/L$）的定义：
$$ E = \frac{\sigma}{\epsilon} = \frac{F/A}{\Delta L/L} = \frac{FL}{A\Delta L} $$

**Conditions / 适用条件:**
**English:**
- The material must be within its **limit of proportionality** (linear elastic region).
- The material must be **homogeneous** and **isotropic** (same properties in all directions).
- The deformation must be **uniaxial** (force applied along one axis only).

**中文：**
- 材料必须在其**比例极限**内（线性弹性区域）。
- 材料必须是**均匀的**和**各向同性的**（所有方向上的性质相同）。
- 形变必须是**单轴的**（力仅沿一个轴施加）。

**Limitations / 局限性:**
**English:**
- Cannot be used for non-linear materials like rubber.
- Cannot be used beyond the limit of proportionality.
- Assumes the cross-sectional area remains constant (which is not true for large strains).

**中文：**
- 不能用于像橡胶这样的非线性材料。
- 不能用于超过比例极限。
- 假设横截面积保持不变（对于大应变这不成立）。

**Rearrangements / 变形:**
**English:**
- To find force: $F = \frac{EA\Delta L}{L}$
- To find extension: $\Delta L = \frac{FL}{EA}$
- To find area: $A = \frac{FL}{E\Delta L}$

**中文：**
- 求力：$F = \frac{EA\Delta L}{L}$
- 求伸长量：$\Delta L = \frac{FL}{EA}$
- 求面积：$A = \frac{FL}{E\Delta L}$

---

## 5.2 Energy Stored per Unit Volume / 单位体积储存的能量

**Equation / 公式:**
$$ \text{Energy per unit volume} = \frac{1}{2} \sigma \epsilon \quad \text{(for linear elastic region)} $$
$$ \text{Total energy stored} = \frac{1}{2} F \Delta L \quad \text{(for linear elastic region)} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\sigma$ | Stress | 应力 | Pa |
| $\epsilon$ | Strain | 应变 | dimensionless |
| $F$ | Force | 力 | N |
| $\Delta L$ | Extension | 伸长量 | m |

**Derivation / 推导:**
**English:**
Work done = average force × displacement. For a linear elastic material, force is proportional to extension ($F = k\Delta L$). The average force is $\frac{1}{2}F_{max}$.
$$ \text{Work done} = \frac{1}{2} F_{max} \Delta L $$
To find energy per unit volume:
$$ \text{Energy per unit volume} = \frac{\text{Work done}}{\text{Volume}} = \frac{\frac{1}{2} F \Delta L}{A L} = \frac{1}{2} \left(\frac{F}{A}\right) \left(\frac{\Delta L}{L}\right) = \frac{1}{2} \sigma \epsilon $$

**中文：**
做功 = 平均力 × 位移。对于线性弹性材料，力与伸长量成正比（$F = k\Delta L$）。平均力是 $\frac{1}{2}F_{max}$。
$$ \text{做功} = \frac{1}{2} F_{max} \Delta L $$
求单位体积能量：
$$ \text{单位体积能量} = \frac{\text{做功}}{\text{体积}} = \frac{\frac{1}{2} F \Delta L}{A L} = \frac{1}{2} \left(\frac{F}{A}\right) \left(\frac{\Delta L}{L}\right) = \frac{1}{2} \sigma \epsilon $$

**Conditions / 适用条件:**
**English:**
- Only applies to the **linear elastic region** (within the limit of proportionality).
- The material must obey [[Hooke's Law]].

**中文：**
- 仅适用于**线性弹性区域**（在比例极限内）。
- 材料必须遵守[[胡克定律]]。

**Limitations / 局限性:**
**English:**
- Cannot be used for non-linear materials.
- Cannot be used beyond the limit of proportionality.
- For non-linear regions, the area under the graph must be found by integration or counting squares.

**中文：**
- 不能用于非线性材料。
- 不能用于超过比例极限。
- 对于非线性区域，必须通过积分或数方格来求图下方面积。

**Rearrangements / 变形:**
**English:**
- Using [[Young Modulus]]: $\text{Energy per unit volume} = \frac{1}{2} E \epsilon^2 = \frac{\sigma^2}{2E}$
- Total energy: $E_{total} = \frac{1}{2} \sigma \epsilon \times \text{Volume}$

**中文：**
- 使用[[杨氏模量]]：$\text{单位体积能量} = \frac{1}{2} E \epsilon^2 = \frac{\sigma^2}{2E}$
- 总能量：$E_{total} = \frac{1}{2} \sigma \epsilon \times \text{体积}$

---

## 5.3 Stress and Strain Definitions / 应力和应变定义

**Equation / 公式:**
$$ \sigma = \frac{F}{A} $$
$$ \epsilon = \frac{\Delta L}{L} $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\sigma$ | Tensile Stress | 拉应力 | Pa (N/m²) |
| $F$ | Force | 力 | N |
| $A$ | Cross-sectional Area | 横截面积 | m² |
| $\epsilon$ | Tensile Strain | 拉应变 | dimensionless (无量纲) |
| $\Delta L$ | Extension | 伸长量 | m |
| $L$ | Original Length | 原始长度 | m |

**Derivation / 推导:**
**English:**
These are definitional equations. Stress is defined as force per unit cross-sectional area. Strain is defined as the fractional change in length. They are not derived from other equations.

**中文：**
这些是定义性方程。应力定义为单位横截面积上的力。应变定义为长度的相对变化。它们不是从其他方程推导出来的。

**Conditions / 适用条件:**
**English:**
- Stress assumes the force is applied perpendicular to the cross-sectional area.
- Strain assumes the deformation is uniform along the length.

**中文：**
- 应力假设力垂直于横截面积施加。
- 应变假设形变沿长度均匀。

**Limitations / 局限性:**
**English:**
- Engineering stress uses the original area, which becomes inaccurate for large plastic deformations where necking occurs.
- True stress uses the actual area at the point of measurement.

**中文：**
- 工程应力使用原始面积，这对于发生颈缩的大塑性形变变得不准确。
- 真实应力使用测量点的实际面积。

**Rearrangements / 变形:**
**English:**
- Force: $F = \sigma A$
- Area: $A = F / \sigma$
- Extension: $\Delta L = \epsilon L$
- Original length: $L = \Delta L / \epsilon$

**中文：**
- 力：$F = \sigma A$
- 面积：$A = F / \sigma$
- 伸长量：$\Delta L = \epsilon L$
- 原始长度：$L = \Delta L / \epsilon$

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Stress-Strain Graph for a Ductile Material / 延性材料的应力-应变图

### Axes / 坐标轴
**English:** y-axis: Stress ($\sigma$ / Pa); x-axis: Strain ($\epsilon$ / dimensionless)
**中文：** y轴：应力（$\sigma$ / Pa）；x轴：应变（$\epsilon$ / 无量纲）

### Shape / 形状
**English:** A steep straight line from the origin (linear elastic region), followed by a curve that flattens at the yield point, rises gradually (work hardening), peaks at the UTS, then drops slightly before fracture.
**中文：** 从原点开始的陡峭直线（线性弹性区域），随后是在屈服点变平的曲线，逐渐上升（加工硬化），在UTS处达到峰值，然后在断裂前略微下降。

### Gradient Meaning / 斜率含义
**English:** The gradient of the linear region is the [[Young Modulus]] ($E$). A steeper gradient means a stiffer material.
**中文：** 线性区域的斜率是[[杨氏模量]]（$E$）。斜率越陡，材料越硬。

### Area Meaning / 面积含义
**English:** The total area under the graph up to the fracture point represents the **energy absorbed per unit volume** before fracture (toughness).
**中文：** 直到断裂点的图下总面代表断裂前**单位体积吸收的能量**（韧性）。

### Exam Interpretation / 考试解读
**English:**
- Identify the limit of proportionality (end of straight line).
- Identify the yield point (where the curve first flattens).
- Identify the UTS (highest point on the curve).
- Identify the breaking stress (point of fracture).
- Compare with other materials: "This material is more ductile because it has a longer plastic region."

**中文：**
- 识别比例极限（直线结束处）。
- 识别屈服点（曲线首次变平处）。
- 识别UTS（曲线最高点）。
- 识别断裂应力（断裂点）。
- 与其他材料比较：“这种材料更具延性，因为它有更长的塑性区域。”

### Common Questions / 常见问题
**English:**
- "Sketch the stress-strain graph for a ductile material and label the key points."
- "Explain why the stress decreases after the UTS."
- "Calculate the Young modulus from the graph."

**中文：**
- “绘制延性材料的应力-应变图并标注关键点。”
- “解释为什么应力在UTS后下降。”
- “从图中计算杨氏模量。”

---

## 6.2 Stress-Strain Graph for a Brittle Material / 脆性材料的应力-应变图

### Axes / 坐标轴
**English:** y-axis: Stress ($\sigma$ / Pa); x-axis: Strain ($\epsilon$ / dimensionless)
**中文：** y轴：应力（$\sigma$ / Pa）；x轴：应变（$\epsilon$ / 无量纲）

### Shape / 形状
**English:** A steep straight line from the origin, ending abruptly at the fracture point. There is no yield point, no plastic region, and no necking.
**中文：** 从原点开始的陡峭直线，在断裂点突然结束。没有屈服点，没有塑性区域，也没有颈缩。

### Gradient Meaning / 斜率含义
**English:** The gradient is the [[Young Modulus]] ($E$). Brittle materials like glass have a high Young modulus.
**中文：** 斜率是[[杨氏模量]]（$E$）。像玻璃这样的脆性材料具有高杨氏模量。

### Area Meaning / 面积含义
**English:** The area under the graph is very small, indicating that brittle materials absorb very little energy before fracturing (low toughness).
**中文：** 图下方面积非常小，表明脆性材料在断裂前吸收的能量非常少（低韧性）。

### Exam Interpretation / 考试解读
**English:**
- Note the absence of a plastic region.
- The breaking stress is the same as the UTS (no necking).
- Compare with ductile materials: "This material is brittle because it fractures with little or no plastic deformation."

**中文：**
- 注意没有塑性区域。
- 断裂应力与UTS相同（无颈缩）。
- 与延性材料比较：“这种材料是脆性的，因为它几乎没有或没有塑性形变就断裂了。”

### Common Questions / 常见问题
**English:**
- "Sketch the stress-strain graph for a brittle material."
- "Explain why brittle materials are dangerous in structural applications."
- "Compare the stress-strain graphs for glass and copper."

**中文：**
- “绘制脆性材料的应力-应变图。”
- “解释为什么脆性材料在结构应用中很危险。”
- “比较玻璃和铜的应力-应变图。”

---

## 6.3 Stress-Strain Graph for a Polymeric Material (Rubber) / 聚合物材料（橡胶）的应力-应变图

### Axes / 坐标轴
**English:** y-axis: Stress ($\sigma$ / Pa); x-axis: Strain ($\epsilon$ / dimensionless)
**中文：** y轴：应力（$\sigma$ / Pa）；x轴：应变（$\epsilon$ / 无量纲）

### Shape / 形状
**English:** A non-linear curve. The initial gradient is shallow (low [[Young Modulus]]). The curve becomes steeper at high strains (stiffening). The loading and unloading curves are different, forming a **hysteresis loop**.
**中文：** 非线性曲线。初始梯度较浅（低[[杨氏模量]]）。曲线在高应变下变得更陡（变硬）。加载和卸载曲线不同，形成**滞后回线**。

### Gradient Meaning / 斜率含义
**English:** The gradient is not constant. The initial gradient is the initial Young modulus. The gradient increases as the polymer chains become aligned.
**中文：** 斜率不是常数。初始梯度是初始杨氏模量。随着聚合物链变得对齐，斜率增加。

### Area Meaning / 面积含义
**English:** The area under the loading curve is the energy put in. The area under the unloading curve is the energy returned. The area of the hysteresis loop (between the two curves) is the **energy dissipated as heat** per cycle.
**中文：** 加载曲线下的面积是输入的能量。卸载曲线下的面积是返回的能量。滞后回线（两条曲线之间）的面积是每个循环**以热量形式耗散的能量**。

### Exam Interpretation / 考试解读
**English:**
- Note the non-linear relationship (does not obey [[Hooke's Law]]).
- Note the large strain (can stretch to several times its original length).
- The hysteresis loop shows that rubber is good at absorbing energy (damping).

**中文：**
- 注意非线性关系（不遵守[[胡克定律]]）。
- 注意大应变（可以拉伸到原始长度的数倍）。
- 滞后回线表明橡胶善于吸收能量（阻尼）。

### Common Questions / 常见问题
**English:**
- "Sketch the stress-strain graph for rubber and explain its shape."
- "Explain what is meant by a hysteresis loop."
- "Calculate the energy dissipated per cycle from the area of the hysteresis loop."

**中文：**
- “绘制橡胶的应力-应变图并解释其形状。”
- “解释滞后回线的含义。”
- “从滞后回线的面积计算每个循环耗散的能量。”

---

## 6.4 Load-Extension Graph vs. Stress-Strain Graph / 载荷-伸长图与应力-应变图

### Axes / 坐标轴
**English:**
- Load-Extension: y-axis = Load (F / N), x-axis = Extension ($\Delta L$ / m)
- Stress-Strain: y-axis = Stress ($\sigma$ / Pa), x-axis = Strain ($\epsilon$ / dimensionless)

**中文：**
- 载荷-伸长：y轴 = 载荷（F / N），x轴 = 伸长量（$\Delta L$ / m）
- 应力-应变：y轴 = 应力（$\sigma$ / Pa），x轴 = 应变（$\epsilon$ / 无量纲）

### Shape / 形状
**English:** The shapes are identical for a given material because stress is proportional to load (for constant area) and strain is proportional to extension (for constant length).
**中文：** 对于给定材料，形状相同，因为应力与载荷成正比（面积恒定），应变与伸长量成正比（长度恒定）。

### Gradient Meaning / 斜率含义
**English:**
- Load-Extension: Gradient = spring constant ($k = F/\Delta L$)
- Stress-Strain: Gradient = [[Young Modulus]] ($E = \sigma/\epsilon$)

**中文：**
- 载荷-伸长：斜率 = 弹簧常数（$k = F/\Delta L$）
- 应力-应变：斜率 = [[杨氏模量]]（$E = \sigma/\epsilon$）

### Area Meaning / 面积含义
**English:**
- Load-Extension: Area = total energy stored ($\frac{1}{2}F\Delta L$)
- Stress-Strain: Area = energy stored per unit volume ($\frac{1}{2}\sigma\epsilon$)

**中文：**
- 载荷-伸长：面积 = 储存的总能量（$\frac{1}{2}F\Delta L$）
- 应力-应变：面积 = 单位体积储存的能量（$\frac{1}{2}\sigma\epsilon$）

### Exam Interpretation / 考试解读
**English:**
- You may be asked to convert between the two graphs.
- To convert load to stress: $\sigma = F/A$
- To convert extension to strain: $\epsilon = \Delta L/L$

**中文：**
- 你可能被要求在两种图之间进行转换。
- 将载荷转换为应力：$\sigma = F/A$
- 将伸长量转换为应变：$\epsilon = \Delta L/L$

### Common Questions / 常见问题
**English:**
- "Explain why the load-extension graph and stress-strain graph have the same shape."
- "A wire of length 2.0 m and cross-sectional area 0.5 mm² is stretched. The load-extension graph is given. Plot the stress-strain graph."

**中文：**
- “解释为什么载荷-伸长图和应力-应变图具有相同的形状。”
- “一根长度为2.0米、横截面积为0.5平方毫米的金属丝被拉伸。给出了载荷-伸长图。绘制应力-应变图。”

---

# 7. Required Diagrams / 必备图表

## 7.1 Stress-Strain Graph for a Ductile Material (Copper) / 延性材料（铜）的应力-应变图

### Description / 描述
**English:** A fully labelled stress-strain graph for a typical ductile material like copper. The graph shows a linear region from the origin to the limit of proportionality, followed by a curved elastic region to the elastic limit, a yield point where the curve flattens, a long plastic region with work hardening rising to the ultimate tensile strength (UTS), and finally necking and fracture at the breaking stress. All key points are labelled.

**中文：** 一个完全标注的典型延性材料（如铜）的应力-应变图。该图显示从原点到比例极限的线性区域，随后是到弹性极限的弯曲弹性区域，曲线变平的屈服点，具有加工硬化的长塑性区域上升到极限抗拉强度（UTS），最后是颈缩和在断裂应力处断裂。所有关键点都已标注。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — D01: Stress-Strain Graph for Ductile Material (Copper)**
>
> A clean, textbook-style 2D line graph on a white background. The y-axis is labelled "Stress σ / Pa" and the x-axis is labelled "Strain ε". The curve starts at the origin (0,0) with a steep straight line. The line then curves slightly, flattens into a plateau (yield point), rises gradually with a positive slope (work hardening), reaches a peak (UTS), and then drops slightly before ending at the fracture point. The following points are clearly marked with arrows and labels: "Limit of Proportionality", "Elastic Limit", "Yield Point", "Ultimate Tensile Strength (UTS)", "Breaking Stress". The regions are labelled: "Elastic Region", "Plastic Region", "Necking". The graph should be in high contrast (black line on white) with a sans-serif font for labels. Style: educational diagram, precise, clean, no grid lines.

### Labels Required / 需要标注
**English:**
- Axes: Stress (σ / Pa), Strain (ε)
- Points: Limit of Proportionality, Elastic Limit, Yield Point, UTS, Breaking Stress
- Regions: Elastic Region, Plastic Region, Necking

**中文：**
- 坐标轴：应力（σ / Pa），应变（ε）
- 点：比例极限，弹性极限，屈服点，UTS，断裂应力
- 区域：弹性区域，塑性区域，颈缩

### Exam Importance / 考试重要性
**English:**
This is the most important diagram in the topic. Students must be able to sketch it from memory and label all key points. It is used in almost every exam paper on materials.

**中文：**
这是本主题中最重要的图表。学生必须能够凭记忆绘制它并标注所有关键点。它几乎出现在每份关于材料的试卷中。

---

## 7.2 Stress-Strain Graph for a Brittle Material (Glass) / 脆性材料（玻璃）的应力-应变图

### Description / 描述
**English:** A fully labelled stress-strain graph for a typical brittle material like glass. The graph shows a steep straight line from the origin to the fracture point. There is no yield point, no plastic region, and no necking. The fracture point is labelled as both the "Ultimate Tensile Strength (UTS)" and "Breaking Stress" because they are the same.

**中文：** 一个完全标注的典型脆性材料（如玻璃）的应力-应变图。该图显示从原点到断裂点的陡峭直线。没有屈服点，没有塑性区域，也没有颈缩。断裂点被标注为“极限抗拉强度（UTS）”和“断裂应力”，因为它们是相同的。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — D02: Stress-Strain Graph for Brittle Material (Glass)**
>
> A clean, textbook-style 2D line graph on a white background. The y-axis is labelled "Stress σ / Pa" and the x-axis is labelled "Strain ε". The curve is a single straight line starting from the origin (0,0) with a steep positive slope. The line ends abruptly at a point labelled "Fracture Point / UTS / Breaking Stress". There is no curvature, no plateau, and no drop. The region under the line is labelled "Elastic Region". The graph should be in high contrast (black line on white) with a sans-serif font for labels. Style: educational diagram, precise, clean, no grid lines.

### Labels Required / 需要标注
**English:**
- Axes: Stress (σ / Pa), Strain (ε)
- Point: Fracture Point / UTS / Breaking Stress
- Region: Elastic Region

**中文：**
- 坐标轴：应力（σ / Pa），应变（ε）
- 点：断裂点 / UTS / 断裂应力
- 区域：弹性区域

### Exam Importance / 考试重要性
**English:**
This diagram is used to contrast with ductile materials. Students must be able to explain why there is no plastic region and why brittle materials are dangerous in tension.

**中文：**
该图用于与延性材料进行对比。学生必须能够解释为什么没有塑性区域，以及为什么脆性材料在拉伸时很危险。

---

## 7.3 Stress-Strain Graph for a Polymeric Material (Rubber) with Hysteresis Loop / 聚合物材料（橡胶）的应力-应变图及滞后回线

### Description / 描述
**English:** A fully labelled stress-strain graph for a typical polymeric material like rubber. The graph shows a non-linear loading curve and a non-linear unloading curve that is different from the loading curve, forming a hysteresis loop. The loading curve starts with a shallow gradient, becomes steeper at high strains, and ends at the breaking point. The unloading curve lies below the loading curve. The area between them is labelled "Energy Dissipated as Heat".

**中文：** 一个完全标注的典型聚合物材料（如橡胶）的应力-应变图。该图显示一条非线性加载曲线和一条与加载曲线不同的非线性卸载曲线，形成一个滞后回线。加载曲线从浅梯度开始，在高应变下变得更陡，并在断裂点结束。卸载曲线位于加载曲线下方。它们之间的面积被标注为“以热量形式耗散的能量”。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — D03: Stress-Strain Graph for Rubber with Hysteresis Loop**
>
> A clean, textbook-style 2D line graph on a white background. The y-axis is labelled "Stress σ / Pa" and the x-axis is labelled "Strain ε". The loading curve (solid line) starts at the origin (0,0) with a shallow curve, then becomes steeper, and ends at a point labelled "Breaking Point". The unloading curve (dashed line) starts at the breaking point and curves downwards, ending at the origin (showing no permanent deformation). The loading and unloading curves are different, creating a loop. The area inside the loop is shaded and labelled "Energy Dissipated as Heat". The graph should be in high contrast (black line on white) with a sans-serif font for labels. Style: educational diagram, precise, clean, no grid lines.

### Labels Required / 需要标注
**English:**
- Axes: Stress (σ / Pa), Strain (ε)
- Curves: Loading Curve, Unloading Curve
- Point: Breaking Point
- Area: Energy Dissipated as Heat (Hysteresis Loop)

**中文：**
- 坐标轴：应力（σ / Pa），应变（ε）
- 曲线：加载曲线，卸载曲线
- 点：断裂点
- 面积：以热量形式耗散的能量（滞后回线）

### Exam Importance / 考试重要性
**English:**
This diagram is specific to polymeric materials. Edexcel specifically requires students to explain the behaviour of polymers in terms of their molecular structure. The hysteresis loop is a key feature.

**中文：**
该图是聚合物材料特有的。爱德思特别要求学生根据分子结构解释聚合物的行为。滞后回线是一个关键特征。

---

## 7.4 Comparison of Stress-Strain Graphs for Three Material Types / 三种材料类型的应力-应变图比较

### Description / 描述
**English:** A single graph showing three curves on the same axes: a ductile material (copper), a brittle material (glass), and a polymeric material (rubber). The curves are clearly distinguished by colour or line style. The key differences in shape, gradient, and area are visible.

**中文：** 一个在同一坐标轴上显示三条曲线的图：延性材料（铜）、脆性材料（玻璃）和聚合物材料（橡胶）。曲线通过颜色或线型清晰区分。形状、梯度和面积的关键差异是可见的。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — D04: Comparison of Stress-Strain Graphs for Ductile, Brittle, and Polymeric Materials**
>
> A clean, textbook-style 2D line graph on a white background. The y-axis is labelled "Stress σ / Pa" and the x-axis is labelled "Strain ε". Three curves are plotted on the same axes:
> 1. **Ductile (Copper):** Solid blue line. Steep straight line, then plateau, then gradual rise to a peak, then slight drop before fracture. Long curve.
> 2. **Brittle (Glass):** Dashed red line. Steep straight line ending abruptly at a low strain. Short curve.
> 3. **Polymeric (Rubber):** Dotted green line. Shallow curve that becomes steeper, ending at a very high strain. Very long curve.
> A legend is included in the top right corner. The graph should be in high contrast with a sans-serif font for labels. Style: educational diagram, precise, clean, no grid lines.

### Labels Required / 需要标注
**English:**
- Axes: Stress (σ / Pa), Strain (ε)
- Curves: Ductile (Copper), Brittle (Glass), Polymeric (Rubber)
- Legend

**中文：**
- 坐标轴：应力（σ / Pa），应变（ε）
- 曲线：延性（铜），脆性（玻璃），聚合物（橡胶）
- 图例

### Exam Importance / 考试重要性
**English:**
This comparison graph is frequently used in exam questions. Students must be able to identify which curve corresponds to which material type and explain the differences.

**中文：**
这个比较图经常在考试题中使用。学生必须能够识别哪条曲线对应哪种材料类型，并解释差异。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Young Modulus and Energy Stored from a Stress-Strain Graph / 从应力-应变图计算杨氏模量和储存的能量

### Question / 题目
**English:**
A copper wire of original length 2.50 m and cross-sectional area $1.20 \times 10^{-6} \text{ m}^2$ is stretched. The stress-strain graph for the wire is shown below. The linear region of the graph passes through the point (strain = 0.0010, stress = $1.10 \times 10^8 \text{ Pa}$).

(a) Calculate the [[Young Modulus]] of copper.
(b) Calculate the energy stored per unit volume in the wire when the strain is 0.0010.
(c) Calculate the total energy stored in the wire at this strain.

**中文：**
一根铜丝，原始长度为2.50米，横截面积为$1.20 \times 10^{-6} \text{ m}^2$，被拉伸。该金属丝的应力-应变图如下所示。图的线性区域通过点（应变 = 0.0010，应力 = $1.10 \times 10^8 \text{ Pa}$）。

(a) 计算铜的[[杨氏模量]]。
(b) 计算当应变为0.0010时，金属丝中单位体积储存的能量。
(c) 计算在此应变下金属丝中储存的总能量。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — E01: Stress-Strain Graph for Copper Wire**
>
> A simple stress-strain graph for copper. The y-axis is labelled "Stress σ / 10^8 Pa" and the x-axis is labelled "Strain ε / 10^-3". The graph shows a straight line from the origin to the point (1.0, 1.1). The point is marked with a dot. No other features are shown. Style: clean, educational, black line on white.

### Solution / 解答

**Step 1: Calculate the Young Modulus (Part a)**
**English:**
The Young Modulus is the gradient of the linear region of the stress-strain graph.
$$ E = \frac{\sigma}{\epsilon} = \frac{1.10 \times 10^8}{0.0010} = 1.10 \times 10^{11} \text{ Pa} $$

**中文：**
杨氏模量是应力-应变图线性区域的斜率。
$$ E = \frac{\sigma}{\epsilon} = \frac{1.10 \times 10^8}{0.0010} = 1.10 \times 10^{11} \text{ Pa} $$

**Step 2: Calculate the energy stored per unit volume (Part b)**
**English:**
For the linear elastic region, the energy stored per unit volume is:
$$ \text{Energy per unit volume} = \frac{1}{2} \sigma \epsilon = \frac{1}{2} \times (1.10 \times 10^8) \times (0.0010) $$
$$ = \frac{1}{2} \times 1.10 \times 10^5 = 5.50 \times 10^4 \text{ J/m}^3 $$

**中文：**
对于线性弹性区域，单位体积储存的能量为：
$$ \text{单位体积能量} = \frac{1}{2} \sigma \epsilon = \frac{1}{2} \times (1.10 \times 10^8) \times (0.0010) $$
$$ = \frac{1}{2} \times 1.10 \times 10^5 = 5.50 \times 10^4 \text{ J/m}^3 $$

**Step 3: Calculate the total energy stored (Part c)**
**English:**
First, calculate the volume of the wire:
$$ V = A \times L = (1.20 \times 10^{-6}) \times 2.50 = 3.00 \times 10^{-6} \text{ m}^3 $$
Then, total energy = energy per unit volume × volume:
$$ E_{total} = (5.50 \times 10^4) \times (3.00 \times 10^{-6}) = 0.165 \text{ J} $$

**中文：**
首先，计算金属丝的体积：
$$ V = A \times L = (1.20 \times 10^{-6}) \times 2.50 = 3.00 \times 10^{-6} \text{ m}^3 $$
然后，总能量 = 单位体积能量 × 体积：
$$ E_{total} = (5.50 \times 10^4) \times (3.00 \times 10^{-6}) = 0.165 \text{ J} $$

### Final Answer / 最终答案
**Answer:**
(a) $E = 1.10 \times 10^{11} \text{ Pa}$
(b) Energy per unit volume = $5.50 \times 10^4 \text{ J/m}^3$
(c) Total energy = $0.165 \text{ J}$

**答案：**
(a) $E = 1.10 \times 10^{11} \text{ Pa}$
(b) 单位体积能量 = $5.50 \times 10^4 \text{ J/m}^3$
(c) 总能量 = $0.165 \text{ J}$

### Examiner Notes / 考官点评
**English:**
- **Common mistake:** Forgetting to convert units. Ensure area is in m², length in m.
- **Common mistake:** Using the formula for total energy ($\frac{1}{2}F\Delta L$) without calculating force and extension first. The stress-strain method is more direct.
- **Mark scheme:** Part (a) 2 marks (1 for correct substitution, 1 for correct answer with unit). Part (b) 2 marks. Part (c) 2 marks (1 for volume, 1 for total energy).
- **Tip:** Always show your working. If you make a numerical error, you may still get method marks.

**中文：**
- **常见错误：** 忘记转换单位。确保面积单位为m²，长度单位为m。
- **常见错误：** 使用总能量公式（$\frac{1}{2}F\Delta L$）而不先计算力和伸长量。应力-应变方法更直接。
- **评分方案：** 第(a)部分2分（1分正确代入，1分正确答案及单位）。第(b)部分2分。第(c)部分2分（1分体积，1分总能量）。
- **提示：** 始终展示你的计算过程。如果你犯了数值错误，你仍然可能获得方法分。

---

## Example 2: Comparing Ductile and Brittle Materials / 比较延性材料和脆性材料

### Question / 题目
**English:**
Two materials, P and Q, are tested to failure. The stress-strain graphs are shown below.

Material P: A steep straight line from the origin to a strain of 0.002, then a long curved region reaching a maximum stress of $4.0 \times 10^8 \text{ Pa}$ at a strain of 0.20, followed by a drop to fracture at a strain of 0.25.

Material Q: A steep straight line from the origin to a strain of 0.002, then fracture at a stress of $3.0 \times 10^8 \text{ Pa}$.

(a) Identify which material is ductile and which is brittle. Explain your reasoning.
(b) Calculate the [[Young Modulus]] for both materials.
(c) Which material is tougher? Explain your answer.

**中文：**
两种材料P和Q被测试至失效。应力-应变图如下所示。

材料P：从原点到应变为0.002的陡峭直线，然后是一个长的弯曲区域，在应变为0.20时达到最大应力$4.0 \times 10^8 \text{ Pa}$，随后下降至应变为0.25时断裂。

材料Q：从原点到应变为0.002的陡峭直线，然后在应力为$3.0 \times 10^8 \text{ Pa}$时断裂。

(a) 识别哪种材料是延性的，哪种是脆性的。解释你的推理。
(b) 计算两种材料的[[杨氏模量]]。
(c) 哪种材料更具韧性？解释你的答案。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — E02: Comparison of Stress-Strain Graphs for Materials P and Q**
>
> Two stress-strain graphs on the same axes. The y-axis is labelled "Stress σ / 10^8 Pa" and the x-axis is labelled "Strain ε". Graph P (solid blue line) shows a steep straight line, then a long curved region peaking at (0.20, 4.0) and dropping to (0.25, 3.5). Graph Q (dashed red line) shows a steep straight line ending abruptly at (0.002, 3.0). A legend is included. Style: clean, educational, black line on white.

### Solution / 解答

**Step 1: Identify ductile and brittle materials (Part a)**
**English:**
- **Material P is ductile.** It undergoes significant plastic deformation (strain from 0.002 to 0.25) before fracturing. It has a clear yield point, UTS, and necking region.
- **Material Q is brittle.** It fractures with no plastic deformation. The graph is a straight line ending abruptly at the fracture point.

**中文：**
- **材料P是延性的。** 它在断裂前经历了显著的塑性形变（应变从0.002到0.25）。它有明显的屈服点、UTS和颈缩区域。
- **材料Q是脆性的。** 它没有塑性形变就断裂了。该图是一条在断裂点突然结束的直线。

**Step 2: Calculate the Young Modulus (Part b)**
**English:**
Both materials have the same gradient in the linear region (strain = 0.002, stress = ?).
For Material P, the linear region ends at strain = 0.002. We need the stress at this point. From the description, the linear region is steep. We can assume the stress at the end of the linear region is proportional. However, we are not given the stress at strain = 0.002 for Material P. We can only calculate the gradient from the given data.

For Material Q, the linear region ends at fracture: stress = $3.0 \times 10^8 \text{ Pa}$, strain = 0.002.
$$ E_Q = \frac{\sigma}{\epsilon} = \frac{3.0 \times 10^8}{0.002} = 1.5 \times 10^{11} \text{ Pa} $$

For Material P, we need the stress at the limit of proportionality. The description says "a steep straight line from the origin to a strain of 0.002". This implies the stress at strain = 0.002 is the stress at the limit of proportionality. However, the value is not given. We can infer it from the shape. Since both materials have a "steep straight line" to the same strain, we can assume they have the same Young modulus. Therefore:
$$ E_P = 1.5 \times 10^{11} \text{ Pa} $$

**中文：**
两种材料在线性区域具有相同的梯度（应变 = 0.002，应力 = ?）。
对于材料P，线性区域在应变 = 0.002处结束。我们需要该点的应力。根据描述，线性区域是陡峭的。我们可以假设线性区域结束时的应力是成比例的。然而，我们没有得到材料P在应变 = 0.002时的应力。我们只能从给定数据计算梯度。

对于材料Q，线性区域在断裂处结束：应力 = $3.0 \times 10^8 \text{ Pa}$，应变 = 0.002。
$$ E_Q = \frac{\sigma}{\epsilon} = \frac{3.0 \times 10^8}{0.002} = 1.5 \times 10^{11} \text{ Pa} $$

对于材料P，我们需要比例极限处的应力。描述说“从原点到应变为0.002的陡峭直线”。这意味着应变为0.002时的应力是比例极限处的应力。然而，没有给出数值。我们可以从形状推断。由于两种材料都具有到相同应变的“陡峭直线”，我们可以假设它们具有相同的杨氏模量。因此：
$$ E_P = 1.5 \times 10^{11} \text{ Pa} $$

**Step 3: Determine which material is tougher (Part c)**
**English:**
**Toughness** is the ability to absorb energy before fracturing. It is measured by the area under the stress-strain graph.

- **Material P:** The area under the graph is large because it has a long plastic region. The area includes the triangle under the linear region plus the area under the curved plastic region. This is a large area.
- **Material Q:** The area under the graph is just the triangle under the linear region. This is a very small area.

Therefore, **Material P is tougher** because it absorbs more energy per unit volume before fracturing.

**中文：**
**韧性**是材料在断裂前吸收能量的能力。它由应力-应变图下的面积衡量。

- **材料P：** 图下方面积很大，因为它有长的塑性区域。面积包括线性区域下的三角形加上弯曲塑性区域下的面积。这是一个很大的面积。
- **材料Q：** 图下方面积只是线性区域下的三角形。这是一个非常小的面积。

因此，**材料P更具韧性**，因为它在断裂前每单位体积吸收更多的能量。

### Final Answer / 最终答案
**Answer:**
(a) Material P is ductile (long plastic region). Material Q is brittle (no plastic region).
(b) $E_P = 1.5 \times 10^{11} \text{ Pa}$, $E_Q = 1.5 \times 10^{11} \text{ Pa}$ (assuming same gradient).
(c) Material P is tougher because it has a larger area under its stress-strain graph.

**答案：**
(a) 材料P是延性的（长塑性区域）。材料Q是脆性的（无塑性区域）。
(b) $E_P = 1.5 \times 10^{11} \text{ Pa}$, $E_Q = 1.5 \times 10^{11} \text{ Pa}$（假设相同梯度）。
(c) 材料P更具韧性，因为其应力-应变图下方面积更大。

### Examiner Notes / 考官点评
**English:**
- **Common mistake:** Confusing toughness with strength. Material P has higher UTS ($4.0 \times 10^8 \text{ Pa}$) than Material Q ($3.0 \times 10^8 \text{ Pa}$), but the key difference is the area under the graph.
- **Common mistake:** Saying "Material P is tougher because it is stronger." Strength (UTS) and toughness are different properties.
- **Mark scheme:** Part (a) 2 marks (1 for identification, 1 for explanation). Part (b) 2 marks. Part (c) 2 marks (1 for identification, 1 for explanation using area under graph).
- **Tip:** Always use the phrase "area under the stress-strain graph" when discussing toughness.

**中文：**
- **常见错误：** 混淆韧性和强度。材料P的UTS（$4.0 \times 10^8 \text{ Pa}$）高于材料Q（$3.0 \times 10^8 \text{ Pa}$），但关键区别在于图下方面积。
- **常见错误：** 说“材料P更具韧性，因为它更强。”强度（UTS）和韧性是不同的性质。
- **评分方案：** 第(a)部分2分（1分识别，1分解释）。第(b)部分2分。第(c)部分2分（1分识别，1分使用图下方面积解释）。
- **提示：** 在讨论韧性时，始终使用短语“应力-应变图下的面积”。

---

# 9. Past Paper Question Types / 历年真题题型

**English:**
The following table summarises the common question types for this topic in both Cambridge 9702 and Edexcel IAL examinations.

**中文：**
下表总结了剑桥9702和爱德思IAL考试中本主题的常见题型。

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of [[Young Modulus]] from graph / 从图计算[[杨氏模量]] | High | Medium | 📝 *待填入* |
| Calculation of energy stored from graph / 从图计算储存的能量 | High | Medium | 📝 *待填入* |
| Sketching stress-strain graphs / 绘制应力-应变图 | High | Medium | 📝 *待填入* |
| Identifying ductile/brittle/polymeric materials / 识别延性/脆性/聚合物材料 | High | Low | 📝 *待填入* |
| Explaining material behaviour (atomic/molecular) / 解释材料行为（原子/分子） | Medium | High | 📝 *待填入* |
| Comparing materials using graphs / 使用图比较材料 | High | Medium | 📝 *待填入* |
| Hysteresis loop analysis / 滞后回线分析 | Low (CIE) / Medium (Edexcel) | High | 📝 *待填入* |
| Practical: determining Young modulus / 实验：测定杨氏模量 | High | Medium | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| Command Word (EN) | Command Word (CN) | What to Do / 做什么 |
|-------------------|-------------------|---------------------|
| State | 陈述 | Give a brief answer without explanation. |
| Define | 定义 | Give the precise meaning of a term. |
| Explain | 解释 | Give reasons for a phenomenon or result. |
| Describe | 描述 | Give a detailed account of a process or graph. |
| Calculate | 计算 | Use numbers and equations to find a value. |
| Determine | 确定 | Find a value, often from a graph. |
| Suggest | 建议 | Use your knowledge to propose a reason or method. |
| Sketch | 绘制 | Draw a graph showing the general shape and key features. |
| Compare | 比较 | Describe similarities and differences. |
| Contrast | 对比 | Describe differences only. |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This topic has strong practical components in both exam boards.

**CAIE 9702:**
- **Paper 3 (AS):** The core practical is "Determination of the Young Modulus of a metal wire." This involves measuring the extension of a wire under different loads, plotting a load-extension graph, calculating stress and strain, and finding the Young modulus from the gradient.
- **Paper 5 (A2):** You may be asked to design an experiment to investigate the stress-strain behaviour of a material, including how to measure force, extension, and cross-sectional area, and how to minimise uncertainties.

**Edexcel IAL:**
- **Unit 3 (AS):** Core Practical 4: "Determine the Young modulus of a material." This involves similar procedures to CAIE Paper 3.
- **Unit 6 (A2):** You may be asked to investigate the plastic behaviour of materials or the hysteresis loop of a polymer.

**Key Practical Skills / 关键实验技能:**

1. **Measurements / 测量:**
   - Force: Use a newtonmeter or masses on a hanger.
   - Extension: Use a micrometer or travelling microscope for small extensions, a ruler for large extensions.
   - Cross-sectional area: Use a micrometer screw gauge to measure the diameter of a wire, then calculate $A = \pi r^2 = \pi d^2/4$.
   - Original length: Use a metre ruler.

2. **Uncertainties / 不确定度:**
   - The largest uncertainty is usually in the measurement of the diameter (since it is squared in the area calculation).
   - Use a micrometer screw gauge (resolution 0.01 mm) to minimise uncertainty.
   - Repeat measurements and calculate the mean.
   - Use error bars on the graph and draw lines of best and worst fit to find the uncertainty in the gradient.

3. **Graph Plotting / 图表绘制:**
   - Plot load (or stress) on the y-axis and extension (or strain) on the x-axis.
   - Draw a line of best fit through the linear region.
   - Calculate the gradient.
   - For the Young modulus: $E = \frac{\text{gradient} \times L}{A}$ (if using load-extension graph).

4. **Experimental Design / 实验设计:**
   - Use a long wire to maximise the extension for a given load (reduces percentage uncertainty).
   - Use a reference wire to compensate for thermal expansion.
   - Add loads gradually and remove them to check for elastic behaviour.
   - Use a safety precaution (e.g., a clamp to catch the masses if the wire breaks).

**中文：**
本主题在两个考试委员会中都有很强的实验成分。

**剑桥9702：**
- **试卷3（AS）：** 核心实验是“测定金属丝的杨氏模量。”这涉及测量金属丝在不同载荷下的伸长量，绘制载荷-伸长图，计算应力和应变，并从梯度求出杨氏模量。
- **试卷5（A2）：** 你可能被要求设计一个实验来研究材料的应力-应变行为，包括如何测量力、伸长量和横截面积，以及如何最小化不确定度。

**爱德思IAL：**
- **单元3（AS）：** 核心实验4：“测定材料的杨氏模量。”这涉及与剑桥试卷3类似的步骤。
- **单元6（A2）：** 你可能被要求研究材料的塑性行为或聚合物的滞后回线。

**关键实验技能：**

1. **测量：**
   - 力：使用牛顿计或挂在挂钩上的砝码。
   - 伸长量：对于小伸长量使用千分尺或移动显微镜，对于大伸长量使用尺子。
   - 横截面积：使用千分尺螺旋测微器测量金属丝的直径，然后计算 $A = \pi r^2 = \pi d^2/4$。
   - 原始长度：使用米尺。

2. **不确定度：**
   - 最大的不确定度通常在于直径的测量（因为它在面积计算中被平方）。
   - 使用千分尺螺旋测微器（分辨率0.01毫米）以最小化不确定度。
   - 重复测量并计算平均值。
   - 在图上使用误差线，并绘制最佳拟合线和最差拟合线以找到梯度的不确定度。

3. **图表绘制：**
   - 在y轴上绘制载荷（或应力），在x轴上绘制伸长量（或应变）。
   - 通过线性区域绘制最佳拟合线。
   - 计算梯度。
   - 对于杨氏模量：$E = \frac{\text{梯度} \times L}{A}$（如果使用载荷-伸长图）。

4. **实验设计：**
   - 使用长金属丝以最大化给定载荷下的伸长量（减少百分比不确定度）。
   - 使用参考金属丝以补偿热膨胀。
   - 逐渐添加载荷并移除它们以检查弹性行为。
   - 使用安全预防措施（例如，如果金属丝断裂，使用夹子接住砝码）。

> 📋 **CIE Only:** Paper 3 often includes questions on the Young modulus experiment. Be familiar with the use of a reference wire and a travelling microscope.
> 📋 **Edexcel Only:** Unit 3 Core Practical 4 is a required practical. You must be able to describe the procedure, calculate the Young modulus, and evaluate the experiment.

---

# 11. Concept Map / 概念图谱

**English:**
The following concept map shows the relationships between this topic (Stress-Strain Graphs and Material Behaviour), its prerequisites, related topics, and sub-topics.

**中文：**
以下概念图显示了本主题（应力-应变图与材料行为）、其先决条件、相关主题和子主题之间的关系。

```mermaid
graph TD
    %% Central Topic
    SSG[Stress-Strain Graphs and Material Behaviour<br>应力-应变图与材料行为]
    
    %% Prerequisites (from other modules)
    PR1[[Stress, Strain and Young Modulus<br>应力、应变和杨氏模量]]
    PR2[[Hooke's Law and Springs<br>胡克定律与弹簧]]
    PR3[[Density<br>密度]]
    
    %% Sub-topics (leaf nodes)
    SUB1[[Stress-Strain Graph for a Ductile Material (Copper)<br>延性材料（铜）的应力-应变图]]
    SUB2[[Stress-Strain Graph for a Brittle Material (Glass)<br>脆性材料（玻璃）的应力-应变图]]
    SUB3[[Stress-Strain Graph for a Polymeric Material (Rubber)<br>聚合物材料（橡胶）的应力-应变图]]
    SUB4[[Elastic and Plastic Regions<br>弹性与塑性区域]]
    SUB5[[Necking and Fracture<br>颈缩与断裂]]
    SUB6[[Material Selection for Engineering Applications<br>工程应用中的材料选择]]
    
    %% Related Topics
    RT1[[Density, Hooke's Law and Springs<br>密度、胡克定律与弹簧]]
    RT2[[Elastic Potential Energy<br>弹性势能]]
    RT3[[Thermal Expansion<br>热膨胀]]
    
    %% Connections
    SSG --> PR1
    SSG --> PR2
    SSG --> PR3
    
    SSG --> SUB1
    SSG --> SUB2
    SSG --> SUB3
    SSG --> SUB4
    SSG --> SUB5
    SSG --> SUB6
    
    SSG --> RT1
    SSG --> RT2
    SSG --> RT3
    
    SUB1 --> SUB4
    SUB1 --> SUB5
    SUB2 --> SUB4
    SUB2 --> SUB5
    SUB3 --> SUB4
    SUB3 --> SUB5
    
    SUB4 --> SUB6
    SUB5 --> SUB6
    
    PR1 --> PR2
    PR1 --> PR3
    
    %% Styling
    classDef central fill:#f9f,stroke:#333,stroke-width:4px;
    classDef prereq fill:#bbf,stroke:#333,stroke-width:2px;
    classDef subtopic fill:#bfb,stroke:#333,stroke-width:2px;
    classDef related fill:#fbb,stroke:#333,stroke-width:2px;
    
    class SSG central;
    class PR1,PR2,PR3 prereq;
    class SUB1,SUB2,SUB3,SUB4,SUB5,SUB6 subtopic;
    class RT1,RT2,RT3 related;
```

---

# 12. Quick Revision Sheet / 速查表

**English:**
The following table provides a one-page bilingual summary of the key points for this topic.

**中文：**
下表提供了本主题关键点的一页双语摘要。

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | **Elastic Deformation / 弹性形变:** Reversible, returns to original shape. **Plastic Deformation / 塑性形变:** Permanent, does not return. **Limit of Proportionality / 比例极限:** End of linear stress-strain relationship. **Elastic Limit / 弹性极限:** End of elastic behaviour. **Yield Point / 屈服点:** Onset of plastic deformation. **UTS / 极限抗拉强度:** Maximum stress. **Breaking Stress / 断裂应力:** Stress at fracture. |
| **Equations / 公式** | **Stress / 应力:** $\sigma = F/A$ (Pa). **Strain / 应变:** $\epsilon = \Delta L/L$ (dimensionless). **Young Modulus / 杨氏模量:** $E = \sigma/\epsilon = FL/(A\Delta L)$ (Pa). **Energy per unit volume / 单位体积能量:** $\frac{1}{2}\sigma\epsilon$ (J/m³) for linear region. **Total energy / 总能量:** $\frac{1}{2}F\Delta L$ (J) for linear region. |
| **Graphs / 图表** | **Ductile / 延性:** Steep line → yield point → long plastic region → UTS → necking → fracture. **Brittle / 脆性:** Steep line → fracture (no plastic region). **Polymeric / 聚合物:** Non-linear curve, large strain, hysteresis loop. **Gradient / 斜率:** Young Modulus. **Area / 面积:** Energy per unit volume (toughness). |
| **Key Facts / 关键事实** | 1. Ductile materials (e.g., copper) have a long plastic region due to dislocation movement. 2. Brittle materials (e.g., glass) fracture with no plastic deformation due to crack propagation. 3. Polymeric materials (e.g., rubber) have non-linear elasticity due to uncoiling of long-chain molecules. 4. The hysteresis loop shows energy dissipated as heat. 5. Toughness = area under stress-strain graph. 6. Stiffness = [[Young Modulus]] (gradient of linear region). |
| **Exam Reminders / 考试提醒** | 1. Always label axes correctly: Stress (Pa) vs Strain (dimensionless). 2. For calculations, ensure units are consistent (m, m², Pa). 3. When comparing materials, use comparative language (higher, lower, more, less). 4. For "explain" questions, link macroscopic behaviour to atomic/molecular structure. 5. For "sketch" questions, show the correct shape and label all key points. 6. For energy calculations, distinguish between total energy and energy per unit volume. 7. Edexcel: Be prepared to explain polymer behaviour in terms of molecular structure. 8. CIE: Be prepared to define and use all key terms. |