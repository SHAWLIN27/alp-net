# 1. Overview / 概述

**English:**
This leaf node focuses on the **stress-strain graph for a ductile material**, specifically using **copper** as the classic example. Ductile materials are those that can undergo significant plastic deformation before fracture. The stress-strain graph for copper is a fundamental tool in materials science and engineering, illustrating the transition from elastic to plastic behavior, the phenomenon of yielding, and the process of necking leading to fracture. Understanding this graph is crucial for selecting materials in applications requiring both strength and the ability to deform without breaking, such as in electrical wiring and plumbing. This sub-topic builds directly on the concepts of [[Stress, Strain and Young Modulus]] and is a key component of the broader [[Stress-Strain Graphs and Material Behaviour]] topic. It contrasts with [[Stress-Strain Graph for a Brittle Material (Glass)]] and [[Stress-Strain Graph for a Polymeric Material (Rubber)]].

**中文:**
本子知识点聚焦于**韧性材料**的应力-应变图，以**铜**作为经典例子。韧性材料是指在断裂前能够发生显著塑性变形的材料。铜的应力-应变图是材料科学和工程学中的基础工具，它展示了从弹性行为到塑性行为的转变、屈服现象以及导致断裂的颈缩过程。理解该图对于在需要同时具备强度和变形能力（如电线和水管）的应用中选择材料至关重要。本子知识点直接建立在[[应力、应变和杨氏模量]]的概念之上，是更广泛的[[应力-应变图与材料行为]]主题的关键组成部分。它与[[脆性材料（玻璃）的应力-应变图]]和[[聚合物材料（橡胶）的应力-应变图]]形成对比。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 6.3(a) Describe the behaviour of materials in terms of stress-strain graphs. | 2.13 Understand the terms elastic deformation and plastic deformation. |
| 6.3(b) Distinguish between elastic and plastic deformation. | 2.14 Understand the terms yield point, ultimate tensile strength (UTS) and breaking stress. |
| 6.3(c) Define and use the terms yield point, ultimate tensile stress and breaking stress. | 2.15 Interpret stress-strain graphs for ductile materials. |
| 6.3(d) Describe the behaviour of ductile materials (e.g., copper) under stress. | 2.16 Understand the concept of necking. |
| 6.3(e) Interpret stress-strain graphs for ductile materials. | 2.17 Distinguish between ductile and brittle materials from their stress-strain graphs. |
| | 2.18 Calculate the Young modulus from the linear region of a stress-strain graph. |

**Examiner Expectations / 考官期望:**
- **CAIE:** Students must be able to describe the shape of the graph, identify key points (elastic limit, yield point, UTS, breaking point), and explain the physical processes occurring at each stage.
- **Edexcel:** Students must be able to interpret the graph, calculate Young modulus from the initial linear region, and understand the significance of the yield point, UTS, and necking.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Ductile Material** / 韧性材料 | A material that can undergo significant plastic deformation before fracture. | 在断裂前能发生显著塑性变形的材料。 | Confusing with "malleable" (can be hammered into sheets). Ductile specifically refers to drawing into wires. |
| **Elastic Limit** / 弹性极限 | The maximum stress a material can withstand without permanent deformation. | 材料在不发生永久变形的情况下能承受的最大应力。 | Thinking it's the same as the limit of proportionality. The elastic limit is slightly higher. |
| **Yield Point** / 屈服点 | The stress at which a material begins to deform plastically without a significant increase in load. | 材料在载荷没有显著增加的情况下开始发生塑性变形的应力点。 | Confusing with the elastic limit. The yield point is where plastic deformation becomes noticeable. |
| **Ultimate Tensile Strength (UTS)** / 极限抗拉强度 | The maximum stress a material can withstand before necking begins. | 材料在颈缩开始前能承受的最大应力。 | Thinking UTS is the breaking stress. UTS is the peak; breaking stress is lower. |
| **Necking** / 颈缩 | A localized reduction in cross-sectional area that occurs after the UTS is reached. | 在达到极限抗拉强度后发生的横截面积的局部减小。 | Thinking necking occurs at the breaking point. It starts at the UTS. |
| **Breaking Stress** / 断裂应力 | The stress at which the material finally fractures. | 材料最终断裂时的应力。 | Confusing with UTS. Breaking stress is always lower than UTS for ductile materials. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Five Stages of the Stress-Strain Graph / 应力-应变图的五个阶段

### Explanation / 解释
**English:** The stress-strain graph for a ductile material like copper can be divided into five distinct stages:

1.  **Proportional (Linear) Region:** Stress is directly proportional to strain. Hooke's law is obeyed. The gradient of this region is the [[Young Modulus]].
2.  **Elastic Region:** The material still returns to its original shape when the stress is removed. This extends slightly beyond the proportional limit to the elastic limit.
3.  **Yield Point:** A small drop in stress may be observed (upper and lower yield points), followed by a region where strain increases significantly with little or no increase in stress. This is where [[Elastic and Plastic Regions]] transition.
4.  **Plastic (Work Hardening) Region:** After yielding, the material requires increasing stress to produce further strain. This is due to dislocations in the crystal lattice becoming entangled, a process called work hardening.
5.  **Necking and Fracture:** At the UTS, the material begins to [[Necking and Fracture|neck]] — a localized reduction in cross-sectional area. This causes the stress to decrease until the material fractures at the breaking stress.

**中文:** 像铜这样的韧性材料的应力-应变图可以分为五个不同的阶段：

1.  **比例（线性）区域：** 应力与应变成正比。遵循胡克定律。该区域的梯度是[[杨氏模量]]。
2.  **弹性区域：** 当应力移除时，材料仍能恢复到原始形状。这略微超出比例极限，延伸到弹性极限。
3.  **屈服点：** 可能会观察到应力的小幅下降（上屈服点和下屈服点），随后是一个应变显著增加而应力几乎没有增加或没有增加的区域。这是[[弹性区域和塑性区域]]过渡的地方。
4.  **塑性（加工硬化）区域：** 屈服后，材料需要增加的应力才能产生进一步的应变。这是由于晶格中的位错变得缠结，这个过程称为加工硬化。
5.  **颈缩和断裂：** 在极限抗拉强度（UTS）处，材料开始[[颈缩和断裂|颈缩]]——横截面积的局部减小。这导致应力下降，直到材料在断裂应力处断裂。

### Physical Meaning / 物理意义
**English:** The graph tells the story of how the internal structure of the material responds to an applied force. Initially, atoms are stretched apart elastically. At the yield point, atomic planes begin to slip past each other (dislocation motion). In the plastic region, these dislocations multiply and interact, making further deformation harder (work hardening). Finally, the material becomes unstable and necks, leading to failure.

**中文:** 该图讲述了材料内部结构如何响应施加的力的故事。最初，原子被弹性拉伸。在屈服点，原子平面开始相互滑过（位错运动）。在塑性区域，这些位错倍增并相互作用，使进一步变形更加困难（加工硬化）。最后，材料变得不稳定并颈缩，导致失效。

### Common Misconceptions / 常见误区
- **Misconception:** The breaking stress is the highest point on the graph.
  **Correction:** The UTS is the highest point. The breaking stress is lower because necking reduces the cross-sectional area.
- **Misconception:** The elastic limit and the limit of proportionality are the same.
  **Correction:** The limit of proportionality is where Hooke's law stops being obeyed. The elastic limit is slightly higher; between them, the material is still elastic but not proportional.
- **Misconception:** All plastic deformation is permanent.
  **Correction:** Yes, plastic deformation is permanent. Elastic deformation is recoverable.

### Exam Tips / 考试提示
- **EN:** Always label the axes correctly (Stress on y-axis, Strain on x-axis). When asked to calculate Young modulus, use the gradient of the initial linear portion. Remember that stress is force/area and strain is extension/original length.
- **中文:** 务必正确标注坐标轴（应力在y轴，应变在x轴）。当被要求计算杨氏模量时，使用初始线性部分的梯度。记住应力是力/面积，应变是伸长量/原始长度。

> 📷 **IMAGE PROMPT — DUCTILE_GRAPH_01: Annotated Stress-Strain Graph for Copper**
> A clear, labeled stress-strain graph for a ductile material (copper). The x-axis is labeled "Strain" and the y-axis "Stress". Five key points are marked: (1) Limit of Proportionality, (2) Elastic Limit, (3) Yield Point, (4) Ultimate Tensile Strength (UTS), and (5) Breaking Point. The regions are labeled: "Elastic Region", "Plastic Region", and "Necking Region". The graph should show a slight dip at the yield point, a rising curve in the plastic region, and a drop after the UTS.

---

# 5. Essential Equations / 核心公式

## 5.1 Young Modulus (from the linear region) / 杨氏模量（来自线性区域）

$$ E = \frac{\sigma}{\epsilon} = \frac{F/A}{\Delta L / L_0} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Young Modulus | 杨氏模量 | Pa (or N m⁻²) |
| $\sigma$ | Stress | 应力 | Pa (or N m⁻²) |
| $\epsilon$ | Strain | 应变 | No unit (dimensionless) |
| $F$ | Force | 力 | N |
| $A$ | Cross-sectional area | 横截面积 | m² |
| $\Delta L$ | Extension | 伸长量 | m |
| $L_0$ | Original length | 原始长度 | m |

**Derivation / 推导:** This is the definition of Young modulus. It is only valid in the linear (proportional) region of the stress-strain graph.

**Conditions / 适用条件:**
- **EN:** Only valid within the limit of proportionality (linear region). The material must be homogeneous and isotropic.
- **中文:** 仅在比例极限内（线性区域）有效。材料必须是均匀且各向同性的。

**Limitations / 局限性:**
- **EN:** Does not apply to plastic deformation. The gradient changes after the yield point.
- **中文:** 不适用于塑性变形。屈服点后梯度会改变。

## 5.2 Stress / 应力

$$ \sigma = \frac{F}{A} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\sigma$ | Stress | 应力 | Pa |
| $F$ | Force | 力 | N |
| $A$ | Cross-sectional area | 横截面积 | m² |

## 5.3 Strain / 应变

$$ \epsilon = \frac{\Delta L}{L_0} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\epsilon$ | Strain | 应变 | No unit |
| $\Delta L$ | Extension | 伸长量 | m |
| $L_0$ | Original length | 原始长度 | m |

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Stress-Strain Graph for Copper / 铜的应力-应变图

### Axes / 坐标轴
- **Y-axis:** Stress ($\sigma$) / 应力 ($\sigma$)
- **X-axis:** Strain ($\epsilon$) / 应变 ($\epsilon$)

### Shape / 形状
**English:** The graph is initially a straight line through the origin (linear elastic region). It then curves, showing a slight dip at the yield point. After yielding, it rises again (work hardening) to a peak (UTS). After the peak, it curves downward until fracture.

**中文:** 该图最初是一条通过原点的直线（线性弹性区域）。然后弯曲，在屈服点处略有下降。屈服后，它再次上升（加工硬化）达到峰值（UTS）。峰值过后，曲线向下直至断裂。

### Gradient Meaning / 斜率含义
- **Linear Region:** Gradient = Young Modulus ($E$). A steeper gradient means a stiffer material.
- **Plastic Region:** The gradient is not constant. It represents the rate of work hardening.

### Area Meaning / 面积含义
**English:** The area under the entire stress-strain curve represents the **toughness** of the material — the energy absorbed per unit volume before fracture. A ductile material like copper has a large area under the curve, indicating high toughness.

**中文:** 整个应力-应变曲线下的面积代表材料的**韧性**——断裂前单位体积吸收的能量。像铜这样的韧性材料曲线下面积很大，表明韧性高。

### Exam Interpretation / 考试解读
- **EN:** If asked to compare ductile and brittle materials, note that ductile materials have a long plastic region and a large area under the curve. Brittle materials have no plastic region and a small area.
- **中文:** 如果被要求比较韧性和脆性材料，注意韧性材料有长的塑性区域和大的曲线下面积。脆性材料没有塑性区域，面积小。

---

# 7. Required Diagrams / 必备图表

## 7.1 Annotated Stress-Strain Graph for Copper / 铜的标注应力-应变图

### Description / 描述
**English:** A fully annotated stress-strain graph for copper showing all key points and regions. The graph should clearly show the linear elastic region, the yield point (with upper and lower yield points if possible), the plastic/work hardening region, the UTS, the necking region, and the breaking point.

**中文:** 一个完全标注的铜的应力-应变图，显示所有关键点和区域。该图应清晰显示线性弹性区域、屈服点（如果可能，显示上、下屈服点）、塑性/加工硬化区域、UTS、颈缩区域和断裂点。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DUCTILE_GRAPH_02: Detailed Annotated Stress-Strain Graph for Copper**
> A professional, textbook-quality stress-strain graph for a ductile material (copper). The x-axis is labeled "Strain (ε)" and the y-axis "Stress (σ)". The graph has five clearly marked points: A (Limit of Proportionality), B (Elastic Limit), C (Yield Point, showing a slight dip), D (Ultimate Tensile Strength, UTS), and E (Breaking Point). The regions are labeled: "Elastic Region" (from O to B), "Plastic Region" (from C to D), and "Necking Region" (from D to E). The gradient of the initial straight line is labeled "Young Modulus (E)". The graph should be clean, with gridlines and a white background.

### Labels Required / 需要标注
- **Axes:** Stress (σ) / Strain (ε)
- **Points:** Limit of Proportionality, Elastic Limit, Yield Point, UTS, Breaking Point
- **Regions:** Elastic Region, Plastic Region, Necking Region
- **Gradient:** Young Modulus (E)

### Exam Importance / 考试重要性
- **EN:** This is the most commonly asked diagram in exams. Students must be able to draw, label, and explain each part.
- **中文:** 这是考试中最常被问到的图表。学生必须能够绘制、标注并解释每个部分。

## 7.2 Necking Diagram / 颈缩示意图

### Description / 描述
**English:** A diagram showing a tensile test specimen before, during, and after necking. The specimen should show a uniform cross-section initially, then a localized reduction in area at the neck, and finally fracture at the neck.

**中文:** 一个显示拉伸试样在颈缩前、中、后的示意图。试样应显示初始均匀的横截面，然后在颈部局部面积减小，最后在颈部断裂。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DUCTILE_NECKING_01: Necking in a Copper Tensile Specimen**
> Three stages of a copper tensile test specimen. Stage 1: A uniform cylindrical rod with a circular cross-section. Stage 2: The rod showing a localized reduction in diameter (necking) in the middle. Stage 3: The rod broken into two pieces at the neck, showing a cup-and-cone fracture surface. Arrows indicate the direction of the applied tensile force. Labels: "Original Specimen", "Necking", "Fracture".

### Labels Required / 需要标注
- Original Specimen
- Necking Region
- Fracture Surface (cup-and-cone)

### Exam Importance / 考试重要性
- **EN:** Understanding necking is crucial for explaining why the stress decreases after the UTS.
- **中文:** 理解颈缩对于解释为什么UTS后应力下降至关重要。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Young Modulus from the Graph / 从图中计算杨氏模量

### Question / 题目
**English:** The stress-strain graph for a copper wire shows that at a stress of 120 MPa, the strain is 0.0012. Calculate the Young modulus of copper.

**中文:** 一根铜线的应力-应变图显示，在应力为120 MPa时，应变为0.0012。计算铜的杨氏模量。

### Solution / 解答

**Step 1:** Identify the relevant equation.
$$ E = \frac{\sigma}{\epsilon} $$

**Step 2:** Substitute the values.
$$ E = \frac{120 \times 10^6 \text{ Pa}}{0.0012} $$

**Step 3:** Calculate.
$$ E = 100 \times 10^9 \text{ Pa} = 100 \text{ GPa} $$

### Final Answer / 最终答案
**Answer:** $E = 100 \text{ GPa}$ | **答案：** $E = 100 \text{ GPa}$

### Quick Tip / 提示
- **EN:** Always convert stress to Pa (N m⁻²) before calculating. 1 MPa = 10⁶ Pa.
- **中文:** 计算前务必将应力转换为Pa (N m⁻²)。1 MPa = 10⁶ Pa。

## Example 2: Interpreting the Graph / 解读图表

### Question / 题目
**English:** A copper rod is subjected to a tensile stress that takes it beyond the yield point. Describe what happens to the rod as the stress is increased from the yield point to the breaking point.

**中文:** 一根铜棒受到拉伸应力，使其超过屈服点。描述当应力从屈服点增加到断裂点时，铜棒会发生什么。

### Solution / 解答

**Step 1:** From yield point to UTS.
The rod undergoes plastic deformation. It does not return to its original length when the stress is removed. The material work-hardens, requiring increasing stress to produce further strain. The cross-sectional area decreases uniformly.

**Step 2:** At UTS.
The rod reaches its maximum load-bearing capacity. Necking begins — a localized reduction in cross-sectional area.

**Step 3:** From UTS to breaking point.
The stress decreases because the cross-sectional area at the neck is reducing rapidly. The rod continues to elongate, but most of the extension is concentrated at the neck. Finally, the rod fractures at the neck.

**中文：**

**步骤1：** 从屈服点到UTS。
铜棒发生塑性变形。当应力移除时，它不会恢复到原始长度。材料发生加工硬化，需要增加的应力才能产生进一步的应变。横截面积均匀减小。

**步骤2：** 在UTS处。
铜棒达到其最大承载能力。颈缩开始——横截面积的局部减小。

**步骤3：** 从UTS到断裂点。
应力下降，因为颈部的横截面积迅速减小。铜棒继续伸长，但大部分伸长集中在颈部。最后，铜棒在颈部断裂。

### Final Answer / 最终答案
**Answer:** See solution above. | **答案：** 见上方解答。

### Quick Tip / 提示
- **EN:** Use the correct terminology: "plastic deformation", "work hardening", "necking", "fracture".
- **中文：** 使用正确的术语："塑性变形"、"加工硬化"、"颈缩"、"断裂"。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Draw and label the stress-strain graph for a ductile material | High | Easy | 📝 *待填入* |
| Calculate Young modulus from the linear region | High | Medium | 📝 *待填入* |
| Explain the shape of the graph (yield point, UTS, necking) | High | Medium | 📝 *待填入* |
| Compare ductile and brittle materials using their graphs | Medium | Medium | 📝 *待填入* |
| Describe what happens to the material at each stage | Medium | Medium | 📝 *待填入* |
| Calculate toughness from the area under the graph | Low | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **EN:** Describe, Explain, Calculate, Draw, Label, Compare, Distinguish
- **中文：** 描述、解释、计算、绘制、标注、比较、区分

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is directly linked to the **tensile test experiment** (Paper 3 for CAIE, Unit 1 Core Practical for Edexcel). Key practical skills include:

1.  **Measurements:** Using a micrometer to measure the diameter of the wire (to calculate cross-sectional area), using a ruler to measure original length, and using a force sensor or masses to apply force.
2.  **Uncertainties:** Calculating the percentage uncertainty in stress (from force and area measurements) and strain (from extension and length measurements). The uncertainty in the Young modulus is the sum of the uncertainties in stress and strain.
3.  **Graph Plotting:** Plotting a stress-strain graph from experimental data. Identifying the linear region and drawing a line of best fit to calculate the gradient (Young modulus).
4.  **Experimental Design:** Ensuring the wire is straight and vertical, using a marker to indicate the original length, and taking readings slowly to avoid exceeding the elastic limit prematurely.

**中文:**
本子知识点与**拉伸实验**直接相关（CAIE的Paper 3，Edexcel的Unit 1核心实践）。关键的实验技能包括：

1.  **测量：** 使用千分尺测量金属丝的直径（以计算横截面积），使用尺子测量原始长度，以及使用力传感器或砝码施加力。
2.  **不确定度：** 计算应力（来自力和面积测量）和应变（来自伸长量和长度测量）的百分比不确定度。杨氏模量的不确定度是应力和应变不确定度之和。
3.  **图表绘制：** 根据实验数据绘制应力-应变图。识别线性区域并绘制最佳拟合线以计算梯度（杨氏模量）。
4.  **实验设计：** 确保金属丝笔直且垂直，使用标记指示原始长度，并缓慢读取读数以避免过早超过弹性极限。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Node
    DUCTILE[Stress-Strain Graph for Ductile Material (Copper)] --> LINEAR[Linear Elastic Region]
    DUCTILE --> YIELD[Yield Point]
    DUCTILE --> PLASTIC[Plastic / Work Hardening Region]
    DUCTILE --> UTS[Ultimate Tensile Strength]
    DUCTILE --> NECK[Necking and Fracture]

    %% Connections to Prerequisites
    LINEAR --> YOUNG[Young Modulus]
    YOUNG --> STRESS[Stress = F/A]
    YOUNG --> STRAIN[Strain = ΔL/L]

    %% Connections to Sibling Nodes
    DUCTILE --> BRITTLE[Stress-Strain Graph for Brittle Material (Glass)]
    DUCTILE --> POLYMER[Stress-Strain Graph for Polymeric Material (Rubber)]
    DUCTILE --> ELASTIC_PLASTIC[Elastic and Plastic Regions]
    DUCTILE --> NECKING[Necking and Fracture]
    DUCTILE --> SELECTION[Material Selection for Engineering Applications]

    %% Connections to Related Topics
    LINEAR --> HOOKE[Hooke's Law and Springs]
    STRESS --> DENSITY[Density]

    %% Properties
    DUCTILE --> TOUGHNESS[Toughness - Area Under Curve]
    DUCTILE --> DUCTILITY[Ductility - % Elongation]

    %% Styling
    style DUCTILE fill:#f9f,stroke:#333,stroke-width:4px
    style LINEAR fill:#bbf,stroke:#333,stroke-width:2px
    style YOUNG fill:#bbf,stroke:#333,stroke-width:2px
    style BRITTLE fill:#fbb,stroke:#333,stroke-width:2px
    style POLYMER fill:#bfb,stroke:#333,stroke-width:2px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | A **ductile material** undergoes significant plastic deformation before fracture. Copper is a classic example. / **韧性材料**在断裂前发生显著的塑性变形。铜是一个经典例子。 |
| **Key Formula / 核心公式** | $E = \frac{\sigma}{\epsilon}$ (Young Modulus from linear region) / 杨氏模量（来自线性区域） |
| **Key Graph / 核心图表** | Stress-Strain Graph: Linear → Yield → Plastic → UTS → Necking → Fracture / 应力-应变图：线性 → 屈服 → 塑性 → UTS → 颈缩 → 断裂 |
| **Key Points / 关键点** | **Limit of Proportionality:** End of Hooke's law. **Elastic Limit:** End of elastic behavior. **Yield Point:** Start of plastic deformation. **UTS:** Maximum stress. **Breaking Point:** Fracture. / **比例极限：** 胡克定律结束。**弹性极限：** 弹性行为结束。**屈服点：** 塑性变形开始。**UTS：** 最大应力。**断裂点：** 断裂。 |
| **Exam Tip / 考试提示** | Always calculate Young modulus from the **initial linear gradient**. Remember that stress decreases after UTS due to **necking**. / 始终从**初始线性梯度**计算杨氏模量。记住由于**颈缩**，UTS后应力下降。 |
| **Common Mistake / 常见错误** | Confusing UTS with breaking stress. UTS is the peak; breaking stress is lower. / 混淆UTS和断裂应力。UTS是峰值；断裂应力更低。 |
| **Practical Skill / 实验技能** | Use a micrometer for diameter, measure original length with a marker, plot stress-strain graph, calculate gradient for Young modulus. / 使用千分尺测量直径，用标记测量原始长度，绘制应力-应变图，计算梯度得到杨氏模量。 |