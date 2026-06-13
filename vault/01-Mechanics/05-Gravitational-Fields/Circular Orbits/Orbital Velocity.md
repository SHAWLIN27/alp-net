# 1. Overview / 概述

**English:**
Orbital velocity is the minimum velocity required for an object to maintain a stable circular orbit around a larger celestial body under the influence of gravity. This sub-topic explores the derivation and application of the orbital velocity formula, which is fundamental to understanding satellite motion, planetary orbits, and space exploration. Orbital velocity connects [[Gravitational Force and Field]] with [[Centripetal Acceleration and Force]] to explain why objects in orbit do not fall to the ground but instead continuously "fall" around the Earth. Understanding orbital velocity is essential for calculating satellite altitudes, launch requirements, and orbital periods, and it serves as a prerequisite for studying [[Kepler's Third Law]] and [[Geostationary Satellites]].

**中文:**
轨道速度是物体在引力作用下围绕较大天体维持稳定圆形轨道所需的最小速度。本子知识点探讨轨道速度公式的推导和应用，这对于理解卫星运动、行星轨道和太空探索至关重要。轨道速度将[[Gravitational Force and Field|引力场]]与[[Centripetal Acceleration and Force|向心加速度和力]]联系起来，解释了为什么轨道上的物体不会掉到地面，而是持续地"绕"地球下落。理解轨道速度对于计算卫星高度、发射要求和轨道周期至关重要，并且是学习[[Kepler's Third Law|开普勒第三定律]]和[[Geostationary Satellites|地球静止卫星]]的先决条件。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 15.3(a) Derive the relationship between orbital speed, radius, and mass of the central body | 6.11 Derive and use the equation for orbital speed: $v = \sqrt{\frac{GM}{r}}$ |
| 15.3(b) Calculate orbital speed for satellites in circular orbits | 6.12 Calculate orbital speed for satellites and planets |
| 15.3(c) Explain why orbital speed decreases with increasing orbital radius | 6.13 Explain the relationship between orbital radius and speed |
| 15.3(d) Apply the orbital speed equation to problems involving satellites and planets | 6.14 Solve problems involving orbital motion |
| 15.3(e) Distinguish between orbital speed and escape speed | 6.15 Compare orbital speed with escape speed |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to derive the orbital velocity formula from equating gravitational force to centripetal force. They should understand that orbital velocity depends only on the mass of the central body and the orbital radius, not on the mass of the orbiting object. Common exam questions involve calculating orbital speed for satellites at different altitudes and explaining why geostationary satellites must orbit at a specific radius.
- **中文:** 学生必须能够通过将引力等于向心力来推导轨道速度公式。他们应该理解轨道速度仅取决于中心天体的质量和轨道半径，而不取决于轨道物体的质量。常见的考试问题涉及计算不同高度卫星的轨道速度，并解释为什么地球静止卫星必须在特定半径上运行。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Orbital Velocity** / 轨道速度 | The minimum velocity required for an object to maintain a stable circular orbit around a larger celestial body, where the gravitational force provides the necessary centripetal force. | 物体围绕较大天体维持稳定圆形轨道所需的最小速度，此时引力提供所需的向心力。 | Confusing orbital velocity with escape velocity — orbital velocity is for circular orbits, escape velocity is to leave the gravitational field entirely. |
| **Centripetal Force** / 向心力 | The net force directed toward the center of a circular path that keeps an object in circular motion. | 指向圆形路径中心的合力，使物体保持圆周运动。 | Thinking centripetal force is a separate force — it is the net force from other forces (here, gravity). |
| **Gravitational Force** / 引力 | The attractive force between two masses, described by Newton's law of universal gravitation: $F = \frac{GMm}{r^2}$. | 两个质量之间的吸引力，由牛顿万有引力定律描述。 | Forgetting that $r$ is the distance between centers of mass, not the surface-to-surface distance. |
| **Orbital Radius** / 轨道半径 | The distance from the center of the central body to the center of the orbiting object. | 从中心天体中心到轨道物体中心的距离。 | Using altitude (height above surface) instead of orbital radius — must add the planet's radius. |
| **Escape Velocity** / 逃逸速度 | The minimum velocity required for an object to escape the gravitational field of a celestial body without further propulsion. | 物体无需进一步推进即可逃离天体引力场所需的最小速度。 | Confusing with orbital velocity — escape velocity is $\sqrt{2}$ times orbital velocity at the same radius. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Derivation of Orbital Velocity / 轨道速度的推导

### Explanation / 解释
**English:**
For an object in a stable circular orbit, the gravitational force from the central body provides exactly the centripetal force needed to keep the object moving in a circle. This is the fundamental insight: gravity IS the centripetal force. Starting from Newton's law of gravitation and the centripetal force equation:

$$F_{\text{grav}} = \frac{GMm}{r^2} \quad \text{and} \quad F_{\text{cent}} = \frac{mv^2}{r}$$

Since $F_{\text{grav}} = F_{\text{cent}}$:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

Cancelling $m$ (the mass of the orbiting object) and one factor of $r$:

$$\frac{GM}{r} = v^2$$

Therefore:

$$v = \sqrt{\frac{GM}{r}}$$

This derivation shows a crucial result: **orbital velocity does not depend on the mass of the orbiting object**. A small satellite and a large space station at the same orbital radius have the same orbital speed.

**中文:**
对于稳定圆形轨道上的物体，来自中心天体的引力恰好提供了使物体保持圆周运动所需的向心力。这是基本的洞察：引力就是向心力。从牛顿万有引力定律和向心力方程开始：

$$F_{\text{grav}} = \frac{GMm}{r^2} \quad \text{和} \quad F_{\text{cent}} = \frac{mv^2}{r}$$

由于 $F_{\text{grav}} = F_{\text{cent}}$：

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

消去 $m$（轨道物体的质量）和一个 $r$ 因子：

$$\frac{GM}{r} = v^2$$

因此：

$$v = \sqrt{\frac{GM}{r}}$$

这个推导显示了一个关键结果：**轨道速度不依赖于轨道物体的质量**。在相同轨道半径上的小卫星和大空间站具有相同的轨道速度。

### Physical Meaning / 物理意义
**English:**
The orbital velocity equation reveals that:
1. **Inverse relationship with radius**: As orbital radius increases, orbital velocity decreases. This is why satellites in low Earth orbit (LEO) travel much faster than geostationary satellites.
2. **Dependence on central mass**: The orbital velocity depends only on the mass of the central body. For a given radius, a more massive planet requires a higher orbital speed.
3. **Mass independence**: The orbiting object's mass cancels out — a feather and a spacecraft at the same orbital radius would orbit at the same speed (in vacuum).

**中文:**
轨道速度方程揭示了：
1. **与半径的反比关系**：随着轨道半径增加，轨道速度减小。这就是为什么低地球轨道（LEO）的卫星比地球静止卫星运动得快得多。
2. **对中心质量的依赖**：轨道速度仅取决于中心天体的质量。对于给定的半径，质量更大的行星需要更高的轨道速度。
3. **质量独立性**：轨道物体的质量被消去——在相同轨道半径上的羽毛和航天器将以相同的速度运行（在真空中）。

### Common Misconceptions / 常见误区
- **English:**
  - ❌ "Orbital velocity is the speed needed to launch a satellite." — No, launch requires much higher speeds to overcome gravity during ascent.
  - ❌ "A heavier satellite needs a higher orbital speed." — No, orbital speed is independent of satellite mass.
  - ❌ "Orbital velocity is constant for all orbits." — No, it decreases as orbital radius increases.
  - ❌ "The orbital radius is the altitude above the surface." — No, it's the distance from the center of the planet.

- **中文:**
  - ❌ "轨道速度是发射卫星所需的速度。" — 不对，发射需要更高的速度来克服上升过程中的引力。
  - ❌ "较重的卫星需要更高的轨道速度。" — 不对，轨道速度与卫星质量无关。
  - ❌ "所有轨道的轨道速度都是恒定的。" — 不对，它随着轨道半径的增加而减小。
  - ❌ "轨道半径是地表以上的高度。" — 不对，它是从行星中心到卫星的距离。

### Exam Tips / 考试提示
- **English:**
  - Always use the orbital radius (center-to-center distance), not altitude
  - Remember: $r = R_{\text{planet}} + h$ where $h$ is altitude above surface
  - Check units: $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$, mass in kg, radius in m
  - For Earth: $M_E = 5.97 \times 10^{24} \text{ kg}$, $R_E = 6.37 \times 10^6 \text{ m}$
  - The derivation is a common exam question — practice writing it step by step

- **中文:**
  - 始终使用轨道半径（中心到中心的距离），而不是高度
  - 记住：$r = R_{\text{行星}} + h$，其中 $h$ 是地表以上的高度
  - 检查单位：$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$，质量用kg，半径用m
  - 对于地球：$M_E = 5.97 \times 10^{24} \text{ kg}$，$R_E = 6.37 \times 10^6 \text{ m}$
  - 推导是常见的考试题目——练习逐步写出推导过程

> 📷 **IMAGE PROMPT — DIAGRAM-01: Orbital Velocity Derivation Diagram**
> A clear physics diagram showing a satellite of mass m orbiting a planet of mass M at orbital radius r. The satellite is shown with velocity vector v tangential to the circular orbit. Two force arrows are shown: the gravitational force F_grav pointing from satellite toward planet center, and the centripetal force F_cent also pointing toward planet center. A callout box shows the equation F_grav = F_cent leading to v = sqrt(GM/r). The diagram should clearly label: M (planet mass), m (satellite mass), r (orbital radius), v (orbital velocity), and the two force vectors. Style: clean educational physics diagram, white background, blue planet, grey satellite, red force arrows.

---

# 5. Essential Equations / 核心公式

## 5.1 Orbital Velocity Equation / 轨道速度方程

$$v = \sqrt{\frac{GM}{r}}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v$ | Orbital velocity | 轨道速度 | $\text{m s}^{-1}$ |
| $G$ | Universal gravitational constant | 万有引力常数 | $\text{N m}^2 \text{ kg}^{-2}$ |
| $M$ | Mass of central body | 中心天体质量 | $\text{kg}$ |
| $r$ | Orbital radius (center-to-center) | 轨道半径（中心到中心） | $\text{m}$ |

**Derivation / 推导:**
As shown in Section 4.1, equating gravitational force to centripetal force:
$$\frac{GMm}{r^2} = \frac{mv^2}{r} \Rightarrow v^2 = \frac{GM}{r} \Rightarrow v = \sqrt{\frac{GM}{r}}$$

**Conditions / 适用条件:**
- **English:** The equation applies only to circular orbits. For elliptical orbits, the speed varies with position. The central body must be much more massive than the orbiting object ($M \gg m$). The derivation assumes no other forces (e.g., atmospheric drag, solar radiation pressure).
- **中文:** 该方程仅适用于圆形轨道。对于椭圆轨道，速度随位置变化。中心天体必须比轨道物体质量大得多（$M \gg m$）。推导假设没有其他力（例如大气阻力、太阳辐射压力）。

**Limitations / 局限性:**
- **English:** Does not account for non-uniform gravitational fields, relativistic effects, or perturbations from other bodies. For very low orbits, atmospheric drag becomes significant and the orbit decays.
- **中文:** 不考虑非均匀引力场、相对论效应或其他天体的扰动。对于非常低的轨道，大气阻力变得显著，轨道会衰减。

## 5.2 Relationship Between Orbital Velocity and Period / 轨道速度与周期的关系

$$v = \frac{2\pi r}{T}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T$ | Orbital period | 轨道周期 | $\text{s}$ |
| $r$ | Orbital radius | 轨道半径 | $\text{m}$ |

**Derivation / 推导:**
For a circular orbit, the distance traveled in one orbit is the circumference $2\pi r$, and the time taken is the period $T$. Speed = distance/time.

**Conditions / 适用条件:**
- **English:** Only for circular orbits. This is a kinematic relationship that applies to any circular motion, not just orbital motion.
- **中文:** 仅适用于圆形轨道。这是一个运动学关系，适用于任何圆周运动，不仅限于轨道运动。

> 📋 **CIE Only:** Students are expected to derive the orbital velocity equation from first principles in exam questions. The derivation is often worth 3-4 marks.

> 📋 **Edexcel Only:** Students should be able to combine $v = \sqrt{GM/r}$ with $v = 2\pi r/T$ to derive Kepler's Third Law: $T^2 = \frac{4\pi^2}{GM}r^3$.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Orbital Velocity vs Orbital Radius / 轨道速度与轨道半径的关系

### Axes / 坐标轴
- **X-axis:** Orbital radius $r$ (m) — 轨道半径 $r$ (m)
- **Y-axis:** Orbital velocity $v$ (m s⁻¹) — 轨道速度 $v$ (m s⁻¹)

### Shape / 形状
- **English:** A decreasing curve that follows $v \propto 1/\sqrt{r}$. The curve is steep at small radii (near the planet's surface) and becomes increasingly shallow at large radii. As $r \to \infty$, $v \to 0$.
- **中文:** 一条遵循 $v \propto 1/\sqrt{r}$ 的递减曲线。曲线在小半径（靠近行星表面）处陡峭，在大半径处变得越来越平缓。当 $r \to \infty$ 时，$v \to 0$。

### Gradient Meaning / 斜率含义
- **English:** The gradient $\frac{dv}{dr} = -\frac{1}{2}\sqrt{\frac{GM}{r^3}}$ is always negative, showing that orbital velocity decreases as radius increases. The magnitude of the gradient decreases with increasing radius.
- **中文:** 梯度 $\frac{dv}{dr} = -\frac{1}{2}\sqrt{\frac{GM}{r^3}}$ 始终为负，表明轨道速度随半径增加而减小。梯度的大小随半径增加而减小。

### Area Meaning / 面积含义
- **English:** The area under the $v$ vs $r$ graph has no direct physical meaning for orbital motion.
- **中文:** $v$ 与 $r$ 关系图下的面积对于轨道运动没有直接的物理意义。

### Exam Interpretation / 考试解读
- **English:** Students may be asked to sketch this graph for different planets. A more massive planet gives a higher curve at the same radius. The graph can be used to find the orbital speed at a given altitude, or to determine the orbital radius for a required speed (e.g., geostationary orbit).
- **中文:** 学生可能会被要求为不同行星绘制此图。质量更大的行星在相同半径处给出更高的曲线。该图可用于找到给定高度的轨道速度，或确定所需速度的轨道半径（例如地球静止轨道）。

> 📷 **IMAGE PROMPT — GRAPH-01: Orbital Velocity vs Radius**
> A graph showing orbital velocity v (y-axis) against orbital radius r (x-axis). The curve follows v = sqrt(GM/r), starting high near the planet's surface (r = R_E) and decreasing asymptotically toward zero as r increases. Two curves should be shown: one for Earth (M_E) and one for a more massive planet (2M_E) to show that higher mass gives higher orbital speed at the same radius. Key points should be marked: LEO (low Earth orbit) at r ≈ 6600 km, and GEO (geostationary) at r ≈ 42000 km. Style: clean physics graph with labeled axes, grid lines, and legend.

---

# 7. Required Diagrams / 必备图表

## 7.1 Orbital Velocity Vector Diagram / 轨道速度矢量图

### Description / 描述
- **English:** A diagram showing a satellite in circular orbit around Earth, with the velocity vector always tangential to the orbit and the gravitational force vector always pointing toward Earth's center. This illustrates that the satellite is constantly "falling" toward Earth but moving sideways fast enough to keep missing it.
- **中文:** 显示卫星绕地球圆形轨道的图，速度矢量始终与轨道相切，引力矢量始终指向地球中心。这说明了卫星不断"落向"地球，但横向移动速度足够快，以至于不断"错过"地球。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-02: Orbital Velocity Vector Diagram**
> A satellite in circular orbit around Earth. The satellite is shown at four positions (top, right, bottom, left) around the orbit. At each position, two arrows are drawn: a tangential velocity vector v (green arrow, pointing in direction of motion) and a radial gravitational force vector F_g (red arrow, pointing toward Earth's center). The velocity vectors are all the same length (constant speed). The force vectors are all the same length (constant force). A note at the bottom reads: "The satellite is constantly falling toward Earth, but moving sideways fast enough to keep missing it." Earth should be drawn as a blue sphere with continents visible. Style: educational physics diagram, clean, labeled, with arrows clearly distinguished by color.

### Labels Required / 需要标注
- **English:** Earth (center), satellite (orbiting object), orbital radius $r$, velocity vector $\vec{v}$ (tangential), gravitational force $\vec{F}_g$ (radial inward), orbit path (dashed circle)
- **中文:** 地球（中心），卫星（轨道物体），轨道半径 $r$，速度矢量 $\vec{v}$（切向），引力 $\vec{F}_g$（径向向内），轨道路径（虚线圆）

### Exam Importance / 考试重要性
- **English:** This diagram is essential for understanding why satellites stay in orbit. It is often used in exam questions to test understanding of the relationship between velocity, force, and orbital motion. Students should be able to draw and label this diagram from memory.
- **中文:** 这个图对于理解卫星为什么保持在轨道上至关重要。它经常在考试题中用于测试对速度、力和轨道运动之间关系的理解。学生应该能够凭记忆绘制并标注这个图。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Orbital Velocity / 例题1：计算轨道速度

### Question / 题目
**English:**
A weather satellite is placed in a circular orbit 300 km above the Earth's surface. Calculate the orbital velocity of the satellite.

Given: $M_E = 5.97 \times 10^{24} \text{ kg}$, $R_E = 6.37 \times 10^6 \text{ m}$, $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$

**中文:**
一颗气象卫星被放置在距地球表面300公里的圆形轨道上。计算该卫星的轨道速度。

已知：$M_E = 5.97 \times 10^{24} \text{ kg}$，$R_E = 6.37 \times 10^6 \text{ m}$，$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$

### Solution / 解答

**Step 1: Determine the orbital radius / 确定轨道半径**
$$r = R_E + h = 6.37 \times 10^6 + 300 \times 10^3 = 6.67 \times 10^6 \text{ m}$$

**Step 2: Apply the orbital velocity equation / 应用轨道速度方程**
$$v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{6.67 \times 10^6}}$$

**Step 3: Calculate / 计算**
$$v = \sqrt{\frac{3.98 \times 10^{14}}{6.67 \times 10^6}} = \sqrt{5.97 \times 10^7} = 7.73 \times 10^3 \text{ m s}^{-1}$$

### Final Answer / 最终答案
**Answer:** $v = 7.73 \times 10^3 \text{ m s}^{-1}$ (approximately 7.73 km/s) | **答案：** $v = 7.73 \times 10^3 \text{ m·s}^{-1}$（约7.73公里/秒）

### Quick Tip / 提示
- **English:** Always convert altitude to meters and add to Earth's radius. A common mistake is using altitude directly as the orbital radius.
- **中文:** 始终将高度转换为米并加到地球半径上。一个常见错误是直接将高度用作轨道半径。

---

## Example 2: Finding Orbital Radius from Velocity / 例题2：从速度求轨道半径

### Question / 题目
**English:**
A satellite orbits Earth with an orbital speed of 3.07 km/s. Calculate the orbital radius and the altitude of the satellite above Earth's surface.

Given: $M_E = 5.97 \times 10^{24} \text{ kg}$, $R_E = 6.37 \times 10^6 \text{ m}$, $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$

**中文:**
一颗卫星以3.07公里/秒的轨道速度绕地球运行。计算轨道半径和卫星距地球表面的高度。

已知：$M_E = 5.97 \times 10^{24} \text{ kg}$，$R_E = 6.37 \times 10^6 \text{ m}$，$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$

### Solution / 解答

**Step 1: Rearrange the orbital velocity equation / 重新排列轨道速度方程**
$$v = \sqrt{\frac{GM}{r}} \Rightarrow v^2 = \frac{GM}{r} \Rightarrow r = \frac{GM}{v^2}$$

**Step 2: Convert velocity to m/s / 将速度转换为米/秒**
$$v = 3.07 \text{ km/s} = 3.07 \times 10^3 \text{ m/s}$$

**Step 3: Calculate orbital radius / 计算轨道半径**
$$r = \frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{(3.07 \times 10^3)^2} = \frac{3.98 \times 10^{14}}{9.42 \times 10^6} = 4.23 \times 10^7 \text{ m}$$

**Step 4: Calculate altitude / 计算高度**
$$h = r - R_E = 4.23 \times 10^7 - 6.37 \times 10^6 = 3.59 \times 10^7 \text{ m} = 3.59 \times 10^4 \text{ km}$$

### Final Answer / 最终答案
**Answer:** $r = 4.23 \times 10^7 \text{ m}$, $h = 3.59 \times 10^7 \text{ m}$ (approximately 35,900 km) | **答案：** $r = 4.23 \times 10^7 \text{ m}$，$h = 3.59 \times 10^7 \text{ m}$（约35,900公里）

### Quick Tip / 提示
- **English:** This is the orbital radius for a geostationary satellite! The calculated altitude of ~36,000 km matches the known geostationary orbit altitude. Remember this value for exam questions.
- **中文:** 这就是地球静止卫星的轨道半径！计算出的约36,000公里高度与已知的地球静止轨道高度相符。记住这个值用于考试题。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Derivation of orbital velocity equation | ★★★★★ Very High | ★★★ Medium | 📝 *待填入* |
| Calculation of orbital speed from given data | ★★★★★ Very High | ★★ Easy | 📝 *待填入* |
| Comparison of orbital speeds at different radii | ★★★★ High | ★★★ Medium | 📝 *待填入* |
| Finding orbital radius from speed or period | ★★★★ High | ★★★★ Hard | 📝 *待填入* |
| Orbital velocity for different planets | ★★★ Medium | ★★★ Medium | 📝 *待填入* |
| Distinguishing orbital vs escape velocity | ★★ Low | ★★ Easy | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Derive, Calculate, Determine, Show that, Explain why, Compare, Sketch
- **中文:** 推导，计算，确定，证明，解释为什么，比较，绘制草图

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
While orbital velocity cannot be directly measured in a school laboratory, the concept connects to several practical skills:

1. **Data Analysis**: Students can analyze orbital data from satellites (e.g., ISS altitude and speed) to verify the $v \propto 1/\sqrt{r}$ relationship.
2. **Graph Plotting**: Plotting $v^2$ against $1/r$ should give a straight line through the origin with gradient $GM$, allowing determination of the central body's mass.
3. **Uncertainty Analysis**: When calculating orbital velocity from given data, students should consider uncertainties in $G$, $M$, and $r$, and propagate them to find the uncertainty in $v$.
4. **Simulation Software**: Many schools use orbital simulation software (e.g., PhET, Stellarium) to visualize how changing orbital radius affects speed.
5. **Experimental Analogy**: A simple experiment using a mass on a string swung in a circle can demonstrate the relationship between speed and radius for a given centripetal force (tension in string ≈ gravitational force).

**中文:**
虽然轨道速度无法在学校实验室直接测量，但该概念与多项实验技能相关：

1. **数据分析**：学生可以分析卫星的轨道数据（例如国际空间站的高度和速度）来验证 $v \propto 1/\sqrt{r}$ 关系。
2. **图表绘制**：绘制 $v^2$ 与 $1/r$ 的关系图应得到一条通过原点的直线，斜率为 $GM$，从而可以确定中心天体的质量。
3. **不确定度分析**：在根据给定数据计算轨道速度时，学生应考虑 $G$、$M$ 和 $r$ 的不确定度，并传播它们以找到 $v$ 的不确定度。
4. **模拟软件**：许多学校使用轨道模拟软件（例如PhET、Stellarium）来可视化改变轨道半径如何影响速度。
5. **实验类比**：使用在圆周上摆动的绳子上的质量的简单实验可以演示给定向心力（绳子张力≈引力）下速度与半径之间的关系。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Orbital Velocity Concept Map
    OV[Orbital Velocity<br/>轨道速度] --> DER[Derivation<br/>推导]
    OV --> APP[Applications<br/>应用]
    OV --> REL[Relationships<br/>关系]
    
    DER --> GF[Gravitational Force<br/>引力 F = GMm/r²]
    DER --> CF[Centripetal Force<br/>向心力 F = mv²/r]
    DER --> EQ[Equate Forces<br/>力相等]
    DER --> FORM[Formula<br/>v = √(GM/r)]
    
    APP --> SAT[Satellite Orbits<br/>卫星轨道]
    APP --> GEO[Geostationary<br/>地球静止卫星]
    APP --> PLAN[Planetary Motion<br/>行星运动]
    
    REL --> RAD[Inverse with r<br/>与半径成反比]
    REL --> MASS[Independent of m<br/>与质量无关]
    REL --> CENT[Depends on M<br/>取决于中心质量]
    
    FORM --> PERIOD[Orbital Period<br/>轨道周期 T = 2πr/v]
    FORM --> KEPLER[Kepler's Third Law<br/>开普勒第三定律]
    FORM --> ESCAPE[Escape Velocity<br/>逃逸速度 v_esc = √2 × v]
    
    %% Links to other topics
    SAT --> GEO
    GEO --> [[Geostationary Satellites]]
    KEPLER --> [[Kepler's Third Law]]
    GF --> [[Gravitational Force and Field]]
    CF --> [[Centripetal Acceleration and Force]]
    ESCAPE --> [[Gravitational Potential]]
    
    %% Styling
    classDef main fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef sub fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    classDef link fill:#fff9c4,stroke:#f57f17,stroke-width:1px
    
    class OV main
    class DER,APP,REL sub
    class GF,CF,EQ,FORM,SAT,GEO,PLAN,RAD,MASS,CENT,PERIOD,KEPLER,ESCAPE link
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Minimum velocity for stable circular orbit; gravity provides centripetal force / 稳定圆形轨道的最小速度；引力提供向心力 |
| **Key Formula / 核心公式** | $v = \sqrt{\frac{GM}{r}}$ — orbital velocity depends only on central mass M and orbital radius r / 轨道速度仅取决于中心质量M和轨道半径r |
| **Key Relationship / 关键关系** | $v \propto \frac{1}{\sqrt{r}}$ — as orbital radius increases, speed decreases / 轨道半径增加，速度减小 |
| **Mass Independence / 质量独立性** | Orbital velocity is independent of satellite mass — all objects at same r have same v / 轨道速度与卫星质量无关——相同r处的所有物体具有相同的v |
| **Orbital Radius / 轨道半径** | $r = R_{\text{planet}} + h$ (center-to-center distance, not altitude) / 中心到中心的距离，不是高度 |
| **Earth Values / 地球数值** | Surface orbit: ~7.9 km/s; LEO (300 km): ~7.7 km/s; GEO (36,000 km): ~3.1 km/s / 表面轨道：~7.9公里/秒；低地球轨道（300公里）：~7.7公里/秒；地球静止轨道（36,000公里）：~3.1公里/秒 |
| **Derivation Steps / 推导步骤** | 1. $F_{\text{grav}} = \frac{GMm}{r^2}$ 2. $F_{\text{cent}} = \frac{mv^2}{r}$ 3. Equate: $\frac{GMm}{r^2} = \frac{mv^2}{r}$ 4. Cancel m and one r: $\frac{GM}{r} = v^2$ 5. $v = \sqrt{\frac{GM}{r}}$ |
| **Common Mistake / 常见错误** | Using altitude instead of orbital radius; forgetting to convert km to m / 使用高度而不是轨道半径；忘记将公里转换为米 |
| **Exam Tip / 考试提示** | Always check: is r the orbital radius (center-to-center) or altitude? If altitude, add planet's radius / 始终检查：r是轨道半径（中心到中心）还是高度？如果是高度，加上行星半径 |
| **Related Topics / 相关主题** | [[Kepler's Third Law]], [[Geostationary Satellites]], [[Gravitational Force and Field]], [[Centripetal Acceleration and Force]], [[Gravitational Potential]] |