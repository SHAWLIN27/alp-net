# 1. Overview / 概述

**English:** This topic explores the physics of objects moving in circular orbits under gravitational forces. It bridges [[Centripetal Acceleration and Force]] with [[Gravitational Force and Field]] to derive key relationships for orbital motion. Understanding circular orbits is fundamental to satellite technology, space exploration, and our understanding of planetary systems. In both CAIE 9702 and Edexcel IAL, this topic is essential for explaining how satellites maintain stable orbits, why geostationary satellites remain fixed above one point on Earth, and how Kepler's laws describe planetary motion. Real-world applications include GPS satellites, communications satellites, weather monitoring, and space station operations.

**中文:** 本专题研究物体在引力作用下做圆周运动的物理规律。它将[[向心加速度与力]]与[[引力与引力场]]联系起来，推导出轨道运动的关键关系。理解圆周轨道对于卫星技术、太空探索以及我们对行星系统的理解至关重要。在CAIE 9702和Edexcel IAL考试中，本专题对于解释卫星如何维持稳定轨道、地球同步卫星为何固定在地球某一点上方，以及开普勒定律如何描述行星运动至关重要。实际应用包括GPS卫星、通信卫星、气象监测和空间站运行。

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 15.3(a) Derive Kepler's third law for circular orbits | 6.11 Understand the relationship between orbital speed, orbital radius, and gravitational field strength |
| 15.3(b) Derive orbital speed for a satellite in circular orbit | 6.12 Derive and use the equation for orbital speed: $v = \sqrt{\frac{GM}{r}}$ |
| 15.3(c) Understand geostationary orbits | 6.13 Understand the concept of geostationary satellites and their uses |
| 15.3(d) Solve problems involving orbital motion | 6.14 Derive and use Kepler's third law: $T^2 \propto r^3$ |
| 15.3(e) Relate orbital period to orbital radius | 6.15 Solve problems involving orbital motion of planets and satellites |

> 📋 **CIE Only:** CAIE requires derivation of Kepler's third law from first principles using [[Centripetal Acceleration and Force]] and [[Gravitational Force and Field]]. Students must be able to derive $T^2 = \frac{4\pi^2}{GM}r^3$ step by step.

> 📋 **Edexcel Only:** Edexcel emphasizes the relationship between orbital speed and gravitational field strength $g$ at the orbital radius. Students should know $v = \sqrt{gr}$ as an alternative form.

**Examiner Expectations / 考官期望:**
- **English:** Students must clearly state assumptions (circular orbit, only gravitational force acts, mass of satellite negligible compared to central mass). Derivation steps must be logical with clear algebraic manipulation. For geostationary satellites, memorise the specific values: orbital radius ≈ 42,000 km from Earth's centre, orbital period = 24 hours, orbit in equatorial plane.
- **中文:** 学生必须明确说明假设条件（圆形轨道、仅受引力作用、卫星质量远小于中心天体质量）。推导步骤必须逻辑清晰，代数运算明确。对于地球同步卫星，需记住具体数值：轨道半径约42,000公里（距地心），轨道周期=24小时，轨道在赤道平面内。

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| [[Orbital Velocity]] / 轨道速度 | The constant speed required for a satellite to maintain a stable circular orbit at a given radius | 卫星在给定半径上维持稳定圆周轨道所需的恒定速度 | Confusing with escape velocity; forgetting that orbital velocity decreases with increasing radius |
| [[Kepler's Third Law]] / 开普勒第三定律 | The square of the orbital period of a planet is directly proportional to the cube of its mean orbital radius | 行星轨道周期的平方与其平均轨道半径的立方成正比 | Using $T \propto r^{3/2}$ incorrectly; forgetting the proportionality constant depends on central mass |
| [[Geostationary Satellites]] / 地球同步卫星 | A satellite that orbits Earth with a period of 24 hours in the equatorial plane, appearing stationary above a fixed point | 在赤道平面内以24小时周期绕地球运行的卫星，看起来固定在地球某一点上方 | Thinking any 24-hour orbit is geostationary; forgetting the equatorial plane requirement |
| Orbital Period / 轨道周期 | The time taken for a satellite to complete one full orbit around the central body | 卫星绕中心天体完成一整圈轨道所需的时间 | Confusing with rotational period of the central body |
| Gravitational Field Strength at Orbit / 轨道处引力场强度 | The gravitational force per unit mass experienced by an object at the orbital radius | 物体在轨道半径处所受的每单位质量的引力 | Using $g$ at Earth's surface instead of $g$ at orbital radius |

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Derivation of Orbital Velocity / 轨道速度的推导

### Explanation / 解释
**English:** For a satellite in a stable circular orbit, the [[Gravitational Force and Field]] provides the necessary [[Centripetal Acceleration and Force]]. Setting gravitational force equal to centripetal force:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

Cancelling $m$ and rearranging gives:

$$v = \sqrt{\frac{GM}{r}}$$

This shows that orbital velocity depends only on the mass of the central body $M$ and the orbital radius $r$, not on the mass of the satellite $m$.

**中文:** 对于稳定圆周轨道上的卫星，[[引力与引力场]]提供所需的[[向心加速度与力]]。令引力等于向心力：

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

消去$m$并整理得：

$$v = \sqrt{\frac{GM}{r}}$$

这表明轨道速度仅取决于中心天体质量$M$和轨道半径$r$，与卫星质量$m$无关。

### Physical Meaning / 物理意义
**English:** As orbital radius increases, orbital velocity decreases. This is why outer planets move slower than inner planets. The inverse square root relationship means doubling the radius reduces speed by a factor of $\sqrt{2}$.

**中文:** 随着轨道半径增大，轨道速度减小。这就是为什么外行星比内行星运动得慢。平方根反比关系意味着半径加倍，速度减小$\sqrt{2}$倍。

### Common Misconceptions / 常见误区
- Thinking a heavier satellite needs a different orbital speed (it doesn't — mass cancels out)
- Confusing orbital velocity with escape velocity (escape velocity is $\sqrt{2}$ times orbital velocity)
- Believing orbital velocity is constant for all satellites (it depends on radius)

### Exam Tips / 考试提示
**English:** Always start derivation with $F_{gravitational} = F_{centripetal}$. Show cancellation of $m$ explicitly. For Edexcel, also know $v = \sqrt{gr}$ where $g$ is gravitational field strength at orbital radius.

**中文:** 始终从$F_{引力} = F_{向心力}$开始推导。明确展示$m$的消去过程。对于Edexcel考试，还需知道$v = \sqrt{gr}$，其中$g$是轨道半径处的引力场强度。

> 📷 **IMAGE PROMPT — [OV-01]: Orbital Velocity vs Radius Graph**
> A graph showing orbital velocity $v$ on y-axis against orbital radius $r$ on x-axis. The curve shows $v \propto 1/\sqrt{r}$ — steep decrease near small r, flattening at large r. Label key points: Earth's surface (r = 6400 km, v ≈ 7.9 km/s), Low Earth Orbit (r ≈ 6600 km, v ≈ 7.8 km/s), Geostationary orbit (r ≈ 42,000 km, v ≈ 3.1 km/s). Style: clean scientific graph with gridlines. Exam importance: HIGH — frequently tested.

## 4.2 Derivation of Kepler's Third Law / 开普勒第三定律的推导

### Explanation / 解释
**English:** Starting from the orbital velocity equation and using $v = \frac{2\pi r}{T}$:

$$\frac{GM}{r} = \frac{4\pi^2 r^2}{T^2}$$

Rearranging:

$$T^2 = \frac{4\pi^2}{GM}r^3$$

This is [[Kepler's Third Law]] for circular orbits: $T^2 \propto r^3$, with proportionality constant $\frac{4\pi^2}{GM}$.

**中文:** 从轨道速度方程出发，利用$v = \frac{2\pi r}{T}$：

$$\frac{GM}{r} = \frac{4\pi^2 r^2}{T^2}$$

整理得：

$$T^2 = \frac{4\pi^2}{GM}r^3$$

这就是圆形轨道的[[开普勒第三定律]]：$T^2 \propto r^3$，比例常数为$\frac{4\pi^2}{GM}$。

### Physical Meaning / 物理意义
**English:** The constant of proportionality depends only on the mass of the central body. For our solar system, using the Sun's mass gives the same constant for all planets. This law allows calculation of orbital periods from orbital radii and vice versa.

**中文:** 比例常数仅取决于中心天体的质量。对于太阳系，使用太阳质量对所有行星得到相同的常数。该定律允许从轨道半径计算轨道周期，反之亦然。

### Common Misconceptions / 常见误区
- Thinking $T \propto r^{3/2}$ is the law (it's $T^2 \propto r^3$)
- Forgetting the constant depends on central mass
- Applying the law to satellites orbiting different central bodies without adjusting the constant

### Exam Tips / 考试提示
**English:** CAIE requires full derivation. Edexcel requires use of the relationship. When comparing two satellites around the same central mass, use $\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$ to avoid calculating the constant.

**中文:** CAIE要求完整推导。Edexcel要求使用该关系。比较绕同一中心天体的两颗卫星时，使用$\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$可避免计算常数。

## 4.3 Geostationary Satellites / 地球同步卫星

### Explanation / 解释
**English:** A [[Geostationary Satellites|geostationary satellite]] must satisfy three conditions:
1. Orbital period = 24 hours (Earth's rotational period)
2. Orbit in the equatorial plane
3. Orbit in the same direction as Earth's rotation

Using Kepler's third law with $T = 24 \text{ h} = 86,400 \text{ s}$:

$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3} \approx 42,000 \text{ km from Earth's centre}$$

This gives an altitude of approximately 36,000 km above Earth's surface.

**中文:** [[地球同步卫星]]必须满足三个条件：
1. 轨道周期 = 24小时（地球自转周期）
2. 轨道在赤道平面内
3. 轨道方向与地球自转方向相同

利用开普勒第三定律，$T = 24 \text{ 小时} = 86,400 \text{ 秒}$：

$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3} \approx 42,000 \text{ 公里（距地心）}$$

这对应距地球表面约36,000公里的高度。

### Physical Meaning / 物理意义
**English:** Geostationary satellites appear fixed in the sky, making them ideal for communications (TV, internet) and weather monitoring. A single geostationary satellite can cover about one-third of Earth's surface.

**中文:** 地球同步卫星在天空中看起来固定不动，使其成为通信（电视、互联网）和气象监测的理想选择。一颗地球同步卫星可覆盖约三分之一的地球表面。

### Common Misconceptions / 常见误区
- Confusing geostationary with geosynchronous (geosynchronous has 24h period but may not be equatorial)
- Thinking geostationary satellites are stationary relative to the Sun (they're stationary relative to Earth)
- Forgetting that the orbital radius is measured from Earth's centre, not its surface

### Exam Tips / 考试提示
**English:** Memorise the key numbers: orbital radius ≈ 42,000 km, altitude ≈ 36,000 km, period = 24 h, orbital speed ≈ 3.1 km/s. Be able to explain why geostationary satellites must be in the equatorial plane.

**中文:** 记住关键数字：轨道半径≈42,000公里，高度≈36,000公里，周期=24小时，轨道速度≈3.1公里/秒。能够解释为什么地球同步卫星必须在赤道平面内。

> 📷 **IMAGE PROMPT — [GS-01]: Geostationary Satellite Orbit**
> A diagram showing Earth with a satellite in geostationary orbit. Labels: Earth (radius 6400 km), Geostationary orbit (radius 42,000 km from centre, altitude 36,000 km), Equatorial plane. Show the satellite's orbital direction matching Earth's rotation. Include a communication dish on Earth pointing at the satellite. Style: clear 2D cross-section diagram. Exam importance: HIGH — frequently tested in both boards.

# 5. Essential Equations / 核心公式

## 5.1 Orbital Velocity / 轨道速度

$$v = \sqrt{\frac{GM}{r}}$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| $v$ | Orbital speed / 轨道速度 | m s⁻¹ |
| $G$ | Gravitational constant / 引力常数 | N m² kg⁻² |
| $M$ | Mass of central body / 中心天体质量 | kg |
| $r$ | Orbital radius (centre to centre) / 轨道半径（中心到中心） | m |

**Derivation / 推导:** $\frac{GMm}{r^2} = \frac{mv^2}{r} \Rightarrow v^2 = \frac{GM}{r}$

**Conditions / 条件:** Circular orbit, satellite mass << central mass, only gravitational force acting

**Limitations / 局限性:** Does not apply to elliptical orbits; assumes point mass or spherical symmetry

**Rearrangements / 变形:**
- $M = \frac{v^2 r}{G}$ (find central mass from orbital data)
- $r = \frac{GM}{v^2}$ (find orbital radius from speed)

## 5.2 Kepler's Third Law / 开普勒第三定律

$$T^2 = \frac{4\pi^2}{GM}r^3$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| $T$ | Orbital period / 轨道周期 | s |
| $r$ | Orbital radius / 轨道半径 | m |
| $G$ | Gravitational constant / 引力常数 | N m² kg⁻² |
| $M$ | Mass of central body / 中心天体质量 | kg |

**Derivation / 推导:** $v = \frac{2\pi r}{T}$, substitute into $v^2 = \frac{GM}{r}$: $\frac{4\pi^2 r^2}{T^2} = \frac{GM}{r} \Rightarrow T^2 = \frac{4\pi^2}{GM}r^3$

**Conditions / 条件:** Same as orbital velocity; also assumes constant orbital radius

**Limitations / 局限性:** For circular orbits only; elliptical orbits use semi-major axis

**Rearrangements / 变形:**
- $r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$ (find orbital radius from period)
- $M = \frac{4\pi^2 r^3}{GT^2}$ (find central mass from orbital data)

## 5.3 Alternative Forms / 替代形式

$$v = \sqrt{gr}$$

| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
|---------------|-----------------|-------------|
| $v$ | Orbital speed / 轨道速度 | m s⁻¹ |
| $g$ | Gravitational field strength at orbital radius / 轨道半径处引力场强度 | N kg⁻¹ |
| $r$ | Orbital radius / 轨道半径 | m |

> 📋 **Edexcel Only:** This form is particularly useful when $g$ at the orbital radius is known or can be calculated from $g = \frac{GM}{r^2}$.

# 6. Graphs and Relationships / 图表与关系

## 6.1 Orbital Velocity vs Orbital Radius / 轨道速度与轨道半径关系图

**Axes / 坐标轴:** x-axis: Orbital radius $r$ (m); y-axis: Orbital velocity $v$ (m s⁻¹)

**Shape / 形状:** Decreasing curve, $v \propto 1/\sqrt{r}$

**Gradient Meaning / 斜率意义:** $\frac{dv}{dr} = -\frac{1}{2}\sqrt{\frac{GM}{r^3}}$ — rate of change of orbital speed with radius

**Area Meaning / 面积意义:** No direct physical meaning for area under this curve

**Exam Interpretation / 考试解读:**
- **English:** Steep gradient at small r (near Earth's surface), shallow gradient at large r. Used to find orbital speed at any radius.
- **中文:** 小r处（近地表）斜率陡峭，大r处斜率平缓。用于求任意半径处的轨道速度。

**Common Questions / 常见问题:**
- Reading orbital speed for a given orbital radius
- Comparing speeds at different radii
- Explaining why outer planets move slower

> 📷 **IMAGE PROMPT — [GR-01]: v vs r Graph for Circular Orbits**
> A graph with orbital radius r on x-axis (from 6.4×10⁶ m to 1×10⁸ m) and orbital velocity v on y-axis (from 0 to 10,000 m/s). Show the curve v = √(GM/r) for Earth. Mark key points: LEO (r ≈ 6.6×10⁶ m, v ≈ 7800 m/s), GPS orbit (r ≈ 2.7×10⁷ m, v ≈ 3900 m/s), Geostationary (r ≈ 4.2×10⁷ m, v ≈ 3100 m/s). Style: scientific graph with labelled points. Exam importance: HIGH.

## 6.2 T² vs r³ Graph / T²与r³关系图

**Axes / 坐标轴:** x-axis: $r^3$ (m³); y-axis: $T^2$ (s²)

**Shape / 形状:** Straight line through origin

**Gradient Meaning / 斜率意义:** Gradient = $\frac{4\pi^2}{GM}$ — allows calculation of central mass $M$

**Area Meaning / 面积意义:** No direct physical meaning

**Exam Interpretation / 考试解读:**
- **English:** A straight line through origin confirms Kepler's third law. Gradient gives $\frac{4\pi^2}{GM}$, from which central mass can be calculated.
- **中文:** 过原点的直线验证了开普勒第三定律。斜率给出$\frac{4\pi^2}{GM}$，可由此计算中心天体质量。

**Common Questions / 常见问题:**
- Calculating central mass from gradient
- Predicting T for a given r using the graph
- Explaining why different central masses give different gradients

> 📷 **IMAGE PROMPT — [GR-02]: T² vs r³ Graph for Solar System Planets**
> A graph with r³ on x-axis and T² on y-axis showing data points for Mercury, Venus, Earth, Mars, Jupiter, Saturn. All points lie on a straight line through origin. Label gradient = 4π²/GM_sun. Include error bars. Style: scatter plot with line of best fit. Exam importance: MEDIUM-HIGH.

## 6.3 Gravitational Force vs Orbital Radius / 引力与轨道半径关系图

**Axes / 坐标轴:** x-axis: Orbital radius $r$ (m); y-axis: Gravitational force $F$ (N)

**Shape / 形状:** Decreasing curve, $F \propto 1/r^2$

**Gradient Meaning / 斜率意义:** $\frac{dF}{dr} = -\frac{2GMm}{r^3}$ — rate of change of gravitational force with distance

**Area Meaning / 面积意义:** Area under $F$ vs $r$ graph gives work done against gravitational force (related to [[Gravitational Potential]])

**Exam Interpretation / 考试解读:**
- **English:** Shows why inner planets experience stronger gravitational pull and thus orbit faster.
- **中文:** 显示为什么内行星受到更强的引力吸引，因此轨道速度更快。

# 7. Required Diagrams / 必备图表

## 7.1 Forces on a Satellite in Circular Orbit / 圆周轨道上卫星的受力图

> 📷 **IMAGE PROMPT — [DG-01]: Forces on an Orbiting Satellite**
> A diagram showing a satellite (represented as a small box or sphere) in circular orbit around Earth (large sphere). Draw a single arrow from the satellite towards Earth's centre labelled "Gravitational force F = GMm/r²" (this is the centripetal force). Show the velocity vector as a tangent arrow labelled "v". Include labels: Earth (mass M), satellite (mass m), orbital radius r. Add a note: "Only gravitational force acts — provides centripetal acceleration". Style: clear physics diagram with vector arrows. Exam importance: VERY HIGH — fundamental diagram.

## 7.2 Geostationary Satellite Orbit / 地球同步卫星轨道图

> 📷 **IMAGE PROMPT — [DG-02]: Geostationary Satellite System**
> A 2D cross-section showing Earth from above the North Pole. Draw the geostationary orbit as a circle in the equatorial plane (shown as a line through Earth's centre). Place 3 satellites equally spaced (120° apart) on this orbit. From each satellite, draw dashed lines showing coverage area (about 1/3 of Earth's surface each). Labels: "Geostationary orbit (r = 42,000 km)", "Altitude = 36,000 km", "Period T = 24 h", "Equatorial plane". Include a ground station with a dish antenna pointing at one satellite. Style: clear schematic diagram. Exam importance: HIGH.

## 7.3 Comparing Orbits at Different Radii / 不同半径轨道的比较

> 📷 **IMAGE PROMPT — [DG-03]: Comparison of Low Earth Orbit and Geostationary Orbit**
> A diagram showing Earth with two orbital paths: (1) Low Earth Orbit (LEO) at r ≈ 6,600 km (altitude ≈ 200 km) — shown as a tight circle close to Earth; (2) Geostationary orbit at r ≈ 42,000 km — shown as a much larger circle. For each orbit, show: orbital velocity vector (tangent), gravitational force vector (towards centre). Include a table comparing: orbital radius, period, speed, altitude. Labels: "LEO: v ≈ 7.8 km/s, T ≈ 90 min", "GEO: v ≈ 3.1 km/s, T = 24 h". Style: comparative diagram with data table. Exam importance: HIGH.

# 8. Worked Examples / 典型例题

## Example 1: Calculating Orbital Speed and Period / 计算轨道速度和周期

### Question / 题目
**English:** A weather satellite orbits Earth at an altitude of 800 km above the surface. Given:
- Earth's mass $M_E = 5.97 \times 10^{24}$ kg
- Earth's radius $R_E = 6.37 \times 10^6$ m
- Gravitational constant $G = 6.67 \times 10^{-11}$ N m² kg⁻²

Calculate:
(a) The orbital speed of the satellite
(b) The orbital period of the satellite in minutes

**中文:** 一颗气象卫星在地球表面上方800公里高度处运行。已知：
- 地球质量 $M_E = 5.97 \times 10^{24}$ kg
- 地球半径 $R_E = 6.37 \times 10^6$ m
- 引力常数 $G = 6.67 \times 10^{-11}$ N m² kg⁻²

计算：
(a) 卫星的轨道速度
(b) 卫星的轨道周期（以分钟为单位）

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — [EX-01]: Weather Satellite Orbit**
> A diagram showing Earth with a satellite in low Earth orbit at 800 km altitude. Label Earth's radius (6370 km), altitude (800 km), orbital radius (7170 km from centre). Show the satellite with velocity vector tangent to orbit. Style: simple schematic. Exam importance: for illustration.

### Solution / 解答

**(a) Orbital speed / 轨道速度:**

Step 1: Calculate orbital radius from centre of Earth
$$r = R_E + h = 6.37 \times 10^6 + 800 \times 10^3 = 7.17 \times 10^6 \text{ m}$$

Step 2: Use orbital velocity equation
$$v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{7.17 \times 10^6}}$$

Step 3: Calculate
$$v = \sqrt{\frac{3.98 \times 10^{14}}{7.17 \times 10^6}} = \sqrt{5.55 \times 10^7} = 7.45 \times 10^3 \text{ m s}^{-1}$$

$$\boxed{v = 7.45 \text{ km s}^{-1}}$$

**(b) Orbital period / 轨道周期:**

Step 1: Use $v = \frac{2\pi r}{T}$ rearranged to $T = \frac{2\pi r}{v}$

$$T = \frac{2\pi (7.17 \times 10^6)}{7.45 \times 10^3} = \frac{4.50 \times 10^7}{7.45 \times 10^3} = 6.04 \times 10^3 \text{ s}$$

Step 2: Convert to minutes
$$T = \frac{6.04 \times 10^3}{60} = 101 \text{ minutes}$$

$$\boxed{T = 101 \text{ min}}$$

### Final Answer / 最终答案
(a) $v = 7.45 \text{ km s}^{-1}$ (b) $T = 101 \text{ min}$

### Examiner Notes / 考官点评
**English:** Common errors include: (1) forgetting to add Earth's radius to altitude, (2) using Earth's surface gravity $g = 9.81$ instead of calculating $g$ at orbital radius, (3) unit conversion mistakes. Always show the orbital radius calculation explicitly. For part (b), using Kepler's third law directly is also acceptable: $T^2 = \frac{4\pi^2}{GM}r^3$.

**中文:** 常见错误包括：(1) 忘记将地球半径加到高度上，(2) 使用地表重力$g = 9.81$而非计算轨道半径处的$g$，(3) 单位换算错误。始终明确展示轨道半径的计算。对于(b)部分，直接使用开普勒第三定律也是可接受的：$T^2 = \frac{4\pi^2}{GM}r^3$。

## Example 2: Geostationary Satellite Radius / 地球同步卫星轨道半径

### Question / 题目
**English:** A geostationary satellite orbits Earth with a period of exactly 24 hours. Using the data below, calculate the orbital radius of the satellite.
- $G = 6.67 \times 10^{-11}$ N m² kg⁻²
- $M_E = 5.97 \times 10^{24}$ kg

Hence determine the altitude of the satellite above Earth's surface ($R_E = 6.37 \times 10^6$ m).

**中文:** 一颗地球同步卫星以恰好24小时的周期绕地球运行。使用以下数据计算卫星的轨道半径。
- $G = 6.67 \times 10^{-11}$ N m² kg⁻²
- $M_E = 5.97 \times 10^{24}$ kg

由此确定卫星在地球表面上方的高度（$R_E = 6.37 \times 10^6$ m）。

### Solution / 解答

Step 1: Convert period to seconds
$$T = 24 \times 60 \times 60 = 86,400 \text{ s}$$

Step 2: Use Kepler's third law rearranged for $r$
$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$$

Step 3: Substitute values
$$r = \left(\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})(86,400)^2}{4\pi^2}\right)^{1/3}$$

Step 4: Calculate numerator
$$GMT^2 = (6.67 \times 10^{-11})(5.97 \times 10^{24})(7.46 \times 10^9)$$
$$= (3.98 \times 10^{14})(7.46 \times 10^9) = 2.97 \times 10^{24}$$

Step 5: Complete calculation
$$r = \left(\frac{2.97 \times 10^{24}}{39.5}\right)^{1/3} = (7.52 \times 10^{22})^{1/3}$$

$$r = 4.22 \times 10^7 \text{ m} = 42,200 \text{ km}$$

Step 6: Calculate altitude
$$h = r - R_E = 4.22 \times 10^7 - 6.37 \times 10^6 = 3.58 \times 10^7 \text{ m}$$

$$\boxed{r = 42,200 \text{ km from centre}}$$
$$\boxed{h = 35,800 \text{ km above surface}}$$

### Final Answer / 最终答案
Orbital radius = 42,200 km from Earth's centre; Altitude = 35,800 km above surface

### Examiner Notes / 考官点评
**English:** This is a classic exam question. Key points: (1) Always convert hours to seconds, (2) Use cube root carefully, (3) Remember to subtract Earth's radius for altitude. The answer should be approximately 42,000 km (centre) and 36,000 km (altitude) — examiners accept small variations due to rounding. Memorising these values saves time in exams.

**中文:** 这是一个经典考题。关键点：(1) 始终将小时转换为秒，(2) 小心计算立方根，(3) 记得减去地球半径得到高度。答案应约为42,000公里（地心距）和36,000公里（高度）——考官接受因四舍五入产生的微小差异。记住这些数值可在考试中节省时间。

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|-------------------|----------------------------------|
| Derive orbital velocity equation | Very High | Medium | 📝 *待填入* |
| Calculate orbital speed from given data | Very High | Easy-Medium | 📝 *待填入* |
| Derive Kepler's third law | High (CAIE) | Medium-Hard | 📝 *待填入* |
| Calculate orbital period from radius | High | Medium | 📝 *待填入* |
| Geostationary satellite calculations | Very High | Medium | 📝 *待填入* |
| Compare orbits at different radii | Medium | Medium | 📝 *待填入* |
| Calculate central mass from orbital data | Medium | Medium | 📝 *待填入* |
| Explain why geostationary satellites are equatorial | High | Easy-Medium | 📝 *待填入* |
| Multi-step problem (combining concepts) | Medium | Hard | 📝 *待填入* |
| Graph interpretation (T² vs r³) | Medium | Medium | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:**
> **English:** Past paper references are being compiled. For CAIE 9702, look for questions in Papers 4 (structured questions) and occasionally Paper 2 (multiple choice). For Edexcel IAL, check Unit 4 Papers. Common question numbers will be added upon completion of the question bank.
> **中文:** 真题索引正在整理中。CAIE 9702的题目出现在试卷4（结构化问题）和偶尔的试卷2（选择题）中。Edexcel IAL请查阅单元4试卷。常见题号将在题库完成后添加。

**Common Command Words / 常见指令词:**
- **Derive / 推导:** Show step-by-step algebraic derivation from fundamental equations
- **Calculate / 计算:** Use given data with appropriate formula
- **Explain / 解释:** Give reasons with physics principles
- **State / 陈述:** Give a concise answer without explanation
- **Determine / 确定:** Calculate with reasoning
- **Compare / 比较:** Discuss similarities and differences
- **Sketch / 简绘:** Draw a graph showing general shape with labelled axes

# 10. Practical Skills Connections / 实验技能链接

**English:** While circular orbits cannot be directly experimented with in a school lab, several practical skills are developed through related activities:

1. **Simulation Software:** Using physics simulation software (e.g., PhET, Tracker) to model orbital motion and verify Kepler's laws
2. **Data Analysis:** Plotting $T^2$ against $r^3$ for planetary data to determine the mass of the Sun (gradient analysis)
3. **Uncertainties:** Propagating uncertainties when calculating orbital parameters from measured data
4. **Graph Plotting:** Drawing best-fit lines through $T^2$ vs $r^3$ data and calculating gradient with error bars
5. **Experimental Design:** For CAIE Paper 5, designing experiments to investigate factors affecting orbital period (e.g., using a mass on a string in circular motion as an analogue)

**中文:** 虽然圆周轨道无法在学校实验室直接实验，但通过相关活动可以培养多项实验技能：

1. **模拟软件：** 使用物理模拟软件（如PhET、Tracker）模拟轨道运动并验证开普勒定律
2. **数据分析：** 绘制行星数据的$T^2$与$r^3$关系图，确定太阳质量（斜率分析）
3. **不确定度：** 从测量数据计算轨道参数时传播不确定度
4. **图表绘制：** 在$T^2$与$r^3$数据上绘制最佳拟合线，计算带误差棒的斜率
5. **实验设计：** 对于CAIE试卷5，设计实验研究影响轨道周期的因素（例如，使用绳子上的质量做圆周运动作为类比）

> 📋 **CIE Only:** Paper 5 may ask students to design an experiment using a mass on a string to model orbital motion. Key considerations: measuring period with light gates, varying radius, controlling variables, reducing uncertainties.

> 📋 **Edexcel Only:** Unit 6 may include analysis of planetary data to verify Kepler's laws. Students should be comfortable with log-log plots ($\log T$ vs $\log r$) to determine the power relationship.

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Circular Orbits / 圆周轨道] --> B[Orbital Velocity / 轨道速度]
    A --> C[Kepler's Third Law / 开普勒第三定律]
    A --> D[Geostationary Satellites / 地球同步卫星]
    
    B --> E[v = √(GM/r)]
    B --> F[v = √(gr)]
    
    C --> G[T² = (4π²/GM)r³]
    C --> H[T² ∝ r³]
    
    D --> I[Conditions / 条件]
    I --> J[T = 24 h]
    I --> K[Equatorial plane / 赤道平面]
    I --> L[Same direction / 同方向]
    
    D --> M[Applications / 应用]
    M --> N[Communications / 通信]
    M --> O[Weather / 气象]
    M --> P[GPS / 全球定位系统]
    
    Q[Prerequisites / 前置知识] --> A
    Q --> R[Gravitational Force and Field / 引力与引力场]
    Q --> S[Centripetal Acceleration and Force / 向心加速度与力]
    
    A --> T[Related Topics / 相关主题]
    T --> U[Gravitational Potential / 引力势]
    
    V[Sub-topics / 子主题] --> A
    V --> W[Orbital Velocity / 轨道速度]
    V --> X[Kepler's Third Law / 开普勒第三定律]
    V --> Y[Geostationary Satellites / 地球同步卫星]
```

# 12. Examiner Insights / 考官洞察

**English:**

**Most Tested Ideas (CAIE 9702):**
1. Derivation of orbital velocity — appears in nearly every Paper 4
2. Geostationary satellite conditions and calculations — very common
3. Kepler's third law derivation — frequently tested in CAIE
4. Comparing orbital parameters at different radii
5. Calculating central mass from orbital data

**Most Tested Ideas (Edexcel IAL):**
1. Using $v = \sqrt{GM/r}$ for calculations
2. Geostationary satellite applications and conditions
3. $T^2 \propto r^3$ relationship and its use
4. Alternative form $v = \sqrt{gr}$
5. Multi-step problems combining orbital mechanics

**Mark Scheme Wording / 评分方案措辞:**
- "Equating gravitational force to centripetal force" — must be explicitly stated
- "Cancelling m" — show this step clearly
- "Substituting v = 2πr/T" — for Kepler's law derivation
- "Using correct units" — especially converting hours to seconds

**Common Lost Marks / 常见失分点:**
- Forgetting to add Earth's radius to altitude
- Using $g = 9.81$ at surface instead of $g$ at orbital radius
- Not showing cancellation of satellite mass
- Incorrect unit conversions (hours to seconds)
- Confusing orbital radius with altitude
- Not stating assumptions (circular orbit, only gravity)

**High-Scoring Structures / 高分答题结构:**
1. State the principle (gravitational force = centripetal force)
2. Write the equation with symbols
3. Substitute numbers with units
4. Show algebraic manipulation clearly
5. Box final answer with correct units and significant figures

**中文:**

**最常考内容（CAIE 9702）：**
1. 轨道速度的推导 — 几乎每份试卷4都出现
2. 地球同步卫星的条件和计算 — 非常常见
3. 开普勒第三定律的推导 — CAIE经常考
4. 比较不同半径处的轨道参数
5. 从轨道数据计算中心天体质量

**最常考内容（Edexcel IAL）：**
1. 使用$v = \sqrt{GM/r}$进行计算
2. 地球同步卫星的应用和条件
3. $T^2 \propto r^3$关系及其应用
4. 替代形式$v = \sqrt{gr}$
5. 结合轨道力学的多步骤问题

**常见失分点：**
- 忘记将地球半径加到高度上
- 使用地表$g = 9.81$而非轨道半径处的$g$
- 未展示卫星质量的消去
- 单位换算错误（小时到秒）
- 混淆轨道半径与高度
- 未说明假设条件（圆形轨道、仅受引力）

# 13. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|-----------------|-------------------|
| **Core Principle / 核心原理** | Gravitational force provides centripetal force: $\frac{GMm}{r^2} = \frac{mv^2}{r}$ / 引力提供向心力 |
| **Orbital Velocity / 轨道速度** | $v = \sqrt{\frac{GM}{r}}$ — decreases as radius increases / 随半径增大而减小 |
| **Kepler's Third Law / 开普勒第三定律** | $T^2 = \frac{4\pi^2}{GM}r^3$ — $T^2 \propto r^3$ for same central mass / 同一中心天体 |
| **Geostationary / 地球同步** | $T = 24$ h, $r = 42,000$ km, altitude $= 36,000$ km, equatorial plane / 赤道平面 |
| **Key Assumptions / 关键假设** | Circular orbit, satellite mass negligible, only gravity acts / 圆形轨道、卫星质量可忽略、仅受引力 |
| **Common Units / 常用单位** | $r$ in m, $T$ in s, $v$ in m s⁻¹, $M$ in kg |
| **Edexcel Alternative / Edexcel替代形式** | $v = \sqrt{gr}$ where $g = GM/r^2$ at orbital radius |
| **Graph: $T^2$ vs $r^3$** | Straight line through origin, gradient $= 4\pi^2/GM$ / 过原点直线 |
| **Central Mass Calculation / 中心质量计算** | $M = \frac{4\pi^2 r^3}{GT^2}$ or $M = \frac{v^2 r}{G}$ |
| **Orbital Radius from Period / 由周期求轨道半径** | $r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$ |
| **Comparison Method / 比较方法** | $\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$ for same central mass / 同一中心天体 |
| **Common Mistake / 常见错误** | Using Earth's surface radius instead of orbital radius / 使用地表半径而非轨道半径 |

# 14. Metadata / 元数据

```yaml
title:
  en: "Circular Orbits"
  cn: "圆周轨道"
subject: Physics
syllabus: [CAIE 9702, Edexcel IAL]
cie_ref: "15.3 (a-e)"
edexcel_ref: "WPH14 U4: 6.11-6.15"
level: A2
node_type: topic_hub
difficulty: advanced
prerequisites:
  - "[[Gravitational Force and Field]]"
  - "[[Centripetal Acceleration and Force]]"
related_topics:
  - "[[Gravitational Potential]]"
sub_topics:
  - "[[Orbital Velocity]]"
  - "[[Kepler's Third Law]]"
  - "[[Geostationary Satellites]]"
formula_count: 3
diagram_count: 6
exam_frequency: very_high
language: bilingual_en_cn
last_updated: 2024-01
```

> 📝 **Note / 备注:** This hub file serves as the central node for the Circular Orbits topic. Leaf nodes [[Orbital Velocity]], [[Kepler's Third Law]], and [[Geostationary Satellites]] contain detailed, focused content on each sub-topic. All cross-references use [[wikilinks]] for Obsidian knowledge graph integration.