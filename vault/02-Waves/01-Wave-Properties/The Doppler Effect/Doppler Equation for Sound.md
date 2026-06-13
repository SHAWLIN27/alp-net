# 1. Overview / 概述

**English:**
The Doppler Equation for Sound is a mathematical relationship that quantifies the observed change in frequency (and wavelength) of a sound wave when there is relative motion between the source and the observer. This equation is the core quantitative tool within the broader [[The Doppler Effect]] topic. It allows us to calculate the exact frequency heard by a stationary observer when a sound source moves, or by a moving observer relative to a stationary source, or when both are moving. Understanding this equation is crucial for applications ranging from police radar guns and medical ultrasound to understanding the sonic boom. This sub-topic builds directly on the conceptual understanding from [[The Doppler Effect Explained]] and requires a solid grasp of [[Progressive Waves]], particularly wave speed, frequency, and wavelength relationships.

**中文:**
多普勒声波方程是一个数学关系式，用于量化当声源和观察者之间存在相对运动时，观察到的声波频率（和波长）的变化。这个方程是更广泛的[[The Doppler Effect]]主题中的核心定量工具。它使我们能够计算当声源移动时静止观察者听到的确切频率，或者当观察者相对于静止声源移动时，或者当两者都移动时的频率。理解这个方程对于从警用雷达测速枪和医学超声到理解音爆等应用至关重要。本子知识点直接建立在[[The Doppler Effect Explained]]的概念理解之上，并且需要扎实掌握[[Progressive Waves]]，特别是波速、频率和波长的关系。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 7.3(a) Recall and use the Doppler equation for sound: $f_o = \frac{f_s v}{v \pm v_s}$ | 5.9 Use the Doppler equation for sound: $f' = \frac{f v}{v \pm v_s}$ |
| 7.3(b) Determine the observed frequency when source moves towards/away from a stationary observer | 5.10 Determine observed frequency for a moving source or moving observer |
| 7.3(c) Determine the observed frequency when observer moves towards/away from a stationary source | 5.11 Explain the application of the Doppler effect to electromagnetic waves (e.g., radar) |
| 7.3(d) Explain the application of the Doppler effect to sound (e.g., speed traps, ultrasound) | |

**Examiner Expectations / 考官期望:**
- **English:** Students must correctly apply the sign convention in the Doppler equation. They must be able to identify whether the source or observer is moving and choose the correct sign (+ or -) in the denominator. They should also be able to rearrange the equation to solve for the source speed ($v_s$) or the observed frequency ($f_o$). Understanding that the equation applies only when the relative speed is much less than the speed of sound is a key limitation.
- **中文:** 学生必须正确应用多普勒方程中的符号约定。他们必须能够识别是声源还是观察者在移动，并选择分母中正确的符号（+ 或 -）。他们还应能够重新排列方程以求解声源速度 ($v_s$) 或观察到的频率 ($f_o$)。理解该方程仅适用于相对速度远小于声速的情况是一个关键限制条件。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Observed Frequency ($f_o$)** / 观察频率 | The frequency of the sound wave as measured by the observer. | 观察者测量到的声波频率。 | Confusing $f_o$ with the source frequency $f_s$. |
| **Source Frequency ($f_s$)** / 声源频率 | The frequency of the sound wave emitted by the source. | 声源发出的声波频率。 | Forgetting that $f_s$ is constant; only $f_o$ changes. |
| **Speed of Sound ($v$)** / 声速 | The speed at which sound waves travel through a medium (typically air at 340 m/s). | 声波在介质中传播的速度（通常在空气中为 340 m/s）。 | Using the speed of light or the speed of the source incorrectly. |
| **Source Speed ($v_s$)** / 声源速度 | The speed at which the source of the sound is moving relative to the medium (air). | 声源相对于介质（空气）移动的速度。 | Using the observer's speed instead of the source's speed. |
| **Observer Speed ($v_o$)** / 观察者速度 | The speed at which the observer is moving relative to the medium (air). | 观察者相对于介质（空气）移动的速度。 | Forgetting to include $v_o$ when the observer is moving. |
| **Relative Motion** / 相对运动 | The motion of the source and observer with respect to each other. | 声源和观察者相对于彼此的运动。 | Not considering the direction of motion (towards or away). |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Sign Convention / 符号约定

### Explanation / 解释
**English:** The Doppler equation for sound has a critical sign convention that determines whether the observed frequency is higher (pitch increase) or lower (pitch decrease). The general equation is:

$$ f_o = \frac{f_s (v \pm v_o)}{v \mp v_s} $$

The top sign ($\pm$) is for the observer's motion, and the bottom sign ($\mp$) is for the source's motion. The rule is:
- **Towards:** Use the top sign (+) for observer moving towards source; use the bottom sign (-) for source moving towards observer.
- **Away:** Use the top sign (-) for observer moving away from source; use the bottom sign (+) for source moving away from observer.

A simpler mnemonic: **"Towards = Top +, Bottom -"** and **"Away = Top -, Bottom +"**.

**中文:** 声波多普勒方程有一个关键的符号约定，它决定了观察到的频率是更高（音调升高）还是更低（音调降低）。通用方程是：

$$ f_o = \frac{f_s (v \pm v_o)}{v \mp v_s} $$

上面的符号 ($\pm$) 用于观察者的运动，下面的符号 ($\mp$) 用于声源的运动。规则是：
- **靠近：** 观察者靠近声源时用上面的加号 (+)；声源靠近观察者时用下面的减号 (-)。
- **远离：** 观察者远离声源时用上面的减号 (-)；声源远离观察者时用下面的加号 (+)。

一个更简单的记忆法：**“靠近 = 上 +，下 -”** 和 **“远离 = 上 -，下 +”**。

### Physical Meaning / 物理意义
**English:** When the source moves towards the observer, the wavefronts are compressed, leading to a shorter wavelength and higher frequency. When the observer moves towards the source, they encounter wavefronts more frequently, also leading to a higher frequency. The opposite happens when moving away.

**中文:** 当声源向观察者移动时，波前被压缩，导致波长变短、频率升高。当观察者向声源移动时，他们更频繁地遇到波前，同样导致频率升高。当远离时则相反。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking the sign convention is the same for both source and observer motion.
  - Forgetting that $v$ is the speed of sound in the medium, not the speed of the source or observer.
  - Applying the equation when the source speed exceeds the speed of sound (supersonic), where a shockwave (sonic boom) occurs instead.
- **中文:**
  - 认为声源和观察者运动的符号约定相同。
  - 忘记 $v$ 是介质中的声速，而不是声源或观察者的速度。
  - 当声源速度超过声速（超音速）时应用该方程，此时会发生激波（音爆）。

### Exam Tips / 考试提示
- **English:** Always draw a quick diagram showing the direction of motion. Write the equation and then substitute the correct signs based on whether the motion is towards or away. Check your final answer: if moving towards, $f_o > f_s$; if moving away, $f_o < f_s$.
- **中文:** 始终画一个简图显示运动方向。写出方程，然后根据是靠近还是远离代入正确的符号。检查最终答案：如果靠近，$f_o > f_s$；如果远离，$f_o < f_s$。

> 📷 **IMAGE PROMPT — DOPPLER-01: Sign Convention Diagram**
> A clear diagram showing a sound source (siren) moving to the right towards a stationary observer. Label the source speed $v_s$, speed of sound $v$, and show compressed wavefronts in front (shorter wavelength, higher frequency) and stretched wavefronts behind (longer wavelength, lower frequency). Include the equation with the correct sign: $f_o = \frac{f_s v}{v - v_s}$ for source moving towards observer.

---

# 5. Essential Equations / 核心公式

## 5.1 General Doppler Equation for Sound / 声波多普勒通用方程

$$ f_o = \frac{f_s (v \pm v_o)}{v \mp v_s} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $f_o$ | Observed frequency | 观察到的频率 | Hz |
| $f_s$ | Source frequency | 声源频率 | Hz |
| $v$ | Speed of sound in the medium | 介质中的声速 | m/s |
| $v_o$ | Speed of the observer relative to the medium | 观察者相对于介质的速度 | m/s |
| $v_s$ | Speed of the source relative to the medium | 声源相对于介质的速度 | m/s |

**Derivation / 推导:**
- **English:** The derivation is based on the relative speed of the wavefronts and the observer. For a stationary source and moving observer, the relative speed of sound is $v \pm v_o$, so $f_o = \frac{v \pm v_o}{\lambda} = \frac{f_s (v \pm v_o)}{v}$. For a moving source, the wavelength is compressed/stretched: $\lambda' = \frac{v \mp v_s}{f_s}$, so $f_o = \frac{v}{\lambda'} = \frac{f_s v}{v \mp v_s}$. Combining both gives the general form.
- **中文:** 推导基于波前和观察者的相对速度。对于静止声源和移动观察者，声波的相对速度为 $v \pm v_o$，所以 $f_o = \frac{v \pm v_o}{\lambda} = \frac{f_s (v \pm v_o)}{v}$。对于移动声源，波长被压缩/拉伸：$\lambda' = \frac{v \mp v_s}{f_s}$，所以 $f_o = \frac{v}{\lambda'} = \frac{f_s v}{v \mp v_s}$。结合两者得到通用形式。

**Conditions / 适用条件:**
- **English:** The equation applies only when $v_s < v$ (subsonic speeds). If $v_s \ge v$, a shockwave forms and the equation is invalid. The medium (air) is assumed to be stationary.
- **中文:** 该方程仅适用于 $v_s < v$（亚音速）的情况。如果 $v_s \ge v$，会形成激波，方程无效。假设介质（空气）是静止的。

**Limitations / 局限性:**
- **English:** Does not account for wind or air currents. Assumes the source and observer move along the same straight line. For electromagnetic waves (light), a different relativistic equation is needed (see [[Doppler Effect for Light (Redshift and Blueshift)]]).
- **中文:** 不考虑风或气流。假设声源和观察者沿同一直线运动。对于电磁波（光），需要不同的相对论方程（参见[[Doppler Effect for Light (Redshift and Blueshift)]]）。

## 5.2 Simplified Forms / 简化形式

**Stationary Observer, Moving Source / 静止观察者，移动声源:**
$$ f_o = \frac{f_s v}{v \mp v_s} $$
- **Towards:** $f_o = \frac{f_s v}{v - v_s}$ (denominator smaller → $f_o$ larger)
- **Away:** $f_o = \frac{f_s v}{v + v_s}$ (denominator larger → $f_o$ smaller)

**Stationary Source, Moving Observer / 静止声源，移动观察者:**
$$ f_o = \frac{f_s (v \pm v_o)}{v} $$
- **Towards:** $f_o = \frac{f_s (v + v_o)}{v}$ (numerator larger → $f_o$ larger)
- **Away:** $f_o = \frac{f_s (v - v_o)}{v}$ (numerator smaller → $f_o$ smaller)

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Observed Frequency vs. Source Speed / 观察频率与声源速度的关系

### Axes / 坐标轴
- **X-axis:** Source speed $v_s$ (m/s) — 声源速度 $v_s$ (m/s)
- **Y-axis:** Observed frequency $f_o$ (Hz) — 观察频率 $f_o$ (Hz)

### Shape / 形状
**English:** For a source moving towards a stationary observer, the graph is a curve that increases steeply as $v_s$ approaches $v$ (the speed of sound). The function is $f_o = \frac{f_s v}{v - v_s}$, which is a hyperbola. As $v_s \to v$, $f_o \to \infty$ (theoretically). For a source moving away, the graph is a decreasing curve: $f_o = \frac{f_s v}{v + v_s}$, approaching zero as $v_s \to \infty$.

**中文:** 对于向静止观察者移动的声源，该图是一条曲线，当 $v_s$ 接近 $v$（声速）时急剧上升。函数 $f_o = \frac{f_s v}{v - v_s}$ 是一条双曲线。当 $v_s \to v$ 时，$f_o \to \infty$（理论上）。对于远离的声源，该图是一条递减曲线：$f_o = \frac{f_s v}{v + v_s}$，当 $v_s \to \infty$ 时趋近于零。

### Gradient Meaning / 斜率含义
**English:** The gradient is not constant. It represents the rate of change of observed frequency with respect to source speed. The gradient is steeper when the source is moving towards the observer (especially near $v_s = v$) and shallower when moving away.

**中文:** 斜率不是常数。它表示观察频率随声源速度的变化率。当声源向观察者移动时（尤其是在 $v_s = v$ 附近），斜率更陡；当远离时，斜率更缓。

### Area Meaning / 面积含义
**English:** The area under the curve has no direct physical meaning in this context.

**中文:** 曲线下的面积在此上下文中没有直接的物理意义。

### Exam Interpretation / 考试解读
- **English:** Be able to sketch this graph qualitatively. Understand that the observed frequency increases without bound as the source approaches the speed of sound (theoretically), but in reality, a sonic boom occurs before this limit.
- **中文:** 能够定性地画出此图。理解当声源接近声速时，观察频率理论上会无限增加，但实际上在此之前会发生音爆。

> 📷 **IMAGE PROMPT — DOPPLER-02: f_o vs v_s Graph**
> A graph with two curves. One curve (towards) rises steeply from $f_s$ at $v_s=0$ and approaches a vertical asymptote at $v_s = v$. The other curve (away) decreases from $f_s$ and approaches zero. Label the asymptote at $v_s = v$ and mark the region $v_s > v$ as "Shockwave / Sonic Boom".

---

# 7. Required Diagrams / 必备图表

## 7.1 Wavefront Compression and Stretching / 波前压缩与拉伸

### Description / 描述
**English:** A diagram showing a moving sound source (e.g., a car with a siren) emitting circular wavefronts. The wavefronts are closer together (compressed) in the direction of motion and farther apart (stretched) behind the source. This illustrates why the observed frequency is higher in front and lower behind.

**中文:** 一个显示移动声源（例如，带有警报器的汽车）发出圆形波前的图表。波前在运动方向上更紧密（压缩），在声源后面更稀疏（拉伸）。这说明了为什么在前方观察到的频率更高，在后方更低。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DOPPLER-03: Wavefront Compression**
> A top-down view of a car moving to the right. Concentric circular wavefronts are emitted from the car's current position. The wavefronts in front of the car are closer together (smaller spacing), and those behind are farther apart (larger spacing). Label the compressed wavefronts as "Higher frequency (shorter wavelength)" and the stretched wavefronts as "Lower frequency (longer wavelength)". Include an arrow showing the direction of motion ($v_s$).

### Labels Required / 需要标注
- **English:** Source, Direction of motion ($v_s$), Compressed wavefronts (higher $f$), Stretched wavefronts (lower $f$), Stationary observer in front, Stationary observer behind.
- **中文:** 声源，运动方向 ($v_s$)，压缩波前（更高 $f$），拉伸波前（更低 $f$），前方的静止观察者，后方的静止观察者。

### Exam Importance / 考试重要性
- **English:** This diagram is frequently used in exam questions to explain the Doppler effect qualitatively. Students should be able to draw and label it from memory.
- **中文:** 该图在考试题中经常用于定性地解释多普勒效应。学生应能凭记忆画出并标注它。

---

# 8. Worked Examples / 典型例题

## Example 1: Moving Source, Stationary Observer / 移动声源，静止观察者

### Question / 题目
**English:** A police car siren emits a sound with a frequency of 800 Hz. The car is moving at 30 m/s towards a stationary observer. The speed of sound in air is 340 m/s. Calculate the frequency heard by the observer.

**中文:** 一辆警车的警报器发出频率为 800 Hz 的声音。该车以 30 m/s 的速度向静止观察者驶来。空气中的声速为 340 m/s。计算观察者听到的频率。

### Solution / 解答
**Step 1:** Identify the correct equation. Since the source is moving and the observer is stationary, use:
$$ f_o = \frac{f_s v}{v \mp v_s} $$

**Step 2:** Determine the sign. The source is moving **towards** the observer, so use the minus sign in the denominator:
$$ f_o = \frac{f_s v}{v - v_s} $$

**Step 3:** Substitute the values:
$$ f_o = \frac{800 \times 340}{340 - 30} = \frac{272000}{310} $$

**Step 4:** Calculate:
$$ f_o = 877.4 \, \text{Hz} $$

### Final Answer / 最终答案
**Answer:** 877 Hz (to 3 significant figures) | **答案：** 877 Hz（保留三位有效数字）

### Quick Tip / 提示
- **English:** Always check: since the source is moving towards the observer, the observed frequency must be higher than the source frequency (877 Hz > 800 Hz). If you get a lower frequency, you've used the wrong sign.
- **中文:** 始终检查：由于声源向观察者移动，观察到的频率必须高于声源频率（877 Hz > 800 Hz）。如果得到更低的频率，则使用了错误的符号。

---

## Example 2: Moving Observer, Stationary Source / 移动观察者，静止声源

### Question / 题目
**English:** A stationary loudspeaker emits a sound of frequency 500 Hz. A person runs towards the loudspeaker at a speed of 5 m/s. The speed of sound is 340 m/s. What frequency does the person hear?

**中文:** 一个静止的扬声器发出频率为 500 Hz 的声音。一个人以 5 m/s 的速度向扬声器跑去。声速为 340 m/s。这个人听到的频率是多少？

### Solution / 解答
**Step 1:** Identify the correct equation. Since the observer is moving and the source is stationary, use:
$$ f_o = \frac{f_s (v \pm v_o)}{v} $$

**Step 2:** Determine the sign. The observer is moving **towards** the source, so use the plus sign in the numerator:
$$ f_o = \frac{f_s (v + v_o)}{v} $$

**Step 3:** Substitute the values:
$$ f_o = \frac{500 \times (340 + 5)}{340} = \frac{500 \times 345}{340} $$

**Step 4:** Calculate:
$$ f_o = \frac{172500}{340} = 507.4 \, \text{Hz} $$

### Final Answer / 最终答案
**Answer:** 507 Hz (to 3 significant figures) | **答案：** 507 Hz（保留三位有效数字）

### Quick Tip / 提示
- **English:** Notice that the frequency change is smaller here (7.4 Hz) compared to Example 1 (77.4 Hz) for similar speeds. This is because the observer's motion affects the rate at which wavefronts are encountered, while the source's motion actually compresses the wavefronts themselves.
- **中文:** 注意，在类似速度下，这里的频率变化（7.4 Hz）比示例1（77.4 Hz）小。这是因为观察者的运动影响遇到波前的速率，而声源的运动实际上压缩了波前本身。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate observed frequency (moving source) | High | Easy-Medium | 📝 *待填入* |
| Calculate observed frequency (moving observer) | Medium | Easy-Medium | 📝 *待填入* |
| Calculate source speed from observed frequency | Medium | Medium | 📝 *待填入* |
| Qualitative explanation with diagram | High | Easy | 📝 *待填入* |
| Compare Doppler effect for sound vs light | Low | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, Show that, Explain, Sketch, State
- **中文:** 计算，确定，证明，解释，画出，陈述

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
The Doppler equation for sound connects to practical work in several ways:
1. **Speed of Sound Measurement:** Using a moving source (e.g., a buzzer on a string) and measuring the observed frequency at different positions can be used to determine the speed of sound.
2. **Speed Measurement (Speed Traps):** Police radar guns use the Doppler effect to measure vehicle speed. The gun emits a microwave signal, and the reflected signal from the car has a shifted frequency. The speed is calculated using the Doppler equation.
3. **Uncertainty Analysis:** When measuring frequencies, students must consider uncertainties in frequency measurements and the speed of sound (which depends on temperature). The equation $v = 331\sqrt{1 + \frac{T}{273}}$ can be used to calculate the speed of sound at a given temperature.
4. **Graph Plotting:** Plotting observed frequency against source speed can yield a curve that can be analyzed to find the speed of sound.

**中文:**
声波多普勒方程在多个方面与实验工作相关：
1. **声速测量：** 使用移动声源（例如，绳子上的蜂鸣器）并测量不同位置的观察频率可用于确定声速。
2. **速度测量（测速雷达）：** 警用雷达测速枪利用多普勒效应测量车辆速度。测速枪发射微波信号，从汽车反射回来的信号频率发生偏移。使用多普勒方程计算速度。
3. **不确定度分析：** 测量频率时，学生必须考虑频率测量和声速（取决于温度）的不确定度。可以使用方程 $v = 331\sqrt{1 + \frac{T}{273}}$ 计算给定温度下的声速。
4. **图表绘制：** 绘制观察频率与声源速度的关系图可以得到一条曲线，分析该曲线可以找到声速。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Node
    DOPPLER_SOUND[Doppler Equation for Sound<br>声波多普勒方程] --> SIGN_CONVENTION[Sign Convention<br>符号约定]
    DOPPLER_SOUND --> GENERAL_EQ[General Equation<br>通用方程]
    
    %% Sub-types
    GENERAL_EQ --> MOVING_SOURCE[Moving Source, Stationary Observer<br>移动声源，静止观察者]
    GENERAL_EQ --> MOVING_OBSERVER[Stationary Source, Moving Observer<br>静止声源，移动观察者]
    GENERAL_EQ --> BOTH_MOVING[Both Moving<br>两者都移动]
    
    %% Sign Rules
    MOVING_SOURCE --> TOWARDS_SOURCE[Towards: f_o = f_s v / (v - v_s)<br>靠近]
    MOVING_SOURCE --> AWAY_SOURCE[Away: f_o = f_s v / (v + v_s)<br>远离]
    MOVING_OBSERVER --> TOWARDS_OBSERVER[Towards: f_o = f_s (v + v_o) / v<br>靠近]
    MOVING_OBSERVER --> AWAY_OBSERVER[Away: f_o = f_s (v - v_o) / v<br>远离]
    
    %% Connections to other topics
    DOPPLER_SOUND --> PREREQ[Prerequisites<br>先修知识]
    PREREQ --> PROGRESSIVE_WAVES[[Progressive Waves]]
    PREREQ --> WAVE_SPEED[Wave Speed: v = fλ<br>波速]
    
    DOPPLER_SOUND --> APPLICATIONS[Applications<br>应用]
    APPLICATIONS --> SPEED_TRAP[Speed Traps / Radar<br>测速雷达]
    APPLICATIONS --> ULTRASOUND[Medical Ultrasound<br>医学超声]
    APPLICATIONS --> SONIC_BOOM[Sonic Boom<br>音爆]
    
    DOPPLER_SOUND --> COMPARISON[Comparison<br>比较]
    COMPARISON --> LIGHT_DOPPLER[[Doppler Effect for Light (Redshift and Blueshift)]]
    
    %% Limitations
    DOPPLER_SOUND --> LIMITATIONS[Limitations<br>局限性]
    LIMITATIONS --> SUBSONIC[Only valid for v_s < v<br>仅当 v_s < v 时有效]
    LIMITATIONS --> SHOCKWAVE[Shockwave at v_s = v<br>在 v_s = v 时产生激波]
    
    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:2px;
    classDef sub fill:#bbf,stroke:#333,stroke-width:1px;
    classDef app fill:#bfb,stroke:#333,stroke-width:1px;
    class DOPPLER_SOUND core;
    class MOVING_SOURCE,MOVING_OBSERVER,BOTH_MOVING sub;
    class SPEED_TRAP,ULTRASOUND,SONIC_BOOM app;
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | The Doppler equation quantifies the change in observed frequency due to relative motion between a sound source and observer. 多普勒方程量化了由于声源和观察者之间的相对运动导致的观察频率变化。 |
| **Key Formula / 核心公式** | $$f_o = \frac{f_s (v \pm v_o)}{v \mp v_s}$$ |
| **Sign Convention / 符号约定** | **Towards:** Top +, Bottom - (numerator larger or denominator smaller → $f_o$ higher) **Away:** Top -, Bottom + (numerator smaller or denominator larger → $f_o$ lower) **靠近：** 上 +，下 -（分子变大或分母变小 → $f_o$ 更高）**远离：** 上 -，下 +（分子变小或分母变大 → $f_o$ 更低） |
| **Key Graph / 核心图表** | $f_o$ vs $v_s$: Hyperbolic curve. Towards: rises steeply to infinity at $v_s = v$. Away: decreases to zero. $f_o$ 与 $v_s$ 的关系图：双曲线。靠近：在 $v_s = v$ 处急剧上升到无穷大。远离：下降到零。 |
| **Limitations / 局限性** | Only valid for $v_s < v$ (subsonic). Assumes medium is stationary. Not valid for light (use relativistic formula). 仅适用于 $v_s < v$（亚音速）。假设介质静止。不适用于光（使用相对论公式）。 |
| **Exam Tip / 考试提示** | Always draw a diagram showing direction of motion. Check: if moving towards, $f_o > f_s$; if moving away, $f_o < f_s$. 始终画出显示运动方向的图表。检查：如果靠近，$f_o > f_s$；如果远离，$f_o < f_s$。 |
| **Common Mistake / 常见错误** | Using the wrong sign in the denominator. Forgetting that $v$ is the speed of sound, not the source speed. 在分母中使用错误的符号。忘记 $v$ 是声速，而不是声源速度。 |
| **Application / 应用** | Speed traps (radar), medical ultrasound, astronomy (redshift). 测速雷达，医学超声，天文学（红移）。 |