# 1. Overview / 概述

**English:**
Faraday's Law of Electromagnetic Induction is the quantitative foundation of electromagnetic induction, stating that the magnitude of the induced electromotive force (EMF) in a circuit is directly proportional to the rate of change of [[Magnetic Flux and Flux Linkage|magnetic flux linkage]] through the circuit. This law, discovered by Michael Faraday in 1831, is one of the most fundamental principles in physics, forming the basis for electrical generators, transformers, and countless modern technologies. In the A-Level syllabus, Faraday's Law is the central equation that connects the abstract concept of [[Magnetic Flux and Flux Linkage|flux linkage]] to the measurable induced EMF, and it works in conjunction with [[Lenz's Law and the Direction of Induced EMF|Lenz's Law]] to determine both the magnitude and direction of induced EMF. Understanding this law is essential for mastering topics like [[AC Generators and Transformers]] and [[Induced EMF in a Moving Conductor]].

**中文:**
法拉第电磁感应定律是电磁感应的定量基础，它指出电路中感应电动势的大小与穿过该电路的[[Magnetic Flux and Flux Linkage|磁通链]]变化率成正比。这一定律由迈克尔·法拉第于1831年发现，是物理学中最基本的原理之一，构成了发电机、变压器以及无数现代技术的基础。在A-Level大纲中，法拉第定律是将[[Magnetic Flux and Flux Linkage|磁通链]]的抽象概念与可测量的感应电动势联系起来的核心方程，它与[[Lenz's Law and the Direction of Induced EMF|楞次定律]]共同作用，以确定感应电动势的大小和方向。理解这一定律对于掌握[[AC Generators and Transformers]]和[[Induced EMF in a Moving Conductor]]等主题至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 20.3(a) Define magnetic flux linkage | 3.10 Understand the concept of magnetic flux |
| 20.3(b) Recall and use Faraday's law of electromagnetic induction | 3.11 Understand and use Faraday's law of electromagnetic induction |
| 20.3(c) Explain the factors affecting induced EMF | 3.12 Solve problems involving induced EMF |
| 20.3(d) Apply Faraday's law to simple situations | 3.13 Understand the relationship between flux linkage and induced EMF |
| 20.3(e) Derive the expression for induced EMF in a rotating coil | 3.14 Derive and use the expression for EMF in a rotating coil |
| 20.3(f) Solve problems involving induced EMF and flux linkage | 3.15 Understand the factors affecting the magnitude of induced EMF |
| 20.3(g) Explain the difference between induced EMF and induced current | |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to recall Faraday's Law in both words and equation form ($\mathcal{E} = -N\frac{d\Phi}{dt}$). They should understand that the negative sign represents [[Lenz's Law and the Direction of Induced EMF|Lenz's Law]]. Students must be able to calculate induced EMF from graphs of flux linkage against time, and derive the expression for a rotating coil in a uniform magnetic field.
- **中文:** 学生必须能够用文字和方程形式（$\mathcal{E} = -N\frac{d\Phi}{dt}$）复述法拉第定律。他们应理解负号代表[[Lenz's Law and the Direction of Induced EMF|楞次定律]]。学生必须能够从磁通链-时间图中计算感应电动势，并推导出在均匀磁场中旋转线圈的表达式。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Faraday's Law** / 法拉第定律 | The magnitude of the induced EMF in a circuit is directly proportional to the rate of change of magnetic flux linkage through the circuit. | 电路中感应电动势的大小与穿过该电路的磁通链变化率成正比。 | Confusing "rate of change of flux" with "flux" itself. A constant flux produces zero induced EMF. |
| **Induced EMF ($\mathcal{E}$)** / 感应电动势 | The electromotive force generated in a circuit due to a changing magnetic flux linkage. | 由于磁通链变化而在电路中产生的电动势。 | Thinking induced EMF is the same as induced current — EMF is the cause, current is the effect. |
| **Rate of change of flux linkage ($\frac{d\Phi}{dt}$)** / 磁通链变化率 | The derivative of magnetic flux linkage with respect to time, measured in webers per second (Wb s⁻¹). | 磁通链对时间的导数，单位为韦伯每秒（Wb s⁻¹）。 | Forgetting that this is a rate — using total change $\Delta\Phi$ instead of $\frac{d\Phi}{dt}$. |
| **Magnetic Flux Linkage ($N\Phi$)** / 磁通链 | The product of the number of turns $N$ of a coil and the magnetic flux $\Phi$ through each turn. | 线圈匝数 $N$ 与穿过每匝磁通量 $\Phi$ 的乘积。 | Confusing flux ($\Phi$) with flux linkage ($N\Phi$). |
| **Lenz's Law** / 楞次定律 | The direction of the induced EMF is such that it opposes the change that produced it. | 感应电动势的方向总是阻碍产生它的变化。 | Forgetting the negative sign in Faraday's Law equation. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Quantitative Relationship / 定量关系

### Explanation / 解释
**English:**
Faraday's Law is expressed mathematically as:

$$ \mathcal{E} = -N\frac{d\Phi}{dt} $$

Where:
- $\mathcal{E}$ is the induced EMF (in volts, V)
- $N$ is the number of turns in the coil
- $\frac{d\Phi}{dt}$ is the rate of change of magnetic flux through one turn (in Wb s⁻¹)

The negative sign is a mathematical representation of [[Lenz's Law and the Direction of Induced EMF|Lenz's Law]] — it indicates that the induced EMF opposes the change in flux that produced it. This is not just a sign convention; it reflects the conservation of energy. If the induced EMF aided the change, it would create a runaway effect, violating energy conservation.

For a coil with $N$ turns, the total flux linkage is $N\Phi$, so the law can also be written as:

$$ \mathcal{E} = -\frac{d(N\Phi)}{dt} $$

**中文:**
法拉第定律的数学表达式为：

$$ \mathcal{E} = -N\frac{d\Phi}{dt} $$

其中：
- $\mathcal{E}$ 是感应电动势（单位：伏特，V）
- $N$ 是线圈匝数
- $\frac{d\Phi}{dt}$ 是通过一匝线圈的磁通量变化率（单位：Wb s⁻¹）

负号是[[Lenz's Law and the Direction of Induced EMF|楞次定律]]的数学表示——它表明感应电动势阻碍产生它的磁通变化。这不仅仅是一个符号约定；它反映了能量守恒。如果感应电动势促进变化，就会产生失控效应，违反能量守恒。

对于有 $N$ 匝的线圈，总磁通链为 $N\Phi$，因此该定律也可以写为：

$$ \mathcal{E} = -\frac{d(N\Phi)}{dt} $$

### Physical Meaning / 物理意义
**English:**
Faraday's Law tells us that:
1. **It's the change that matters** — a constant magnetic flux produces NO induced EMF, regardless of how large the flux is.
2. **Faster changes produce larger EMFs** — the induced EMF is proportional to the rate of change, not the total change.
3. **More turns give larger EMFs** — each turn of the coil contributes to the total induced EMF.
4. **The induced EMF opposes the change** — this is the physical meaning of the negative sign.

**中文:**
法拉第定律告诉我们：
1. **变化才是关键** — 恒定的磁通量不会产生感应电动势，无论磁通量有多大。
2. **变化越快，电动势越大** — 感应电动势与变化率成正比，而非总变化量。
3. **匝数越多，电动势越大** — 线圈的每一匝都对总感应电动势有贡献。
4. **感应电动势阻碍变化** — 这是负号的物理意义。

### Common Misconceptions / 常见误区
- **English:**
  - ❌ "A large magnetic flux produces a large induced EMF." → ✅ Only a *changing* flux produces an induced EMF.
  - ❌ "The induced EMF is proportional to $\Delta\Phi$." → ✅ It is proportional to $\frac{\Delta\Phi}{\Delta t}$ (the rate of change).
  - ❌ "The negative sign is optional." → ✅ The negative sign is essential and represents Lenz's Law.
  - ❌ "Induced EMF and induced current are the same thing." → ✅ EMF is the cause; current is the effect (depends on circuit resistance).

- **中文:**
  - ❌ "大的磁通量产生大的感应电动势。" → ✅ 只有*变化的*磁通量才会产生感应电动势。
  - ❌ "感应电动势与$\Delta\Phi$成正比。" → ✅ 它与$\frac{\Delta\Phi}{\Delta t}$（变化率）成正比。
  - ❌ "负号是可选的。" → ✅ 负号是必不可少的，代表楞次定律。
  - ❌ "感应电动势和感应电流是同一回事。" → ✅ 电动势是原因；电流是结果（取决于电路电阻）。

### Exam Tips / 考试提示
- **English:** When calculating induced EMF from a graph of flux linkage vs. time, remember that the EMF equals the negative of the gradient. For a straight-line graph, EMF is constant. For a curved graph, EMF varies with time. Always include the negative sign in your equation, even if you only need the magnitude.
- **中文:** 从磁通链-时间图计算感应电动势时，记住电动势等于斜率的负值。对于直线图，电动势是恒定的。对于曲线图，电动势随时间变化。始终在方程中包含负号，即使只需要大小。

---

# 5. Essential Equations / 核心公式

## Equation 1: Faraday's Law (Standard Form) / 法拉第定律（标准形式）

$$ \mathcal{E} = -N\frac{d\Phi}{dt} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\mathcal{E}$ | Induced electromotive force | 感应电动势 | V (volts) |
| $N$ | Number of turns in the coil | 线圈匝数 | dimensionless |
| $\frac{d\Phi}{dt}$ | Rate of change of magnetic flux | 磁通量变化率 | Wb s⁻¹ (or V) |
| $\Phi$ | Magnetic flux ($\Phi = BA\cos\theta$) | 磁通量 | Wb (webers) |

**Derivation / 推导:**
Faraday's Law is an empirical law — it was discovered experimentally. It cannot be derived from more fundamental principles; it is itself a fundamental law of electromagnetism.

**Conditions / 适用条件:**
- **English:** The law applies to any closed circuit experiencing a changing magnetic flux. It is valid for both motional EMF (where the conductor moves) and transformer EMF (where the magnetic field changes).
- **中文:** 该定律适用于任何经历磁通量变化的闭合电路。它适用于动生电动势（导体运动）和感生电动势（磁场变化）。

**Limitations / 局限性:**
- **English:** Faraday's Law gives the magnitude and direction (via Lenz's Law) of the induced EMF, but it does not explain the mechanism by which the EMF is produced. For that, we need the concept of [[Induced EMF in a Moving Conductor|motional EMF]] or Maxwell's equations.
- **中文:** 法拉第定律给出了感应电动势的大小和方向（通过楞次定律），但没有解释产生电动势的机制。为此，我们需要[[Induced EMF in a Moving Conductor|动生电动势]]或麦克斯韦方程组的概念。

---

## Equation 2: Faraday's Law (Flux Linkage Form) / 法拉第定律（磁通链形式）

$$ \mathcal{E} = -\frac{d(N\Phi)}{dt} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $N\Phi$ | Magnetic flux linkage | 磁通链 | Wb (webers) |
| $\frac{d(N\Phi)}{dt}$ | Rate of change of flux linkage | 磁通链变化率 | Wb s⁻¹ (or V) |

**Derivation / 推导:**
This is simply a rearrangement of the standard form, combining $N$ and $\Phi$ into the single quantity "flux linkage."

**Conditions / 适用条件:**
- **English:** This form is particularly useful when dealing with coils where the number of turns is fixed.
- **中文:** 这种形式在处理匝数固定的线圈时特别有用。

---

## Equation 3: Induced EMF in a Rotating Coil / 旋转线圈中的感应电动势

$$ \mathcal{E} = NBA\omega\sin(\omega t) $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $N$ | Number of turns | 匝数 | dimensionless |
| $B$ | Magnetic flux density | 磁通密度 | T (tesla) |
| $A$ | Area of the coil | 线圈面积 | m² |
| $\omega$ | Angular velocity | 角速度 | rad s⁻¹ |
| $t$ | Time | 时间 | s |

**Derivation / 推导:**
For a coil rotating in a uniform magnetic field, the flux through the coil at time $t$ is:
$$\Phi = BA\cos\theta = BA\cos(\omega t)$$

The flux linkage is:
$$N\Phi = NBA\cos(\omega t)$$

Applying Faraday's Law:
$$\mathcal{E} = -\frac{d(N\Phi)}{dt} = -\frac{d}{dt}[NBA\cos(\omega t)] = NBA\omega\sin(\omega t)$$

**Conditions / 适用条件:**
- **English:** This equation assumes the coil rotates with constant angular velocity $\omega$ in a uniform magnetic field $B$, starting from the position where the plane of the coil is perpendicular to the field ($\theta = 0$ at $t=0$).
- **中文:** 该方程假设线圈在均匀磁场 $B$ 中以恒定角速度 $\omega$ 旋转，从线圈平面垂直于磁场的位置开始（$t=0$ 时 $\theta=0$）。

**Limitations / 局限性:**
- **English:** This is an idealized model. Real generators have factors like resistance, inductance, and non-uniform fields that modify the output.
- **中文:** 这是一个理想化模型。实际发电机具有电阻、电感和非均匀场等因素，会改变输出。

> 📷 **IMAGE PROMPT — EQ01: Faraday's Law Visualization**
> A clear diagram showing a coil with N turns connected to a galvanometer. A bar magnet is shown moving towards the coil. Arrows indicate the direction of magnetic field lines. The galvanometer needle deflects, showing induced EMF. Labels: "Magnetic flux Φ", "N turns", "Induced EMF ε", "Rate of change dΦ/dt". The equation ε = -N dΦ/dt is displayed prominently.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Flux Linkage vs. Time for a Rotating Coil / 旋转线圈的磁通链-时间图

### Axes / 坐标轴
- **X-axis:** Time ($t$) / 时间 ($t$)
- **Y-axis:** Magnetic flux linkage ($N\Phi$) / 磁通链 ($N\Phi$)

### Shape / 形状
- **English:** Cosine curve: $N\Phi = NBA\cos(\omega t)$. The graph is a cosine wave with amplitude $NBA$ and period $T = \frac{2\pi}{\omega}$.
- **中文:** 余弦曲线：$N\Phi = NBA\cos(\omega t)$。该图是振幅为 $NBA$、周期为 $T = \frac{2\pi}{\omega}$ 的余弦波。

### Gradient Meaning / 斜率含义
- **English:** The gradient of the flux linkage-time graph is $\frac{d(N\Phi)}{dt}$, which is the negative of the induced EMF ($\mathcal{E} = -\frac{d(N\Phi)}{dt}$). The gradient is steepest when $N\Phi = 0$ (coil parallel to field), and zero when $N\Phi$ is maximum (coil perpendicular to field).
- **中文:** 磁通链-时间图的斜率为 $\frac{d(N\Phi)}{dt}$，即感应电动势的负值（$\mathcal{E} = -\frac{d(N\Phi)}{dt}$）。当 $N\Phi = 0$（线圈平行于磁场）时斜率最大，当 $N\Phi$ 最大（线圈垂直于磁场）时斜率为零。

### Area Meaning / 面积含义
- **English:** The area under the flux linkage-time graph has no direct physical meaning in this context.
- **中文:** 磁通链-时间图下的面积在此上下文中没有直接的物理意义。

### Exam Interpretation / 考试解读
- **English:** Students are often asked to sketch the induced EMF vs. time graph from the flux linkage vs. time graph. Remember: EMF is the negative gradient. So a cosine flux linkage gives a sine EMF. The EMF is maximum when flux linkage is zero, and zero when flux linkage is maximum.
- **中文:** 学生经常被要求从磁通链-时间图画出感应电动势-时间图。记住：电动势是斜率的负值。因此，余弦磁通链给出正弦电动势。当磁通链为零时电动势最大，当磁通链最大时电动势为零。

```mermaid
graph TD
    subgraph "Flux Linkage vs Time"
        A[Cosine wave: NΦ = NBA cos(ωt)]
    end
    subgraph "Induced EMF vs Time"
        B[Sine wave: ε = NBAω sin(ωt)]
    end
    A -->|"Gradient = -ε"| B
```

---

## 6.2 Induced EMF vs. Time for a Rotating Coil / 旋转线圈的感应电动势-时间图

### Axes / 坐标轴
- **X-axis:** Time ($t$) / 时间 ($t$)
- **Y-axis:** Induced EMF ($\mathcal{E}$) / 感应电动势 ($\mathcal{E}$)

### Shape / 形状
- **English:** Sine curve: $\mathcal{E} = NBA\omega\sin(\omega t)$. The graph is a sine wave with amplitude $NBA\omega$ and period $T = \frac{2\pi}{\omega}$.
- **中文:** 正弦曲线：$\mathcal{E} = NBA\omega\sin(\omega t)$。该图是振幅为 $NBA\omega$、周期为 $T = \frac{2\pi}{\omega}$ 的正弦波。

### Gradient Meaning / 斜率含义
- **English:** The gradient of the EMF-time graph gives the rate of change of induced EMF, which is related to the second derivative of flux linkage.
- **中文:** 电动势-时间图的斜率给出感应电动势的变化率，与磁通链的二阶导数有关。

### Area Meaning / 面积含义
- **English:** The area under the EMF-time graph represents the change in flux linkage ($\Delta(N\Phi) = \int \mathcal{E} dt$). This is a key relationship: the integral of EMF with respect to time gives the total change in flux linkage.
- **中文:** 电动势-时间图下的面积代表磁通链的变化（$\Delta(N\Phi) = \int \mathcal{E} dt$）。这是一个关键关系：电动势对时间的积分给出磁通链的总变化。

### Exam Interpretation / 考试解读
- **English:** The amplitude of the induced EMF is $NBA\omega$. This shows that the maximum EMF can be increased by: increasing $N$ (more turns), increasing $B$ (stronger magnet), increasing $A$ (larger coil), or increasing $\omega$ (faster rotation).
- **中文:** 感应电动势的振幅为 $NBA\omega$。这表明最大电动势可以通过以下方式增加：增加 $N$（更多匝数）、增加 $B$（更强的磁场）、增加 $A$（更大的线圈）或增加 $\omega$（更快的旋转）。

> 📷 **IMAGE PROMPT — GR01: Flux Linkage and Induced EMF Graphs**
> Two graphs stacked vertically with aligned time axes. Top graph: Cosine wave labeled "Flux Linkage NΦ" with amplitude NBA and period T. Bottom graph: Sine wave labeled "Induced EMF ε" with amplitude NBAω and same period T. Vertical dashed lines show that EMF is maximum when flux linkage is zero, and EMF is zero when flux linkage is maximum. Labels: "ε = -d(NΦ)/dt".

---

# 7. Required Diagrams / 必备图表

## 7.1 Faraday's Law Experiment / 法拉第定律实验

### Description / 描述
**English:** A diagram showing the classic Faraday's law demonstration: a coil connected to a sensitive galvanometer, with a bar magnet being moved in and out of the coil. The diagram should show the magnetic field lines, the direction of motion, and the deflection of the galvanometer.

**中文:** 展示经典法拉第定律演示的图表：一个线圈连接到灵敏电流计，条形磁铁在线圈中移入移出。图表应显示磁场线、运动方向和电流计的偏转。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG01: Faraday's Law Experiment**
> A clean physics diagram showing a cylindrical coil with N visible turns of wire, connected by wires to a galvanometer (center-zero scale). A bar magnet with N and S poles labeled is shown partially inserted into the coil. Magnetic field lines (curved arrows) are shown from N to S pole. An arrow indicates the direction of magnet motion (v). The galvanometer needle is deflected to one side. Labels: "Coil (N turns)", "Galvanometer", "Bar magnet", "Magnetic field lines", "Direction of motion v". The equation ε = -N dΦ/dt is shown in a box. Style: textbook-quality, clean lines, white background, educational.

### Labels Required / 需要标注
- **English:** Coil (N turns), Galvanometer, Bar magnet (N/S poles), Magnetic field lines, Direction of motion (v), Induced EMF (ε)
- **中文:** 线圈（N匝），电流计，条形磁铁（N/S极），磁场线，运动方向（v），感应电动势（ε）

### Exam Importance / 考试重要性
- **English:** This is a standard experiment that students should be able to describe. Key observations: faster motion gives larger deflection; stronger magnet gives larger deflection; more turns give larger deflection; reversing direction reverses deflection.
- **中文:** 这是学生应该能够描述的标准实验。关键观察：运动越快，偏转越大；磁铁越强，偏转越大；匝数越多，偏转越大；反向运动使偏转反向。

---

## 7.2 Rotating Coil in a Magnetic Field / 磁场中的旋转线圈

### Description / 描述
**English:** A diagram showing a rectangular coil rotating in a uniform magnetic field between two magnetic poles. The coil is shown at an angle θ to the field, with the axis of rotation perpendicular to the field direction. The induced EMF is shown on a graph alongside.

**中文:** 展示矩形线圈在两个磁极之间的均匀磁场中旋转的图表。线圈与磁场成角度θ，旋转轴垂直于磁场方向。感应电动势显示在旁边图表中。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAG02: Rotating Coil in Magnetic Field**
> A detailed physics diagram showing a rectangular coil (N turns) placed between the N and S poles of a magnet. The coil is shown at an angle θ to the horizontal magnetic field lines. The axis of rotation is vertical (perpendicular to the page). The coil has sides of length l and width w, with area A = l×w. Labels: "Magnetic field B", "Coil area A", "Angle θ", "Axis of rotation", "N turns". Beside the diagram, a small graph shows a sine wave labeled "Induced EMF ε = NBAω sin(ωt)". Style: textbook-quality, clean lines, white background, educational.

### Labels Required / 需要标注
- **English:** Magnetic field (B), Coil area (A), Number of turns (N), Angle (θ), Axis of rotation, Induced EMF (ε)
- **中文:** 磁场（B），线圈面积（A），匝数（N），角度（θ），旋转轴，感应电动势（ε）

### Exam Importance / 考试重要性
- **English:** This diagram is essential for understanding how AC generators work. Students must be able to derive the expression $\mathcal{E} = NBA\omega\sin(\omega t)$ from this diagram.
- **中文:** 这个图表对于理解交流发电机的工作原理至关重要。学生必须能够从这个图表推导出表达式 $\mathcal{E} = NBA\omega\sin(\omega t)$。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Induced EMF from Flux Change / 从磁通变化计算感应电动势

### Question / 题目
**English:**
A coil with 200 turns has a magnetic flux of 0.05 Wb through each turn. The flux is reduced uniformly to zero in 0.25 s. Calculate the magnitude of the induced EMF in the coil.

**中文:**
一个200匝的线圈，每匝的磁通量为0.05 Wb。磁通量在0.25秒内均匀减小到零。计算线圈中感应电动势的大小。

### Solution / 解答

**Step 1: Identify the known quantities / 步骤1：确定已知量**
- $N = 200$ turns
- $\Phi_{\text{initial}} = 0.05$ Wb
- $\Phi_{\text{final}} = 0$ Wb
- $\Delta t = 0.25$ s

**Step 2: Calculate the change in flux / 步骤2：计算磁通变化**
$$\Delta\Phi = \Phi_{\text{final}} - \Phi_{\text{initial}} = 0 - 0.05 = -0.05 \text{ Wb}$$

**Step 3: Calculate the rate of change of flux / 步骤3：计算磁通变化率**
$$\frac{d\Phi}{dt} = \frac{\Delta\Phi}{\Delta t} = \frac{-0.05}{0.25} = -0.2 \text{ Wb s}^{-1}$$

**Step 4: Apply Faraday's Law / 步骤4：应用法拉第定律**
$$\mathcal{E} = -N\frac{d\Phi}{dt} = -(200)(-0.2) = 40 \text{ V}$$

### Final Answer / 最终答案
**Answer:** 40 V | **答案：** 40 V

### Quick Tip / 提示
- **English:** The question asks for the "magnitude," so we take the absolute value. However, always include the negative sign in your working to show you understand Lenz's Law.
- **中文:** 问题要求"大小"，所以我们取绝对值。但是，在计算过程中始终包含负号，以表明你理解楞次定律。

---

## Example 2: Rotating Coil in a Generator / 发电机中的旋转线圈

### Question / 题目
**English:**
A rectangular coil of 50 turns, each of area 0.04 m², rotates at 60 revolutions per second in a uniform magnetic field of flux density 0.5 T. The axis of rotation is perpendicular to the field direction.

(a) Calculate the maximum induced EMF.
(b) Write an expression for the induced EMF as a function of time, assuming the plane of the coil is perpendicular to the field at $t = 0$.

**中文:**
一个50匝的矩形线圈，每匝面积为0.04 m²，在磁通密度为0.5 T的均匀磁场中以每秒60转的速度旋转。旋转轴垂直于磁场方向。

(a) 计算最大感应电动势。
(b) 写出感应电动势作为时间函数的表达式，假设在 $t = 0$ 时线圈平面垂直于磁场。

### Solution / 解答

**Part (a): Maximum induced EMF / 部分(a)：最大感应电动势**

**Step 1: Convert angular velocity / 步骤1：转换角速度**
$$\omega = 2\pi f = 2\pi \times 60 = 120\pi \text{ rad s}^{-1}$$

**Step 2: Apply the formula for maximum EMF / 步骤2：应用最大电动势公式**
$$\mathcal{E}_{\text{max}} = NBA\omega$$
$$\mathcal{E}_{\text{max}} = 50 \times 0.5 \times 0.04 \times 120\pi$$
$$\mathcal{E}_{\text{max}} = 50 \times 0.5 \times 0.04 \times 120 \times 3.142$$
$$\mathcal{E}_{\text{max}} = 50 \times 0.5 \times 0.04 \times 377$$
$$\mathcal{E}_{\text{max}} = 50 \times 7.54$$
$$\mathcal{E}_{\text{max}} = 377 \text{ V}$$

**Part (b): Expression for induced EMF / 部分(b)：感应电动势表达式**

**Step 3: Write the general expression / 步骤3：写出一般表达式**
$$\mathcal{E} = \mathcal{E}_{\text{max}} \sin(\omega t)$$
$$\mathcal{E} = 377 \sin(120\pi t) \text{ V}$$

### Final Answer / 最终答案
**Answer:** (a) 377 V (b) $\mathcal{E} = 377\sin(120\pi t)$ V | **答案：** (a) 377 V (b) $\mathcal{E} = 377\sin(120\pi t)$ V

### Quick Tip / 提示
- **English:** Remember that $\omega = 2\pi f$, not $\omega = f$. A common mistake is to use frequency directly in the EMF equation. Also, check whether the coil starts perpendicular ($\cos$ form for flux, $\sin$ form for EMF) or parallel ($\sin$ form for flux, $\cos$ form for EMF) to the field.
- **中文:** 记住 $\omega = 2\pi f$，而不是 $\omega = f$。一个常见错误是直接在电动势方程中使用频率。另外，检查线圈是垂直于磁场开始（磁通为$\cos$形式，电动势为$\sin$形式）还是平行于磁场开始（磁通为$\sin$形式，电动势为$\cos$形式）。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate induced EMF from given flux change | Very High | Easy | 📝 *待填入* |
| Derive expression for rotating coil EMF | High | Medium | 📝 *待填入* |
| Interpret flux linkage vs. time graphs | High | Medium | 📝 *待填入* |
| Sketch EMF vs. time from flux linkage graph | Medium | Medium | 📝 *待填入* |
| Multi-step problem with Lenz's Law | Medium | Hard | 📝 *待填入* |
| Experimental design for Faraday's Law | Low | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Calculate", "Derive", "Sketch", "Explain", "Determine", "Show that", "State"
- **中文:** "计算"，"推导"，"画出"，"解释"，"确定"，"证明"，"陈述"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Faraday's Law connects to practical work in several ways:

1. **Measurements:** Students should be able to measure induced EMF using a voltmeter or data logger, and measure magnetic flux density using a Hall probe. Key measurements include: the time for a magnet to fall through a coil, the number of turns, and the area of the coil.

2. **Uncertainties:** The main sources of uncertainty in Faraday's Law experiments include: timing errors (especially for fast motions), non-uniform magnetic fields, and the difficulty of measuring instantaneous rate of change. Students should be able to estimate and combine these uncertainties.

3. **Graph Plotting:** A common experiment involves plotting induced EMF against the speed of the magnet (or rate of change of flux). The graph should be a straight line through the origin, confirming Faraday's Law. Students should be able to draw a line of best fit and calculate the gradient, which gives $N$ (if other quantities are known).

4. **Experimental Design:** Students should be able to design an experiment to investigate the factors affecting induced EMF: varying $N$ (using coils with different numbers of turns), varying $B$ (using different magnets), varying the speed of motion, and varying the area of the coil.

5. **Data Logger:** Using a data logger with a voltage sensor allows students to capture the induced EMF pulse as a magnet falls through a coil. The area under the EMF-time graph gives the change in flux linkage, which should equal $2N\Phi$ (for a magnet passing through and out).

**中文:**
法拉第定律在多个方面与实验工作相关：

1. **测量：** 学生应能够使用电压表或数据记录器测量感应电动势，并使用霍尔探头测量磁通密度。关键测量包括：磁铁通过线圈的时间、匝数和线圈面积。

2. **不确定度：** 法拉第定律实验中的主要不确定度来源包括：计时误差（特别是快速运动时）、非均匀磁场以及测量瞬时变化率的困难。学生应能够估计和合并这些不确定度。

3. **作图：** 一个常见的实验是绘制感应电动势与磁铁速度（或磁通变化率）的关系图。该图应为通过原点的直线，验证法拉第定律。学生应能够画出最佳拟合线并计算斜率，从而得到 $N$（如果其他量已知）。

4. **实验设计：** 学生应能够设计实验来研究影响感应电动势的因素：改变 $N$（使用不同匝数的线圈）、改变 $B$（使用不同的磁铁）、改变运动速度以及改变线圈面积。

5. **数据记录器：** 使用带有电压传感器的数据记录器，学生可以捕捉磁铁通过线圈时的感应电动势脉冲。电动势-时间图下的面积给出磁通链的变化，应等于 $2N\Phi$（对于磁铁穿过并离开的情况）。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Faraday's Law Leaf Node
    FL[Faraday's Law<br>ε = -N dΦ/dt] --> MF[Magnetic Flux<br>Φ = BA cos θ]
    FL --> FLX[Flux Linkage<br>NΦ]
    FL --> LL[Lenz's Law<br>Direction of EMF]
    FL --> RC[Rotating Coil<br>ε = NBAω sin(ωt)]
    
    MF --> MB[Magnetic Fields<br>and Forces]
    FLX --> N[Number of Turns N]
    FLX --> A[Area of Coil A]
    FLX --> B[Magnetic Flux Density B]
    
    RC --> AC[AC Generators<br>and Transformers]
    RC --> GR[Graphs: Flux & EMF vs Time]
    
    LL --> EC[Eddy Currents<br>and Their Applications]
    
    FL --> ME[Motional EMF<br>ε = Blv]
    ME --> MC[Moving Conductor<br>in Magnetic Field]
    
    %% Styling
    classDef leaf fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef parent fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef sibling fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef prerequisite fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    
    class FL leaf
    class MF,FLX,RC,ME,GR leaf
    class LL,EC,MC sibling
    class MB prerequisite
    class AC parent
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | The induced EMF in a circuit is proportional to the rate of change of magnetic flux linkage through the circuit. / 电路中感应电动势与穿过该电路的磁通链变化率成正比。 |
| **Key Formula / 核心公式** | $\mathcal{E} = -N\frac{d\Phi}{dt} = -\frac{d(N\Phi)}{dt}$ |
| **Rotating Coil / 旋转线圈** | $\mathcal{E} = NBA\omega\sin(\omega t)$, $\mathcal{E}_{\text{max}} = NBA\omega$ |
| **Key Graph / 核心图表** | Flux linkage vs. time: cosine wave; EMF vs. time: sine wave. EMF = negative gradient of flux linkage graph. / 磁通链-时间图：余弦波；电动势-时间图：正弦波。电动势 = 磁通链图斜率的负值。 |
| **Factors Affecting EMF / 影响电动势的因素** | $N$ (more turns → larger EMF), $B$ (stronger field → larger EMF), $A$ (larger area → larger EMF), $\frac{d\Phi}{dt}$ (faster change → larger EMF) / $N$（匝数多→电动势大），$B$（磁场强→电动势大），$A$（面积大→电动势大），$\frac{d\Phi}{dt}$（变化快→电动势大） |
| **Common Mistake / 常见错误** | Using $\Delta\Phi$ instead of $\frac{d\Phi}{dt}$; forgetting the negative sign; confusing flux with flux linkage. / 使用$\Delta\Phi$而非$\frac{d\Phi}{dt}$；忘记负号；混淆磁通量与磁通链。 |
| **Exam Tip / 考试提示** | Always write the negative sign in the equation. For graph questions, remember EMF = -gradient. For rotating coils, check the starting position. / 始终在方程中写负号。对于图表题，记住电动势 = -斜率。对于旋转线圈，检查起始位置。 |
| **Practical Connection / 实验联系** | Measure EMF with voltmeter/data logger; vary $N$, $B$, speed; plot EMF vs. speed to verify linear relationship. / 用电压表/数据记录器测量电动势；改变$N$、$B$、速度；绘制电动势-速度图验证线性关系。 |