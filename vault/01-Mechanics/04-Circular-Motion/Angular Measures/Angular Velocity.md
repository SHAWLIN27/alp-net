# 1. Overview / 概述

**English:**
Angular velocity is a fundamental concept in rotational mechanics that describes how fast an object rotates or revolves around a fixed axis. It is the rotational analogue of linear velocity and is essential for understanding circular motion, rotational dynamics, and periodic motion. This sub-topic introduces the definition, calculation, and physical significance of angular velocity, including its relationship with [[Period and Frequency]] and [[Radians and Angular Displacement]]. Angular velocity forms the foundation for more advanced topics like [[Centripetal Acceleration and Force]] and rotational kinetic energy.

**中文:**
角速度是旋转力学中的一个基本概念，描述物体绕固定轴旋转或公转的快慢。它是线速度的旋转类比，对于理解圆周运动、旋转动力学和周期运动至关重要。本子知识点介绍角速度的定义、计算和物理意义，包括它与[[周期与频率]]和[[弧度与角位移]]的关系。角速度为更高级的主题如[[向心加速度与向心力]]和旋转动能奠定基础。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 14.1(a) Define radian and understand angular displacement | 5.1 Define angular velocity (ω) as rate of change of angular displacement |
| 14.1(b) Understand angular velocity (ω) as rate of change of angular displacement | 5.2 Use ω = Δθ/Δt for uniform angular velocity |
| 14.1(c) Use ω = 2π/T = 2πf | 5.3 Derive and use ω = 2π/T = 2πf |
| 14.1(d) Understand that angular velocity is a vector quantity (direction along axis) | 5.4 Understand direction of angular velocity vector (right-hand rule) |
| 14.1(e) Solve problems involving angular velocity in circular motion | — |

**Examiner Expectations / 考官期望:**
- **CAIE:** Students must be able to define angular velocity, derive ω = 2π/T, and apply it to problems involving uniform circular motion. Understanding that angular velocity is a vector (direction given by right-hand rule) is required.
- **Edexcel:** Students must define angular velocity, derive relationships with period and frequency, and apply to real-world contexts like rotating machinery and planetary motion.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Angular Velocity** / 角速度 | The rate of change of angular displacement with respect to time. A vector quantity directed along the axis of rotation. | 角位移随时间的变化率。矢量，方向沿旋转轴。 | Confusing with angular speed (scalar). Angular velocity has direction. |
| **Angular Displacement** / 角位移 | The angle through which an object rotates about a fixed axis, measured in radians. | 物体绕固定轴旋转的角度，以弧度为单位。 | Forgetting to use radians instead of degrees. |
| **Period (T)** / 周期 | The time taken for one complete revolution or cycle. | 完成一次完整旋转或循环所需的时间。 | Confusing period with frequency. |
| **Frequency (f)** / 频率 | The number of complete revolutions or cycles per unit time. | 单位时间内完成的完整旋转或循环次数。 | Using Hz incorrectly for non-periodic motion. |
| **Radians** / 弧度 | The SI unit of angular measure, defined as the angle subtended at the center of a circle by an arc equal in length to the radius. | 角度的SI单位，定义为弧长等于半径时在圆心所张的角度。 | Not converting degrees to radians in calculations. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Definition of Angular Velocity / 角速度的定义

### Explanation / 解释
**English:**
Angular velocity (ω) is defined as the rate of change of [[Angular Displacement]] (θ) with respect to time (t). For uniform circular motion, where the angular velocity is constant:

$$ \omega = \frac{\Delta \theta}{\Delta t} $$

where Δθ is the angular displacement in radians and Δt is the time interval. The SI unit of angular velocity is radians per second (rad s⁻¹).

Angular velocity is a **vector quantity**. Its direction is given by the **right-hand rule**: curl the fingers of your right hand in the direction of rotation; your thumb points in the direction of the angular velocity vector, which is along the axis of rotation.

**中文:**
角速度 (ω) 定义为[[角位移]] (θ) 随时间 (t) 的变化率。对于匀速圆周运动，角速度恒定：

$$ \omega = \frac{\Delta \theta}{\Delta t} $$

其中 Δθ 是以弧度表示的角位移，Δt 是时间间隔。角速度的SI单位是弧度每秒 (rad s⁻¹)。

角速度是一个**矢量**。其方向由**右手定则**确定：将右手手指弯曲指向旋转方向；拇指指向角速度矢量的方向，即沿旋转轴方向。

### Physical Meaning / 物理意义
**English:**
Angular velocity tells us how fast an object is rotating. A higher angular velocity means the object completes more radians per second. For example, a spinning top has angular velocity; the Earth's rotation gives it an angular velocity of approximately 7.27 × 10⁻⁵ rad s⁻¹.

**中文:**
角速度告诉我们物体旋转的快慢。角速度越高，物体每秒完成的弧度数越多。例如，旋转的陀螺具有角速度；地球自转的角速度约为 7.27 × 10⁻⁵ rad s⁻¹。

### Common Misconceptions / 常见误区
- **Mistaking angular speed for angular velocity:** Angular speed is the magnitude of angular velocity. Angular velocity includes direction.
- **Forgetting units:** Always use rad s⁻¹, not degrees per second.
- **Assuming constant angular velocity:** In non-uniform circular motion, angular acceleration exists.

### Exam Tips / 考试提示
- **CAIE:** Always convert degrees to radians before using ω = Δθ/Δt.
- **Edexcel:** Be prepared to derive ω = 2π/T from the definition.

## 4.2 Relationship with Period and Frequency / 与周期和频率的关系

### Explanation / 解释
**English:**
For an object in uniform circular motion, one complete revolution corresponds to an angular displacement of 2π radians. The time for one revolution is the period T. Therefore:

$$ \omega = \frac{2\pi}{T} $$

Since frequency f = 1/T, we also have:

$$ \omega = 2\pi f $$

These relationships are crucial for connecting rotational motion to periodic motion.

**中文:**
对于匀速圆周运动的物体，一次完整旋转对应 2π 弧度的角位移。一次旋转所需的时间是周期 T。因此：

$$ \omega = \frac{2\pi}{T} $$

由于频率 f = 1/T，我们还有：

$$ \omega = 2\pi f $$

这些关系对于将旋转运动与周期运动联系起来至关重要。

### Physical Meaning / 物理意义
**English:**
These equations show that angular velocity is directly proportional to frequency and inversely proportional to period. A higher frequency means more rotations per second, hence higher angular velocity.

**中文:**
这些方程表明角速度与频率成正比，与周期成反比。频率越高意味着每秒旋转次数越多，因此角速度越大。

### Common Misconceptions / 常见误区
- **Using degrees instead of radians:** Always use 2π rad for one revolution.
- **Confusing T and f:** Remember T = 1/f and f = 1/T.

### Exam Tips / 考试提示
- **CAIE:** Derive ω = 2π/T from first principles in exam answers.
- **Edexcel:** Use ω = 2πf when frequency is given directly.

---

# 5. Essential Equations / 核心公式

## Equation 1: Definition of Angular Velocity / 角速度定义

$$ \omega = \frac{\Delta \theta}{\Delta t} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| ω | Angular velocity | 角速度 | rad s⁻¹ |
| Δθ | Angular displacement | 角位移 | rad |
| Δt | Time interval | 时间间隔 | s |

**Derivation / 推导:** Direct from definition.
**Conditions / 适用条件:** Uniform angular velocity (constant ω).
**Limitations / 局限性:** Does not apply to non-uniform circular motion without modification.

## Equation 2: Angular Velocity and Period / 角速度与周期

$$ \omega = \frac{2\pi}{T} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| ω | Angular velocity | 角速度 | rad s⁻¹ |
| T | Period | 周期 | s |

**Derivation / 推导:** For one complete revolution, Δθ = 2π rad and Δt = T. Substituting into ω = Δθ/Δt gives ω = 2π/T.
**Conditions / 适用条件:** Uniform circular motion.
**Limitations / 局限性:** Only valid for complete revolutions.

## Equation 3: Angular Velocity and Frequency / 角速度与频率

$$ \omega = 2\pi f $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| ω | Angular velocity | 角速度 | rad s⁻¹ |
| f | Frequency | 频率 | Hz (s⁻¹) |

**Derivation / 推导:** Since f = 1/T, substitute into ω = 2π/T.
**Conditions / 适用条件:** Uniform circular motion.
**Limitations / 局限性:** Only valid for periodic motion.

> 📷 **IMAGE PROMPT — EQ01: Angular Velocity Definition Diagram**
> A diagram showing a rotating object with angular displacement Δθ marked, a time interval Δt, and the formula ω = Δθ/Δt displayed. Include a circular path with radius r, the object at two positions, and the angle between them labeled.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Angular Displacement vs Time / 角位移-时间图

### Axes / 坐标轴
- **X-axis:** Time (t) / 时间 (t)
- **Y-axis:** Angular displacement (θ) / 角位移 (θ)

### Shape / 形状
- **Uniform angular velocity:** Straight line through origin with positive gradient.
- **Non-uniform:** Curved line (parabolic for constant angular acceleration).

### Gradient Meaning / 斜率含义
- Gradient = Δθ/Δt = ω (angular velocity)

### Area Meaning / 面积含义
- Area under graph has no direct physical meaning for this graph.

### Exam Interpretation / 考试解读
- **CAIE:** Calculate angular velocity from gradient of θ-t graph.
- **Edexcel:** Use gradient to find ω for uniform motion.

```mermaid
graph LR
    A[θ-t Graph] --> B[Gradient = ω]
    B --> C[Constant ω: Straight line]
    B --> D[Changing ω: Curved line]
```

## 6.2 Angular Velocity vs Time / 角速度-时间图

### Axes / 坐标轴
- **X-axis:** Time (t) / 时间 (t)
- **Y-axis:** Angular velocity (ω) / 角速度 (ω)

### Shape / 形状
- **Uniform angular velocity:** Horizontal line (constant ω).
- **Constant angular acceleration:** Straight line with positive gradient.

### Gradient Meaning / 斜率含义
- Gradient = Δω/Δt = α (angular acceleration)

### Area Meaning / 面积含义
- Area under graph = angular displacement (θ)

### Exam Interpretation / 考试解读
- **CAIE:** Use area to find total angular displacement.
- **Edexcel:** Calculate angular acceleration from gradient.

---

# 7. Required Diagrams / 必备图表

## 7.1 Angular Velocity Direction (Right-Hand Rule) / 角速度方向（右手定则）

### Description / 描述
**English:** A diagram showing a rotating object (e.g., a wheel or disc) with the axis of rotation. The right-hand rule is illustrated: fingers curl in direction of rotation, thumb points in direction of angular velocity vector.

**中文:** 显示旋转物体（如轮子或圆盘）及旋转轴的示意图。展示右手定则：手指弯曲指向旋转方向，拇指指向角速度矢量方向。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG01: Right-Hand Rule for Angular Velocity**
> A 3D diagram of a rotating disc with a central axis. A right hand is shown with fingers curled in the direction of rotation (clockwise or counterclockwise) and thumb pointing upward along the axis. Label "ω" with an arrow pointing along the axis. Use clear colors: blue for rotation direction arrows, red for ω vector. Include labels: "Axis of Rotation", "Direction of Rotation", "Angular Velocity ω".

### Labels Required / 需要标注
- Axis of rotation / 旋转轴
- Direction of rotation / 旋转方向
- Angular velocity vector (ω) / 角速度矢量 (ω)
- Right hand / 右手

### Exam Importance / 考试重要性
- **CAIE:** Required for understanding vector nature of angular velocity.
- **Edexcel:** Essential for applying right-hand rule in problems.

## 7.2 Angular Displacement in Circular Motion / 圆周运动中的角位移

### Description / 描述
**English:** A diagram showing an object moving in a circular path, with angular displacement θ marked between two positions. The radius r and arc length s are also shown.

**中文:** 显示物体在圆形路径上运动的示意图，标出两个位置之间的角位移 θ，同时显示半径 r 和弧长 s。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG02: Angular Displacement in Circular Motion**
> A circle with center O. An object at two positions A and B on the circumference. Draw radii OA and OB. Label the angle between them as θ (in radians). Draw the arc AB and label it s. Include labels: "Center O", "Radius r", "Arc length s", "Angular displacement θ". Use arrows to show direction of motion.

### Labels Required / 需要标注
- Center O / 圆心 O
- Radius r / 半径 r
- Arc length s / 弧长 s
- Angular displacement θ / 角位移 θ
- Positions A and B / 位置 A 和 B

### Exam Importance / 考试重要性
- **CAIE:** Foundation for understanding ω = Δθ/Δt.
- **Edexcel:** Used in deriving v = rω.

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Angular Velocity / 计算角速度

### Question / 题目
**English:**
A fan blade rotates through an angle of 120° in 0.50 seconds. Calculate the angular velocity of the fan blade in rad s⁻¹.

**中文:**
风扇叶片在 0.50 秒内旋转 120°。计算风扇叶片的角速度，单位为 rad s⁻¹。

### Solution / 解答
**Step 1:** Convert angle from degrees to radians.
$$ \theta = 120^\circ \times \frac{\pi}{180^\circ} = \frac{2\pi}{3} \text{ rad} $$

**Step 2:** Use the definition of angular velocity.
$$ \omega = \frac{\Delta \theta}{\Delta t} = \frac{2\pi/3}{0.50} = \frac{2\pi}{3 \times 0.50} = \frac{2\pi}{1.5} $$

**Step 3:** Calculate numerical value.
$$ \omega = \frac{2 \times 3.1416}{1.5} = 4.19 \text{ rad s}^{-1} $$

### Final Answer / 最终答案
**Answer:** ω = 4.19 rad s⁻¹ | **答案：** ω = 4.19 rad s⁻¹

### Quick Tip / 提示
**English:** Always convert degrees to radians before using ω = Δθ/Δt. Remember: 180° = π rad.
**中文:** 在使用 ω = Δθ/Δt 之前，务必先将角度转换为弧度。记住：180° = π rad。

## Example 2: Angular Velocity from Period / 从周期计算角速度

### Question / 题目
**English:**
A satellite orbits the Earth with a period of 90 minutes. Calculate its angular velocity in rad s⁻¹.

**中文:**
一颗卫星绕地球运行的周期为 90 分钟。计算其角速度，单位为 rad s⁻¹。

### Solution / 解答
**Step 1:** Convert period to seconds.
$$ T = 90 \text{ min} \times 60 \text{ s/min} = 5400 \text{ s} $$

**Step 2:** Use ω = 2π/T.
$$ \omega = \frac{2\pi}{T} = \frac{2\pi}{5400} $$

**Step 3:** Calculate numerical value.
$$ \omega = \frac{2 \times 3.1416}{5400} = 1.16 \times 10^{-3} \text{ rad s}^{-1} $$

### Final Answer / 最终答案
**Answer:** ω = 1.16 × 10⁻³ rad s⁻¹ | **答案：** ω = 1.16 × 10⁻³ rad s⁻¹

### Quick Tip / 提示
**English:** When using ω = 2π/T, ensure T is in seconds. For frequency, use ω = 2πf.
**中文:** 使用 ω = 2π/T 时，确保 T 的单位是秒。对于频率，使用 ω = 2πf。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate ω from Δθ and Δt | High | Easy | 📝 *待填入* |
| Derive ω = 2π/T | Medium | Medium | 📝 *待填入* |
| Convert between ω, T, f | High | Easy | 📝 *待填入* |
| Right-hand rule direction | Low | Medium | 📝 *待填入* |
| ω in context of centripetal force | High | Medium-Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Define / 定义:** State the meaning precisely (e.g., "Define angular velocity")
- **Calculate / 计算:** Use formula to find numerical value
- **Derive / 推导:** Show step-by-step mathematical derivation
- **State / 陈述:** Give a brief answer without explanation
- **Explain / 解释:** Provide reasoning with physics principles

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Angular velocity is measured in practical contexts using:
- **Stroboscope:** Measure frequency of rotation, then calculate ω = 2πf.
- **Light gate and data logger:** Measure time for one revolution to find T, then ω = 2π/T.
- **Video analysis:** Track angular displacement over time using software.

**Uncertainties:**
- Uncertainty in ω comes from uncertainties in Δθ and Δt.
- For ω = 2π/T, percentage uncertainty in ω equals percentage uncertainty in T.

**Graph plotting:**
- Plot θ vs t to find ω from gradient.
- Plot ω vs t to find angular acceleration from gradient.

**Experimental design:**
- Use a rotating platform with a marker to measure angular displacement.
- Use a protractor for angle measurement (uncertainty ±1°).

**中文:**
角速度在实验中的测量方法包括：
- **频闪仪：** 测量旋转频率，然后计算 ω = 2πf。
- **光门和数据记录器：** 测量一次旋转的时间以求得 T，然后 ω = 2π/T。
- **视频分析：** 使用软件追踪角位移随时间的变化。

**不确定度：**
- ω 的不确定度来自 Δθ 和 Δt 的不确定度。
- 对于 ω = 2π/T，ω 的百分比不确定度等于 T 的百分比不确定度。

**图表绘制：**
- 绘制 θ-t 图，从斜率求 ω。
- 绘制 ω-t 图，从斜率求角加速度。

**实验设计：**
- 使用带有标记的旋转平台测量角位移。
- 使用量角器测量角度（不确定度 ±1°）。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Angular Velocity Concept Map
    AV[Angular Velocity ω] --> DEF[Definition: ω = Δθ/Δt]
    AV --> REL[Relationships]
    AV --> DIR[Direction: Right-Hand Rule]
    
    REL --> PER[ω = 2π/T]
    REL --> FREQ[ω = 2πf]
    
    DEF --> AD[Angular Displacement θ]
    DEF --> TIME[Time t]
    
    AD --> RAD[Radians]
    AD --> ARC[Arc Length s = rθ]
    
    PER --> T[Period]
    FREQ --> F[Frequency]
    
    DIR --> AXIS[Axis of Rotation]
    
    AV --> LIN[Linear Velocity v = rω]
    LIN --> [[Relationship Between Linear and Angular Quantities]]
    
    AV --> CENT[Centripetal Acceleration a = rω²]
    CENT --> [[Centripetal Acceleration and Force]]
    
    AV --> PREREQ[[Displacement, Velocity and Acceleration]]
    
    style AV fill:#f9f,stroke:#333,stroke-width:2px
    style DEF fill:#bbf,stroke:#333,stroke-width:1px
    style REL fill:#bbf,stroke:#333,stroke-width:1px
    style DIR fill:#bbf,stroke:#333,stroke-width:1px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | ω = Δθ/Δt, where Δθ in radians, Δt in seconds. Vector quantity. |
| **Key Formula / 核心公式** | ω = 2π/T = 2πf |
| **Key Graph / 核心图表** | θ-t graph: gradient = ω; ω-t graph: gradient = α, area = θ |
| **Unit / 单位** | rad s⁻¹ (radians per second) |
| **Direction / 方向** | Right-hand rule: thumb points along axis of rotation |
| **Common Mistake / 常见错误** | Using degrees instead of radians; confusing ω with linear velocity |
| **Exam Tip / 考试提示** | Always convert to radians; derive ω = 2π/T from first principles |
| **Related Topics / 相关主题** | [[Radians and Angular Displacement]], [[Period and Frequency]], [[Relationship Between Linear and Angular Quantities]], [[Centripetal Acceleration and Force]] |
| **Prerequisites / 前置知识** | [[Displacement, Velocity and Acceleration]] |