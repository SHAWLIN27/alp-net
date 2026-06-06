# 1. Overview / 概述

**English:**
Angular velocity is a fundamental concept in rotational mechanics, describing how quickly an object rotates or revolves around a fixed axis. This sub-topic introduces the definition, calculation, and physical interpretation of angular velocity ($\omega$), which is the rotational analogue of linear velocity. Understanding angular velocity is essential for analyzing circular motion, from spinning wheels to planetary orbits. It forms the core of the [[Angular Measures]] hub and directly connects to [[Centripetal Acceleration and Force]], where angular velocity determines the required centripetal force for uniform circular motion.

**中文:**
角速度是旋转力学中的基本概念，描述物体绕固定轴旋转或公转的快慢。本子知识点介绍角速度 ($\omega$) 的定义、计算和物理意义，它是线速度在旋转运动中的对应量。理解角速度对于分析圆周运动至关重要，从旋转的车轮到行星轨道。它是 [[Angular Measures]] 知识枢纽的核心，并直接连接到 [[Centripetal Acceleration and Force]]，其中角速度决定了匀速圆周运动所需的向心力。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Angular Velocity** / 角速度 | The rate of change of angular displacement with respect to time, measured in radians per second (rad s⁻¹). | 角位移随时间的变化率，单位为弧度每秒 (rad s⁻¹)。 |
| **Uniform Angular Velocity** / 匀角速度 | Constant angular velocity where equal angular displacements occur in equal time intervals. | 恒定角速度，在相等时间间隔内发生相等的角位移。 |
| **Instantaneous Angular Velocity** / 瞬时角速度 | The angular velocity at a specific instant, given by the limit of $\Delta\theta/\Delta t$ as $\Delta t \to 0$. | 某一特定时刻的角速度，由 $\Delta\theta/\Delta t$ 在 $\Delta t \to 0$ 时的极限给出。 |
| **Direction of Angular Velocity** / 角速度方向 | Determined by the right-hand rule: fingers curl in direction of rotation, thumb points along axis of rotation. | 由右手定则确定：手指弯曲方向为旋转方向，拇指指向旋转轴方向。 |
| **Mean Angular Velocity** / 平均角速度 | Total angular displacement divided by total time taken: $\bar{\omega} = \Delta\theta/\Delta t$. | 总角位移除以总时间：$\bar{\omega} = \Delta\theta/\Delta t$。 |

---

# 3. Key Concepts / 关键概念

**English:**
Angular velocity ($\omega$) is the rotational counterpart to linear velocity ($v$). While linear velocity describes how fast an object changes its position along a straight line, angular velocity describes how fast an object changes its angular position around a fixed axis.

**Definition and Calculation:**
The fundamental definition is:
$$\omega = \frac{d\theta}{dt}$$

For uniform circular motion, where angular velocity is constant:
$$\omega = \frac{\Delta\theta}{\Delta t}$$

**Physical Interpretation:**
- A larger $\omega$ means the object rotates faster
- $\omega$ is a vector quantity (direction given by right-hand rule)
- In A-Level physics, we typically consider magnitude only for uniform circular motion
- Angular velocity is directly related to [[Period and Frequency]]: $\omega = 2\pi f = \frac{2\pi}{T}$

**Common Pitfalls:**
1. **Confusing angular velocity with linear velocity**: Angular velocity describes rotation rate, not speed along a circular path
2. **Forgetting units**: Always use radians per second (rad s⁻¹), not degrees per second
3. **Direction confusion**: For A-Level, focus on magnitude unless specifically asked about vector nature
4. **Mixing with frequency**: Angular velocity ($\omega$) and frequency ($f$) are related but distinct — $\omega = 2\pi f$

**Connection to Prerequisites:**
Angular velocity builds on the concept of [[Displacement, Velocity and Acceleration]] from linear motion. The key difference is that angular displacement replaces linear displacement, and the rate of change of angular displacement gives angular velocity instead of linear velocity.

**中文:**
角速度 ($\omega$) 是线速度 ($v$) 在旋转运动中的对应量。线速度描述物体沿直线改变位置的速度，而角速度描述物体绕固定轴改变角位置的速度。

**定义与计算:**
基本定义为：
$$\omega = \frac{d\theta}{dt}$$

对于匀速圆周运动，角速度恒定：
$$\omega = \frac{\Delta\theta}{\Delta t}$$

**物理意义:**
- $\omega$ 越大，物体旋转越快
- $\omega$ 是矢量（方向由右手定则确定）
- 在A-Level物理中，对于匀速圆周运动通常只考虑大小
- 角速度与[[Period and Frequency]]直接相关：$\omega = 2\pi f = \frac{2\pi}{T}$

**常见错误:**
1. **混淆角速度与线速度**：角速度描述旋转速率，而非沿圆周路径的速度
2. **忘记单位**：始终使用弧度每秒 (rad s⁻¹)，而非度每秒
3. **方向混淆**：除非特别问到矢量性质，A-Level中关注大小
4. **与频率混淆**：角速度 ($\omega$) 和频率 ($f$) 相关但不同 — $\omega = 2\pi f$

**与先修知识的联系:**
角速度建立在[[Displacement, Velocity and Acceleration]]的线运动概念之上。关键区别在于角位移取代了线位移，角位移的变化率给出角速度而非线速度。

---

# 4. Formulas / 公式

## Primary Formula / 主要公式

$$\omega = \frac{\Delta\theta}{\Delta t}$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\omega$ | Angular velocity | 角速度 | rad s⁻¹ |
| $\Delta\theta$ | Angular displacement | 角位移 | rad |
| $\Delta t$ | Time interval | 时间间隔 | s |

## Relationship with Period and Frequency / 与周期和频率的关系

$$\omega = \frac{2\pi}{T} = 2\pi f$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T$ | Period | 周期 | s |
| $f$ | Frequency | 频率 | Hz |

## Instantaneous Angular Velocity / 瞬时角速度

$$\omega = \frac{d\theta}{dt}$$

**Derivation / 推导:**
The instantaneous angular velocity is the limit of the average angular velocity as the time interval approaches zero:
$$\omega = \lim_{\Delta t \to 0} \frac{\Delta\theta}{\Delta t} = \frac{d\theta}{dt}$$

**Conditions / 适用条件:**
- The formula $\omega = \Delta\theta/\Delta t$ applies for **uniform** angular velocity (constant $\omega$)
- For non-uniform rotation, use $\omega = d\theta/dt$ for instantaneous values
- Angular displacement must be measured in **radians**, not degrees
- The axis of rotation must be fixed

> 📷 **IMAGE PROMPT — AV01: Angular Velocity Definition Diagram**
>
> **English Prompt:**
> A clean textbook-style vector diagram showing a rotating object (a small circle) moving along a circular path of radius r. The center of the circle is marked O. The object at two positions: position 1 at angle θ₁ and position 2 at angle θ₂, with angular displacement Δθ = θ₂ - θ₁ marked clearly. An arc arrow shows the direction of rotation. A clock icon nearby indicates time interval Δt. Labels: "Angular velocity ω = Δθ/Δt" at the bottom. White background, blue and black lines, professional physics textbook style.
>
> **中文描述:**
> 一个清晰的教科书风格矢量图，显示一个旋转物体（小圆）沿半径为r的圆周路径运动。圆心标记为O。物体在两个位置：位置1在角度θ₁，位置2在角度θ₂，角位移Δθ = θ₂ - θ₁清晰标注。弧线箭头显示旋转方向。旁边的时钟图标表示时间间隔Δt。底部标签："角速度 ω = Δθ/Δt"。白色背景，蓝色和黑色线条，专业物理教科书风格。
>
> **Labels Required / 需要标注:**
> * O (center of circle / 圆心)
> * θ₁, θ₂ (angular positions / 角位置)
> * Δθ (angular displacement / 角位移)
> * r (radius / 半径)
> * ω = Δθ/Δt (angular velocity / 角速度)
>
> **Style / 风格:** Textbook vector / 教科书矢量图
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding the definition of angular velocity and appears in many exam questions about circular motion.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — AV02: Right-Hand Rule for Angular Velocity Direction**
>
> **English Prompt:**
> A 3D rendered diagram showing a rotating disk (blue) with its axis of rotation (vertical dashed line). A hand illustration (simplified) shows the right-hand rule: fingers curl in the direction of rotation (clockwise or anticlockwise), thumb points upward along the axis. The angular velocity vector ω is shown as a red arrow pointing along the axis. Labels: "ω (angular velocity)", "Axis of rotation", "Direction of rotation". Clean white background, professional 3D render style suitable for physics textbooks.
>
> **中文描述:**
> 一个3D渲染图，显示一个旋转圆盘（蓝色）及其旋转轴（垂直虚线）。一个简化手部插图展示右手定则：手指弯曲方向为旋转方向，拇指沿轴向上。角速度矢量ω显示为沿轴的红色箭头。标签："ω (角速度)"、"旋转轴"、"旋转方向"。干净的白色背景，适合物理教科书的专业3D渲染风格。
>
> **Labels Required / 需要标注:**
> * ω (angular velocity vector / 角速度矢量)
> * Axis of rotation / 旋转轴
> * Direction of rotation / 旋转方向
>
> **Style / 风格:** 3D render / 3D渲染
>
> **Exam Relevance / 考试关联:**
> Understanding the vector nature of angular velocity is important for advanced topics like angular momentum and gyroscopic motion.

---

# 6. Worked Example / 典型例题

### Example 1: Calculating Angular Velocity from Period / 从周期计算角速度

### Question / 题目
**English:**
A ceiling fan rotates at a constant speed, completing one full revolution every 0.50 seconds. Calculate the angular velocity of the fan in rad s⁻¹.

**中文:**
一台吊扇匀速旋转，每0.50秒完成一整圈。计算吊扇的角速度，单位为rad s⁻¹。

### Solution / 解答

**Step 1:** Identify known quantities
- Period $T = 0.50$ s
- One full revolution = $2\pi$ radians

**Step 2:** Use the relationship between angular velocity and period
$$\omega = \frac{2\pi}{T}$$

**Step 3:** Substitute values
$$\omega = \frac{2\pi}{0.50}$$

**Step 4:** Calculate
$$\omega = 4\pi = 12.57 \text{ rad s}^{-1}$$

### Final Answer / 最终答案
**Answer:** $\omega = 12.6$ rad s⁻¹ (3 s.f.) **答案:** $\omega = 12.6$ rad s⁻¹ (3位有效数字)

### Quick Tip / 提示
Remember that one complete revolution equals $2\pi$ radians, not 360 degrees. Always convert to radians when using angular velocity formulas.

---

### Example 2: Finding Angular Displacement / 求角位移

### Question / 题目
**English:**
A spinning top has an angular velocity of 8.0 rad s⁻¹. Through what angle does it rotate in 2.5 seconds? Give your answer in radians and degrees.

**中文:**
一个旋转陀螺的角速度为8.0 rad s⁻¹。它在2.5秒内旋转了多少角度？以弧度和度为单位给出答案。

### Solution / 解答

**Step 1:** Identify known quantities
- $\omega = 8.0$ rad s⁻¹
- $\Delta t = 2.5$ s

**Step 2:** Use the definition of angular velocity
$$\omega = \frac{\Delta\theta}{\Delta t}$$

**Step 3:** Rearrange for angular displacement
$$\Delta\theta = \omega \times \Delta t$$

**Step 4:** Substitute values
$$\Delta\theta = 8.0 \times 2.5 = 20 \text{ rad}$$

**Step 5:** Convert to degrees
$$1 \text{ rad} = \frac{180^\circ}{\pi}$$
$$\Delta\theta = 20 \times \frac{180^\circ}{\pi} = 1146^\circ$$

### Final Answer / 最终答案
**Answer:** $\Delta\theta = 20$ rad = $1.15 \times 10^3$ degrees (3 s.f.) **答案:** $\Delta\theta = 20$ rad = $1.15 \times 10^3$ 度 (3位有效数字)

### Quick Tip / 提示
When converting between radians and degrees, use $1 \text{ rad} = 180^\circ/\pi \approx 57.3^\circ$. For A-Level, always give final answers in radians unless the question specifically asks for degrees.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is angular velocity and what are its SI units?
Q (CN): 什么是角速度？它的SI单位是什么？
A (EN): Angular velocity is the rate of change of angular displacement with respect to time. Its SI unit is rad s⁻¹ (radians per second).
A (CN): 角速度是角位移随时间的变化率。它的SI单位是rad s⁻¹（弧度每秒）。

**Flashcard 2:**
Q (EN): Write the formula relating angular velocity to period and frequency.
Q (CN): 写出角速度与周期和频率的关系公式。
A (EN): $\omega = \frac{2\pi}{T} = 2\pi f$
A (CN): $\omega = \frac{2\pi}{T} = 2\pi f$

**Flashcard 3:**
Q (EN): How do you determine the direction of angular velocity?
Q (CN): 如何确定角速度的方向？
A (EN): Using the right-hand rule: curl fingers in the direction of rotation, thumb points along the axis in the direction of angular velocity.
A (CN): 使用右手定则：手指弯曲方向为旋转方向，拇指指向轴的方向即为角速度方向。

**Flashcard 4:**
Q (EN): A wheel rotates through 3π radians in 1.5 seconds. Calculate its angular velocity.
Q (CN): 一个轮子在1.5秒内旋转了3π弧度。计算其角速度。
A (EN): $\omega = \Delta\theta/\Delta t = 3\pi/1.5 = 2\pi$ rad s⁻¹
A (CN): $\omega = \Delta\theta/\Delta t = 3\pi/1.5 = 2\pi$ rad s⁻¹

**Flashcard 5:**
Q (EN): What is the difference between angular velocity and linear velocity?
Q (CN): 角速度和线速度有什么区别？
A (EN): Angular velocity describes the rate of change of angular displacement (rotation rate), while linear velocity describes the rate of change of linear position (speed along a path). They are related by $v = \omega r$.
A (CN): 角速度描述角位移的变化率（旋转速率），而线速度描述线性位置的变化率（沿路径的速度）。它们通过 $v = \omega r$ 相关联。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Angular Velocity
  cn: 角速度
parent_topic: Angular Measures
parent_hub: "[[Angular Measures]]"
subject: Physics
syllabus:
  - CAIE 9702: 14.1 (a-e)
  - Edexcel IAL: WPH14 U4: 5.1-5.4
level: A2
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Radians and Angular Displacement]]"
  - "[[Period and Frequency]]"
  - "[[Relationship Between Linear and Angular Quantities]]"
  - "[[Centripetal Acceleration and Force]]"
prerequisites:
  - "[[Displacement, Velocity and Acceleration]]"
language: bilingual_en_cn