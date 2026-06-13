# Path Difference and Phase Difference / 光程差与相位差

---

# 1. Overview / 概述

**English:**
Path difference and phase difference are fundamental concepts that describe the relationship between two or more waves arriving at a point. Path difference ($\Delta x$) is the physical distance one wave travels more than another, while phase difference ($\Delta \phi$) describes how much one wave is "ahead" or "behind" another in its cycle. These two quantities are directly proportional — a path difference of one wavelength corresponds to a phase difference of $2\pi$ radians (or 360°). Understanding this relationship is essential for predicting whether waves will interfere [[Constructive and Destructive Interference|constructively or destructively]] at a given point, forming the mathematical foundation of the [[Principle of Superposition]]. This sub-topic is critical for analysing [[Young's Double-Slit Experiment]], [[Diffraction and the Diffraction Grating]], and [[Stationary Waves]].

**中文:**
光程差和相位差是描述两个或多个波到达某一点时相互关系的基本概念。光程差（$\Delta x$）是一个波比另一个波多传播的物理距离，而相位差（$\Delta \phi$）描述了一个波在周期中比另一个波"领先"或"落后"多少。这两个量成正比关系——一个波长的光程差对应 $2\pi$ 弧度（或360°）的相位差。理解这种关系对于预测波在给定点是否会[[Constructive and Destructive Interference|相长或相消干涉]]至关重要，构成了[[Principle of Superposition|叠加原理]]的数学基础。本子知识点对于分析[[Young's Double-Slit Experiment|杨氏双缝实验]]、[[Diffraction and the Diffraction Grating|衍射和衍射光栅]]以及[[Stationary Waves|驻波]]至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 8.1(a) Explain the meaning of the terms path difference and phase difference | 5.12 Understand the terms path difference and phase difference |
| 8.1(b) State the relationship between path difference and phase difference | 5.13 Use the relationship between path difference and phase difference |
| 8.1(c) Use the relationship $\Delta \phi = \frac{2\pi}{\lambda} \Delta x$ | 5.14 Apply the relationship to interference problems |
| 8.1(d) Determine whether interference is constructive or destructive from path/phase difference | 5.15 Determine conditions for constructive and destructive interference |
| 8.1(e) Apply to two-source interference patterns | 5.16 Solve problems involving two-source interference |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to convert between path difference and phase difference using the formula $\Delta \phi = \frac{2\pi}{\lambda} \Delta x$. They must also be able to determine whether interference is constructive ($\Delta \phi = 2n\pi$ or $\Delta x = n\lambda$) or destructive ($\Delta \phi = (2n+1)\pi$ or $\Delta x = (n+\frac{1}{2})\lambda$) for any given situation.
- **中文:** 学生必须能够使用公式 $\Delta \phi = \frac{2\pi}{\lambda} \Delta x$ 在光程差和相位差之间进行转换。还必须能够判断在任何给定情况下干涉是相长（$\Delta \phi = 2n\pi$ 或 $\Delta x = n\lambda$）还是相消（$\Delta \phi = (2n+1)\pi$ 或 $\Delta x = (n+\frac{1}{2})\lambda$）。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Path Difference** / 光程差 | The difference in distance travelled by two waves from their sources to a point of observation. | 两个波从波源到观测点所传播距离的差值。 | Confusing path difference with the distance between sources. Path difference is measured at the observation point, not at the sources. |
| **Phase Difference** / 相位差 | The difference in phase between two oscillating particles or waves, measured in radians or degrees. | 两个振荡质点或波之间的相位差异，以弧度或度为单位测量。 | Forgetting that phase difference is measured in radians (not degrees) in most A-Level formulas. |
| **Coherent Sources** / 相干波源 | Sources that have a constant phase difference and the same frequency. | 具有恒定相位差和相同频率的波源。 | Assuming any two sources are coherent — they must have constant phase difference. |
| **Wavelength** / 波长 | The distance between successive points of the same phase on a wave. | 波上相邻同相点之间的距离。 | Using wavelength in the path difference formula without checking units (must be in same units). |
| **Constructive Interference** / 相长干涉 | When two waves meet with a phase difference of $0, 2\pi, 4\pi, ...$ (path difference of $0, \lambda, 2\lambda, ...$) | 当两个波以 $0, 2\pi, 4\pi, ...$ 的相位差（$0, \lambda, 2\lambda, ...$ 的光程差）相遇时。 | Thinking constructive interference always means maximum amplitude — it requires equal amplitudes too. |
| **Destructive Interference** / 相消干涉 | When two waves meet with a phase difference of $\pi, 3\pi, 5\pi, ...$ (path difference of $\frac{\lambda}{2}, \frac{3\lambda}{2}, ...$) | 当两个波以 $\pi, 3\pi, 5\pi, ...$ 的相位差（$\frac{\lambda}{2}, \frac{3\lambda}{2}, ...$ 的光程差）相遇时。 | Forgetting the half-wavelength condition — destructive interference occurs at odd multiples of half-wavelengths. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Relationship Between Path Difference and Phase Difference / 光程差与相位差的关系

### Explanation / 解释
**English:**
The relationship between path difference ($\Delta x$) and phase difference ($\Delta \phi$) is derived from the wave equation. A wave completes one full cycle ($2\pi$ radians) as it travels one wavelength ($\lambda$). Therefore, the phase difference is proportional to the path difference:

$$ \Delta \phi = \frac{2\pi}{\lambda} \Delta x $$

Where:
- $\Delta \phi$ = phase difference (radians)
- $\Delta x$ = path difference (metres)
- $\lambda$ = wavelength (metres)

This relationship can also be expressed in degrees: $\Delta \phi = \frac{360^\circ}{\lambda} \Delta x$

**中文:**
光程差（$\Delta x$）和相位差（$\Delta \phi$）之间的关系源自波动方程。波传播一个波长（$\lambda$）完成一个完整周期（$2\pi$ 弧度）。因此，相位差与光程差成正比：

$$ \Delta \phi = \frac{2\pi}{\lambda} \Delta x $$

其中：
- $\Delta \phi$ = 相位差（弧度）
- $\Delta x$ = 光程差（米）
- $\lambda$ = 波长（米）

这个关系也可以用度数表示：$\Delta \phi = \frac{360^\circ}{\lambda} \Delta x$

### Physical Meaning / 物理意义
**English:**
If two waves start in phase at their sources, the wave that travels further will be "behind" in its cycle. For every extra wavelength travelled, the wave lags by one complete cycle ($2\pi$ radians). This means that at the observation point, the two waves are at different points in their oscillation cycles.

**中文:**
如果两个波在波源处同相开始，传播更远的波将在其周期中"落后"。每多传播一个波长，波就落后一个完整周期（$2\pi$ 弧度）。这意味着在观测点，两个波处于其振荡周期的不同位置。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking path difference is the distance between sources (it's the difference in distances from sources to the observation point)
  - Confusing phase difference with phase constant (phase difference is relative between two waves)
  - Using degrees in formulas that require radians
  - Forgetting that $\Delta \phi = 0$ means waves are in phase, not that there is no wave

- **中文:**
  - 认为光程差是波源之间的距离（实际是从波源到观测点的距离差）
  - 混淆相位差和相位常数（相位差是两个波之间的相对量）
  - 在需要弧度的公式中使用度数
  - 忘记 $\Delta \phi = 0$ 意味着波同相，而不是没有波

### Exam Tips / 考试提示
- **English:** Always check whether the question asks for phase difference in radians or degrees. Convert using $\pi \text{ rad} = 180^\circ$. For interference problems, first find the path difference, then convert to phase difference.
- **中文:** 始终检查题目要求相位差用弧度还是度表示。使用 $\pi \text{ rad} = 180^\circ$ 进行转换。对于干涉问题，先求光程差，再转换为相位差。

> 📷 **IMAGE PROMPT — PD01: Path Difference Diagram**
> Two coherent wave sources S1 and S2 emitting circular waves. A point P is shown at a distance r1 from S1 and r2 from S2. The path difference Δx = |r1 - r2| is labelled. The waves are shown as concentric circles with alternating crests (solid) and troughs (dashed). The point P is located where the waves from both sources meet. Labels: S1, S2, r1, r2, Δx, P. Clean white background, educational style, suitable for A-Level physics textbook.

---

## 4.2 Conditions for Constructive and Destructive Interference / 相长和相消干涉的条件

### Explanation / 解释
**English:**
Using the relationship between path difference and phase difference, we can determine the conditions for interference:

**Constructive Interference (maximum amplitude):**
- Phase difference: $\Delta \phi = 2n\pi$ where $n = 0, 1, 2, 3, ...$
- Path difference: $\Delta x = n\lambda$ where $n = 0, 1, 2, 3, ...$

**Destructive Interference (minimum amplitude):**
- Phase difference: $\Delta \phi = (2n+1)\pi$ where $n = 0, 1, 2, 3, ...$
- Path difference: $\Delta x = (n + \frac{1}{2})\lambda$ where $n = 0, 1, 2, 3, ...$

**中文:**
利用光程差和相位差的关系，我们可以确定干涉的条件：

**相长干涉（最大振幅）：**
- 相位差：$\Delta \phi = 2n\pi$，其中 $n = 0, 1, 2, 3, ...$
- 光程差：$\Delta x = n\lambda$，其中 $n = 0, 1, 2, 3, ...$

**相消干涉（最小振幅）：**
- 相位差：$\Delta \phi = (2n+1)\pi$，其中 $n = 0, 1, 2, 3, ...$
- 光程差：$\Delta x = (n + \frac{1}{2})\lambda$，其中 $n = 0, 1, 2, 3, ...$

### Physical Meaning / 物理意义
**English:**
When two waves arrive in phase (phase difference = 0, $2\pi$, $4\pi$, ...), their displacements add to give maximum amplitude — constructive interference. When they arrive exactly out of phase (phase difference = $\pi$, $3\pi$, $5\pi$, ...), their displacements cancel — destructive interference. The path difference tells us how many extra wavelengths one wave has travelled, which directly determines the phase relationship.

**中文:**
当两个波同相到达时（相位差 = 0, $2\pi$, $4\pi$, ...），它们的位移相加得到最大振幅——相长干涉。当它们正好反相到达时（相位差 = $\pi$, $3\pi$, $5\pi$, ...），它们的位移相互抵消——相消干涉。光程差告诉我们一个波多传播了多少个波长，这直接决定了相位关系。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking $n$ starts at 1 for constructive interference (it starts at 0 — the central maximum)
  - Forgetting that destructive interference requires odd multiples of half-wavelengths, not just any half-wavelength
  - Assuming complete cancellation always occurs (this requires equal amplitudes)
  - Confusing $n$ in constructive ($n\lambda$) with $n$ in destructive ($(n+\frac{1}{2})\lambda$)

- **中文:**
  - 认为相长干涉的 $n$ 从1开始（实际从0开始——中央极大）
  - 忘记相消干涉需要半波长的奇数倍，而不仅仅是任何半波长
  - 假设总是完全抵消（这需要振幅相等）
  - 混淆相长干涉中的 $n$（$n\lambda$）和相消干涉中的 $n$（$(n+\frac{1}{2})\lambda$）

### Exam Tips / 考试提示
- **English:** For two-source interference, the central maximum (directly opposite the midpoint between sources) always has path difference = 0 and is constructive. Use this as a reference point.
- **中文:** 对于双源干涉，中央极大（正对两波源中点）的光程差总是为0，是相长干涉。以此作为参考点。

> 📷 **IMAGE PROMPT — PD02: Constructive vs Destructive Interference**
> Two diagrams side by side. Left: Two waves in phase (crest aligned with crest) showing constructive interference with a larger resultant wave. Right: Two waves out of phase by π (crest aligned with trough) showing destructive interference with a flat line resultant. Labels: "Constructive: Δφ = 0, 2π, 4π..." and "Destructive: Δφ = π, 3π, 5π...". Clean educational style.

---

## 4.3 Phase Difference from Initial Conditions / 初始条件引起的相位差

### Explanation / 解释
**English:**
Sometimes waves start with an initial phase difference at their sources. For example:
- If one source is $\frac{\lambda}{2}$ further from the observation point than the other, the path difference contributes $\pi$ to the phase difference
- If the sources themselves are out of phase (e.g., one source is $\pi$ radians ahead), this adds to the phase difference from path difference

The total phase difference is:
$$ \Delta \phi_{\text{total}} = \Delta \phi_{\text{path}} + \Delta \phi_{\text{initial}} $$

Where $\Delta \phi_{\text{path}} = \frac{2\pi}{\lambda} \Delta x$

**中文:**
有时波在波源处就有初始相位差。例如：
- 如果一个波源比另一个离观测点远 $\frac{\lambda}{2}$，光程差贡献 $\pi$ 的相位差
- 如果波源本身不同相（例如，一个波源领先 $\pi$ 弧度），这会加到光程差引起的相位差上

总相位差为：
$$ \Delta \phi_{\text{总}} = \Delta \phi_{\text{光程}} + \Delta \phi_{\text{初始}} $$

其中 $\Delta \phi_{\text{光程}} = \frac{2\pi}{\lambda} \Delta x$

### Physical Meaning / 物理意义
**English:**
The phase difference at the observation point depends on two factors: (1) the difference in distances travelled (path difference), and (2) any initial phase difference between the sources. This is why coherent sources must have a constant phase difference — if the initial phase difference varies, the interference pattern changes unpredictably.

**中文:**
观测点的相位差取决于两个因素：(1) 传播距离的差异（光程差），(2) 波源之间的任何初始相位差。这就是为什么相干波源必须有恒定的相位差——如果初始相位差变化，干涉图案会不可预测地变化。

### Common Misconceptions / 常见误区
- **English:**
  - Forgetting to include initial phase difference when sources are not in phase
  - Adding phase differences incorrectly (they add algebraically, not vectorially)
  - Thinking that path difference alone determines interference (initial phase matters too)

- **中文:**
  - 当波源不同相时忘记包括初始相位差
  - 错误地相加相位差（它们是代数相加，不是矢量相加）
  - 认为仅光程差就决定干涉（初始相位也很重要）

### Exam Tips / 考试提示
- **English:** If a question says "sources are in phase" or "coherent sources", assume $\Delta \phi_{\text{initial}} = 0$ unless stated otherwise. If sources are "out of phase by $\pi$", add this to your calculation.
- **中文:** 如果题目说"波源同相"或"相干波源"，除非另有说明，否则假设 $\Delta \phi_{\text{初始}} = 0$。如果波源"反相（相差 $\pi$）"，将其加到计算中。

---

# 5. Essential Equations / 核心公式

## Equation 1: Phase Difference from Path Difference

$$ \Delta \phi = \frac{2\pi}{\lambda} \Delta x $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta \phi$ | Phase difference | 相位差 | rad (radians) |
| $\lambda$ | Wavelength | 波长 | m |
| $\Delta x$ | Path difference | 光程差 | m |

**Derivation / 推导:**
A wave travels one wavelength ($\lambda$) in one complete cycle ($2\pi$ radians). Therefore, the phase change per unit distance is $\frac{2\pi}{\lambda}$. For a path difference $\Delta x$, the phase difference is $\frac{2\pi}{\lambda} \times \Delta x$.

**Conditions / 适用条件:**
- **English:** Waves must have the same frequency and wavelength. The medium must be uniform (constant wave speed).
- **中文:** 波必须具有相同的频率和波长。介质必须均匀（波速恒定）。

**Limitations / 局限性:**
- **English:** This formula assumes waves travel in the same medium. If waves travel through different media, the wavelength changes and the formula must be applied separately for each segment.
- **中文:** 该公式假设波在相同介质中传播。如果波通过不同介质传播，波长会变化，必须分别对每段应用公式。

## Equation 2: Constructive Interference Condition

$$ \Delta x = n\lambda \quad \text{or} \quad \Delta \phi = 2n\pi $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $n$ | Integer (0, 1, 2, 3, ...) | 整数 (0, 1, 2, 3, ...) | dimensionless |
| $\Delta x$ | Path difference | 光程差 | m |
| $\lambda$ | Wavelength | 波长 | m |
| $\Delta \phi$ | Phase difference | 相位差 | rad |

**Conditions / 适用条件:**
- **English:** Sources must be coherent (constant phase difference, same frequency). Amplitudes should be equal for maximum effect.
- **中文:** 波源必须相干（恒定相位差，相同频率）。为获得最大效果，振幅应相等。

## Equation 3: Destructive Interference Condition

$$ \Delta x = \left(n + \frac{1}{2}\right)\lambda \quad \text{or} \quad \Delta \phi = (2n+1)\pi $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $n$ | Integer (0, 1, 2, 3, ...) | 整数 (0, 1, 2, 3, ...) | dimensionless |
| $\Delta x$ | Path difference | 光程差 | m |
| $\lambda$ | Wavelength | 波长 | m |
| $\Delta \phi$ | Phase difference | 相位差 | rad |

**Conditions / 适用条件:**
- **English:** Sources must be coherent. For complete cancellation, amplitudes must be equal.
- **中文:** 波源必须相干。为完全抵消，振幅必须相等。

> 📷 **IMAGE PROMPT — PD03: Phase Difference Formula Diagram**
> A wave shown as a sine curve with one wavelength λ marked. Below, the same wave is shown shifted by Δx. The phase difference Δφ is shown as the angular separation on a circular reference diagram. Labels: λ, Δx, Δφ = 2πΔx/λ. Educational style.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Phase Difference vs Path Difference / 相位差与光程差的关系

### Axes / 坐标轴
- **X-axis:** Path difference $\Delta x$ (m) / 光程差 $\Delta x$（米）
- **Y-axis:** Phase difference $\Delta \phi$ (rad) / 相位差 $\Delta \phi$（弧度）

### Shape / 形状
**English:** A straight line through the origin with gradient $\frac{2\pi}{\lambda}$. The relationship is directly proportional.

**中文:** 一条通过原点的直线，斜率为 $\frac{2\pi}{\lambda}$。关系是正比关系。

### Gradient Meaning / 斜率含义
**English:** The gradient $\frac{2\pi}{\lambda}$ represents the phase change per unit path difference. A shorter wavelength gives a steeper gradient (more phase difference per metre of path difference).

**中文:** 斜率 $\frac{2\pi}{\lambda}$ 表示单位光程差引起的相位变化。波长越短，斜率越大（每米光程差引起的相位差越大）。

### Area Meaning / 面积含义
**English:** Not applicable — the area under this graph has no physical significance.

**中文:** 不适用——该图下方的面积没有物理意义。

### Exam Interpretation / 考试解读
**English:** Given any path difference, you can read off the phase difference from this graph. The graph also shows that for constructive interference ($\Delta \phi = 2n\pi$), the path difference must be $n\lambda$.

**中文:** 给定任何光程差，可以从该图中读出相位差。该图还显示，对于相长干涉（$\Delta \phi = 2n\pi$），光程差必须为 $n\lambda$。

```mermaid
graph LR
    A[Path Difference Δx] -->|Multiply by 2π/λ| B[Phase Difference Δφ]
    B -->|Δφ = 2nπ| C[Constructive Interference]
    B -->|Δφ = (2n+1)π| D[Destructive Interference]
    A -->|Δx = nλ| C
    A -->|Δx = (n+½)λ| D
```

---

# 7. Required Diagrams / 必备图表

## 7.1 Path Difference in Two-Source Interference / 双源干涉中的光程差

### Description / 描述
**English:** A diagram showing two coherent sources S1 and S2 separated by distance $d$, and a point P at a large distance $D$ from the sources. The distances from S1 to P ($r_1$) and S2 to P ($r_2$) are shown. The path difference $\Delta x = |r_1 - r_2|$ is labelled. For points far away (Fraunhofer condition), the path difference can be approximated as $\Delta x = d\sin\theta$ where $\theta$ is the angle from the central axis.

**中文:** 一个显示两个相干波源 S1 和 S2（间距为 $d$）以及距离波源很远 $D$ 处的点 P 的示意图。显示了从 S1 到 P（$r_1$）和从 S2 到 P（$r_2$）的距离。光程差 $\Delta x = |r_1 - r_2|$ 被标注。对于远处的点（夫琅禾费条件），光程差可以近似为 $\Delta x = d\sin\theta$，其中 $\theta$ 是偏离中心轴的角度。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — PD04: Two-Source Path Difference**
> Two point sources S1 and S2 separated by distance d. A distant point P is shown at angle θ from the central axis. The distances r1 (from S1 to P) and r2 (from S2 to P) are drawn as straight lines. A dashed perpendicular line from S1 to the line S2P shows the path difference d sinθ. Labels: S1, S2, d, P, θ, r1, r2, Δx = d sinθ. Clean educational diagram, white background.

### Labels Required / 需要标注
- S1, S2 (sources / 波源)
- $d$ (source separation / 波源间距)
- $P$ (observation point / 观测点)
- $\theta$ (angle from central axis / 偏离中心轴的角度)
- $r_1$, $r_2$ (distances from sources / 到波源的距离)
- $\Delta x = d\sin\theta$ (path difference / 光程差)

### Exam Importance / 考试重要性
**English:** This diagram is essential for understanding [[Young's Double-Slit Experiment]] and [[Diffraction and the Diffraction Grating]]. The approximation $\Delta x = d\sin\theta$ is used in nearly all two-source interference problems.

**中文:** 该图对于理解[[Young's Double-Slit Experiment|杨氏双缝实验]]和[[Diffraction and the Diffraction Grating|衍射和衍射光栅]]至关重要。近似 $\Delta x = d\sin\theta$ 几乎用于所有双源干涉问题。

---

## 7.2 Phase Difference on a Wave Diagram / 波图上的相位差

### Description / 描述
**English:** A diagram showing two waves with the same frequency and wavelength but shifted relative to each other. The phase difference is shown as the fraction of a cycle between corresponding points (e.g., crest to crest). For a phase difference of $\pi$, one wave's crest aligns with the other's trough.

**中文:** 一个显示两个频率和波长相同但相对偏移的波的示意图。相位差显示为对应点（例如，波峰到波峰）之间的周期分数。对于 $\pi$ 的相位差，一个波的波峰与另一个波的波谷对齐。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — PD05: Phase Difference on Wave Diagram**
> Two sine waves on the same axes. Wave 1 (solid blue) and Wave 2 (dashed red) with same amplitude and wavelength. The horizontal shift between them is labelled as Δx (path difference). A vertical arrow shows the phase difference Δφ as a fraction of 2π. Labels: Wave 1, Wave 2, λ, Δx, Δφ. Educational style, clean background.

### Labels Required / 需要标注
- Wave 1, Wave 2 (波1, 波2)
- $\lambda$ (wavelength / 波长)
- $\Delta x$ (path difference / 光程差)
- $\Delta \phi$ (phase difference / 相位差)

### Exam Importance / 考试重要性
**English:** This diagram helps visualise the relationship between path difference and phase difference. Students should be able to sketch such diagrams to explain interference conditions.

**中文:** 该图有助于直观理解光程差和相位差之间的关系。学生应该能够画出这样的图来解释干涉条件。

---

# 8. Worked Examples / 典型例题

## Example 1: Converting Path Difference to Phase Difference / 光程差转换为相位差

### Question / 题目
**English:**
Two coherent sources emit waves of wavelength 500 nm. At a point P, the waves from the two sources have travelled distances of 2.50 mm and 2.75 mm respectively. Calculate:
(a) The path difference at P
(b) The phase difference at P in radians
(c) State whether the interference at P is constructive or destructive

**中文:**
两个相干波源发射波长为 500 nm 的波。在点 P，来自两个波源的波分别传播了 2.50 mm 和 2.75 mm。计算：
(a) 点 P 的光程差
(b) 点 P 的相位差（弧度）
(c) 说明点 P 的干涉是相长还是相消

### Solution / 解答

**Step 1: Calculate path difference**
$$ \Delta x = |r_1 - r_2| = |2.50 \text{ mm} - 2.75 \text{ mm}| = 0.25 \text{ mm} = 2.5 \times 10^{-4} \text{ m} $$

**Step 2: Convert wavelength to metres**
$$ \lambda = 500 \text{ nm} = 500 \times 10^{-9} \text{ m} = 5.0 \times 10^{-7} \text{ m} $$

**Step 3: Calculate phase difference**
$$ \Delta \phi = \frac{2\pi}{\lambda} \Delta x = \frac{2\pi}{5.0 \times 10^{-7}} \times 2.5 \times 10^{-4} $$
$$ \Delta \phi = \frac{2\pi \times 2.5 \times 10^{-4}}{5.0 \times 10^{-7}} = \frac{2\pi \times 500}{1} = 1000\pi \text{ rad} $$

**Step 4: Determine interference type**
$$ \Delta \phi = 1000\pi = 2(500)\pi $$
Since $\Delta \phi = 2n\pi$ where $n = 500$, the interference is constructive.

### Final Answer / 最终答案
**Answer:**
(a) $\Delta x = 2.5 \times 10^{-4} \text{ m}$
(b) $\Delta \phi = 1000\pi \text{ rad}$
(c) Constructive interference / 相长干涉

**答案：**
(a) $\Delta x = 2.5 \times 10^{-4} \text{ m}$
(b) $\Delta \phi = 1000\pi \text{ rad}$
(c) 相长干涉

### Quick Tip / 提示
**English:** When the phase difference is a large multiple of $\pi$, simplify by dividing by $2\pi$ to find $n$. If $n$ is an integer, it's constructive; if $n$ is a half-integer (e.g., 500.5), it's destructive.

**中文:** 当相位差是 $\pi$ 的大倍数时，除以 $2\pi$ 简化求 $n$。如果 $n$ 是整数，则为相长干涉；如果 $n$ 是半整数（例如 500.5），则为相消干涉。

---

## Example 2: Finding Positions of Constructive Interference / 求相长干涉的位置

### Question / 题目
**English:**
Two coherent sources S1 and S2 are separated by 0.50 mm. They emit waves of wavelength 600 nm. A screen is placed 1.5 m away. Calculate the distance from the central maximum to the first-order maximum ($n=1$) on the screen.

**中文:**
两个相干波源 S1 和 S2 相距 0.50 mm。它们发射波长为 600 nm 的波。屏幕放置在 1.5 m 远处。计算从中央极大到屏幕上第一级极大（$n=1$）的距离。

### Solution / 解答

**Step 1: Identify known quantities**
$$ d = 0.50 \text{ mm} = 5.0 \times 10^{-4} \text{ m} $$
$$ \lambda = 600 \text{ nm} = 6.0 \times 10^{-7} \text{ m} $$
$$ D = 1.5 \text{ m} $$
$$ n = 1 $$

**Step 2: Use the condition for constructive interference**
For constructive interference: $\Delta x = n\lambda = d\sin\theta$

$$ d\sin\theta = n\lambda $$
$$ \sin\theta = \frac{n\lambda}{d} = \frac{1 \times 6.0 \times 10^{-7}}{5.0 \times 10^{-4}} = 1.2 \times 10^{-3} $$

**Step 3: Use small angle approximation**
For small angles, $\sin\theta \approx \tan\theta \approx \frac{y}{D}$, where $y$ is the distance from the central maximum.

$$ \frac{y}{D} = \frac{n\lambda}{d} $$
$$ y = \frac{n\lambda D}{d} = \frac{1 \times 6.0 \times 10^{-7} \times 1.5}{5.0 \times 10^{-4}} $$
$$ y = \frac{9.0 \times 10^{-7}}{5.0 \times 10^{-4}} = 1.8 \times 10^{-3} \text{ m} = 1.8 \text{ mm} $$

### Final Answer / 最终答案
**Answer:** $y = 1.8 \text{ mm}$ from the central maximum / 距离中央极大 1.8 mm

**答案：** $y = 1.8 \text{ mm}$

### Quick Tip / 提示
**English:** The formula $y = \frac{n\lambda D}{d}$ is derived from the path difference condition. Remember that this uses the small angle approximation, which is valid when $D \gg d$ (screen is far from sources).

**中文:** 公式 $y = \frac{n\lambda D}{d}$ 由光程差条件推导得出。记住这使用了小角度近似，当 $D \gg d$（屏幕远离波源）时有效。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate phase difference from path difference | High | Easy | 📝 *待填入* |
| Determine constructive/destructive from given distances | High | Medium | 📝 *待填入* |
| Find position of maxima/minima in double-slit | High | Medium | 📝 *待填入* |
| Explain why sources must be coherent | Medium | Easy | 📝 *待填入* |
| Combined with initial phase difference | Low | Hard | 📝 *待填入* |
| Phase difference in stationary waves | Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, State, Explain, Show that, Sketch, Deduce
- **中文:** 计算，确定，说明，解释，证明，画出，推导

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Path difference and phase difference concepts are essential for understanding and analysing several required practicals:

1. **[[Young's Double-Slit Experiment]] (CIE 9702/ Edexcel IAL):**
   - Measuring fringe spacing to determine wavelength
   - Understanding why fringes form (path difference changes across the screen)
   - Calculating expected positions of maxima and minima

2. **Measuring Wavelength Using a Diffraction Grating:**
   - Using $\Delta x = d\sin\theta$ to find path difference
   - Applying constructive interference condition $d\sin\theta = n\lambda$

3. **Stationary Waves on a String:**
   - Understanding that nodes occur where path difference between incident and reflected waves leads to destructive interference
   - Antinodes occur where constructive interference occurs

**Measurements and Uncertainties:**
- Measuring fringe spacing with a ruler or travelling microscope
- Estimating uncertainty in fringe spacing measurements
- Using multiple fringes to reduce percentage uncertainty

**Graph Plotting:**
- Plotting $y$ (fringe position) against $n$ (order number) to find wavelength from gradient
- The gradient $\frac{\lambda D}{d}$ gives the fringe spacing

**Experimental Design:**
- Ensuring sources are coherent (using a single source with two slits)
- Using monochromatic light (laser or filter) to maintain constant wavelength
- Measuring $D$ (distance to screen) accurately

**中文:**
光程差和相位差的概念对于理解和分析几个必修实验至关重要：

1. **[[Young's Double-Slit Experiment|杨氏双缝实验]]（CIE 9702/ Edexcel IAL）：**
   - 测量条纹间距以确定波长
   - 理解条纹形成的原因（光程差在屏幕上变化）
   - 计算极大和极小的预期位置

2. **使用衍射光栅测量波长：**
   - 使用 $\Delta x = d\sin\theta$ 求光程差
   - 应用相长干涉条件 $d\sin\theta = n\lambda$

3. **弦上的驻波：**
   - 理解波节出现在入射波和反射波之间的光程差导致相消干涉的位置
   - 波腹出现在相长干涉的位置

**测量和不确定度：**
- 用尺子或读数显微镜测量条纹间距
- 估计条纹间距测量的不确定度
- 使用多个条纹以减少百分比不确定度

**图表绘制：**
- 绘制 $y$（条纹位置）对 $n$（级数）的图，从斜率求波长
- 斜率 $\frac{\lambda D}{d}$ 给出条纹间距

**实验设计：**
- 确保波源相干（使用单个光源和两个狭缝）
- 使用单色光（激光或滤光片）以保持恒定波长
- 准确测量 $D$（到屏幕的距离）

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core concepts
    PD[Path Difference Δx] -->|Δφ = 2πΔx/λ| PHD[Phase Difference Δφ]
    
    %% Interference conditions
    PD -->|Δx = nλ| CI[Constructive Interference]
    PD -->|Δx = (n+½)λ| DI[Destructive Interference]
    PHD -->|Δφ = 2nπ| CI
    PHD -->|Δφ = (2n+1)π| DI
    
    %% Prerequisites
    PW[Progressive Waves] -->|provides| WAV[Wave Properties: λ, f, v]
    WAV --> PD
    WAV --> PHD
    
    %% Applications
    CI -->|produces| MAX[Maxima / Bright Fringes]
    DI -->|produces| MIN[Minima / Dark Fringes]
    
    %% Experiments
    YDSE[Young's Double-Slit] -->|uses| PD
    DG[Diffraction Grating] -->|uses| PD
    SW[Stationary Waves] -->|involves| PHD
    
    %% Parent topic
    SI[Superposition and Interference] -->|contains| PD
    SI -->|contains| PHD
    SI -->|contains| CI
    SI -->|contains| DI
    
    %% Styling
    classDef core fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef condition fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef result fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef experiment fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    
    class PD,PHD core
    class CI,DI condition
    class MAX,MIN result
    class YDSE,DG,SW experiment
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Path difference = difference in distances travelled by two waves / 光程差 = 两个波传播距离的差 |
| | Phase difference = how much one wave leads/lags another in its cycle / 相位差 = 一个波在周期中领先/落后另一个波的程度 |
| **Key Formula / 核心公式** | $\Delta \phi = \frac{2\pi}{\lambda} \Delta x$ |
| | $\Delta \phi$ in degrees: $\Delta \phi = \frac{360^\circ}{\lambda} \Delta x$ |
| **Constructive / 相长** | $\Delta x = n\lambda$ (n = 0, 1, 2, ...) |
| | $\Delta \phi = 2n\pi$ rad |
| **Destructive / 相消** | $\Delta x = (n + \frac{1}{2})\lambda$ (n = 0, 1, 2, ...) |
| | $\Delta \phi = (2n+1)\pi$ rad |
| **Key Graph / 核心图表** | $\Delta \phi$ vs $\Delta x$: straight line through origin, gradient $= \frac{2\pi}{\lambda}$ |
| **Common Mistake / 常见错误** | Using degrees in radian formulas / 在弧度公式中使用度数 |
| | Forgetting $n$ starts at 0 for constructive / 忘记相长干涉的 $n$ 从0开始 |
| | Confusing path difference with source separation / 混淆光程差和波源间距 |
| **Exam Tip / 考试提示** | Always convert all lengths to metres first / 始终先将所有长度转换为米 |
| | For double-slit: $y = \frac{n\lambda D}{d}$ for maxima / 对于双缝：极大值 $y = \frac{n\lambda D}{d}$ |
| | Check if sources are in phase or have initial phase difference / 检查波源是否同相或有初始相位差 |
| **Units / 单位** | $\Delta x$: m (metres) / 米 |
| | $\Delta \phi$: rad (radians) or degrees / 弧度或度 |
| | $\lambda$: m (metres) / 米 |

---

> 📋 **CIE Only:** CAIE 9702 specifically requires students to "explain the meaning of" path difference and phase difference (AO1 knowledge), and to "use the relationship" (AO2 application). Expect definition questions and calculation problems.
>
> 📋 **Edexcel Only:** Edexcel IAL uses the command word "understand" for definitions and "use" for applications. Problems often appear in the context of the Young's double-slit experiment or diffraction gratings.

---

**Related Leaf Nodes:**
- [[Principle of Superposition]]
- [[Constructive and Destructive Interference]]
- [[Young's Double-Slit Experiment]]

**Parent Hub:**
- [[Superposition and Interference]]

**Prerequisites:**
- [[Progressive Waves]]

**Related Topics:**
- [[Stationary Waves]]
- [[Diffraction and the Diffraction Grating]]