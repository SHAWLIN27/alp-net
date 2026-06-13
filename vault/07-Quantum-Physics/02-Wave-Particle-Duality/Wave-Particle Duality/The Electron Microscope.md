---
# 1. Overview / 概述

**English:**
The electron microscope is a landmark application of [[Wave-Particle Duality for Matter]], specifically the [[de Broglie Wavelength]] of electrons. This sub-topic explains how the wave nature of electrons, discovered through [[Electron Diffraction and the Davisson-Germer Experiment]], is exploited to achieve extremely high resolution imaging far beyond the capabilities of optical microscopes. We will cover the fundamental principle: the de Broglie wavelength of an electron is inversely proportional to its momentum, and by accelerating electrons through a high voltage, we can achieve wavelengths thousands of times shorter than visible light. This allows the microscope to resolve details at the atomic scale. The note also covers the basic construction of a Transmission Electron Microscope (TEM) and a Scanning Electron Microscope (SEM), the role of magnetic lenses, and the key advantages and limitations of electron microscopy compared to optical microscopy. This topic directly links the abstract concept of wave-particle duality to a powerful real-world technology.

**中文:**
电子显微镜是[[物质波粒二象性]]，特别是电子[[德布罗意波长]]的一个里程碑式的应用。本子知识点解释了如何利用通过[[电子衍射与戴维森-革末实验]]发现的电子的波动性，来实现远超光学显微镜能力的超高分辨率成像。我们将涵盖基本原理：电子的德布罗意波长与其动量成反比，通过高压加速电子，我们可以获得比可见光短数千倍的波长。这使得显微镜能够分辨原子尺度的细节。本笔记还涵盖了透射电子显微镜（TEM）和扫描电子显微镜（SEM）的基本结构、磁透镜的作用，以及电子显微镜相较于光学显微镜的主要优势和局限性。该主题将波粒二象性的抽象概念与强大的现实世界技术直接联系起来。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 (22.2 a-f) | Edexcel IAL (WPH14 U4: 7.7-7.12) |
|-----------|-------------|
| (a) Explain how the wave nature of electrons is used in the electron microscope. | 7.7 Understand how the de Broglie wavelength of an electron is used in the electron microscope. |
| (b) Understand the relationship between the accelerating voltage and the de Broglie wavelength of an electron. | 7.8 Be able to calculate the de Broglie wavelength of an electron given its kinetic energy. |
| (c) Describe the basic structure and operation of a transmission electron microscope (TEM). | 7.9 Understand the role of magnetic fields in focusing an electron beam. |
| (d) Describe the basic structure and operation of a scanning electron microscope (SEM). | 7.10 Understand the difference between TEM and SEM. |
| (e) Understand the advantages of the electron microscope over the optical microscope in terms of resolution. | 7.11 Understand the advantages and limitations of the electron microscope. |
| (f) Understand the limitations of the electron microscope. | 7.12 Understand the need for a vacuum in an electron microscope. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to calculate the de Broglie wavelength of an electron from its accelerating voltage. You should be able to explain why a shorter wavelength leads to better resolution. You need to describe the basic principles of TEM and SEM, including the function of magnetic lenses and the need for a vacuum. Be prepared to compare and contrast electron microscopes with optical microscopes.
- **中文:** 你必须能够根据加速电压计算电子的德布罗意波长。你应该能够解释为什么更短的波长能带来更好的分辨率。你需要描述TEM和SEM的基本原理，包括磁透镜的功能和真空的必要性。准备好比较和对比电子显微镜与光学显微镜。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Electron Microscope** / 电子显微镜 | A microscope that uses a beam of accelerated electrons as a source of illumination to form an image of a specimen. | 使用加速电子束作为照明源来形成样本图像的显微镜。 | Confusing it with a scanning tunneling microscope (STM), which uses a different principle (quantum tunneling). |
| **de Broglie Wavelength** / 德布罗意波长 | The wavelength associated with a moving particle, given by $\lambda = h/p$, where $h$ is Planck's constant and $p$ is the momentum. | 与运动粒子相关的波长，由 $\lambda = h/p$ 给出，其中 $h$ 是普朗克常数，$p$ 是动量。 | Forgetting that the momentum $p$ is $mv$, not just $m$. |
| **Resolution** / 分辨率 | The smallest distance between two points that can be distinguished as separate by an imaging system. | 成像系统能够区分两个点之间的最小距离。 | Confusing resolution with magnification. High magnification without high resolution is useless ("empty magnification"). |
| **Magnetic Lens** / 磁透镜 | A device that uses a magnetic field to focus a beam of electrons, analogous to a glass lens focusing light. | 一种利用磁场聚焦电子束的装置，类似于玻璃透镜聚焦光线。 | Thinking they focus electrons by slowing them down; they work by applying a Lorentz force to change the electron's path. |
| **Transmission Electron Microscope (TEM)** / 透射电子显微镜 | An electron microscope where electrons are transmitted through a very thin specimen to form an image. | 电子穿过非常薄的样本以形成图像的电子显微镜。 | Forgetting the specimen must be extremely thin. |
| **Scanning Electron Microscope (SEM)** / 扫描电子显微镜 | An electron microscope where a focused beam of electrons scans the surface of a specimen to form an image. | 聚焦电子束扫描样本表面以形成图像的电子显微镜。 | Thinking it transmits through the sample; it detects reflected/scattered electrons. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Principle of Resolution / 分辨率原理

### Explanation / 解释
**English:** The fundamental limit to the resolution of any microscope is determined by the wavelength of the radiation used to illuminate the specimen. This is known as the **Abbe diffraction limit**. For an optical microscope, the best possible resolution is roughly half the wavelength of light used ($\approx 200$ nm for visible light). To see smaller details, a shorter wavelength is needed. The [[de Broglie Wavelength]] of an electron can be made incredibly small by accelerating it through a high voltage. For example, an electron accelerated through 100 kV has a wavelength of about 0.0037 nm, which is over 50,000 times shorter than visible light. This allows electron microscopes to achieve resolutions down to the atomic scale (sub-nanometer).

**中文:** 任何显微镜分辨率的根本限制由用于照亮样本的辐射波长决定。这被称为**阿贝衍射极限**。对于光学显微镜，最佳可能分辨率大约是所用光波长的一半（可见光约为200纳米）。要看到更小的细节，就需要更短的波长。电子的[[德布罗意波长]]可以通过高压加速而变得非常小。例如，一个经过100 kV加速的电子，其波长约为0.0037 nm，比可见光短了超过50,000倍。这使得电子显微镜能够达到原子尺度（亚纳米级）的分辨率。

### Physical Meaning / 物理意义
**English:** The wave nature of matter is not just a theoretical curiosity; it imposes a physical limit on what we can see. By using electrons, we are using their wave properties to "see" things that are too small for light waves to interact with. The shorter the wavelength, the smaller the object that can be resolved.

**中文:** 物质的波动性不仅仅是理论上的好奇；它对我们能看到什么施加了物理限制。通过使用电子，我们是在利用它们的波动特性来“看见”那些光波无法与之相互作用的微小物体。波长越短，能够分辨的物体就越小。

### Common Misconceptions / 常见误区
- **English:** Thinking that higher *magnification* automatically means better *resolution*. Resolution is the limiting factor; magnification just makes the image bigger. If the resolution is poor, magnifying a blurry image just gives a bigger blurry image.
- **中文:** 认为更高的*放大倍数*自动意味着更好的*分辨率*。分辨率是限制因素；放大倍数只是让图像变大。如果分辨率差，放大模糊的图像只会得到一个更大的模糊图像。
- **English:** Believing that the electron beam "sees" the sample like a light beam. The image is formed by complex interactions (scattering, secondary electron emission) between the electron beam and the sample.
- **中文:** 认为电子束像光束一样“看到”样本。图像是由电子束与样本之间复杂的相互作用（散射、二次电子发射）形成的。

### Exam Tips / 考试提示
- **English:** Be prepared to calculate the de Broglie wavelength of an electron given its accelerating voltage. Use the formula $\lambda = h / \sqrt{2 m e V}$.
- **中文:** 准备好根据加速电压计算电子的德布罗意波长。使用公式 $\lambda = h / \sqrt{2 m e V}$。
- **English:** Clearly state that the key advantage of an electron microscope is its *higher resolution* due to the *shorter wavelength* of electrons.
- **中文:** 清楚地说明电子显微镜的关键优势是由于电子的*波长更短*而具有的*更高分辨率*。

> 📷 **IMAGE PROMPT — DIAGRAM-01: Comparison of Resolution**
> A side-by-side comparison diagram. Left: An optical microscope image of a cell, with a scale bar showing a resolution limit of ~200 nm. Right: A TEM image of a virus or a crystal lattice, with a scale bar showing a resolution limit of < 1 nm. Annotations in English and Chinese explaining the difference in wavelength and resolution.

## 4.2 Magnetic Lenses / 磁透镜

### Explanation / 解释
**English:** Unlike optical microscopes which use glass lenses to bend light, electron microscopes use **magnetic lenses** to focus the electron beam. A magnetic lens is essentially an electromagnet (a coil of wire with a current flowing through it) that produces a non-uniform magnetic field. When a moving electron enters this field, it experiences a Lorentz force ($F = q v \times B$). This force acts perpendicular to both the electron's velocity and the magnetic field, causing the electron to follow a helical path. By carefully shaping the magnetic field, the lens can be made to converge the electron beam to a focus, analogous to a convex lens for light. The focal length of a magnetic lens can be adjusted by changing the current through the coil.

**中文:** 与使用玻璃透镜弯曲光线的光学显微镜不同，电子显微镜使用**磁透镜**来聚焦电子束。磁透镜本质上是一个电磁铁（一个通有电流的线圈），产生一个非均匀磁场。当一个运动的电子进入这个磁场时，它会受到洛伦兹力 ($F = q v \times B$)。这个力垂直于电子的速度和磁场，使电子沿着螺旋路径运动。通过仔细塑造磁场形状，可以使透镜会聚电子束到一个焦点，类似于凸透镜对光的作用。磁透镜的焦距可以通过改变线圈中的电流来调节。

### Physical Meaning / 物理意义
**English:** We cannot use glass lenses for electrons because electrons are charged particles and would be absorbed or scattered by the glass. Magnetic fields, however, can exert a force on moving charges without absorbing them, making them the perfect tool for manipulating electron beams in a vacuum.

**中文:** 我们不能对电子使用玻璃透镜，因为电子是带电粒子，会被玻璃吸收或散射。然而，磁场可以在不吸收运动电荷的情况下对其施加力，这使其成为在真空中操纵电子束的理想工具。

### Common Misconceptions / 常见误区
- **English:** Thinking magnetic lenses "slow down" or "speed up" electrons. They only change the *direction* of the electrons, not their speed (and therefore not their de Broglie wavelength).
- **中文:** 认为磁透镜会“减慢”或“加速”电子。它们只改变电子的*方向*，而不改变其速度（因此也不改变其德布罗意波长）。

### Exam Tips / 考试提示
- **English:** You don't need to know the detailed physics of magnetic lenses, but you must understand their *purpose*: to focus the electron beam.
- **中文:** 你不需要知道磁透镜的详细物理原理，但必须理解它们的*目的*：聚焦电子束。

> 📷 **IMAGE PROMPT — DIAGRAM-02: Magnetic Lens Focusing**
> A cross-section diagram of a magnetic lens. Show a coil of wire (electromagnet) with a current. Draw several electron paths entering from the top, initially parallel. As they pass through the magnetic field region (shown as a shaded area), the paths curve inward and converge to a focal point below the lens. Label the coil, magnetic field lines, electron beam, and focal point in both English and Chinese.

## 4.3 The Need for a Vacuum / 真空的必要性

### Explanation / 解释
**English:** The entire column of an electron microscope must be kept under a high vacuum. This is crucial for two main reasons:
1.  **To prevent electron scattering:** Air molecules would collide with the electron beam, scattering it and preventing a focused, coherent beam from reaching the specimen. This would drastically reduce resolution and image quality.
2.  **To protect the electron source:** The filament (usually tungsten) that emits electrons is at a very high temperature. In the presence of oxygen, it would rapidly oxidize and burn out. A vacuum prevents this.

**中文:** 电子显微镜的整个镜筒必须保持在高真空状态下。这至关重要，主要有两个原因：
1.  **防止电子散射：** 空气分子会与电子束碰撞，使其散射，从而阻止聚焦的、相干的电子束到达样本。这会极大地降低分辨率和图像质量。
2.  **保护电子源：** 发射电子的灯丝（通常是钨丝）处于非常高的温度。在有氧气存在的情况下，它会迅速氧化并烧毁。真空可以防止这种情况发生。

### Physical Meaning / 物理意义
**English:** The mean free path of an electron in air at atmospheric pressure is extremely short. For the electron to travel from the source to the specimen (a distance of up to a meter or more) without colliding with air molecules, the pressure must be reduced to a very low level.

**中文:** 在大气压下，电子在空气中的平均自由程非常短。为了使电子从源行进到样本（距离可达一米或更长）而不与空气分子碰撞，必须将压力降低到非常低的水平。

### Common Misconceptions / 常见误区
- **English:** Thinking the vacuum is needed to prevent the sample from being damaged. While some samples can be damaged by the beam, the primary reason for the vacuum is to protect the beam and the source.
- **中文:** 认为真空是为了防止样本被损坏。虽然某些样本可能被电子束损坏，但真空的主要原因是保护电子束和电子源。

### Exam Tips / 考试提示
- **English:** This is a very common exam question. Be ready to state the two main reasons for the vacuum.
- **中文:** 这是一个非常常见的考试题目。准备好陈述真空的两个主要原因。

---

# 5. Essential Equations / 核心公式

## 5.1 de Broglie Wavelength of an Accelerated Electron / 加速电子的德布罗意波长

$$ \lambda = \frac{h}{p} = \frac{h}{\sqrt{2 m e V}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\lambda$ | de Broglie wavelength | 德布罗意波长 | m (meters) |
| $h$ | Planck's constant ($6.63 \times 10^{-34} \text{ J s}$) | 普朗克常数 | J s |
| $p$ | Momentum of the electron | 电子的动量 | kg m s$^{-1}$ |
| $m$ | Mass of an electron ($9.11 \times 10^{-31} \text{ kg}$) | 电子质量 | kg |
| $e$ | Elementary charge ($1.60 \times 10^{-19} \text{ C}$) | 元电荷 | C |
| $V$ | Accelerating voltage | 加速电压 | V (volts) |

**Derivation / 推导:**
1.  Kinetic energy gained by electron: $E_k = eV$
2.  Kinetic energy in terms of momentum: $E_k = \frac{p^2}{2m}$
3.  Equating: $\frac{p^2}{2m} = eV \Rightarrow p = \sqrt{2 m e V}$
4.  de Broglie relation: $\lambda = \frac{h}{p} = \frac{h}{\sqrt{2 m e V}}$

**Conditions / 适用条件:**
- **English:** This formula is valid for non-relativistic electrons. For accelerating voltages above about 100 kV, relativistic effects become significant and a relativistic correction is needed. At A-Level, you will almost always use this non-relativistic formula.
- **中文:** 该公式适用于非相对论性电子。对于大约100 kV以上的加速电压，相对论效应变得显著，需要进行相对论修正。在A-Level考试中，你几乎总是使用这个非相对论公式。

**Limitations / 局限性:**
- **English:** It assumes all the electrical potential energy is converted into kinetic energy. It does not account for energy losses.
- **中文:** 它假设所有电势能都转化为动能。它不考虑能量损失。

> 📷 **IMAGE PROMPT — DIAGRAM-03: Wavelength vs Voltage Graph**
> A graph showing the de Broglie wavelength $\lambda$ on the y-axis and accelerating voltage $V$ on the x-axis. The curve should show a steep decrease at low voltages and a more gradual decrease at higher voltages, illustrating the inverse square root relationship $\lambda \propto 1/\sqrt{V}$.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 de Broglie Wavelength vs. Accelerating Voltage / 德布罗意波长与加速电压的关系

### Axes / 坐标轴
- **X-axis:** Accelerating Voltage, $V$ / 加速电压 $V$
- **Y-axis:** de Broglie Wavelength, $\lambda$ / 德布罗意波长 $\lambda$

### Shape / 形状
- **English:** A decreasing curve. The wavelength decreases rapidly at first, then more slowly as voltage increases. It follows an inverse square root relationship ($\lambda \propto 1/\sqrt{V}$).
- **中文:** 一条下降的曲线。波长起初迅速减小，然后随着电压增加而减慢。它遵循反平方根关系 ($\lambda \propto 1/\sqrt{V}$)。

### Gradient Meaning / 斜率含义
- **English:** The gradient of the curve at any point represents the rate of change of wavelength with respect to voltage. It is negative and its magnitude decreases as voltage increases.
- **中文:** 曲线上任意一点的斜率表示波长相对于电压的变化率。它是负的，其大小随着电压的增加而减小。

### Area Meaning / 面积含义
- **English:** The area under this curve has no direct physical meaning.
- **中文:** 该曲线下的面积没有直接的物理意义。

### Exam Interpretation / 考试解读
- **English:** You may be asked to use this graph to find the wavelength for a given voltage, or to explain why increasing the voltage improves resolution (because it decreases the wavelength).
- **中文:** 你可能会被要求使用此图来查找给定电压下的波长，或解释为什么增加电压可以提高分辨率（因为它减小了波长）。

---

# 7. Required Diagrams / 必备图表

## 7.1 Transmission Electron Microscope (TEM) / 透射电子显微镜

### Description / 描述
- **English:** A schematic diagram showing the main components of a TEM: an electron gun (cathode and anode), a condenser magnetic lens, the specimen, an objective magnetic lens, a projector magnetic lens, and a fluorescent screen or detector. The path of the electron beam should be shown.
- **中文:** 显示TEM主要部件的示意图：电子枪（阴极和阳极）、聚光磁透镜、样本、物镜磁透镜、投影磁透镜以及荧光屏或探测器。应显示电子束的路径。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-04: Transmission Electron Microscope (TEM) Schematic**
> A clean, labeled schematic diagram of a Transmission Electron Microscope. At the top, an "Electron Gun" with a "Cathode" (filament) and "Anode". Below it, a "Condenser Lens" (magnetic coil). Below that, a thin "Specimen" on a grid. Below the specimen, an "Objective Lens". Below that, a "Projector Lens". At the bottom, a "Fluorescent Screen / Detector". Arrows show the "Electron Beam" path from top to bottom. All labels in English and Chinese. The entire column is enclosed in a "Vacuum Chamber" label.

### Labels Required / 需要标注
- Electron Gun / 电子枪
- Cathode (Filament) / 阴极 (灯丝)
- Anode / 阳极
- Condenser Lens / 聚光透镜
- Specimen (thin) / 样本 (薄)
- Objective Lens / 物镜
- Projector Lens / 投影透镜
- Fluorescent Screen / Detector / 荧光屏 / 探测器
- Vacuum Chamber / 真空室

### Exam Importance / 考试重要性
- **English:** Very high. You must be able to draw and label a simple schematic of a TEM and explain the function of each part.
- **中文:** 非常高。你必须能够绘制并标注TEM的简单示意图，并解释每个部分的功能。

## 7.2 Scanning Electron Microscope (SEM) / 扫描电子显微镜

### Description / 描述
- **English:** A schematic diagram showing the main components of an SEM: an electron gun, condenser and objective magnetic lenses (to focus the beam to a fine point), scanning coils, the specimen, and a detector for secondary electrons.
- **中文:** 显示SEM主要部件的示意图：电子枪、聚光和物镜磁透镜（将光束聚焦成一个细点）、扫描线圈、样本以及二次电子探测器。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-05: Scanning Electron Microscope (SEM) Schematic**
> A clean, labeled schematic diagram of a Scanning Electron Microscope. At the top, an "Electron Gun". Below it, "Condenser and Objective Lenses" focusing the beam. Below the lenses, "Scanning Coils" that deflect the beam. The focused beam scans across the surface of a "Specimen". A "Secondary Electron Detector" is placed at an angle near the specimen. Arrows show the "Electron Beam" path. All labels in English and Chinese. The entire column is enclosed in a "Vacuum Chamber" label.

### Labels Required / 需要标注
- Electron Gun / 电子枪
- Condenser and Objective Lenses / 聚光和物镜
- Scanning Coils / 扫描线圈
- Specimen / 样本
- Secondary Electron Detector / 二次电子探测器
- Vacuum Chamber / 真空室

### Exam Importance / 考试重要性
- **English:** High. You should be able to draw and label a simple schematic of an SEM and explain how it differs from a TEM.
- **中文:** 高。你应该能够绘制并标注SEM的简单示意图，并解释它与TEM的不同之处。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating de Broglie Wavelength / 计算德布罗意波长

### Question / 题目
**English:** An electron is accelerated from rest through a potential difference of 50 kV in an electron microscope. Calculate the de Broglie wavelength of the electron. (Use $h = 6.63 \times 10^{-34} \text{ J s}$, $m_e = 9.11 \times 10^{-31} \text{ kg}$, $e = 1.60 \times 10^{-19} \text{ C}$)
**中文:** 在电子显微镜中，一个电子从静止开始经过50 kV的电势差加速。计算该电子的德布罗意波长。（使用 $h = 6.63 \times 10^{-34} \text{ J s}$, $m_e = 9.11 \times 10^{-31} \text{ kg}$, $e = 1.60 \times 10^{-19} \text{ C}$）

### Solution / 解答
**Step 1: Write down the known quantities.**
$V = 50 \text{ kV} = 50 \times 10^3 \text{ V} = 5.0 \times 10^4 \text{ V}$
$h = 6.63 \times 10^{-34} \text{ J s}$
$m = 9.11 \times 10^{-31} \text{ kg}$
$e = 1.60 \times 10^{-19} \text{ C}$

**Step 2: Use the formula for the de Broglie wavelength of an accelerated electron.**
$$ \lambda = \frac{h}{\sqrt{2 m e V}} $$

**Step 3: Substitute the values.**
$$ \lambda = \frac{6.63 \times 10^{-34}}{\sqrt{2 \times (9.11 \times 10^{-31}) \times (1.60 \times 10^{-19}) \times (5.0 \times 10^4)}} $$

**Step 4: Calculate the denominator.**
First, calculate the product inside the square root:
$2 \times 9.11 \times 10^{-31} \times 1.60 \times 10^{-19} \times 5.0 \times 10^4 = 2 \times 9.11 \times 1.60 \times 5.0 \times 10^{-31-19+4} = 145.76 \times 10^{-46} = 1.4576 \times 10^{-44}$

Now, take the square root:
$\sqrt{1.4576 \times 10^{-44}} = \sqrt{1.4576} \times \sqrt{10^{-44}} = 1.207 \times 10^{-22} \text{ kg}^{1/2} \text{ m}^{1/2} \text{ s}^{-1/2} \text{ C}^{1/2} \text{ V}^{1/2}$

**Step 5: Calculate the wavelength.**
$$ \lambda = \frac{6.63 \times 10^{-34}}{1.207 \times 10^{-22}} = 5.49 \times 10^{-12} \text{ m} $$

### Final Answer / 最终答案
**Answer:** $\lambda = 5.49 \times 10^{-12} \text{ m}$ (or 0.00549 nm) | **答案：** $\lambda = 5.49 \times 10^{-12} \text{ m}$ (或 0.00549 nm)

### Quick Tip / 提示
- **English:** Always convert kV to V before substituting into the formula. Remember that the wavelength is in the picometer (pm) range for typical electron microscope voltages.
- **中文:** 在代入公式前，务必将kV转换为V。请记住，对于典型的电子显微镜电压，波长在皮米（pm）量级。

## Example 2: Comparing Resolution / 比较分辨率

### Question / 题目
**English:** An optical microscope uses light of wavelength 550 nm. An electron microscope uses electrons accelerated through 100 kV. Calculate the ratio of the resolution of the electron microscope to that of the optical microscope, assuming the resolution is directly proportional to the wavelength.
**中文:** 一台光学显微镜使用波长为550 nm的光。一台电子显微镜使用经过100 kV加速的电子。假设分辨率与波长成正比，计算电子显微镜与光学显微镜的分辨率之比。

### Solution / 解答
**Step 1: Calculate the de Broglie wavelength of the electron.**
$\lambda_e = \frac{h}{\sqrt{2 m e V}} = \frac{6.63 \times 10^{-34}}{\sqrt{2 \times 9.11 \times 10^{-31} \times 1.60 \times 10^{-19} \times 100 \times 10^3}}$
$\lambda_e = \frac{6.63 \times 10^{-34}}{\sqrt{2.915 \times 10^{-44}}} = \frac{6.63 \times 10^{-34}}{5.40 \times 10^{-22}} = 1.23 \times 10^{-12} \text{ m}$

**Step 2: Write the wavelength of light.**
$\lambda_{light} = 550 \text{ nm} = 550 \times 10^{-9} \text{ m} = 5.50 \times 10^{-7} \text{ m}$

**Step 3: Calculate the ratio of resolutions.**
Since resolution $\propto \lambda$, the ratio of resolutions is:
$$ \frac{\text{Resolution}_{electron}}{\text{Resolution}_{optical}} = \frac{\lambda_e}{\lambda_{light}} = \frac{1.23 \times 10^{-12}}{5.50 \times 10^{-7}} = 2.24 \times 10^{-6} $$

### Final Answer / 最终答案
**Answer:** The electron microscope's resolution is $2.24 \times 10^{-6}$ times that of the optical microscope (i.e., it is about 450,000 times better). | **答案：** 电子显微镜的分辨率是光学显微镜的 $2.24 \times 10^{-6}$ 倍（即大约好45万倍）。

### Quick Tip / 提示
- **English:** This calculation dramatically illustrates why electron microscopes can see much finer details than optical microscopes.
- **中文:** 这个计算戏剧性地说明了为什么电子显微镜能看到比光学显微镜精细得多的细节。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of de Broglie wavelength from accelerating voltage | Very High | Medium | 📝 *待填入* |
| Explanation of why electron microscopes have higher resolution | Very High | Easy | 📝 *待填入* |
| Comparison of TEM and SEM | High | Medium | 📝 *待填入* |
| Explanation of the function of magnetic lenses | Medium | Medium | 📝 *待填入* |
| Explanation of the need for a vacuum | High | Easy | 📝 *待填入* |
| Advantages and limitations of electron microscopes | High | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Explain, Describe, Compare, Contrast, State, Suggest
- **中文:** 计算，解释，描述，比较，对比，陈述，提出

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic connects to practical skills in several ways:
- **Data Analysis:** You may be given data for accelerating voltage and corresponding de Broglie wavelength and asked to plot a graph or determine a relationship.
- **Uncertainties:** You might need to calculate the uncertainty in the de Broglie wavelength given uncertainties in voltage or other constants.
- **Experimental Design:** You could be asked to design a simple experiment to demonstrate the wave nature of electrons (e.g., [[Electron Diffraction and the Davisson-Germer Experiment]]), which is the underlying principle of the electron microscope.
- **Limitations:** Understanding the limitations of electron microscopes (e.g., need for vacuum, sample preparation, potential for beam damage) is a key practical consideration.

**中文:**
本子知识点通过以下几种方式与实验技能相联系：
- **数据分析：** 你可能会获得加速电压和相应德布罗意波长的数据，并被要求绘制图表或确定关系。
- **不确定度：** 你可能需要根据电压或其他常数的不确定度来计算德布罗意波长的不确定度。
- **实验设计：** 你可能会被要求设计一个简单的实验来证明电子的波动性（例如，[[电子衍射与戴维森-革末实验]]），这是电子显微镜的基本原理。
- **局限性：** 理解电子显微镜的局限性（例如，需要真空、样品制备、潜在的束流损伤）是一个关键的实践考量。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core Concept
    A[Electron Microscope] --> B[Principle: de Broglie Wavelength]
    A --> C[Key Components]
    A --> D[Types]
    A --> E[Advantages & Limitations]

    %% Principle
    B --> F[λ = h / √(2 m e V)]
    B --> G[Shorter λ → Higher Resolution]
    B --> H[Overcomes Abbe Diffraction Limit]

    %% Components
    C --> I[Electron Gun]
    C --> J[Magnetic Lenses]
    C --> K[Vacuum Chamber]
    C --> L[Detector / Screen]

    I --> M[Thermionic Emission]
    J --> N[Focus Beam via Lorentz Force]
    K --> O[Prevents Scattering & Oxidation]

    %% Types
    D --> P[Transmission Electron Microscope (TEM)]
    D --> Q[Scanning Electron Microscope (SEM)]

    P --> R[Electrons Transmit Through Thin Sample]
    P --> S[High Resolution, 2D Internal Structure]
    Q --> T[Electrons Scan Surface]
    Q --> U[3D Surface Topography]

    %% Advantages & Limitations
    E --> V[Advantage: Very High Resolution]
    E --> W[Limitation: Requires Vacuum]
    E --> X[Limitation: Sample Must be Conductive/Thin]
    E --> Y[Limitation: Expensive & Large]

    %% Connections to other topics
    B -.-> Z[[de Broglie Wavelength]]
    B -.-> AA[[Electron Diffraction and the Davisson-Germer Experiment]]
    B -.-> AB[[Wave-Particle Duality for Matter]]
    A -.-> AC[[The Photoelectric Effect]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | A microscope using a beam of electrons to achieve very high resolution. / 使用电子束实现非常高分辨率的显微镜。 |
| **Key Formula / 核心公式** | $\lambda = \frac{h}{\sqrt{2 m e V}}$ |
| **Key Graph / 核心图表** | $\lambda$ vs $V$: Decreasing curve ($\lambda \propto 1/\sqrt{V}$). / $\lambda$ 对 $V$ 的图：下降曲线 ($\lambda \propto 1/\sqrt{V}$)。 |
| **Key Diagrams / 核心图表** | Schematic of TEM (transmission) and SEM (scanning). / TEM（透射）和SEM（扫描）的示意图。 |
| **Key Advantage / 关键优势** | Much higher resolution than optical microscopes due to the much shorter de Broglie wavelength of electrons. / 由于电子的德布罗意波长更短，分辨率远高于光学显微镜。 |
| **Key Limitations / 关键局限** | Requires a vacuum; samples must be very thin (TEM) or conductive (SEM); expensive; potential for beam damage. / 需要真空；样品必须非常薄（TEM）或导电（SEM）；昂贵；可能存在束流损伤。 |
| **Exam Tip / 考试提示** | Always state that resolution is limited by wavelength. For calculations, convert kV to V. / 始终说明分辨率受波长限制。计算时，将kV转换为V。 |