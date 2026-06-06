# 1. Overview / 概述

**English:**
This sub-topic bridges the gap between linear (straight-line) motion and rotational motion. It establishes the fundamental mathematical relationships that connect linear quantities — such as displacement $s$, velocity $v$, and acceleration $a$ — to their angular counterparts — angular displacement $\theta$, angular velocity $\omega$, and angular acceleration $\alpha$. Understanding these relationships is essential because it allows us to apply familiar linear kinematics equations to rotating systems, which is the foundation for studying [[Centripetal Acceleration and Force]] and circular motion dynamics. This sub-topic is the "translation layer" between the linear world and the rotational world.

**中文:**
本子知识点搭建了直线运动与旋转运动之间的桥梁。它建立了连接线性量（如位移 $s$、速度 $v$、加速度 $a$）与角量（角位移 $\theta$、角速度 $\omega$、角加速度 $\alpha$）的基本数学关系。理解这些关系至关重要，因为它使我们能够将熟悉的线性运动学方程应用于旋转系统，这是学习[[Centripetal Acceleration and Force]]和圆周运动动力学的基础。本子知识点是线性世界与旋转世界之间的"翻译层"。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Arc Length** / 弧长 | The distance $s$ measured along the circumference of a circle, subtended by an angle $\theta$ at the centre. | 沿圆周测量的距离 $s$，由圆心角 $\theta$ 所对。 |
| **Linear Velocity** / 线速度 | The instantaneous rate of change of linear displacement of a point on a rotating object, tangent to the circular path. | 旋转物体上某点的线性位移的瞬时变化率，方向沿圆周的切线方向。 |
| **Tangential Acceleration** / 切向加速度 | The component of acceleration that changes the magnitude of linear velocity, directed tangent to the circular path. | 改变线速度大小的加速度分量，方向沿圆周的切线方向。 |
| **Radius of Rotation** / 旋转半径 | The fixed distance $r$ from the centre of rotation to the point of interest on the rotating body. | 从旋转中心到旋转体上感兴趣点的固定距离 $r$。 |
| **Angular-Linear Bridge** / 角-线桥梁 | The set of equations $s = r\theta$, $v = r\omega$, and $a = r\alpha$ that connect linear and angular quantities. | 连接线性量与角量的一组方程 $s = r\theta$, $v = r\omega$, $a = r\alpha$。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core idea is that every point on a rigid rotating body shares the same angular quantities ($\theta$, $\omega$, $\alpha$) but has different linear quantities ($s$, $v$, $a$) depending on its distance $r$ from the centre of rotation.

**Step-by-step reasoning:**
1. **Arc Length Relationship:** When a rigid body rotates through an angle $\theta$ (in radians), a point at radius $r$ travels an arc length $s = r\theta$. This is derived directly from the definition of the radian: $\theta = s/r$.
2. **Linear Velocity Relationship:** Differentiating $s = r\theta$ with respect to time gives $v = r\omega$. The linear velocity is tangential to the circular path — it is not directed radially.
3. **Tangential Acceleration Relationship:** Differentiating $v = r\omega$ with respect to time gives $a = r\alpha$. This is the *tangential* acceleration, which changes the *speed* of the point. It is distinct from [[Centripetal Acceleration and Force|centripetal acceleration]], which changes the *direction* of velocity.

**Physical Interpretation:**
- A point farther from the centre (larger $r$) moves faster linearly for the same angular velocity — think of the outer edge of a spinning disc.
- The linear velocity vector is always tangent to the circle, while the angular velocity vector points along the axis of rotation (right-hand rule).

**Common Pitfalls:**
- **Confusing tangential and centripetal acceleration:** $a = r\alpha$ gives tangential acceleration (changes speed), NOT centripetal acceleration ($a_c = v^2/r = \omega^2 r$).
- **Forgetting radians:** These relationships only work when $\theta$ is measured in radians, not degrees.
- **Assuming $v$ is radial:** Linear velocity in circular motion is tangential, not radial.

**中文:**
核心思想是：刚体上的每个点共享相同的角量（$\theta$, $\omega$, $\alpha$），但根据其到旋转中心的距离 $r$ 不同，具有不同的线性量（$s$, $v$, $a$）。

**逐步推理：**
1. **弧长关系：** 当刚体旋转角度 $\theta$（弧度）时，半径为 $r$ 的点经过的弧长 $s = r\theta$。这直接来自弧度的定义：$\theta = s/r$。
2. **线速度关系：** 对 $s = r\theta$ 关于时间求导，得到 $v = r\omega$。线速度沿圆周的切线方向——不是径向的。
3. **切向加速度关系：** 对 $v = r\omega$ 关于时间求导，得到 $a = r\alpha$。这是*切向*加速度，改变速度的*大小*。它与[[Centripetal Acceleration and Force|向心加速度]]不同，后者改变速度的*方向*。

**物理解释：**
- 离中心较远的点（较大的 $r$）在相同角速度下移动得更快——想想旋转圆盘的外缘。
- 线速度矢量始终与圆相切，而角速度矢量沿旋转轴方向（右手定则）。

**常见错误：**
- **混淆切向加速度和向心加速度：** $a = r\alpha$ 给出切向加速度（改变速度大小），而不是向心加速度（$a_c = v^2/r = \omega^2 r$）。
- **忘记弧度：** 这些关系仅在 $\theta$ 以弧度测量时才成立，度数不行。
- **假设 $v$ 是径向的：** 圆周运动中的线速度是切向的，不是径向的。

---

# 4. Formulas / 公式

## Primary Bridge Equations / 主要桥梁方程

$$ s = r\theta $$

$$ v = r\omega $$

$$ a_t = r\alpha $$

Where $a_t$ is tangential acceleration (not centripetal).

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $s$ | Arc length (linear displacement along path) | 弧长（沿路径的线性位移） | m |
| $r$ | Radius of rotation | 旋转半径 | m |
| $\theta$ | Angular displacement | 角位移 | rad |
| $v$ | Linear (tangential) velocity | 线（切向）速度 | m s⁻¹ |
| $\omega$ | Angular velocity | 角速度 | rad s⁻¹ |
| $a_t$ | Tangential acceleration | 切向加速度 | m s⁻² |
| $\alpha$ | Angular acceleration | 角加速度 | rad s⁻² |

## Derived Relationships / 导出关系

$$ v = \frac{2\pi r}{T} = 2\pi r f $$

$$ a_c = \frac{v^2}{r} = \omega^2 r $$

(Note: $a_c$ is centripetal acceleration, covered in [[Centripetal Acceleration and Force]])

**Derivation / 推导:**
Starting from the definition of the radian: $\theta = \frac{s}{r}$.
Multiply both sides by $r$: $s = r\theta$.
Differentiate with respect to time: $\frac{ds}{dt} = r\frac{d\theta}{dt}$, giving $v = r\omega$.
Differentiate again: $\frac{dv}{dt} = r\frac{d\omega}{dt}$, giving $a_t = r\alpha$.

**Conditions / 适用条件:**
- $\theta$ must be in radians (not degrees).
- The body must be rigid (all points share the same $\omega$ and $\alpha$).
- For $v = r\omega$, the motion can be uniform or non-uniform circular motion.
- For $a_t = r\alpha$, the angular acceleration must be constant or instantaneous.

