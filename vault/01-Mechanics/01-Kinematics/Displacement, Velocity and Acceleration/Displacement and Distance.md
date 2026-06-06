# Displacement and Distance / 位移与路程

---

## 1. Overview / 概述

**English:**
Displacement and distance are two fundamental concepts in kinematics that describe "how far" an object has moved, but they do so in fundamentally different ways. Distance is a scalar quantity that measures the total length of the path traveled, regardless of direction. Displacement is a vector quantity that measures the straight-line change in position from the starting point to the ending point, including direction. Understanding the distinction between these two concepts is essential for mastering [[Displacement, Velocity and Acceleration]] and forms the foundation for [[Speed and Velocity]], [[Acceleration]], and eventually [[Equations of Motion (SUVAT)]]. This distinction relies heavily on the prerequisite understanding of [[Scalars and Vectors]].

**中文:**
位移和路程是运动学中描述物体"移动了多远"的两个基本概念，但它们的含义有本质区别。路程是标量，测量的是物体实际经过的路径总长度，不考虑方向。位移是矢量，测量的是从起点到终点的直线位置变化，包含方向信息。理解这两个概念的区别对于掌握[[Displacement, Velocity and Acceleration]]至关重要，也是学习[[Speed and Velocity]]、[[Acceleration]]以及[[Equations of Motion (SUVAT)]]的基础。这一区分依赖于对[[Scalars and Vectors]]的先修理解。

---

## 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Distance** / 路程 | The total length of the path traveled by an object, irrespective of direction. It is a scalar quantity. | 物体运动路径的总长度，与方向无关。是一个标量。 |
| **Displacement** / 位移 | The straight-line distance from the starting point to the ending point, measured in a specific direction. It is a vector quantity. | 从起点到终点的直线距离，沿特定方向测量。是一个矢量。 |
| **Magnitude of Displacement** / 位移大小 | The numerical value of displacement, equal to the shortest distance between start and end points. | 位移的数值，等于起点和终点之间的最短距离。 |
| **Path** / 路径 | The actual route taken by an object as it moves from one position to another. | 物体从一个位置移动到另一个位置时实际经过的路线。 |
| **Position** / 位置 | The location of an object relative to a chosen reference point or origin. | 物体相对于所选参考点或原点的位置。 |

---

## 3. Key Concepts / 关键概念

**English:**

### The Fundamental Distinction

The key difference between distance and displacement lies in whether direction matters. Distance is a [[Scalars and Vectors|scalar]] — it only has magnitude. Displacement is a [[Scalars and Vectors|vector]] — it has both magnitude and direction.

Consider a student walking from their classroom to the library:
- If they walk 200 m east, then 100 m west to get a book, then 50 m east again to reach the library:
  - **Distance** = 200 + 100 + 50 = 350 m (total path length)
  - **Displacement** = 200 - 100 + 50 = 150 m east (net change in position)

### Why This Matters

This distinction is crucial because:
1. **Velocity** is derived from displacement (not distance) — see [[Speed and Velocity]]
2. **Acceleration** depends on changes in velocity — see [[Acceleration]]
3. [[Motion Graphs]] use displacement-time graphs, not distance-time graphs
4. [[Equations of Motion (SUVAT)]] use displacement ($s$), not distance

### Common Pitfalls

1. **Confusing "distance traveled" with "displacement"** — Always check if direction matters in the problem.
2. **Assuming displacement equals distance** — This is only true for straight-line motion in one direction without changing direction.
3. **Forgetting the direction** — Displacement must include a direction (e.g., "50 m north" not just "50 m").
4. **Adding distances as vectors** — Distance is always added as positive numbers; displacement uses vector addition with signs.

### Physical Interpretation

- **Distance** tells you "how much ground was covered" — useful for fuel consumption, wear and tear, etc.
- **Displacement** tells you "how far and in what direction from the start" — useful for navigation, final position, etc.

**中文:**

### 基本区别

路程和位移的关键区别在于方向是否重要。路程是[[Scalars and Vectors|标量]]——只有大小。位移是[[Scalars and Vectors|矢量]]——既有大小又有方向。

考虑一个学生从教室走到图书馆：
- 如果他们先向东走200米，然后向西走100米取书，再向东走50米到达图书馆：
  - **路程** = 200 + 100 + 50 = 350米（路径总长度）
  - **位移** = 200 - 100 + 50 = 150米向东（位置净变化）

### 为什么这很重要

这一区别至关重要，因为：
1. **速度**由位移（而非路程）导出——参见[[Speed and Velocity]]
2. **加速度**取决于速度的变化——参见[[Acceleration]]
3. [[Motion Graphs]]使用位移-时间图，而非路程-时间图
4. [[Equations of Motion (SUVAT)]]使用位移（$s$），而非路程

### 常见错误

1. **混淆"走过的距离"和"位移"**——始终检查问题中方向是否重要。
2. **假设位移等于路程**——这仅适用于不改变方向的直线运动。
3. **忘记方向**——位移必须包含方向（例如"向北50米"而非仅"50米"）。
4. **将路程作为矢量相加**——路程总是作为正数相加；位移使用带符号的矢量加法。

### 物理解释

- **路程**告诉你"覆盖了多少地面"——适用于燃料消耗、磨损等。
- **位移**告诉你"离起点多远以及什么方向"——适用于导航、最终位置等。

---

## 4. Formulas / 公式

### Displacement Formula / 位移公式

$$ \vec{s} = \vec{r}_f - \vec{r}_i $$

Where $\vec{r}_f$ is the final position vector and $\vec{r}_i$ is the initial position vector.

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\vec{s}$ | Displacement vector | 位移矢量 | m (米) |
| $\vec{r}_f$ | Final position vector | 最终位置矢量 | m (米) |
| $\vec{r}_i$ | Initial position vector | 初始位置矢量 | m (米) |

### Distance Formula / 路程公式

For a path consisting of $n$ straight segments:

$$ d = \sum_{k=1}^{n} |\Delta \vec{r}_k| = |\Delta \vec{r}_1| + |\Delta \vec{r}_2| + ... + |\Delta \vec{r}_n| $$

Where $|\Delta \vec{r}_k|$ is the magnitude of each displacement segment.

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $d$ | Total distance | 总路程 | m (米) |
| $|\Delta \vec{r}_k|$ | Magnitude of k-th segment | 第k段位移的大小 | m (米) |

### Relationship / 关系

For any motion:
$$ |\vec{s}| \leq d $$

The magnitude of displacement is always less than or equal to the distance traveled. Equality holds only for straight-line motion in one direction without changing direction.

**中文：**

对于任何运动：
$$ |\vec{s}| \leq d $$

位移的大小总是小于或等于路程。等号仅在不改变方向的直线运动中成立。

> 📷 **IMAGE PROMPT — D&D-01: Displacement vs Distance Diagram**
>
> **English Prompt:**
> A clear textbook-style vector diagram showing a curved path (dashed line) from point A to point B, with a straight arrow (solid, red) labeled "Displacement" connecting A to B. The curved path is labeled "Distance" in blue. Include a coordinate system (x-y axes) with origin O. Points A and B are marked with coordinates. The diagram should be clean, minimal, with clear labels in English. White background, suitable for A-Level physics textbook.
>
> **中文描述:**
> 清晰的教科书风格矢量图，显示从A点到B点的弯曲路径（虚线），以及连接A和B的直线箭头（实线，红色），标注为"位移"。弯曲路径用蓝色标注为"路程"。包含坐标系（x-y轴）和原点O。A点和B点标有坐标。图表应简洁、清晰，带有英文标签。白色背景，适合A-Level物理教科书。
>
> **Labels Required / 需要标注:**
> * "Displacement $\vec{s}$" (red arrow)
> * "Distance $d$" (blue dashed curve)
> * Point A (initial position)
> * Point B (final position)
> * x-axis, y-axis, origin O
>
> **Style / 风格:** Textbook vector diagram
>
> **Exam Relevance / 考试关联:**
> This diagram is frequently used in exam questions to test the distinction between distance and displacement, especially in multiple-choice questions.

