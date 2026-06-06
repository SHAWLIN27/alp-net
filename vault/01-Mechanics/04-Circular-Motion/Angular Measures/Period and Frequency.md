# 1. Overview / 概述

**English:**
Period and Frequency are two fundamental, reciprocal concepts that describe how quickly an object completes one full cycle of circular motion. They form the temporal backbone of [[Angular Measures]], providing the time dimension to rotational dynamics. Period ($T$) is the time taken for one complete revolution, while Frequency ($f$) is the number of complete revolutions per second. These concepts are essential for linking circular motion to [[Angular Velocity]] and later to [[Centripetal Acceleration and Force]]. Understanding the relationship $T = 1/f$ is critical for solving problems involving rotational timing, from simple pendulums to planetary orbits.

**中文:**
周期和频率是两个基本且互为倒数的概念，描述物体完成一个完整圆周运动的速度。它们构成了 [[Angular Measures]] 的时间基础，为旋转动力学提供了时间维度。周期 ($T$) 是完成一次完整旋转所需的时间，而频率 ($f$) 是每秒完成的完整旋转次数。这些概念对于将圆周运动与 [[Angular Velocity]] 以及后续的 [[Centripetal Acceleration and Force]] 联系起来至关重要。理解 $T = 1/f$ 的关系对于解决涉及旋转时间的问题（从简单的单摆到行星轨道）至关重要。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Period** / 周期 | The time taken for one complete cycle of motion. | 完成一个完整运动周期所需的时间。 |
| **Frequency** / 频率 | The number of complete cycles of motion per unit time. | 单位时间内完成的完整运动周期数。 |
| **Cycle** / 周期（循环） | One complete revolution or oscillation, returning to the starting state. | 一次完整的旋转或振荡，回到起始状态。 |
| **Reciprocal** / 倒数 | Two quantities whose product equals 1. | 乘积等于1的两个量。 |
| **Hertz (Hz)** / 赫兹 | The SI unit of frequency, equivalent to $s^{-1}$. | 频率的国际单位制单位，等于 $s^{-1}$。 |

---

# 3. Key Concepts / 关键概念

**English:**
Period and Frequency are **inversely proportional** to each other. This means that as one increases, the other decreases proportionally. For example, if a wheel completes 10 revolutions per second ($f = 10 \text{ Hz}$), then each revolution takes $T = 0.1 \text{ s}$.

The relationship is derived from the definition of frequency: if $f$ cycles occur in 1 second, then 1 cycle takes $1/f$ seconds. Therefore:
$$ T = \frac{1}{f} \quad \text{and} \quad f = \frac{1}{T} $$

**Physical Interpretation:**
- **Period** is a measure of "how long" — it answers "How much time does one rotation take?"
- **Frequency** is a measure of "how often" — it answers "How many rotations happen per second?"

**Common Pitfalls:**
1. **Confusing units**: Period is measured in seconds (s), not Hz. Frequency is measured in Hz ($s^{-1}$).
2. **Forgetting the reciprocal relationship**: Students often mistakenly add or multiply $T$ and $f$ instead of using $T = 1/f$.
3. **Mixing with angular velocity**: While related, $T$ and $f$ are not the same as [[Angular Velocity]] ($\omega$). The connection is $\omega = 2\pi f = \frac{2\pi}{T}$.

**Connection to [[Displacement, Velocity and Acceleration]]:**
In linear motion, we talk about time intervals. Period and Frequency extend this idea to repetitive circular motion, where the "displacement" is angular and repeats every cycle.

**中文:**
周期和频率是**反比关系**。这意味着当一个增加时，另一个按比例减少。例如，如果一个轮子每秒完成10次旋转 ($f = 10 \text{ Hz}$)，那么每次旋转需要 $T = 0.1 \text{ s}$。

这个关系源于频率的定义：如果 $f$ 个周期在1秒内发生，那么1个周期需要 $1/f$ 秒。因此：
$$ T = \frac{1}{f} \quad \text{and} \quad f = \frac{1}{T} $$

**物理意义：**
- **周期** 衡量"多久"——回答"一次旋转需要多少时间？"
- **频率** 衡量"多频繁"——回答"每秒发生多少次旋转？"

**常见错误：**
1. **混淆单位**：周期以秒 (s) 为单位，不是 Hz。频率以 Hz ($s^{-1}$) 为单位。
2. **忘记倒数关系**：学生常常错误地加减 $T$ 和 $f$，而不是使用 $T = 1/f$。
3. **与角速度混淆**：虽然相关，$T$ 和 $f$ 不同于 [[Angular Velocity]] ($\omega$)。联系是 $\omega = 2\pi f = \frac{2\pi}{T}$。

**与 [[Displacement, Velocity and Acceleration]] 的联系：**
在线性运动中，我们讨论时间间隔。周期和频率将这个想法扩展到重复的圆周运动，其中"位移"是角度的，并且每个周期重复。

---

# 4. Formulas / 公式

## Primary Formula: Period-Frequency Relationship

$$ T = \frac{1}{f} \quad \text{or} \quad f = \frac{1}{T} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $T$ | Period | 周期 | s (秒) |
| $f$ | Frequency | 频率 | Hz ($s^{-1}$) |

## Derived Formula: Connection to Angular Velocity

$$ \omega = 2\pi f = \frac{2\pi}{T} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $\omega$ | Angular velocity | 角速度 | rad $s^{-1}$ |
| $f$ | Frequency | 频率 | Hz |
| $T$ | Period | 周期 | s |

**Derivation / 推导:**
In one complete cycle, the angular displacement is $2\pi$ radians. Angular velocity is defined as angular displacement per unit time:
$$ \omega = \frac{\Delta \theta}{\Delta t} $$
For one cycle: $\Delta \theta = 2\pi$ rad and $\Delta t = T$ s, so:
$$ \omega = \frac{2\pi}{T} = 2\pi f $$

**Conditions / 适用条件:**
- Applies to **uniform circular motion** (constant speed)
- The motion must be **periodic** (repeating at regular intervals)
- Valid for any system where one complete cycle corresponds to $2\pi$ radians of angular displacement

> 📷 **IMAGE PROMPT — PF01: Period and Frequency Relationship Diagram**
>
> **English Prompt:**
> A clean, textbook-style vector diagram showing two side-by-side illustrations. Left side: A clock face with a second hand completing one full rotation, labeled "T = 60 s" with an arrow showing the full circle. Right side: A series of clock faces showing 1 second intervals, with the second hand at different positions, labeled "f = 1/60 Hz". Below both, a simple graph showing T vs f as a hyperbolic curve (T = 1/f), with labeled axes (T in seconds on y-axis, f in Hz on x-axis). Use blue for period-related elements and red for frequency-related elements. Include a small box with the formula T = 1/f. Style: clean vector illustration, white background, suitable for A-Level textbook.
>
> **中文描述:**
> 一个干净的教科书风格矢量图，显示两个并排的插图。左侧：一个时钟面，秒针完成一次完整旋转，标注"T = 60 s"，箭头显示完整圆圈。右侧：一系列时钟面显示1秒间隔，秒针在不同位置，标注"f = 1/60 Hz"。下方是一个简单的T vs f双曲线图（T = 1/f），坐标轴标注（y轴T以秒为单位，x轴f以Hz为单位）。周期相关元素用蓝色，频率相关元素用红色。包含一个带有公式T = 1/f的小框。风格：干净矢量图，白色背景，适合A-Level教科书。
>
> **Labels Required / 需要标注:**
> * T = 60 s (on left clock)
> * f = 1/60 Hz (on right clocks)
> * T = 1/f (formula box)
> * Axes: T (s) and f (Hz)
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> Helps students visualize the reciprocal relationship and understand that period and frequency describe the same motion from different perspectives.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — PF02: Real-World Examples of Period and Frequency**
>
> **English Prompt:**
> A split-screen educational diagram showing three real-world examples of periodic motion with their T and f values. Top panel: A Ferris wheel with one cabin highlighted, showing T = 30 s, f = 1/30 Hz. Middle panel: A spinning bicycle wheel with a marked spoke, showing T = 0.5 s, f = 2 Hz. Bottom panel: A rotating fan blade with a marked tip, showing T = 0.1 s, f = 10 Hz. Each example has a small clock icon showing the period duration and a counter showing frequency. Use consistent color coding: blue for period, red for frequency. Include a summary table at the bottom with columns: Object, T (s), f (Hz). Style: clean educational infographic, realistic 3D render style, white background.
>
> **中文描述:**
> 一个分屏教育图，显示三个周期性运动的真实世界示例及其T和f值。顶部面板：摩天轮，一个座舱被高亮，显示T = 30 s，f = 1/30 Hz。中间面板：旋转的自行车轮，一个辐条被标记，显示T = 0.5 s，f = 2 Hz。底部面板：旋转的风扇叶片，一个尖端被标记，显示T = 0.1 s，f = 10 Hz。每个示例有一个小时钟图标显示周期持续时间，一个计数器显示频率。使用一致的颜色编码：蓝色代表周期，红色代表频率。底部包含一个汇总表，列：物体、T (s)、f (Hz)。风格：干净的教育信息图，逼真的3D渲染风格，白色背景。
>
> **Labels Required / 需要标注:**
> * Ferris wheel: T = 30 s, f = 1/30 Hz
> * Bicycle wheel: T = 0.5 s, f = 2 Hz
> * Fan blade: T = 0.1 s, f = 10 Hz
> * Summary table with values
>
> **Style / 风格:** 3D render / educational infographic
>
> **Exam Relevance / 考试关联:**
> Helps students connect abstract concepts to familiar real-world objects, making it easier to estimate reasonable values in exam problems.

---

# 6. Worked Example / 典型例题

### Example 1: Basic Period-Frequency Conversion

### Question / 题目
**English:** A ceiling fan rotates at a frequency of 5 Hz. Calculate:
(a) The period of rotation.
(b) The number of complete rotations the fan makes in 2 minutes.

**中文:** 一个吊扇以5 Hz的频率旋转。计算：
(a) 旋转周期。
(b) 风扇在2分钟内完成的完整旋转次数。

### Solution / 解答

**(a) Period calculation:**
Using $T = \frac{1}{f}$:
$$ T = \frac{1}{5 \text{ Hz}} = 0.2 \text{ s} $$

**(b) Number of rotations in 2 minutes:**
First, convert 2 minutes to seconds: $2 \text{ min} = 2 \times 60 = 120 \text{ s}$

Number of rotations = Frequency × Time
$$ N = f \times t = 5 \text{ Hz} \times 120 \text{ s} = 600 \text{ rotations} $$

Alternatively, using period:
$$ N = \frac{t}{T} = \frac{120 \text{ s}}{0.2 \text{ s}} = 600 \text{ rotations} $$

### Final Answer / 最终答案
**Answer:** (a) $T = 0.2 \text{ s}$ (b) 600 rotations
**答案:** (a) $T = 0.2 \text{ s}$ (b) 600次旋转

### Quick Tip / 提示
Always check units: if time is given in minutes, convert to seconds before using formulas. Remember that frequency in Hz means "per second", so time must be in seconds.

---

### Example 2: Connecting Period to Angular Velocity

### Question / 题目
**English:** A satellite orbits Earth with a period of 90 minutes. Calculate:
(a) The frequency of the satellite's orbit in Hz.
(b) The angular velocity of the satellite in rad $s^{-1}$.

**中文:** 一颗卫星以90分钟的周期绕地球运行。计算：
(a) 卫星轨道的频率（以Hz为单位）。
(b) 卫星的角速度（以rad $s^{-1}$为单位）。

### Solution / 解答

**(a) Frequency calculation:**
First, convert period to seconds:
$$ T = 90 \text{ min} = 90 \times 60 = 5400 \text{ s} $$

Using $f = \frac{1}{T}$:
$$ f = \frac{1}{5400 \text{ s}} = 1.85 \times 10^{-4} \text{ Hz} $$

**(b) Angular velocity:**
Using $\omega = \frac{2\pi}{T}$:
$$ \omega = \frac{2\pi}{5400 \text{ s}} = 1.16 \times 10^{-3} \text{ rad } s^{-1} $$

Alternatively, using $\omega = 2\pi f$:
$$ \omega = 2\pi \times (1.85 \times 10^{-4}) = 1.16 \times 10^{-3} \text{ rad } s^{-1} $$

### Final Answer / 最终答案
**Answer:** (a) $f = 1.85 \times 10^{-4} \text{ Hz}$ (b) $\omega = 1.16 \times 10^{-3} \text{ rad } s^{-1}$
**答案:** (a) $f = 1.85 \times 10^{-4} \text{ Hz}$ (b) $\omega = 1.16 \times 10^{-3} \text{ rad } s^{-1}$

### Quick Tip / 提示
When dealing with large periods (like orbital periods), the frequency becomes very small. Use scientific notation and be careful with unit conversions. The connection $\omega = 2\pi/T$ is often more direct than going through frequency.

---

# 7. Flashcards / 闪卡

**Flashcard 1:**
Q (EN): What is the relationship between period (T) and frequency (f)?
Q (CN): 周期 (T) 和频率 (f) 之间的关系是什么？
A (EN): They are reciprocals: $T = 1/f$ and $f = 1/T$.
A (CN): 它们互为倒数：$T = 1/f$ 和 $f = 1/T$。

**Flashcard 2:**
Q (EN): What are the SI units for period and frequency?
Q (CN): 周期和频率的国际单位制单位是什么？
A (EN): Period is measured in seconds (s). Frequency is measured in hertz (Hz), which is equivalent to $s^{-1}$.
A (CN): 周期以秒 (s) 为单位。频率以赫兹 (Hz) 为单位，等于 $s^{-1}$。

**Flashcard 3:**
Q (EN): How do you calculate angular velocity ($\omega$) from period (T) or frequency (f)?
Q (CN): 如何从周期 (T) 或频率 (f) 计算角速度 ($\omega$)？
A (EN): $\omega = 2\pi f = \frac{2\pi}{T}$
A (CN): $\omega = 2\pi f = \frac{2\pi}{T}$

**Flashcard 4:**
Q (EN): If a wheel completes 20 rotations in 5 seconds, what are its frequency and period?
Q (CN): 如果一个轮子在5秒内完成20次旋转，它的频率和周期是多少？
A (EN): Frequency $f = 20/5 = 4$ Hz. Period $T = 1/4 = 0.25$ s.
A (CN): 频率 $f = 20/5 = 4$ Hz。周期 $T = 1/4 = 0.25$ s。

**Flashcard 5:**
Q (EN): What is the physical meaning of period and frequency?
Q (CN): 周期和频率的物理意义是什么？
A (EN): Period is the time for one complete cycle. Frequency is the number of complete cycles per second.
A (CN): 周期是完成一个完整周期所需的时间。频率是每秒完成的完整周期数。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Period and Frequency
  cn: 周期与频率
parent_topic: Angular Measures
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
  - "[[Relationship Between Linear and Angular Quantities]]"
  - "[[Centripetal Acceleration and Force]]"
prerequisites:
  - "[[Displacement, Velocity and Acceleration]]"
language: bilingual_en_cn