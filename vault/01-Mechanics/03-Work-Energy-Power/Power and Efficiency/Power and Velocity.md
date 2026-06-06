# 1. Overview / 概述

**English:**
This sub-topic explores the direct relationship between **power** and **velocity** — a crucial concept for understanding how vehicles, engines, and moving objects transfer energy. When an object moves at constant velocity under a constant driving force, the power output is simply the product of that force and the velocity. This relationship, $P = Fv$, is derived from the definition of power ($P = W/t$) and the definition of work done ($W = Fs$). Understanding this link allows you to analyse real-world systems like cars climbing hills, boats moving through water, or aircraft in flight. This sub-topic builds directly on [[Work Done by a Force]] and [[Conservation of Energy]], and is a sibling to [[Definition of Power]] and [[Efficiency of Energy Transfers]] within the [[Power and Efficiency]] hub.

**中文:**
本子知识点探讨**功率**与**速度**之间的直接关系——这是理解车辆、发动机和运动物体如何传递能量的关键概念。当一个物体在恒定驱动力下以恒定速度运动时，输出功率就是该力与速度的乘积。这个关系 $P = Fv$ 是从功率的定义 ($P = W/t$) 和做功的定义 ($W = Fs$) 推导出来的。理解这一联系使您能够分析现实世界中的系统，例如汽车爬坡、船只在水中移动或飞机飞行。本子知识点直接建立在[[Work Done by a Force]]和[[Conservation of Energy]]的基础上，是[[Power and Efficiency]]知识库中[[Definition of Power]]和[[Efficiency of Energy Transfers]]的兄弟知识点。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Power** / 功率 | The rate at which work is done or energy is transferred. | 做功或能量传递的速率。 |
| **Velocity** / 速度 | The rate of change of displacement; a vector quantity with both magnitude and direction. | 位移的变化率；具有大小和方向的矢量。 |
| **Driving Force** / 驱动力 | The net force that propels an object forward, overcoming resistive forces. | 推动物体前进、克服阻力的净力。 |
| **Resistive Force** / 阻力 | Forces that oppose motion, such as friction, air resistance, or drag. | 阻碍运动的力，如摩擦力、空气阻力或阻力。 |
| **Constant Velocity** / 恒定速度 | Motion where speed and direction remain unchanged; net force is zero. | 速度和方向保持不变的运动；净力为零。 |
| **Instantaneous Power** / 瞬时功率 | The power delivered at a specific instant in time, given by $P = Fv$ when $F$ is the instantaneous force and $v$ is the instantaneous velocity. | 在特定瞬间传递的功率，由 $P = Fv$ 给出，其中 $F$ 是瞬时力，$v$ 是瞬时速度。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core relationship $P = Fv$ is derived from the fundamental definitions:

1. **From work and time:** Power is defined as $P = \frac{W}{t}$, where $W$ is work done and $t$ is time.
2. **From force and displacement:** Work done by a constant force is $W = Fs$, where $s$ is displacement in the direction of the force.
3. **Combining:** $P = \frac{Fs}{t} = F \cdot \frac{s}{t} = Fv$

