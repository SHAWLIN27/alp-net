# Orbital Velocity / 轨道速度

---

# 1. Overview / 概述

**English:**
Orbital velocity is the minimum speed required for a satellite or celestial body to maintain a stable circular orbit around a larger central mass. This sub-topic explores the derivation and application of the orbital velocity formula, linking [[Gravitational Force and Field]] with [[Centripetal Acceleration and Force]]. Understanding orbital velocity is essential for explaining satellite motion, planetary orbits, and the design of [[Geostationary Satellites]]. It also connects directly to [[Kepler's Third Law]] through the relationship between orbital radius and period.

**中文:**
轨道速度是卫星或天体围绕更大中心质量维持稳定圆形轨道所需的最小速度。本子知识点探讨轨道速度公式的推导和应用，将[[Gravitational Force and Field]]与[[Centripetal Acceleration and Force]]联系起来。理解轨道速度对于解释卫星运动、行星轨道以及[[Geostationary Satellites]]的设计至关重要。它还通过轨道半径与周期之间的关系直接连接到[[Kepler's Third Law]]。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Orbital Velocity** / 轨道速度 | The constant tangential speed required for an object to maintain a stable circular orbit around a larger central mass, where the gravitational force provides the necessary centripetal force. | 物体围绕较大中心质量维持稳定圆形轨道所需的恒定切向速度，此时引力提供必要的向心力。 |
| **Tangential Velocity** / 切向速度 | The instantaneous velocity of an orbiting object perpendicular to the radius vector from the center of mass. | 轨道物体垂直于中心质量半径矢量的瞬时速度。 |
| **Gravitational Force** / 引力 | The attractive force between two masses, given by Newton's law of universal gravitation. | 两个质量之间的吸引力，由牛顿万有引力定律给出。 |
| **Centripetal Force** / 向心力 | The net force directed toward the center of a circular path, required for circular motion. | 指向圆形路径中心的净力，是圆周运动所必需的。 |
| **Orbital Radius** / 轨道半径 | The distance from the center of the central mass to the orbiting object. | 从中心质量中心到轨道物体的距离。 |

---

# 3. Key Concepts / 关键概念

**English:**

### Derivation of Orbital Velocity

The key insight is that for a stable circular orbit, the **gravitational force** must exactly equal the **centripetal force** required to keep the satellite moving in a circle:

$$ F_{\text{grav}} = F_{\text{centripetal}} $$

$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

Where:
- $G$ = universal gravitational constant
- $M$ = mass of central body (e.g., Earth)
- $m$ = mass of orbiting satellite (cancels out!)
- $r$ = orbital radius (distance from center of central mass)
- $v$ = orbital velocity

Cancelling $m$ and simplifying:

$$ v = \sqrt{\frac{GM}{r}} $$

### Key Observations

1. **Mass independence**: The orbital velocity does NOT depend on the mass of the satellite ($m$ cancels out). This is why a heavy satellite and a light satellite at the same orbital radius have the same speed.

2. **Inverse square root relationship**: As orbital radius $r$ increases, orbital velocity $v$ decreases. Satellites closer to Earth move faster than those farther away.

3. **Direction**: The velocity is always tangential to the orbit, perpendicular to the gravitational force.

### Common Pitfalls

- **Confusing orbital radius with altitude**: Remember $r = R_{\text{Earth}} + h$, where $h$ is altitude above Earth's surface.
- **Forgetting units**: $G$ is $6.67 \times 10^{-11} \text{ N·m}^2/\text{kg}^2$, so all quantities must be in SI units.
- **Assuming orbital velocity is constant for all orbits**: It varies with $r$ — lower orbits require higher speeds.

**中文:**

### 轨道速度的推导

关键洞察是：对于稳定的圆形轨道，**引力**必须恰好等于保持卫星做圆周运动所需的**向心力**：

$$ F_{\text{grav}} = F_{\text{centripetal}} $$

$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

其中：
- $G$ = 万有引力常数
- $M$ = 中心天体质量（如地球）
- $m$ = 轨道卫星质量（会消去！）
- $r$ = 轨道半径（距中心天体中心的距离）
- $v$ = 轨道速度

消去 $m$ 并简化：

$$ v = \sqrt{\frac{GM}{r}} $$

### 关键观察

1. **质量无关性**：轨道速度不依赖于卫星的质量（$m$ 消去）。这就是为什么在同一轨道半径上，重卫星和轻卫星具有相同的速度。

2. **反平方根关系**：随着轨道半径 $r$ 增加，轨道速度 $v$ 减小。靠近地球的卫星比远离的卫星运动得更快。

3. **方向**：速度始终与轨道相切，垂直于引力方向。

### 常见错误

- **混淆轨道半径与高度**：记住 $r = R_{\text{地球}} + h$，其中 $h$ 是地球表面以上的高度。
- **忘记单位**：$G$ 是 $6.67 \times 10^{-11} \text{ N·m}^2/\text{kg}^2$，因此所有量必须使用SI单位。
- **假设所有轨道的轨道速度恒定**：它随 $r$ 变化——较低的轨道需要更高的速度。

---

# 4. Formulas / 公式

## Primary Formula / 主要公式

$$ v = \sqrt{\frac{GM}{r}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $v$ | Orbital velocity | 轨道速度 | m/s |
| $G$ | Universal gravitational constant | 万有引力常数 | N·m²/kg² |
| $M$ | Mass of central body | 中心天体质量 | kg |
| $r$ | Orbital radius (center to center) | 轨道半径（中心到中心） | m |

## Alternative Forms / 其他形式

Using the relationship between orbital radius and period ($T$):

$$ v = \frac{2\pi r}{T} $$

Combining with the primary formula gives [[Kepler's Third Law]]:

$$ T^2 = \frac{4\pi^2 r^3}{GM} $$

## Derivation / 推导

**Step 1:** Write Newton's law of gravitation:
$$ F_{\text{grav}} = \frac{GMm}{r^2} $$

**Step 2:** Write centripetal force for circular motion:
$$ F_{\text{centripetal}} = \frac{mv^2}{r} $$

**Step 3:** Set them equal for stable orbit:
$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

**Step 4:** Cancel $m$ and rearrange:
$$ \frac{GM}{r} = v^2 $$

**Step 5:** Take square root:
$$ v = \sqrt{\frac{GM}{r}} $$

## Conditions / 适用条件

- **Circular orbit only**: This formula applies to circular orbits, not elliptical ones.
- **Central mass much larger**: $M \gg m$ (the central mass is much larger than the orbiting mass).
- **No other forces**: Assumes only gravitational force acts (no atmospheric drag, no other gravitational influences).
- **Newtonian gravity**: Valid for non-relativistic speeds ($v \ll c$).

> 📷 **IMAGE PROMPT — OV01: Orbital Velocity Derivation Diagram**
>
> **English Prompt:**
> A clean textbook-style vector diagram showing a satellite in circular orbit around Earth. The diagram should include:
> - Earth as a blue sphere at center, labeled "Earth (Mass M)"
> - A satellite as a small grey sphere at distance r from Earth's center, labeled "Satellite (Mass m)"
> - A dashed circular orbit path
> - Two arrows from the satellite: one red arrow pointing toward Earth's center labeled "Gravitational Force F_grav = GMm/r²" and one blue arrow tangential to the orbit labeled "Orbital Velocity v"
> - A radial line from Earth's center to the satellite labeled "Orbital Radius r"
> - A small curved arrow showing direction of motion
> - Clean white background, professional physics textbook style
>
> **中文描述:**
> 一个干净的教科书风格矢量图，显示卫星绕地球的圆形轨道。图中应包括：
> - 地球作为蓝色球体在中心，标注"地球（质量M）"
> - 卫星作为灰色小球体，距离地球中心r，标注"卫星（质量m）"
> - 虚线圆形轨道路径
> - 从卫星出发的两个箭头：一个红色箭头指向地球中心，标注"引力 F_grav = GMm/r²"；一个蓝色箭头与轨道相切，标注"轨道速度 v"
> - 从地球中心到卫星的径向线，标注"轨道半径 r"
> - 显示运动方向的小弧形箭头
> - 干净的白色背景，专业物理教科书风格
>
> **Labels Required / 需要标注:**
> * Earth (Mass M) / 地球（质量M）
> * Satellite (Mass m) / 卫星（质量m）
> * Orbital Radius r / 轨道半径 r
> * Gravitational Force F_grav / 引力 F_grav
> * Orbital Velocity v / 轨道速度 v
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding the force balance in orbital motion. Exam questions often ask students to draw and label this diagram, or to derive the orbital velocity formula from it.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — OV02: Orbital Velocity vs Radius Graph**
>
> **English Prompt:**
> A graph showing orbital velocity v (y-axis) vs orbital radius r (x-axis) for satellites around Earth. The curve should show a steep decrease at small r (near Earth's surface) and flatten out at large r. Key points marked:
> - Low Earth Orbit (LEO) at r ≈ 6600 km (altitude 200 km) with v ≈ 7800 m/s
> - Geostationary orbit at r ≈ 42,000 km with v ≈ 3070 m/s
> - The curve follows v ∝ 1/√r
> - Axes labeled with units
> - Professional graph style with gridlines
>
> **中文描述:**
> 显示绕地球卫星的轨道速度v（y轴）与轨道半径r（x轴）关系的图表。曲线应在小r（靠近地球表面）处急剧下降，在大r处趋于平缓。标记关键点：
> - 近地轨道（LEO）在r ≈ 6600 km（高度200 km）处，v ≈ 7800 m/s
> - 地球静止轨道在r ≈ 42,000 km处，v ≈ 3070 m/s
> - 曲线遵循 v ∝ 1/√r
> - 坐标轴标注单位
> - 带网格线的专业图表风格
>
> **Labels Required / 需要标注:**
> * Low Earth Orbit (LEO) / 近地轨道
> * Geostationary Orbit / 地球静止轨道
> * v ∝ 1/√r
>
> **Style / 风格:** Professional graph / 专业图表
>
> **Exam Relevance / 考试关联:**
> Understanding the inverse relationship between orbital velocity and radius is crucial for exam questions comparing different satellite orbits.

---

# 6. Worked Example / 典型例题

### Example 1: Low Earth Orbit Satellite

### Question / 题目
**English:**
A satellite is placed in a circular orbit 300 km above the Earth's surface. Given:
- Earth's mass $M_E = 5.97 \times 10^{24} \text{ kg}$
- Earth's radius $R_E = 6.37 \times 10^6 \text{ m}$
- $G = 6.67 \times 10^{-11} \text{ N·m}^2/\text{kg}^2$

Calculate the orbital velocity of the satellite.

**中文:**
一颗卫星被放置在距地球表面300 km的圆形轨道上。已知：
- 地球质量 $M_E = 5.97 \times 10^{24} \text{ kg}$
- 地球半径 $R_E = 6.37 \times 10^6 \text{ m}$
- $G = 6.67 \times 10^{-11} \text{ N·m}^2/\text{kg}^2$

计算卫星的轨道速度。

### Solution / 解答

**Step 1:** Calculate orbital radius $r$
$$ r = R_E + h = 6.37 \times 10^6 + 300 \times 10^3 = 6.67 \times 10^6 \text{ m} $$

**Step 2:** Apply orbital velocity formula
$$ v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{6.67 \times 10^6}} $$

**Step 3:** Simplify
$$ v = \sqrt{\frac{3.98 \times 10^{14}}{6.67 \times 10^6}} = \sqrt{5.97 \times 10^7} $$

**Step 4:** Calculate
$$ v = 7.73 \times 10^3 \text{ m/s} = 7730 \text{ m/s} $$

### Final Answer / 最终答案
**Answer:** $v = 7.73 \times 10^3 \text{ m/s}$ (approximately 7.73 km/s)
**答案:** $v = 7.73 \times 10^3 \text{ m/s}$（约7.73 km/s）

### Quick Tip / 提示
Always convert altitude to orbital radius by adding Earth's radius. A common mistake is using altitude directly as $r$ in the formula.

---

### Example 2: Comparing Orbital Velocities

### Question / 题目
**English:**
Two satellites orbit Earth. Satellite A is at an orbital radius of $7.0 \times 10^6 \text{ m}$, and Satellite B is at an orbital radius of $4.2 \times 10^7 \text{ m}$. Calculate the ratio of their orbital velocities $v_A : v_B$.

**中文:**
两颗卫星绕地球运行。卫星A的轨道半径为 $7.0 \times 10^6 \text{ m}$，卫星B的轨道半径为 $4.2 \times 10^7 \text{ m}$。计算它们的轨道速度之比 $v_A : v_B$。

### Solution / 解答

**Step 1:** Write the ratio using the formula
$$ \frac{v_A}{v_B} = \frac{\sqrt{GM/r_A}}{\sqrt{GM/r_B}} = \sqrt{\frac{r_B}{r_A}} $$

**Step 2:** Substitute values
$$ \frac{v_A}{v_B} = \sqrt{\frac{4.2 \times 10^7}{7.0 \times 10^6}} = \sqrt{6.0} = 2.45 $$

**Step 3:** Express as ratio
$$ v_A : v_B = 2.45 : 1 $$

### Final Answer / 最终答案
**Answer:** $v_A : v_B = 2.45 : 1$ (Satellite A is about 2.45 times faster)
**答案:** $v_A : v_B = 2.45 : 1$（卫星A的速度大约是卫星B的2.45倍）

### Quick Tip / 提示
When comparing orbital velocities, the ratio depends only on the square root of the inverse ratio of radii. The mass of Earth cancels out, so you don't need $G$ or $M$ for ratio problems.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the formula for orbital velocity of a satellite in circular orbit?
Q (CN): 圆形轨道上卫星的轨道速度公式是什么？
A (EN): $v = \sqrt{\frac{GM}{r}}$, where $G$ is the gravitational constant, $M$ is the mass of the central body, and $r$ is the orbital radius.
A (CN): $v = \sqrt{\frac{GM}{r}}$，其中 $G$ 是万有引力常数，$M$ 是中心天体的质量，$r$ 是轨道半径。

**Flashcard 2:**
Q (EN): Does the orbital velocity depend on the mass of the satellite? Why?
Q (CN): 轨道速度是否依赖于卫星的质量？为什么？
A (EN): No. The satellite's mass cancels out when equating gravitational force and centripetal force, so orbital velocity depends only on the central mass and orbital radius.
A (CN): 不依赖。当引力等于向心力时，卫星的质量被消去，因此轨道速度只取决于中心天体的质量和轨道半径。

**Flashcard 3:**
Q (EN): How does orbital velocity change as orbital radius increases?
Q (CN): 随着轨道半径增加，轨道速度如何变化？
A (EN): Orbital velocity decreases as orbital radius increases, following $v \propto 1/\sqrt{r}$.
A (CN): 轨道速度随着轨道半径增加而减小，遵循 $v \propto 1/\sqrt{r}$。

**Flashcard 4:**
Q (EN): What is the difference between orbital radius and altitude?
Q (CN): 轨道半径和高度有什么区别？
A (EN): Orbital radius $r$ is measured from the center of the central mass, while altitude $h$ is measured from the surface. They are related by $r = R_{\text{central}} + h$.
A (CN): 轨道半径 $r$ 是从中心天体的中心测量的，而高度 $h$ 是从表面测量的。它们的关系是 $r = R_{\text{中心}} + h$。

**Flashcard 5:**
Q (EN): What condition must be satisfied for a stable circular orbit?
Q (CN): 稳定圆形轨道必须满足什么条件？
A (EN): The gravitational force must exactly equal the centripetal force required for circular motion: $\frac{GMm}{r^2} = \frac{mv^2}{r}$.
A (CN): 引力必须恰好等于圆周运动所需的向心力：$\frac{GMm}{r^2} = \frac{mv^2}{r}$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Orbital Velocity
  cn: 轨道速度
parent_topic: Circular Orbits
parent_hub: "[[Circular Orbits]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Kepler's Third Law]]"
  - "[[Geostationary Satellites]]"
  - "[[Gravitational Force and Field]]"
  - "[[Centripetal Acceleration and Force]]"
  - "[[Gravitational Potential]]"
language: bilingual_en_cn