> 📷 **IMAGE PROMPT — BRIDGE-01: Angular-Linear Relationship Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a rotating disc with a point P at radius r from centre O. The disc rotates through angle θ. Show: (1) arc length s traced by point P along the circumference, labelled clearly; (2) tangential velocity vector v at point P, drawn as an arrow tangent to the circle; (3) radius r drawn from O to P. Use a colour scheme: blue for linear quantities (s, v), red for angular quantities (θ, ω). Include a small callout box showing the three bridge equations: s = rθ, v = rω, a = rα. White background, clean sans-serif font, suitable for A-Level textbook.
>
> **中文描述:**
> 一个清晰、教科书风格的矢量图，显示一个旋转圆盘，点P位于距中心O半径r处。圆盘旋转角度θ。显示：(1) 点P沿圆周经过的弧长s，清晰标注；(2) 点P处的切向速度矢量v，绘制为与圆相切的箭头；(3) 从O到P的半径r。使用配色方案：蓝色表示线性量（s, v），红色表示角量（θ, ω）。包含一个小标注框，显示三个桥梁方程：s = rθ, v = rω, a = rα。白色背景，干净的无衬线字体，适合A-Level教科书。
>
> **Labels Required / 需要标注:**
> * Centre O / 中心 O
> * Radius r / 半径 r
> * Point P / 点 P
> * Arc length s / 弧长 s
> * Angular displacement θ / 角位移 θ
> * Tangential velocity v / 切向速度 v
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding how to translate between linear and angular quantities. Exam questions often ask students to identify which quantity is which on a diagram.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — BRIDGE-02: Tangential vs Centripetal Acceleration Comparison**
>
> **English Prompt:**
> A split-panel vector diagram comparing tangential acceleration and centripetal acceleration for a point on a rotating disc. Left panel: a disc with angular acceleration α, showing tangential acceleration vector a_t (arrow tangent to circle) and the direction of increasing speed. Right panel: the same disc in uniform circular motion (constant ω), showing centripetal acceleration vector a_c (arrow pointing radially inward toward centre O). Use arrows of different colours: green for a_t, red for a_c. Include equation callouts: a_t = rα on left, a_c = v²/r = ω²r on right. White background, clean sans-serif font, suitable for A-Level textbook.
>
> **中文描述:**
> 一个分屏矢量图，比较旋转圆盘上某点的切向加速度和向心加速度。左面板：具有角加速度α的圆盘，显示切向加速度矢量a_t（与圆相切的箭头）和速度增加的方向。右面板：相同圆盘在匀速圆周运动中（恒定ω），显示向心加速度矢量a_c（指向中心O的径向箭头）。使用不同颜色的箭头：绿色表示a_t，红色表示a_c。包含方程标注：左侧为a_t = rα，右侧为a_c = v²/r = ω²r。白色背景，干净的无衬线字体，适合A-Level教科书。
>
> **Labels Required / 需要标注:**
> * Tangential acceleration a_t / 切向加速度 a_t
> * Centripetal acceleration a_c / 向心加速度 a_c
> * Centre O / 中心 O
> * Direction of motion / 运动方向
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> Students frequently confuse tangential and centripetal acceleration. This comparison diagram clarifies the distinction, which is a common exam question topic.

---

# 6. Worked Example / 典型例题

### Example 1: Linear Speed of a Point on a Rotating Disc

### Question / 题目
**English:**
A disc of radius 0.25 m rotates at a constant angular velocity of 12 rad s⁻¹. Calculate:
(a) The linear speed of a point on the rim of the disc.
(b) The linear speed of a point 0.10 m from the centre.

**中文:**
一个半径为0.25 m的圆盘以12 rad s⁻¹的恒定角速度旋转。计算：
(a) 圆盘边缘上一点的线速度。
(b) 距中心0.10 m处一点的线速度。

### Solution / 解答

**(a)** Using $v = r\omega$:
$$ v = (0.25)(12) = 3.0 \text{ m s}^{-1} $$

**(b)** Using $v = r\omega$ with $r = 0.10$ m:
$$ v = (0.10)(12) = 1.2 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** (a) 3.0 m s⁻¹ (b) 1.2 m s⁻¹
**答案:** (a) 3.0 m s⁻¹ (b) 1.2 m s⁻¹

### Quick Tip / 提示
Notice that the point closer to the centre has a lower linear speed, even though the angular velocity is the same. This is a key concept: linear quantities depend on $r$, angular quantities do not.

---

### Example 2: Tangential Acceleration from Angular Acceleration

### Question / 题目
**English:**
A wheel of radius 0.40 m starts from rest and accelerates uniformly at 2.5 rad s⁻². Calculate:
(a) The tangential acceleration of a point on the rim.
(b) The linear speed of that point after 3.0 seconds.

**中文:**
一个半径为0.40 m的车轮从静止开始，以2.5 rad s⁻²的角加速度匀加速旋转。计算：
(a) 边缘上一点的切向加速度。
(b) 3.0秒后该点的线速度。

### Solution / 解答

**(a)** Using $a_t = r\alpha$:
$$ a_t = (0.40)(2.5) = 1.0 \text{ m s}^{-2} $$

**(b)** First find angular velocity after 3.0 s using $\omega = \omega_0 + \alpha t$:
$$ \omega = 0 + (2.5)(3.0) = 7.5 \text{ rad s}^{-1} $$

Then find linear speed using $v = r\omega$:
$$ v = (0.40)(7.5) = 3.0 \text{ m s}^{-1} $$

### Final Answer / 最终答案
**Answer:** (a) 1.0 m s⁻² (b) 3.0 m s⁻¹
**答案:** (a) 1.0 m s⁻² (b) 3.0 m s⁻¹

### Quick Tip / 提示
You can also solve part (b) using linear kinematics: $v = u + a_t t = 0 + (1.0)(3.0) = 3.0$ m s⁻¹. Both methods give the same answer — this shows the power of the bridge equations!

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the relationship between arc length s and angular displacement θ?
Q (CN): 弧长 s 和角位移 θ 之间的关系是什么？
A (EN): s = rθ, where r is the radius of rotation. θ must be in radians.
A (CN): s = rθ，其中 r 是旋转半径。θ 必须以弧度为单位。

**Flashcard 2:**
Q (EN): How is linear (tangential) velocity v related to angular velocity ω?
Q (CN): 线（切向）速度 v 与角速度 ω 有何关系？
A (EN): v = rω. The linear velocity is tangent to the circular path.
A (CN): v = rω。线速度沿圆周的切线方向。

**Flashcard 3:**
Q (EN): What does a = rα represent, and what does it NOT represent?
Q (CN): a = rα 代表什么，它不代表什么？
A (EN): It represents tangential acceleration (change in speed). It does NOT represent centripetal acceleration (change in direction).
A (CN): 它代表切向加速度（速度大小的变化）。它不代表向心加速度（速度方向的变化）。

**Flashcard 4:**
Q (EN): A point on a rotating disc has angular velocity ω. If the point is moved to twice the radius, what happens to its linear speed?
Q (CN): 旋转圆盘上的一点具有角速度 ω。如果将该点移动到两倍半径处，其线速度会如何变化？
A (EN): The linear speed doubles, because v = rω and r has doubled while ω remains the same.
A (CN): 线速度加倍，因为 v = rω，r 加倍而 ω 保持不变。

**Flashcard 5:**
Q (EN): What condition must be satisfied for the bridge equations s = rθ, v = rω, and a = rα to be valid?
Q (CN): 桥梁方程 s = rθ, v = rω, a = rα 成立需要满足什么条件？
A (EN): θ must be measured in radians (not degrees), and the body must be rigid.
A (CN): θ 必须以弧度（而非度数）测量，且物体必须是刚体。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Relationship Between Linear and Angular Quantities"
  cn: "线性量与角量之间的关系"
parent_topic: "Angular Measures"
parent_hub: "[[Angular Measures]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Radians and Angular Displacement]]"
  - "[[Angular Velocity]]"
  - "[[Period and Frequency]]"
  - "[[Centripetal Acceleration and Force]]"
prerequisites:
  - "[[Displacement, Velocity and Acceleration]]"
language: bilingual_en_cn