---

## 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — D&D-02: Real-World Example - Walking Path**
>
> **English Prompt:**
> A top-down view of a city block with a person walking along a path (dotted line) from a school (point A) to a library (point B). The path goes: east 2 blocks, north 1 block, east 1 block. Show the total path as a blue dotted line labeled "Distance = 4 blocks". Show a straight red arrow from school to library labeled "Displacement = 3.2 blocks NE". Include street names, buildings, and a compass rose. Clean, colorful, educational illustration style.
>
> **中文描述:**
> 城市街区的俯视图，一个人沿着路径（虚线）从学校（A点）走到图书馆（B点）。路径为：向东2个街区，向北1个街区，向东1个街区。用蓝色虚线显示总路径，标注"路程 = 4个街区"。用红色直线箭头从学校指向图书馆，标注"位移 = 3.2个街区 东北方向"。包含街道名称、建筑物和指南针。干净、彩色、教育插画风格。
>
> **Labels Required / 需要标注:**
> * "Distance = 4 blocks" (blue dotted path)
> * "Displacement = 3.2 blocks NE" (red arrow)
> * School (point A), Library (point B)
> * Compass rose (N, S, E, W)
> * Street names
>
> **Style / 风格:** Educational illustration, top-down view
>
> **Exam Relevance / 考试关联:**
> Real-world context questions often use city block or walking path scenarios to test the distance vs displacement concept.

---

## 6. Worked Example / 典型例题

### Example 1: Walking Path / 例题1：行走路径

#### Question / 题目

**English:**
A student walks 300 m east from home to school, then 400 m north to the library. Calculate:
(a) The total distance traveled.
(b) The magnitude of the displacement from home to the library.
(c) The direction of the displacement.

**中文:**
一名学生从家向东走300米到学校，然后向北走400米到图书馆。计算：
(a) 总路程。
(b) 从家到图书馆的位移大小。
(c) 位移的方向。

#### Solution / 解答

**Step 1: Identify the path segments**
- Segment 1: 300 m east
- Segment 2: 400 m north

**Step 2: Calculate distance (a)**
$$ d = 300 + 400 = 700 \text{ m} $$

**Step 3: Calculate displacement magnitude (b)**
Using Pythagoras' theorem:
$$ |\vec{s}| = \sqrt{300^2 + 400^2} = \sqrt{90,000 + 160,000} = \sqrt{250,000} = 500 \text{ m} $$

**Step 4: Calculate displacement direction (c)**
$$ \theta = \tan^{-1}\left(\frac{400}{300}\right) = \tan^{-1}\left(\frac{4}{3}\right) \approx 53.1^\circ \text{ north of east} $$

#### Final Answer / 最终答案

**Answer:**
(a) Distance = 700 m
(b) Displacement magnitude = 500 m
(c) Direction = 53.1° north of east (or 036.9° on a bearing)

**答案:**
(a) 路程 = 700米
(b) 位移大小 = 500米
(c) 方向 = 东偏北53.1°（或方位角036.9°）

#### Quick Tip / 提示

**English:** When calculating displacement, always draw a vector diagram first. Use Pythagoras for perpendicular components and trigonometry for direction. Remember that distance is always the sum of absolute values, while displacement uses vector addition.

**中文:** 计算位移时，先画矢量图。垂直分量用勾股定理，方向用三角函数。记住路程是绝对值的和，而位移使用矢量加法。

---

### Example 2: Round Trip / 例题2：往返行程

#### Question / 题目

**English:**
A cyclist rides 5 km east from town A to town B, then immediately rides 5 km west back to town A. Calculate:
(a) The total distance traveled.
(b) The displacement at the end of the journey.

**中文:**
一名骑行者从A镇向东骑行5公里到B镇，然后立即向西骑行5公里返回A镇。计算：
(a) 总路程。
(b) 行程结束时的位移。

#### Solution / 解答

**Step 1: Identify the path segments**
- Segment 1: 5 km east
- Segment 2: 5 km west

**Step 2: Calculate distance (a)**
$$ d = 5 + 5 = 10 \text{ km} $$

**Step 3: Calculate displacement (b)**
$$ \vec{s} = 5 \text{ km east} + 5 \text{ km west} = 5 \text{ km east} - 5 \text{ km east} = 0 \text{ km} $$

#### Final Answer / 最终答案

**Answer:**
(a) Distance = 10 km
(b) Displacement = 0 km (the cyclist returns to the starting point)

**答案:**
(a) 路程 = 10公里
(b) 位移 = 0公里（骑行者返回起点）

#### Quick Tip / 提示

**English:** A round trip always results in zero displacement (if you return to the start), but the distance traveled is never zero. This is a classic exam question to test understanding of the scalar vs vector distinction.

**中文:** 往返行程的位移总是零（如果返回起点），但路程永远不会是零。这是测试标量与矢量区别的经典考题。

---

## 7. Flashcards / 闪卡

**Flashcard 1:**
- Q (EN): What is the difference between distance and displacement?
- Q (CN): 路程和位移有什么区别？
- A (EN): Distance is a scalar quantity measuring the total path length traveled. Displacement is a vector quantity measuring the straight-line change in position from start to end, including direction.
- A (CN): 路程是标量，测量运动路径的总长度。位移是矢量，测量从起点到终点的直线位置变化，包含方向。

**Flashcard 2:**
- Q (EN): Is distance always greater than or equal to the magnitude of displacement?
- Q (CN): 路程总是大于或等于位移的大小吗？
- A (EN): Yes. The magnitude of displacement is always less than or equal to the distance traveled. Equality holds only for straight-line motion in one direction without changing direction.
- A (CN): 是的。位移的大小总是小于或等于路程。仅在不改变方向的直线运动中相等。

**Flashcard 3:**
- Q (EN): A person walks 3 m east, then 4 m north. What is the distance traveled and the magnitude of displacement?
- Q (CN): 一个人向东走3米，然后向北走4米。路程和位移大小各是多少？
- A (EN): Distance = 7 m. Displacement magnitude = 5 m (using Pythagoras: √(3² + 4²) = 5).
- A (CN): 路程 = 7米。位移大小 = 5米（使用勾股定理：√(3² + 4²) = 5）。

**Flashcard 4:**
- Q (EN): What is the displacement after a complete round trip?
- Q (CN): 完成一次完整的往返行程后，位移是多少？
- A (EN): Zero. Because the final position is the same as the initial position.
- A (CN): 零。因为最终位置与初始位置相同。

**Flashcard 5:**
- Q (EN): Which quantity is used to calculate average velocity: distance or displacement?
- Q (CN): 计算平均速度使用哪个量：路程还是位移？
- A (EN): Displacement. Average velocity = displacement / time. Distance is used for average speed.
- A (CN): 位移。平均速度 = 位移 / 时间。路程用于计算平均速率。

---

## 8. Metadata / 元数据

```yaml
title:
  en: Displacement and Distance
  cn: 位移与路程
parent_topic: Displacement, Velocity and Acceleration
parent_hub: "[[Displacement, Velocity and Acceleration]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: foundation
related_leaf_nodes:
  - "[[Speed and Velocity]]"
  - "[[Acceleration]]"
  - "[[Terminal Velocity]]"
prerequisites:
  - "[[Scalars and Vectors]]"
related_topics:
  - "[[Motion Graphs]]"
  - "[[Equations of Motion (SUVAT)]]"
language: bilingual_en_cn