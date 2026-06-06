# 1. Overview / 概述

**English:**
Resolving forces on inclined planes is a fundamental skill in [[Free-body Diagrams]] that bridges geometry and mechanics. When an object rests on a slope, its weight does not act perpendicular to the surface — instead, it must be split into two perpendicular components: one parallel to the slope (causing acceleration) and one perpendicular (determining the normal reaction). This sub-topic is essential for understanding [[Newton's Laws of Motion]] applications, particularly for objects sliding, resting, or being pulled up ramps. Mastering this skill allows you to simplify complex 2D problems into two independent 1D problems along and perpendicular to the plane.

**中文:**
斜面受力分解是[[Free-body Diagrams]]中的一项基本技能，它将几何学与力学联系起来。当物体放置在斜面上时，其重力并不垂直于斜面表面——必须将其分解为两个垂直分量：一个平行于斜面（导致加速度），一个垂直于斜面（决定法向反作用力）。这个子知识点对于理解[[Newton's Laws of Motion]]的应用至关重要，特别是对于在斜坡上滑动、静止或被拉动的物体。掌握这项技能可以将复杂的二维问题简化为沿斜面和平行于斜面方向的两个独立的一维问题。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Resolving forces** / 力的分解 | Splitting a single force into two perpendicular components that together have the same effect as the original force. | 将一个力分解为两个相互垂直的分量，这两个分量的共同作用效果与原力相同。 |
| **Inclined plane** / 斜面 | A flat surface tilted at an angle θ to the horizontal, used to study the effects of gravity on objects at an angle. | 与水平面成θ角的平面，用于研究重力在倾斜方向上的作用效果。 |
| **Component parallel to slope** / 沿斜面分量 | The part of the weight that acts down the slope, given by $mg\sin\theta$, causing acceleration or requiring an opposing force. | 重力沿斜面方向的分量，大小为$mg\sin\theta$，导致加速度或需要相反的力来平衡。 |
| **Component perpendicular to slope** / 垂直斜面分量 | The part of the weight that acts into the slope, given by $mg\cos\theta$, balanced by the normal reaction force. | 重力垂直于斜面方向的分量，大小为$mg\cos\theta$，由法向反作用力平衡。 |
| **Normal reaction** / 法向反作用力 | The force exerted by the surface perpendicular to the plane, equal in magnitude to $mg\cos\theta$ when no other vertical forces act. | 斜面施加的垂直于平面的力，当没有其他垂直力作用时，大小等于$mg\cos\theta$。 |
| **Angle of inclination** / 倾斜角 | The angle θ between the inclined plane and the horizontal, measured from the horizontal upward. | 斜面与水平面之间的夹角θ，从水平面向上测量。 |

---

# 3. Key Concepts / 关键概念

**English:**
The key insight for resolving forces on inclined planes is that **the weight vector $mg$ always acts vertically downward**, regardless of the slope angle. This means we must rotate our coordinate system to align with the plane, not the horizontal.

**Step-by-step reasoning:**

1. **Draw the free-body diagram** (see [[Drawing Free-body Diagrams]]): Show the object, the weight $mg$ vertically down, the normal reaction $N$ perpendicular to the slope, and any friction $F$ parallel to the slope.

2. **Choose axes**: Align the x-axis parallel to the slope (downward positive is conventional) and the y-axis perpendicular to the slope (away from the surface positive).

3. **Resolve the weight**: The weight $mg$ makes an angle θ with the perpendicular to the slope (or equivalently, θ with the vertical). Using trigonometry:
   - Component parallel to slope (down the plane): $mg\sin\theta$
   - Component perpendicular to slope (into the plane): $mg\cos\theta$

4. **Apply Newton's Second Law** ([[Newton's Laws of Motion]]):
   - Perpendicular to slope: $N - mg\cos\theta = ma_y$ (usually $a_y = 0$ if no motion off the surface)
   - Parallel to slope: $mg\sin\theta - F = ma$ (if friction opposes motion)

**Common pitfalls:**
- ❌ Confusing which component uses sin vs cos. **Tip**: If the angle is measured from the horizontal, the parallel component uses sin; if from the vertical, it uses cos. Always draw the right-angled triangle.
- ❌ Forgetting that the normal reaction is NOT equal to $mg$ on a slope — it's $mg\cos\theta$.
- ❌ Using the wrong angle when the plane is not at the standard angle.

**中文:**
斜面受力分解的关键在于：**重力矢量$mg$始终竖直向下**，与斜面角度无关。这意味着我们必须旋转坐标系使其与斜面平行，而不是与水平面平行。

**逐步推理：**

1. **绘制受力分析图**（参见[[Drawing Free-body Diagrams]]）：画出物体、竖直向下的重力$mg$、垂直于斜面的法向反作用力$N$，以及平行于斜面的摩擦力$F$。

2. **选择坐标轴**：将x轴平行于斜面（通常向下为正），y轴垂直于斜面（远离斜面为正）。

3. **分解重力**：重力$mg$与斜面垂线之间的夹角为θ（或等效地与竖直方向夹角为θ）。使用三角函数：
   - 平行于斜面的分量（沿斜面向下）：$mg\sin\theta$
   - 垂直于斜面的分量（垂直进入斜面）：$mg\cos\theta$

4. **应用牛顿第二定律**（[[Newton's Laws of Motion]]）：
   - 垂直于斜面：$N - mg\cos\theta = ma_y$（通常$a_y = 0$，如果没有离开表面的运动）
   - 平行于斜面：$mg\sin\theta - F = ma$（如果摩擦力阻碍运动）

**常见错误：**
- ❌ 混淆哪个分量用sin，哪个用cos。**提示**：如果角度从水平面测量，平行分量用sin；如果从竖直方向测量，则用cos。始终画出直角三角形。
- ❌ 忘记斜面上的法向反作用力不等于$mg$——而是$mg\cos\theta$。
- ❌ 当斜面不是标准角度时使用错误的角度。

---

# 4. Formulas / 公式

**Primary formula for resolving weight on an inclined plane:**

$$ \text{Parallel component: } F_{\parallel} = mg\sin\theta $$
$$ \text{Perpendicular component: } F_{\perp} = mg\cos\theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $m$ | mass of object | 物体的质量 | kg |
| $g$ | acceleration due to gravity (9.81 m s⁻²) | 重力加速度 (9.81 m s⁻²) | m s⁻² |
| $\theta$ | angle of inclination from horizontal | 斜面与水平面的夹角 | degrees or radians |
| $F_{\parallel}$ | component of weight parallel to slope | 重力沿斜面的分量 | N |
| $F_{\perp}$ | component of weight perpendicular to slope | 重力垂直于斜面的分量 | N |

**Derivation / 推导:**

Consider a block on a slope at angle θ to the horizontal. The weight $mg$ acts vertically down. Draw a right-angled triangle where:
- The hypotenuse is $mg$
- The side opposite θ (parallel to slope) is $mg\sin\theta$
- The side adjacent to θ (perpendicular to slope) is $mg\cos\theta$

This follows from basic trigonometry: $\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}$ and $\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}$.

**Conditions / 适用条件:**
- The plane is a straight, rigid surface
- The angle θ is measured from the horizontal
- The object is in contact with the surface (no jumping off)
- Standard gravity $g = 9.81 \text{ m s}^{-2}$ applies

> 📷 **IMAGE PROMPT — FBD-IP-01: Weight Resolution on Inclined Plane**
>
> **English Prompt:**
> A clean 2D vector diagram showing a rectangular block on an inclined plane at angle θ (30°). The weight vector mg points straight down from the center of the block. Two dashed lines extend from the tip of the weight vector: one parallel to the slope (labeled "mg sin θ") and one perpendicular to the slope (labeled "mg cos θ"). A right-angle symbol connects these components. The normal reaction N points perpendicularly away from the surface. The angle θ is marked between the horizontal and the slope. Use a textbook-style vector diagram with arrows, clear labels, and a white background. Color code: weight in red, components in blue, normal in green.
>
> **中文描述:**
> 一个清晰的二维矢量图，显示一个矩形块在倾斜角为θ（30°）的斜面上。重力矢量mg从块的中心竖直向下。从重力矢量末端延伸出两条虚线：一条平行于斜面（标注"mg sin θ"），一条垂直于斜面（标注"mg cos θ"）。这些分量之间有一个直角符号。法向反作用力N垂直于斜面指向外。角度θ标记在水平面和斜面之间。采用教科书风格的矢量图，带有箭头、清晰的标签和白色背景。颜色编码：重力为红色，分量为蓝色，法向力为绿色。
>
> **Labels Required / 需要标注:**
> * θ (angle of inclination)
> * mg (weight, vertical down)
> * mg sin θ (parallel component)
> * mg cos θ (perpendicular component)
> * N (normal reaction)
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This is the most common diagram in inclined plane questions — students must be able to draw and label it from memory.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — FBD-IP-02: Three Cases of Inclined Plane Forces**
>
> **English Prompt:**
> A split-panel diagram showing three different scenarios on the same inclined plane (θ = 25°). Left panel: Block at rest with friction — show all forces: weight mg (vertical down), normal N (perpendicular), friction F (up the slope), and resolved components mg sin θ and mg cos θ. Middle panel: Block sliding down with no friction — only weight components and normal, with an acceleration arrow a down the slope. Right panel: Block being pulled up the slope by a force T parallel to the slope — show T, friction F down the slope, weight components, and normal. Each panel has a coordinate system (x parallel, y perpendicular). Use a clean educational illustration style with consistent color coding: weight = red, normal = blue, friction = orange, tension = purple, acceleration = green dashed arrow. White background, clear labels in English.
>
> **中文描述:**
> 一个分屏图，显示同一斜面（θ = 25°）上的三种不同情景。左面板：静止且有摩擦的块——显示所有力：重力mg（竖直向下）、法向力N（垂直）、摩擦力F（沿斜面向上）以及分解分量mg sin θ和mg cos θ。中面板：无摩擦下滑的块——仅显示重力分量和法向力，沿斜面向下有一个加速度箭头a。右面板：被平行于斜面的力T向上拉的块——显示T、沿斜面向下的摩擦力F、重力分量和法向力。每个面板都有坐标系（x平行，y垂直）。采用清晰的教育插图风格，颜色编码一致：重力=红色，法向力=蓝色，摩擦力=橙色，拉力=紫色，加速度=绿色虚线箭头。白色背景，清晰的英文标签。
>
> **Labels Required / 需要标注:**
> * θ (angle)
> * mg, mg sin θ, mg cos θ
> * N (normal reaction)
> * F (friction, with direction)
> * T (tension, if applicable)
> * a (acceleration, if applicable)
>
> **Style / 风格:** Educational illustration, split-panel
>
> **Exam Relevance / 考试关联:**
> Exam questions often ask students to compare scenarios with and without friction, or with an applied force. This diagram helps visualize all three common cases.

---

# 6. Worked Example / 典型例题

### Example 1: Block Sliding Down a Smooth Inclined Plane

### Question / 题目
**English:**
A block of mass 5.0 kg slides down a smooth (frictionless) inclined plane at an angle of 30° to the horizontal. Calculate:
(a) The component of the weight acting down the slope.
(b) The acceleration of the block down the slope.
(c) The normal reaction force from the plane on the block.
(Take $g = 9.81 \text{ m s}^{-2}$)

**中文:**
一个质量为5.0 kg的块在光滑（无摩擦）斜面上滑下，斜面与水平面夹角为30°。计算：
(a) 沿斜面方向的重力分量。
(b) 块沿斜面的加速度。
(c) 斜面对块的法向反作用力。
（取$g = 9.81 \text{ m s}^{-2}$）

### Solution / 解答

**Step 1: Identify forces and resolve weight**
Weight: $mg = 5.0 \times 9.81 = 49.05 \text{ N}$

Parallel component: $F_{\parallel} = mg\sin\theta = 49.05 \times \sin 30° = 49.05 \times 0.5 = 24.525 \text{ N}$

Perpendicular component: $F_{\perp} = mg\cos\theta = 49.05 \times \cos 30° = 49.05 \times 0.866 = 42.48 \text{ N}$

**Step 2: Apply Newton's Second Law parallel to slope**
Since no friction: $F_{\text{net, parallel}} = mg\sin\theta = ma$
$$24.525 = 5.0 \times a$$
$$a = \frac{24.525}{5.0} = 4.905 \text{ m s}^{-2}$$

**Step 3: Apply Newton's Second Law perpendicular to slope**
No motion perpendicular to slope: $N - mg\cos\theta = 0$
$$N = mg\cos\theta = 42.48 \text{ N}$$

### Final Answer / 最终答案
**Answer:**
(a) $F_{\parallel} = 24.5 \text{ N}$ (3 s.f.)
(b) $a = 4.91 \text{ m s}^{-2}$ (3 s.f.)
(c) $N = 42.5 \text{ N}$ (3 s.f.)

**答案：**
(a) $F_{\parallel} = 24.5 \text{ N}$（3位有效数字）
(b) $a = 4.91 \text{ m s}^{-2}$（3位有效数字）
(c) $N = 42.5 \text{ N}$（3位有效数字）

### Quick Tip / 提示
**English:** For a frictionless inclined plane, the acceleration is always $a = g\sin\theta$, independent of mass! This is a common exam shortcut.

**中文：** 对于光滑斜面，加速度总是$a = g\sin\theta$，与质量无关！这是一个常见的考试捷径。

---

### Example 2: Block at Rest on a Rough Inclined Plane

### Question / 题目
**English:**
A block of mass 2.0 kg is at rest on a rough inclined plane at 20° to the horizontal. The coefficient of static friction between the block and the plane is 0.40. Show whether the block will slide down the plane.

**中文:**
一个质量为2.0 kg的块静止在粗糙斜面上，斜面与水平面夹角为20°。块与斜面之间的静摩擦系数为0.40。判断块是否会沿斜面下滑。

### Solution / 解答

**Step 1: Calculate the component of weight down the slope**
$$F_{\parallel} = mg\sin\theta = 2.0 \times 9.81 \times \sin 20° = 2.0 \times 9.81 \times 0.342 = 6.71 \text{ N}$$

**Step 2: Calculate the maximum static friction**
First find normal reaction: $N = mg\cos\theta = 2.0 \times 9.81 \times \cos 20° = 2.0 \times 9.81 \times 0.940 = 18.44 \text{ N}$

Maximum static friction: $F_{\text{max}} = \mu_s N = 0.40 \times 18.44 = 7.38 \text{ N}$

**Step 3: Compare forces**
$F_{\parallel} = 6.71 \text{ N} < F_{\text{max}} = 7.38 \text{ N}$

Since the weight component down the slope is less than the maximum static friction, the block will **not** slide.

### Final Answer / 最终答案
**Answer:** The block will NOT slide because $mg\sin\theta = 6.71 \text{ N} < \mu_s mg\cos\theta = 7.38 \text{ N}$.

**答案：** 块不会下滑，因为$mg\sin\theta = 6.71 \text{ N} < \mu_s mg\cos\theta = 7.38 \text{ N}$。

### Quick Tip / 提示
**English:** The condition for a block to just start sliding is $mg\sin\theta = \mu_s mg\cos\theta$, which simplifies to $\tan\theta = \mu_s$. This is a quick check for limiting equilibrium.

**中文：** 块刚好开始滑动的条件是$mg\sin\theta = \mu_s mg\cos\theta$，简化为$\tan\theta = \mu_s$。这是检查极限平衡的快速方法。

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): What are the two components of weight on an inclined plane at angle θ?
Q (CN): 在倾角为θ的斜面上，重力的两个分量是什么？
A (EN): Parallel component = mg sin θ (down the slope), Perpendicular component = mg cos θ (into the slope).
A (CN): 平行分量 = mg sin θ（沿斜面向下），垂直分量 = mg cos θ（垂直进入斜面）。

