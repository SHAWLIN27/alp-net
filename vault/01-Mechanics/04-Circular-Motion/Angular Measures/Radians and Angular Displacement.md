# Radians and Angular Displacement / 弧度与角位移

---

# 1. Overview / 概述

**English:**
This sub-topic introduces the fundamental concept of **angular displacement** and the **radian** as the SI unit for measuring angles in physics. Unlike degrees, which are arbitrary (360° for a full circle), the radian is a natural unit derived directly from the geometry of a circle. Understanding radians is essential because all angular equations in A-Level Physics (e.g., angular velocity $\omega = \frac{\Delta\theta}{\Delta t}$, centripetal acceleration $a = \omega^2 r$) are defined using radians, not degrees. This sub-topic forms the foundation for [[Angular Velocity]], [[Period and Frequency]], and the [[Relationship Between Linear and Angular Quantities]]. It builds directly on [[Displacement, Velocity and Acceleration]] from linear motion.

**中文:**
本子知识点介绍**角位移**的基本概念，以及**弧度**作为物理学中测量角度的SI单位。与度数（一个完整圆为360°）不同，弧度是一个自然单位，直接从圆的几何性质推导而来。理解弧度至关重要，因为A-Level物理中所有角量方程（如角速度 $\omega = \frac{\Delta\theta}{\Delta t}$、向心加速度 $a = \omega^2 r$）都使用弧度定义，而非度数。本子知识点为[[角速度]]、[[周期与频率]]以及[[线性量与角量的关系]]奠定基础，并直接建立在[[位移、速度与加速度]]的线性运动知识之上。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (14.1 a-e) | Edexcel IAL (WPH14 U4: 5.1-5.4) |
|-----------------------|----------------------------------|
| Understand the concept of angular displacement | Understand the concept of angular displacement |
| Define the radian | Define the radian |
| Convert between degrees and radians | Convert between degrees and radians |
| Use angular displacement in circular motion problems | Use angular displacement in circular motion problems |
| Relate angular displacement to arc length | Relate angular displacement to arc length |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to define a radian in words and mathematically. You must be able to convert between degrees and radians without a calculator for common angles (e.g., 30°, 45°, 60°, 90°, 180°). You must understand that angular displacement is a vector quantity (direction given by the right-hand rule) and use the equation $s = r\theta$ correctly.
- **中文:** 必须能用文字和数学方式定义弧度。必须能在常见角度（如30°、45°、60°、90°、180°）之间进行度数与弧度的换算，且不依赖计算器。必须理解角位移是矢量（方向由右手定则确定），并能正确使用公式 $s = r\theta$。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Radian** / 弧度 | The angle subtended at the centre of a circle by an arc equal in length to the radius of the circle. | 在圆中，弧长等于半径时，该弧所对的圆心角的大小。 | ❌ Thinking 1 rad ≈ 57.3° is an approximation for calculation only — it is the exact definition. / 认为1 rad ≈ 57.3° 只是计算近似值——这是精确定义。 |
| **Angular Displacement** / 角位移 | The angle through which a point or line has been rotated in a specified direction about a specified axis. | 一个点或一条线绕指定轴在指定方向上旋转过的角度。 | ❌ Confusing angular displacement (vector) with angle (scalar). / 混淆角位移（矢量）与角度（标量）。 |
| **Arc Length** / 弧长 | The distance along the curved path of a circle between two points on the circumference. | 圆周上两点之间沿圆弧路径的距离。 | ❌ Using chord length instead of arc length in $s = r\theta$. / 在 $s = r\theta$ 中使用弦长而非弧长。 |
| **Right-Hand Rule** / 右手定则 | A convention to determine the direction of angular displacement: curl fingers in direction of rotation, thumb points in direction of angular displacement vector. | 确定角位移方向的约定：手指弯曲方向为旋转方向，拇指指向角位移矢量方向。 | ❌ Forgetting that angular displacement is a vector with direction. / 忘记角位移是有方向的矢量。 |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Radian / 弧度

### Explanation / 解释
**English:**
The radian (rad) is the SI unit for measuring angles. One radian is defined as the angle subtended at the centre of a circle by an arc whose length is exactly equal to the radius of the circle. This means that for any circle, if you take a piece of string equal to the radius and lay it along the circumference, the angle at the centre is exactly 1 radian.

The relationship between arc length $s$, radius $r$, and angle $\theta$ (in radians) is:
$$ s = r\theta $$

Since the circumference of a full circle is $2\pi r$, the angle for a full circle is:
$$ \theta_{\text{full}} = \frac{s}{r} = \frac{2\pi r}{r} = 2\pi \text{ rad} $$

Therefore:
$$ 2\pi \text{ rad} = 360^\circ $$
$$ \pi \text{ rad} = 180^\circ $$
$$ 1 \text{ rad} = \frac{180^\circ}{\pi} \approx 57.3^\circ $$

**中文:**
弧度（rad）是测量角度的SI单位。一弧度定义为：在圆中，弧长恰好等于半径时，该弧所对的圆心角的大小。这意味着对于任何圆，如果你取一段等于半径长度的绳子，沿着圆周放置，圆心处的角度恰好为1弧度。

弧长 $s$、半径 $r$ 和角度 $\theta$（以弧度为单位）之间的关系为：
$$ s = r\theta $$

由于整个圆的周长为 $2\pi r$，整个圆对应的角度为：
$$ \theta_{\text{全圆}} = \frac{s}{r} = \frac{2\pi r}{r} = 2\pi \text{ rad} $$

因此：
$$ 2\pi \text{ rad} = 360^\circ $$
$$ \pi \text{ rad} = 180^\circ $$
$$ 1 \text{ rad} = \frac{180^\circ}{\pi} \approx 57.3^\circ $$

### Physical Meaning / 物理意义
**English:** The radian is a "natural" unit because it is dimensionless — it is a ratio of two lengths (arc length / radius). This makes all angular equations in physics simpler and more elegant. When you use radians, the derivative of $\sin\theta$ is $\cos\theta$; when you use degrees, it is $\frac{\pi}{180}\cos\theta$ — messy!

**中文:** 弧度是一个"自然"单位，因为它无量纲——它是两个长度的比值（弧长/半径）。这使得物理学中所有角量方程更简单、更优雅。使用弧度时，$\sin\theta$ 的导数是 $\cos\theta$；使用度数时，则是 $\frac{\pi}{180}\cos\theta$ —— 很繁琐！

### Common Misconceptions / 常见误区
- ❌ **"Radians are just another unit like degrees."** — No! Radians are dimensionless; degrees are arbitrary. All physics equations require radians.
- ❌ **"I can use degrees in $s = r\theta$."** — No! The formula $s = r\theta$ only works when $\theta$ is in radians.
- ❌ **"1 radian is exactly 57.3°."** — It's approximately 57.3°. The exact value is $180^\circ/\pi$.

- ❌ **"弧度只是另一种像度数一样的单位。"** — 不对！弧度无量纲；度数是人为定义的。所有物理方程都需要弧度。
- ❌ **"我可以在 $s = r\theta$ 中使用度数。"** — 不对！公式 $s = r\theta$ 仅在 $\theta$ 以弧度为单位时成立。
- ❌ **"1弧度正好是57.3°。"** — 这是近似值。精确值是 $180^\circ/\pi$。

### Exam Tips / 考试提示
- **English:** Always check the mode of your calculator (RAD vs DEG). In A-Level Physics, unless explicitly stated, assume angles are in radians. Memorise common conversions: $30^\circ = \pi/6$, $45^\circ = \pi/4$, $60^\circ = \pi/3$, $90^\circ = \pi/2$, $180^\circ = \pi$, $360^\circ = 2\pi$.
- **中文:** 始终检查计算器的模式（RAD vs DEG）。在A-Level物理中，除非明确说明，否则假设角度以弧度为单位。记住常见换算：$30^\circ = \pi/6$, $45^\circ = \pi/4$, $60^\circ = \pi/3$, $90^\circ = \pi/2$, $180^\circ = \pi$, $360^\circ = 2\pi$。

> 📷 **IMAGE PROMPT — DIAGRAM-01: Definition of a Radian**
> A clear diagram showing a circle with centre O, radius r. An arc of length r is marked on the circumference. The angle at the centre subtended by this arc is labelled "1 radian". Include labels: radius = r, arc length = r, angle θ = 1 rad. Use clean vector graphics style with blue circle, red arc, and black labels.

## 4.2 Angular Displacement / 角位移

### Explanation / 解释
**English:**
Angular displacement ($\theta$ or $\Delta\theta$) is the angle through which an object rotates about a fixed axis. It is a **vector** quantity. The magnitude is the angle of rotation (in radians), and the direction is given by the **right-hand rule**: curl the fingers of your right hand in the direction of rotation; your thumb points in the direction of the angular displacement vector.

For a complete revolution:
$$ \Delta\theta = 2\pi \text{ rad} $$

For $n$ revolutions:
$$ \Delta\theta = 2\pi n \text{ rad} $$

**中文:**
角位移（$\theta$ 或 $\Delta\theta$）是物体绕固定轴旋转过的角度。它是一个**矢量**量。大小是旋转角度（以弧度为单位），方向由**右手定则**确定：右手手指弯曲方向为旋转方向，拇指指向角位移矢量方向。

对于一整圈：
$$ \Delta\theta = 2\pi \text{ rad} $$

对于 $n$ 圈：
$$ \Delta\theta = 2\pi n \text{ rad} $$

### Physical Meaning / 物理意义
**English:** Angular displacement is the rotational analogue of linear displacement. Just as linear displacement tells you how far and in what direction an object has moved, angular displacement tells you how much and in which direction an object has rotated. It is the foundation for defining [[Angular Velocity]] ($\omega = \Delta\theta/\Delta t$).

**中文:** 角位移是线性位移的旋转类比。正如线性位移告诉你物体移动了多远以及方向，角位移告诉你物体旋转了多少以及方向。它是定义[[角速度]]（$\omega = \Delta\theta/\Delta t$）的基础。

### Common Misconceptions / 常见误区
- ❌ **"Angular displacement is just an angle."** — No! It is a vector with magnitude and direction.
- ❌ **"After one full rotation, angular displacement is zero."** — No! It is $2\pi$ rad (or $360^\circ$). The object has rotated, even if it returns to its starting orientation.
- ❌ **"Direction doesn't matter for angular displacement."** — It does! Clockwise vs anticlockwise are opposite directions.

- ❌ **"角位移只是一个角度。"** — 不对！它是具有大小和方向的矢量。
- ❌ **"旋转一整圈后，角位移为零。"** — 不对！是 $2\pi$ rad（或 $360^\circ$）。物体已经旋转了，即使它回到了起始方向。
- ❌ **"方向对角位移不重要。"** — 重要！顺时针和逆时针是相反方向。

### Exam Tips / 考试提示
- **English:** When a question says "the object rotates through 5 complete revolutions", the angular displacement is $10\pi$ rad, not 0. Always specify direction (clockwise/anticlockwise) when describing angular displacement.
- **中文:** 当题目说"物体旋转了5整圈"时，角位移是 $10\pi$ rad，而不是0。描述角位移时始终指明方向（顺时针/逆时针）。

---

# 5. Essential Equations / 核心公式

## 5.1 Arc Length Equation / 弧长公式

$$ s = r\theta $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $s$ | Arc length | 弧长 | m |
| $r$ | Radius of circle | 圆的半径 | m |
| $\theta$ | Angle in radians | 以弧度为单位的角度 | rad (dimensionless) |

**Derivation / 推导:**
By definition of radian: $\theta = s/r$. Rearranging gives $s = r\theta$.

**Conditions / 适用条件:**
- **English:** $\theta$ MUST be in radians. The formula is exact for any angle. For very small angles ($\theta \ll 1$ rad), the arc length is approximately equal to the chord length.
- **中文:** $\theta$ 必须以弧度为单位。该公式对任何角度都精确成立。对于非常小的角度（$\theta \ll 1$ rad），弧长近似等于弦长。

**Limitations / 局限性:**
- **English:** Only applies to circular arcs. Does not apply to elliptical or other curved paths.
- **中文:** 仅适用于圆弧。不适用于椭圆或其他曲线路径。

## 5.2 Conversion Between Degrees and Radians / 度数与弧度换算

$$ \theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180} $$

$$ \theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\theta_{\text{rad}}$ | Angle in radians | 以弧度为单位的角度 | rad |
| $\theta_{\text{deg}}$ | Angle in degrees | 以度数为单位的角度 | ° |

**Derivation / 推导:**
From $360^\circ = 2\pi$ rad, dividing both sides by 360 gives $1^\circ = \frac{\pi}{180}$ rad.

**Conditions / 适用条件:**
- **English:** Always exact. Use $\pi$ symbol in answers unless a numerical value is requested.
- **中文:** 始终精确。除非要求数值，否则在答案中使用 $\pi$ 符号。

**Limitations / 局限性:**
- **English:** None — it's a pure conversion factor.
- **中文:** 无——这是纯换算因子。

## 5.3 Angular Displacement for Multiple Revolutions / 多圈角位移

$$ \Delta\theta = 2\pi n $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta\theta$ | Angular displacement | 角位移 | rad |
| $n$ | Number of complete revolutions | 完整旋转圈数 | dimensionless |

**Derivation / 推导:**
Each complete revolution is $2\pi$ rad. For $n$ revolutions, total angle = $n \times 2\pi$ rad.

**Conditions / 适用条件:**
- **English:** Only for complete revolutions. For partial revolutions, use $s = r\theta$ or direct measurement.
- **中文:** 仅适用于完整旋转。对于部分旋转，使用 $s = r\theta$ 或直接测量。

**Limitations / 局限性:**
- **English:** Assumes rotation about a fixed axis.
- **中文:** 假设绕固定轴旋转。

> 📷 **IMAGE PROMPT — DIAGRAM-02: Arc Length and Angle**
> A circle with centre O, radius r. An arc of length s is highlighted in red. The angle θ at the centre is shown. Labels: s = rθ, r = radius, θ in radians. Include a small inset showing a very small angle where arc ≈ chord.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Arc Length vs Angle (Constant Radius) / 弧长与角度关系（半径恒定）

### Axes / 坐标轴
- **X-axis:** Angle $\theta$ / rad (角度 $\theta$ / rad)
- **Y-axis:** Arc length $s$ / m (弧长 $s$ / m)

### Shape / 形状
- **English:** A straight line through the origin with gradient equal to the radius $r$.
- **中文:** 一条通过原点的直线，斜率等于半径 $r$。

### Gradient Meaning / 斜率含义
- **English:** The gradient $= r$ (radius of the circle). A steeper line means a larger radius.
- **中文:** 斜率 $= r$（圆的半径）。直线越陡，半径越大。

### Area Meaning / 面积含义
- **English:** No meaningful physical area.
- **中文:** 没有有意义的物理面积。

### Exam Interpretation / 考试解读
- **English:** If given a graph of $s$ vs $\theta$, the gradient gives the radius. If the line is not straight, the radius is changing (not circular motion).
- **中文:** 如果给出 $s$ vs $\theta$ 的图表，斜率给出半径。如果直线不直，则半径在变化（不是圆周运动）。

```mermaid
graph LR
    A[Angle θ / rad] --> B[Arc Length s = rθ]
    B --> C[Gradient = r]
    C --> D[Radius of Circle]
```

---

# 7. Required Diagrams / 必备图表

## 7.1 Definition of a Radian / 弧度的定义

### Description / 描述
**English:** A circle with centre O, showing an arc of length equal to the radius, subtending an angle of 1 radian at the centre.
**中文:** 一个圆心为O的圆，显示一段长度等于半径的弧，在圆心处对应1弧度的角度。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-01: Definition of a Radian**
> Ultra-detailed AI image generation prompt: "A clean, textbook-style diagram of a circle with centre O. The radius r is drawn from O to point A on the circumference. An arc of length exactly r is drawn from point A to point B along the circumference. The angle AOB at the centre is labelled '1 radian'. Labels: 'radius = r', 'arc length = r', 'θ = 1 rad'. Use blue for the circle outline, red for the arc, black for labels. Vector graphics style, white background, suitable for A-Level physics textbook."

### Labels Required / 需要标注
- Centre O / 圆心O
- Radius r / 半径r
- Arc length = r / 弧长 = r
- Angle θ = 1 rad / 角度 θ = 1 rad

### Exam Importance / 考试重要性
- **English:** High — definition of radian is a common 2-mark question. Must be able to reproduce this diagram from memory.
- **中文:** 高——弧度的定义是常见的2分题。必须能凭记忆重现此图。

## 7.2 Angular Displacement Direction (Right-Hand Rule) / 角位移方向（右手定则）

### Description / 描述
**English:** A diagram showing a rotating object (e.g., a wheel) with the axis of rotation, the direction of rotation (curved arrow), and the angular displacement vector (straight arrow) pointing along the axis according to the right-hand rule.
**中文:** 显示旋转物体（如轮子）的图表，包括旋转轴、旋转方向（弯曲箭头）以及根据右手定则沿轴指向的角位移矢量（直线箭头）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-03: Right-Hand Rule for Angular Displacement**
> "A 3D-style diagram showing a wheel rotating anticlockwise when viewed from above. The axis of rotation is vertical. A curved arrow shows the direction of rotation (anticlockwise). A straight arrow points upward along the axis, labelled 'angular displacement vector'. A hand icon in the corner shows the right-hand rule: fingers curled anticlockwise, thumb pointing up. Clean vector style, blue and red arrows, white background."

### Labels Required / 需要标注
- Axis of rotation / 旋转轴
- Direction of rotation / 旋转方向
- Angular displacement vector / 角位移矢量
- Right-hand rule / 右手定则

### Exam Importance / 考试重要性
- **English:** Medium — understanding direction is crucial for vector addition of angular displacements and for understanding angular velocity as a vector.
- **中文:** 中——理解方向对于角位移的矢量加法以及理解角速度作为矢量至关重要。

---

# 8. Worked Examples / 典型例题

## Example 1: Converting Degrees to Radians / 度数与弧度换算

### Question / 题目
**English:**
Convert the following angles to radians:
(a) $45^\circ$
(b) $120^\circ$
(c) $270^\circ$

**中文:**
将以下角度转换为弧度：
(a) $45^\circ$
(b) $120^\circ$
(c) $270^\circ$

### Solution / 解答
**Step 1:** Use the conversion factor $\frac{\pi}{180}$.

**Step 2:** Multiply each angle by $\frac{\pi}{180}$.

(a) $45^\circ \times \frac{\pi}{180} = \frac{45\pi}{180} = \frac{\pi}{4}$ rad

(b) $120^\circ \times \frac{\pi}{180} = \frac{120\pi}{180} = \frac{2\pi}{3}$ rad

(c) $270^\circ \times \frac{\pi}{180} = \frac{270\pi}{180} = \frac{3\pi}{2}$ rad

### Final Answer / 最终答案
**Answer:** (a) $\frac{\pi}{4}$ rad, (b) $\frac{2\pi}{3}$ rad, (c) $\frac{3\pi}{2}$ rad | **答案：** (a) $\frac{\pi}{4}$ rad, (b) $\frac{2\pi}{3}$ rad, (c) $\frac{3\pi}{2}$ rad

