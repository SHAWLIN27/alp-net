# 1. Overview / 概述

**English:**
Radioactive decay is the spontaneous and random process by which an unstable atomic nucleus loses energy by emitting radiation. This topic forms the cornerstone of nuclear physics, explaining how and why certain isotopes transform into other elements over time. The study of radioactive decay is fundamental to understanding [[Atomic Structure and the Nucleus]], as it reveals the internal dynamics of the nucleus and the forces that govern its stability.

In the Cambridge 9702 and Edexcel IAL A-Level Physics syllabuses, this topic is assessed through both theoretical understanding and practical applications. Students must grasp the probabilistic nature of decay, the types of radiation emitted ([[Alpha, Beta and Gamma Radiation]]), and the mathematical laws governing decay rates. Real-world applications include carbon dating in archaeology, medical imaging (PET scans), nuclear power generation, and radiation therapy for cancer treatment. The concept of [[Half-Life and Activity]] is directly derived from the exponential decay law, making this topic essential for understanding nuclear safety, radioactive waste management, and environmental monitoring.

**中文：**
放射性衰变是不稳定原子核通过发射辐射自发且随机地失去能量的过程。本课题是核物理的基石，解释了某些同位素如何以及为何随时间转化为其他元素。放射性衰变的研究对于理解[[原子结构与原子核]]至关重要，因为它揭示了原子核的内部动力学以及控制其稳定性的力。

在剑桥 9702 和爱德思 IAL A-Level 物理考纲中，本课题通过理论理解和实际应用进行评估。学生必须掌握衰变的概率性质、发射的辐射类型（[[α、β 和 γ 辐射]]）以及控制衰变速率的数学定律。实际应用包括考古学中的碳定年法、医学成像（PET 扫描）、核能发电和癌症放射治疗。[[半衰期与活度]]的概念直接源自指数衰变定律，使得本课题对于理解核安全、放射性废物管理和环境监测至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 23.1(a) Describe the spontaneous and random nature of radioactive decay | 8.1 Understand that radioactive decay is a spontaneous and random process |
| 23.1(b) Define activity and decay constant | 8.2 Use the equation $A = \lambda N$ |
| 23.1(c) Use the equation $A = \lambda N$ | 8.3 Derive and use $N = N_0 e^{-\lambda t}$ |
| 23.1(d) Use the equation $N = N_0 e^{-\lambda t}$ | 8.4 Define and use half-life |
| 23.1(e) Define half-life | 8.5 Understand the relationship between half-life and decay constant |
| 23.1(f) Use the equation $\lambda = \frac{\ln 2}{t_{1/2}}$ | 8.6 Solve problems involving exponential decay |
| 23.1(g) Solve problems using exponential decay equations | — |

**Examiner Expectations / 考官期望：**

**English:**
- Students must distinguish between *spontaneous* (not triggered by external factors) and *random* (unpredictable individual decay events).
- The decay constant $\lambda$ must be understood as a probability per unit time, not a rate.
- Graphical analysis of decay curves is frequently tested, including logarithmic plots to determine $\lambda$.
- Students should be able to derive the exponential decay law from first principles using calculus (Edexcel) or by reasoning (CAIE).
- Half-life problems often involve multiple half-lives, requiring careful handling of fractions.

**中文：**
- 学生必须区分*自发*（不受外部因素触发）和*随机*（单个衰变事件不可预测）。
- 衰变常数 $\lambda$ 必须理解为每单位时间的概率，而不是速率。
- 衰变曲线的图形分析经常被测试，包括用于确定 $\lambda$ 的对数图。
- 学生应能够从基本原理推导指数衰变定律（爱德思使用微积分，剑桥使用推理）。
- 半衰期问题通常涉及多个半衰期，需要仔细处理分数。

> 📋 **CIE Only:** CAIE requires students to describe the random nature of decay using the concept of *probability* and to sketch decay curves. The derivation of $N = N_0 e^{-\lambda t}$ is not required via calculus but through logical reasoning.
>
> 📋 **Edexcel Only:** Edexcel explicitly requires the derivation of $N = N_0 e^{-\lambda t}$ from $\frac{dN}{dt} = -\lambda N$ using integration. Students must also handle problems involving background radiation correction.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Radioactive Decay** / 放射性衰变 | The spontaneous and random process by which an unstable nucleus emits radiation to become more stable. | 不稳定原子核自发且随机地发射辐射以变得更稳定的过程。 | Confusing *spontaneous* with *random*; they are distinct properties. |
| **Activity ($A$)** / 活度 | The number of radioactive decays per unit time in a sample. | 样品中单位时间内发生的放射性衰变次数。 | Forgetting that activity decreases over time; it is not constant. |
| **Decay Constant ($\lambda$)** / 衰变常数 | The probability per unit time that a given nucleus will decay. | 给定原子核在单位时间内发生衰变的概率。 | Treating $\lambda$ as a rate (decays per second) rather than a probability. |
| **Half-Life ($t_{1/2}$)** / 半衰期 | The time taken for half the nuclei in a sample to decay, or for the activity to halve. | 样品中一半原子核发生衰变或活度减半所需的时间。 | Assuming half-life is the time for *all* nuclei to decay; it is not. |
| **Exponential Decay** / 指数衰变 | A process where the rate of decay is proportional to the number of undecayed nuclei present. | 衰变速率与未衰变原子核数量成正比的过程。 | Thinking the graph is linear; it is a decreasing exponential. |
| **Spontaneous** / 自发 | Not influenced by external factors such as temperature, pressure, or chemical state. | 不受温度、压力或化学状态等外部因素影响。 | Believing decay can be accelerated by heating or pressure. |
| **Random** / 随机 | Impossible to predict which nucleus will decay next; each nucleus has an equal probability of decaying. | 无法预测哪个原子核会衰变；每个原子核有相等的衰变概率。 | Thinking randomness means no pattern; the *average* behaviour follows a precise law. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Spontaneous and Random Nature / 自发性和随机性

### Explanation / 解释
**English:**
Radioactive decay is **spontaneous**, meaning it is not triggered by any external influence like temperature, pressure, or chemical reactions. It is also **random**, meaning it is impossible to predict exactly when a particular nucleus will decay. However, for a large number of nuclei, the *average* behaviour follows a precise mathematical law — the [[Exponential Decay Law]]. This duality (random individual events but predictable bulk behaviour) is a key feature of quantum mechanics and statistical physics.

**中文：**
放射性衰变是**自发**的，意味着它不受温度、压力或化学反应等任何外部影响触发。它也是**随机**的，意味着无法精确预测某个特定原子核何时会衰变。然而，对于大量原子核，*平均*行为遵循精确的数学定律——[[指数衰变定律]]。这种二元性（随机个体事件但可预测整体行为）是量子力学和统计物理学的关键特征。

### Physical Meaning / 物理意义
**English:**
Imagine a room full of people each holding a ticking bomb with a random timer. You cannot know which person's bomb will explode next, but you can predict how many explosions will occur in the next minute. Similarly, for a radioactive sample, you cannot say which nucleus will decay next, but you can calculate the activity (decays per second) with high precision.

**中文：**
想象一个房间里挤满了人，每人手持一个带有随机计时器的炸弹。你无法知道谁的炸弹会下一个爆炸，但你可以预测下一分钟会发生多少次爆炸。类似地，对于放射性样品，你无法说哪个原子核会下一个衰变，但你可以高精度地计算活度（每秒衰变次数）。

### Common Misconceptions / 常见误区
1. **"Decay can be accelerated by heating"** — False. Radioactive decay is spontaneous and unaffected by external conditions.
2. **"Random means no pattern exists"** — False. Random individual events produce predictable statistical patterns for large numbers.
3. **"Half-life is the time for all nuclei to decay"** — False. After one half-life, half remain; after two, a quarter remain; it never reaches zero.

### Exam Tips / 考试提示
**English:**
- CAIE often asks: "Explain what is meant by *random* and *spontaneous* in the context of radioactive decay." Use precise wording.
- Edexcel may ask: "State two pieces of evidence that radioactive decay is random." (e.g., constant activity fluctuations, unpredictable individual decay times).
- Use the phrase "constant probability per unit time" to describe $\lambda$.

**中文：**
- 剑桥常问："在放射性衰变背景下解释*随机*和*自发*的含义。"使用精确措辞。
- 爱德思可能问："陈述放射性衰变是随机的两个证据。"（例如，活度恒定波动，单个衰变时间不可预测）。
- 使用短语"每单位时间的恒定概率"来描述 $\lambda$。

---

## 4.2 Activity and Decay Constant / 活度和衰变常数

### Explanation / 解释
**English:**
**Activity ($A$)** is the number of decays per second, measured in becquerels (Bq), where 1 Bq = 1 decay per second. The **decay constant ($\lambda$)** is the probability per second that a given nucleus will decay. The relationship is:

$$A = \lambda N$$

where $N$ is the number of undecayed nuclei. This equation shows that activity is proportional to the number of undecayed nuclei. As nuclei decay, $N$ decreases, so $A$ also decreases — this is why activity is not constant.

**中文：**
**活度 ($A$)** 是每秒衰变次数，以贝克勒尔 (Bq) 为单位，其中 1 Bq = 1 次衰变/秒。**衰变常数 ($\lambda$)** 是给定原子核每秒衰变的概率。关系为：

$$A = \lambda N$$

其中 $N$ 是未衰变原子核的数量。该方程表明活度与未衰变原子核数量成正比。随着原子核衰变，$N$ 减少，因此 $A$ 也减少——这就是活度不恒定的原因。

### Physical Meaning / 物理意义
**English:**
If $\lambda = 0.01 \, \text{s}^{-1}$, each nucleus has a 1% chance of decaying in the next second. For 1000 nuclei, the expected activity is $0.01 \times 1000 = 10$ decays per second. As nuclei decay, fewer remain, so the activity drops.

**中文：**
如果 $\lambda = 0.01 \, \text{s}^{-1}$，每个原子核在下一秒有 1% 的衰变概率。对于 1000 个原子核，预期活度为 $0.01 \times 1000 = 10$ 次衰变/秒。随着原子核衰变，剩余数量减少，因此活度下降。

### Common Misconceptions / 常见误区
1. **"Activity is constant"** — False. Activity decreases exponentially over time.
2. **"$\lambda$ is the same as decay rate"** — $\lambda$ is a *probability*, not a rate. The rate is $A = \lambda N$.
3. **"$\lambda$ depends on sample size"** — False. $\lambda$ is a property of the isotope, independent of sample size.

### Exam Tips / 考试提示
**English:**
- Always state units: $A$ in Bq, $\lambda$ in s$^{-1}$, $N$ is dimensionless.
- Edexcel may ask: "Show that the decay constant has units of s$^{-1}$."
- CAIE may ask: "Calculate the number of nuclei from activity and decay constant."

**中文：**
- 始终说明单位：$A$ 以 Bq 为单位，$\lambda$ 以 s$^{-1}$ 为单位，$N$ 无量纲。
- 爱德思可能问："证明衰变常数的单位为 s$^{-1}$。"
- 剑桥可能问："从活度和衰变常数计算原子核数量。"

---

## 4.3 The Exponential Decay Law / 指数衰变定律

### Explanation / 解释
**English:**
The exponential decay law describes how the number of undecayed nuclei changes with time:

$$N = N_0 e^{-\lambda t}$$

where $N_0$ is the initial number of nuclei, $\lambda$ is the decay constant, and $t$ is time. This equation arises from the differential equation:

$$\frac{dN}{dt} = -\lambda N$$

which states that the rate of decay is proportional to the number of undecayed nuclei. The solution is obtained by separation of variables and integration:

$$\int_{N_0}^{N} \frac{dN}{N} = -\lambda \int_0^t dt$$

$$\ln\left(\frac{N}{N_0}\right) = -\lambda t$$

$$N = N_0 e^{-\lambda t}$$

**中文：**
指数衰变定律描述了未衰变原子核数量随时间的变化：

$$N = N_0 e^{-\lambda t}$$

其中 $N_0$ 是初始原子核数量，$\lambda$ 是衰变常数，$t$ 是时间。该方程源自微分方程：

$$\frac{dN}{dt} = -\lambda N$$

该方程表明衰变速率与未衰变原子核数量成正比。通过分离变量和积分得到解：

$$\int_{N_0}^{N} \frac{dN}{N} = -\lambda \int_0^t dt$$

$$\ln\left(\frac{N}{N_0}\right) = -\lambda t$$

$$N = N_0 e^{-\lambda t}$$

### Physical Meaning / 物理意义
**English:**
The exponential decay law means that the fraction of nuclei remaining after each equal time interval is constant. For example, if 50% remain after 1 hour, then after 2 hours 25% remain, after 3 hours 12.5%, and so on. This constant fraction property is the defining feature of exponential decay.

**中文：**
指数衰变定律意味着每个相等时间间隔后剩余的原子核比例是恒定的。例如，如果 1 小时后剩余 50%，那么 2 小时后剩余 25%，3 小时后剩余 12.5%，依此类推。这种恒定比例性质是指数衰变的定义特征。

### Common Misconceptions / 常见误区
1. **"The graph of $N$ vs $t$ is a straight line"** — False. It is a decreasing exponential curve.
2. **"$N$ becomes zero after a finite time"** — False. Exponential decay approaches zero asymptotically.
3. **"The decay constant is the same as the half-life"** — False. They are inversely related: $\lambda = \ln 2 / t_{1/2}$.

### Exam Tips / 考试提示
**English:**
- CAIE: You may be asked to sketch the decay curve and label $N_0$ and $t_{1/2}$.
- Edexcel: Derivation from $\frac{dN}{dt} = -\lambda N$ is required.
- Both boards: Use logarithmic plots ($\ln N$ vs $t$) to determine $\lambda$ from the gradient.
- Remember: $\ln N = \ln N_0 - \lambda t$, so gradient $= -\lambda$.

**中文：**
- 剑桥：可能要求绘制衰变曲线并标注 $N_0$ 和 $t_{1/2}$。
- 爱德思：需要从 $\frac{dN}{dt} = -\lambda N$ 推导。
- 两个考试局：使用对数图（$\ln N$ 对 $t$）从斜率确定 $\lambda$。
- 记住：$\ln N = \ln N_0 - \lambda t$，因此斜率 $= -\lambda$。

---

## 4.4 Half-Life / 半衰期

### Explanation / 解释
**English:**
**Half-life ($t_{1/2}$)** is the time taken for half the nuclei in a sample to decay, or equivalently, for the activity to halve. It is related to the decay constant by:

$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$$

This relationship is derived by setting $N = N_0/2$ in the exponential decay law:

$$\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}}$$

$$\frac{1}{2} = e^{-\lambda t_{1/2}}$$

$$\ln\left(\frac{1}{2}\right) = -\lambda t_{1/2}$$

$$-\ln 2 = -\lambda t_{1/2}$$

$$t_{1/2} = \frac{\ln 2}{\lambda}$$

**中文：**
**半衰期 ($t_{1/2}$)** 是样品中一半原子核衰变所需的时间，或等效地，活度减半所需的时间。它与衰变常数的关系为：

$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$$

该关系通过将 $N = N_0/2$ 代入指数衰变定律推导得出：

$$\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}}$$

$$\frac{1}{2} = e^{-\lambda t_{1/2}}$$

$$\ln\left(\frac{1}{2}\right) = -\lambda t_{1/2}$$

$$-\ln 2 = -\lambda t_{1/2}$$

$$t_{1/2} = \frac{\ln 2}{\lambda}$$

### Physical Meaning / 物理意义
**English:**
Half-life is a characteristic property of each radioactive isotope. It ranges from fractions of a second (e.g., polonium-214: $1.6 \times 10^{-4}$ s) to billions of years (e.g., uranium-238: $4.5 \times 10^9$ years). Short half-lives mean rapid decay and high activity; long half-lives mean slow decay and low activity.

**中文：**
半衰期是每种放射性同位素的特征性质。范围从几分之一秒（例如，钋-214：$1.6 \times 10^{-4}$ 秒）到数十亿年（例如，铀-238：$4.5 \times 10^9$ 年）。短半衰期意味着快速衰变和高活度；长半衰期意味着慢速衰变和低活度。

### Common Misconceptions / 常见误区
1. **"Half-life is the time for all nuclei to decay"** — False. After one half-life, half remain; after two, a quarter; it never reaches zero.
2. **"Half-life changes with temperature"** — False. Half-life is constant for a given isotope.
3. **"Half-life is half the total decay time"** — False. There is no "total decay time" because decay is asymptotic.

### Exam Tips / 考试提示
**English:**
- Both boards: Be able to calculate the fraction remaining after $n$ half-lives: $1/2^n$.
- CAIE: May ask: "A sample has activity 800 Bq. After 12 days, activity is 50 Bq. Find the half-life." (Answer: 3 days, since $800 \to 400 \to 200 \to 100 \to 50$ is 4 half-lives in 12 days.)
- Edexcel: May ask: "Show that the half-life is given by $t_{1/2} = \ln 2 / \lambda$."

**中文：**
- 两个考试局：能够计算 $n$ 个半衰期后的剩余分数：$1/2^n$。
- 剑桥：可能问："样品活度为 800 Bq。12 天后，活度为 50 Bq。求半衰期。"（答案：3 天，因为 $800 \to 400 \to 200 \to 100 \to 50$ 是 12 天内的 4 个半衰期。）
- 爱德思：可能问："证明半衰期由 $t_{1/2} = \ln 2 / \lambda$ 给出。"

---

## 4.5 Types of Radioactive Decay / 放射性衰变类型

### Explanation / 解释
**English:**
There are four main types of radioactive decay: [[Alpha Decay]], [[Beta-minus Decay]], [[Beta-plus Decay]], and [[Gamma Decay]]. Each involves different particles and conservation laws:

- **Alpha ($\alpha$) decay:** Emission of a helium nucleus ($^4_2\text{He}$). Occurs in heavy nuclei (Z > 82). Reduces atomic number by 2, mass number by 4.
- **Beta-minus ($\beta^-$) decay:** Emission of an electron and an antineutrino. A neutron converts to a proton. Increases atomic number by 1, mass number unchanged.
- **Beta-plus ($\beta^+$) decay:** Emission of a positron and a neutrino. A proton converts to a neutron. Decreases atomic number by 1, mass number unchanged.
- **Gamma ($\gamma$) decay:** Emission of high-energy photons. Occurs when a nucleus is in an excited state. No change in atomic or mass number.

**中文：**
放射性衰变有四种主要类型：[[α 衰变]]、[[β⁻ 衰变]]、[[β⁺ 衰变]]和[[γ 衰变]]。每种涉及不同的粒子和守恒定律：

- **α 衰变：** 发射氦原子核 ($^4_2\text{He}$)。发生在重核中 (Z > 82)。原子序数减少 2，质量数减少 4。
- **β⁻ 衰变：** 发射电子和反中微子。中子转化为质子。原子序数增加 1，质量数不变。
- **β⁺ 衰变：** 发射正电子和中微子。质子转化为中子。原子序数减少 1，质量数不变。
- **γ 衰变：** 发射高能光子。发生在原子核处于激发态时。原子序数和质量数不变。

### Physical Meaning / 物理意义
**English:**
Each decay type is nature's way of moving a nucleus toward greater stability. Heavy nuclei shed mass via alpha decay. Neutron-rich nuclei convert neutrons to protons via beta-minus decay. Proton-rich nuclei convert protons to neutrons via beta-plus decay. Excited nuclei release energy via gamma decay.

**中文：**
每种衰变类型是自然界使原子核趋向更稳定的方式。重核通过 α 衰变释放质量。中子过多的原子核通过 β⁻ 衰变将中子转化为质子。质子过多的原子核通过 β⁺ 衰变将质子转化为中子。激发态原子核通过 γ 衰变释放能量。

### Common Misconceptions / 常见误区
1. **"Gamma rays are particles"** — False. Gamma rays are electromagnetic radiation (photons).
2. **"Beta particles are electrons from the electron cloud"** — False. Beta particles are emitted from the nucleus.
3. **"Alpha decay changes mass number by 2"** — Correct, but students often forget the atomic number change.

### Exam Tips / 考试提示
**English:**
- Both boards: Be able to write balanced decay equations using [[Decay Equations and Conservation]].
- CAIE: May ask: "Identify the type of decay from a given equation."
- Edexcel: May ask: "Explain the role of [[Neutrinos and Antineutrinos]] in beta decay."

**中文：**
- 两个考试局：能够使用[[衰变方程与守恒]]写出平衡的衰变方程。
- 剑桥：可能问："从给定方程识别衰变类型。"
- 爱德思：可能问："解释[[中微子和反中微子]]在 β 衰变中的作用。"

---

> 📷 **IMAGE PROMPT — [RC-01]: Types of Radioactive Decay Diagram**
>
> A clean, educational diagram showing four panels side by side. Panel 1: Alpha decay — a large nucleus (e.g., U-238) emitting a helium nucleus (2 protons, 2 neutrons) and becoming Th-234. Panel 2: Beta-minus decay — a nucleus with a neutron converting to a proton, emitting an electron (β⁻) and an antineutrino (ν̄ₑ). Panel 3: Beta-plus decay — a nucleus with a proton converting to a neutron, emitting a positron (β⁺) and a neutrino (νₑ). Panel 4: Gamma decay — an excited nucleus (with asterisk) emitting a photon (γ) and returning to ground state. Each panel has clear labels in English and Chinese. Style: textbook-quality, flat vector illustration, white background, blue and red color scheme for protons and neutrons. Labels: parent nucleus, daughter nucleus, emitted particle, symbol.

---

# 5. Essential Equations / 核心公式

## 5.1 Activity Equation / 活度方程

**Equation / 公式:**
$$A = \lambda N$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $A$ | Activity | 活度 | Bq (becquerel) |
| $\lambda$ | Decay constant | 衰变常数 | s$^{-1}$ |
| $N$ | Number of undecayed nuclei | 未衰变原子核数量 | dimensionless |

**Derivation / 推导:**
**English:**
The decay constant $\lambda$ is defined as the probability per unit time of decay. For $N$ nuclei, the expected number of decays per unit time is $\lambda N$, which is the activity $A$.

**中文：**
衰变常数 $\lambda$ 定义为每单位时间的衰变概率。对于 $N$ 个原子核，每单位时间的预期衰变次数为 $\lambda N$，即活度 $A$。

**Conditions / 适用条件:**
**English:** Valid for any radioactive sample where $\lambda$ is constant and $N$ is large enough for statistical averaging.
**中文：** 适用于任何 $\lambda$ 恒定且 $N$ 足够大以进行统计平均的放射性样品。

**Limitations / 局限性:**
**English:** Not valid for very small samples (e.g., fewer than 10 nuclei) where statistical fluctuations dominate.
**中文：** 不适用于非常小的样品（例如，少于 10 个原子核），此时统计波动占主导。

**Rearrangements / 变形:**
$$N = \frac{A}{\lambda}, \quad \lambda = \frac{A}{N}$$

---

## 5.2 Exponential Decay Law / 指数衰变定律

**Equation / 公式:**
$$N = N_0 e^{-\lambda t}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $N$ | Number of undecayed nuclei at time $t$ | 时间 $t$ 时未衰变原子核数量 | dimensionless |
| $N_0$ | Initial number of undecayed nuclei | 初始未衰变原子核数量 | dimensionless |
| $\lambda$ | Decay constant | 衰变常数 | s$^{-1}$ |
| $t$ | Time elapsed | 经过的时间 | s |

**Derivation / 推导:**
**English:**
Starting from the differential equation:
$$\frac{dN}{dt} = -\lambda N$$
Separate variables:
$$\frac{dN}{N} = -\lambda \, dt$$
Integrate both sides:
$$\int_{N_0}^{N} \frac{dN}{N} = -\lambda \int_0^t dt$$
$$\left[\ln N\right]_{N_0}^{N} = -\lambda t$$
$$\ln N - \ln N_0 = -\lambda t$$
$$\ln\left(\frac{N}{N_0}\right) = -\lambda t$$
Exponentiate both sides:
$$\frac{N}{N_0} = e^{-\lambda t}$$
$$N = N_0 e^{-\lambda t}$$

**中文：**
从微分方程开始：
$$\frac{dN}{dt} = -\lambda N$$
分离变量：
$$\frac{dN}{N} = -\lambda \, dt$$
两边积分：
$$\int_{N_0}^{N} \frac{dN}{N} = -\lambda \int_0^t dt$$
$$\left[\ln N\right]_{N_0}^{N} = -\lambda t$$
$$\ln N - \ln N_0 = -\lambda t$$
$$\ln\left(\frac{N}{N_0}\right) = -\lambda t$$
两边取指数：
$$\frac{N}{N_0} = e^{-\lambda t}$$
$$N = N_0 e^{-\lambda t}$$

**Conditions / 适用条件:**
**English:** Valid for any radioactive decay process where $\lambda$ is constant and the decay is a first-order process.
**中文：** 适用于任何 $\lambda$ 恒定且衰变是一级过程的放射性衰变过程。

**Limitations / 局限性:**
**English:** Does not apply to chain decays (where daughter products are also radioactive) without modification.
**中文：** 不适用于链式衰变（子产物也具有放射性）而不加修改。

**Rearrangements / 变形:**
$$\lambda = -\frac{1}{t} \ln\left(\frac{N}{N_0}\right), \quad t = -\frac{1}{\lambda} \ln\left(\frac{N}{N_0}\right)$$

---

## 5.3 Activity Exponential Decay / 活度指数衰变

**Equation / 公式:**
$$A = A_0 e^{-\lambda t}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $A$ | Activity at time $t$ | 时间 $t$ 时的活度 | Bq |
| $A_0$ | Initial activity | 初始活度 | Bq |
| $\lambda$ | Decay constant | 衰变常数 | s$^{-1}$ |
| $t$ | Time elapsed | 经过的时间 | s |

**Derivation / 推导:**
**English:**
Since $A = \lambda N$ and $N = N_0 e^{-\lambda t}$, substituting gives:
$$A = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$$
where $A_0 = \lambda N_0$.

**中文：**
由于 $A = \lambda N$ 且 $N = N_0 e^{-\lambda t}$，代入得：
$$A = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$$
其中 $A_0 = \lambda N_0$。

**Conditions / 适用条件:**
**English:** Same as for $N = N_0 e^{-\lambda t}$.
**中文：** 与 $N = N_0 e^{-\lambda t}$ 相同。

**Limitations / 局限性:**
**English:** Same as for $N = N_0 e^{-\lambda t}$.
**中文：** 与 $N = N_0 e^{-\lambda t}$ 相同。

**Rearrangements / 变形:**
$$\lambda = -\frac{1}{t} \ln\left(\frac{A}{A_0}\right), \quad t = -\frac{1}{\lambda} \ln\left(\frac{A}{A_0}\right)$$

---

## 5.4 Half-Life and Decay Constant / 半衰期与衰变常数

**Equation / 公式:**
$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $t_{1/2}$ | Half-life | 半衰期 | s (or any time unit) |
| $\lambda$ | Decay constant | 衰变常数 | s$^{-1}$ |

**Derivation / 推导:**
**English:**
Set $N = N_0/2$ and $t = t_{1/2}$ in $N = N_0 e^{-\lambda t}$:
$$\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}}$$
$$\frac{1}{2} = e^{-\lambda t_{1/2}}$$
$$\ln\left(\frac{1}{2}\right) = -\lambda t_{1/2}$$
$$-\ln 2 = -\lambda t_{1/2}$$
$$t_{1/2} = \frac{\ln 2}{\lambda}$$

**中文：**
在 $N = N_0 e^{-\lambda t}$ 中设 $N = N_0/2$ 和 $t = t_{1/2}$：
$$\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}}$$
$$\frac{1}{2} = e^{-\lambda t_{1/2}}$$
$$\ln\left(\frac{1}{2}\right) = -\lambda t_{1/2}$$
$$-\ln 2 = -\lambda t_{1/2}$$
$$t_{1/2} = \frac{\ln 2}{\lambda}$$

**Conditions / 适用条件:**
**English:** Valid for any exponential decay process.
**中文：** 适用于任何指数衰变过程。

**Limitations / 局限性:**
**English:** Only applies to single-step decay; not for complex decay chains.
**中文：** 仅适用于单步衰变；不适用于复杂衰变链。

**Rearrangements / 变形:**
$$\lambda = \frac{\ln 2}{t_{1/2}}$$

---

## 5.5 Fraction Remaining After n Half-Lives / n 个半衰期后的剩余分数

**Equation / 公式:**
$$\frac{N}{N_0} = \left(\frac{1}{2}\right)^n = 2^{-n}$$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $N/N_0$ | Fraction remaining | 剩余分数 | dimensionless |
| $n$ | Number of half-lives elapsed ($n = t/t_{1/2}$) | 经过的半衰期数量 | dimensionless |

**Derivation / 推导:**
**English:**
After one half-life: $N = N_0/2$
After two half-lives: $N = N_0/4 = N_0/2^2$
After three half-lives: $N = N_0/8 = N_0/2^3$
After $n$ half-lives: $N = N_0/2^n$

**中文：**
一个半衰期后：$N = N_0/2$
两个半衰期后：$N = N_0/4 = N_0/2^2$
三个半衰期后：$N = N_0/8 = N_0/2^3$
$n$ 个半衰期后：$N = N_0/2^n$

**Conditions / 适用条件:**
**English:** Only valid when $n$ is an integer. For non-integer $n$, use $N = N_0 e^{-\lambda t}$.
**中文：** 仅当 $n$ 为整数时有效。对于非整数 $n$，使用 $N = N_0 e^{-\lambda t}$。

**Limitations / 局限性:**
**English:** Approximate for non-integer half-lives.
**中文：** 对于非整数半衰期为近似值。

**Rearrangements / 变形:**
$$n = \frac{\ln(N_0/N)}{\ln 2}, \quad t = n t_{1/2}$$

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Number of Undecayed Nuclei vs Time / 未衰变原子核数量与时间的关系

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: Number of undecayed nuclei ($N$)
**中文：** x 轴：时间 ($t$)，y 轴：未衰变原子核数量 ($N$)

### Shape / 形状
**English:** A decreasing exponential curve. Starts at $N_0$ on the y-axis, decreases rapidly initially, then more slowly, approaching zero asymptotically.
**中文：** 递减指数曲线。从 y 轴上的 $N_0$ 开始，初始快速下降，然后变慢，渐近趋近于零。

### Gradient Meaning / 斜率含义
**English:** The gradient $\frac{dN}{dt}$ represents the rate of decay (negative). Its magnitude is the activity $A = \lambda N$. The gradient becomes less steep over time as $N$ decreases.
**中文：** 斜率 $\frac{dN}{dt}$ 表示衰变速率（负值）。其大小是活度 $A = \lambda N$。随着 $N$ 减少，斜率随时间变缓。

### Area Meaning / 面积含义
**English:** The area under the $N$ vs $t$ curve has no direct physical meaning in this context.
**中文：** $N$ 对 $t$ 曲线下的面积在此背景下没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:**
- Identify $N_0$ as the y-intercept.
- Determine $t_{1/2}$ by finding the time for $N$ to halve.
- Compare half-lives of different isotopes: steeper curve = shorter half-life.
- Sketch curves for different $\lambda$ values.

**中文：**
- 将 $N_0$ 识别为 y 截距。
- 通过找到 $N$ 减半的时间来确定 $t_{1/2}$。
- 比较不同同位素的半衰期：曲线越陡 = 半衰期越短。
- 绘制不同 $\lambda$ 值的曲线。

### Common Questions / 常见问题
**English:**
- "Use the graph to determine the half-life."
- "Sketch the decay curve for an isotope with a longer half-life."
- "Explain why the gradient decreases over time."

**中文：**
- "使用图表确定半衰期。"
- "绘制半衰期更长的同位素的衰变曲线。"
- "解释为什么斜率随时间减小。"

---

## 6.2 Natural Logarithm of N vs Time / N 的自然对数与时间的关系

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: $\ln N$
**中文：** x 轴：时间 ($t$)，y 轴：$\ln N$

### Shape / 形状
**English:** A straight line with negative slope. The linearization comes from:
$$\ln N = \ln N_0 - \lambda t$$
**中文：** 一条具有负斜率的直线。线性化来自：
$$\ln N = \ln N_0 - \lambda t$$

### Gradient Meaning / 斜率含义
**English:** The gradient is $-\lambda$ (negative of the decay constant). A steeper negative slope means a larger $\lambda$ and shorter half-life.
**中文：** 斜率为 $-\lambda$（衰变常数的负值）。负斜率越陡意味着 $\lambda$ 越大，半衰期越短。

### Area Meaning / 面积含义
**English:** No direct physical meaning.
**中文：** 没有直接的物理意义。

### Exam Interpretation / 考试解读
**English:**
- Determine $\lambda$ from the gradient: $\lambda = - \text{gradient}$.
- Determine $N_0$ from the y-intercept: $\ln N_0$ is the intercept.
- Check if data follows exponential decay: points should lie on a straight line.
- Calculate half-life from $\lambda$: $t_{1/2} = \ln 2 / \lambda$.

**中文：**
- 从斜率确定 $\lambda$：$\lambda = - \text{斜率}$。
- 从 y 截距确定 $N_0$：$\ln N_0$ 是截距。
- 检查数据是否遵循指数衰变：点应位于直线上。
- 从 $\lambda$ 计算半衰期：$t_{1/2} = \ln 2 / \lambda$。

### Common Questions / 常见问题
**English:**
- "Plot $\ln N$ against $t$ and determine the decay constant."
- "Explain why a straight line on a $\ln N$ vs $t$ graph confirms exponential decay."
- "Calculate the half-life from the gradient."

**中文：**
- "绘制 $\ln N$ 对 $t$ 的图并确定衰变常数。"
- "解释为什么 $\ln N$ 对 $t$ 图上的直线确认了指数衰变。"
- "从斜率计算半衰期。"

---

## 6.3 Activity vs Time / 活度与时间的关系

### Axes / 坐标轴
**English:** x-axis: Time ($t$), y-axis: Activity ($A$)
**中文：** x 轴：时间 ($t$)，y 轴：活度 ($A$)

### Shape / 形状
**English:** Identical shape to $N$ vs $t$ — a decreasing exponential curve starting at $A_0$.
**中文：** 与 $N$ 对 $t$ 形状相同——从 $A_0$ 开始的递减指数曲线。

### Gradient Meaning / 斜率含义
**English:** The gradient $\frac{dA}{dt}$ represents the rate of change of activity. It is negative and becomes less steep over time.
**中文：** 斜率 $\frac{dA}{dt}$ 表示活度的变化率。它是负的，并随时间变缓。

### Area Meaning / 面积含义
**English:** The area under the $A$ vs $t$ curve represents the total number of decays that have occurred up to time $t$:
$$\text{Total decays} = \int_0^t A \, dt = N_0 - N$$
**中文：** $A$ 对 $t$ 曲线下的面积表示到时间 $t$ 为止发生的总衰变次数：
$$\text{总衰变次数} = \int_0^t A \, dt = N_0 - N$$

### Exam Interpretation / 考试解读
**English:**
- Use to find total decays over a time interval.
- Correct for background radiation when measuring activity.
- Determine half-life from activity measurements.

**中文：**
- 用于找到时间间隔内的总衰变次数。
- 测量活度时校正本底辐射。
- 从活度测量确定半衰期。

### Common Questions / 常见问题
**English:**
- "Estimate the total number of decays in the first 10 seconds from the graph."
- "Explain how background radiation affects activity measurements."

**中文：**
- "从图表估计前 10 秒内的总衰变次数。"
- "解释本底辐射如何影响活度测量。"

---

> 📷 **IMAGE PROMPT — [RC-02]: Decay Curves Comparison**
>
> A graph with two curves on the same axes. x-axis: Time (0 to 10 units), y-axis: Number of nuclei (0 to 1000). Curve A: steep exponential decay with half-life of 1 unit (reaches 500 at t=1, 250 at t=2, etc.). Curve B: shallower exponential decay with half-life of 3 units (reaches 500 at t=3, 250 at t=6, etc.). Both curves start at N₀=1000. Labels: N₀, t₁/₂(A), t₁/₂(B). Below, a second graph showing ln N vs t for both curves as straight lines with different slopes. Style: clean scientific graph, grid lines, clear axis labels in English and Chinese, color-coded (red for A, blue for B).

---

# 7. Required Diagrams / 必备图表

## 7.1 Exponential Decay Curve / 指数衰变曲线

### Description / 描述
**English:**
A graph showing the number of undecayed nuclei ($N$) on the y-axis against time ($t$) on the x-axis. The curve starts at $N_0$ and decreases exponentially, approaching zero asymptotically. Key features marked: $N_0$ (initial number), $t_{1/2}$ (half-life), and the points where $N = N_0/2$, $N = N_0/4$, $N = N_0/8$.

**中文：**
显示未衰变原子核数量 ($N$) 在 y 轴上对时间 ($t$) 在 x 轴上的图表。曲线从 $N_0$ 开始并指数下降，渐近趋近于零。标记的关键特征：$N_0$（初始数量）、$t_{1/2}$（半衰期）以及 $N = N_0/2$、$N = N_0/4$、$N = N_0/8$ 的点。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [RC-03]: Exponential Decay Curve**
>
> A textbook-quality graph with x-axis labeled "Time / s" and y-axis labeled "Number of undecayed nuclei / N". The curve is a smooth decreasing exponential starting at N₀=1000 on the y-axis. Mark points: (t=0, N=1000) labeled N₀, (t=t₁/₂, N=500) with dashed lines to axes, (t=2t₁/₂, N=250), (t=3t₁/₂, N=125). The curve approaches but never reaches N=0. Style: clean vector illustration, white background, blue curve, black axes with grid lines, labels in English and Chinese. Include a small inset showing the same data on a log-linear scale (ln N vs t) as a straight line.

### Labels Required / 需要标注
| English | 中文 |
|---------|------|
| $N_0$ — Initial number of nuclei | $N_0$ — 初始原子核数量 |
| $t_{1/2}$ — Half-life | $t_{1/2}$ — 半衰期 |
| $N = N_0/2$ | $N = N_0/2$ |
| $N = N_0/4$ | $N = N_0/4$ |
| Time axis | 时间轴 |
| Number axis | 数量轴 |

### Exam Importance / 考试重要性
**English:**
This is the most fundamental diagram in radioactive decay. Both CAIE and Edexcel require students to sketch, interpret, and extract information from this curve. It is used to determine half-life, compare decay rates, and understand the exponential nature of decay.

**中文：**
这是放射性衰变中最基本的图表。剑桥和爱德思都要求学生绘制、解释并从该曲线中提取信息。它用于确定半衰期、比较衰变速率以及理解衰变的指数性质。

---

## 7.2 Log-Linear Plot (ln N vs t) / 对数线性图 (ln N 对 t)

### Description / 描述
**English:**
A graph with $\ln N$ on the y-axis and time $t$ on the x-axis. The data points form a straight line with negative slope. The y-intercept is $\ln N_0$, and the gradient is $-\lambda$. This plot is used to verify exponential decay and determine the decay constant.

**中文：**
$\ln N$ 在 y 轴上、时间 $t$ 在 x 轴上的图表。数据点形成一条具有负斜率的直线。y 截距为 $\ln N_0$，斜率为 $-\lambda$。该图用于验证指数衰变并确定衰变常数。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [RC-04]: Log-Linear Plot for Radioactive Decay**
>
> A graph with x-axis labeled "Time / s" and y-axis labeled "ln(N)". A straight line with negative slope passes through data points with small error bars. The y-intercept is marked as ln(N₀) ≈ 6.91 (corresponding to N₀=1000). The gradient is calculated as -0.693 s⁻¹, corresponding to λ = 0.693 s⁻¹ and t₁/₂ = 1.0 s. Style: scientific journal quality, grid lines, clear axis labels in English and Chinese, points with error bars, line of best fit, equation of line displayed: ln(N) = 6.91 - 0.693t.

### Labels Required / 需要标注
| English | 中文 |
|---------|------|
| $\ln N_0$ — y-intercept | $\ln N_0$ — y 截距 |
| Gradient $= -\lambda$ | 斜率 $= -\lambda$ |
| $\lambda$ — Decay constant | $\lambda$ — 衰变常数 |
| $t_{1/2} = \ln 2 / \lambda$ | $t_{1/2} = \ln 2 / \lambda$ |

### Exam Importance / 考试重要性
**English:**
Edexcel explicitly requires the use of log-linear plots to determine $\lambda$. CAIE also tests this method. This diagram is essential for practical work (Paper 5 for CAIE, Unit 6 for Edexcel) where students plot experimental data to find half-life.

**中文：**
爱德思明确要求使用对数线性图来确定 $\lambda$。剑桥也测试这种方法。该图对于实验工作（剑桥 Paper 5，爱德思 Unit 6）至关重要，学生在此绘制实验数据以找到半衰期。

---

## 7.3 Decay Chain Diagram / 衰变链图

### Description / 描述
**English:**
A diagram showing a sequence of radioactive decays, where a parent nucleus decays into a daughter, which may itself be radioactive and decay further. The diagram shows each step with the type of decay, half-life, and emitted particles. A common example is the uranium-238 decay series ending in lead-206.

**中文：**
显示一系列放射性衰变的图表，其中母核衰变为子核，子核本身可能具有放射性并进一步衰变。图表显示每一步的衰变类型、半衰期和发射粒子。一个常见例子是铀-238 衰变系列，最终变为铅-206。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [RC-05]: Uranium-238 Decay Chain**
>
> A vertical flowchart showing the decay chain from U-238 to Pb-206. Each node is a nucleus with its symbol, atomic number, mass number, and half-life. Arrows between nodes are labeled with decay type (α or β⁻) and emitted particles. Key steps: U-238 (α, 4.5×10⁹ yr) → Th-234 (β⁻, 24 days) → Pa-234 (β⁻, 1.2 min) → U-234 (α, 2.5×10⁵ yr) → Th-230 (α, 7.5×10⁴ yr) → Ra-226 (α, 1600 yr) → Rn-222 (α, 3.8 days) → Po-218 (α, 3.1 min) → Pb-214 (β⁻, 27 min) → Bi-214 (β⁻, 20 min) → Po-214 (α, 1.6×10⁻⁴ s) → Pb-210 (β⁻, 22 yr) → Bi-210 (β⁻, 5 days) → Po-210 (α, 138 days) → Pb-206 (stable). Style: clean flowchart, color-coded by decay type (red for α, blue for β⁻), white background, clear labels in English and Chinese.

### Labels Required / 需要标注
| English | 中文 |
|---------|------|
| Parent nucleus | 母核 |
| Daughter nucleus | 子核 |
| Decay type (α, β⁻, β⁺, γ) | 衰变类型 (α, β⁻, β⁺, γ) |
| Half-life | 半衰期 |
| Stable end product | 稳定终产物 |

### Exam Importance / 考试重要性
**English:**
Both boards test understanding of decay chains, especially in the context of [[Decay Equations and Conservation]]. CAIE may ask students to complete a decay chain given partial information. Edexcel may ask about secular equilibrium in decay chains.

**中文：**
两个考试局都测试对衰变链的理解，特别是在[[衰变方程与守恒]]的背景下。剑桥可能要求学生在给定部分信息的情况下完成衰变链。爱德思可能问及衰变链中的长期平衡。

---

# 8. Worked Examples / 典型例题

## Example 1: Finding Half-Life from Activity Data / 从活度数据求半衰期

### Question / 题目
**English:**
A radioactive sample has an initial activity of 1200 Bq. After 8.0 hours, the activity is measured as 150 Bq. Calculate:
(a) The number of half-lives that have elapsed.
(b) The half-life of the sample.
(c) The decay constant.

**中文：**
一个放射性样品的初始活度为 1200 Bq。8.0 小时后，测得活度为 150 Bq。计算：
(a) 经过的半衰期数量。
(b) 样品的半衰期。
(c) 衰变常数。

### Solution / 解答

**Step 1: Find the number of half-lives (n)**
**English:**
The activity halves every half-life:
$$A = A_0 \left(\frac{1}{2}\right)^n$$
$$150 = 1200 \left(\frac{1}{2}\right)^n$$
$$\frac{150}{1200} = \left(\frac{1}{2}\right)^n$$
$$\frac{1}{8} = \left(\frac{1}{2}\right)^n$$
Since $\frac{1}{8} = \left(\frac{1}{2}\right)^3$, we have $n = 3$.

**中文：**
活度每经过一个半衰期减半：
$$A = A_0 \left(\frac{1}{2}\right)^n$$
$$150 = 1200 \left(\frac{1}{2}\right)^n$$
$$\frac{150}{1200} = \left(\frac{1}{2}\right)^n$$
$$\frac{1}{8} = \left(\frac{1}{2}\right)^n$$
由于 $\frac{1}{8} = \left(\frac{1}{2}\right)^3$，因此 $n = 3$。

**Step 2: Find the half-life**
**English:**
$$n = \frac{t}{t_{1/2}}$$
$$3 = \frac{8.0}{t_{1/2}}$$
$$t_{1/2} = \frac{8.0}{3} = 2.67 \text{ hours}$$

**中文：**
$$n = \frac{t}{t_{1/2}}$$
$$3 = \frac{8.0}{t_{1/2}}$$
$$t_{1/2} = \frac{8.0}{3} = 2.67 \text{ 小时}$$

**Step 3: Find the decay constant**
**English:**
$$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{2.67 \times 3600} = \frac{0.693}{9612} = 7.21 \times 10^{-5} \text{ s}^{-1}$$

**中文：**
$$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{2.67 \times 3600} = \frac{0.693}{9612} = 7.21 \times 10^{-5} \text{ s}^{-1}$$

### Final Answer / 最终答案
**Answer:** (a) 3 half-lives, (b) $t_{1/2} = 2.67$ hours, (c) $\lambda = 7.21 \times 10^{-5} \text{ s}^{-1}$
**答案：** (a) 3 个半衰期，(b) $t_{1/2} = 2.67$ 小时，(c) $\lambda = 7.21 \times 10^{-5} \text{ s}^{-1}$

### Examiner Notes / 考官点评
**English:**
- Common mistake: Forgetting to convert hours to seconds for $\lambda$ in s$^{-1}$.
- Alternative method: Use $A = A_0 e^{-\lambda t}$ directly: $150 = 1200 e^{-\lambda \times 8 \times 3600}$, solve for $\lambda$, then find $t_{1/2}$.
- Marks awarded for: correct equation, substitution, unit conversion, final answer with units.

**中文：**
- 常见错误：忘记将小时转换为秒以得到以 s$^{-1}$ 为单位的 $\lambda$。
- 替代方法：直接使用 $A = A_0 e^{-\lambda t}$：$150 = 1200 e^{-\lambda \times 8 \times 3600}$，解出 $\lambda$，然后求 $t_{1/2}$。
- 得分点：正确方程、代入、单位转换、带单位的最终答案。

---

## Example 2: Carbon Dating Problem / 碳定年问题

### Question / 题目
**English:**
The isotope carbon-14 has a half-life of 5730 years. A sample of ancient wood has an activity of 4.0 decays per minute per gram of carbon. A living tree has an activity of 16.0 decays per minute per gram of carbon. Calculate the age of the ancient wood sample.

**中文：**
碳-14 同位素的半衰期为 5730 年。一块古木样品每克碳的活度为 4.0 次衰变/分钟。一棵活树每克碳的活度为 16.0 次衰变/分钟。计算古木样品的年龄。

### Solution / 解答

**Step 1: Find the decay constant**
**English:**
$$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{5730} = 1.209 \times 10^{-4} \text{ year}^{-1}$$

**中文：**
$$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{5730} = 1.209 \times 10^{-4} \text{ 年}^{-1}$$

**Step 2: Use the exponential decay equation**
**English:**
$$A = A_0 e^{-\lambda t}$$
$$4.0 = 16.0 e^{-1.209 \times 10^{-4} t}$$
$$\frac{4.0}{16.0} = e^{-1.209 \times 10^{-4} t}$$
$$0.25 = e^{-1.209 \times 10^{-4} t}$$

**中文：**
$$A = A_0 e^{-\lambda t}$$
$$4.0 = 16.0 e^{-1.209 \times 10^{-4} t}$$
$$\frac{4.0}{16.0} = e^{-1.209 \times 10^{-4} t}$$
$$0.25 = e^{-1.209 \times 10^{-4} t}$$

**Step 3: Take natural logarithms**
**English:**
$$\ln(0.25) = -1.209 \times 10^{-4} t$$
$$-1.386 = -1.209 \times 10^{-4} t$$
$$t = \frac{1.386}{1.209 \times 10^{-4}} = 1.146 \times 10^4 \text{ years}$$

**中文：**
$$\ln(0.25) = -1.209 \times 10^{-4} t$$
$$-1.386 = -1.209 \times 10^{-4} t$$
$$t = \frac{1.386}{1.209 \times 10^{-4}} = 1.146 \times 10^4 \text{ 年}$$

**Alternative method using half-lives:**
**English:**
$16.0 \to 8.0 \to 4.0$ is 2 half-lives.
$t = 2 \times 5730 = 11460$ years (close to the calculated value).

**中文：**
$16.0 \to 8.0 \to 4.0$ 是 2 个半衰期。
$t = 2 \times 5730 = 11460$ 年（接近计算值）。

### Final Answer / 最终答案
**Answer:** The ancient wood sample is approximately $1.15 \times 10^4$ years old (11500 years).
**答案：** 古木样品大约有 $1.15 \times 10^4$ 年历史（11500 年）。

### Examiner Notes / 考官点评
**English:**
- Common mistake: Using the half-life method without checking if the number of half-lives is exact. Here, 0.25 = (1/2)², so it works.
- Important assumption: The activity of carbon-14 in the atmosphere has remained constant over time.
- Marks awarded for: correct $\lambda$, correct substitution, correct logarithm manipulation, final answer with units.

**中文：**
- 常见错误：未检查半衰期数量是否精确就使用半衰期方法。这里 0.25 = (1/2)²，所以有效。
- 重要假设：大气中碳-14 的活度随时间保持恒定。
- 得分点：正确的 $\lambda$、正确的代入、正确的对数运算、带单位的最终答案。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation of half-life from data / 从数据计算半衰期 | High | Medium | 📝 *待填入* |
| Exponential decay equation manipulation / 指数衰变方程运算 | High | Medium | 📝 *待填入* |
| Graph analysis (N vs t, ln N vs t) / 图表分析 | High | Medium-High | 📝 *待填入* |
| Explanation of random/spontaneous nature / 解释随机/自发性质 | Medium | Low | 📝 *待填入* |
| Derivation of $t_{1/2} = \ln 2 / \lambda$ / 推导半衰期公式 | Medium | Medium | 📝 *待填入* |
| Carbon dating problems / 碳定年问题 | Medium | Medium-High | 📝 *待填入* |
| Decay chain completion / 衰变链完成 | Low-Medium | Medium | 📝 *待填入* |
| Practical: determining half-life from experiment / 实验：从实验确定半衰期 | Medium | High | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

**Common Command Words / 常见指令词：**

| English | 中文 | Typical Usage / 典型用法 |
|---------|------|------------------------|
| State | 陈述 | "State what is meant by *random* in radioactive decay." |
| Define | 定义 | "Define the term *half-life*." |
| Explain | 解释 | "Explain why the activity of a sample decreases over time." |
| Describe | 描述 | "Describe the shape of the decay curve." |
| Calculate | 计算 | "Calculate the decay constant from the half-life." |
| Determine | 确定 | "Determine the age of the sample from the data." |
| Derive | 推导 | "Derive the relationship $t_{1/2} = \ln 2 / \lambda$." |
| Sketch | 绘制 | "Sketch a graph of $N$ against $t$ for a radioactive isotope." |
| Suggest | 建议 | "Suggest why carbon dating is not suitable for samples older than 50000 years." |

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Radioactive decay provides excellent opportunities for practical work in both CAIE and Edexcel specifications.

**CAIE Paper 3 (AS) / Paper 5 (A2):**
- **Paper 3:** Students may measure the activity of a radioactive source using a Geiger-Müller (GM) tube and counter. They must correct for background radiation by measuring background count rate and subtracting it from measured values.
- **Paper 5:** Students design experiments to determine half-life, including:
  - Using a GM tube to measure count rate at regular time intervals.
  - Plotting count rate (corrected for background) against time.
  - Using a log-linear plot ($\ln A$ vs $t$) to determine $\lambda$ and $t_{1/2}$.
  - Estimating uncertainties in count rate (Poisson statistics: uncertainty $\approx \sqrt{\text{count}}$).
  - Evaluating the effect of source distance, shielding, and dead time.

**Edexcel Unit 3 (AS) / Unit 6 (A2):**
- **Unit 3:** Core practical on radioactive decay — measuring half-life of a short-lived isotope (e.g., protactinium-234 or using a simulation).
- **Unit 6:** More advanced practical work including:
  - Investigating the inverse square law for gamma radiation.
  - Determining half-life using a GM tube and data logging.
  - Statistical analysis of radioactive decay data (Poisson distribution).
  - Error analysis and propagation of uncertainties.

**Key Practical Skills / 关键实验技能：**

| Skill / 技能 | Description (EN) | Description (CN) |
|-------------|------------------|------------------|
| Background correction / 本底校正 | Measure background count rate without source, subtract from all readings | 在没有源的情况下测量本底计数率，从所有读数中减去 |
| Count rate vs activity / 计数率与活度 | Understand that count rate is proportional to activity but not equal (due to detector efficiency and geometry) | 理解计数率与活度成正比但不相等（由于探测器效率和几何因素） |
| Statistical uncertainty / 统计不确定度 | For $N$ counts, uncertainty $\approx \sqrt{N}$; use this in error bars | 对于 $N$ 次计数，不确定度 $\approx \sqrt{N}$；在误差棒中使用 |
| Half-life determination / 半衰期确定 | From linear plot of $\ln(\text{count rate})$ vs $t$, gradient $= -\lambda$ | 从 $\ln(\text{计数率})$ 对 $t$ 的线性图，斜率 $= -\lambda$ |
| Safety precautions / 安全预防措施 | Use tongs, minimize exposure time, maximize distance, use shielding | 使用钳子、最小化暴露时间、最大化距离、使用屏蔽 |

> 📋 **CIE Only:** CAIE Paper 5 often includes questions on experimental design for half-life determination, including choice of detector, data collection intervals, and error analysis.
>
> 📋 **Edexcel Only:** Edexcel Unit 6 includes core practicals on radioactive decay where students must demonstrate competence in using GM tubes, data loggers, and statistical analysis.

**中文：**
放射性衰变为剑桥和爱德思考纲中的实验工作提供了极好的机会。

**剑桥 Paper 3 (AS) / Paper 5 (A2)：**
- **Paper 3：** 学生可以使用盖革-米勒 (GM) 管和计数器测量放射源的活度。他们必须通过测量本底计数率并从测量值中减去来校正本底辐射。
- **Paper 5：** 学生设计实验以确定半衰期，包括：
  - 使用 GM 管按规则时间间隔测量计数率。
  - 绘制计数率（经本底校正）对时间的图。
  - 使用对数线性图（$\ln A$ 对 $t$）确定 $\lambda$ 和 $t_{1/2}$。
  - 估计计数率的不确定度（泊松统计：不确定度 $\approx \sqrt{\text{计数}}$）。
  - 评估源距离、屏蔽和死时间的影响。

**爱德思 Unit 3 (AS) / Unit 6 (A2)：**
- **Unit 3：** 关于放射性衰变的核心实验——测量短寿命同位素（例如，镤-234 或使用模拟）的半衰期。
- **Unit 6：** 更高级的实验工作，包括：
  - 研究伽马辐射的平方反比定律。
  - 使用 GM 管和数据记录确定半衰期。
  - 放射性衰变数据的统计分析（泊松分布）。
  - 误差分析和不确定度传播。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Main Topic
    RD[Radioactive Decay] -->|is a type of| NP[Nuclear Physics]
    RD -->|requires understanding of| ASN[Atomic Structure and the Nucleus]
    
    %% Sub-topics
    RD --> TORD[Types of Radioactive Decay]
    RD --> DEC[Decay Equations and Conservation]
    RD --> NA[Neutrinos and Antineutrinos]
    RD --> EDL[Exponential Decay Law]
    
    %% Types of Decay
    TORD --> AD[Alpha Decay]
    TORD --> BMD[Beta-minus Decay]
    TORD --> BPD[Beta-plus Decay]
    TORD --> GD[Gamma Decay]
    
    AD -->|emits| He[Helium Nucleus]
    BMD -->|emits| E[Electron]
    BMD -->|emits| AN[Antineutrino]
    BPD -->|emits| P[Positron]
    BPD -->|emits| N[Neutrino]
    GD -->|emits| PH[Photon]
    
    %% Decay Equations
    DEC -->|conserves| CN[Charge Number]
    DEC -->|conserves| MN[Mass Number]
    DEC -->|conserves| E_C[Energy]
    DEC -->|conserves| M_C[Momentum]
    
    %% Neutrinos
    NA -->|involved in| BMD
    NA -->|involved in| BPD
    NA -->|explains| E_C[Energy Conservation]
    NA -->|explains| M_C[Momentum Conservation]
    
    %% Exponential Decay Law
    EDL -->|defines| A[Activity]
    EDL -->|defines| DC[Decay Constant]
    EDL -->|leads to| HL[Half-Life]
    EDL -->|gives| EQ[N = N₀e^(-λt)]
    
    HL -->|related by| HL_EQ[t₁/₂ = ln2/λ]
    A -->|related by| A_EQ[A = λN]
    
    %% Related Topics
    RD -->|leads to| HLA[Half-Life and Activity]
    RD -->|involves| ABG[Alpha, Beta and Gamma Radiation]
    
    %% Practical Connections
    RD -->|measured by| GM[Geiger-Müller Tube]
    RD -->|used in| CD[Carbon Dating]
    RD -->|used in| NM[Nuclear Medicine]
    RD -->|used in| NP_G[Nuclear Power Generation]
    
    %% Prerequisites
    ASN -->|includes| P[Protons]
    ASN -->|includes| N[Neutrons]
    ASN -->|includes| E_Cloud[Electron Cloud]
    
    %% Styling
    classDef main fill:#f9f,stroke:#333,stroke-width:4px;
    classDef subtopic fill:#bbf,stroke:#333,stroke-width:2px;
    classDef concept fill:#dfd,stroke:#333,stroke-width:2px;
    classDef equation fill:#ffd,stroke:#333,stroke-width:2px;
    classDef practical fill:#fdd,stroke:#333,stroke-width:2px;
    
    class RD main;
    class TORD,DEC,NA,EDL subtopic;
    class AD,BMD,BPD,GD,HL,A,DC concept;
    class EQ,HL_EQ,A_EQ equation;
    class GM,CD,NM,NP_G practical;
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definitions / 定义** | • **Radioactive decay:** Spontaneous, random process where unstable nucleus emits radiation<br>• **Activity ($A$):** Number of decays per second (Bq)<br>• **Decay constant ($\lambda$):** Probability per second of decay (s$^{-1}$)<br>• **Half-life ($t_{1/2}$):** Time for half the nuclei to decay |
| **Equations / 公式** | • $A = \lambda N$ — Activity equation<br>• $N = N_0 e^{-\lambda t}$ — Exponential decay law<br>• $A = A_0 e^{-\lambda t}$ — Activity decay<br>• $t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$ — Half-life relation<br>• $\frac{N}{N_0} = \left(\frac{1}{2}\right)^n$ — Fraction after $n$ half-lives |
| **Graphs / 图表** | • $N$ vs $t$: Decreasing exponential, starts at $N_0$, approaches zero asymptotically<br>• $\ln N$ vs $t$: Straight line, gradient $= -\lambda$, intercept $= \ln N_0$<br>• $A$ vs $t$: Same shape as $N$ vs $t$<br>• Area under $A$ vs $t$ = total decays |
| **Key Facts / 关键事实** | • Decay is **spontaneous** — unaffected by temperature, pressure, chemistry<br>• Decay is **random** — cannot predict which nucleus decays next<br>• $\lambda$ is constant for a given isotope<br>• Half-life ranges from $10^{-4}$ s to $10^9$ years<br>• Exponential decay never reaches zero |
| **Exam Reminders / 考试提醒** | • Always correct for background radiation in experiments<br>• Convert time units consistently (hours → seconds for $\lambda$ in s$^{-1}$)<br>• Use $\ln$ (natural log), not $\log_{10}$, in equations<br>• For non-integer half-lives, use $N = N_0 e^{-\lambda t}$, not $N = N_0/2^n$<br>• Check if $n$ is exact before using the fraction method<br>• Remember: $\ln 2 \approx 0.693$ |
| **Common Mistakes / 常见错误** | ❌ Thinking activity is constant<br>❌ Confusing $\lambda$ with decay rate<br>❌ Believing half-life changes with conditions<br>❌ Using $\log_{10}$ instead of $\ln$<br>❌ Forgetting to subtract background radiation |
| **Practical Tips / 实验提示** | • Use GM tube with counter for activity measurements<br>• Measure background for at least 5 minutes<br>• Correct each reading: corrected = measured − background<br>• Uncertainty in count: $\sqrt{N}$ (Poisson statistics)<br>• Plot $\ln(\text{corrected count})$ vs $t$ for straight line<br>• Gradient $= -\lambda$, so $\lambda = -\text{gradient}$<br>• Safety: use tongs, minimize time, maximize distance |