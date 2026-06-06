# 1. Overview / 概述

**English:**
This sub-topic focuses on two critical parameters in [[Projectile Motion]]: the **Time of Flight** (the total time a projectile remains in the air) and the **Range** (the horizontal distance it travels before landing). These quantities are derived by combining the [[Horizontal and Vertical Components]] of motion using [[Equations of Motion (SUVAT)]]. Understanding how to calculate time of flight and range is essential for solving real-world problems, from sports physics (e.g., basketball shots) to engineering (e.g., artillery trajectories). This sub-topic builds directly on the decomposition of initial velocity into horizontal and vertical components and requires a solid grasp of [[Scalars and Vectors]] to handle direction correctly.

**中文:**
本子知识点聚焦于[[抛体运动]]中的两个关键参数：**飞行时间**（抛体在空中停留的总时间）和**射程**（落地前飞行的水平距离）。这些量通过使用[[运动学方程 (SUVAT)]]结合[[水平与竖直分量]]推导得出。掌握飞行时间和射程的计算对于解决现实问题至关重要，从运动物理学（如篮球投篮）到工程学（如弹道轨迹）。本子知识点直接建立在将初速度分解为水平和竖直分量的基础上，并需要扎实理解[[标量与矢量]]以正确处理方向。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Time of Flight** / 飞行时间 | The total time a projectile remains in the air from launch to landing, assuming launch and landing heights are equal. | 抛体从发射到落地在空中停留的总时间，假设发射高度与落地高度相等。 |
| **Range** / 射程 | The horizontal distance travelled by a projectile from launch point to landing point. | 抛体从发射点到落地点所经过的水平距离。 |
| **Launch Angle** / 发射角 | The angle between the initial velocity vector and the horizontal plane. | 初速度矢量与水平面之间的夹角。 |
| **Initial Velocity** / 初速度 | The velocity at the moment of launch, with both horizontal and vertical components. | 发射瞬间的速度，包含水平和竖直分量。 |
| **Symmetry** / 对称性 | In ideal projectile motion (no air resistance, equal launch/landing heights), the ascent and descent times are equal. | 在理想抛体运动中（无空气阻力，发射与落地高度相等），上升和下降时间相等。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core idea is that time of flight and range are determined **solely by the vertical and horizontal components** of the initial velocity, respectively. Since horizontal motion is uniform (constant velocity) and vertical motion is uniformly accelerated (due to gravity), we can treat them independently using [[Equations of Motion (SUVAT)]].

**Time of Flight Derivation:**
- The vertical motion determines how long the projectile stays in the air.
- At the highest point, vertical velocity becomes zero. By symmetry, the time to reach maximum height equals the time to fall back down.
- Using $v = u + at$ in the vertical direction: $0 = u\sin\theta - gt_{\text{up}}$, so $t_{\text{up}} = \frac{u\sin\theta}{g}$.
- Total time of flight: $T = 2t_{\text{up}} = \frac{2u\sin\theta}{g}$.

**Range Derivation:**
- The horizontal motion is constant velocity: $v_x = u\cos\theta$.
- Range = horizontal velocity × time of flight: $R = (u\cos\theta) \times T = (u\cos\theta) \times \frac{2u\sin\theta}{g}$.
- Using the identity $2\sin\theta\cos\theta = \sin 2\theta$, we get: $R = \frac{u^2 \sin 2\theta}{g}$.

**Key Insight:**
- For a given initial speed $u$, the maximum range occurs when $\sin 2\theta = 1$, i.e., $\theta = 45^\circ$.
- Complementary angles (e.g., $30^\circ$ and $60^\circ$) give the same range.
- Time of flight depends only on the vertical component, so a steeper angle gives a longer flight time.

**Common Pitfalls:**
- Forgetting that the formula $R = \frac{u^2 \sin 2\theta}{g}$ assumes **equal launch and landing heights**.
- Confusing time of flight with time to maximum height (the latter is half of the former).
- Using degrees in trigonometric functions without checking calculator mode.

**中文:**
核心思想是飞行时间和射程分别**仅由初速度的竖直分量和水平分量**决定。由于水平运动是匀速的（恒定速度），竖直运动是匀加速的（受重力作用），我们可以使用[[运动学方程 (SUVAT)]]独立处理它们。

**飞行时间推导：**
- 竖直运动决定了抛体在空中停留的时间。
- 在最高点，竖直速度为零。由对称性，到达最高点的时间等于下落时间。
- 在竖直方向使用 $v = u + at$：$0 = u\sin\theta - gt_{\text{up}}$，所以 $t_{\text{up}} = \frac{u\sin\theta}{g}$。
- 总飞行时间：$T = 2t_{\text{up}} = \frac{2u\sin\theta}{g}$。

**射程推导：**
- 水平运动是匀速的：$v_x = u\cos\theta$。
- 射程 = 水平速度 × 飞行时间：$R = (u\cos\theta) \times T = (u\cos\theta) \times \frac{2u\sin\theta}{g}$。
- 使用恒等式 $2\sin\theta\cos\theta = \sin 2\theta$，得到：$R = \frac{u^2 \sin 2\theta}{g}$。

**关键见解：**
- 对于给定的初速度 $u$，当 $\sin 2\theta = 1$，即 $\theta = 45^\circ$ 时，射程最大。
- 互补角（如 $30^\circ$ 和 $60^\circ$）给出相同的射程。
- 飞行时间仅取决于竖直分量，因此更陡的角度产生更长的飞行时间。

**常见错误：**
- 忘记公式 $R = \frac{u^2 \sin 2\theta}{g}$ 假设**发射高度与落地高度相等**。
- 将飞行时间与到达最大高度的时间混淆（后者是前者的一半）。
- 在三角函数中使用度数时未检查计算器模式。

---

# 4. Formulas / 公式

## Time of Flight / 飞行时间

$$ T = \frac{2u\sin\theta}{g} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T$ | Time of flight | 飞行时间 | s |
| $u$ | Initial speed | 初速度 | m/s |
| $\theta$ | Launch angle above horizontal | 发射角（与水平面夹角） | ° or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m/s² |

## Range / 射程

$$ R = \frac{u^2 \sin 2\theta}{g} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $R$ | Range | 射程 | m |
| $u$ | Initial speed | 初速度 | m/s |
| $\theta$ | Launch angle | 发射角 | ° or rad |
| $g$ | Acceleration due to gravity | 重力加速度 | m/s² |

**Derivation / 推导:**
1. Resolve initial velocity: $u_x = u\cos\theta$, $u_y = u\sin\theta$.
2. Vertical motion: $v_y = u_y - gt$. At top, $v_y = 0 \Rightarrow t_{\text{up}} = \frac{u\sin\theta}{g}$.
3. By symmetry, $T = 2t_{\text{up}} = \frac{2u\sin\theta}{g}$.
4. Horizontal motion: $R = u_x \times T = (u\cos\theta) \times \frac{2u\sin\theta}{g} = \frac{u^2 \sin 2\theta}{g}$.

**Conditions / 适用条件:**
- No air resistance (ideal projectile motion).
- Launch and landing at the same vertical height.
- Uniform gravitational field ($g$ constant).
- Earth's surface approximated as flat.

> 📷 **IMAGE PROMPT — TFR-01: Range vs Launch Angle Graph**
>
> **English Prompt:**
> A clean, textbook-style graph showing Range (R) on the y-axis vs Launch Angle (θ) on the x-axis (0° to 90°). The curve is a smooth parabola peaking at θ = 45°. Annotate the maximum point with "R_max = u²/g". Show two symmetric points at 30° and 60° with equal range values. Use a white background, blue curve, black axes with gridlines. Include labels: "Range / m" on y-axis, "Launch Angle / °" on x-axis. Add a small inset diagram of a projectile trajectory at 45°.
>
> **中文描述:**
> 一张干净、教科书风格的图表，y轴为射程R，x轴为发射角θ（0°到90°）。曲线为平滑抛物线，在θ=45°处达到峰值。标注最大值点"R_max = u²/g"。显示30°和60°两个对称点，具有相等的射程值。使用白色背景、蓝色曲线、黑色坐标轴和网格线。y轴标注"射程 / m"，x轴标注"发射角 / °"。添加一个45°抛体轨迹的小插图。
>
> **Labels Required / 需要标注:**
> * R_max = u²/g at θ = 45°
> * Equal ranges at 30° and 60°
> * Axes: Range (y), Launch Angle (x)
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This graph is frequently used in multiple-choice questions to test understanding of the relationship between launch angle and range, especially the symmetry property.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — TFR-02: Projectile Trajectory with Time of Flight and Range Labels**
>
> **English Prompt:**
> A 2D side-view diagram of a projectile trajectory (parabolic arc) from launch point (left) to landing point (right). The launch angle θ is shown at the start. A horizontal dashed arrow labeled "Range (R)" spans from launch to landing. A vertical dashed line at the peak shows maximum height. Two small clock icons: one at launch, one at landing, with "T" (time of flight) written between them. The initial velocity vector u is shown at launch, decomposed into u_x (horizontal) and u_y (vertical) components. Use a clean vector style, white background, blue trajectory, red dashed lines for components. Include labels: "Launch", "Landing", "θ", "u_x = u cos θ", "u_y = u sin θ".
>
> **中文描述:**
> 一张抛体轨迹（抛物线弧）的二维侧视图，从发射点（左侧）到落地点（右侧）。在起点处显示发射角θ。一条水平虚线箭头从发射到落地标注为"射程(R)"。在最高点处有一条竖直虚线显示最大高度。两个小钟表图标：一个在发射点，一个在落地点，之间写有"T"（飞行时间）。在发射点显示初速度矢量u，分解为u_x（水平）和u_y（竖直）分量。使用干净的矢量风格，白色背景，蓝色轨迹，红色虚线表示分量。包含标签："发射"、"落地"、"θ"、"u_x = u cos θ"、"u_y = u sin θ"。
>
> **Labels Required / 需要标注:**
> * Range (R) — horizontal dashed arrow
> * Time of Flight (T) — between launch and landing
> * Launch angle θ
> * Velocity components: u_x, u_y
> * Launch and Landing points
>
> **Style / 风格:** Textbook vector / 3D render
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding how time of flight and range are derived from the components. It is commonly used in exam questions asking students to label or calculate these quantities.

---

# 6. Worked Example / 典型例题

### Example 1: Standard Calculation / 例题1：标准计算

**English:**
A projectile is launched with an initial speed of 20 m/s at an angle of 30° above the horizontal. Calculate:
(a) The time of flight.
(b) The range.
Assume $g = 9.81 \text{ m/s}^2$ and no air resistance.

**中文:**
一个抛体以20 m/s的初速度、与水平面成30°角发射。计算：
(a) 飞行时间。
(b) 射程。
假设 $g = 9.81 \text{ m/s}^2$，无空气阻力。

### Solution / 解答

**Step 1: Identify knowns**
$u = 20 \text{ m/s}$, $\theta = 30^\circ$, $g = 9.81 \text{ m/s}^2$

**Step 2: Time of flight**
$$ T = \frac{2u\sin\theta}{g} = \frac{2 \times 20 \times \sin 30^\circ}{9.81} = \frac{40 \times 0.5}{9.81} = \frac{20}{9.81} \approx 2.04 \text{ s} $$

**Step 3: Range**
$$ R = \frac{u^2 \sin 2\theta}{g} = \frac{20^2 \times \sin 60^\circ}{9.81} = \frac{400 \times 0.8660}{9.81} = \frac{346.4}{9.81} \approx 35.3 \text{ m} $$

### Final Answer / 最终答案
**Answer:** (a) $T \approx 2.04 \text{ s}$, (b) $R \approx 35.3 \text{ m}$
**答案:** (a) $T \approx 2.04 \text{ s}$, (b) $R \approx 35.3 \text{ m}$

### Quick Tip / 提示
Always check your calculator is in **degree mode** when using angles in degrees. A common mistake is using radian mode, which gives incorrect trigonometric values.

---

### Example 2: Finding Launch Angle / 例题2：求发射角

**English:**
A projectile has a range of 50 m when launched with an initial speed of 25 m/s. Find the two possible launch angles. Take $g = 9.81 \text{ m/s}^2$.

**中文:**
一个抛体以25 m/s的初速度发射，射程为50 m。求两个可能的发射角。取 $g = 9.81 \text{ m/s}^2$。

### Solution / 解答

**Step 1: Use range formula**
$$ R = \frac{u^2 \sin 2\theta}{g} \Rightarrow 50 = \frac{25^2 \times \sin 2\theta}{9.81} $$

**Step 2: Solve for $\sin 2\theta$**
$$ \sin 2\theta = \frac{50 \times 9.81}{625} = \frac{490.5}{625} = 0.7848 $$

**Step 3: Find $2\theta$**
$$ 2\theta = \sin^{-1}(0.7848) \approx 51.7^\circ \text{ or } 180^\circ - 51.7^\circ = 128.3^\circ $$

**Step 4: Find $\theta$**
$$ \theta = \frac{51.7^\circ}{2} \approx 25.9^\circ \quad \text{or} \quad \theta = \frac{128.3^\circ}{2} \approx 64.1^\circ $$

### Final Answer / 最终答案
**Answer:** $\theta \approx 25.9^\circ$ and $\theta \approx 64.1^\circ$ (complementary angles)
**答案:** $\theta \approx 25.9^\circ$ 和 $\theta \approx 64.1^\circ$（互补角）

### Quick Tip / 提示
Remember that $\sin(180^\circ - \alpha) = \sin \alpha$, so there are always two angles that give the same range (except at 45°). These are complementary angles (sum to 90°).

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the formula for time of flight of a projectile launched from ground level?
Q (CN): 从地面发射的抛体，其飞行时间的公式是什么？
A (EN): $T = \frac{2u\sin\theta}{g}$, where $u$ is initial speed, $\theta$ is launch angle, and $g$ is acceleration due to gravity.
A (CN): $T = \frac{2u\sin\theta}{g}$，其中 $u$ 是初速度，$\theta$ 是发射角，$g$ 是重力加速度。

**Flashcard 2:**
Q (EN): What launch angle gives the maximum range for a given initial speed?
Q (CN): 对于给定的初速度，哪个发射角能获得最大射程？
A (EN): 45° above the horizontal.
A (CN): 与水平面成45°角。

**Flashcard 3:**
Q (EN): Two projectiles are launched with the same speed at angles of 30° and 60°. How do their ranges compare?
Q (CN): 两个抛体以相同速度分别在30°和60°角发射。它们的射程如何比较？
A (EN): They have the same range because $\sin(2 \times 30^\circ) = \sin(2 \times 60^\circ) = \sin 60^\circ$.
A (CN): 它们具有相同的射程，因为 $\sin(2 \times 30^\circ) = \sin(2 \times 60^\circ) = \sin 60^\circ$。

**Flashcard 4:**
Q (EN): What assumption is made in the standard range formula $R = \frac{u^2 \sin 2\theta}{g}$?
Q (CN): 标准射程公式 $R = \frac{u^2 \sin 2\theta}{g}$ 做了哪些假设？
A (EN): Launch and landing heights are equal, no air resistance, and uniform gravitational field.
A (CN): 发射高度与落地高度相等，无空气阻力，均匀重力场。

**Flashcard 5:**
Q (EN): If the launch angle is increased from 30° to 45° (same initial speed), what happens to the time of flight?
Q (CN): 如果发射角从30°增加到45°（初速度相同），飞行时间如何变化？
A (EN): It increases because $\sin\theta$ increases, so $T = \frac{2u\sin\theta}{g}$ becomes larger.
A (CN): 飞行时间增加，因为 $\sin\theta$ 增大，所以 $T = \frac{2u\sin\theta}{g}$ 变大。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Time of Flight and Range
  cn: 飞行时间与射程
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
  - "[[Maximum Height]]"
  - "[[Projectile Motion Graphs]]"
prerequisites:
  - "[[Scalars and Vectors]]"
  - "[[Equations of Motion (SUVAT)]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn