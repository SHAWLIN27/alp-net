# 1. Overview / 概述

**English:**
Kepler's Third Law establishes a fundamental relationship between the orbital period of a satellite or planet and its orbital radius. This law states that the square of the orbital period ($T^2$) is directly proportional to the cube of the mean orbital radius ($r^3$). For A-Level Physics, this sub-topic bridges [[Gravitational Force and Field]] with [[Circular Orbits]], allowing us to derive the law from Newton's law of gravitation and centripetal force. Understanding Kepler's Third Law is essential for calculating orbital periods of planets, moons, and artificial satellites, and it forms the basis for determining the mass of celestial bodies. This law is particularly important in [[Geostationary Satellites]] and [[Orbital Velocity]] calculations.

**中文:**
开普勒第三定律建立了卫星或行星的轨道周期与轨道半径之间的基本关系。该定律指出，轨道周期的平方（$T^2$）与平均轨道半径的立方（$r^3$）成正比。在A-Level物理中，本子知识点将[[Gravitational Force and Field]]与[[Circular Orbits]]联系起来，使我们能够从牛顿万有引力定律和向心力推导出该定律。理解开普勒第三定律对于计算行星、卫星和人造卫星的轨道周期至关重要，并且是确定天体质量的基础。该定律在[[Geostationary Satellites]]和[[Orbital Velocity]]计算中尤为重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 15.3(a) State Kepler's laws of planetary motion | 6.11 Understand that for a planet orbiting the Sun, $T^2 \propto r^3$ |
| 15.3(b) Derive Kepler's third law from Newton's law of gravitation and centripetal force | 6.12 Use the relationship $T^2 = \frac{4\pi^2}{GM}r^3$ |
| 15.3(c) Use Kepler's third law to calculate orbital periods and radii | 6.13 Apply Kepler's third law to binary star systems |
| 15.3(d) Apply Kepler's third law to binary star systems | 6.14 Determine the mass of a central body using orbital data |
| 15.3(e) Determine the mass of a central body using orbital data | 6.15 Understand the significance of the constant $\frac{4\pi^2}{GM}$ |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to derive $T^2 = \frac{4\pi^2}{GM}r^3$ from first principles, apply it to both circular and elliptical orbits (using mean radius), and use it to calculate the mass of a central body. For binary star systems, students should understand that both stars orbit their common center of mass.
- **中文:** 学生必须能够从基本原理推导出 $T^2 = \frac{4\pi^2}{GM}r^3$，将其应用于圆形和椭圆轨道（使用平均半径），并用于计算中心天体的质量。对于双星系统，学生应理解两颗恒星都围绕它们的共同质心运行。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Orbital Period** / 轨道周期 | The time taken for a satellite or planet to complete one full orbit around its central body | 卫星或行星绕中心天体完成一次完整轨道所需的时间 | Confusing period with frequency ($f = 1/T$) |
| **Mean Orbital Radius** / 平均轨道半径 | The average distance from the center of the orbiting body to the center of the central body; for elliptical orbits, this is the semi-major axis | 从轨道天体中心到中心天体中心的平均距离；对于椭圆轨道，这是半长轴 | Using the distance of closest approach instead of the mean radius |
| **Kepler's Third Law** / 开普勒第三定律 | The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit: $T^2 \propto r^3$ | 行星轨道周期的平方与其轨道半长轴的立方成正比：$T^2 \propto r^3$ | Forgetting that the constant depends on the mass of the central body |
| **Gravitational Constant** / 万有引力常数 | The universal constant $G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$ that appears in Newton's law of gravitation | 出现在牛顿万有引力定律中的普适常数 $G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$ | Using $g = 9.81$ instead of $G$ |
| **Binary Star System** / 双星系统 | A system of two stars orbiting their common center of mass under mutual gravitational attraction | 两颗恒星在相互引力作用下绕共同质心运行的系统 | Assuming both stars have the same orbital radius |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Derivation of Kepler's Third Law / 开普勒第三定律的推导

### Explanation / 解释
**English:**
Kepler's Third Law can be derived by equating the gravitational force to the centripetal force for a satellite in a circular orbit. For a satellite of mass $m$ orbiting a central body of mass $M$ at radius $r$:

$$F_{\text{gravitational}} = F_{\text{centripetal}}$$

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

Since $v = \frac{2\pi r}{T}$ (orbital speed = circumference/period):

$$\frac{GMm}{r^2} = \frac{m(2\pi r/T)^2}{r}$$

Simplifying:

$$\frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}$$

Rearranging:

$$T^2 = \frac{4\pi^2}{GM}r^3$$

This shows that $T^2 \propto r^3$, with the constant of proportionality $\frac{4\pi^2}{GM}$ depending only on the mass of the central body. This derivation assumes a circular orbit and that the satellite's mass is negligible compared to the central body.

**中文:**
开普勒第三定律可以通过将万有引力与向心力相等来推导。对于质量为 $m$、绕质量为 $M$ 的中心天体在半径 $r$ 处运行的卫星：

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

由于 $v = \frac{2\pi r}{T}$（轨道速度 = 周长/周期）：

$$\frac{GMm}{r^2} = \frac{m(2\pi r/T)^2}{r}$$

简化后：

$$\frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}$$

整理得：

$$T^2 = \frac{4\pi^2}{GM}r^3$$

这表明 $T^2 \propto r^3$，比例常数 $\frac{4\pi^2}{GM}$ 仅取决于中心天体的质量。该推导假设圆形轨道且卫星质量相对于中心天体可忽略不计。

### Physical Meaning / 物理意义
**English:**
The physical meaning is that planets farther from the Sun take longer to complete one orbit. The $T^2 \propto r^3$ relationship means that if you double the orbital radius, the period increases by a factor of $2^{3/2} \approx 2.83$. This is because the gravitational force weakens with distance ($1/r^2$), requiring a slower orbital speed, and the orbital circumference also increases linearly with $r$.

**中文:**
物理意义是离太阳越远的行星完成一次轨道所需的时间越长。$T^2 \propto r^3$ 的关系意味着如果将轨道半径加倍，周期将增加 $2^{3/2} \approx 2.83$ 倍。这是因为万有引力随距离减弱（$1/r^2$），需要更慢的轨道速度，同时轨道周长也随 $r$ 线性增加。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking the constant in Kepler's Third Law is universal — it depends on $M$, the mass of the central body
  - Confusing orbital radius with altitude (altitude = radius - planet radius)
  - Applying the law to satellites orbiting different central bodies without adjusting the constant
  - Forgetting that for elliptical orbits, $r$ is the semi-major axis, not the distance at any specific point

- **中文:**
  - 认为开普勒第三定律中的常数是普适的——它取决于中心天体的质量 $M$
  - 混淆轨道半径与高度（高度 = 半径 - 行星半径）
  - 将定律应用于绕不同中心天体运行的卫星而不调整常数
  - 忘记对于椭圆轨道，$r$ 是半长轴，而不是任何特定点的距离

### Exam Tips / 考试提示
- **English:**
  - Always write the full equation $T^2 = \frac{4\pi^2}{GM}r^3$ before substituting values
  - Check units: $T$ in seconds, $r$ in meters, $M$ in kg
  - For ratio problems, use $\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$ (the constant cancels out)
  - Remember that $G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$

- **中文:**
  - 在代入数值前始终写出完整方程 $T^2 = \frac{4\pi^2}{GM}r^3$
  - 检查单位：$T$ 以秒为单位，$r$ 以米为单位，$M$ 以千克为单位
  - 对于比例问题，使用 $\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$（常数抵消）
  - 记住 $G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$

> 📷 **IMAGE PROMPT — KEPLER-01: Kepler's Third Law Derivation Diagram**
> A clear diagram showing a planet of mass m orbiting a star of mass M in a circular orbit of radius r. Include labels: gravitational force F_G = GMm/r² pointing inward, centripetal force F_c = mv²/r pointing inward, orbital velocity v = 2πr/T tangent to orbit. Show the derivation steps: F_G = F_c → GMm/r² = mv²/r → GM/r² = (2πr/T)²/r → T² = (4π²/GM)r³. Use a clean, educational style suitable for A-Level physics textbook.

---

## 4.2 Application to Binary Star Systems / 在双星系统中的应用

### Explanation / 解释
**English:**
In a binary star system, two stars of masses $M_1$ and $M_2$ orbit their common center of mass. The key difference from a planet-sun system is that both stars have comparable masses, so neither can be considered stationary. For each star, the gravitational force from the other star provides the centripetal force:

$$\frac{GM_1M_2}{r^2} = M_1\omega^2 r_1 = M_2\omega^2 r_2$$

where $r = r_1 + r_2$ is the separation between stars, and $r_1$, $r_2$ are distances from the center of mass. The center of mass condition gives $M_1r_1 = M_2r_2$.

The combined Kepler's Third Law for binary systems becomes:

$$T^2 = \frac{4\pi^2}{G(M_1 + M_2)}r^3$$

Note that the total mass $M_1 + M_2$ replaces the single central mass $M$.

**中文:**
在双星系统中，两颗质量分别为 $M_1$ 和 $M_2$ 的恒星绕它们的共同质心运行。与行星-太阳系统的关键区别在于两颗恒星的质量相当，因此两者都不能被视为静止。对于每颗恒星，来自另一颗恒星的万有引力提供向心力：

$$\frac{GM_1M_2}{r^2} = M_1\omega^2 r_1 = M_2\omega^2 r_2$$

其中 $r = r_1 + r_2$ 是恒星之间的距离，$r_1$、$r_2$ 是到质心的距离。质心条件给出 $M_1r_1 = M_2r_2$。

双星系统的组合开普勒第三定律变为：

$$T^2 = \frac{4\pi^2}{G(M_1 + M_2)}r^3$$

注意总质量 $M_1 + M_2$ 取代了单个中心质量 $M$。

### Physical Meaning / 物理意义
**English:**
In binary systems, the orbital period depends on the total mass of the system, not just one star's mass. This allows astronomers to determine the masses of stars in binary systems by measuring their orbital periods and separation. More massive binary systems have shorter orbital periods for the same separation.

**中文:**
在双星系统中，轨道周期取决于系统的总质量，而不仅仅是一颗恒星的质量。这使得天文学家能够通过测量双星系统的轨道周期和间距来确定恒星的质量。对于相同的间距，质量更大的双星系统具有更短的轨道周期。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking both stars have the same orbital radius — they orbit at different distances from the center of mass
  - Using $M$ instead of $M_1 + M_2$ in the binary star formula
  - Confusing the separation $r$ with individual orbital radii $r_1$ and $r_2$

- **中文:**
  - 认为两颗恒星具有相同的轨道半径——它们到质心的距离不同
  - 在双星公式中使用 $M$ 而不是 $M_1 + M_2$
  - 混淆间距 $r$ 与单个轨道半径 $r_1$ 和 $r_2$

### Exam Tips / 考试提示
- **English:**
  - For binary systems, always identify which distance is given: separation or individual orbital radius
  - Use the center of mass equation $M_1r_1 = M_2r_2$ to find individual radii
  - Remember that both stars have the same angular velocity $\omega$ and period $T$

- **中文:**
  - 对于双星系统，始终确定给出的距离是间距还是单个轨道半径
  - 使用质心方程 $M_1r_1 = M_2r_2$ 求单个半径
  - 记住两颗恒星具有相同的角速度 $\omega$ 和周期 $T$

> 📷 **IMAGE PROMPT — KEPLER-02: Binary Star System Diagram**
> A diagram showing two stars of masses M₁ and M₂ orbiting their common center of mass (COM). Label: separation r = r₁ + r₂, distances from COM: r₁ and r₂. Show both stars on circular orbits around COM with same angular velocity ω. Include force arrows: gravitational force F_G = GM₁M₂/r² acting on each star toward the other. Use different colors for the two stars and their orbits. Educational style for A-Level physics.

---

# 5. Essential Equations / 核心公式

## Equation 1: Kepler's Third Law (Standard Form) / 开普勒第三定律（标准形式）

$$T^2 = \frac{4\pi^2}{GM}r^3$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T$ | Orbital period | 轨道周期 | s |
| $r$ | Mean orbital radius (semi-major axis) | 平均轨道半径（半长轴） | m |
| $G$ | Gravitational constant ($6.67 \times 10^{-11}$) | 万有引力常数 | N·m²·kg⁻² |
| $M$ | Mass of central body | 中心天体质量 | kg |

**Derivation / 推导:**
From $\frac{GMm}{r^2} = \frac{mv^2}{r}$ and $v = \frac{2\pi r}{T}$, as shown in Section 4.1.

**Conditions / 适用条件:**
- **English:** Circular orbit (or elliptical orbit using semi-major axis); satellite mass negligible compared to central body; only gravitational force acting
- **中文:** 圆形轨道（或使用半长轴的椭圆轨道）；卫星质量相对于中心天体可忽略；仅受万有引力作用

**Limitations / 局限性:**
- **English:** Does not account for relativistic effects; assumes isolated two-body system; inaccurate for highly elliptical orbits if mean radius is not used
- **中文:** 不考虑相对论效应；假设孤立的二体系统；如果不使用平均半径，对于高椭圆轨道不准确

## Equation 2: Kepler's Third Law (Ratio Form) / 开普勒第三定律（比例形式）

$$\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T_1, T_2$ | Orbital periods of two satellites | 两颗卫星的轨道周期 | s |
| $r_1, r_2$ | Orbital radii of two satellites | 两颗卫星的轨道半径 | m |

**Conditions / 适用条件:**
- **English:** Both satellites orbit the same central body; the constant $\frac{4\pi^2}{GM}$ cancels out
- **中文:** 两颗卫星绕同一中心天体运行；常数 $\frac{4\pi^2}{GM}$ 抵消

## Equation 3: Kepler's Third Law (Binary Star Systems) / 开普勒第三定律（双星系统）

$$T^2 = \frac{4\pi^2}{G(M_1 + M_2)}r^3$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $M_1, M_2$ | Masses of the two stars | 两颗恒星的质量 | kg |
| $r$ | Separation between stars | 恒星间距 | m |

**Derivation / 推导:**
From $\frac{GM_1M_2}{r^2} = M_1\omega^2 r_1 = M_2\omega^2 r_2$, with $r = r_1 + r_2$ and $\omega = \frac{2\pi}{T}$.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 $T^2$ vs $r^3$ Graph / $T^2$ 对 $r^3$ 图

### Axes / 坐标轴
- **X-axis:** $r^3$ (m³) — cube of orbital radius / 轨道半径的立方
- **Y-axis:** $T^2$ (s²) — square of orbital period / 轨道周期的平方

### Shape / 形状
- **English:** A straight line through the origin, indicating direct proportionality
- **中文:** 一条通过原点的直线，表示正比关系

### Gradient Meaning / 斜率含义
- **English:** Gradient = $\frac{4\pi^2}{GM}$, which is constant for a given central body. The gradient decreases as the central mass $M$ increases
- **中文:** 斜率 = $\frac{4\pi^2}{GM}$，对于给定的中心天体是常数。斜率随中心质量 $M$ 增加而减小

### Area Meaning / 面积含义
- **English:** No physical meaning for area under this graph
- **中文:** 该图下的面积没有物理意义

### Exam Interpretation / 考试解读
- **English:** A straight line through origin confirms Kepler's Third Law. The gradient can be used to calculate the mass of the central body: $M = \frac{4\pi^2}{G \times \text{gradient}}$
- **中文:** 通过原点的直线证实了开普勒第三定律。斜率可用于计算中心天体的质量：$M = \frac{4\pi^2}{G \times \text{斜率}}$

```mermaid
graph LR
    A[Collect orbital data: T and r] --> B[Calculate T² and r³]
    B --> C[Plot T² vs r³]
    C --> D{Straight line through origin?}
    D -->|Yes| E[Kepler's Third Law confirmed]
    D -->|No| F[Check data or assumptions]
    E --> G[Calculate gradient]
    G --> H[Find M = 4π²/(G × gradient)]
```

> 📷 **IMAGE PROMPT — KEPLER-03: T² vs r³ Graph**
> A graph showing T² on the y-axis and r³ on the x-axis. Plot several data points for planets in our solar system (Mercury, Venus, Earth, Mars, Jupiter, Saturn) forming a straight line through the origin. Label the gradient as 4π²/GM. Include error bars on data points. Clean, educational style for A-Level physics.

## 6.2 $T$ vs $r$ Graph / $T$ 对 $r$ 图

### Axes / 坐标轴
- **X-axis:** $r$ (m) — orbital radius / 轨道半径
- **Y-axis:** $T$ (s) — orbital period / 轨道周期

### Shape / 形状
- **English:** A curve showing $T \propto r^{3/2}$ (power law relationship)
- **中文:** 一条曲线，显示 $T \propto r^{3/2}$（幂律关系）

### Gradient Meaning / 斜率含义
- **English:** The gradient changes at every point; not directly useful for calculations
- **中文:** 斜率在每一点都变化；对计算没有直接用处

### Exam Interpretation / 考试解读
- **English:** Use log-log graph ($\log T$ vs $\log r$) to obtain a straight line with gradient $3/2$, confirming the $T \propto r^{3/2}$ relationship
- **中文:** 使用对数-对数图（$\log T$ 对 $\log r$）得到斜率为 $3/2$ 的直线，确认 $T \propto r^{3/2}$ 关系

---

# 7. Required Diagrams / 必备图表

## 7.1 Kepler's Third Law Derivation Diagram / 开普勒第三定律推导图

### Description / 描述
**English:**
A diagram showing a satellite of mass $m$ in a circular orbit of radius $r$ around a central body of mass $M$. The diagram should illustrate the balance between gravitational force and centripetal force, with the orbital velocity $v = 2\pi r/T$ indicated.

**中文:**
一个显示质量为 $m$ 的卫星绕质量为 $M$ 的中心天体在半径为 $r$ 的圆形轨道上运行的图。该图应说明万有引力与向心力之间的平衡，并标出轨道速度 $v = 2\pi r/T$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — KEPLER-04: Kepler's Third Law Derivation**
> A clean educational diagram showing a planet (mass m) orbiting a star (mass M) in a circular orbit of radius r. The planet is shown at one position with velocity vector v tangent to the orbit. Two force arrows point toward the star: F_gravitational = GMm/r² and F_centripetal = mv²/r, labeled as equal. Below the diagram, show the derivation steps: F_G = F_c → GMm/r² = mv²/r → v = 2πr/T → GM/r² = (2πr/T)²/r → T² = (4π²/GM)r³. Use a textbook-quality style with clear labels and equations.

### Labels Required / 需要标注
- **English:** Central body mass $M$, satellite mass $m$, orbital radius $r$, orbital velocity $v$, gravitational force $F_G$, centripetal force $F_c$, orbital period $T$
- **中文:** 中心天体质量 $M$，卫星质量 $m$，轨道半径 $r$，轨道速度 $v$，万有引力 $F_G$，向心力 $F_c$，轨道周期 $T$

### Exam Importance / 考试重要性
- **English:** High — students are often asked to derive Kepler's Third Law in exams; having the diagram in mind helps structure the derivation
- **中文:** 高——考试中常要求学生推导开普勒第三定律；记住该图有助于组织推导过程

## 7.2 Binary Star System Diagram / 双星系统图

### Description / 描述
**English:**
A diagram showing two stars of masses $M_1$ and $M_2$ orbiting their common center of mass. The distances $r_1$ and $r_2$ from the center of mass should be labeled, along with the total separation $r = r_1 + r_2$.

**中文:**
一个显示两颗质量分别为 $M_1$ 和 $M_2$ 的恒星绕共同质心运行的图。应标出到质心的距离 $r_1$ 和 $r_2$，以及总间距 $r = r_1 + r_2$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — KEPLER-05: Binary Star System**
> A diagram showing two stars of different sizes (M₁ larger, M₂ smaller) orbiting their common center of mass (COM). Show circular orbits around COM with radii r₁ and r₂. Label: M₁, M₂, r₁, r₂, and total separation r = r₁ + r₂. Include force arrows: F_G = GM₁M₂/r² acting on each star. Show that both stars have the same angular velocity ω and period T. Use different colors for the two stars. Educational style for A-Level physics.

### Labels Required / 需要标注
- **English:** Star masses $M_1$ and $M_2$, distances from COM $r_1$ and $r_2$, separation $r$, gravitational force $F_G$, angular velocity $\omega$, period $T$
- **中文:** 恒星质量 $M_1$ 和 $M_2$，到质心的距离 $r_1$ 和 $r_2$，间距 $r$，万有引力 $F_G$，角速度 $\omega$，周期 $T$

### Exam Importance / 考试重要性
- **English:** Medium — binary star questions appear less frequently but are common in A2 papers
- **中文:** 中等——双星问题出现频率较低，但在A2试卷中常见

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Orbital Period / 计算轨道周期

### Question / 题目
**English:**
The Moon orbits the Earth at a mean distance of $3.84 \times 10^8$ m. The mass of the Earth is $5.97 \times 10^{24}$ kg. Calculate the orbital period of the Moon in days. ($G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$)

**中文:**
月球绕地球运行的平均距离为 $3.84 \times 10^8$ m。地球质量为 $5.97 \times 10^{24}$ kg。计算月球的轨道周期（以天为单位）。（$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$）

### Solution / 解答

**Step 1:** Write Kepler's Third Law / 写出开普勒第三定律

$$T^2 = \frac{4\pi^2}{GM}r^3$$

**Step 2:** Substitute values / 代入数值

$$T^2 = \frac{4\pi^2}{(6.67 \times 10^{-11})(5.97 \times 10^{24})} \times (3.84 \times 10^8)^3$$

**Step 3:** Calculate denominator / 计算分母

$$GM = (6.67 \times 10^{-11})(5.97 \times 10^{24}) = 3.98 \times 10^{14} \text{ m}^3\text{·s}^{-2}$$

**Step 4:** Calculate $r^3$ / 计算 $r^3$

$$r^3 = (3.84 \times 10^8)^3 = 5.66 \times 10^{25} \text{ m}^3$$

**Step 5:** Calculate $T^2$ / 计算 $T^2$

$$T^2 = \frac{4\pi^2}{3.98 \times 10^{14}} \times 5.66 \times 10^{25}$$

$$T^2 = \frac{39.48}{3.98 \times 10^{14}} \times 5.66 \times 10^{25}$$

$$T^2 = 9.92 \times 10^{-14} \times 5.66 \times 10^{25}$$

$$T^2 = 5.61 \times 10^{12} \text{ s}^2$$

**Step 6:** Find $T$ / 求 $T$

$$T = \sqrt{5.61 \times 10^{12}} = 2.37 \times 10^6 \text{ s}$$

**Step 7:** Convert to days / 转换为天

$$T = \frac{2.37 \times 10^6}{24 \times 3600} = \frac{2.37 \times 10^6}{86400} = 27.4 \text{ days}$$

### Final Answer / 最终答案
**Answer:** 27.4 days | **答案：** 27.4 天

### Quick Tip / 提示
**English:** Always convert to SI units first. For period in days, divide seconds by 86400 (24 × 3600). Remember that the Moon's actual orbital period is about 27.3 days — your answer should be close to this.

**中文:** 始终先转换为SI单位。要将周期转换为天，将秒数除以86400（24 × 3600）。记住月球的实际轨道周期约为27.3天——你的答案应接近这个值。

---

## Example 2: Determining Mass of Central Body / 确定中心天体质量

### Question / 题目
**English:**
A satellite orbits Mars with a period of 7.65 hours at a mean orbital radius of $9.40 \times 10^6$ m. Calculate the mass of Mars. ($G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$)

**中文:**
一颗卫星以7.65小时的周期绕火星运行，平均轨道半径为 $9.40 \times 10^6$ m。计算火星的质量。（$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$）

### Solution / 解答

**Step 1:** Convert period to seconds / 将周期转换为秒

$$T = 7.65 \times 3600 = 2.75 \times 10^4 \text{ s}$$

**Step 2:** Rearrange Kepler's Third Law for $M$ / 重新排列开普勒第三定律求 $M$

$$T^2 = \frac{4\pi^2}{GM}r^3$$

$$M = \frac{4\pi^2 r^3}{GT^2}$$

**Step 3:** Substitute values / 代入数值

$$M = \frac{4\pi^2 (9.40 \times 10^6)^3}{(6.67 \times 10^{-11})(2.75 \times 10^4)^2}$$

**Step 4:** Calculate $r^3$ / 计算 $r^3$

$$r^3 = (9.40 \times 10^6)^3 = 8.31 \times 10^{20} \text{ m}^3$$

**Step 5:** Calculate $T^2$ / 计算 $T^2$

$$T^2 = (2.75 \times 10^4)^2 = 7.56 \times 10^8 \text{ s}^2$$

**Step 6:** Calculate numerator / 计算分子

$$4\pi^2 r^3 = 4 \times \pi^2 \times 8.31 \times 10^{20} = 3.28 \times 10^{22} \text{ m}^3$$

**Step 7:** Calculate denominator / 计算分母

$$GT^2 = (6.67 \times 10^{-11})(7.56 \times 10^8) = 5.04 \times 10^{-2} \text{ m}^3\text{·kg}^{-1}\text{·s}^{-2} \times \text{s}^2 = 5.04 \times 10^{-2} \text{ m}^3\text{·kg}^{-1}$$

**Step 8:** Calculate $M$ / 计算 $M$

$$M = \frac{3.28 \times 10^{22}}{5.04 \times 10^{-2}} = 6.51 \times 10^{23} \text{ kg}$$

### Final Answer / 最终答案
**Answer:** $6.51 \times 10^{23}$ kg | **答案：** $6.51 \times 10^{23}$ kg

### Quick Tip / 提示
**English:** When solving for $M$, always check that your units work out: $M$ should be in kg. The actual mass of Mars is $6.39 \times 10^{23}$ kg — your calculated value should be close.

**中文:** 求解 $M$ 时，始终检查单位是否正确：$M$ 应以千克为单位。火星的实际质量为 $6.39 \times 10^{23}$ kg——你的计算值应接近这个值。

---

## Example 3: Binary Star System / 双星系统

### Question / 题目
**English:**
Two stars in a binary system have masses $M_1 = 2.0 \times 10^{30}$ kg and $M_2 = 1.0 \times 10^{30}$ kg. Their separation is $1.5 \times 10^{11}$ m. Calculate their orbital period in years. ($G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$, 1 year = $3.16 \times 10^7$ s)

**中文:**
双星系统中的两颗恒星质量分别为 $M_1 = 2.0 \times 10^{30}$ kg 和 $M_2 = 1.0 \times 10^{30}$ kg。它们的间距为 $1.5 \times 10^{11}$ m。计算它们的轨道周期（以年为单位）。（$G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$，1年 = $3.16 \times 10^7$ s）

### Solution / 解答

**Step 1:** Use binary star form of Kepler's Third Law / 使用双星形式的开普勒第三定律

$$T^2 = \frac{4\pi^2}{G(M_1 + M_2)}r^3$$

**Step 2:** Calculate total mass / 计算总质量

$$M_1 + M_2 = 2.0 \times 10^{30} + 1.0 \times 10^{30} = 3.0 \times 10^{30} \text{ kg}$$

**Step 3:** Substitute values / 代入数值

$$T^2 = \frac{4\pi^2}{(6.67 \times 10^{-11})(3.0 \times 10^{30})} \times (1.5 \times 10^{11})^3$$

**Step 4:** Calculate denominator / 计算分母

$$G(M_1 + M_2) = (6.67 \times 10^{-11})(3.0 \times 10^{30}) = 2.00 \times 10^{20} \text{ m}^3\text{·s}^{-2}$$

**Step 5:** Calculate $r^3$ / 计算 $r^3$

$$r^3 = (1.5 \times 10^{11})^3 = 3.38 \times 10^{33} \text{ m}^3$$

**Step 6:** Calculate $T^2$ / 计算 $T^2$

$$T^2 = \frac{4\pi^2}{2.00 \times 10^{20}} \times 3.38 \times 10^{33}$$

$$T^2 = \frac{39.48}{2.00 \times 10^{20}} \times 3.38 \times 10^{33}$$

$$T^2 = 1.97 \times 10^{-19} \times 3.38 \times 10^{33}$$

$$T^2 = 6.66 \times 10^{14} \text{ s}^2$$

**Step 7:** Find $T$ / 求 $T$

$$T = \sqrt{6.66 \times 10^{14}} = 2.58 \times 10^7 \text{ s}$$

**Step 8:** Convert to years / 转换为年

$$T = \frac{2.58 \times 10^7}{3.16 \times 10^7} = 0.816 \text{ years}$$

### Final Answer / 最终答案
**Answer:** 0.816 years | **答案：** 0.816 年

### Quick Tip / 提示
**English:** In binary systems, always use the total mass $M_1 + M_2$ and the separation $r$ (not individual orbital radii). The period is the same for both stars.

**中文:** 在双星系统中，始终使用总质量 $M_1 + M_2$ 和间距 $r$（而不是单个轨道半径）。两颗恒星的周期相同。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Derivation of Kepler's Third Law / 推导开普勒第三定律 | High / 高 | Medium / 中等 | 📝 *待填入* |
| Calculating orbital period from given radius / 从给定半径计算轨道周期 | High / 高 | Easy-Medium / 简单-中等 | 📝 *待填入* |
| Determining mass of central body / 确定中心天体质量 | High / 高 | Medium / 中等 | 📝 *待填入* |
| Ratio problems using $T^2 \propto r^3$ / 使用 $T^2 \propto r^3$ 的比例问题 | Medium / 中等 | Easy / 简单 | 📝 *待填入* |
| Binary star system calculations / 双星系统计算 | Low-Medium / 低-中等 | Hard / 困难 | 📝 *待填入* |
| Graph interpretation ($T^2$ vs $r^3$) / 图表解读（$T^2$ 对 $r^3$） | Medium / 中等 | Medium / 中等 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Derive, Calculate, Determine, Show that, State, Explain, Plot, Use
- **中文:** 推导，计算，确定，证明，陈述，解释，绘制，使用

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Kepler's Third Law connects to practical skills in several ways:

1. **Data Collection and Analysis:** Students may be asked to analyze orbital data for moons of Jupiter or Saturn to verify $T^2 \propto r^3$. This involves collecting $T$ and $r$ values, calculating $T^2$ and $r^3$, and plotting a graph.

2. **Graph Plotting and Interpretation:** Plotting $T^2$ against $r^3$ should yield a straight line through the origin. The gradient can be used to calculate the mass of the central body. Students must understand how to determine the gradient from the line of best fit and calculate uncertainties.

3. **Uncertainty Analysis:** When determining the mass of a central body, uncertainties in $T$ and $r$ propagate to the final mass value. Students should be able to calculate percentage uncertainties and combine them.

4. **Experimental Design:** While direct experiments with planetary orbits are impossible in the lab, simulations or data from astronomical observations can be used. Students should understand the limitations of such data (e.g., elliptical orbits, perturbations from other bodies).

5. **Log-Log Graphs:** To confirm the $T \propto r^{3/2}$ relationship, students can plot $\log T$ against $\log r$. The gradient should be $3/2$, confirming the power law.

**中文:**
开普勒第三定律在多个方面与实验技能相关：

1. **数据收集与分析：** 学生可能需要分析木星或土星卫星的轨道数据，以验证 $T^2 \propto r^3$。这涉及收集 $T$ 和 $r$ 值，计算 $T^2$ 和 $r^3$，并绘制图表。

2. **图表绘制与解读：** 绘制 $T^2$ 对 $r^3$ 的图应得到一条通过原点的直线。斜率可用于计算中心天体的质量。学生必须理解如何从最佳拟合线确定斜率并计算不确定度。

3. **不确定度分析：** 在确定中心天体质量时，$T$ 和 $r$ 的不确定度会传播到最终质量值。学生应能够计算百分比不确定度并将其合并。

4. **实验设计：** 虽然在实验室中无法直接进行行星轨道实验，但可以使用模拟或天文观测数据。学生应理解此类数据的局限性（例如，椭圆轨道、其他天体的扰动）。

5. **对数-对数图：** 为确认 $T \propto r^{3/2}$ 关系，学生可以绘制 $\log T$ 对 $\log r$ 的图。斜率应为 $3/2$，确认幂律关系。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Kepler's Third Law Concept Map
    K3L[Kepler's Third Law<br>T² ∝ r³] --> DER[Derivation]
    K3L --> APP[Applications]
    K3L --> GRAPH[Graphical Analysis]
    
    DER --> GF[Gravitational Force<br>F = GMm/r²]
    DER --> CF[Centripetal Force<br>F = mv²/r]
    DER --> V[Orbital Velocity<br>v = 2πr/T]
    DER --> EQ[T² = (4π²/GM)r³]
    
    GF --> GFF[[Gravitational Force and Field]]
    CF --> CAF[[Centripetal Acceleration and Force]]
    V --> OV[[Orbital Velocity]]
    
    APP --> PERIOD[Calculate Orbital Period]
    APP --> MASS[Determine Central Mass]
    APP --> BINARY[Binary Star Systems]
    APP --> GEO[Geostationary Satellites]
    
    PERIOD --> CO[[Circular Orbits]]
    MASS --> CO
    GEO --> GS[[Geostationary Satellites]]
    
    BINARY --> COM[Center of Mass]
    BINARY --> TOTAL[T² = (4π²/G(M₁+M₂))r³]
    
    GRAPH --> T2R3[T² vs r³ Graph]
    GRAPH --> LOG[log T vs log r]
    
    T2R3 --> STRAIGHT[Straight line through origin]
    T2R3 --> GRADIENT[Gradient = 4π²/GM]
    
    LOG --> GRAD3[Gradient = 3/2]
    
    %% Prerequisites
    GFF -.-> GF
    CAF -.-> CF
    
    %% Related topics
    K3L -.-> GP[[Gravitational Potential]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | $T^2 \propto r^3$ — Square of orbital period ∝ cube of mean orbital radius / 轨道周期的平方 ∝ 平均轨道半径的立方 |
| **Key Formula / 核心公式** | $T^2 = \frac{4\pi^2}{GM}r^3$ (standard) / $T^2 = \frac{4\pi^2}{G(M_1+M_2)}r^3$ (binary) |
| **Derivation / 推导** | $F_G = F_c$ → $\frac{GMm}{r^2} = \frac{mv^2}{r}$ → $v = \frac{2\pi r}{T}$ → $T^2 = \frac{4\pi^2}{GM}r^3$ |
| **Key Graph / 核心图表** | $T^2$ vs $r^3$: Straight line through origin, gradient = $\frac{4\pi^2}{GM}$ / $T^2$ 对 $r^3$：通过原点的直线，斜率 = $\frac{4\pi^2}{GM}$ |
| **Constant / 常数** | $\frac{4\pi^2}{GM}$ depends on central mass $M$ — NOT universal / 取决于中心质量 $M$ — 不是普适常数 |
| **Binary Systems / 双星系统** | Use total mass $M_1+M_2$ and separation $r$; both stars have same $T$ / 使用总质量 $M_1+M_2$ 和间距 $r$；两颗恒星具有相同的 $T$ |
| **Mass Determination / 质量确定** | $M = \frac{4\pi^2 r^3}{GT^2}$ — rearrange Kepler's Third Law / 重新排列开普勒第三定律 |
| **Ratio Problems / 比例问题** | $\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$ — constant cancels for same central body / 常数抵消（同一中心天体） |
| **Units / 单位** | $T$ in s, $r$ in m, $M$ in kg, $G = 6.67 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$ |
| **Common Mistake / 常见错误** | Using altitude instead of orbital radius; forgetting $G$ is not $g$ / 使用高度而不是轨道半径；忘记 $G$ 不是 $g$ |
| **Exam Tip / 考试提示** | Always derive from $F_G = F_c$ first; show all steps; check units / 始终先从 $F_G = F_c$ 推导；展示所有步骤；检查单位 |
| **Prerequisites / 前置知识** | [[Gravitational Force and Field]], [[Centripetal Acceleration and Force]] |
| **Related Topics / 相关主题** | [[Circular Orbits]], [[Orbital Velocity]], [[Geostationary Satellites]], [[Gravitational Potential]] |