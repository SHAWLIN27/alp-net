# 1. Overview / 概述

**English:**
Two-dimensional collisions extend the principle of [[Conservation of Momentum]] from straight-line motion to collisions occurring in a plane. Unlike one-dimensional collisions where all motion is along a single axis, two-dimensional collisions involve momentum components in both the x and y directions. This sub-topic is crucial for understanding real-world collisions — from car crashes at intersections to particle physics experiments. The key insight is that momentum is a vector quantity, so it must be conserved separately in each perpendicular direction. This builds directly on [[Linear Momentum and Impulse]] and connects to [[Elastic Collisions]] and [[Inelastic Collisions]] when considering energy conservation.

**中文:**
二维碰撞将[[Conservation of Momentum]]的原理从直线运动扩展到平面内的碰撞。与所有运动沿单一轴的一维碰撞不同，二维碰撞涉及x和y两个方向上的动量分量。这个子知识点对于理解现实世界中的碰撞至关重要——从十字路口的车祸到粒子物理实验。关键洞察是动量是矢量量，因此必须在每个垂直方向上分别守恒。这直接建立在[[Linear Momentum and Impulse]]的基础上，并在考虑能量守恒时与[[Elastic Collisions]]和[[Inelastic Collisions]]相关联。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Two-Dimensional Collision** / 二维碰撞 | A collision where the velocities of the objects before and after impact have components in two perpendicular directions (typically x and y). | 物体碰撞前后的速度在两个垂直方向（通常为x和y）上都有分量的碰撞。 |
| **Component Method** / 分量法 | The technique of resolving momentum vectors into perpendicular components and applying conservation separately to each direction. | 将动量矢量分解为垂直分量，并分别对每个方向应用守恒定律的技巧。 |
| **Oblique Collision** / 斜碰 | A collision where the line of impact is not aligned with the initial velocity vectors, causing deflection. | 碰撞线不与初始速度矢量对齐，导致偏转的碰撞。 |
| **Line of Impact** / 碰撞线 | The line passing through the centers of two colliding objects at the point of contact; momentum is conserved along this line. | 通过两个碰撞物体接触点中心的线；动量沿此线守恒。 |
| **Coefficient of Restitution (2D)** / 恢复系数（二维） | The ratio of relative speed of separation to relative speed of approach along the line of impact, extended to two dimensions. | 沿碰撞线的分离相对速度与接近相对速度之比，扩展到二维。 |
| **Glancing Collision** / 擦碰 | A collision where objects do not collide head-on, resulting in both objects moving off at angles to their original directions. | 物体非正面碰撞，导致两个物体都沿与原始方向成角度的方向运动的碰撞。 |

---

# 3. Key Concepts / 关键概念

**English:**
The fundamental principle of two-dimensional collisions is **vector conservation of momentum**. Since momentum is a vector, the total momentum before collision equals the total momentum after collision in **both** the x-direction and y-direction independently.

### Step-by-Step Approach:
1. **Define coordinate axes**: Choose x and y axes (often aligning one axis with the initial direction of one object).
2. **Resolve velocities**: Break all velocities into x and y components using trigonometry ($v_x = v\cos\theta$, $v_y = v\sin\theta$).
3. **Apply conservation in x-direction**: $m_1u_{1x} + m_2u_{2x} = m_1v_{1x} + m_2v_{2x}$
4. **Apply conservation in y-direction**: $m_1u_{1y} + m_2u_{2y} = m_1v_{1y} + m_2v_{2y}$
5. **Solve the system**: Two equations, which may allow solving for up to two unknowns.

### Physical Interpretation:
In a glancing collision (e.g., one ball striking another off-center), the struck object gains momentum in a direction perpendicular to the line of centers, while the incoming object is deflected. This is why snooker balls scatter at angles — momentum is redistributed in both dimensions.

### Common Pitfalls:
- **Forgetting that momentum is a vector**: Always include direction signs (+/−) for components.
- **Assuming equal angles**: In elastic collisions of equal masses, the angle between final velocities is 90°, but this is a special case, not a general rule.
- **Mixing up coordinate systems**: Be consistent with which angle is measured from which axis.
- **Neglecting the line of impact**: In oblique collisions, only momentum components along the line of impact are affected by the collision force; perpendicular components remain unchanged.

### Connection to [[Newton's Laws of Motion]]:
The conservation of momentum in 2D follows directly from Newton's Third Law — the impulse between two objects acts along the line of impact, so perpendicular components of momentum are unaffected by the collision itself.

**中文:**
二维碰撞的基本原理是**动量的矢量守恒**。由于动量是矢量，碰撞前的总动量在**x方向和y方向**上分别等于碰撞后的总动量。

### 分步方法：
1. **定义坐标轴**：选择x和y轴（通常将其中一个轴与一个物体的初始方向对齐）。
2. **分解速度**：使用三角函数将所有速度分解为x和y分量（$v_x = v\cos\theta$, $v_y = v\sin\theta$）。
3. **在x方向应用守恒**：$m_1u_{1x} + m_2u_{2x} = m_1v_{1x} + m_2v_{2x}$
4. **在y方向应用守恒**：$m_1u_{1y} + m_2u_{2y} = m_1v_{1y} + m_2v_{2y}$
5. **解方程组**：两个方程，最多可解两个未知数。

### 物理解释：
在擦碰中（例如一个球偏离中心撞击另一个球），被撞击的物体在垂直于中心线的方向上获得动量，而入射物体被偏转。这就是台球以角度散开的原因——动量在两个维度上重新分配。

### 常见错误：
- **忘记动量是矢量**：始终包含方向符号（+/−）。
- **假设角度相等**：在等质量的弹性碰撞中，最终速度之间的角度为90°，但这是特殊情况，不是一般规则。
- **混淆坐标系**：确保角度是从哪个轴测量的保持一致。
- **忽略碰撞线**：在斜碰中，只有沿碰撞线的动量分量受碰撞力影响；垂直分量保持不变。

---

# 4. Formulas / 公式

## Primary Formula: Conservation of Momentum in 2D

$$ \vec{p}_{\text{total before}} = \vec{p}_{\text{total after}} $$

In component form:

$$ m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2 $$

$$ \begin{cases} m_1u_{1x} + m_2u_{2x} = m_1v_{1x} + m_2v_{2x} \\ m_1u_{1y} + m_2u_{2y} = m_1v_{1y} + m_2v_{2y} \end{cases} $$

Where:
$$ u_{ix} = u_i\cos\theta_i, \quad u_{iy} = u_i\sin\theta_i $$
$$ v_{ix} = v_i\cos\phi_i, \quad v_{iy} = v_i\sin\phi_i $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $m_1, m_2$ | Masses of objects 1 and 2 | 物体1和2的质量 | kg |
| $\vec{u}_1, \vec{u}_2$ | Initial velocity vectors | 初始速度矢量 | m s⁻¹ |
| $\vec{v}_1, \vec{v}_2$ | Final velocity vectors | 最终速度矢量 | m s⁻¹ |
| $\theta_i$ | Angle of initial velocity from x-axis | 初始速度与x轴的夹角 | ° or rad |
| $\phi_i$ | Angle of final velocity from x-axis | 最终速度与x轴的夹角 | ° or rad |
| $u_{ix}, u_{iy}$ | x and y components of initial velocity | 初始速度的x和y分量 | m s⁻¹ |
| $v_{ix}, v_{iy}$ | x and y components of final velocity | 最终速度的x和y分量 | m s⁻¹ |

## Special Case: Elastic Collision in 2D (Equal Masses)

For an elastic collision between two equal masses where one is initially stationary:

$$ \phi_1 + \phi_2 = 90^\circ $$

This means the two objects move off at right angles to each other.

## Special Case: Stationary Target

If object 2 is initially stationary ($\vec{u}_2 = 0$):

$$ m_1\vec{u}_1 = m_1\vec{v}_1 + m_2\vec{v}_2 $$

**Derivation / 推导:**
The component equations come directly from resolving the vector equation. For the equal-mass elastic case, combining conservation of momentum (vector) with conservation of kinetic energy (scalar) yields the 90° result — a classic A-Level derivation.

**Conditions / 适用条件:**
- No external forces act on the system during the collision (or they are negligible).
- The collision is instantaneous (impulsive forces dominate).
- For the 90° rule: elastic collision, equal masses, one object initially at rest.

> 📷 **IMAGE PROMPT — 2D-COL-01: Two-Dimensional Collision Vector Diagram**
>
> **English Prompt:**
> A clean textbook-style vector diagram showing a two-dimensional collision between two balls. Ball 1 (mass m₁, red) approaches from the left at angle θ₁ to the x-axis with velocity u₁. Ball 2 (mass m₂, blue) is initially stationary at the origin. After collision, ball 1 moves at angle φ₁ with velocity v₁, and ball 2 moves at angle φ₂ with velocity v₂. Show all velocity vectors as labeled arrows with components. Include dashed construction lines for x and y components. Use a white background with black lines and colored vectors. Add a coordinate axis system (x, y) in the bottom-left corner. Label all angles clearly.
>
> **中文描述:**
> 一个干净的教科书式矢量图，显示两个球之间的二维碰撞。球1（质量m₁，红色）从左侧以与x轴成θ₁角、速度u₁接近。球2（质量m₂，蓝色）最初静止在原点。碰撞后，球1以角度φ₁、速度v₁运动，球2以角度φ₂、速度v₂运动。显示所有速度矢量为带标签的箭头，并带有分量。包括x和y分量的虚线构造线。使用白色背景、黑色线条和彩色矢量。在左下角添加坐标轴系统（x, y）。清晰标注所有角度。
>
> **Labels Required / 需要标注:**
> * m₁, u₁, θ₁ (before)
> * m₂ (at rest, before)
> * m₁, v₁, φ₁ (after)
> * m₂, v₂, φ₂ (after)
> * x, y axes
>
> **Style / 风格:** Textbook vector diagram, clean, 2D, flat colors
>
> **Exam Relevance / 考试关联:**
> Essential for visualizing how to set up momentum conservation equations in two dimensions. Students must be able to draw and interpret such diagrams.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — 2D-COL-02: Snooker Ball Glancing Collision**
>
> **English Prompt:**
> A photorealistic top-down view of a snooker table showing a glancing collision between two balls. The cue ball (white) is approaching a stationary red ball at an angle. Show the moment of impact with a small flash/spark effect at the contact point. Use motion blur trails behind both balls to show their paths before and after collision. The red ball should be moving off at an angle to the cue ball's original path. Include faint dotted lines showing the original path of the cue ball and the line of centers at impact. Use warm lighting, green baize texture, and realistic ball reflections. The perspective should be directly overhead.
>
> **中文描述:**
> 一张逼真的俯视图，显示斯诺克台球桌上的擦碰。白球（白色）以一定角度接近静止的红球。显示碰撞瞬间，接触点有微小的闪光/火花效果。在两个球后面使用运动模糊轨迹显示它们碰撞前后的路径。红球应以与白球原始路径成角度的方向运动。包括显示白球原始路径和碰撞时中心线的淡虚线。使用暖色灯光、绿色台面纹理和逼真的球体反射。视角应为正上方。
>
> **Labels Required / 需要标注:**
> * Cue ball path (before and after)
> * Red ball path (after)
> * Line of centers
> * Impact point
>
> **Style / 风格:** Photorealistic, top-down, sports photography style
>
> **Exam Relevance / 考试关联:**
> Helps students connect the abstract vector mathematics to a familiar real-world scenario. Snooker collisions are classic examples of 2D momentum conservation.

---

# 6. Worked Example / 典型例题

### Question / 题目

**English:**
A ball of mass 0.50 kg moving at 4.0 m s⁻¹ strikes a stationary ball of mass 0.30 kg. After the collision, the 0.50 kg ball moves at 2.5 m s⁻¹ at an angle of 30° to its original direction. Calculate:
(a) The velocity (magnitude and direction) of the 0.30 kg ball after the collision.
(b) Determine whether the collision is elastic or inelastic.

**中文:**
一个质量为0.50 kg、以4.0 m s⁻¹运动的球撞击一个质量为0.30 kg的静止球。碰撞后，0.50 kg的球以2.5 m s⁻¹的速度沿与其原始方向成30°角的方向运动。计算：
(a) 碰撞后0.30 kg球的速度（大小和方向）。
(b) 判断该碰撞是弹性碰撞还是非弹性碰撞。

### Solution / 解答

**Step 1: Set up coordinate system**
Let the original direction of the 0.50 kg ball be the x-axis.

**Step 2: Write known values**
- $m_1 = 0.50\text{ kg}$, $u_1 = 4.0\text{ m s}^{-1}$, $\theta_1 = 0^\circ$
- $m_2 = 0.30\text{ kg}$, $u_2 = 0\text{ m s}^{-1}$
- $v_1 = 2.5\text{ m s}^{-1}$, $\phi_1 = 30^\circ$
- Unknown: $v_2$, $\phi_2$

**Step 3: Resolve initial momenta**
$$p_{1x} = 0.50 \times 4.0 = 2.0\text{ kg m s}^{-1}$$
$$p_{1y} = 0$$
$$p_{2x} = 0,\ p_{2y} = 0$$

**Step 4: Resolve final momenta of ball 1**
$$v_{1x} = 2.5\cos30^\circ = 2.5 \times 0.866 = 2.165\text{ m s}^{-1}$$
$$v_{1y} = 2.5\sin30^\circ = 2.5 \times 0.5 = 1.25\text{ m s}^{-1}$$

**Step 5: Apply conservation of momentum in x-direction**
$$m_1u_{1x} + m_2u_{2x} = m_1v_{1x} + m_2v_{2x}$$
$$2.0 + 0 = (0.50 \times 2.165) + 0.30v_{2x}$$
$$2.0 = 1.0825 + 0.30v_{2x}$$
$$0.30v_{2x} = 0.9175$$
$$v_{2x} = 3.058\text{ m s}^{-1}$$

**Step 6: Apply conservation of momentum in y-direction**
$$m_1u_{1y} + m_2u_{2y} = m_1v_{1y} + m_2v_{2y}$$
$$0 + 0 = (0.50 \times 1.25) + 0.30v_{2y}$$
$$0 = 0.625 + 0.30v_{2y}$$
$$v_{2y} = -2.083\text{ m s}^{-1}$$

**Step 7: Calculate magnitude and direction of $v_2$**
$$v_2 = \sqrt{v_{2x}^2 + v_{2y}^2} = \sqrt{3.058^2 + (-2.083)^2}$$
$$v_2 = \sqrt{9.351 + 4.339} = \sqrt{13.690} = 3.70\text{ m s}^{-1}$$

$$\tan\phi_2 = \frac{v_{2y}}{v_{2x}} = \frac{-2.083}{3.058} = -0.681$$
$$\phi_2 = \tan^{-1}(-0.681) = -34.3^\circ$$

The negative sign means the 0.30 kg ball moves at 34.3° **below** the x-axis.

**Step 8: Check if collision is elastic**
Calculate total kinetic energy before:
$$KE_{\text{before}} = \frac{1}{2}m_1u_1^2 = \frac{1}{2} \times 0.50 \times 4.0^2 = 4.0\text{ J}$$

Calculate total kinetic energy after:
$$KE_{\text{after}} = \frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2$$
$$KE_{\text{after}} = \frac{1}{2} \times 0.50 \times 2.5^2 + \frac{1}{2} \times 0.30 \times 3.70^2$$
$$KE_{\text{after}} = 1.5625 + 2.0535 = 3.616\text{ J}$$

Since $KE_{\text{before}} \neq KE_{\text{after}}$, the collision is **inelastic**.

### Final Answer / 最终答案

**Answer:**
(a) The 0.30 kg ball moves at **3.70 m s⁻¹** at an angle of **34.3° below the original direction** of the 0.50 kg ball.
(b) The collision is **inelastic** (kinetic energy is not conserved).

**答案：**
(a) 0.30 kg的球以**3.70 m s⁻¹**的速度，沿与0.50 kg球原始方向成**34.3°向下**的角度运动。
(b) 该碰撞是**非弹性碰撞**（动能不守恒）。

### Quick Tip / 提示

**English:** Always check the sign of your y-component velocity. A negative y-component means the object moves downward (or opposite to your chosen positive y-direction). In 2D collision problems, the two equations (x and y) are independent — solve them separately, then combine for the final vector.

**中文：** 始终检查y分量速度的符号。负的y分量意味着物体向下运动（或与你选择的正y方向相反）。在二维碰撞问题中，两个方程（x和y）是独立的——分别求解，然后组合得到最终矢量。

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): Why must momentum be conserved separately in the x and y directions for a 2D collision?
Q (CN): 为什么二维碰撞中动量必须在x和y方向上分别守恒？
A (EN): Because momentum is a vector. The total momentum vector before collision equals the total momentum vector after collision, which means each component must be equal independently.
A (CN): 因为动量是矢量。碰撞前的总动量矢量等于碰撞后的总动量矢量，这意味着每个分量必须分别相等。

**Flashcard 2**
Q (EN): What is the 90° rule in 2D collisions, and what conditions are required for it to apply?
Q (CN): 二维碰撞中的90°规则是什么，需要什么条件才能应用？
A (EN): In an elastic collision between two equal masses where one is initially stationary, the two objects move off at right angles (90°) to each other after the collision.
A (CN): 在两个等质量的弹性碰撞中，其中一个初始静止，碰撞后两个物体以直角（90°）相互分开运动。

**Flashcard 3**
Q (EN): How do you resolve a velocity vector v at angle θ into components for a 2D collision problem?
Q (CN): 如何将角度为θ的速度矢量v分解为二维碰撞问题的分量？
A (EN): vₓ = v cos θ (horizontal component), vᵧ = v sin θ (vertical component). Ensure your angle is measured from the correct axis.
A (CN): vₓ = v cos θ（水平分量），vᵧ = v sin θ（垂直分量）。确保角度是从正确的轴测量的。

**Flashcard 4**
Q (EN): In a 2D collision, what happens to the momentum component perpendicular to the line of impact?
Q (CN): 在二维碰撞中，垂直于碰撞线的动量分量会发生什么变化？
A (EN): The momentum component perpendicular to the line of impact remains unchanged for each object individually, because the collision force acts only along the line of impact.
A (CN): 垂直于碰撞线的动量分量对每个物体单独保持不变，因为碰撞力只沿碰撞线作用。

**Flashcard 5**
Q (EN): A 2 kg ball moving at 3 m s⁻¹ east strikes a stationary 1 kg ball. After collision, the 2 kg ball moves at 2 m s⁻¹ at 40° north of east. What is the y-component of the 1 kg ball's velocity?
Q (CN): 一个2 kg的球以3 m s⁻¹向东运动，撞击一个静止的1 kg球。碰撞后，2 kg的球以2 m s⁻¹的速度沿东偏北40°运动。1 kg球速度的y分量是多少？
A (EN): Using conservation of momentum in y-direction: 0 = (2 × 2 sin 40°) + (1 × v₂ᵧ), so v₂ᵧ = -2.57 m s⁻¹ (southward).
A (CN): 使用y方向的动量守恒：0 = (2 × 2 sin 40°) + (1 × v₂ᵧ)，所以v₂ᵧ = -2.57 m s⁻¹（向南）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Two-Dimensional Collisions"
  cn: "二维碰撞"
parent_topic: "Conservation of Momentum"
parent_hub: "[[Conservation of Momentum]]"
subject: Physics
syllabus:
  - CAIE 9702: 3.2 (i-k)
  - Edexcel IAL: WPH11 U1: 2.15-2.18
level: AS
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Elastic Collisions]]"
  - "[[Inelastic Collisions]]"
  - "[[Explosions and Recoil]]"
prerequisites:
  - "[[Linear Momentum and Impulse]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn