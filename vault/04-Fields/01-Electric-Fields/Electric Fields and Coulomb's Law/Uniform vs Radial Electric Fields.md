# Uniform vs Radial Electric Fields / 匀强电场与径向电场

---

# 1. Overview / 概述

**English:**
This sub-topic distinguishes between the two fundamental types of electric field configurations encountered in A-Level Physics: **uniform electric fields** and **radial (non-uniform) electric fields**. A uniform electric field has constant magnitude and direction between two parallel charged plates, while a radial electric field emanates from or converges toward a point charge or charged sphere. Understanding the differences in field patterns, force behavior, and mathematical descriptions is essential for solving problems involving charged particles in electric fields and forms the foundation for [[Electric Potential]] and [[Capacitance and Capacitors]].

The key distinction lies in how [[Electric Field Strength]] $E$ varies with position: constant in uniform fields, inversely proportional to $r^2$ in radial fields. This sub-topic builds directly on [[Electric Field Concept and Field Lines]] and [[Coulomb's Law]], and is closely related to [[Electric Field Between Parallel Plates]].

**中文:**
本子知识点区分了A-Level物理中遇到的两种基本电场构型：**匀强电场**和**径向（非匀强）电场**。匀强电场在两块平行带电板之间具有恒定的大小和方向，而径向电场则从点电荷或带电球体发出或向其汇聚。理解场模式、力的行为和数学描述的差异，对于解决涉及带电粒子在电场中运动的问题至关重要，并为[[Electric Potential]]和[[Capacitance and Capacitors]]奠定基础。

关键区别在于[[Electric Field Strength]] $E$ 随位置的变化方式：在匀强电场中恒定，在径向电场中与 $r^2$ 成反比。本子知识点直接建立在[[Electric Field Concept and Field Lines]]和[[Coulomb's Law]]之上，并与[[Electric Field Between Parallel Plates]]密切相关。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 18.1(a) Describe an electric field as a region where electric forces act on charged particles | 2.1 Understand electric fields as regions where charged particles experience a force |
| 18.1(b) Distinguish between uniform and radial electric fields | 2.2 Distinguish between uniform and radial electric fields |
| 18.1(c) Recall and use $E = \frac{V}{d}$ for a uniform field | 2.3 Use $E = \frac{V}{d}$ for uniform fields |
| 18.1(d) Recall and use $E = \frac{Q}{4\pi\epsilon_0 r^2}$ for a radial field | 2.4 Use $E = \frac{Q}{4\pi\epsilon_0 r^2}$ for radial fields |
| 18.1(e) Describe field patterns using field lines | 2.5 Draw and interpret electric field patterns |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to visually identify and sketch both field patterns, apply the correct formula for each case, and explain why field strength varies differently. Common exam tasks include comparing forces on test charges, calculating field strengths, and interpreting field line diagrams.
- **中文:** 学生必须能够直观识别和绘制两种场模式，对每种情况应用正确的公式，并解释场强为何不同变化。常见的考试任务包括比较对试探电荷的力、计算场强以及解释场线图。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Uniform Electric Field** / 匀强电场 | An electric field in which the electric field strength $E$ has the same magnitude and direction at every point. | 电场强度 $E$ 在每个点都具有相同大小和方向的电场。 | Confusing "uniform" with "constant potential" — potential changes linearly, not constant. / 将"均匀"与"恒定电势"混淆——电势线性变化，并非恒定。 |
| **Radial Electric Field** / 径向电场 | An electric field that radiates outward from or inward toward a point charge or charged sphere, with field strength decreasing as $1/r^2$. | 从点电荷或带电球体向外辐射或向内汇聚的电场，场强按 $1/r^2$ 减小。 | Thinking field lines are equally spaced — they spread out, so spacing increases with distance. / 认为场线等间距分布——实际上它们散开，间距随距离增大。 |
| **Field Line** / 场线 | An imaginary line whose direction at any point gives the direction of the electric field at that point. | 一种假想线，其上任意点的方向表示该点电场的方向。 | Drawing lines that cross — field lines never cross. / 画出交叉的线——场线永不相交。 |
| **Parallel Plates** / 平行板 | Two flat conducting plates placed parallel to each other, carrying equal and opposite charges, producing a uniform field between them. | 两块彼此平行放置的扁平导体板，带有等量异种电荷，在它们之间产生匀强电场。 | Forgetting fringing effects at edges — field is only approximately uniform in the central region. / 忽略边缘的 fringe 效应——仅在中心区域场近似均匀。 |
| **Point Charge** / 点电荷 | An idealized charge concentrated at a single point in space. | 理想化的电荷，集中在空间中的一个点上。 | Applying $E = \frac{Q}{4\pi\epsilon_0 r^2}$ to finite-sized conductors without considering charge distribution. / 将 $E = \frac{Q}{4\pi\epsilon_0 r^2}$ 应用于有限尺寸导体而不考虑电荷分布。 |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Uniform Electric Field / 匀强电场

### Explanation / 解释
**English:**
A uniform electric field is created between two parallel conducting plates connected to a power supply. The plates carry equal and opposite charges, producing a field that is constant in both magnitude and direction throughout the region between them (ignoring edge effects). The field lines are parallel, equally spaced, and directed from the positive plate to the negative plate. The [[Electric Field Strength]] is given by $E = \frac{V}{d}$, where $V$ is the potential difference between the plates and $d$ is their separation.

**中文:**
匀强电场由连接到电源的两块平行导体板产生。两块板带有等量异种电荷，在它们之间的区域内产生大小和方向都恒定的电场（忽略边缘效应）。场线平行、等间距，从正极板指向负极板。[[Electric Field Strength]] 由 $E = \frac{V}{d}$ 给出，其中 $V$ 是两极板间的电势差，$d$ 是它们的间距。

### Physical Meaning / 物理意义
**English:**
In a uniform field, a charged particle experiences a constant force $F = qE$ regardless of its position. This means the acceleration of the particle is constant, leading to parabolic trajectories for particles entering perpendicular to the field (similar to projectile motion under gravity). The constant field also means the potential changes linearly with distance: $V = Ed$.

**中文:**
在匀强电场中，带电粒子无论处于什么位置，都受到恒定的力 $F = qE$。这意味着粒子的加速度恒定，导致垂直于电场进入的粒子产生抛物线轨迹（类似于重力作用下的抛体运动）。恒定的场也意味着电势随距离线性变化：$V = Ed$。

### Common Misconceptions / 常见误区
- **English:** Thinking the field is uniform everywhere, including outside the plates. The field is only uniform in the region between the plates.
- **中文:** 认为场在任何地方都是均匀的，包括板外。场仅在两极板之间的区域是均匀的。
- **English:** Confusing $V$ (potential difference) with $E$ (field strength). $V$ is energy per unit charge; $E$ is force per unit charge.
- **中文:** 混淆 $V$（电势差）和 $E$（场强）。$V$ 是单位电荷的能量；$E$ 是单位电荷的力。
- **English:** Assuming $E = V/d$ applies to all fields — it only applies to uniform fields.
- **中文:** 假设 $E = V/d$ 适用于所有电场——它只适用于匀强电场。

### Exam Tips / 考试提示
- **English:** Always check if the field is uniform before using $E = V/d$. For radial fields, use $E = \frac{Q}{4\pi\epsilon_0 r^2}$.
- **中文:** 在使用 $E = V/d$ 之前，务必检查场是否为匀强。对于径向场，使用 $E = \frac{Q}{4\pi\epsilon_0 r^2}$。
- **English:** In trajectory problems, treat the uniform field like a gravitational field — use SUVAT equations for constant acceleration.
- **中文:** 在轨迹问题中，将匀强场视为重力场——使用匀加速运动的SUVAT方程。

> 📷 **IMAGE PROMPT — URF-01: Uniform Electric Field Between Parallel Plates**
> A clear diagram showing two parallel metal plates connected to a DC power supply. The positive plate is labeled "+" and the negative plate is labeled "−". Between the plates, draw equally spaced parallel arrows pointing from positive to negative, representing the uniform electric field. Label the plate separation as "d" and the potential difference as "V". Show a small positive test charge +q experiencing a constant force F = qE. Include a note about "fringing fields" at the edges.

---

## 4.2 Radial Electric Field / 径向电场

### Explanation / 解释
**English:**
A radial electric field is produced by an isolated point charge or a charged sphere. The field lines radiate outward from a positive charge and inward toward a negative charge. The field strength varies with distance from the charge according to [[Coulomb's Law]]: $E = \frac{Q}{4\pi\epsilon_0 r^2}$. The field is non-uniform because the magnitude decreases as $1/r^2$ and the direction changes with position.

**中文:**
径向电场由孤立的点电荷或带电球体产生。场线从正电荷向外辐射，向负电荷汇聚。场强根据[[Coulomb's Law]]随距电荷的距离变化：$E = \frac{Q}{4\pi\epsilon_0 r^2}$。场是非匀强的，因为大小按 $1/r^2$ 减小，且方向随位置变化。

### Physical Meaning / 物理意义
**English:**
In a radial field, the force on a test charge depends on its distance from the source charge. Closer to the source, the force is stronger; farther away, it weakens. This inverse-square relationship means that doubling the distance reduces the field strength to one-quarter. The potential also varies with distance, following $V = \frac{Q}{4\pi\epsilon_0 r}$ (for a point charge).

**中文:**
在径向电场中，对试探电荷的力取决于它离源电荷的距离。离源越近，力越强；越远，力越弱。这种平方反比关系意味着距离加倍会使场强减小到四分之一。电势也随距离变化，遵循 $V = \frac{Q}{4\pi\epsilon_0 r}$（对于点电荷）。

### Common Misconceptions / 常见误区
- **English:** Thinking the field is uniform near the surface of a charged sphere. While the field lines are perpendicular to the surface, the magnitude still follows $1/r^2$ from the center.
- **中文:** 认为带电球体表面附近的场是均匀的。虽然场线垂直于表面，但大小仍然遵循从球心算起的 $1/r^2$ 关系。
- **English:** Confusing radial field lines with magnetic field lines — electric field lines start on positive charges and end on negative charges.
- **中文:** 将径向场线与磁感线混淆——电场线始于正电荷，止于负电荷。
- **English:** Forgetting that $r$ in $E = \frac{Q}{4\pi\epsilon_0 r^2}$ is the distance from the center of the charge, not the surface.
- **中文:** 忘记 $E = \frac{Q}{4\pi\epsilon_0 r^2}$ 中的 $r$ 是距电荷中心的距离，而不是距表面的距离。

### Exam Tips / 考试提示
- **English:** For a charged sphere, treat it as a point charge at the center when calculating field strength outside the sphere.
- **中文:** 对于带电球体，在计算球外场强时，将其视为球心的点电荷。
- **English:** Remember that field lines are closer together where the field is stronger — near the charge.
- **中文:** 记住，场线在场强更大的地方更密集——即靠近电荷处。

> 📷 **IMAGE PROMPT — URF-02: Radial Electric Field Around a Point Charge**
> A diagram showing a positive point charge +Q at the center. Draw radial arrows pointing outward in all directions, with arrows closer together near the charge and spreading apart as distance increases. Label the distance r from the charge and show the field strength E decreasing as 1/r². Include a second diagram for a negative point charge −Q with arrows pointing inward. Add labels: "E ∝ 1/r²" and "Non-uniform field".

---

## 4.3 Comparison: Uniform vs Radial / 比较：匀强 vs 径向

| Feature / 特征 | Uniform Field / 匀强电场 | Radial Field / 径向电场 |
|----------------|-------------------------|------------------------|
| **Source** / 来源 | Parallel plates | Point charge or charged sphere |
| **Field lines** / 场线 | Parallel, equally spaced | Radial, spacing increases with distance |
| **E magnitude** / E的大小 | Constant | $E \propto 1/r^2$ |
| **E direction** / E的方向 | Constant (one direction) | Varies with position |
| **Formula** / 公式 | $E = \frac{V}{d}$ | $E = \frac{Q}{4\pi\epsilon_0 r^2}$ |
| **Force on test charge** / 对试探电荷的力 | Constant | Varies with $1/r^2$ |
| **Potential variation** / 电势变化 | Linear: $V = Ed$ | $V \propto 1/r$ |

---

# 5. Essential Equations / 核心公式

## Equation 1: Uniform Field Strength / 匀强电场场强

$$ E = \frac{V}{d} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Electric field strength | 电场强度 | N C$^{-1}$ or V m$^{-1}$ |
| $V$ | Potential difference between plates | 两极板间的电势差 | V |
| $d$ | Separation between plates | 两极板间距 | m |

**Derivation / 推导:**
From $W = qV$ (work done moving charge through potential difference) and $W = Fd = qEd$ (work done by constant force), equating gives $qV = qEd$, so $E = V/d$.

**Conditions / 适用条件:**
- **English:** Only applies to uniform electric fields between parallel plates. Assumes field is perfectly uniform (ignoring edge effects).
- **中文:** 仅适用于平行板之间的匀强电场。假设场完全均匀（忽略边缘效应）。

**Limitations / 局限性:**
- **English:** Does not apply to radial fields or non-uniform fields. Edge effects cause non-uniformity near plate boundaries.
- **中文:** 不适用于径向场或非匀强场。边缘效应导致板边界附近场不均匀。

---

## Equation 2: Radial Field Strength / 径向电场场强

$$ E = \frac{Q}{4\pi\epsilon_0 r^2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $E$ | Electric field strength | 电场强度 | N C$^{-1}$ |
| $Q$ | Source charge | 源电荷 | C |
| $\epsilon_0$ | Permittivity of free space | 真空介电常数 | F m$^{-1}$ |
| $r$ | Distance from center of charge | 距电荷中心的距离 | m |

**Derivation / 推导:**
From [[Coulomb's Law]]: $F = \frac{Qq}{4\pi\epsilon_0 r^2}$. Since $E = F/q$, dividing by $q$ gives $E = \frac{Q}{4\pi\epsilon_0 r^2}$.

**Conditions / 适用条件:**
- **English:** Applies to point charges and charged spheres (for points outside the sphere). Assumes vacuum or air.
- **中文:** 适用于点电荷和带电球体（对于球外点）。假设真空或空气。

**Limitations / 局限性:**
- **English:** Does not apply inside a charged conductor (field is zero inside). For finite-sized conductors, charge distribution may not be perfectly spherical.
- **中文:** 不适用于带电导体内部（内部场为零）。对于有限尺寸的导体，电荷分布可能不是完美的球形。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 E vs r for Uniform Field / 匀强电场的 E-r 图

### Axes / 坐标轴
- **X-axis:** Distance from positive plate / 距正极板的距离
- **Y-axis:** Electric field strength E / 电场强度 E

### Shape / 形状
- **English:** Horizontal straight line — E is constant regardless of position between the plates.
- **中文:** 水平直线——E 在极板间任何位置都恒定。

### Gradient Meaning / 斜率含义
- **English:** Zero gradient — field strength does not change with position.
- **中文:** 零斜率——场强不随位置变化。

### Area Meaning / 面积含义
- **English:** Area under the graph gives the potential difference: $V = E \times d$.
- **中文:** 图线下面积给出电势差：$V = E \times d$。

### Exam Interpretation / 考试解读
- **English:** If asked to sketch E vs r for a uniform field, draw a horizontal line. The line should start at the positive plate and end at the negative plate.
- **中文:** 如果要求画出匀强电场的 E-r 图，画一条水平线。线应从正极板开始，到负极板结束。

> 📷 **IMAGE PROMPT — URF-03: E vs r Graph for Uniform Field**
> A simple graph with distance r on the x-axis and electric field strength E on the y-axis. Draw a horizontal line from r=0 to r=d, labeled "E = constant". Shade the area under the line and label it "Area = V = E × d". Add axis labels and a title.

---

## 6.2 E vs r for Radial Field / 径向电场的 E-r 图

### Axes / 坐标轴
- **X-axis:** Distance from charge center / 距电荷中心的距离
- **Y-axis:** Electric field strength E / 电场强度 E

### Shape / 形状
- **English:** Curve decreasing as $1/r^2$ — steep near the charge, flattening out at large distances.
- **中文:** 按 $1/r^2$ 减小的曲线——靠近电荷处陡峭，远处趋于平缓。

### Gradient Meaning / 斜率含义
- **English:** Negative gradient that decreases in magnitude with distance. The gradient is $\frac{dE}{dr} = -\frac{2Q}{4\pi\epsilon_0 r^3}$.
- **中文:** 负斜率，其大小随距离减小。梯度为 $\frac{dE}{dr} = -\frac{2Q}{4\pi\epsilon_0 r^3}$。

### Area Meaning / 面积含义
- **English:** Area under the graph gives the potential difference between two points: $\Delta V = -\int_{r_1}^{r_2} E \, dr$.
- **中文:** 图线下面积给出两点间的电势差：$\Delta V = -\int_{r_1}^{r_2} E \, dr$。

### Exam Interpretation / 考试解读
- **English:** The graph shows the non-uniform nature clearly. Doubling r reduces E to one-quarter. The curve never reaches zero — field extends to infinity.
- **中文:** 该图清晰地显示了非匀强性质。r 加倍使 E 减小到四分之一。曲线永远不会达到零——场延伸到无穷远。

> 📷 **IMAGE PROMPT — URF-04: E vs r Graph for Radial Field**
> A graph with distance r on the x-axis and electric field strength E on the y-axis. Draw a decreasing curve that is steep near the origin and flattens out. Label the curve "E ∝ 1/r²". Mark two points at r and 2r, showing that E at 2r is one-quarter of E at r. Add axis labels and a title.

---

# 7. Required Diagrams / 必备图表

## 7.1 Uniform Electric Field Diagram / 匀强电场示意图

### Description / 描述
**English:**
A diagram showing two parallel metal plates connected to a DC power supply. The positive plate is connected to the positive terminal and the negative plate to the negative terminal. Between the plates, draw equally spaced parallel arrows pointing from the positive to the negative plate. Label the plate separation as $d$ and the potential difference as $V$. Show a test charge $+q$ experiencing a constant force $F = qE$.

**中文:**
显示两块连接到直流电源的平行金属板的示意图。正极板连接到正极端子，负极板连接到负极端子。在极板之间，画出等间距的平行箭头，从正极板指向负极板。将极板间距标记为 $d$，电势差标记为 $V$。显示一个试探电荷 $+q$ 受到恒定的力 $F = qE$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — URF-05: Uniform Electric Field Between Parallel Plates**
> A clear physics diagram showing two parallel metal plates (rectangular, gray) separated by distance d. The top plate is labeled "+" and connected to the positive terminal of a battery symbol. The bottom plate is labeled "−" and connected to the negative terminal. Between the plates, draw 5-7 equally spaced vertical arrows pointing downward from positive to negative. Label the arrows "E (uniform)". Show a small positive charge +q between the plates with a force vector F = qE pointing downward. Add labels: "V = potential difference", "d = plate separation". Include a note: "Field is uniform in central region; fringing at edges."

### Labels Required / 需要标注
- **English:** + plate, − plate, $d$ (separation), $V$ (p.d.), $E$ (field), $F = qE$ (force on test charge)
- **中文:** +极板, −极板, $d$ (间距), $V$ (电势差), $E$ (场), $F = qE$ (对试探电荷的力)

### Exam Importance / 考试重要性
- **English:** High — students are often asked to draw or interpret this diagram. Key points: parallel lines, equal spacing, direction from + to −.
- **中文:** 高——学生经常被要求绘制或解释此图。关键点：平行线、等间距、方向从 + 到 −。

---

## 7.2 Radial Electric Field Diagram / 径向电场示意图

### Description / 描述
**English:**
A diagram showing a point charge at the center. For a positive charge, draw radial arrows pointing outward in all directions. For a negative charge, draw radial arrows pointing inward. Show that the arrows are closer together near the charge (stronger field) and spread apart at greater distances (weaker field). Label the distance $r$ from the charge.

**中文:**
显示中心点电荷的示意图。对于正电荷，画出向所有方向辐射的箭头。对于负电荷，画出指向中心的箭头。显示箭头在靠近电荷处更密集（场更强），在更远处散开（场更弱）。标记距电荷的距离 $r$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — URF-06: Radial Electric Field Around Point Charges**
> Two side-by-side diagrams. Left: A positive point charge +Q at center with 8-12 radial arrows pointing outward in all directions. Arrows are closer together near the charge and spread apart farther away. Label one arrow "E" and show distance r. Right: A negative point charge −Q at center with 8-12 radial arrows pointing inward toward the charge. Add labels: "Radial field", "E ∝ 1/r²", "Non-uniform". Include a note: "Field lines never cross."

### Labels Required / 需要标注
- **English:** $+Q$ or $-Q$ (source charge), $r$ (distance), $E$ (field vector), "Field lines closer = stronger field"
- **中文:** $+Q$ 或 $-Q$ (源电荷), $r$ (距离), $E$ (场矢量), "场线越密 = 场越强"

### Exam Importance / 考试重要性
- **English:** High — students must be able to sketch radial fields and explain why field strength varies.
- **中文:** 高——学生必须能够绘制径向场并解释场强为何变化。

---

# 8. Worked Examples / 典型例题

## Example 1: Comparing Field Strengths / 比较场强

### Question / 题目
**English:**
A uniform electric field is created between two parallel plates separated by 5.0 cm with a potential difference of 200 V. A radial electric field is produced by a point charge of $+2.0 \times 10^{-9}$ C. Calculate:
(a) The electric field strength in the uniform field.
(b) The distance from the point charge where the radial field strength equals the uniform field strength.
($\epsilon_0 = 8.85 \times 10^{-12}$ F m$^{-1}$)

**中文:**
两块平行板间距为 5.0 cm，电势差为 200 V，产生匀强电场。一个 $+2.0 \times 10^{-9}$ C 的点电荷产生径向电场。计算：
(a) 匀强电场中的电场强度。
(b) 径向场强等于匀强场强时距点电荷的距离。
($\epsilon_0 = 8.85 \times 10^{-12}$ F m$^{-1}$)

### Solution / 解答

**Part (a):**
$$ E_{\text{uniform}} = \frac{V}{d} = \frac{200}{0.050} = 4000 \text{ V m}^{-1} $$

**Part (b):**
Set $E_{\text{radial}} = E_{\text{uniform}}$:
$$ \frac{Q}{4\pi\epsilon_0 r^2} = 4000 $$

$$ r^2 = \frac{Q}{4\pi\epsilon_0 \times 4000} $$

$$ r^2 = \frac{2.0 \times 10^{-9}}{4\pi \times 8.85 \times 10^{-12} \times 4000} $$

$$ r^2 = \frac{2.0 \times 10^{-9}}{4.45 \times 10^{-7}} $$

$$ r^2 = 4.49 \times 10^{-3} $$

$$ r = \sqrt{4.49 \times 10^{-3}} = 0.067 \text{ m} = 6.7 \text{ cm} $$

### Final Answer / 最终答案
**Answer:** (a) $E = 4000$ V m$^{-1}$ | (b) $r = 6.7$ cm
**答案：** (a) $E = 4000$ V m$^{-1}$ | (b) $r = 6.7$ cm

### Quick Tip / 提示
- **English:** Always convert cm to m before calculating. For radial fields, remember $r$ is measured from the center of the charge.
- **中文:** 计算前务必将 cm 转换为 m。对于径向场，记住 $r$ 是从电荷中心测量的。

---

## Example 2: Force on a Test Charge / 对试探电荷的力

### Question / 题目
**English:**
A proton ($q = +1.6 \times 10^{-19}$ C) is placed:
(a) In a uniform field of $E = 5000$ N C$^{-1}$.
(b) At a distance of 0.10 m from a point charge of $+5.0 \times 10^{-8}$ C.
Calculate the force on the proton in each case.

**中文:**
一个质子 ($q = +1.6 \times 10^{-19}$ C) 被放置在：
(a) 匀强电场 $E = 5000$ N C$^{-1}$ 中。
(b) 距 $+5.0 \times 10^{-8}$ C 点电荷 0.10 m 处。
计算每种情况下质子所受的力。

### Solution / 解答

**Part (a) — Uniform field:**
$$ F = qE = (1.6 \times 10^{-19})(5000) = 8.0 \times 10^{-16} \text{ N} $$

**Part (b) — Radial field:**
First find $E$ at $r = 0.10$ m:
$$ E = \frac{Q}{4\pi\epsilon_0 r^2} = \frac{5.0 \times 10^{-8}}{4\pi(8.85 \times 10^{-12})(0.10)^2} $$

$$ E = \frac{5.0 \times 10^{-8}}{1.11 \times 10^{-12}} = 4.50 \times 10^4 \text{ N C}^{-1} $$

Then:
$$ F = qE = (1.6 \times 10^{-19})(4.50 \times 10^4) = 7.20 \times 10^{-15} \text{ N} $$

### Final Answer / 最终答案
**Answer:** (a) $F = 8.0 \times 10^{-16}$ N | (b) $F = 7.2 \times 10^{-15}$ N
**答案：** (a) $F = 8.0 \times 10^{-16}$ N | (b) $F = 7.2 \times 10^{-15}$ N

### Quick Tip / 提示
- **English:** In a uniform field, force is constant regardless of position. In a radial field, force depends on distance — always calculate $E$ first using $E = Q/(4\pi\epsilon_0 r^2)$.
- **中文:** 在匀强电场中，力与位置无关，是恒定的。在径向电场中，力取决于距离——始终先用 $E = Q/(4\pi\epsilon_0 r^2)$ 计算 $E$。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Sketch field patterns / 绘制场模式 | High | Easy | 📝 *待填入* |
| Calculate E using $E = V/d$ / 用 $E = V/d$ 计算 E | High | Medium | 📝 *待填入* |
| Calculate E using $E = Q/(4\pi\epsilon_0 r^2)$ / 用 $E = Q/(4\pi\epsilon_0 r^2)$ 计算 E | Medium | Medium | 📝 *待填入* |
| Compare forces in uniform vs radial fields / 比较匀强与径向场中的力 | Medium | Medium-Hard | 📝 *待填入* |
| Interpret E-r graphs / 解释 E-r 图 | Low-Medium | Medium | 📝 *待填入* |
| Trajectory of charged particle in uniform field / 带电粒子在匀强场中的轨迹 | Medium | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Sketch, Calculate, Determine, Compare, Explain, State
- **中文:** 画出、计算、确定、比较、解释、写出

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in several ways:

1. **Measuring Uniform Field Strength:** Use a search electrode (a small conducting sphere) connected to a voltmeter to measure potential at different points between parallel plates. Plotting potential against distance gives a straight line; the gradient gives $E$.

2. **Investigating Radial Fields:** Use a charged sphere and a search electrode to measure potential at various distances. Plot $V$ against $1/r$ to verify the inverse relationship.

3. **Uncertainties:** When measuring $d$ (plate separation), use a micrometer for precision. For $V$, use a high-impedance voltmeter to avoid drawing current. Calculate percentage uncertainties in $E = V/d$ using $\frac{\Delta E}{E} = \frac{\Delta V}{V} + \frac{\Delta d}{d}$.

4. **Graph Plotting:** For uniform fields, plot $V$ vs $d$ — expect a linear graph through origin. For radial fields, plot $E$ vs $1/r^2$ — expect a linear graph.

**中文:**
本子知识点通过多种方式与实验工作联系：

1. **测量匀强场强：** 使用连接到电压表的搜索电极（小导体球）测量平行板间不同点的电势。绘制电势与距离的关系图得到一条直线；斜率给出 $E$。

2. **研究径向场：** 使用带电球体和搜索电极测量不同距离处的电势。绘制 $V$ 与 $1/r$ 的关系图以验证反比关系。

3. **不确定度：** 测量 $d$（板间距）时，使用千分尺提高精度。对于 $V$，使用高阻抗电压表以避免吸取电流。使用 $\frac{\Delta E}{E} = \frac{\Delta V}{V} + \frac{\Delta d}{d}$ 计算 $E = V/d$ 的百分比不确定度。

4. **绘图：** 对于匀强场，绘制 $V$ 与 $d$ 的关系图——预期得到一条通过原点的直线。对于径向场，绘制 $E$ 与 $1/r^2$ 的关系图——预期得到一条直线。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main topic
    URF[Uniform vs Radial Electric Fields] --> UF[Uniform Electric Field]
    URF --> RF[Radial Electric Field]
    
    %% Uniform field connections
    UF --> PP[Parallel Plates]
    PP --> E_uni[E = V/d]
    E_uni --> ConstForce[Constant Force F = qE]
    ConstForce --> ParaTraj[Parabolic Trajectories]
    
    %% Radial field connections
    RF --> PC[Point Charge]
    RF --> CS[Charged Sphere]
    PC --> E_rad[E = Q/(4πε₀r²)]
    E_rad --> VarForce[Force ∝ 1/r²]
    E_rad --> InvSquare[Inverse Square Law]
    
    %% Cross connections
    E_uni --> |Compare| E_rad
    UF --> |Field lines: parallel, equally spaced| FieldLines[Field Line Patterns]
    RF --> |Field lines: radial, spreading| FieldLines
    
    %% External links
    PP --> ElectricFieldBetweenParallelPlates[[Electric Field Between Parallel Plates]]
    PC --> CoulombsLaw[[Coulomb's Law]]
    E_uni --> ElectricPotential[[Electric Potential]]
    E_rad --> ElectricPotential
    ConstForce --> CapacitanceAndCapacitors[[Capacitance and Capacitors]]
    
    %% Prerequisites
    FieldLines --> ElectricFieldConceptAndFieldLines[[Electric Field Concept and Field Lines]]
    InvSquare --> ScalarsAndVectors[[Scalars and Vectors]]
    InvSquare --> GravitationalForceAndField[[Gravitational Force and Field]]
    
    %% Styling
    classDef main fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef uniform fill:#fff3e0,stroke:#e65100,stroke-width:1px
    classDef radial fill:#f3e5f5,stroke:#4a148c,stroke-width:1px
    classDef external fill:#e8f5e9,stroke:#1b5e20,stroke-width:1px
    
    class URF main
    class UF,PP,E_uni,ConstForce,ParaTraj uniform
    class RF,PC,CS,E_rad,VarForce,InvSquare radial
    class ElectricFieldBetweenParallelPlates,CoulombsLaw,ElectricPotential,CapacitanceAndCapacitors,ElectricFieldConceptAndFieldLines,ScalarsAndVectors,GravitationalForceAndField external
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Uniform:** Constant $E$ everywhere between parallel plates. **Radial:** $E$ varies with $1/r^2$ from a point charge. / **匀强：** 平行板间各处 $E$ 恒定。**径向：** $E$ 随距点电荷的距离按 $1/r^2$ 变化。 |
| **Key Formula / 核心公式** | **Uniform:** $E = \frac{V}{d}$ (only for parallel plates). **Radial:** $E = \frac{Q}{4\pi\epsilon_0 r^2}$ (for point charge or outside sphere). / **匀强：** $E = \frac{V}{d}$（仅适用于平行板）。**径向：** $E = \frac{Q}{4\pi\epsilon_0 r^2}$（适用于点电荷或球外）。 |
| **Key Graph / 核心图表** | **Uniform:** $E$ vs $r$ — horizontal line. **Radial:** $E$ vs $r$ — decreasing $1/r^2$ curve. / **匀强：** $E$-$r$ 图——水平线。**径向：** $E$-$r$ 图——递减的 $1/r^2$ 曲线。 |
| **Field Lines / 场线** | **Uniform:** Parallel, equally spaced, from + to −. **Radial:** Radial lines, closer near charge, spreading out. / **匀强：** 平行、等间距，从 + 到 −。**径向：** 径向线，靠近电荷处密集，向外散开。 |
| **Force on Test Charge / 对试探电荷的力** | **Uniform:** Constant $F = qE$. **Radial:** $F = \frac{Qq}{4\pi\epsilon_0 r^2}$ — varies with distance. / **匀强：** 恒定 $F = qE$。**径向：** $F = \frac{Qq}{4\pi\epsilon_0 r^2}$ — 随距离变化。 |
| **Exam Tip / 考试提示** | Always identify field type first. Use $E = V/d$ only for uniform fields. For radial fields, $r$ is from charge center. Convert units (cm → m) before calculation. / 始终先识别场类型。仅对匀强场使用 $E = V/d$。对于径向场，$r$ 从电荷中心算起。计算前转换单位（cm → m）。 |
| **Common Mistake / 常见错误** | Applying $E = V/d$ to radial fields. Forgetting $r$ is from center, not surface. Drawing crossing field lines. / 将 $E = V/d$ 应用于径向场。忘记 $r$ 是从中心算起，不是从表面。画出交叉的场线。 |
| **Practical Link / 实验联系** | Use search electrode + voltmeter to measure potential. Plot $V$ vs $d$ for uniform field (linear). Plot $E$ vs $1/r^2$ for radial field (linear). / 使用搜索电极 + 电压表测量电势。匀强场绘制 $V$-$d$ 图（线性）。径向场绘制 $E$-$1/r^2$ 图（线性）。 |

---

> 📋 **CIE Only:** CAIE 9702 specifically requires students to describe field patterns using field lines (18.1e) and distinguish between uniform and radial fields (18.1b). The formula $E = \frac{Q}{4\pi\epsilon_0 r^2}$ is given in the formula booklet.
>
> 📋 **Edexcel Only:** Edexcel IAL WPH14 Unit 4 requires understanding of both field types for applications including charged particles in accelerators and deflection in cathode ray tubes. The constant $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$ N m$^2$ C$^{-2}$ is provided in the data booklet.