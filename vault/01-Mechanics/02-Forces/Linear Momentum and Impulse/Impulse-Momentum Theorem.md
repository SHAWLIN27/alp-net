# 1. Overview / 概述

**English:**
The Impulse-Momentum Theorem is a fundamental principle that directly links the concepts of [[Definition of Linear Momentum]] and [[Impulse and Force-Time Graphs]]. It states that the impulse applied to an object equals the change in its momentum. This theorem provides a powerful alternative to using Newton's Second Law directly, especially when dealing with forces that vary with time or act over very short intervals (like collisions or impacts). It is the conceptual bridge between force and momentum, and it forms the foundation for understanding the [[Conservation of Momentum]] principle.

**中文:**
冲量-动量定理是一个基本原理，它直接连接了[[Definition of Linear Momentum|线性动量的定义]]和[[Impulse and Force-Time Graphs|冲量与力-时间图]]的概念。该定理指出，施加在物体上的冲量等于其动量的变化。这个定理为直接使用牛顿第二定律提供了一种强大的替代方案，特别是在处理随时间变化的力或在极短时间间隔内作用的力（如碰撞或冲击）时。它是连接力和动量的概念桥梁，也是理解[[Conservation of Momentum|动量守恒]]原理的基础。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Impulse-Momentum Theorem** / 冲量-动量定理 | The impulse acting on an object is equal to the change in momentum of that object. | 作用在物体上的冲量等于该物体动量的变化。 |
| **Net Impulse** / 净冲量 | The total impulse resulting from the net force acting on an object over a time interval. | 在时间间隔内，由作用在物体上的合力产生的总冲量。 |
| **Change in Momentum** / 动量变化 | The difference between the final momentum and the initial momentum of an object ($\Delta p = p_f - p_i$). | 物体末动量与初动量之差 ($\Delta p = p_f - p_i$)。 |
| **Average Force** / 平均力 | A constant force that would produce the same impulse over the same time interval as a varying force. | 在相同时间间隔内，能产生与变力相同冲量的恒定力。 |

---

# 3. Key Concepts / 关键概念

**English:**
The Impulse-Momentum Theorem is derived directly from [[Newton's Laws of Motion|Newton's Second Law of Motion]].

**Step-by-step reasoning:**
1.  Newton's Second Law states: $F_{net} = ma = m\frac{\Delta v}{\Delta t}$.
2.  Rearranging: $F_{net} \Delta t = m \Delta v$.
3.  Since $\Delta p = m \Delta v$, we get: $F_{net} \Delta t = \Delta p$.
4.  The left side, $F_{net} \Delta t$, is the **impulse** ($J$). The right side is the **change in momentum**.

**Physical Interpretation:**
The theorem tells us that a force does not need to be large to change an object's momentum; it can be a small force applied over a long time (e.g., a rocket engine firing slowly) or a large force applied over a short time (e.g., a hammer hitting a nail). This is why airbags in cars save lives: they increase the time over which the collision force acts, thereby reducing the average force experienced by the passenger for the same change in momentum.

**Common Pitfalls:**
- **Direction:** Impulse and momentum are vector quantities. A change in direction (e.g., a ball bouncing off a wall) involves a change in momentum, even if the speed is constant.
- **Net Force:** The theorem applies to the *net* force, not just one force. If multiple forces act, the net impulse equals the change in momentum.
- **Sign Convention:** Always define a positive direction. A force opposite to this direction produces a negative impulse and a negative change in momentum.

**中文:**
冲量-动量定理直接源自[[Newton's Laws of Motion|牛顿第二运动定律]]。

**逐步推理：**
1.  牛顿第二定律指出：$F_{net} = ma = m\frac{\Delta v}{\Delta t}$。
2.  重新排列：$F_{net} \Delta t = m \Delta v$。
3.  由于 $\Delta p = m \Delta v$，我们得到：$F_{net} \Delta t = \Delta p$。
4.  左边 $F_{net} \Delta t$ 是**冲量** ($J$)。右边是**动量变化**。

**物理解释：**
该定理告诉我们，改变物体的动量并不一定需要很大的力；可以是长时间施加的小力（例如，火箭发动机缓慢点火），也可以是短时间施加的大力（例如，锤子敲钉子）。这就是为什么汽车中的安全气囊能挽救生命：它们增加了碰撞力作用的时间，从而在动量变化相同的情况下，减少了乘客所承受的平均力。

**常见误区：**
- **方向：** 冲量和动量是矢量。方向的改变（例如，球从墙上弹回）涉及动量的变化，即使速度大小不变。
- **合力：** 该定理适用于*合力*，而不仅仅是某一个力。如果有多个力作用，净冲量等于动量变化。
- **符号约定：** 始终定义一个正方向。与该方向相反的力产生负冲量和负动量变化。

---

# 4. Formulas / 公式

The core formula of the Impulse-Momentum Theorem:

$$ J = F_{net} \Delta t = \Delta p = m \Delta v = m(v_f - v_i) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $J$ | Impulse | 冲量 | N·s (or kg·m/s) |
| $F_{net}$ | Net (average) force | 净（平均）力 | N |
| $\Delta t$ | Time interval | 时间间隔 | s |
| $\Delta p$ | Change in momentum | 动量变化 | kg·m/s |
| $m$ | Mass | 质量 | kg |
| $v_f$ | Final velocity | 末速度 | m/s |
| $v_i$ | Initial velocity | 初速度 | m/s |

**Derivation / 推导:**
Starting from Newton's Second Law: $F_{net} = \frac{\Delta p}{\Delta t}$.
Multiplying both sides by $\Delta t$: $F_{net} \Delta t = \Delta p$.
Therefore, $J = \Delta p$.

**Conditions / 适用条件:**
- The theorem applies to any object or system of objects.
- $F_{net}$ is the average net force if the force is not constant.
- The time interval $\Delta t$ must be finite (not instantaneous).

> 📷 **IMAGE PROMPT — IMT-01: Impulse-Momentum Theorem Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing a ball of mass m moving with initial velocity v_i towards a wall. The ball hits the wall and rebounds with final velocity v_f in the opposite direction. A large force arrow F (red) is shown acting on the ball during the short collision time Δt. A callout box shows the equation: FΔt = m(v_f - v_i). The diagram should clearly label the initial and final velocities, the force, and the time interval.
>
> **中文描述:**
> 一个清晰、教科书风格的矢量图，显示一个质量为 m 的球以初速度 v_i 向墙壁运动。球撞击墙壁并以相反方向的末速度 v_f 反弹。一个大的力箭头 F（红色）显示在短暂的碰撞时间 Δt 内作用在球上。一个标注框显示方程：FΔt = m(v_f - v_i)。图表应清晰标注初速度和末速度、力以及时间间隔。
>
> **Labels Required / 需要标注:**
> * m (mass / 质量)
> * v_i (initial velocity / 初速度)
> * v_f (final velocity / 末速度)
> * F (average force / 平均力)
> * Δt (collision time / 碰撞时间)
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This diagram is essential for understanding how to apply the theorem to collision problems, a common exam scenario.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — IMT-02: Airbag Safety Application**
>
> **English Prompt:**
> A split-screen photorealistic 3D render comparing two car crash scenarios. Left side: A driver without an airbag hits the steering wheel directly. A large red "F" arrow and a small "Δt" label are shown, indicating a large force over a short time. Right side: A driver with an airbag deploys. The airbag is shown compressing, with a smaller "F" arrow and a larger "Δt" label, indicating a smaller force over a longer time. Both drivers have the same change in momentum (Δp). A banner at the bottom reads: "Same Δp, Larger Δt = Smaller F".
>
> **中文描述:**
> 一个分屏的逼真3D渲染图，比较两种汽车碰撞场景。左侧：没有安全气囊的驾驶员直接撞向方向盘。显示一个大的红色 "F" 箭头和一个小的 "Δt" 标签，表示短时间内的巨大作用力。右侧：有安全气囊的驾驶员，气囊展开。显示气囊正在压缩，有一个较小的 "F" 箭头和一个较大的 "Δt" 标签，表示较长时间内的较小作用力。两位驾驶员具有相同的动量变化 (Δp)。底部横幅写着："相同 Δp，更大的 Δt = 更小的 F"。
>
> **Labels Required / 需要标注:**
> * F (large / 大) vs. F (small / 小)
> * Δt (small / 小) vs. Δt (large / 大)
> * Δp (same / 相同)
>
> **Style / 风格:** Photorealistic 3D render
>
> **Exam Relevance / 考试关联:**
> This is a classic real-world application question in exams. Understanding this concept helps answer "explain" and "suggest" questions about safety features.

---

# 6. Worked Example / 典型例题

### Question / 题目
**English:**
A cricket ball of mass 160 g is bowled at a speed of 30 m/s. The batsman hits the ball straight back towards the bowler at a speed of 20 m/s. The ball is in contact with the bat for 0.05 s.
(a) Calculate the impulse imparted to the ball by the bat.
(b) Calculate the average force exerted by the bat on the ball.

**中文:**
一个质量为 160 g 的板球以 30 m/s 的速度投出。击球手将球径直击回投球手，速度为 20 m/s。球与球棒接触的时间为 0.05 s。
(a) 计算球棒施加给球的冲量。
(b) 计算球棒对球的平均作用力。

### Solution / 解答

**Step 1: Define the positive direction.**
Let the direction from the bowler to the batsman be positive (+).

**Step 2: Identify known values.**
$m = 160 \text{ g} = 0.16 \text{ kg}$
$v_i = +30 \text{ m/s}$ (towards batsman)
$v_f = -20 \text{ m/s}$ (back towards bowler, opposite direction)
$\Delta t = 0.05 \text{ s}$

**Step 3: Apply the Impulse-Momentum Theorem.**
(a) $J = \Delta p = m(v_f - v_i)$
$J = 0.16 \times (-20 - 30)$
$J = 0.16 \times (-50)$
$J = -8.0 \text{ N·s}$

The negative sign indicates the impulse is in the direction from the batsman back towards the bowler (opposite to the initial direction).

(b) $J = F_{avg} \Delta t$
$F_{avg} = \frac{J}{\Delta t} = \frac{-8.0}{0.05}$
$F_{avg} = -160 \text{ N}$

The negative sign indicates the average force is also directed back towards the bowler.

### Final Answer / 最终答案
**Answer:** (a) Impulse = 8.0 N·s (towards the bowler) **答案:** (a) 冲量 = 8.0 N·s (朝向投球手)
(b) Average force = 160 N (towards the bowler) (b) 平均力 = 160 N (朝向投球手)

### Quick Tip / 提示
**EN:** Always define a sign convention before starting. The change in velocity ($v_f - v_i$) is crucial — don't forget the signs!
**CN:** 在开始前始终定义一个符号约定。速度的变化 ($v_f - v_i$) 至关重要——不要忘记符号！

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): State the Impulse-Momentum Theorem.
Q (CN): 陈述冲量-动量定理。
A (EN): The impulse acting on an object is equal to the change in momentum of that object.
A (CN): 作用在物体上的冲量等于该物体动量的变化。

**Flashcard 2:**
Q (EN): What is the formula for the Impulse-Momentum Theorem?
Q (CN): 冲量-动量定理的公式是什么？
A (EN): $F_{net} \Delta t = \Delta p = m \Delta v$
A (CN): $F_{net} \Delta t = \Delta p = m \Delta v$

**Flashcard 3:**
Q (EN): How does an airbag reduce injury in a car crash, according to the Impulse-Momentum Theorem?
Q (CN): 根据冲量-动量定理，安全气囊如何减少车祸中的伤害？
A (EN): It increases the collision time ($\Delta t$), which reduces the average force ($F_{avg}$) for the same change in momentum ($\Delta p$).
A (CN): 它增加了碰撞时间 ($\Delta t$)，从而在相同的动量变化 ($\Delta p$) 下减少了平均力 ($F_{avg}$)。

**Flashcard 4:**
Q (EN): A ball hits a wall and rebounds. Is the change in momentum zero if its speed is the same before and after?
Q (CN): 一个球撞击墙壁并反弹。如果其前后速度大小相同，动量变化是否为零？
A (EN): No. Momentum is a vector. The direction has changed, so there is a change in momentum.
A (CN): 不是。动量是矢量。方向改变了，所以动量有变化。

**Flashcard 5:**
Q (EN): What are the SI units of impulse?
Q (CN): 冲量的SI单位是什么？
A (EN): N·s (Newton-seconds) or kg·m/s.
A (CN): N·s (牛顿·秒) 或 kg·m/s。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Impulse-Momentum Theorem"
  cn: "冲量-动量定理"
parent_topic: "Linear Momentum and Impulse"
parent_hub: "[[Linear Momentum and Impulse]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Definition of Linear Momentum]]"
  - "[[Impulse and Force-Time Graphs]]"
  - "[[Conservation of Momentum]]"
prerequisites:
  - "[[Newton's Laws of Motion]]"
language: bilingual_en_cn