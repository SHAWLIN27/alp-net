Here is the complete bilingual leaf node for **Geostationary Satellites**, designed as a standalone Obsidian note and knowledge graph entry.

---

# 1. Overview / 概述

**English:**
Geostationary satellites are a special and highly practical application of [[Circular Orbits]]. Unlike most satellites that move relative to the Earth's surface, a geostationary satellite appears to remain fixed above a specific point on the equator. This unique property makes them indispensable for modern communication, broadcasting, and weather monitoring. This sub-topic explores the precise conditions required for a satellite to achieve this "stationary" state, linking the concepts of [[Orbital Velocity]], [[Kepler's Third Law]], and the fundamental forces of [[Gravitational Force and Field]] and [[Centripetal Acceleration and Force]]. Understanding geostationary orbits is a classic A-Level exam topic, requiring you to combine multiple physics principles into a single, coherent calculation.

**中文:**
地球静止卫星是[[Circular Orbits]]中一种特殊且非常实用的应用。与大多数相对于地球表面移动的卫星不同，地球静止卫星看起来固定在地球赤道某一点的上方。这一独特特性使其在现代通信、广播和气象监测中不可或缺。本子知识点探讨了卫星达到这种“静止”状态所需的确切条件，将[[Orbital Velocity]]、[[Kepler's Third Law]]以及[[Gravitational Force and Field]]和[[Centripetal Acceleration and Force]]的基本概念联系起来。理解地球静止轨道是A-Level考试中的经典考点，要求你将多个物理原理结合到一个连贯的计算中。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Geostationary Satellite** / 地球静止卫星 | A satellite that orbits the Earth with a period of 24 hours, in the same direction as the Earth's rotation (eastward), directly above the equator, so that it appears stationary relative to a point on the Earth's surface. | 一颗绕地球运行周期为24小时、与地球自转方向相同（向东）、位于赤道正上方的卫星，因此它相对于地球表面上的某一点看起来是静止的。 |
| **Geosynchronous Orbit** / 地球同步轨道 | An orbit with a period of 24 hours. A satellite in this orbit will return to the same point in the sky each day, but may not be fixed over the equator. | 周期为24小时的轨道。处于该轨道的卫星每天会回到天空中的同一点，但不一定固定在赤道上方。 |
| **Orbital Radius** / 轨道半径 | The distance from the centre of the Earth to the satellite. For a geostationary satellite, this is a fixed value of approximately 42,300 km. | 从地心到卫星的距离。对于地球静止卫星，这是一个固定值，约为42,300公里。 |
| **Orbital Period ($T$)** / 轨道周期 | The time taken for a satellite to complete one full orbit. For a geostationary satellite, $T = 24 \text{ hours} = 86,400 \text{ s}$. | 卫星完成一次完整轨道运行所需的时间。对于地球静止卫星，$T = 24 \text{小时} = 86,400 \text{秒}$。 |

---

# 3. Key Concepts / 关键概念

**English:**
The key to understanding geostationary satellites is recognizing that they are a specific solution to the general problem of [[Circular Orbits]]. For any satellite, the gravitational force provides the necessary [[Centripetal Acceleration and Force]]. This gives us the equation:

$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

For a geostationary satellite, three conditions must be met simultaneously:

1.  **Period Condition:** The orbital period $T$ must equal the Earth's rotational period (24 hours). This is the "geosynchronous" condition.
2.  **Direction Condition:** The orbit must be in the same direction as the Earth's rotation (eastward).
3.  **Equatorial Condition:** The orbit must lie directly above the equator. This is because the centripetal force must point towards the centre of the Earth, and the satellite's orbit must be centred on the Earth's centre. Only an equatorial orbit allows the satellite to remain fixed over a single point.

If any of these conditions are not met, the satellite will appear to drift north-south or east-west in the sky. The fixed orbital radius is derived from the period condition using [[Kepler's Third Law]] ($T^2 \propto r^3$). This radius is approximately 42,300 km from the Earth's centre, which corresponds to an altitude of about 35,800 km above the Earth's surface.

**Common Pitfall:** Students often confuse "geostationary" with "geosynchronous". All geostationary orbits are geosynchronous, but not all geosynchronous orbits are geostationary. A geosynchronous satellite will return to the same point in the sky each day, but it will trace a figure-8 pattern if it is not equatorial.

**中文:**
理解地球静止卫星的关键在于认识到它们是[[Circular Orbits]]一般问题的一个特定解。对于任何卫星，万有引力提供了所需的[[Centripetal Acceleration and Force]]。这给出了方程：

$$ \frac{GMm}{r^2} = \frac{mv^2}{r} $$

对于地球静止卫星，必须同时满足三个条件：

1.  **周期条件：** 轨道周期 $T$ 必须等于地球的自转周期（24小时）。这就是“地球同步”条件。
2.  **方向条件：** 轨道必须与地球自转方向相同（向东）。
3.  **赤道条件：** 轨道必须位于赤道正上方。这是因为向心力必须指向地心，并且卫星的轨道必须以地心为中心。只有赤道轨道才能让卫星固定在某一点的上方。

如果这些条件中的任何一个不满足，卫星在天空中看起来就会南北或东西漂移。固定的轨道半径是利用[[Kepler's Third Law]]（$T^2 \propto r^3$）从周期条件推导出来的。这个半径距地心约42,300公里，对应地球表面上方约35,800公里的高度。

**常见错误：** 学生经常混淆“地球静止”和“地球同步”。所有地球静止轨道都是地球同步的，但并非所有地球同步轨道都是地球静止的。地球同步卫星每天会回到天空中的同一点，但如果它不是赤道轨道，它会画出一个“8”字形图案。

> 📷 **IMAGE PROMPT — GEO-01: Geostationary vs. Geosynchronous Orbits**
>
> **English Prompt:**
> A 3D schematic diagram of Earth from a tilted perspective. Show two distinct orbits: 1) A solid green circular orbit directly above the equator (Geostationary). 2) A dashed red circular orbit inclined at 45 degrees to the equator (Geosynchronous). On the equatorial orbit, place a single satellite icon. On the inclined orbit, show the satellite's ground track as a figure-8 pattern over the Earth's surface. Include labels: "Geostationary Orbit (Equatorial, T=24h)", "Geosynchronous Orbit (Inclined, T=24h)", "Figure-8 Ground Track". Use a dark space background with a starfield.
>
> **中文描述:**
> 一张从倾斜视角看地球的3D示意图。显示两条不同的轨道：1) 一条位于赤道正上方的实心绿色圆形轨道（地球静止）。2) 一条与赤道成45度角的虚线红色圆形轨道（地球同步）。在赤道轨道上放置一个卫星图标。在倾斜轨道上，显示卫星在地球表面上的“8”字形地面轨迹。包含标签：“地球静止轨道（赤道，T=24h）”、“地球同步轨道（倾斜，T=24h）”、“8字形地面轨迹”。使用带有星空的深色太空背景。
>
> **Labels Required / 需要标注:**
> * Geostationary Orbit (Equatorial, T=24h)
> * Geosynchronous Orbit (Inclined, T=24h)
> * Figure-8 Ground Track
>
> **Style / 风格:** 3D schematic / textbook diagram
>
> **Exam Relevance / 考试关联:**
> This diagram clarifies the critical distinction between the two terms, a common source of confusion in exam questions.

---

# 4. Formulas / 公式

The primary formula for determining the orbital radius of a geostationary satellite is derived from equating gravitational and centripetal forces.

$$ \frac{GMm}{r^2} = m \omega^2 r $$

Since $\omega = \frac{2\pi}{T}$, we can rewrite this as:

$$ \frac{GM}{r^2} = \left(\frac{2\pi}{T}\right)^2 r $$

$$ \boxed{r^3 = \frac{GMT^2}{4\pi^2}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $r$ | Orbital radius from Earth's centre | 距地心的轨道半径 | m |
| $G$ | Gravitational constant ($6.67 \times 10^{-11}$) | 万有引力常数 | N m² kg⁻² |
| $M$ | Mass of the Earth ($5.97 \times 10^{24}$ kg) | 地球质量 | kg |
| $T$ | Orbital period (86,400 s for geostationary) | 轨道周期（地球静止为86,400秒） | s |

**Derivation / 推导:**
1.  Start with Newton's law of gravitation and centripetal force: $\frac{GMm}{r^2} = \frac{mv^2}{r}$.
2.  Substitute $v = \frac{2\pi r}{T}$: $\frac{GMm}{r^2} = \frac{m(2\pi r/T)^2}{r}$.
3.  Simplify: $\frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}$.
4.  Rearrange for $r^3$: $r^3 = \frac{GMT^2}{4\pi^2}$.

**Conditions / 适用条件:**
- The satellite's mass $m$ is negligible compared to the Earth's mass $M$.
- The orbit is perfectly circular.
- The only significant force is gravity (no atmospheric drag, no other celestial bodies).

> 📷 **IMAGE PROMPT — GEO-02: Geostationary Orbit Radius Derivation**
>
> **English Prompt:**
> A clean, textbook-style vector diagram. On the left, show a large circle representing Earth with centre labelled "O". A small satellite icon is shown at a distance 'r' from the centre. Draw two arrows from the satellite: one labelled "F_g = GMm/r²" pointing towards the Earth's centre, and one labelled "F_c = mω²r" pointing in the same direction (towards the centre). On the right side of the diagram, show the key equation: r³ = GMT²/4π². Use a white background with black and blue lines.
>
> **中文描述:**
> 一个干净的教科书式矢量图。左侧显示一个代表地球的大圆，圆心标为“O”。在距圆心距离“r”处显示一个小卫星图标。从卫星画出两个箭头：一个标有“F_g = GMm/r²”指向地心，另一个标有“F_c = mω²r”指向同一方向（朝向圆心）。在图的右侧，显示关键方程：r³ = GMT²/4π²。使用白色背景，黑色和蓝色线条。
>
> **Labels Required / 需要标注:**
> * O (Earth's centre)
> * r (Orbital radius)
> * F_g = GMm/r² (Gravitational force)
> * F_c = mω²r (Centripetal force)
> * r³ = GMT²/4π²
>
> **Style / 风格:** Textbook vector / clean diagram
>
> **Exam Relevance / 考试关联:**
> This diagram visually represents the force balance that leads to the key formula, which is the most common calculation for this topic.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — GEO-03: Geostationary Satellite Applications**
>
> **English Prompt:**
> A photorealistic 3D render of Earth from space, with the Sun illuminating the right side. Show a single, large geostationary satellite positioned above the equator. The satellite should have visible solar panels and a large dish antenna. Draw a dashed, glowing ring around the Earth at the geostationary altitude (approx 35,800 km above surface). From the satellite's dish, draw three distinct beams of light (e.g., red, blue, green) pointing down to different continents (e.g., one to North America, one to Europe, one to Asia). Add small icons representing TV, phone, and weather radar at the endpoints of these beams. The background should be a deep black with a faint Milky Way. Add a text label: "Geostationary Orbit: 35,800 km Altitude".
>
> **中文描述:**
> 一张从太空看地球的逼真3D渲染图，太阳照亮了右侧。显示一个位于赤道上空的大型地球静止卫星。卫星应有可见的太阳能电池板和一个大型碟形天线。在地球周围的地球静止高度（约地表上方35,800公里）画一条虚线发光的环。从卫星的碟形天线画出三束不同颜色的光（例如红、蓝、绿）指向不同的大陆（例如一束指向北美，一束指向欧洲，一束指向亚洲）。在这些光束的末端添加代表电视、电话和天气雷达的小图标。背景应为深黑色，带有淡淡的银河。添加文字标签：“地球静止轨道：35,800公里高度”。
>
> **Labels Required / 需要标注:**
> * Geostationary Orbit: 35,800 km Altitude
> * Communication / TV Broadcast
> * Weather Monitoring
>
> **Style / 风格:** Photorealistic 3D render
>
> **Exam Relevance / 考试关联:**
> This image helps students visualize the practical importance of geostationary satellites, which is often asked about in "explain" or "state" questions.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A satellite is to be placed in a geostationary orbit around the Earth. Given that the mass of the Earth is $M = 5.97 \times 10^{24}$ kg and the gravitational constant $G = 6.67 \times 10^{-11}$ N m² kg⁻², calculate the orbital radius $r$ of the satellite. (Assume 1 day = 86,400 s).

**中文:**
一颗卫星将被放置在地球周围的静止轨道上。已知地球质量为 $M = 5.97 \times 10^{24}$ kg，万有引力常数为 $G = 6.67 \times 10^{-11}$ N m² kg⁻²，计算卫星的轨道半径 $r$。（假设1天 = 86,400秒）。

### Solution / 解答
**Step 1:** Identify the known values.
$T = 86,400$ s, $G = 6.67 \times 10^{-11}$ N m² kg⁻², $M = 5.97 \times 10^{24}$ kg.

**Step 2:** Use the derived formula for orbital radius.
$$ r^3 = \frac{GMT^2}{4\pi^2} $$

**Step 3:** Substitute the values.
$$ r^3 = \frac{(6.67 \times 10^{-11}) \times (5.97 \times 10^{24}) \times (86,400)^2}{4\pi^2} $$

**Step 4:** Calculate.
$$ r^3 = \frac{(6.67 \times 10^{-11}) \times (5.97 \times 10^{24}) \times (7.46 \times 10^9)}{39.48} $$
$$ r^3 = \frac{2.97 \times 10^{24}}{39.48} $$
$$ r^3 = 7.53 \times 10^{22} \text{ m}^3 $$

**Step 5:** Take the cube root.
$$ r = \sqrt[3]{7.53 \times 10^{22}} $$
$$ r = 4.22 \times 10^7 \text{ m} $$

### Final Answer / 最终答案
**Answer:** $r = 4.22 \times 10^7$ m (or 42,200 km from Earth's centre). **答案:** $r = 4.22 \times 10^7$ 米（或距地心42,200公里）。

### Quick Tip / 提示
**EN:** Always convert the period to seconds. A common mistake is to use 24 hours directly without converting. Also, remember this radius is from the *centre* of the Earth. To find the altitude above the surface, subtract the Earth's radius ($6.37 \times 10^6$ m).
**CN:** 始终将周期转换为秒。一个常见的错误是直接使用24小时而不进行转换。另外，请记住这个半径是从地心算起的。要找到地表以上的高度，需要减去地球半径（$6.37 \times 10^6$ 米）。

---

# 7. Flashcards / 闪卡

**Q (EN):** What are the three conditions for a satellite to be geostationary?
**Q (CN):** 卫星成为地球静止卫星的三个条件是什么？
**A (EN):** 1. Orbital period of 24 hours. 2. Orbit above the equator. 3. Orbit in the same direction as Earth's rotation (eastward).
**A (CN):** 1. 轨道周期为24小时。2. 轨道在赤道上方。3. 轨道方向与地球自转方向相同（向东）。

**Q (EN):** What is the difference between a geostationary and a geosynchronous orbit?
**Q (CN):** 地球静止轨道和地球同步轨道有什么区别？
**A (EN):** A geosynchronous orbit has a period of 24 hours but may be inclined. A geostationary orbit is a specific type of geosynchronous orbit that is also equatorial, making it appear fixed.
**A (CN):** 地球同步轨道的周期为24小时，但可能有倾角。地球静止轨道是地球同步轨道的一种特定类型，它同时也是赤道轨道，因此看起来是固定的。

**Q (EN):** What provides the centripetal force for a satellite in orbit?
**Q (CN):** 是什么为轨道上的卫星提供向心力？
**A (EN):** The gravitational force between the satellite and the Earth.
**A (CN):** 卫星与地球之间的万有引力。

**Q (EN):** What is the approximate orbital radius of a geostationary satellite from the Earth's centre?
**Q (CN):** 地球静止卫星距地心的大致轨道半径是多少？
**A (EN):)** Approximately 42,300 km (or $4.23 \times 10^7$ m).
**A (CN):** 大约42,300公里（或 $4.23 \times 10^7$ 米）。

**Q (EN):** Why must a geostationary satellite orbit above the equator?
**Q (CN):** 为什么地球静止卫星必须在赤道上方轨道运行？
**A (EN):** The centripetal force must point towards the centre of the Earth. Only an equatorial orbit allows the satellite to remain fixed over a single point on the surface.
**A (CN):** 向心力必须指向地心。只有赤道轨道才能让卫星固定在地表某一点的上方。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Geostationary Satellites
  cn: 地球静止卫星
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
  - "[[Orbital Velocity]]"
  - "[[Kepler's Third Law]]"
prerequisite_nodes:
  - "[[Gravitational Force and Field]]"
  - "[[Centripetal Acceleration and Force]]"
related_topics:
  - "[[Gravitational Potential]]"
language: bilingual_en_cn