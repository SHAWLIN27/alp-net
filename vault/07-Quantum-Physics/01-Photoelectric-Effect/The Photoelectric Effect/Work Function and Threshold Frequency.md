---
# Work Function and Threshold Frequency / 逸出功与截止频率

---

# 1. Overview / 概述

**English:**
This sub-topic focuses on two fundamental concepts in the [[The Photoelectric Effect]]: the **work function** ($\Phi$) and the **threshold frequency** ($f_0$). The work function is the minimum energy required to remove an electron from the surface of a metal, while the threshold frequency is the minimum frequency of incident light needed to cause photoemission. These concepts are crucial for understanding why the photoelectric effect occurs only above a certain frequency, regardless of light intensity. They form the bedrock of [[Einstein's Photon Model]] and are directly linked to the [[The Photoelectric Equation]]. Understanding these ideas is essential for grasping the particle nature of light and the failure of classical wave theory.

**中文:**
本子知识点聚焦于[[The Photoelectric Effect]]中的两个基本概念：**逸出功** ($\Phi$) 和**截止频率** ($f_0$)。逸出功是从金属表面移除一个电子所需的最小能量，而截止频率是引起光电发射所需入射光的最小频率。这些概念对于理解为什么光电效应只发生在特定频率以上（与光强无关）至关重要。它们是[[Einstein's Photon Model]]的基石，并直接与[[The Photoelectric Equation]]相关联。理解这些概念对于掌握光的粒子性和经典波动理论的失败至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 22.1 (a) Define and use the terms work function and threshold frequency. | 7.1 Understand the concept of the work function of a metal. |
| 22.1 (b) Recall and use the photoelectric equation $hf = \Phi + \frac{1}{2}mv^2_{\text{max}}$. | 7.2 Understand the concept of threshold frequency. |
| 22.1 (c) Explain why the photoelectric effect cannot be explained by wave theory. | 7.3 Use the photoelectric equation $hf = \Phi + E_{k,\text{max}}$. |
| 22.1 (d) Understand the significance of threshold frequency. | 7.4 Explain the significance of the work function in the photoelectric effect. |
| 22.1 (e) Use the Einstein photoelectric equation. | 7.5 Relate threshold frequency to work function. |
| 22.1 (f) Explain the effect of varying frequency and intensity. | 7.6 Solve problems involving work function and threshold frequency. |
| 22.1 (g) Understand the concept of stopping potential. | |
| 22.1 (h) Use the equation $eV_s = \frac{1}{2}mv^2_{\text{max}}$. | |

**Examiner Expectations / 考官期望:**
- **CAIE:** Students must be able to define work function and threshold frequency precisely, use the photoelectric equation to calculate these values, and explain their physical significance. They should also be able to interpret graphs of maximum kinetic energy against frequency.
- **Edexcel:** Students must understand the work function as a material property, relate it to threshold frequency via $f_0 = \Phi/h$, and apply the photoelectric equation in problem-solving. They should also be able to explain why the work function is a constant for a given metal.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Work Function** ($\Phi$) / 逸出功 | The minimum energy required to remove an electron from the surface of a metal. | 从金属表面移除一个电子所需的最小能量。 | Confusing work function with ionization energy (which applies to isolated atoms). |
| **Threshold Frequency** ($f_0$) / 截止频率 | The minimum frequency of incident electromagnetic radiation required to just eject an electron from a metal surface. | 刚好能从金属表面发射出电子所需的入射电磁辐射的最小频率。 | Thinking threshold frequency depends on light intensity (it does not). |
| **Photon Energy** ($E = hf$) / 光子能量 | The energy carried by a single photon of electromagnetic radiation, proportional to its frequency. | 单个电磁辐射光子携带的能量，与其频率成正比。 | Forgetting that $h$ is Planck's constant ($6.63 \times 10^{-34} \text{ J s}$). |
| **Maximum Kinetic Energy** ($E_{k,\text{max}}$) / 最大动能 | The maximum kinetic energy of an emitted photoelectron, equal to the energy of the incident photon minus the work function. | 发射出的光电子的最大动能，等于入射光子能量减去逸出功。 | Confusing with average kinetic energy; $E_{k,\text{max}}$ is for electrons at the surface. |
| **Stopping Potential** ($V_s$) / 遏止电势 | The minimum potential difference required to stop the most energetic photoelectrons from reaching the anode. | 阻止能量最大的光电子到达阳极所需的最小电势差。 | Forgetting that $eV_s = E_{k,\text{max}}$. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Work Function ($\Phi$) / 逸出功

### Explanation / 解释
**English:**
The work function ($\Phi$) is a property of the metal surface. It represents the energy barrier that an electron must overcome to escape from the metal. This energy is required because electrons are bound to the metal lattice by attractive forces. The work function is typically measured in **electronvolts (eV)** or **joules (J)**. For example, the work function of sodium is about 2.3 eV, while for platinum it is about 6.4 eV. The work function is a constant for a given metal under fixed conditions.

**中文:**
逸出功 ($\Phi$) 是金属表面的一个属性。它代表了电子从金属中逸出必须克服的能量势垒。需要这部分能量是因为电子通过吸引力被束缚在金属晶格中。逸出功通常以**电子伏特 (eV)** 或**焦耳 (J)** 为单位。例如，钠的逸出功约为 2.3 eV，而铂的逸出功约为 6.4 eV。在固定条件下，给定金属的逸出功是一个常数。

### Physical Meaning / 物理意义
**English:**
Physically, the work function is the minimum energy needed to liberate an electron from the metal's surface. It is a measure of how tightly electrons are bound. Metals with a low work function (e.g., cesium, 2.1 eV) are more easily photoemissive, while those with a high work function (e.g., gold, 5.1 eV) require higher-energy photons.

**中文:**
从物理上讲，逸出功是将电子从金属表面释放所需的最小能量。它衡量了电子被束缚的紧密程度。逸出功低的金属（如铯，2.1 eV）更容易发生光电发射，而逸出功高的金属（如金，5.1 eV）则需要更高能量的光子。

### Common Misconceptions / 常见误区
- **Misconception:** The work function is the same for all metals.
  **Correction:** The work function varies from metal to metal (e.g., sodium ~2.3 eV, zinc ~4.3 eV).
- **Misconception:** The work function depends on light intensity.
  **Correction:** The work function is a material property and is independent of light intensity or frequency.
- **Misconception:** The work function is the energy of the incident photon.
  **Correction:** The work function is the energy required to remove an electron; the photon energy must be at least equal to the work function.

### Exam Tips / 考试提示
- **Tip:** Always convert work function from eV to Joules when using the photoelectric equation: $1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$.
- **Tip:** Remember that the work function is the **minimum** energy; some electrons require more energy if they are deeper in the metal.

> 📷 **IMAGE PROMPT — WF-01: Work Function Diagram**
> A diagram showing a metal surface with electrons bound inside. An arrow labeled "Work Function ($\Phi$)" points upward from the electron to the vacuum level. The metal lattice is shown as a grid of positive ions, with electrons as small circles. The energy barrier is depicted as a hill or step.

---

## 4.2 Threshold Frequency ($f_0$) / 截止频率

### Explanation / 解释
**English:**
The threshold frequency ($f_0$) is the minimum frequency of incident light that can cause photoemission. It is directly related to the work function by the equation:
$$ f_0 = \frac{\Phi}{h} $$
where $h$ is Planck's constant. If the frequency of incident light is below $f_0$, no photoelectrons are emitted, regardless of the light intensity. This is a key piece of evidence for the particle nature of light.

**中文:**
截止频率 ($f_0$) 是能引起光电发射的入射光的最小频率。它与逸出功通过以下方程直接相关：
$$ f_0 = \frac{\Phi}{h} $$
其中 $h$ 是普朗克常数。如果入射光的频率低于 $f_0$，则无论光强如何，都不会发射光电子。这是光具有粒子性的关键证据之一。

### Physical Meaning / 物理意义
**English:**
The threshold frequency corresponds to the photon energy exactly equal to the work function. At this frequency, the photon has just enough energy to free an electron, but the electron has zero kinetic energy after emission. For frequencies above $f_0$, the excess energy becomes kinetic energy of the photoelectron.

**中文:**
截止频率对应于光子能量恰好等于逸出功的情况。在此频率下，光子刚好有足够的能量释放电子，但电子在发射后动能为零。对于高于 $f_0$ 的频率，多余的能量转化为光电子的动能。

### Common Misconceptions / 常见误区
- **Misconception:** Threshold frequency depends on light intensity.
  **Correction:** Threshold frequency is a material property; it depends only on the work function.
- **Misconception:** Below threshold frequency, increasing intensity will eventually cause emission.
  **Correction:** No — if $f < f_0$, no electrons are emitted, no matter how intense the light.
- **Misconception:** Threshold frequency is the same for all metals.
  **Correction:** Different metals have different work functions, so they have different threshold frequencies.

### Exam Tips / 考试提示
- **Tip:** To find threshold frequency from a graph of $E_{k,\text{max}}$ vs $f$, find the $f$-intercept (where $E_{k,\text{max}} = 0$).
- **Tip:** Remember that $f_0$ is in Hz, and $\Phi$ must be in Joules for the calculation.

> 📷 **IMAGE PROMPT — TF-01: Threshold Frequency Concept**
> A diagram showing two scenarios: (1) Light with frequency $f < f_0$ hitting a metal surface — no electrons emitted. (2) Light with frequency $f > f_0$ hitting the same surface — electrons are emitted. Label the threshold frequency as the boundary.

---

## 4.3 Relationship Between Work Function and Threshold Frequency / 逸出功与截止频率的关系

### Explanation / 解释
**English:**
The work function and threshold frequency are intimately linked. The threshold frequency is the frequency at which the photon energy equals the work function:
$$ h f_0 = \Phi $$
This means that if you know the work function of a metal, you can calculate its threshold frequency, and vice versa. This relationship is fundamental to the [[The Photoelectric Equation]]:
$$ h f = \Phi + \frac{1}{2} m v_{\text{max}}^2 $$
At the threshold frequency, the kinetic energy term is zero.

**中文:**
逸出功和截止频率密切相关。截止频率是光子能量等于逸出功时的频率：
$$ h f_0 = \Phi $$
这意味着，如果你知道金属的逸出功，就可以计算其截止频率，反之亦然。这个关系是[[The Photoelectric Equation]]的基础：
$$ h f = \Phi + \frac{1}{2} m v_{\text{max}}^2 $$
在截止频率处，动能项为零。

### Physical Meaning / 物理意义
**English:**
This relationship shows that the photoelectric effect is a quantum phenomenon. Each photon transfers its entire energy to a single electron. If the photon energy is less than the work function, the electron cannot escape. This is why there is a sharp cutoff frequency — it's not about the total energy delivered (intensity), but about the energy per photon.

**中文:**
这个关系表明光电效应是一种量子现象。每个光子将其全部能量传递给一个电子。如果光子能量小于逸出功，电子就无法逸出。这就是为什么存在一个尖锐的截止频率——这不是关于传递的总能量（强度），而是关于每个光子的能量。

### Common Misconceptions / 常见误区
- **Misconception:** The work function and threshold frequency are independent concepts.
  **Correction:** They are directly proportional: $f_0 = \Phi/h$.
- **Misconception:** The threshold frequency can be changed by using a brighter light.
  **Correction:** The threshold frequency is fixed for a given metal.

### Exam Tips / 考试提示
- **Tip:** When given a graph of $E_{k,\text{max}}$ vs $f$, the $y$-intercept is $-\Phi$ (in Joules), and the $x$-intercept is $f_0$.
- **Tip:** Always check units — work function may be given in eV, but Planck's constant is in J s.

> 📷 **IMAGE PROMPT — WF-TF-01: Work Function and Threshold Frequency Graph**
> A graph of $E_{k,\text{max}}$ (y-axis) vs $f$ (x-axis). The line is straight with a positive slope. Label the $x$-intercept as $f_0$ (threshold frequency) and the $y$-intercept as $-\Phi$ (negative work function). The slope is $h$ (Planck's constant).

---

# 5. Essential Equations / 核心公式

## Equation 1: Work Function and Threshold Frequency / 逸出功与截止频率

$$ \Phi = h f_0 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Phi$ | Work function | 逸出功 | J (or eV) |
| $h$ | Planck's constant ($6.63 \times 10^{-34} \text{ J s}$) | 普朗克常数 | J s |
| $f_0$ | Threshold frequency | 截止频率 | Hz |

**Derivation / 推导:**
This equation is derived from the condition for photoemission: the photon energy must be at least equal to the work function. At the threshold, $hf_0 = \Phi$.

**Conditions / 适用条件:**
- The metal surface is clean and at a fixed temperature.
- The incident radiation is monochromatic.

**Limitations / 局限性:**
- This equation assumes a perfect surface; real surfaces may have impurities that affect the work function.

---

## Equation 2: The Photoelectric Equation / 光电效应方程

$$ h f = \Phi + \frac{1}{2} m v_{\text{max}}^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $h f$ | Energy of incident photon | 入射光子能量 | J |
| $\Phi$ | Work function | 逸出功 | J |
| $\frac{1}{2} m v_{\text{max}}^2$ | Maximum kinetic energy of photoelectron | 光电子的最大动能 | J |

**Derivation / 推导:**
Einstein proposed that a photon transfers all its energy to a single electron. The electron uses some energy to escape the metal (work function) and the rest becomes kinetic energy.

**Conditions / 适用条件:**
- The photon energy must be greater than or equal to the work function ($hf \ge \Phi$).
- The electron is assumed to be at the surface (minimum energy to escape).

**Limitations / 局限性:**
- This equation gives the **maximum** kinetic energy; most electrons have less kinetic energy due to collisions within the metal.

---

## Equation 3: Stopping Potential / 遏止电势

$$ e V_s = \frac{1}{2} m v_{\text{max}}^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $e$ | Elementary charge ($1.60 \times 10^{-19} \text{ C}$) | 元电荷 | C |
| $V_s$ | Stopping potential | 遏止电势 | V |
| $\frac{1}{2} m v_{\text{max}}^2$ | Maximum kinetic energy | 最大动能 | J |

**Derivation / 推导:**
The stopping potential is the potential difference that just stops the most energetic photoelectrons. The work done by the electric field ($eV_s$) equals the maximum kinetic energy.

**Conditions / 适用条件:**
- The stopping potential is measured when the photocurrent reaches zero.
- The electric field is uniform.

**Limitations / 局限性:**
- This equation assumes no other forces act on the electron.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Maximum Kinetic Energy vs Frequency / 最大动能与频率关系图

### Axes / 坐标轴
- **X-axis:** Frequency of incident light, $f$ (Hz) / 入射光频率 $f$ (Hz)
- **Y-axis:** Maximum kinetic energy of photoelectrons, $E_{k,\text{max}}$ (J) / 光电子最大动能 $E_{k,\text{max}}$ (J)

### Shape / 形状
A straight line with a positive slope, starting from the x-axis at $f = f_0$.

### Gradient Meaning / 斜率含义
The gradient of the line is Planck's constant, $h$ ($6.63 \times 10^{-34} \text{ J s}$).

### Area Meaning / 面积含义
There is no meaningful area under this graph.

### Exam Interpretation / 考试解读
- **X-intercept:** Threshold frequency ($f_0$).
- **Y-intercept:** Negative of the work function ($-\Phi$).
- **Equation of the line:** $E_{k,\text{max}} = h f - \Phi$.

> 📷 **IMAGE PROMPT — GRAPH-01: E_k_max vs f**
> A graph with frequency on the x-axis and maximum kinetic energy on the y-axis. A straight line starts from the x-axis at $f_0$ and goes upward. The slope is labeled $h$. The y-intercept is labeled $-\Phi$. The line equation $E_{k,\text{max}} = hf - \Phi$ is shown.

---

## 6.2 Photocurrent vs Applied Voltage / 光电流与外加电压关系图

### Axes / 坐标轴
- **X-axis:** Applied voltage, $V$ (V) / 外加电压 $V$ (V)
- **Y-axis:** Photocurrent, $I$ (A) / 光电流 $I$ (A)

### Shape / 形状
The curve starts at a negative voltage (stopping potential) where current is zero, then rises rapidly and saturates at a plateau.

### Gradient Meaning / 斜率含义
The gradient at any point represents the rate of change of current with voltage.

### Area Meaning / 面积含义
There is no meaningful area under this graph.

### Exam Interpretation / 考试解读
- **X-intercept (negative):** Stopping potential ($V_s$).
- **Saturation current:** Proportional to light intensity.
- **Effect of frequency:** Increasing frequency increases $V_s$ (shifts the curve left).

> 📷 **IMAGE PROMPT — GRAPH-02: Photocurrent vs Voltage**
> A graph with voltage on the x-axis and photocurrent on the y-axis. The curve starts at a negative voltage (labeled $V_s$) where current is zero, rises steeply, and then plateaus. Two curves are shown: one for low intensity (lower plateau) and one for high intensity (higher plateau).

---

# 7. Required Diagrams / 必备图表

## 7.1 Energy Level Diagram for Photoelectric Effect / 光电效应能级图

### Description / 描述
**English:**
This diagram shows the energy levels of an electron in a metal. The work function is represented as an energy barrier that the electron must overcome to escape. The incident photon provides the energy to overcome this barrier.

**中文:**
该图显示了金属中电子的能级。逸出功被表示为电子必须克服才能逸出的能量势垒。入射光子提供克服该势垒的能量。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-01: Energy Level Diagram**
> A diagram showing a horizontal line representing the vacuum level (zero energy). Below it, a shaded region represents the metal with electrons at various energy levels. An arrow labeled "Work Function ($\Phi$)" points from the highest occupied level to the vacuum level. An incoming photon (wavy arrow) with energy $hf$ is shown hitting an electron, which then jumps to the vacuum level and beyond, with the excess energy shown as kinetic energy.

### Labels Required / 需要标注
- Vacuum level / 真空能级
- Work function ($\Phi$) / 逸出功
- Incident photon ($hf$) / 入射光子
- Kinetic energy ($E_k$) / 动能
- Metal surface / 金属表面

### Exam Importance / 考试重要性
**English:**
This diagram is essential for understanding the energy balance in the photoelectric effect. It helps visualize why the photon energy must exceed the work function.

**中文:**
该图对于理解光电效应中的能量平衡至关重要。它有助于形象化理解为什么光子能量必须超过逸出功。

---

## 7.2 Experimental Setup for Measuring Work Function / 测量逸出功的实验装置

### Description / 描述
**English:**
This diagram shows the apparatus used to measure the work function and threshold frequency. It includes a light source, a monochromator (to select frequency), a photocell (metal cathode and anode), a variable power supply, and a sensitive ammeter.

**中文:**
该图显示了用于测量逸出功和截止频率的装置。它包括光源、单色仪（用于选择频率）、光电管（金属阴极和阳极）、可变电源和灵敏电流计。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG-02: Experimental Setup**
> A diagram showing a light source (with a filter or monochromator) shining on a metal cathode inside an evacuated glass tube. The cathode is connected to the negative terminal of a variable power supply, and the anode is connected to the positive terminal. A sensitive ammeter is in series. A voltmeter is connected across the power supply.

### Labels Required / 需要标注
- Light source / 光源
- Monochromator / 单色仪
- Cathode (metal) / 阴极（金属）
- Anode / 阳极
- Variable power supply / 可变电源
- Ammeter / 电流计
- Voltmeter / 电压表
- Evacuated tube / 真空管

### Exam Importance / 考试重要性
**English:**
This setup is used to measure the stopping potential, from which the maximum kinetic energy and work function can be determined.

**中文:**
该装置用于测量遏止电势，从而可以确定最大动能和逸出功。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Threshold Frequency / 计算截止频率

### Question / 题目
**English:**
The work function of sodium is 2.3 eV. Calculate:
(a) The threshold frequency for sodium.
(b) The maximum kinetic energy of photoelectrons emitted when light of frequency $7.0 \times 10^{14} \text{ Hz}$ is incident on a sodium surface.

Given: $h = 6.63 \times 10^{-34} \text{ J s}$, $1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$.

**中文:**
钠的逸出功为 2.3 eV。计算：
(a) 钠的截止频率。
(b) 当频率为 $7.0 \times 10^{14} \text{ Hz}$ 的光照射到钠表面时，发射出的光电子的最大动能。

已知：$h = 6.63 \times 10^{-34} \text{ J s}$，$1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$。

### Solution / 解答

**Part (a):**
1. Convert work function to Joules:
   $$ \Phi = 2.3 \text{ eV} \times 1.60 \times 10^{-19} \text{ J/eV} = 3.68 \times 10^{-19} \text{ J} $$

2. Use the threshold frequency equation:
   $$ f_0 = \frac{\Phi}{h} = \frac{3.68 \times 10^{-19}}{6.63 \times 10^{-34}} $$

3. Calculate:
   $$ f_0 = 5.55 \times 10^{14} \text{ Hz} $$

**Part (b):**
1. Use the photoelectric equation:
   $$ E_{k,\text{max}} = h f - \Phi $$

2. Substitute values:
   $$ E_{k,\text{max}} = (6.63 \times 10^{-34})(7.0 \times 10^{14}) - 3.68 \times 10^{-19} $$

3. Calculate:
   $$ E_{k,\text{max}} = 4.64 \times 10^{-19} - 3.68 \times 10^{-19} = 9.6 \times 10^{-20} \text{ J} $$

4. Convert to eV:
   $$ E_{k,\text{max}} = \frac{9.6 \times 10^{-20}}{1.60 \times 10^{-19}} = 0.60 \text{ eV} $$

### Final Answer / 最终答案
**Answer:** (a) $f_0 = 5.55 \times 10^{14} \text{ Hz}$ | **答案：** (a) $f_0 = 5.55 \times 10^{14} \text{ Hz}$
**Answer:** (b) $E_{k,\text{max}} = 9.6 \times 10^{-20} \text{ J} = 0.60 \text{ eV}$ | **答案：** (b) $E_{k,\text{max}} = 9.6 \times 10^{-20} \text{ J} = 0.60 \text{ eV}$

### Quick Tip / 提示
**English:** Always convert work function to Joules before using the photoelectric equation. Remember that $1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$.

**中文:** 在使用光电效应方程之前，务必将逸出功转换为焦耳。记住 $1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$。

---

## Example 2: Determining Work Function from Stopping Potential / 从遏止电势确定逸出功

### Question / 题目
**English:**
In a photoelectric experiment, light of wavelength $4.0 \times 10^{-7} \text{ m}$ is incident on a metal surface. The stopping potential is measured to be 1.2 V. Calculate:
(a) The maximum kinetic energy of the photoelectrons in Joules.
(b) The work function of the metal in eV.

Given: $h = 6.63 \times 10^{-34} \text{ J s}$, $c = 3.00 \times 10^8 \text{ m/s}$, $e = 1.60 \times 10^{-19} \text{ C}$.

**中文:**
在光电效应实验中，波长为 $4.0 \times 10^{-7} \text{ m}$ 的光照射到金属表面。测得的遏止电势为 1.2 V。计算：
(a) 光电子的最大动能（以焦耳为单位）。
(b) 金属的逸出功（以 eV 为单位）。

已知：$h = 6.63 \times 10^{-34} \text{ J s}$，$c = 3.00 \times 10^8 \text{ m/s}$，$e = 1.60 \times 10^{-19} \text{ C}$。

### Solution / 解答

**Part (a):**
1. Use the stopping potential equation:
   $$ E_{k,\text{max}} = e V_s $$

2. Substitute values:
   $$ E_{k,\text{max}} = (1.60 \times 10^{-19})(1.2) = 1.92 \times 10^{-19} \text{ J} $$

**Part (b):**
1. Calculate the photon energy:
   $$ E = h f = \frac{h c}{\lambda} = \frac{(6.63 \times 10^{-34})(3.00 \times 10^8)}{4.0 \times 10^{-7}} $$

2. Calculate:
   $$ E = \frac{1.989 \times 10^{-25}}{4.0 \times 10^{-7}} = 4.97 \times 10^{-19} \text{ J} $$

3. Convert to eV:
   $$ E = \frac{4.97 \times 10^{-19}}{1.60 \times 10^{-19}} = 3.11 \text{ eV} $$

4. Use the photoelectric equation:
   $$ \Phi = h f - E_{k,\text{max}} = 3.11 \text{ eV} - 1.2 \text{ eV} = 1.91 \text{ eV} $$

### Final Answer / 最终答案
**Answer:** (a) $E_{k,\text{max}} = 1.92 \times 10^{-19} \text{ J}$ | **答案：** (a) $E_{k,\text{max}} = 1.92 \times 10^{-19} \text{ J}$
**Answer:** (b) $\Phi = 1.91 \text{ eV}$ | **答案：** (b) $\Phi = 1.91 \text{ eV}$

### Quick Tip / 提示
**English:** When given wavelength, first convert to frequency using $f = c/\lambda$. The stopping potential directly gives the maximum kinetic energy in eV (since $eV_s$ in eV equals $V_s$ in volts).

**中文:** 当给定波长时，首先使用 $f = c/\lambda$ 转换为频率。遏止电势直接以 eV 为单位给出最大动能（因为以 eV 为单位的 $eV_s$ 等于以伏特为单位的 $V_s$）。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Definition of work function and threshold frequency | High | Easy | 📝 *待填入* |
| Calculation of threshold frequency from work function | High | Medium | 📝 *待填入* |
| Calculation of work function from stopping potential | High | Medium | 📝 *待填入* |
| Graph interpretation ($E_{k,\text{max}}$ vs $f$) | High | Medium | 📝 *待填入* |
| Explanation of why wave theory fails | Medium | Hard | 📝 *待填入* |
| Comparison of different metals' work functions | Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Define / 定义:** State the precise meaning (e.g., "Define work function").
- **Calculate / 计算:** Use a formula to find a numerical value.
- **Explain / 解释:** Give reasons for a phenomenon.
- **Determine / 确定:** Find a value from a graph or data.
- **Sketch / 画图:** Draw a graph showing the general shape.

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical work in several ways:

1. **Measuring Stopping Potential:** Students should be able to set up the photoelectric effect apparatus, vary the voltage, and measure the stopping potential. This requires careful use of a sensitive ammeter and voltmeter.

2. **Determining Work Function:** By measuring the stopping potential for different frequencies of light, students can plot a graph of $E_{k,\text{max}}$ vs $f$ and determine the work function from the y-intercept.

3. **Uncertainties:** The main sources of uncertainty include:
   - Accuracy of the frequency/wavelength of light.
   - Accuracy of the voltmeter and ammeter.
   - Temperature effects on the metal surface.
   - Surface contamination affecting the work function.

4. **Graph Plotting:** Students should be able to plot $E_{k,\text{max}}$ vs $f$, draw a line of best fit, and determine the gradient (Planck's constant) and intercepts (work function and threshold frequency).

5. **Experimental Design:** Students should understand why the tube must be evacuated (to prevent collisions with air molecules) and why a monochromatic light source is needed.

**中文:**
本子知识点在多个方面与实验工作相关：

1. **测量遏止电势：** 学生应能够搭建光电效应装置，改变电压，并测量遏止电势。这需要谨慎使用灵敏电流计和电压表。

2. **确定逸出功：** 通过测量不同频率光的遏止电势，学生可以绘制 $E_{k,\text{max}}$ 与 $f$ 的关系图，并从 y 轴截距确定逸出功。

3. **不确定度：** 不确定度的主要来源包括：
   - 光的频率/波长的精度。
   - 电压表和电流表的精度。
   - 温度对金属表面的影响。
   - 表面污染影响逸出功。

4. **图表绘制：** 学生应能够绘制 $E_{k,\text{max}}$ 与 $f$ 的关系图，画出最佳拟合线，并确定斜率（普朗克常数）和截距（逸出功和截止频率）。

5. **实验设计：** 学生应理解为什么管子必须抽真空（以防止与空气分子碰撞）以及为什么需要单色光源。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Work Function and Threshold Frequency Concept Map
    A[Work Function (Φ)] -->|Defines| B[Threshold Frequency (f₀)]
    A -->|Related by| C[Φ = h f₀]
    B -->|Minimum frequency for| D[Photoemission]
    C -->|Used in| E[Photoelectric Equation: hf = Φ + E_k,max]
    E -->|Connects to| F[Stopping Potential: eV_s = E_k,max]
    E -->|Explains| G[Failure of Classical Wave Theory]
    A -->|Property of| H[Metal Surface]
    B -->|Independent of| I[Light Intensity]
    F -->|Measured using| J[Experimental Setup]
    J -->|Produces| K[Graph of E_k,max vs f]
    K -->|Gradient =| L[Planck's Constant (h)]
    K -->|X-intercept =| B
    K -->|Y-intercept =| M[Negative of Φ]
    
    %% Links to other topics
    A -->|Prerequisite| N[[Progressive Waves]]
    E -->|Related to| O[[Wave-Particle Duality]]
    H -->|Related to| P[[Energy Levels and Spectra]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Work Function (Φ):** Minimum energy to remove an electron from a metal surface. / **逸出功 (Φ):** 从金属表面移除一个电子所需的最小能量。 |
| | **Threshold Frequency (f₀):** Minimum frequency of light to cause photoemission. / **截止频率 (f₀):** 引起光电发射所需的最小光频率。 |
| **Key Formula / 核心公式** | $Φ = h f₀$ — Work function equals Planck's constant times threshold frequency. |
| | $hf = Φ + E_{k,max}$ — The photoelectric equation. |
| | $eV_s = E_{k,max}$ — Stopping potential relates to maximum kinetic energy. |
| **Key Graph / 核心图表** | $E_{k,max}$ vs $f$: Straight line, slope = $h$, x-intercept = $f₀$, y-intercept = $-Φ$. |
| **Key Units / 关键单位** | $Φ$ in J or eV ($1 \text{ eV} = 1.60 \times 10^{-19} \text{ J}$) |
| | $f₀$ in Hz |
| | $h = 6.63 \times 10^{-34} \text{ J s}$ |
| **Exam Tip / 考试提示** | Always convert work function to Joules before calculations. |
| | The threshold frequency is a material property — it does NOT depend on light intensity. |
| | On a graph of $E_{k,max}$ vs $f$, the y-intercept is $-Φ$ (negative work function). |
| **Common Mistake / 常见错误** | Confusing work function with ionization energy. |
| | Thinking threshold frequency depends on intensity. |
| | Forgetting to convert eV to J. |