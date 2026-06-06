# 1. Overview / 概述

**English:**
Centripetal Force is the net force required to keep an object moving in a circular path. Unlike "real" forces like gravity or tension, centripetal force is not a new type of force — it is the **resultant** of all forces acting towards the centre of the circle. This sub-topic explores how to identify and calculate the centripetal force in various physical scenarios, from a car turning a corner to a satellite orbiting Earth. Understanding centripetal force is essential for mastering [[Centripetal Acceleration and Force]] and connects directly to [[Banked Tracks and Conical Pendulum]] and [[Circular Orbits]].

**中文:**
向心力是使物体沿圆周运动所需的净力。与重力或张力等"真实"力不同，向心力并非一种新的力——它是所有指向圆心的力的**合力**。本子知识点探讨如何在各种物理场景中识别和计算向心力，从汽车转弯到卫星绕地球运行。理解向心力是掌握[[Centripetal Acceleration and Force]]的关键，并直接连接到[[Banked Tracks and Conical Pendulum]]和[[Circular Orbits]]。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Centripetal Force** / 向心力 | The net force acting towards the centre of a circular path that causes an object to undergo circular motion. | 指向圆心的净力，使物体做圆周运动。 |
| **Resultant Force** / 合力 | The vector sum of all forces acting on an object. | 作用在物体上所有力的矢量和。 |
| **Radial Direction** / 径向 | The direction pointing towards or away from the centre of the circle. | 指向或远离圆心的方向。 |
| **Tangential Direction** / 切向 | The direction perpendicular to the radial direction, tangent to the circular path. | 垂直于径向、与圆周路径相切的方向。 |
| **Centrifugal Force** / 离心力 | A fictitious force experienced in a rotating reference frame, pointing outward from the centre. | 在旋转参考系中感受到的假想力，指向远离圆心。 |

---

# 3. Key Concepts / 关键概念

**English:**
Centripetal force is **not** a new fundamental force — it is the **resultant** of existing forces. For example:
- A car turning: friction provides the centripetal force
- A satellite orbiting: gravity provides the centripetal force
- A ball on a string: tension provides the centripetal force

The key equation is $F = m a_c$, where $a_c$ is the [[Centripetal Acceleration Formula]]. Since $a_c = \frac{v^2}{r} = \omega^2 r$, we get:

$$F_c = \frac{mv^2}{r} = m\omega^2 r$$

**Common pitfalls:**
1. **Confusing centripetal force with centrifugal force** — centrifugal force is a fictitious force only apparent in rotating frames (e.g., feeling "pushed outward" in a car turning). In an inertial frame, only centripetal force exists.
2. **Forgetting that centripetal force is a resultant** — students often list "centripetal force" as a separate force in free-body diagrams. Instead, identify the real forces (tension, friction, gravity, normal reaction) and find their resultant towards the centre.
3. **Direction matters** — centripetal force always points towards the centre, perpendicular to velocity. It does **no work** because displacement is perpendicular to force.

**Connection to [[Newton's Laws of Motion]]:** Newton's Second Law ($F = ma$) applies directly — centripetal force is the net force causing centripetal acceleration.

**中文:**
向心力**不是**一种新的基本力——它是现有力的**合力**。例如：
- 汽车转弯：摩擦力提供向心力
- 卫星运行：重力提供向心力
- 绳子上的球：张力提供向心力

关键方程是 $F = m a_c$，其中 $a_c$ 是[[Centripetal Acceleration Formula]]。由于 $a_c = \frac{v^2}{r} = \omega^2 r$，我们得到：

$$F_c = \frac{mv^2}{r} = m\omega^2 r$$

**常见陷阱：**
1. **混淆向心力与离心力**——离心力是旋转参考系中的假想力（如转弯时感觉被"向外推"）。在惯性参考系中，只有向心力存在。
2. **忘记向心力是合力**——学生常在受力分析图中将"向心力"列为单独力。应识别真实力（张力、摩擦力、重力、法向反力）并找出指向圆心的合力。
3. **方向很重要**——向心力始终指向圆心，垂直于速度。它**不做功**，因为位移垂直于力。

**与[[Newton's Laws of Motion]]的联系：** 牛顿第二定律（$F = ma$）直接适用——向心力是引起向心加速度的净力。

---

# 4. Formulas / 公式

$$F_c = \frac{mv^2}{r} = m\omega^2 r$$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $F_c$ | Centripetal force | 向心力 | N |
| $m$ | Mass of object | 物体质量 | kg |
| $v$ | Linear speed | 线速度 | m/s |
| $r$ | Radius of circular path | 圆周半径 | m |
| $\omega$ | Angular speed | 角速度 | rad/s |

**Derivation / 推导:**
From Newton's Second Law: $F = ma$
From [[Centripetal Acceleration Formula]]: $a_c = \frac{v^2}{r} = \omega^2 r$
Therefore: $F_c = m \cdot \frac{v^2}{r} = m\omega^2 r$

**Conditions / 适用条件:**
- Object moves in uniform circular motion (constant speed)
- Valid in inertial reference frames only
- $F_c$ is the **net** force towards the centre, not an additional force

> 📷 **IMAGE PROMPT — FBD: Centripetal Force Free-Body Diagrams**
>
> **English Prompt:**
> A split-panel educational diagram showing three common scenarios of centripetal force. Left panel: a car turning on a flat road, with arrows showing friction (f) pointing towards the centre of the turn. Middle panel: a satellite orbiting Earth, with gravitational force (Fg) pointing towards Earth's centre. Right panel: a ball on a string swung in a vertical circle at the bottom position, with tension (T) upward and weight (mg) downward, net force upward. All arrows labelled with force names. Clean textbook vector style, white background, blue and red arrows.
>
> **中文描述:**
> 三面板教育示意图，展示向心力的三种常见场景。左面板：汽车在平路上转弯，箭头显示摩擦力（f）指向转弯中心。中面板：卫星绕地球运行，引力（Fg）指向地心。右面板：绳子上的球在竖直圆周最低点，张力（T）向上，重力（mg）向下，净力向上。所有箭头标注力名称。干净教科书矢量风格，白色背景，蓝色和红色箭头。
>
> **Labels Required / 需要标注:**
> * f (friction / 摩擦力)
> * Fg (gravitational force / 重力)
> * T (tension / 张力)
> * mg (weight / 重量)
> * Net F (resultant / 合力)
>
> **Style / 风格:** Textbook vector / 教科书矢量
>
> **Exam Relevance / 考试关联:**
> Students must correctly identify which real force(s) provide centripetal force in different scenarios — a common exam question.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — DIAGRAM: Centripetal vs Centrifugal Force**
>
> **English Prompt:**
> A comparison diagram showing two reference frames. Left side: inertial frame (outside the car) — a car turning left, with a single arrow labelled "Centripetal Force (Fc)" pointing towards the centre of the turn. Right side: rotating frame (inside the car) — the same car, but with a passenger feeling pushed to the right, with an arrow labelled "Centrifugal Force (fictitious)" pointing outward. Dashed line shows the circular path. Clean vector illustration, warm colours for centrifugal, cool colours for centripetal. Labels in English.
>
> **中文描述:**
> 对比图显示两个参考系。左侧：惯性系（车外）——汽车左转，单个箭头标注"向心力（Fc）"指向转弯中心。右侧：旋转系（车内）——同一辆车，乘客感觉被向右推，箭头标注"离心力（假想力）"指向外。虚线显示圆周路径。干净矢量图，暖色表示离心力，冷色表示向心力。英文标注。
>
> **Labels Required / 需要标注:**
> * Inertial Frame / 惯性参考系
> * Rotating Frame / 旋转参考系
> * Centripetal Force (Fc) / 向心力
> * Centrifugal Force (fictitious) / 离心力（假想力）
>
> **Style / 风格:** Textbook vector / 教科书矢量
>
> **Exam Relevance / 考试关联:**
> Exam questions often test understanding that centrifugal force is not real — this diagram clarifies the distinction.

---

# 6. Worked Example / 典型例题

### Example 1: Car Turning on a Flat Road

### Question / 题目
**English:** A car of mass 1200 kg travels around a circular bend of radius 50 m at a constant speed of 15 m/s. Calculate the centripetal force required. If the maximum frictional force between the tyres and the road is 6000 N, will the car skid?

**中文:** 一辆质量为1200 kg的汽车以15 m/s的恒定速度绕半径为50 m的圆形弯道行驶。计算所需的向心力。如果轮胎与路面之间的最大摩擦力为6000 N，汽车会打滑吗？

### Solution / 解答

**Step 1:** Identify the centripetal force formula.
$$F_c = \frac{mv^2}{r}$$

**Step 2:** Substitute values.
$$F_c = \frac{1200 \times (15)^2}{50}$$

**Step 3:** Calculate.
$$F_c = \frac{1200 \times 225}{50} = \frac{270000}{50} = 5400 \text{ N}$$

**Step 4:** Compare with maximum friction.
Maximum friction = 6000 N
Required centripetal force = 5400 N
Since 5400 N < 6000 N, the car will **not** skid.

### Final Answer / 最终答案
**Answer:** $F_c = 5400 \text{ N}$; No, the car will not skid. **答案:** $F_c = 5400 \text{ N}$；不，汽车不会打滑。

### Quick Tip / 提示
**English:** Friction provides the centripetal force for a car turning on a flat road. If the required centripetal force exceeds maximum friction, the car skids outward.
**中文:** 在平路上，摩擦力提供汽车转弯所需的向心力。如果所需向心力超过最大摩擦力，汽车会向外打滑。

---

### Example 2: Satellite in Orbit

### Question / 题目
**English:** A satellite of mass 500 kg orbits Earth at a radius of 7000 km from Earth's centre. The gravitational force on the satellite is 4000 N. Calculate the orbital speed of the satellite.

**中文:** 一颗质量为500 kg的卫星在距地心7000 km的轨道上运行。卫星受到的引力为4000 N。计算卫星的轨道速度。

### Solution / 解答

**Step 1:** For a satellite, gravity provides the centripetal force.
$$F_g = F_c = \frac{mv^2}{r}$$

**Step 2:** Rearrange for $v$.
$$v = \sqrt{\frac{F_c \cdot r}{m}}$$

**Step 3:** Convert radius to metres.
$$r = 7000 \text{ km} = 7.0 \times 10^6 \text{ m}$$

**Step 4:** Substitute values.
$$v = \sqrt{\frac{4000 \times 7.0 \times 10^6}{500}}$$

**Step 5:** Calculate.
$$v = \sqrt{\frac{2.8 \times 10^{10}}{500}} = \sqrt{5.6 \times 10^7} = 7483 \text{ m/s}$$

### Final Answer / 最终答案
**Answer:** $v = 7480 \text{ m/s}$ (3 s.f.) **答案:** $v = 7480 \text{ m/s}$（3位有效数字）

### Quick Tip / 提示
**English:** In orbital problems, the centripetal force is always provided by gravity. Remember to convert km to m.
**中文:** 在轨道问题中，向心力始终由重力提供。记得将km转换为m。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is centripetal force?
Q (CN): 什么是向心力？
A (EN): The net force acting towards the centre of a circular path that causes an object to undergo circular motion. It is not a separate force but the resultant of real forces.
A (CN): 指向圆心的净力，使物体做圆周运动。它不是单独的力，而是真实力的合力。

**Flashcard 2:**
Q (EN): Write the two formulas for centripetal force.
Q (CN): 写出向心力的两个公式。
A (EN): $F_c = \frac{mv^2}{r}$ and $F_c = m\omega^2 r$
A (CN): $F_c = \frac{mv^2}{r}$ 和 $F_c = m\omega^2 r$

**Flashcard 3:**
Q (EN): Is centrifugal force a real force? Explain.
Q (CN): 离心力是真实力吗？解释。
A (EN): No, centrifugal force is a fictitious force experienced in a rotating reference frame. In an inertial frame, only centripetal force exists.
A (CN): 不是，离心力是旋转参考系中感受到的假想力。在惯性参考系中，只有向心力存在。

**Flashcard 4:**
Q (EN): What provides the centripetal force for a car turning on a flat road?
Q (CN): 汽车在平路上转弯时，什么提供向心力？
A (EN): Friction between the tyres and the road.
A (CN): 轮胎与路面之间的摩擦力。

**Flashcard 5:**
Q (EN): Does centripetal force do work on an object in circular motion? Why?
Q (CN): 向心力对做圆周运动的物体做功吗？为什么？
A (EN): No, because centripetal force is always perpendicular to the direction of motion (velocity), so work done $W = Fd\cos 90^\circ = 0$.
A (CN): 不做功，因为向心力始终垂直于运动方向（速度），所以做功 $W = Fd\cos 90^\circ = 0$。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Centripetal Force"
  cn: "向心力"
parent_topic: "Centripetal Acceleration and Force"
parent_hub: "[[Centripetal Acceleration and Force]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: A2
node_type: leaf_concept
difficulty: advanced
related_leaf_nodes:
  - "[[Centripetal Acceleration Formula]]"
  - "[[Banked Tracks and Conical Pendulum]]"
  - "[[Circular Orbits]]"
prerequisites:
  - "[[Angular Measures]]"
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn