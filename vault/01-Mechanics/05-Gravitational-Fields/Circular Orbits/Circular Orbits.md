# 1. Overview / 概述

**English:**
This topic, **Circular Orbits**, is a cornerstone of A2 Physics, bridging [[Gravitational Force and Field]] with [[Centripetal Acceleration and Force]] to explain how celestial bodies and artificial satellites move under gravity. It studies the conditions for stable circular motion in a gravitational field, deriving relationships between orbital radius, speed, period, and the mass of the central body. The key insight is that the gravitational force provides the necessary centripetal force, leading to a set of powerful equations that govern everything from a planet orbiting a star to a satellite orbiting Earth.

This topic matters because it explains the fundamental mechanics of the universe—why the Moon stays in orbit, how satellites enable global communication and GPS, and how we can calculate the mass of distant stars and black holes. Real-world applications include satellite communication ([[Geostationary Satellites]]), space exploration, and astronomical observations. In examinations, both Cambridge 9702 and Edexcel IAL assess this topic through calculations of orbital parameters, explanations of satellite behaviour, and derivations of [[Kepler's Third Law]]. It is a high-difficulty, high-reward topic that tests both mathematical manipulation and conceptual understanding.

**中文：**
本主题**圆形轨道**是A2物理学的基石，它将[[引力与场]]与[[向心加速度与力]]联系起来，解释天体和人造卫星如何在引力作用下运动。它研究在引力场中稳定圆周运动的条件，推导出轨道半径、速度、周期和中心天体质量之间的关系。关键见解是引力提供必要的向心力，从而产生一组强大的方程，这些方程支配着从绕恒星运行的行星到绕地球运行的卫星的一切。

这个主题之所以重要，是因为它解释了宇宙的基本力学——为什么月球保持在轨道上，卫星如何实现全球通信和GPS，以及我们如何计算遥远恒星和黑洞的质量。实际应用包括卫星通信（[[地球静止卫星]]）、太空探索和天文观测。在考试中，剑桥9702和爱德思IAL都通过轨道参数计算、卫星行为解释和[[开普勒第三定律]]的推导来评估本主题。这是一个高难度、高回报的主题，考验数学操作和概念理解。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

**English:**
The following table maps the specific learning objectives from both exam boards. Students must be able to apply these to both natural (planets, moons) and artificial (satellites) systems.

**中文：**
下表映射了两个考试委员会的具体学习目标。学生必须能够将这些目标应用于自然（行星、卫星）和人造（卫星）系统。

| CAIE 9702 (15.3 a-e) | Edexcel IAL (WPH14 U4: 6.11-6.15) |
|----------------------|-----------------------------------|
| (a) Understand that a gravitational force provides the centripetal force for circular orbits. | 6.11 Understand that for a body in a circular orbit, the gravitational force provides the centripetal force. |
| (b) Derive and use the relationship $v = \sqrt{\frac{GM}{r}}$ for orbital speed. | 6.12 Derive and use the relationship $v = \sqrt{\frac{GM}{r}}$ for orbital speed. |
| (c) Derive and use the relationship $T = \frac{2\pi r}{v}$ and $T^2 = \frac{4\pi^2 r^3}{GM}$ ([[Kepler's Third Law]]). | 6.13 Derive and use the relationship $T^2 = \frac{4\pi^2 r^3}{GM}$ for the period of an orbit. |
| (d) Understand that for a satellite in a circular orbit, the centripetal force is provided by the gravitational force, leading to a constant speed. | 6.14 Understand that for a satellite in a circular orbit, the centripetal force is provided by the gravitational force, leading to a constant speed. |
| (e) Describe and explain the characteristics of a [[Geostationary Satellites|geostationary orbit]]. | 6.15 Describe and explain the characteristics of a geostationary orbit. |

> 📋 **CIE Only:** CAIE explicitly requires students to "derive and use" the relationships, meaning derivations from first principles are examinable. They also place emphasis on understanding the energy considerations of orbits (linked to [[Gravitational Potential]]).
>
> 📋 **Edexcel Only:** Edexcel explicitly includes the derivation of $v = \sqrt{\frac{GM}{r}}$ and $T^2 = \frac{4\pi^2 r^3}{GM}$ in their specification. They also expect students to apply these to binary star systems and to calculate the mass of a central body from orbital data.

**Examiner Expectations / 考官期望:**
- **English:** Examiners expect students to clearly state the principle that gravitational force = centripetal force as the starting point for any derivation or calculation. Marks are often awarded for showing this step explicitly. Students must be able to manipulate equations algebraically and handle powers of 10 and standard form confidently. For geostationary satellites, memorising the three key characteristics (period = 24 hours, equatorial orbit, fixed position above a point on Earth) is essential.
- **中文：** 考官期望学生明确陈述引力 = 向心力这一原理，作为任何推导或计算的起点。明确展示这一步骤通常会获得分数。学生必须能够熟练地进行代数方程变换，并自信地处理10的幂和标准形式。对于地球静止卫星，记住三个关键特征（周期=24小时，赤道轨道，在地球上某一点上方固定位置）至关重要。

---

# 3. Core Definitions / 核心定义

**English:**
The following table provides the essential definitions for this topic, with common mistakes highlighted.

**中文：**
下表提供了本主题的基本定义，并强调了常见错误。

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Circular Orbit / 圆形轨道** | A path of an object around a central body where the distance from the centre remains constant, and the motion is governed by a centripetal force. | 物体围绕中心天体的路径，其中距中心的距离保持恒定，运动由向心力支配。 | Confusing with elliptical orbits; assuming speed is constant in all orbits (it is constant only in circular orbits). |
| **Orbital Speed / 轨道速度** | The constant speed of an object in a circular orbit, given by $v = \sqrt{\frac{GM}{r}}$, where $M$ is the mass of the central body and $r$ is the orbital radius. | 物体在圆形轨道中的恒定速度，由 $v = \sqrt{\frac{GM}{r}}$ 给出，其中 $M$ 是中心天体的质量，$r$ 是轨道半径。 | Thinking orbital speed depends on the mass of the orbiting object (it does not, as it cancels out in the derivation). |
| **Orbital Period / 轨道周期** | The time taken for an object to complete one full orbit around a central body. | 物体绕中心天体完成一整圈轨道所需的时间。 | Forgetting that period is measured in seconds in equations; confusing with frequency. |
| **[[Geostationary Satellites\|Geostationary Orbit / 地球静止轨道]]** | A circular orbit around the Earth's equator with a period of 24 hours, such that the satellite appears stationary above a fixed point on the Earth's surface. | 绕地球赤道的圆形轨道，周期为24小时，使得卫星看起来在地球表面某固定点上方静止。 | Thinking any orbit with a 24-hour period is geostationary (it must also be equatorial and circular). |
| **[[Kepler's Third Law]] / 开普勒第三定律** | The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit ($T^2 \propto r^3$). For circular orbits, this becomes $T^2 = \frac{4\pi^2 r^3}{GM}$. | 行星轨道周期的平方与其轨道半长轴的立方成正比（$T^2 \propto r^3$）。对于圆形轨道，这变为 $T^2 = \frac{4\pi^2 r^3}{GM}$。 | Applying the law without the constant of proportionality; forgetting that $M$ is the mass of the central body, not the orbiting body. |
| **Centripetal Force / 向心力** | The net force required to keep an object moving in a circular path, directed towards the centre of the circle. In orbits, this is provided by [[Gravitational Force and Field\|gravitational force]]. | 使物体保持圆周运动所需的净力，方向指向圆心。在轨道中，这由[[引力与场\|引力]]提供。 | Thinking centripetal force is a separate force; it is the resultant of other forces (here, gravity). |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Gravitational Force as Centripetal Force / 引力作为向心力

### Explanation / 解释
**English:**
The fundamental principle of circular orbits is that the [[Gravitational Force and Field|gravitational force]] acting on an orbiting object provides exactly the required [[Centripetal Acceleration and Force|centripetal force]] to keep it in a circular path. For an object of mass $m$ orbiting a central body of mass $M$ at a distance $r$ from its centre, the gravitational force is given by Newton's law of gravitation:

$$F_g = \frac{GMm}{r^2}$$

The centripetal force required for circular motion at speed $v$ is:

$$F_c = \frac{mv^2}{r}$$

For a stable circular orbit, these two forces must be equal:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

This equality is the starting point for all derivations in this topic. Notice that the mass of the orbiting object $m$ cancels out, meaning the orbital speed is independent of the mass of the satellite.

**中文：**
圆形轨道的基本原理是，作用在轨道物体上的[[引力与场|引力]]恰好提供了使其保持圆周运动所需的[[向心加速度与力|向心力]]。对于质量为 $m$、绕中心天体（质量为 $M$）在距离其中心 $r$ 处运行的物体，引力由牛顿万有引力定律给出：

$$F_g = \frac{GMm}{r^2}$$

以速度 $v$ 进行圆周运动所需的向心力为：

$$F_c = \frac{mv^2}{r}$$

对于稳定的圆形轨道，这两个力必须相等：

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

这个等式是本主题所有推导的起点。注意，轨道物体的质量 $m$ 被消去，这意味着轨道速度与卫星的质量无关。

### Physical Meaning / 物理意义
**English:**
This concept explains why the Moon doesn't fall into the Earth and why satellites can orbit without fuel. The gravitational pull is perfectly balanced by the satellite's inertia—its tendency to move in a straight line. The satellite is essentially "falling" around the Earth, constantly being pulled towards it but moving sideways fast enough that it keeps missing.

**中文：**
这个概念解释了为什么月球不会掉到地球上，以及为什么卫星可以在没有燃料的情况下运行。引力被卫星的惯性完美平衡——它倾向于直线运动。卫星本质上是围绕地球“下落”，不断被拉向地球，但侧向移动速度足够快，以至于它不断错过。

### Common Misconceptions / 常见误区
- **English:** Students often think there is no force acting on an orbiting object because it is "weightless". In fact, gravity is still acting; weightlessness is due to freefall, not absence of force.
- **中文：** 学生常常认为轨道物体上没有力作用，因为它“失重”。事实上，引力仍然在作用；失重是由于自由落体，而不是没有力。
- **English:** Another misconception is that the centripetal force is an additional force. It is the resultant of gravitational force.
- **中文：** 另一个误解是向心力是一个额外的力。它是引力的合力。

### Exam Tips / 考试提示
**English:**
Always start any orbital calculation by writing the equality $F_g = F_c$. This is a mark-scoring step. Examiners look for this explicit statement before substituting equations.

**中文：**
始终通过写出等式 $F_g = F_c$ 来开始任何轨道计算。这是一个得分步骤。考官在代入方程之前会寻找这个明确的陈述。

---

## 4.2 Orbital Speed / 轨道速度

### Explanation / 解释
**English:**
From the equality $F_g = F_c$, we can derive the expression for orbital speed. Cancelling $m$ and rearranging:

$$\frac{GM}{r^2} = \frac{v^2}{r}$$

$$v^2 = \frac{GM}{r}$$

$$v = \sqrt{\frac{GM}{r}}$$

This is the [[Orbital Velocity|orbital speed]] for a circular orbit. Key observations:
- $v \propto \frac{1}{\sqrt{r}}$: As orbital radius increases, speed decreases.
- $v$ is independent of the mass of the orbiting object.
- $v$ depends only on the mass of the central body $M$ and the orbital radius $r$.

**中文：**
从等式 $F_g = F_c$，我们可以推导出轨道速度的表达式。消去 $m$ 并重新排列：

$$\frac{GM}{r^2} = \frac{v^2}{r}$$

$$v^2 = \frac{GM}{r}$$

$$v = \sqrt{\frac{GM}{r}}$$

这就是圆形轨道的[[轨道速度|轨道速度]]。关键观察：
- $v \propto \frac{1}{\sqrt{r}}$：随着轨道半径增加，速度减小。
- $v$ 与轨道物体的质量无关。
- $v$ 仅取决于中心天体的质量 $M$ 和轨道半径 $r$。

### Physical Meaning / 物理意义
**English:**
A satellite in low Earth orbit (e.g., 200 km altitude) must travel at about 7.8 km/s to stay in orbit. The Moon, much farther away, orbits at only about 1 km/s. This inverse square root relationship explains why inner planets orbit faster than outer planets.

**中文：**
低地球轨道（例如，200公里高度）的卫星必须以大约7.8公里/秒的速度运行才能保持在轨道上。月球距离远得多，轨道速度仅为约1公里/秒。这种平方根反比关系解释了为什么内行星比外行星运行得更快。

### Common Misconceptions / 常见误区
- **English:** Thinking that increasing orbital radius increases speed (it decreases it).
- **中文：** 认为增加轨道半径会增加速度（实际上会减小）。
- **English:** Forgetting that $r$ is the distance from the centre of the central body, not the altitude above its surface.
- **中文：** 忘记 $r$ 是距中心天体中心的距离，而不是其表面以上的高度。

### Exam Tips / 考试提示
**English:**
When calculating orbital speed, always check whether the question gives altitude or orbital radius. If altitude is given, add the radius of the central body to get $r$. For Earth, $R_E = 6.37 \times 10^6$ m.

**中文：**
计算轨道速度时，始终检查问题是给出高度还是轨道半径。如果给出高度，则加上中心天体的半径得到 $r$。对于地球，$R_E = 6.37 \times 10^6$ 米。

---

## 4.3 Orbital Period and Kepler's Third Law / 轨道周期与开普勒第三定律

### Explanation / 解释
**English:**
The orbital period $T$ is related to orbital speed and radius by:

$$v = \frac{2\pi r}{T}$$

Substituting $v = \sqrt{\frac{GM}{r}}$:

$$\frac{2\pi r}{T} = \sqrt{\frac{GM}{r}}$$

Squaring both sides:

$$\frac{4\pi^2 r^2}{T^2} = \frac{GM}{r}$$

Rearranging for $T^2$:

$$T^2 = \frac{4\pi^2 r^3}{GM}$$

This is [[Kepler's Third Law]] for circular orbits. Key observations:
- $T^2 \propto r^3$: The square of the period is proportional to the cube of the orbital radius.
- The constant of proportionality is $\frac{4\pi^2}{GM}$, which depends only on the mass of the central body.
- This law allows us to calculate the mass of a central body if we know the orbital period and radius of a satellite.

**中文：**
轨道周期 $T$ 与轨道速度和半径的关系为：

$$v = \frac{2\pi r}{T}$$

代入 $v = \sqrt{\frac{GM}{r}}$：

$$\frac{2\pi r}{T} = \sqrt{\frac{GM}{r}}$$

两边平方：

$$\frac{4\pi^2 r^2}{T^2} = \frac{GM}{r}$$

重新排列求 $T^2$：

$$T^2 = \frac{4\pi^2 r^3}{GM}$$

这就是圆形轨道的[[开普勒第三定律]]。关键观察：
- $T^2 \propto r^3$：周期的平方与轨道半径的立方成正比。
- 比例常数为 $\frac{4\pi^2}{GM}$，仅取决于中心天体的质量。
- 这个定律允许我们通过已知卫星的轨道周期和半径来计算中心天体的质量。

### Physical Meaning / 物理意义
**English:**
This law explains why outer planets have much longer years. Jupiter's orbital radius is about 5.2 times Earth's, so its orbital period is about $5.2^{3/2} \approx 11.9$ Earth years. It also allows astronomers to determine the mass of stars and black holes by observing the orbits of their companions.

**中文：**
这个定律解释了为什么外行星有更长的年份。木星的轨道半径大约是地球的5.2倍，所以它的轨道周期大约是 $5.2^{3/2} \approx 11.9$ 地球年。它还允许天文学家通过观察其伴星的轨道来确定恒星和黑洞的质量。

### Common Misconceptions / 常见误区
- **English:** Applying Kepler's Third Law without the constant $\frac{4\pi^2}{GM}$, i.e., using $T^2 \propto r^3$ without the proportionality constant.
- **中文：** 在没有常数 $\frac{4\pi^2}{GM}$ 的情况下应用开普勒第三定律，即使用 $T^2 \propto r^3$ 而没有比例常数。
- **English:** Forgetting that $M$ is the mass of the central body, not the orbiting body.
- **中文：** 忘记 $M$ 是中心天体的质量，而不是轨道物体的质量。

### Exam Tips / 考试提示
**English:**
When using $T^2 = \frac{4\pi^2 r^3}{GM}$, ensure all quantities are in SI units. Period must be in seconds, radius in metres, and mass in kilograms. A common trick is to give the period in hours or days—convert to seconds first.

**中文：**
使用 $T^2 = \frac{4\pi^2 r^3}{GM}$ 时，确保所有量都是SI单位。周期必须以秒为单位，半径以米为单位，质量以千克为单位。一个常见的技巧是给出以小时或天为单位的周期——先转换为秒。

---

## 4.4 Geostationary Satellites / 地球静止卫星

### Explanation / 解释
**English:**
A [[Geostationary Satellites|geostationary satellite]] is a special type of satellite that appears stationary above a fixed point on the Earth's equator. This is achieved by satisfying three conditions:
1. **Orbital Period:** $T = 24$ hours (exactly 86,400 seconds), matching the Earth's rotational period.
2. **Orbital Plane:** The orbit must be in the equatorial plane (directly above the equator).
3. **Direction:** The satellite must orbit in the same direction as the Earth's rotation (west to east).

Using Kepler's Third Law, we can calculate the orbital radius for a geostationary orbit:

$$T^2 = \frac{4\pi^2 r^3}{GM_E}$$

$$r^3 = \frac{GM_E T^2}{4\pi^2}$$

$$r = \sqrt[3]{\frac{GM_E T^2}{4\pi^2}}$$

Substituting $G = 6.67 \times 10^{-11}$ N m² kg⁻², $M_E = 5.97 \times 10^{24}$ kg, and $T = 86,400$ s gives $r \approx 4.23 \times 10^7$ m. This is about 42,300 km from the Earth's centre, or approximately 35,800 km above the Earth's surface.

**中文：**
[[地球静止卫星|地球静止卫星]]是一种特殊的卫星，它看起来在地球赤道上某固定点上方静止。这是通过满足三个条件实现的：
1. **轨道周期：** $T = 24$ 小时（精确为86,400秒），与地球的自转周期匹配。
2. **轨道平面：** 轨道必须在赤道平面内（赤道正上方）。
3. **方向：** 卫星必须与地球自转方向相同（自西向东）运行。

使用开普勒第三定律，我们可以计算地球静止轨道的轨道半径：

$$T^2 = \frac{4\pi^2 r^3}{GM_E}$$

$$r^3 = \frac{GM_E T^2}{4\pi^2}$$

$$r = \sqrt[3]{\frac{GM_E T^2}{4\pi^2}}$$

代入 $G = 6.67 \times 10^{-11}$ N m² kg⁻², $M_E = 5.97 \times 10^{24}$ kg, 和 $T = 86,400$ s 得到 $r \approx 4.23 \times 10^7$ m。这大约是距地球中心42,300公里，或地球表面以上约35,800公里。

### Physical Meaning / 物理意义
**English:**
Geostationary satellites are ideal for communication (TV, internet, phone) because their fixed position means ground antennas can point at them without tracking. They are also used for weather monitoring, as they can continuously observe the same region of the Earth.

**中文：**
地球静止卫星非常适合通信（电视、互联网、电话），因为它们的位置固定意味着地面天线可以指向它们而无需跟踪。它们也用于天气监测，因为它们可以连续观察地球的同一区域。

### Common Misconceptions / 常见误区
- **English:** Thinking any satellite with a 24-hour period is geostationary. It must also be equatorial and circular.
- **中文：** 认为任何周期为24小时的卫星都是地球静止的。它还必须是在赤道平面内且为圆形轨道。
- **English:** Confusing geostationary with geosynchronous. A geosynchronous orbit has a 24-hour period but may be inclined, so it appears to move in a figure-8 pattern.
- **中文：** 混淆地球静止与地球同步。地球同步轨道周期为24小时，但可能有倾角，因此看起来呈8字形运动。

### Exam Tips / 考试提示
**English:**
Memorise the three conditions for a geostationary orbit. In exam questions, you may be asked to calculate the orbital radius or speed of a geostationary satellite, or to explain why a satellite in a different orbit cannot be geostationary.

**中文：**
记住地球静止轨道的三个条件。在考试问题中，你可能会被要求计算地球静止卫星的轨道半径或速度，或者解释为什么在不同轨道中的卫星不能是地球静止的。

---

# 5. Essential Equations / 核心公式

## 5.1 Gravitational Force / 万有引力

**Equation / 公式:**
$$F_g = \frac{GMm}{r^2}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $F_g$ | Gravitational force | 万有引力 | N (Newtons) |
| $G$ | Gravitational constant ($6.67 \times 10^{-11}$) | 万有引力常数 | N m² kg⁻² |
| $M$ | Mass of central body | 中心天体质量 | kg |
| $m$ | Mass of orbiting object | 轨道物体质量 | kg |
| $r$ | Distance between centres | 中心间距离 | m |

**Derivation / 推导:**
**English:** This is Newton's law of universal gravitation, an empirical law. It is not derived but stated. The constant $G$ was determined experimentally by Henry Cavendish.

**中文：** 这是牛顿的万有引力定律，是一个经验定律。它不是推导出来的，而是陈述的。常数 $G$ 由亨利·卡文迪许通过实验确定。

**Conditions / 适用条件:**
**English:** Applies to point masses or spherically symmetric objects. For objects above the Earth's surface, $r$ is the distance from the Earth's centre.

**中文：** 适用于点质量或球对称物体。对于地球表面以上的物体，$r$ 是距地球中心的距离。

**Limitations / 局限性:**
**English:** Does not apply at very small distances (quantum scale) or very high speeds (relativistic scale). It assumes instantaneous action at a distance.

**中文：** 不适用于非常小的距离（量子尺度）或非常高的速度（相对论尺度）。它假设瞬时超距作用。

**Rearrangements / 变形:**
**English:**
- $M = \frac{F_g r^2}{Gm}$ (to find mass of central body)
- $r = \sqrt{\frac{GMm}{F_g}}$ (to find orbital radius)

**中文：**
- $M = \frac{F_g r^2}{Gm}$ (求中心天体质量)
- $r = \sqrt{\frac{GMm}{F_g}}$ (求轨道半径)

---

## 5.2 Centripetal Force / 向心力

**Equation / 公式:**
$$F_c = \frac{mv^2}{r}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $F_c$ | Centripetal force | 向心力 | N |
| $m$ | Mass of orbiting object | 轨道物体质量 | kg |
| $v$ | Orbital speed | 轨道速度 | m s⁻¹ |
| $r$ | Orbital radius | 轨道半径 | m |

**Derivation / 推导:**
**English:** Derived from Newton's second law ($F = ma$) and the expression for centripetal acceleration ($a = v^2/r$). The centripetal acceleration is derived from the geometry of circular motion.

**中文：** 从牛顿第二定律 ($F = ma$) 和向心加速度表达式 ($a = v^2/r$) 推导得出。向心加速度是从圆周运动的几何学推导出来的。

**Conditions / 适用条件:**
**English:** Applies only to uniform circular motion (constant speed). The force is always directed towards the centre of the circle.

**中文：** 仅适用于匀速圆周运动（恒定速度）。力始终指向圆心。

**Limitations / 局限性:**
**English:** Does not apply to non-circular paths or variable speed circular motion.

**中文：** 不适用于非圆形路径或变速圆周运动。

**Rearrangements / 变形:**
**English:**
- $v = \sqrt{\frac{F_c r}{m}}$ (to find speed)
- $r = \frac{mv^2}{F_c}$ (to find radius)

**中文：**
- $v = \sqrt{\frac{F_c r}{m}}$ (求速度)
- $r = \frac{mv^2}{F_c}$ (求半径)

---

## 5.3 Orbital Speed / 轨道速度

**Equation / 公式:**
$$v = \sqrt{\frac{GM}{r}}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v$ | Orbital speed | 轨道速度 | m s⁻¹ |
| $G$ | Gravitational constant | 万有引力常数 | N m² kg⁻² |
| $M$ | Mass of central body | 中心天体质量 | kg |
| $r$ | Orbital radius | 轨道半径 | m |

**Derivation / 推导:**
**English:**
Set gravitational force equal to centripetal force:
$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$
Cancel $m$:
$$\frac{GM}{r^2} = \frac{v^2}{r}$$
Multiply both sides by $r$:
$$\frac{GM}{r} = v^2$$
Take square root:
$$v = \sqrt{\frac{GM}{r}}$$

**中文：**
令引力等于向心力：
$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$
消去 $m$：
$$\frac{GM}{r^2} = \frac{v^2}{r}$$
两边乘以 $r$：
$$\frac{GM}{r} = v^2$$
取平方根：
$$v = \sqrt{\frac{GM}{r}}$$

**Conditions / 适用条件:**
**English:** Applies only to circular orbits around a spherically symmetric central body. The orbiting object's mass must be negligible compared to the central body.

**中文：** 仅适用于围绕球对称中心天体的圆形轨道。轨道物体的质量与中心天体相比必须可忽略不计。

**Limitations / 局限性:**
**English:** Does not apply to elliptical orbits (where speed varies). Assumes no other forces (e.g., atmospheric drag, solar radiation pressure).

**中文：** 不适用于椭圆轨道（速度变化）。假设没有其他力（例如，大气阻力、太阳辐射压力）。

**Rearrangements / 变形:**
**English:**
- $M = \frac{v^2 r}{G}$ (to find mass of central body)
- $r = \frac{GM}{v^2}$ (to find orbital radius)

**中文：**
- $M = \frac{v^2 r}{G}$ (求中心天体质量)
- $r = \frac{GM}{v^2}$ (求轨道半径)

---

## 5.4 Orbital Period (Kepler's Third Law) / 轨道周期（开普勒第三定律）

**Equation / 公式:**
$$T^2 = \frac{4\pi^2 r^3}{GM}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $T$ | Orbital period | 轨道周期 | s |
| $G$ | Gravitational constant | 万有引力常数 | N m² kg⁻² |
| $M$ | Mass of central body | 中心天体质量 | kg |
| $r$ | Orbital radius | 轨道半径 | m |

**Derivation / 推导:**
**English:**
Start with the orbital speed equation and the relationship between speed, period, and radius:
$$v = \sqrt{\frac{GM}{r}} \quad \text{and} \quad v = \frac{2\pi r}{T}$$
Equate the two expressions for $v$:
$$\frac{2\pi r}{T} = \sqrt{\frac{GM}{r}}$$
Square both sides:
$$\frac{4\pi^2 r^2}{T^2} = \frac{GM}{r}$$
Multiply both sides by $T^2$:
$$4\pi^2 r^2 = \frac{GM T^2}{r}$$
Multiply both sides by $r$:
$$4\pi^2 r^3 = GM T^2$$
Divide both sides by $GM$:
$$T^2 = \frac{4\pi^2 r^3}{GM}$$

**中文：**
从轨道速度方程以及速度、周期和半径之间的关系开始：
$$v = \sqrt{\frac{GM}{r}} \quad \text{和} \quad v = \frac{2\pi r}{T}$$
令 $v$ 的两个表达式相等：
$$\frac{2\pi r}{T} = \sqrt{\frac{GM}{r}}$$
两边平方：
$$\frac{4\pi^2 r^2}{T^2} = \frac{GM}{r}$$
两边乘以 $T^2$：
$$4\pi^2 r^2 = \frac{GM T^2}{r}$$
两边乘以 $r$：
$$4\pi^2 r^3 = GM T^2$$
两边除以 $GM$：
$$T^2 = \frac{4\pi^2 r^3}{GM}$$

**Conditions / 适用条件:**
**English:** Applies to any object in a circular orbit around a much larger central body. The central body must be spherically symmetric.

**中文：** 适用于围绕大得多的中心天体的圆形轨道中的任何物体。中心天体必须是球对称的。

**Limitations / 局限性:**
**English:** Does not apply if the orbiting object's mass is comparable to the central body (e.g., binary star systems without approximation). For elliptical orbits, $r$ is replaced by the semi-major axis $a$.

**中文：** 如果轨道物体的质量与中心天体相当（例如，没有近似的双星系统），则不适用。对于椭圆轨道，$r$ 被半长轴 $a$ 替换。

**Rearrangements / 变形:**
**English:**
- $M = \frac{4\pi^2 r^3}{G T^2}$ (to find mass of central body)
- $r = \sqrt[3]{\frac{GM T^2}{4\pi^2}}$ (to find orbital radius)
- $T = 2\pi \sqrt{\frac{r^3}{GM}}$ (to find period)

**中文：**
- $M = \frac{4\pi^2 r^3}{G T^2}$ (求中心天体质量)
- $r = \sqrt[3]{\frac{GM T^2}{4\pi^2}}$ (求轨道半径)
- $T = 2\pi \sqrt{\frac{r^3}{GM}}$ (求周期)

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Orbital Speed vs Orbital Radius / 轨道速度与轨道半径

### Axes / 坐标轴
**English:** x-axis: Orbital radius $r$ (m); y-axis: Orbital speed $v$ (m s⁻¹)
**中文：** x轴：轨道半径 $r$ (m)；y轴：轨道速度 $v$ (m s⁻¹)

### Shape / 形状
**English:** A decreasing curve. $v \propto \frac{1}{\sqrt{r}}$, so the graph is a smooth, decreasing curve that approaches zero as $r \to \infty$ and approaches infinity as $r \to 0$ (though physically limited by the size of the central body).
**中文：** 一条递减曲线。$v \propto \frac{1}{\sqrt{r}}$，所以图形是一条平滑的递减曲线，当 $r \to \infty$ 时趋近于零，当 $r \to 0$ 时趋近于无穷大（尽管物理上受中心天体大小的限制）。

### Gradient Meaning / 斜率含义
**English:** The gradient $\frac{dv}{dr} = -\frac{1}{2} \sqrt{\frac{GM}{r^3}} = -\frac{v}{2r}$. It is always negative, showing that speed decreases as radius increases. The magnitude of the gradient decreases as $r$ increases.
**中文：** 斜率 $\frac{dv}{dr} = -\frac{1}{2} \sqrt{\frac{GM}{r^3}} = -\frac{v}{2r}$。它始终为负，表明速度随半径增加而减小。斜率的幅度随 $r$ 增加而减小。

### Area Meaning / 面积含义
**English:** The area under the $v$ vs $r$ graph has no direct physical meaning in this context.
**中文：** 在此上下文中，$v$ 对 $r$ 图形下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** You may be asked to sketch this graph or to use it to compare orbital speeds at different radii. A common question is to calculate the speed at a given radius or to find the radius for a given speed.
**中文：** 你可能会被要求画出这个图形，或者用它来比较不同半径下的轨道速度。一个常见的问题是计算给定半径下的速度，或者找到给定速度下的半径。

### Common Questions / 常见问题
**English:**
- "Sketch a graph showing how orbital speed varies with orbital radius for satellites around Earth."
- "Use the graph to determine the orbital radius of a satellite with speed $v$."
**中文：**
- "画图显示绕地球卫星的轨道速度如何随轨道半径变化。"
- "使用图形确定速度为 $v$ 的卫星的轨道半径。"

---

## 6.2 Orbital Period vs Orbital Radius / 轨道周期与轨道半径

### Axes / 坐标轴
**English:** x-axis: Orbital radius $r$ (m); y-axis: Orbital period $T$ (s)
**中文：** x轴：轨道半径 $r$ (m)；y轴：轨道周期 $T$ (s)

### Shape / 形状
**English:** An increasing curve. $T \propto r^{3/2}$, so the graph is a smooth, increasing curve that starts at zero (for $r=0$) and increases without bound as $r$ increases.
**中文：** 一条递增曲线。$T \propto r^{3/2}$，所以图形是一条平滑的递增曲线，从零开始（对于 $r=0$），并随着 $r$ 的增加而无界增加。

### Gradient Meaning / 斜率含义
**English:** The gradient $\frac{dT}{dr} = \frac{3\pi}{\sqrt{GM}} \sqrt{r} = \frac{3T}{2r}$. It is always positive and increases with $r$.
**中文：** 斜率 $\frac{dT}{dr} = \frac{3\pi}{\sqrt{GM}} \sqrt{r} = \frac{3T}{2r}$。它始终为正，并随 $r$ 增加而增加。

### Area Meaning / 面积含义
**English:** The area under the $T$ vs $r$ graph has no direct physical meaning.
**中文：** $T$ 对 $r$ 图形下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** A more useful graph is $T^2$ vs $r^3$, which should be a straight line through the origin with gradient $\frac{4\pi^2}{GM}$. This is a common way to verify Kepler's Third Law experimentally.
**中文：** 更有用的图形是 $T^2$ 对 $r^3$，它应该是一条通过原点的直线，斜率为 $\frac{4\pi^2}{GM}$。这是实验验证开普勒第三定律的常用方法。

### Common Questions / 常见问题
**English:**
- "Plot a graph of $T^2$ against $r^3$ and use it to determine the mass of the central body."
- "Explain why the graph of $T$ against $r$ is not a straight line."
**中文：**
- "绘制 $T^2$ 对 $r^3$ 的图形，并用它来确定中心天体的质量。"
- "解释为什么 $T$ 对 $r$ 的图形不是一条直线。"

---

## 6.3 $T^2$ vs $r^3$ (Kepler's Third Law Verification) / $T^2$ 对 $r^3$（开普勒第三定律验证）

### Axes / 坐标轴
**English:** x-axis: $r^3$ (m³); y-axis: $T^2$ (s²)
**中文：** x轴：$r^3$ (m³)；y轴：$T^2$ (s²)

### Shape / 形状
**English:** A straight line through the origin. This is because $T^2 = \frac{4\pi^2}{GM} r^3$, which is of the form $y = mx$ where $m = \frac{4\pi^2}{GM}$.
**中文：** 一条通过原点的直线。这是因为 $T^2 = \frac{4\pi^2}{GM} r^3$，形式为 $y = mx$，其中 $m = \frac{4\pi^2}{GM}$。

### Gradient Meaning / 斜率含义
**English:** The gradient $m = \frac{4\pi^2}{GM}$. From this, the mass of the central body can be calculated: $M = \frac{4\pi^2}{Gm}$.
**中文：** 斜率 $m = \frac{4\pi^2}{GM}$。由此可以计算中心天体的质量：$M = \frac{4\pi^2}{Gm}$。

### Area Meaning / 面积含义
**English:** The area under the $T^2$ vs $r^3$ graph has no direct physical meaning.
**中文：** $T^2$ 对 $r^3$ 图形下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:** This is a very common exam graph. You may be asked to plot data, calculate the gradient, and use it to find the mass of a planet or star. The straight line confirms Kepler's Third Law.
**中文：** 这是一个非常常见的考试图形。你可能会被要求绘制数据、计算斜率，并用它来求行星或恒星的质量。直线证实了开普勒第三定律。

### Common Questions / 常见问题
**English:**
- "Use the gradient of the $T^2$ vs $r^3$ graph to determine the mass of Jupiter."
- "Explain why the line passes through the origin."
**中文：**
- "使用 $T^2$ 对 $r^3$ 图形的斜率来确定木星的质量。"
- "解释为什么直线通过原点。"

---

# 7. Required Diagrams / 必备图表

## 7.1 Forces in a Circular Orbit / 圆形轨道中的力

### Description / 描述
**English:**
A diagram showing a satellite of mass $m$ in a circular orbit of radius $r$ around a central body of mass $M$. The diagram should show:
- The satellite at a point on the circular path.
- The gravitational force vector $F_g$ pointing radially inward towards the centre of the central body.
- The centripetal force vector $F_c$ (same direction as $F_g$).
- The velocity vector $v$ tangential to the circular path.
- The orbital radius $r$ from the centre of the central body to the satellite.

**中文：**
一个显示质量为 $m$ 的卫星在半径为 $r$ 的圆形轨道上绕质量为 $M$ 的中心天体运行的图。该图应显示：
- 卫星在圆形路径上的一点。
- 引力矢量 $F_g$ 径向向内指向中心天体的中心。
- 向心力矢量 $F_c$（与 $F_g$ 方向相同）。
- 速度矢量 $v$ 与圆形路径相切。
- 从中心天体中心到卫星的轨道半径 $r$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-01: Forces in a Circular Orbit**
>
> A clean, educational 2D diagram showing a large blue sphere (Earth) at the centre. A small grey satellite is shown on a dashed circular orbit path around the Earth. From the satellite, three arrows originate: a red arrow labelled "F_g = F_c" pointing straight down towards the Earth's centre, and a green arrow labelled "v" pointing tangentially to the orbit (to the right). A dashed line from the Earth's centre to the satellite is labelled "r". The background is dark with a few stars. Style: textbook diagram, vector graphics, clear labels, no perspective distortion. Labels in English.

### Labels Required / 需要标注
**English:**
- Central body (Earth)
- Satellite
- Orbital path (dashed circle)
- $r$ (orbital radius)
- $F_g = F_c$ (gravitational/centripetal force)
- $v$ (orbital velocity)

**中文：**
- 中心天体（地球）
- 卫星
- 轨道路径（虚线圆）
- $r$（轨道半径）
- $F_g = F_c$（引力/向心力）
- $v$（轨道速度）

### Exam Importance / 考试重要性
**English:**
This diagram is essential for understanding the force balance in circular orbits. Examiners often ask students to draw or label this diagram to show their understanding of the principle that gravitational force provides the centripetal force.

**中文：**
这个图对于理解圆形轨道中的力平衡至关重要。考官经常要求学生绘制或标注此图，以展示他们对引力提供向心力这一原理的理解。

---

## 7.2 Geostationary Orbit / 地球静止轨道

### Description / 描述
**English:**
A diagram showing the Earth with a geostationary satellite in orbit above the equator. The diagram should show:
- The Earth with its axis of rotation.
- The equator.
- A satellite in a circular orbit directly above the equator.
- The orbital radius $r$ (approximately 42,300 km from Earth's centre).
- The satellite's position relative to a fixed point on the Earth's surface.
- The direction of the satellite's motion (west to east, same as Earth's rotation).

**中文：**
一个显示地球和赤道上空轨道中地球静止卫星的图。该图应显示：
- 地球及其自转轴。
- 赤道。
- 一颗卫星在赤道正上方的圆形轨道中。
- 轨道半径 $r$（距地球中心约42,300公里）。
- 卫星相对于地球表面某固定点的位置。
- 卫星运动方向（自西向东，与地球自转相同）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-02: Geostationary Orbit**
>
> A 3D-style educational diagram showing the Earth from a slight angle, with the equator clearly marked as a red dashed line. A single satellite is shown in a circular orbit (white dashed line) directly above the equator. A curved arrow around the Earth's axis shows the direction of Earth's rotation (counterclockwise when viewed from above the North Pole). A matching curved arrow on the satellite's orbit shows it moving in the same direction. A label points to the satellite: "Geostationary Satellite (T = 24 h)". Another label shows the orbital radius: "r ≈ 42,300 km". The Earth is blue and green, space is dark. Style: realistic but schematic, clear labels, educational tone.

### Labels Required / 需要标注
**English:**
- Earth
- Equator
- Geostationary satellite
- Orbital path (circular, above equator)
- $r \approx 4.23 \times 10^7$ m (orbital radius)
- Direction of Earth's rotation
- Direction of satellite's motion
- Fixed point on Earth's surface

**中文：**
- 地球
- 赤道
- 地球静止卫星
- 轨道路径（圆形，赤道上方）
- $r \approx 4.23 \times 10^7$ m（轨道半径）
- 地球自转方向
- 卫星运动方向
- 地球表面固定点

### Exam Importance / 考试重要性
**English:**
This diagram is frequently used in exam questions about geostationary satellites. Students must be able to explain why the orbit must be equatorial and circular, and why the period must be 24 hours.

**中文：**
这个图经常用于关于地球静止卫星的考试问题中。学生必须能够解释为什么轨道必须是赤道平面内且为圆形，以及为什么周期必须是24小时。

---

## 7.3 Kepler's Third Law Graph / 开普勒第三定律图形

### Description / 描述
**English:**
A graph of $T^2$ (y-axis) against $r^3$ (x-axis) for planets orbiting the Sun or moons orbiting a planet. The graph should show:
- A straight line passing through the origin.
- Data points for several planets/moons.
- The gradient of the line labelled as $m = \frac{4\pi^2}{GM}$.
- Axes labelled with units.

**中文：**
绕太阳运行的行星或绕行星运行的卫星的 $T^2$（y轴）对 $r^3$（x轴）的图形。该图应显示：
- 一条通过原点的直线。
- 几个行星/卫星的数据点。
- 直线的斜率标注为 $m = \frac{4\pi^2}{GM}$。
- 带有单位的坐标轴标签。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-03: Kepler's Third Law Graph**
>
> A clean, textbook-style graph with a white background and gridlines. The x-axis is labelled "r^3 / (10^24 m^3)" and the y-axis is labelled "T^2 / (10^12 s^2)". Five data points are plotted (Mercury, Venus, Earth, Mars, Jupiter) with small circles. A best-fit straight line passes through the origin and all points. The gradient is calculated and displayed: "Gradient = 2.97 × 10^-19 s^2 m^-3". A note reads: "From gradient, M_sun = 1.99 × 10^30 kg". Style: scientific graph, clear, professional, suitable for an exam paper.

### Labels Required / 需要标注
**English:**
- $r^3$ / m³ (x-axis)
- $T^2$ / s² (y-axis)
- Data points (e.g., Mercury, Venus, Earth, Mars, Jupiter)
- Best-fit straight line through origin
- Gradient $m = \frac{4\pi^2}{GM}$

**中文：**
- $r^3$ / m³ (x轴)
- $T^2$ / s² (y轴)
- 数据点（例如，水星、金星、地球、火星、木星）
- 通过原点的最佳拟合直线
- 斜率 $m = \frac{4\pi^2}{GM}$

### Exam Importance / 考试重要性
**English:**
This graph is a common way to test understanding of Kepler's Third Law. Students may be asked to plot data, calculate the gradient, and use it to find the mass of the central body. It also tests practical skills like drawing best-fit lines and calculating gradients.

**中文：**
这个图形是测试对开普勒第三定律理解的常用方法。学生可能会被要求绘制数据、计算斜率，并用它来求中心天体的质量。它也测试实践技能，如绘制最佳拟合线和计算斜率。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Orbital Speed and Period / 示例1：计算轨道速度和周期

### Question / 题目
**English:**
A weather satellite is placed in a circular orbit 300 km above the Earth's surface. Given that the mass of the Earth is $5.97 \times 10^{24}$ kg and the radius of the Earth is $6.37 \times 10^6$ m, calculate:
(a) The orbital speed of the satellite.
(b) The orbital period of the satellite in minutes.

**中文：**
一颗气象卫星被放置在地球表面上方300公里的圆形轨道中。已知地球质量为 $5.97 \times 10^{24}$ kg，地球半径为 $6.37 \times 10^6$ m，计算：
(a) 卫星的轨道速度。
(b) 卫星的轨道周期（以分钟为单位）。

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — EX01: Low Earth Orbit Satellite**
>
> A diagram showing a small satellite (with solar panels) in a circular orbit around the Earth. The Earth is shown as a blue sphere. A label indicates the altitude: "h = 300 km". Another label shows the orbital radius: "r = R_E + h = 6.67 × 10^6 m". The satellite is moving tangentially. Style: simple schematic, educational.

### Solution / 解答

**Step 1: Determine the orbital radius.**
**English:**
The orbital radius $r$ is the distance from the Earth's centre to the satellite:
$$r = R_E + h = 6.37 \times 10^6 + 300 \times 10^3 = 6.67 \times 10^6 \text{ m}$$

**中文：**
轨道半径 $r$ 是从地球中心到卫星的距离：
$$r = R_E + h = 6.37 \times 10^6 + 300 \times 10^3 = 6.67 \times 10^6 \text{ m}$$

**Step 2: Calculate the orbital speed.**
**English:**
Use the equation $v = \sqrt{\frac{GM}{r}}$:
$$v = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{6.67 \times 10^6}}$$

First, calculate the numerator:
$$GM = (6.67 \times 10^{-11})(5.97 \times 10^{24}) = 3.98 \times 10^{14} \text{ N m}^2 \text{ kg}^{-1}$$

Then:
$$v = \sqrt{\frac{3.98 \times 10^{14}}{6.67 \times 10^6}} = \sqrt{5.97 \times 10^7} = 7.73 \times 10^3 \text{ m s}^{-1}$$

**中文：**
使用方程 $v = \sqrt{\frac{GM}{r}}$：
$$v = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{6.67 \times 10^6}}$$

首先，计算分子：
$$GM = (6.67 \times 10^{-11})(5.97 \times 10^{24}) = 3.98 \times 10^{14} \text{ N m}^2 \text{ kg}^{-1}$$

然后：
$$v = \sqrt{\frac{3.98 \times 10^{14}}{6.67 \times 10^6}} = \sqrt{5.97 \times 10^7} = 7.73 \times 10^3 \text{ m s}^{-1}$$

**Step 3: Calculate the orbital period.**
**English:**
Use the equation $T = \frac{2\pi r}{v}$:
$$T = \frac{2\pi (6.67 \times 10^6)}{7.73 \times 10^3} = \frac{4.19 \times 10^7}{7.73 \times 10^3} = 5.42 \times 10^3 \text{ s}$$

Convert to minutes:
$$T = \frac{5.42 \times 10^3}{60} = 90.3 \text{ minutes}$$

**中文：**
使用方程 $T = \frac{2\pi r}{v}$：
$$T = \frac{2\pi (6.67 \times 10^6)}{7.73 \times 10^3} = \frac{4.19 \times 10^7}{7.73 \times 10^3} = 5.42 \times 10^3 \text{ s}$$

转换为分钟：
$$T = \frac{5.42 \times 10^3}{60} = 90.3 \text{ minutes}$$

### Final Answer / 最终答案
**Answer:**
(a) Orbital speed $v = 7.73 \times 10^3$ m s⁻¹ (or 7.73 km s⁻¹)
(b) Orbital period $T = 90.3$ minutes

**答案：**
(a) 轨道速度 $v = 7.73 \times 10^3$ m s⁻¹ (或 7.73 km s⁻¹)
(b) 轨道周期 $T = 90.3$ 分钟

### Examiner Notes / 考官点评
**English:**
- **Common mistake:** Using altitude (300 km) instead of orbital radius. Always add the Earth's radius.
- **Mark scheme:** 1 mark for correct $r$, 1 mark for correct substitution into $v = \sqrt{GM/r}$, 1 mark for correct $v$, 1 mark for correct $T$ in seconds, 1 mark for conversion to minutes.
- **Tip:** Remember that $G = 6.67 \times 10^{-11}$ N m² kg⁻² is a standard constant that should be memorised.

**中文：**
- **常见错误：** 使用高度（300公里）而不是轨道半径。始终加上地球半径。
- **评分方案：** 正确 $r$ 得1分，正确代入 $v = \sqrt{GM/r}$ 得1分，正确 $v$ 得1分，正确 $T$（以秒为单位）得1分，转换为分钟得1分。
- **提示：** 记住 $G = 6.67 \times 10^{-11}$ N m² kg⁻² 是一个应该记住的标准常数。

### Alternative Method / 替代方法
**English:**
For part (b), you could also use Kepler's Third Law directly:
$$T^2 = \frac{4\pi^2 r^3}{GM}$$
$$T = 2\pi \sqrt{\frac{r^3}{GM}} = 2\pi \sqrt{\frac{(6.67 \times 10^6)^3}{3.98 \times 10^{14}}} = 5.42 \times 10^3 \text{ s}$$

**中文：**
对于(b)部分，你也可以直接使用开普勒第三定律：
$$T^2 = \frac{4\pi^2 r^3}{GM}$$
$$T = 2\pi \sqrt{\frac{r^3}{GM}} = 2\pi \sqrt{\frac{(6.67 \times 10^6)^3}{3.98 \times 10^{14}}} = 5.42 \times 10^3 \text{ s}$$

---

## Example 2: Finding the Mass of a Planet / 示例2：求行星质量

### Question / 题目
**English:**
A moon of Jupiter, Io, orbits Jupiter in a nearly circular orbit with a period of 1.77 days and an orbital radius of $4.22 \times 10^8$ m. Calculate the mass of Jupiter.

**中文：**
木星的卫星Io以近圆形轨道绕木星运行，周期为1.77天，轨道半径为 $4.22 \times 10^8$ m。计算木星的质量。

### Solution / 解答

**Step 1: Convert the period to seconds.**
**English:**
$$T = 1.77 \text{ days} \times 24 \text{ hours/day} \times 3600 \text{ s/hour} = 1.53 \times 10^5 \text{ s}$$

**中文：**
$$T = 1.77 \text{ 天} \times 24 \text{ 小时/天} \times 3600 \text{ 秒/小时} = 1.53 \times 10^5 \text{ s}$$

**Step 2: Use Kepler's Third Law to find the mass.**
**English:**
From $T^2 = \frac{4\pi^2 r^3}{GM}$, rearrange for $M$:
$$M = \frac{4\pi^2 r^3}{G T^2}$$

Substitute values:
$$M = \frac{4\pi^2 (4.22 \times 10^8)^3}{(6.67 \times 10^{-11})(1.53 \times 10^5)^2}$$

First, calculate $r^3$:
$$r^3 = (4.22 \times 10^8)^3 = 7.51 \times 10^{25} \text{ m}^3$$

Then, calculate $T^2$:
$$T^2 = (1.53 \times 10^5)^2 = 2.34 \times 10^{10} \text{ s}^2$$

Now:
$$M = \frac{4\pi^2 (7.51 \times 10^{25})}{(6.67 \times 10^{-11})(2.34 \times 10^{10})}$$

Calculate numerator:
$$4\pi^2 (7.51 \times 10^{25}) = 39.48 \times 7.51 \times 10^{25} = 2.96 \times 10^{27}$$

Calculate denominator:
$$(6.67 \times 10^{-11})(2.34 \times 10^{10}) = 1.56 \times 10^0 = 1.56$$

Therefore:
$$M = \frac{2.96 \times 10^{27}}{1.56} = 1.90 \times 10^{27} \text{ kg}$$

**中文：**

**步骤1：将周期转换为秒。**
$$T = 1.77 \text{ 天} \times 24 \text{ 小时/天} \times 3600 \text{ 秒/小时} = 1.53 \times 10^5 \text{ s}$$

**步骤2：使用开普勒第三定律求质量。**
从 $T^2 = \frac{4\pi^2 r^3}{GM}$，重新排列求 $M$：
$$M = \frac{4\pi^2 r^3}{G T^2}$$

代入数值：
$$M = \frac{4\pi^2 (4.22 \times 10^8)^3}{(6.67 \times 10^{-11})(1.53 \times 10^5)^2}$$

首先，计算 $r^3$：
$$r^3 = (4.22 \times 10^8)^3 = 7.51 \times 10^{25} \text{ m}^3$$

然后，计算 $T^2$：
$$T^2 = (1.53 \times 10^5)^2 = 2.34 \times 10^{10} \text{ s}^2$$

现在：
$$M = \frac{4\pi^2 (7.51 \times 10^{25})}{(6.67 \times 10^{-11})(2.34 \times 10^{10})}$$

计算分子：
$$4\pi^2 (7.51 \times 10^{25}) = 39.48 \times 7.51 \times 10^{25} = 2.96 \times 10^{27}$$

计算分母：
$$(6.67 \times 10^{-11})(2.34 \times 10^{10}) = 1.56 \times 10^0 = 1.56$$

因此：
$$M = \frac{2.96 \times 10^{27}}{1.56} = 1.90 \times 10^{27} \text{ kg}$$

### Final Answer / 最终答案
**Answer:** Mass of Jupiter $M_J = 1.90 \times 10^{27}$ kg (accepted value is $1.90 \times 10^{27}$ kg)

**答案：** 木星质量 $M_J = 1.90 \times 10^{27}$ kg（公认值为 $1.90 \times 10^{27}$ kg）

### Examiner Notes / 考官点评
**English:**
- **Common mistake:** Forgetting to convert days to seconds. Using $T = 1.77$ s would give a completely wrong answer.
- **Mark scheme:** 1 mark for correct conversion, 1 mark for correct rearrangement, 1 mark for correct substitution, 1 mark for correct calculation.
- **Tip:** Always check your answer against known values. The mass of Jupiter is about 318 times the mass of Earth ($5.97 \times 10^{24}$ kg), so $1.90 \times 10^{27}$ kg is reasonable.

**中文：**
- **常见错误：** 忘记将天转换为秒。使用 $T = 1.77$ s 会得到完全错误的答案。
- **评分方案：** 正确转换得1分，正确重新排列得1分，正确代入得1分，正确计算得1分。
- **提示：** 始终对照已知值检查你的答案。木星质量大约是地球质量（$5.97 \times 10^{24}$ kg）的318倍，所以 $1.90 \times 10^{27}$ kg 是合理的。

---

# 9. Past Paper Question Types / 历年真题题型

**English:**
The following table summarises the types of questions that appear in Cambridge 9702 and Edexcel IAL exams for this topic. The frequency and difficulty ratings are based on analysis of past papers.

**中文：**
下表总结了剑桥9702和爱德思IAL考试中本主题出现的问题类型。频率和难度评级基于对历年试卷的分析。

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of orbital speed / 轨道速度计算 | High | Medium | 📝 *待填入* |
| Calculation of orbital period / 轨道周期计算 | High | Medium | 📝 *待填入* |
| Calculation of central body mass / 中心天体质量计算 | High | High | 📝 *待填入* |
| Derivation of $v = \sqrt{GM/r}$ / 推导 $v = \sqrt{GM/r}$ | Medium | Medium | 📝 *待填入* |
| Derivation of $T^2 = 4\pi^2 r^3 / GM$ / 推导 $T^2 = 4\pi^2 r^3 / GM$ | Medium | Medium | 📝 *待填入* |
| Explanation of geostationary orbit / 地球静止轨道解释 | High | Low | 📝 *待填入* |
| Graph analysis ($T^2$ vs $r^3$) / 图形分析 ($T^2$ 对 $r^3$) | Medium | High | 📝 *待填入* |
| Comparison of orbital parameters / 轨道参数比较 | Medium | Medium | 📝 *待填入* |
| Practical design (determining $M$ from orbital data) / 实验设计（从轨道数据确定 $M$） | Low | High | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词:**

| Command Word (EN) | Command Word (CN) | What to Do / 做什么 |
|-------------------|-------------------|---------------------|
| State | 陈述 | Give a brief answer without explanation. |
| Define | 定义 | Give the precise meaning of a term. |
| Explain | 解释 | Give reasons or causes for a phenomenon. |
| Describe | 描述 | Give a detailed account of a process or observation. |
| Calculate | 计算 | Use mathematical operations to find a numerical answer. |
| Determine | 确定 | Find a value using given data or a graph. |
| Suggest | 建议 | Use your knowledge to propose a plausible explanation or method. |
| Derive | 推导 | Show the steps to obtain an equation from first principles. |
| Sketch | 画图 | Draw a graph or diagram showing the general shape and key features. |
| Plot | 绘制 | Draw a graph using data points. |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This topic connects to practical skills in several ways, particularly in the context of determining the mass of a central body (e.g., Earth, Jupiter, the Sun) from orbital data.

**Measurements / 测量:**
- **Orbital radius $r$:** This can be determined using parallax methods (for nearby objects) or by using Kepler's Third Law in reverse (if the mass is known). In a school lab, this is often given data.
- **Orbital period $T$:** Measured using timing methods. For moons of Jupiter, this can be done by observing the moon's position over several nights. For Earth satellites, it can be calculated from the time between successive passes over a fixed point.
- **Uncertainties / 不确定度:** When measuring $T$, the uncertainty is typically ±0.5 s for a single period, but can be reduced by measuring multiple periods. The uncertainty in $r$ is often the largest source of error.

**Graph Plotting / 图表绘制:**
- Plotting $T^2$ against $r^3$ is a key practical skill. The graph should be a straight line through the origin.
- **Best-fit line:** Draw a straight line that passes through as many points as possible, with equal numbers of points above and below the line. The line must pass through the origin (0,0).
- **Gradient calculation:** Choose two points far apart on the best-fit line (not data points) to calculate the gradient. Use $\text{gradient} = \frac{\Delta y}{\Delta x}$.
- **Determining mass:** From the gradient $m = \frac{4\pi^2}{GM}$, calculate $M = \frac{4\pi^2}{Gm}$.

**Experimental Design / 实验设计:**
- **CAIE Paper 5 / Edexcel Unit 6:** You may be asked to design an experiment to determine the mass of a planet or star. This would involve:
  1. Observing the orbit of a moon or planet over time.
  2. Measuring the orbital radius (using angular measurements and distance).
  3. Measuring the orbital period.
  4. Plotting $T^2$ against $r^3$.
  5. Calculating the gradient and hence the mass.
- **Error analysis:** Identify sources of error (e.g., non-circular orbits, timing errors, distance measurement errors) and suggest improvements (e.g., use longer observation times, use more precise instruments).

**中文：**
本主题以多种方式与实践技能相关联，特别是在从轨道数据确定中心天体（例如，地球、木星、太阳）质量的背景下。

**测量：**
- **轨道半径 $r$：** 可以使用视差法（对于近处物体）或反向使用开普勒第三定律（如果已知质量）来确定。在学校实验室中，这通常是给出的数据。
- **轨道周期 $T$：** 使用计时方法测量。对于木星的卫星，可以通过连续几个晚上观察卫星的位置来完成。对于地球卫星，可以根据连续经过固定点之间的时间来计算。
- **不确定度：** 测量 $T$ 时，单个周期的不确定度通常为 ±0.5 秒，但可以通过测量多个周期来减少。$r$ 的不确定度通常是最大的误差来源。

**图表绘制：**
- 绘制 $T^2$ 对 $r^3$ 的图形是一项关键的实践技能。图形应该是一条通过原点的直线。
- **最佳拟合线：** 绘制一条尽可能多地穿过点的直线，线上方和下方的点数量相等。该线必须通过原点 (0,0)。
- **斜率计算：** 在最佳拟合线上选择两个相距较远的点（不是数据点）来计算斜率。使用 $\text{斜率} = \frac{\Delta y}{\Delta x}$。
- **确定质量：** 从斜率 $m = \frac{4\pi^2}{GM}$，计算 $M = \frac{4\pi^2}{Gm}$。

**实验设计：**
- **CAIE Paper 5 / Edexcel Unit 6：** 你可能会被要求设计一个实验来确定行星或恒星的质量。这将包括：
  1. 随时间观察卫星或行星的轨道。
  2. 测量轨道半径（使用角度测量和距离）。
  3. 测量轨道周期。
  4. 绘制 $T^2$ 对 $r^3$ 的图形。
  5. 计算斜率，从而计算质量。
- **误差分析：** 识别误差来源（例如，非圆形轨道、计时误差、距离测量误差）并提出改进建议（例如，使用更长的观察时间，使用更精密的仪器）。

> 📋 **CIE Only:** CAIE Paper 5 often includes questions on designing experiments to determine astronomical quantities. Students should be familiar with the use of telescopes, CCD cameras, and timing methods.
>
> 📋 **Edexcel Only:** Edexcel Unit 6 may include a practical investigation where students analyse given orbital data to determine the mass of a central body. Graph plotting and gradient calculation are key skills.

---

# 11. Concept Map / 概念图谱

**English:**
The following Mermaid diagram shows the connections between this topic (Circular Orbits), its prerequisites, related topics, and sub-topics.

**中文：**
以下Mermaid图显示了本主题（圆形轨道）、其先决条件、相关主题和子主题之间的联系。

```mermaid
graph TD
    %% Central Topic
    CO[Circular Orbits / 圆形轨道]
    
    %% Prerequisites (from other modules)
    GF[Gravitational Force and Field / 引力与场]
    CA[Centripetal Acceleration and Force / 向心加速度与力]
    N2[Newton's Second Law / 牛顿第二定律]
    UCM[Uniform Circular Motion / 匀速圆周运动]
    
    %% Sub-topics (leaf nodes)
    OV[Orbital Velocity / 轨道速度]
    K3[Kepler's Third Law / 开普勒第三定律]
    GS[Geostationary Satellites / 地球静止卫星]
    
    %% Related Topics
    GP[Gravitational Potential / 引力势]
    ESO[Energy in Stable Orbits / 稳定轨道中的能量]
    SS[Solar System Dynamics / 太阳系动力学]
    
    %% Connections
    GF -->|Provides centripetal force| CO
    CA -->|Required for circular motion| CO
    N2 -->|F = ma| CA
    UCM -->|v = 2πr/T| CA
    
    CO -->|Derives| OV
    CO -->|Derives| K3
    CO -->|Special case| GS
    
    CO -->|Related to| GP
    CO -->|Related to| ESO
    K3 -->|Applies to| SS
    
    OV -->|v = sqrt(GM/r)| K3
    GS -->|Uses| K3
    
    %% Styling
    classDef topic fill:#f9f,stroke:#333,stroke-width:2px;
    classDef sub fill:#bbf,stroke:#333,stroke-width:1px;
    classDef pre fill:#bfb,stroke:#333,stroke-width:1px;
    classDef rel fill:#fbb,stroke:#333,stroke-width:1px;
    
    class CO topic;
    class OV,K3,GS sub;
    class GF,CA,N2,UCM pre;
    class GP,ESO,SS rel;
```

---

# 12. Quick Revision Sheet / 速查表

**English:**
This one-page summary provides all the key information for Circular Orbits in a compact format.

**中文：**
此一页摘要以紧凑格式提供了圆形轨道的所有关键信息。

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | **Circular Orbit:** Path where gravitational force provides centripetal force. <br> **Orbital Speed:** $v = \sqrt{GM/r}$, independent of satellite mass. <br> **Orbital Period:** $T = 2\pi r/v = 2\pi \sqrt{r^3/GM}$. <br> **Geostationary:** $T = 24$ h, equatorial, circular, west-to-east. |
| **Equations / 公式** | $F_g = \frac{GMm}{r^2}$ (Gravitational force) <br> $F_c = \frac{mv^2}{r}$ (Centripetal force) <br> $F_g = F_c$ (Key principle) <br> $v = \sqrt{\frac{GM}{r}}$ (Orbital speed) <br> $T^2 = \frac{4\pi^2 r^3}{GM}$ (Kepler's Third Law) <br> $M = \frac{4\pi^2 r^3}{G T^2}$ (Mass of central body) |
| **Graphs / 图表** | **$v$ vs $r$:** Decreasing curve, $v \propto 1/\sqrt{r}$. <br> **$T$ vs $r$:** Increasing curve, $T \propto r^{3/2}$. <br> **$T^2$ vs $r^3$:** Straight line through origin, gradient $= 4\pi^2/GM$. |
| **Key Facts / 关键事实** | 1. Orbital speed decreases as radius increases. <br> 2. Orbital period increases as radius increases. <br> 3. Mass of satellite does NOT affect orbit (cancels out). <br> 4. Geostationary orbit radius $\approx 4.23 \times 10^7$ m (altitude $\approx 3.58 \times 10^7$ m). <br> 5. Low Earth orbit period $\approx 90$ minutes. |
| **Exam Reminders / 考试提醒** | 1. Always start with $F_g = F_c$. <br> 2. Convert all units to SI (period to seconds, radius to metres). <br> 3. $r$ is from centre of central body, not surface. <br> 4. Memorise $G = 6.67 \times 10^{-11}$ N m² kg⁻². <br> 5. For geostationary: 3 conditions (period, equatorial, direction). <br> 6. Graph of $T^2$ vs $r^3$: line through origin. <br> 7. Mass of central body from gradient: $M = 4\pi^2/(G \times \text{gradient})$. |