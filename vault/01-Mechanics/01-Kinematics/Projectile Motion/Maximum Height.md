# Maximum Height / 最大高度

---

## 1. Overview / 概述

**English:**
Maximum height is the highest vertical displacement reached by a projectile during its flight. This sub-topic focuses on calculating the peak altitude of a projectile launched at an angle to the horizontal. Understanding maximum height is crucial for analyzing projectile trajectories, from sports physics (e.g., basketball shots, golf drives) to engineering applications (e.g., rocket launches, artillery fire). It connects directly to [[Horizontal and Vertical Components]] because the vertical component of initial velocity determines how high the projectile rises, and to [[Time of Flight and Range]] since the time to reach maximum height is exactly half the total time of flight for symmetrical trajectories.

**中文:**
最大高度是抛射体在飞行过程中达到的最高垂直位移。本子知识点专注于计算以一定角度发射的抛射体的最高点高度。理解最大高度对于分析抛射体轨迹至关重要，从体育物理（如篮球投篮、高尔夫击球）到工程应用（如火箭发射、火炮射击）都有涉及。它与[[水平与垂直分量]]直接相关，因为初速度的垂直分量决定了抛射体上升的高度；与[[飞行时间与射程]]相关，因为对于对称轨迹，到达最大高度的时间正好是总飞行时间的一半。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Maximum Height** / 最大高度 | The greatest vertical displacement of a projectile from its launch point, occurring when the vertical component of velocity becomes zero. | 抛射体从发射点达到的最大垂直位移，发生在速度的垂直分量变为零的时刻。 |
| **Peak / Apex** / 顶点 | The point on a projectile's trajectory where maximum height is reached; at this point, $v_y = 0$ and the projectile is moving horizontally only. | 抛射体轨迹上达到最大高度的点；在该点，$v_y = 0$，抛射体仅做水平运动。 |
| **Vertical Component of Initial Velocity** / 初速度垂直分量 | The upward component of the launch velocity, given by $u_y = u \sin \theta$, where $u$ is the initial speed and $\theta$ is the launch angle. | 发射速度的向上分量，由 $u_y = u \sin \theta$ 给出，其中 $u$ 是初速度大小，$\theta$ 是发射角。 |
| **Symmetrical Trajectory** / 对称轨迹 | A projectile path where launch and landing heights are equal; the time to maximum height equals the time from maximum height to landing. | 发射高度和落地高度相等的抛射体路径；到达最大高度的时间等于从最大高度到落地的时间。 |

---

## 3. Key Concepts / 关键概念

**English:**

The maximum height of a projectile is determined entirely by its **vertical motion**. Since horizontal and vertical motions are independent (as established in [[Horizontal and Vertical Components]]), we can analyze the vertical component separately using [[Equations of Motion (SUVAT)]].

### Step-by-Step Reasoning:

1. **At the peak**, the projectile's vertical velocity becomes zero ($v_y = 0$). This is the defining condition for maximum height.
2. The projectile decelerates upward at $g = 9.81 \text{ m/s}^2$ (downward acceleration due to gravity).
3. Using the SUVAT equation $v^2 = u^2 + 2as$, with $v = 0$, $u = u_y = u \sin \theta$, $a = -g$, and $s = H$ (maximum height), we derive:

$$ H = \frac{u^2 \sin^2 \theta}{2g} $$

### Physical Interpretation:
- Maximum height depends on the **square** of the initial speed — doubling the launch speed quadruples the maximum height.
- Maximum height depends on $\sin^2 \theta$ — it is maximized when $\theta = 90^\circ$ (straight up), giving $H = u^2/(2g)$.
- For a given speed, a 30° launch and a 60° launch reach the same maximum height because $\sin^2 30^\circ = \sin^2 60^\circ = 0.25$.

### Common Pitfalls:
- **Forgetting the square**: Students often write $H = u \sin \theta / (2g)$ instead of $H = u^2 \sin^2 \theta / (2g)$.
- **Using total time instead of time to peak**: The time to reach maximum height is $t_{\text{peak}} = u \sin \theta / g$, not the total time of flight.
- **Ignoring launch height**: If the projectile is launched from a height above ground, the maximum height above ground is $H + h_0$, where $h_0$ is the launch height.

**中文:**

抛射体的最大高度完全由其**垂直运动**决定。由于水平和垂直运动是独立的（如[[水平与垂直分量]]中所述），我们可以使用[[运动学方程 (SUVAT)]]单独分析垂直分量。

### 逐步推理：

1. **在顶点处**，抛射体的垂直速度变为零（$v_y = 0$）。这是最大高度的定义条件。
2. 抛射体以 $g = 9.81 \text{ m/s}^2$（重力引起的向下加速度）向上减速。
3. 使用SUVAT方程 $v^2 = u^2 + 2as$，其中 $v = 0$，$u = u_y = u \sin \theta$，$a = -g$，$s = H$（最大高度），我们推导出：

$$ H = \frac{u^2 \sin^2 \theta}{2g} $$

### 物理意义：
- 最大高度取决于初速度的**平方**——发射速度加倍，最大高度变为四倍。
- 最大高度取决于 $\sin^2 \theta$——当 $\theta = 90^\circ$（垂直向上）时最大，此时 $H = u^2/(2g)$。
- 对于相同的速度，30°发射和60°发射达到相同的最大高度，因为 $\sin^2 30^\circ = \sin^2 60^\circ = 0.25$。

### 常见错误：
- **忘记平方**：学生常写成 $H = u \sin \theta / (2g)$ 而不是 $H = u^2 \sin^2 \theta / (2g)$。
- **使用总时间而非到达顶点的时间**：到达最大高度的时间是 $t_{\text{peak}} = u \sin \theta / g$，而不是总飞行时间。
- **忽略发射高度**：如果抛射体从高于地面的高度发射，则相对于地面的最大高度为 $H + h_0$，其中 $h_0$ 是发射高度。

---

## 4. Formulas / 公式

### Primary Formula:

$$ H = \frac{u^2 \sin^2 \theta}{2g} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $H$ | Maximum height | 最大高度 | m |
| $u$ | Initial speed | 初速度大小 | m/s |
| $\theta$ | Launch angle above horizontal | 发射角（与水平面的夹角） | ° or rad |
| $g$ | Acceleration due to gravity (9.81 m/s²) | 重力加速度 (9.81 m/s²) | m/s² |

### Alternative Form (using vertical component):

$$ H = \frac{u_y^2}{2g} $$

Where $u_y = u \sin \theta$ is the vertical component of initial velocity.

### Time to Reach Maximum Height:

$$ t_{\text{peak}} = \frac{u \sin \theta}{g} = \frac{u_y}{g} $$

### Derivation / 推导:

Starting from SUVAT equation $v^2 = u^2 + 2as$:

1. Set $v = 0$ (vertical velocity at peak), $u = u_y = u \sin \theta$, $a = -g$, $s = H$
2. $0 = (u \sin \theta)^2 + 2(-g)H$
3. $0 = u^2 \sin^2 \theta - 2gH$
4. $2gH = u^2 \sin^2 \theta$
5. $H = \frac{u^2 \sin^2 \theta}{2g}$

### Conditions / 适用条件:

- **Launch and landing at same height**: This formula assumes the projectile is launched from and lands at the same vertical level.
- **No air resistance**: The formula applies only in ideal conditions where air resistance is negligible.
- **Constant gravity**: $g$ is assumed constant throughout the motion.
- **Flat ground**: The ground is assumed horizontal.

> 📷 **IMAGE PROMPT — MH01: Maximum Height Diagram**
>
> **English Prompt:**
> A clean textbook-style vector diagram showing a projectile trajectory with labeled maximum height. The trajectory is a parabolic arc starting from the origin (0,0) and ending on the x-axis. At the peak of the parabola, a dashed horizontal line extends to the y-axis, labeled "H = maximum height". The initial velocity vector is shown at the launch point, split into horizontal component (u_x, horizontal arrow) and vertical component (u_y, vertical arrow). The launch angle θ is marked between the initial velocity vector and the horizontal. A small annotation at the peak reads "v_y = 0". Use a white background, black lines, and blue/red color coding for components. Include a grid in light gray for reference.
>
> **中文描述:**
> 一个干净的教科书式矢量图，显示带有标注最大高度的抛射体轨迹。轨迹是从原点(0,0)开始并在x轴上结束的抛物线弧。在抛物线的顶点处，一条虚线水平线延伸到y轴，标注为"H = 最大高度"。在发射点处显示初速度矢量，分解为水平分量(u_x，水平箭头)和垂直分量(u_y，垂直箭头)。发射角θ标记在初速度矢量和水平线之间。顶点处有一个小标注"v_y = 0"。使用白色背景、黑色线条，分量用蓝/红色编码。包含浅灰色参考网格。
>
> **Labels Required / 需要标注:**
> * H (maximum height)
> * u (initial velocity vector)
> * u_x = u cos θ (horizontal component)
> * u_y = u sin θ (vertical component)
> * θ (launch angle)
> * v_y = 0 (at peak)
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding the geometry of projectile motion and is frequently used in exam questions to test students' ability to identify and calculate maximum height.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — MH02: Comparison of Maximum Heights for Different Launch Angles**
>
> **English Prompt:**
> A multi-panel comparison diagram showing three projectile trajectories with the same initial speed (u = 20 m/s) but different launch angles: 30°, 45°, and 60°. All three parabolas are overlaid on the same coordinate axes. The 45° trajectory has the greatest range (as shown in [[Time of Flight and Range]]), while the 30° and 60° trajectories have the same maximum height (both reaching H = 5.1 m). The 60° trajectory reaches a higher peak (H = 15.3 m) than the 30° trajectory (H = 5.1 m). Each peak is marked with a dashed horizontal line to the y-axis, with the height value labeled. Use different colors for each trajectory (blue for 30°, green for 45°, red for 60°). Include a legend. The background should be white with light grid lines.
>
> **中文描述:**
> 一个多面板比较图，显示三个具有相同初速度(u = 20 m/s)但不同发射角度的抛射体轨迹：30°、45°和60°。所有三条抛物线都叠加在同一个坐标系上。45°轨迹具有最大射程（如[[飞行时间与射程]]所示），而30°和60°轨迹具有相同的最大高度（都达到H = 5.1 m）。60°轨迹达到更高的顶点(H = 15.3 m)比30°轨迹(H = 5.1 m)。每个顶点都用虚线水平线标记到y轴，并标注高度值。每条轨迹使用不同颜色（30°用蓝色，45°用绿色，60°用红色）。包含图例。背景为白色，带有浅色网格线。
>
> **Labels Required / 需要标注:**
> * θ = 30°, H = 5.1 m
> * θ = 45°, H = 10.2 m
> * θ = 60°, H = 15.3 m
> * u = 20 m/s (same for all)
>
> **Style / 风格:** Multi-panel comparison diagram
>
> **Exam Relevance / 考试关联:**
> This comparison helps students understand the relationship between launch angle and maximum height, a common exam topic. It also reinforces the concept that complementary angles (30° and 60°) produce different heights but the same range.

---

## 6. Worked Example / 典型例题

### Example 1: Basic Maximum Height Calculation

### Question / 题目

**English:**
A projectile is launched with an initial speed of 25 m/s at an angle of 40° above the horizontal. Calculate the maximum height reached by the projectile. (Take $g = 9.81 \text{ m/s}^2$)

**中文:**
一个抛射体以25 m/s的初速度、与水平面成40°的角度发射。计算抛射体达到的最大高度。（取 $g = 9.81 \text{ m/s}^2$）

### Solution / 解答

**Step 1:** Identify the vertical component of initial velocity.

$$ u_y = u \sin \theta = 25 \times \sin 40^\circ $$

$$ u_y = 25 \times 0.6428 = 16.07 \text{ m/s} $$

**Step 2:** Use the maximum height formula.

$$ H = \frac{u_y^2}{2g} = \frac{(16.07)^2}{2 \times 9.81} $$

**Step 3:** Calculate.

$$ H = \frac{258.2}{19.62} = 13.16 \text{ m} $$

### Final Answer / 最终答案

**Answer:** $H = 13.2 \text{ m}$ (3 s.f.) **答案:** $H = 13.2 \text{ m}$ (3位有效数字)

### Quick Tip / 提示

Always calculate $u_y = u \sin \theta$ first, then use $H = u_y^2/(2g)$. This reduces errors from forgetting to square the sine term.

---

### Example 2: Finding Launch Speed from Maximum Height

### Question / 题目

**English:**
A basketball player shoots a ball at an angle of 55° to the horizontal. The ball reaches a maximum height of 3.5 m above the release point. Calculate the initial speed of the ball. (Take $g = 9.81 \text{ m/s}^2$)

**中文:**
一名篮球运动员以与水平面成55°的角度投篮。球在出手点上方达到3.5 m的最大高度。计算球的初速度。（取 $g = 9.81 \text{ m/s}^2$）

### Solution / 解答

**Step 1:** Rearrange the maximum height formula to find $u$.

$$ H = \frac{u^2 \sin^2 \theta}{2g} $$

$$ u^2 = \frac{2gH}{\sin^2 \theta} $$

**Step 2:** Substitute values.

$$ u^2 = \frac{2 \times 9.81 \times 3.5}{\sin^2 55^\circ} $$

$$ \sin 55^\circ = 0.8192, \quad \sin^2 55^\circ = 0.6710 $$

$$ u^2 = \frac{68.67}{0.6710} = 102.3 $$

**Step 3:** Take square root.

$$ u = \sqrt{102.3} = 10.11 \text{ m/s} $$

### Final Answer / 最终答案

**Answer:** $u = 10.1 \text{ m/s}$ (3 s.f.) **答案:** $u = 10.1 \text{ m/s}$ (3位有效数字)

### Quick Tip / 提示

When rearranging for $u$, remember to take the square root at the end. A common mistake is to forget the square root and give $u^2$ as the answer.

---

## 7. Flashcards / 闪卡

**Flashcard 1:**
- **Q (EN):** What is the condition for maximum height in projectile motion?
- **Q (CN):** 抛射体运动中最大高度的条件是什么？
- **A (EN):** The vertical component of velocity becomes zero ($v_y = 0$) at the peak of the trajectory.
- **A (CN):** 在轨迹顶点处，速度的垂直分量变为零（$v_y = 0$）。

**Flashcard 2:**
- **Q (EN):** Write the formula for maximum height of a projectile launched with speed $u$ at angle $\theta$.
- **Q (CN):** 写出以速度 $u$、角度 $\theta$ 发射的抛射体的最大高度公式。
- **A (EN):** $H = \frac{u^2 \sin^2 \theta}{2g}$
- **A (CN):** $H = \frac{u^2 \sin^2 \theta}{2g}$

**Flashcard 3:**
- **Q (EN):)** How does doubling the launch speed affect the maximum height?
- **Q (CN):** 将发射速度加倍如何影响最大高度？
- **A (EN):** Doubling the launch speed quadruples the maximum height, because $H \propto u^2$.
- **A (CN):** 将发射速度加倍会使最大高度变为四倍，因为 $H \propto u^2$。

**Flashcard 4:**
- **Q (EN):** What launch angle gives the maximum possible height for a given initial speed?
- **Q (CN):** 对于给定的初速度，什么发射角度能获得最大可能高度？
- **A (EN):** $\theta = 90^\circ$ (straight upward), giving $H = u^2/(2g)$.
- **A (CN):** $\theta = 90^\circ$（垂直向上），此时 $H = u^2/(2g)$。

**Flashcard 5:**
- **Q (EN):** What is the time taken to reach maximum height?
- **Q (CN):** 到达最大高度所需的时间是多少？
- **A (EN):** $t_{\text{peak}} = \frac{u \sin \theta}{g} = \frac{u_y}{g}$
- **A (CN):** $t_{\text{peak}} = \frac{u \sin \theta}{g} = \frac{u_y}{g}$

---

## 8. Metadata / 元数据

```yaml
title:
  en: Maximum Height
  cn: 最大高度
parent_topic: Projectile Motion
parent_hub: "[[Projectile Motion]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Horizontal and Vertical Components]]"
  - "[[Time of Flight and Range]]"
  - "[[Projectile Motion Graphs]]"
prerequisites:
  - "[[Scalars and Vectors]]"
  - "[[Equations of Motion (SUVAT)]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn