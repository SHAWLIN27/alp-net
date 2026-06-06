# Newton's Second Law (F=ma) / 牛顿第二定律 (F=ma)

---

# 1. Overview / 概述

**English:**
Newton's Second Law is the cornerstone of classical mechanics, providing a quantitative relationship between force, mass, and acceleration. This sub-topic explores how an object's acceleration is directly proportional to the net force acting on it and inversely proportional to its mass. Understanding F=ma is essential for analyzing motion in real-world scenarios, from calculating the thrust of a rocket to determining the braking distance of a car. This leaf node builds directly on [[Free-body Diagrams]] and serves as a foundation for [[Applications of Newton's Laws]], [[Linear Momentum and Impulse]], and [[Conservation of Momentum]].

**中文:**
牛顿第二定律是经典力学的基石，建立了力、质量和加速度之间的定量关系。本子知识点探讨物体的加速度如何与作用在其上的净力成正比，与其质量成反比。理解 F=ma 对于分析现实世界中的运动至关重要，从计算火箭的推力到确定汽车的制动距离。本叶节点直接建立在[[Free-body Diagrams]]的基础上，并为[[Applications of Newton's Laws]]、[[Linear Momentum and Impulse]]和[[Conservation of Momentum]]奠定基础。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Newton's Second Law** / 牛顿第二定律 | The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass, in the same direction as the net force. | 物体的加速度与作用在其上的净力成正比，与其质量成反比，方向与净力方向相同。 |
| **Net Force** / 净力 | The vector sum of all forces acting on an object. | 作用在物体上所有力的矢量和。 |
| **Acceleration** / 加速度 | The rate of change of velocity of an object with respect to time. | 物体速度随时间的变化率。 |
| **Inertial Mass** / 惯性质量 | A measure of an object's resistance to acceleration when a force is applied. | 物体在受力时抵抗加速度的量度。 |
| **Resultant Force** / 合力 | Another term for net force; the single force that has the same effect as all forces combined. | 净力的另一种说法；与所有力组合效果相同的单一力。 |
| **Proportionality** / 比例关系 | The relationship where one quantity changes in direct proportion to another. | 一个量随另一个量成比例变化的关系。 |

---

# 3. Key Concepts / 关键概念

**English:**

Newton's Second Law can be expressed mathematically as:

$$ \vec{F}_{\text{net}} = m\vec{a} $$

Where $\vec{F}_{\text{net}}$ is the net (resultant) force, $m$ is the mass, and $\vec{a}$ is the acceleration.

**Step-by-step reasoning:**
1. **Identify all forces** acting on the object using a [[Free-body Diagrams]].
2. **Resolve forces** into components along chosen axes (typically horizontal and vertical).
3. **Calculate net force** by summing forces in each direction: $\Sigma F_x = ma_x$, $\Sigma F_y = ma_y$.
4. **Apply F=ma** to find acceleration, or use known acceleration to find unknown forces.

**Physical interpretation:**
- **Force causes acceleration**, not velocity. An object can have constant velocity (including zero) even with forces acting, as long as they balance.
- **Mass is a measure of inertia** — larger mass means smaller acceleration for the same force.
- **Direction matters**: acceleration is always in the direction of the net force.

**Common pitfalls:**
- **Forgetting vector nature**: Forces are vectors; direction must be considered.
- **Confusing mass and weight**: Mass ($m$) is constant; weight ($W=mg$) is a force.
- **Ignoring all forces**: Only the **net** force causes acceleration, not individual forces.
- **Applying F=ma to non-inertial frames**: The law holds only in inertial (non-accelerating) reference frames.

**中文:**

牛顿第二定律可以用数学表达式表示为：

$$ \vec{F}_{\text{net}} = m\vec{a} $$

其中 $\vec{F}_{\text{net}}$ 是净（合）力，$m$ 是质量，$\vec{a}$ 是加速度。

**逐步推理：**
1. **识别所有力** 使用[[Free-body Diagrams]]作用在物体上的力。
2. **分解力** 沿选定轴（通常为水平和垂直）分解为分量。
3. **计算净力** 在每个方向上求和力：$\Sigma F_x = ma_x$，$\Sigma F_y = ma_y$。
4. **应用 F=ma** 求加速度，或利用已知加速度求未知力。

**物理意义：**
- **力引起加速度**，而不是速度。即使有力作用，只要它们平衡，物体可以保持恒定速度（包括零）。
- **质量是惯性的量度** — 质量越大，相同力产生的加速度越小。
- **方向很重要**：加速度始终与净力方向相同。

**常见错误：**
- **忘记矢量性质**：力是矢量，必须考虑方向。
- **混淆质量和重量**：质量（$m$）是常数；重量（$W=mg$）是一种力。
- **忽略所有力**：只有**净**力引起加速度，而不是单个力。
- **在非惯性系中应用 F=ma**：该定律仅在惯性（非加速）参考系中成立。

---

# 4. Formulas / 公式

## Primary Formula / 主要公式

$$ \vec{F}_{\text{net}} = m\vec{a} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{F}_{\text{net}}$ | Net (resultant) force | 净力（合力） | N (newton) |
| $m$ | Mass of the object | 物体的质量 | kg |
| $\vec{a}$ | Acceleration | 加速度 | m/s² |

## Component Forms / 分量形式

$$ \Sigma F_x = ma_x \quad \text{and} \quad \Sigma F_y = ma_y $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\Sigma F_x$ | Sum of forces in x-direction | x方向力的总和 | N |
| $a_x$ | Acceleration in x-direction | x方向加速度 | m/s² |

## Weight as a Special Case / 重量作为特例

$$ W = mg $$

Where $g = 9.81 \text{ m/s}^2$ (gravitational field strength on Earth).

**Derivation / 推导:**
When only gravity acts on an object (free fall), the net force is weight $W = mg$. Applying F=ma:
$$ F_{\text{net}} = ma \implies mg = ma \implies a = g $$
This shows all objects in free fall accelerate at $g$ regardless of mass.

**Conditions / 适用条件:**
- The object's mass is constant (non-relativistic speeds).
- Forces are measured in an inertial reference frame.
- The net force is the vector sum of all forces.

> 📷 **IMAGE PROMPT — FMA-01: Force-Acceleration Relationship Diagram**
>
> **English Prompt:**
> A clean textbook-style vector diagram showing three scenarios: (1) A 2kg block with a single 10N force arrow to the right, labeled "F=10N", with acceleration arrow "a=5 m/s²" above. (2) Same block with two forces: 10N right and 4N left, net force 6N right, acceleration "a=3 m/s²". (3) A 4kg block with same 10N force, acceleration "a=2.5 m/s²". All on a frictionless horizontal surface. Use blue for force arrows, red for acceleration arrows. Labels in clear sans-serif font. White background with subtle grid lines.
>
> **中文描述:**
> 一个干净的教科书风格矢量图，显示三种情景：(1) 一个2kg的方块，右侧有一个10N的力箭头，标注"F=10N"，上方有加速度箭头"a=5 m/s²"。(2) 同一个方块有两个力：右侧10N和左侧4N，净力6N向右，加速度"a=3 m/s²"。(3) 一个4kg的方块，同样10N的力，加速度"a=2.5 m/s²"。所有情景在无摩擦水平面上。力箭头用蓝色，加速度箭头用红色。标签使用清晰无衬线字体。白色背景带轻微网格线。
>
> **Labels Required / 需要标注:**
> * F=10N (force arrow)
> * a=5 m/s² (acceleration arrow)
> * m=2kg (mass label)
> * Net force = 6N (for scenario 2)
>
> **Style / 风格:** Textbook vector / 2D diagram
>
> **Exam Relevance / 考试关联:**
> This diagram directly illustrates the proportional relationship between net force and acceleration, and the inverse relationship between mass and acceleration — both key exam concepts.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — FMA-02: Free-body Diagram to F=ma Application**
>
> **English Prompt:**
> A step-by-step visual guide showing a box on a rough inclined plane at 30°. Step 1: Free-body diagram with weight (W=mg) vertically down, normal reaction (N) perpendicular to plane, friction (f) up the plane. Step 2: Resolving weight into components: mg sinθ down the plane, mg cosθ perpendicular to plane. Step 3: Applying F=ma along the plane: mg sinθ - f = ma. Use color coding: green for weight, blue for normal, red for friction, orange for components. Include coordinate axes. Professional physics textbook illustration style.
>
> **中文描述:**
> 一个逐步视觉指南，显示一个盒子在30°粗糙斜面上。步骤1：受力分析图，重量（W=mg）垂直向下，法向反力（N）垂直于斜面，摩擦力（f）沿斜面向上。步骤2：将重量分解为分量：mg sinθ沿斜面向下，mg cosθ垂直于斜面。步骤3：沿斜面应用F=ma：mg sinθ - f = ma。使用颜色编码：绿色表示重量，蓝色表示法向力，红色表示摩擦力，橙色表示分量。包括坐标轴。专业物理教科书插图风格。
>
> **Labels Required / 需要标注:**
> * θ=30°
> * mg sinθ
> * mg cosθ
> * N (normal reaction)
> * f (friction)
> * a (acceleration direction)
>
> **Style / 风格:** Textbook vector / step-by-step diagram
>
> **Exam Relevance / 考试关联:**
> Inclined plane problems are a common exam application of F=ma, testing students' ability to resolve forces and apply the law in two dimensions.

---

# 6. Worked Example / 典型例题

## Example 1: Horizontal Motion / 水平运动示例

### Question / 题目
**English:**
A 5.0 kg box is pulled across a rough horizontal surface by a horizontal force of 30 N. The frictional force opposing motion is 12 N. Calculate:
(a) The acceleration of the box.
(b) The distance traveled in 4.0 seconds starting from rest.

**中文:**
一个5.0 kg的盒子在粗糙水平面上被30 N的水平力拉动。阻碍运动的摩擦力为12 N。计算：
(a) 盒子的加速度。
(b) 从静止开始4.0秒内行进的距离。

### Solution / 解答

**(a) Acceleration / 加速度**

Step 1: Identify forces in horizontal direction.
- Applied force: $F = 30 \text{ N}$ (to the right)
- Friction: $f = 12 \text{ N}$ (to the left)

Step 2: Calculate net force.
$$ F_{\text{net}} = F - f = 30 - 12 = 18 \text{ N} $$

Step 3: Apply F=ma.
$$ a = \frac{F_{\text{net}}}{m} = \frac{18}{5.0} = 3.6 \text{ m/s}^2 $$

**Answer (a):** $a = 3.6 \text{ m/s}^2$ to the right

**(b) Distance traveled / 行进距离**

Using $s = ut + \frac{1}{2}at^2$ with $u = 0$, $t = 4.0 \text{ s}$, $a = 3.6 \text{ m/s}^2$:

$$ s = 0 + \frac{1}{2}(3.6)(4.0)^2 = \frac{1}{2}(3.6)(16) = 28.8 \text{ m} $$

**Answer (b):** $s = 29 \text{ m}$ (2 significant figures)

### Final Answer / 最终答案
**Answer:** (a) $3.6 \text{ m/s}^2$ (b) $29 \text{ m}$
**答案：** (a) $3.6 \text{ m/s}^2$ (b) $29 \text{ m}$

### Quick Tip / 提示
Always draw a [[Free-body Diagrams]] first! Identify all forces, then find the **net** force before applying F=ma. Remember that friction always opposes motion.

---

## Example 2: Vertical Motion / 竖直运动示例

### Question / 题目
**English:**
A 2.0 kg mass is suspended from a spring scale in a lift (elevator). Calculate the reading on the scale when:
(a) The lift accelerates upward at $2.0 \text{ m/s}^2$.
(b) The lift moves upward at constant velocity of $3.0 \text{ m/s}$.
(c) The lift accelerates downward at $1.5 \text{ m/s}^2$.

**中文:**
一个2.0 kg的质量悬挂在电梯中的弹簧秤上。计算弹簧秤的读数当：
(a) 电梯以$2.0 \text{ m/s}^2$向上加速。
(b) 电梯以$3.0 \text{ m/s}$匀速向上运动。
(c) 电梯以$1.5 \text{ m/s}^2$向下加速。

### Solution / 解答

The spring scale reading equals the tension $T$ in the string (apparent weight).

**General approach:** Apply F=ma vertically. Take upward as positive.

$$ \Sigma F_y = T - mg = ma_y $$

$$ T = m(g + a_y) $$

**(a) Upward acceleration ($a_y = +2.0 \text{ m/s}^2$):**
$$ T = 2.0(9.81 + 2.0) = 2.0(11.81) = 23.62 \text{ N} $$

**Answer (a):** $T = 24 \text{ N}$ (apparent weight increases)

**(b) Constant velocity ($a_y = 0$):**
$$ T = 2.0(9.81 + 0) = 19.62 \text{ N} $$

**Answer (b):** $T = 20 \text{ N}$ (apparent weight equals actual weight)

**(c) Downward acceleration ($a_y = -1.5 \text{ m/s}^2$):**
$$ T = 2.0(9.81 - 1.5) = 2.0(8.31) = 16.62 \text{ N} $$

**Answer (c):** $T = 17 \text{ N}$ (apparent weight decreases)

### Final Answer / 最终答案
**Answer:** (a) $24 \text{ N}$ (b) $20 \text{ N}$ (c) $17 \text{ N}$
**答案：** (a) $24 \text{ N}$ (b) $20 \text{ N}$ (c) $17 \text{ N}$

### Quick Tip / 提示
In lift problems, the apparent weight changes because the normal reaction (or tension) must provide both the weight and the acceleration. If the lift cable breaks ($a_y = -g$), the apparent weight becomes zero — this is "weightlessness."

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
- Q (EN): State Newton's Second Law of Motion.
- Q (CN): 陈述牛顿第二运动定律。
- A (EN): The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass, in the same direction as the net force. Mathematically: F_net = ma.
- A (CN): 物体的加速度与作用在其上的净力成正比，与其质量成反比，方向与净力方向相同。数学表达式：F_net = ma。

**Flashcard 2:**
- Q (EN): What is the difference between mass and weight?
- Q (CN): 质量和重量有什么区别？
- A (EN): Mass (m) is a scalar measure of the amount of matter in an object, measured in kg. Weight (W = mg) is a force due to gravity, measured in N. Mass is constant; weight varies with gravitational field strength.
- A (CN): 质量（m）是物体中物质数量的标量量度，单位为kg。重量（W = mg）是由于重力产生的力，单位为N。质量是常数；重量随重力场强度变化。

**Flashcard 3:**
- Q (EN): A 3.0 kg object experiences a net force of 12 N. What is its acceleration?
- Q (CN): 一个3.0 kg的物体受到12 N的净力。它的加速度是多少？
- A (EN): a = F_net / m = 12 / 3.0 = 4.0 m/s² in the direction of the net force.
- A (CN): a = F_net / m = 12 / 3.0 = 4.0 m/s²，方向与净力方向相同。

**Flashcard 4:**
- Q (EN): What happens to the apparent weight of a person in a lift accelerating upward?
- Q (CN): 在向上加速的电梯中，人的表观重量会发生什么变化？
- A (EN): The apparent weight increases because the normal reaction force must provide both the weight (mg) and the upward acceleration (ma). Apparent weight = m(g + a).
- A (CN): 表观重量增加，因为法向反力必须同时提供重量（mg）和向上加速度（ma）。表观重量 = m(g + a)。

**Flashcard 5:**
- Q (EN): Why is Newton's Second Law considered a vector law?
- Q (CN): 为什么牛顿第二定律被认为是矢量定律？
- A (EN): Because force and acceleration are both vectors. The acceleration is always in the same direction as the net force. The law must be applied separately to each component direction (e.g., ΣFx = max, ΣFy = may).
- A (CN): 因为力和加速度都是矢量。加速度始终与净力方向相同。该定律必须分别应用于每个分量方向（例如，ΣFx = max，ΣFy = may）。

---

# 8. Metadata / 元数据

```yaml
title:
  en: "Newton's Second Law (F=ma)"
  cn: "牛顿第二定律 (F=ma)"
parent_topic: "Newton's Laws of Motion"
parent_hub: "[[Newton's Laws of Motion]]"
subject: Physics
syllabus:
  - CAIE 9702: 3.2 (d-e)
  - Edexcel IAL: WPH11 U1: 2.7-2.10
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[Newton's First Law (Inertia)]]"
  - "[[Newton's Third Law (Action-Reaction)]]"
  - "[[Applications of Newton's Laws]]"
  - "[[Free-body Diagrams]]"
  - "[[Linear Momentum and Impulse]]"
  - "[[Conservation of Momentum]]"
language: bilingual_en_cn