**Important interpretations:**
- **Constant velocity case:** When an object moves at constant velocity, the driving force exactly balances the total resistive force (from [[Conservation of Energy]], no net work is done on the object's kinetic energy). The power output of the engine is $P = F_{\text{drive}} v = F_{\text{resistive}} v$.
- **Variable velocity case:** If velocity is changing, $P = Fv$ gives the **instantaneous power** at that moment. The force $F$ is the net force in the direction of motion.
- **Maximum power:** Many engines have a maximum power output. If $P_{\text{max}}$ is constant, then as velocity increases, the maximum possible driving force decreases ($F = P_{\text{max}}/v$). This explains why vehicles have lower acceleration at higher speeds.

**Common pitfalls:**
- Confusing $P = Fv$ with $P = F \times \text{speed}$ — remember $v$ is velocity in the direction of the force.
- Forgetting that $F$ must be the force **in the direction of motion**.
- Applying $P = Fv$ when the force is not constant — it gives instantaneous power only.

**中文:**
核心关系 $P = Fv$ 是从基本定义推导出来的：

1. **从功和时间出发：** 功率定义为 $P = \frac{W}{t}$，其中 $W$ 是做功，$t$ 是时间。
2. **从力和位移出发：** 恒力做功为 $W = Fs$，其中 $s$ 是力方向上的位移。
3. **结合：** $P = \frac{Fs}{t} = F \cdot \frac{s}{t} = Fv$

**重要解释：**
- **恒定速度情况：** 当物体以恒定速度运动时，驱动力恰好平衡总阻力（根据[[Conservation of Energy]]，没有净功作用于物体的动能）。发动机的输出功率为 $P = F_{\text{驱动}} v = F_{\text{阻力}} v$。
- **变速情况：** 如果速度在变化，$P = Fv$ 给出该时刻的**瞬时功率**。力 $F$ 是运动方向上的净力。
- **最大功率：** 许多发动机有最大功率输出。如果 $P_{\text{max}}$ 恒定，那么随着速度增加，最大可能的驱动力会减小 ($F = P_{\text{max}}/v$)。这解释了为什么车辆在高速时加速度较低。

**常见陷阱：**
- 混淆 $P = Fv$ 与 $P = F \times \text{速率}$ — 记住 $v$ 是力方向上的速度。
- 忘记 $F$ 必须是**运动方向上**的力。
- 当力不恒定时应用 $P = Fv$ — 它只给出瞬时功率。

---

# 4. Formulas / 公式

$$ P = Fv $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $P$ | Power | 功率 | W (watts) |
| $F$ | Force in direction of motion | 运动方向上的力 | N (newtons) |
| $v$ | Velocity | 速度 | m s⁻¹ (metres per second) |

**Derivation / 推导:**
$$ P = \frac{W}{t} = \frac{Fs}{t} = F \cdot \frac{s}{t} = Fv $$

**Conditions / 适用条件:**
- The force $F$ must be **constant** for the average power over a distance; for instantaneous power, $F$ and $v$ are instantaneous values.
- The force must be **parallel** to the velocity.
- For constant velocity, $F$ is the net driving force (equal to resistive forces).

> 📷 **IMAGE PROMPT — PWR-VEL-01: Power-Velocity Relationship Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a car moving to the right on a flat road. The car has an arrow labeled "F_drive" (driving force) pointing forward, and an arrow labeled "F_resistive" (total resistive force) pointing backward. Below the car, a horizontal line shows displacement s over time t. A callout box shows the derivation: P = W/t = Fs/t = Fv. Use a white background, blue and red arrows, and clear sans-serif labels. The car should be a simple side-profile silhouette.
>
> **中文描述:**
> 一个干净、教科书风格的矢量图，显示一辆汽车在平坦道路上向右行驶。汽车有一个标有"F_驱动"（驱动力）的箭头指向前方，和一个标有"F_阻力"（总阻力）的箭头指向后方。汽车下方，一条水平线显示随时间t的位移s。一个标注框显示推导过程：P = W/t = Fs/t = Fv。使用白色背景、蓝色和红色箭头，以及清晰的无衬线标签。汽车应为简单的侧面轮廓剪影。
>
> **Labels Required / 需要标注:**
> * F_drive (forward arrow)
> * F_resistive (backward arrow)
> * v (velocity arrow above car)
> * s (displacement line below)
> * Derivation box: P = W/t = Fs/t = Fv
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding how to derive and apply $P = Fv$ in exam problems involving vehicles and constant velocity.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — PWR-VEL-02: Maximum Power and Variable Velocity**
>
> **English Prompt:**
> A 3D-rendered infographic showing a graph with two curves on a white background. The x-axis is labeled "Velocity (v)" and the y-axis is labeled "Force (F)". The first curve (blue) shows F = P_max / v, a decreasing hyperbola. The second curve (red) shows a constant resistive force line. The intersection point is marked with a dot and labeled "Maximum Velocity". Below the graph, three small car icons show: (1) low speed, high force (steep hill), (2) medium speed, medium force, (3) high speed, low force (flat road). Use clean, modern design with gradient fills and drop shadows.
>
> **中文描述:**
> 一个3D渲染的信息图，在白色背景上显示一个带有两条曲线的图表。x轴标记为"速度 (v)"，y轴标记为"力 (F)"。第一条曲线（蓝色）显示 F = P_max / v，是一条递减的双曲线。第二条曲线（红色）显示一条恒定的阻力线。交点用点标记并标注为"最大速度"。图表下方，三个小汽车图标显示：(1) 低速、大力（陡坡），(2) 中速、中力，(3) 高速、小力（平路）。使用干净、现代的设计，带有渐变填充和投影。
>
> **Labels Required / 需要标注:**
> * x-axis: Velocity (v) / 速度 (v)
> * y-axis: Force (F) / 力 (F)
> * Blue curve: F = P_max / v
> * Red line: Resistive Force / 阻力
> * Intersection dot: Maximum Velocity / 最大速度
> * Three car icons with speed/force annotations
>
> **Style / 风格:** 3D-rendered infographic
>
> **Exam Relevance / 考试关联:**
> This graph is commonly used in exam questions to explain why vehicles have a maximum speed and why acceleration decreases at higher speeds.

---

# 6. Worked Example / 典型例题

### Example 1: Constant Velocity on a Flat Road

### Question / 题目
**English:** A car travels at a constant velocity of 25 m s⁻¹ on a flat road. The total resistive force (friction + air resistance) acting on the car is 800 N. Calculate the power output of the car's engine.

**中文:** 一辆汽车在平直道路上以 25 m s⁻¹ 的恒定速度行驶。作用在汽车上的总阻力（摩擦力 + 空气阻力）为 800 N。计算汽车发动机的输出功率。

### Solution / 解答
**Step 1:** Identify the driving force. Since velocity is constant, net force = 0, so driving force = resistive force.
$$ F_{\text{drive}} = F_{\text{resistive}} = 800 \text{ N} $$

**Step 2:** Apply $P = Fv$.
$$ P = 800 \times 25 = 20\,000 \text{ W} $$

**Step 3:** Convert to kW if needed.
$$ P = 20 \text{ kW} $$

### Final Answer / 最终答案
**Answer:** 20 kW **答案:** 20 千瓦

### Quick Tip / 提示
**EN:** At constant velocity, always set driving force equal to resistive force. This is the most common exam setup for $P = Fv$.
**CN:** 在恒定速度下，始终将驱动力设为等于阻力。这是 $P = Fv$ 最常见的考试设置。

---

### Example 2: Maximum Power and Hill Climbing

### Question / 题目
**English:** A car has a maximum power output of 60 kW. The total resistive force (including friction and air resistance) is constant at 1200 N. Calculate:
(a) The maximum constant velocity the car can achieve on a flat road.
(b) The maximum driving force available when the car is travelling at 15 m s⁻¹.

**中文:** 一辆汽车的最大功率输出为 60 kW。总阻力（包括摩擦力和空气阻力）恒定为 1200 N。计算：
(a) 汽车在平直道路上能达到的最大恒定速度。
(b) 当汽车以 15 m s⁻¹ 行驶时，可用的最大驱动力。

### Solution / 解答
**Part (a):**
At maximum velocity, driving force = resistive force = 1200 N.
$$ P_{\text{max}} = F_{\text{drive}} v_{\text{max}} $$
$$ 60\,000 = 1200 \times v_{\text{max}} $$
$$ v_{\text{max}} = \frac{60\,000}{1200} = 50 \text{ m s}^{-1} $$

**Part (b):**
Using $P_{\text{max}} = F_{\text{drive}} v$:
$$ 60\,000 = F_{\text{drive}} \times 15 $$
$$ F_{\text{drive}} = \frac{60\,000}{15} = 4\,000 \text{ N} $$

### Final Answer / 最终答案
**Answer:** (a) 50 m s⁻¹ (b) 4000 N **答案:** (a) 50 米/秒 (b) 4000 牛

### Quick Tip / 提示
**EN:** When power is constant, force and velocity are inversely proportional. This explains why cars struggle to accelerate at high speeds.
**CN:** 当功率恒定时，力和速度成反比。这解释了为什么汽车在高速时加速困难。

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the formula linking power, force, and velocity?
Q (CN): 连接功率、力和速度的公式是什么？
A (EN): P = Fv, where P is power (W), F is force in direction of motion (N), and v is velocity (m s⁻¹).
A (CN): P = Fv，其中 P 是功率（瓦），F 是运动方向上的力（牛），v 是速度（米/秒）。

**Flashcard 2:**
Q (EN): How is P = Fv derived from the definition of power?
Q (CN): 如何从功率的定义推导出 P = Fv？
A (EN): P = W/t = Fs/t = F(s/t) = Fv.
A (CN): P = W/t = Fs/t = F(s/t) = Fv。

**Flashcard 3:**
Q (EN): What condition must be true for P = Fv to give the average power over a distance?
Q (CN): 要使 P = Fv 给出某段距离上的平均功率，必须满足什么条件？
A (EN): The force F must be constant and parallel to the velocity.
A (CN): 力 F 必须恒定且与速度平行。

**Flashcard 4:**
Q (EN): If a car has constant maximum power, what happens to the maximum driving force as velocity increases?
Q (CN): 如果汽车有恒定的最大功率，随着速度增加，最大驱动力会发生什么变化？
A (EN): The maximum driving force decreases (F = P_max / v).
A (CN): 最大驱动力减小 (F = P_max / v)。

**Flashcard 5:**
Q (EN): At constant velocity on a flat road, what is the relationship between driving force and resistive force?
Q (CN): 在平直道路上以恒定速度行驶时，驱动力和阻力之间有什么关系？
A (EN): They are equal (net force = 0).
A (CN): 它们相等（净力 = 0）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Power and Velocity
  cn: 功率与速度
parent_topic: Power and Efficiency
parent_hub: "[[Power and Efficiency]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Definition of Power]]"
  - "[[Efficiency of Energy Transfers]]"
prerequisites:
  - "[[Work Done by a Force]]"
  - "[[Conservation of Energy]]"
language: bilingual_en_cn