### Quick Tip / 提示
- **English:** Always simplify fractions. Memorise common angles: $30^\circ = \pi/6$, $45^\circ = \pi/4$, $60^\circ = \pi/3$, $90^\circ = \pi/2$, $180^\circ = \pi$.
- **中文:** 始终化简分数。记住常见角度：$30^\circ = \pi/6$, $45^\circ = \pi/4$, $60^\circ = \pi/3$, $90^\circ = \pi/2$, $180^\circ = \pi$。

---

## Example 2: Using $s = r\theta$ / 使用 $s = r\theta$

### Question / 题目
**English:**
A bicycle wheel has a radius of 0.35 m. The wheel rotates through an angle of $150^\circ$. Calculate the distance travelled by a point on the rim of the wheel.

**中文:**
自行车轮半径为0.35 m。车轮旋转了 $150^\circ$。计算轮缘上一点移动的距离。

### Solution / 解答
**Step 1:** Convert angle to radians.
$$ \theta = 150^\circ \times \frac{\pi}{180} = \frac{150\pi}{180} = \frac{5\pi}{6} \text{ rad} $$

**Step 2:** Use $s = r\theta$.
$$ s = 0.35 \times \frac{5\pi}{6} $$

**Step 3:** Calculate.
$$ s = 0.35 \times \frac{5 \times 3.1416}{6} = 0.35 \times 2.618 = 0.916 \text{ m} $$

### Final Answer / 最终答案
**Answer:** 0.916 m (or $\frac{7\pi}{24}$ m exactly) | **答案：** 0.916 m（精确值为 $\frac{7\pi}{24}$ m）

### Quick Tip / 提示
- **English:** Always convert degrees to radians before using $s = r\theta$. Leaving the answer in terms of $\pi$ is often acceptable and preferred in exam questions.
- **中文:** 在使用 $s = r\theta$ 之前，始终将度数转换为弧度。在考试题中，答案保留 $\pi$ 通常是可以接受且更受青睐的。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Define a radian / 定义弧度 | High / 高 | Easy / 简单 | 📝 *待填入* |
| Convert degrees to radians / 度转弧度 | High / 高 | Easy / 简单 | 📝 *待填入* |
| Calculate arc length using $s = r\theta$ / 使用 $s = r\theta$ 计算弧长 | Medium / 中 | Medium / 中等 | 📝 *待填入* |
| Angular displacement in multi-revolution problems / 多圈旋转中的角位移 | Medium / 中 | Medium / 中等 | 📝 *待填入* |
| Vector nature of angular displacement / 角位移的矢量性 | Low / 低 | Hard / 困难 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Define, Convert, Calculate, Determine, Show that, State
- **中文:** 定义、转换、计算、确定、证明、陈述

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in the following ways:

1. **Measuring Angular Displacement:** In experiments involving circular motion (e.g., [[Centripetal Acceleration and Force]]), you may need to measure angular displacement using a protractor or by counting revolutions and converting to radians.

2. **Uncertainty in Angle Measurement:** When measuring angles with a protractor, the typical uncertainty is $\pm 0.5^\circ$. This must be converted to radians: $\pm 0.5^\circ \times \frac{\pi}{180} \approx \pm 0.0087$ rad. This uncertainty propagates into calculations of arc length and angular velocity.

3. **Graph Plotting:** When plotting graphs of arc length vs angle, the gradient gives the radius. You must ensure angles are in radians for the gradient to be meaningful.

4. **Experimental Design:** In experiments to determine the relationship between angle and arc length (e.g., using a rotating platform), you must control the radius and measure angles accurately.

**中文:**
本子知识点通过以下方式与实验工作联系：

1. **测量角位移：** 在涉及圆周运动的实验中（如[[向心加速度与力]]），可能需要使用量角器测量角位移，或通过计数旋转圈数并转换为弧度。

2. **角度测量的不确定度：** 使用量角器测量角度时，典型不确定度为 $\pm 0.5^\circ$。这必须转换为弧度：$\pm 0.5^\circ \times \frac{\pi}{180} \approx \pm 0.0087$ rad。该不确定度会传播到弧长和角速度的计算中。

3. **图表绘制：** 绘制弧长与角度的关系图时，斜率给出半径。必须确保角度以弧度为单位，斜率才有意义。

4. **实验设计：** 在确定角度与弧长关系的实验中（如使用旋转平台），必须控制半径并准确测量角度。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Radians and Angular Displacement - Leaf Node Concept Map
    A[Radians and Angular Displacement] --> B[Definition of Radian]
    A --> C[Angular Displacement]
    A --> D[Conversion: Degrees ↔ Radians]
    A --> E[Arc Length Formula: s = rθ]
    
    B --> B1[Arc length = radius]
    B --> B2[Natural unit]
    B --> B3[2π rad = 360°]
    
    C --> C1[Vector quantity]
    C --> C2[Right-hand rule for direction]
    C --> C3[Δθ = 2πn for n revolutions]
    
    D --> D1[Multiply by π/180]
    D --> D2[Common angles to memorise]
    
    E --> E1[θ must be in radians]
    E --> E2[Gradient of s vs θ graph = r]
    
    %% Links to parent and siblings
    A --> F[Parent: [[Angular Measures]]]
    A --> G[Sibling: [[Angular Velocity]]]
    A --> H[Sibling: [[Period and Frequency]]]
    A --> I[Sibling: [[Relationship Between Linear and Angular Quantities]]]
    
    %% Prerequisites
    A --> J[Prerequisite: [[Displacement, Velocity and Acceleration]]]
    
    %% Related topics
    A --> K[Related: [[Centripetal Acceleration and Force]]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Radian:** Angle when arc length = radius. **Angular displacement:** Angle rotated about an axis (vector). / **弧度：** 弧长等于半径时的角度。**角位移：** 绕轴旋转的角度（矢量）。 |
| **Key Formula / 核心公式** | $s = r\theta$ (θ in rad), $\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$, $\Delta\theta = 2\pi n$ |
| **Key Conversion / 核心换算** | $30^\circ = \pi/6$, $45^\circ = \pi/4$, $60^\circ = \pi/3$, $90^\circ = \pi/2$, $180^\circ = \pi$, $360^\circ = 2\pi$ |
| **Key Graph / 核心图表** | $s$ vs $\theta$: straight line through origin, gradient = radius $r$ / $s$ vs $\theta$：通过原点的直线，斜率 = 半径 $r$ |
| **Common Mistake / 常见错误** | Using degrees in $s = r\theta$; forgetting angular displacement is a vector / 在 $s = r\theta$ 中使用度数；忘记角位移是矢量 |
| **Exam Tip / 考试提示** | Always check calculator mode (RAD/DEG). Memorise common conversions. Leave answers in terms of $\pi$ when possible. / 始终检查计算器模式（RAD/DEG）。记住常见换算。尽可能保留 $\pi$ 在答案中。 |
| **Direction / 方向** | Right-hand rule: fingers curl in rotation direction, thumb points along axis / 右手定则：手指弯曲方向为旋转方向，拇指指向轴方向 |
| **SI Unit / SI单位** | radian (rad) — dimensionless / 弧度（rad）— 无量纲 |

---

> 📋 **CIE Only:** CAIE 9702 syllabus 14.1 specifically requires understanding of angular displacement as a vector and the use of the right-hand rule. Be prepared for questions asking you to state the direction of angular displacement.
> 
> 📋 **Edexcel Only:** Edexcel IAL WPH14 U4 5.1-5.4 focuses more on the mathematical relationship $s = r\theta$ and conversion between degrees and radians. The vector nature is less emphasised but still important for understanding angular velocity.