**Flashcard 2**
Q (EN): On a frictionless inclined plane, what is the acceleration of a block?
Q (CN): 在光滑斜面上，块的加速度是多少？
A (EN): a = g sin θ, independent of the mass of the block.
A (CN): a = g sin θ，与块的质量无关。

**Flashcard 3**
Q (EN): What is the normal reaction force on an inclined plane?
Q (CN): 斜面上的法向反作用力是多少？
A (EN): N = mg cos θ (when no other forces perpendicular to the plane act).
A (CN): N = mg cos θ（当没有其他垂直于斜面的力作用时）。

**Flashcard 4**
Q (EN): How do you determine if a block will slide on a rough inclined plane?
Q (CN): 如何判断块是否会在粗糙斜面上滑动？
A (EN): Compare mg sin θ (force down slope) with μ_s mg cos θ (maximum static friction). If mg sin θ > μ_s mg cos θ, it slides.
A (CN): 比较 mg sin θ（沿斜面向下的力）和 μ_s mg cos θ（最大静摩擦力）。如果 mg sin θ > μ_s mg cos θ，则滑动。

**Flashcard 5**
Q (EN): What is the condition for limiting equilibrium on an inclined plane?
Q (CN): 斜面上极限平衡的条件是什么？
A (EN): tan θ = μ_s, where θ is the angle of inclination and μ_s is the coefficient of static friction.
A (CN): tan θ = μ_s，其中θ是倾斜角，μ_s是静摩擦系数。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Resolving Forces on Inclined Planes"
  cn: "斜面受力分解"
parent_topic: "Free-body Diagrams"
parent_hub: "[[Free-body Diagrams]]"
subject: Physics
syllabus:
  - CAIE 9702: 3.2 (b-c)
  - Edexcel IAL: WPH11 U1: 2.4-2.6
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Drawing Free-body Diagrams]]"
  - "[[Equilibrium Conditions]]"
prerequisites:
  - "[[Types of Force]]"
related_topics:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn