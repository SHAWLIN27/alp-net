# 1. Overview / 概述

**English:**
Accuracy and precision are two fundamental concepts in experimental physics that describe the quality of measurements. While often confused in everyday language, they have distinct meanings in physics. **Accuracy** refers to how close a measured value is to the true or accepted value, while **precision** refers to how close repeated measurements are to each other. Understanding this distinction is crucial for evaluating experimental data, identifying sources of error, and communicating the reliability of results. This sub-topic forms the conceptual foundation for [[Systematic vs Random Errors]] and [[Uncertainty from Repeated Measurements]].

**中文:**
准确度和精密度是实验物理学中描述测量质量的两个基本概念。虽然在日常用语中经常混淆，但它们在物理学中有着截然不同的含义。**准确度**指测量值与真实值或公认值的接近程度，而**精密度**指多次重复测量值之间的接近程度。理解这一区别对于评估实验数据、识别误差来源以及传达结果的可靠性至关重要。本子知识点构成了[[Systematic vs Random Errors]]和[[Uncertainty from Repeated Measurements]]的概念基础。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 1.4(a) Distinguish between precision and accuracy | 1.7 Distinguish between precision and accuracy |
| 1.4(b) Assess the precision of a measurement from the range of values | 1.8 Explain how precision relates to the range of readings |
| 1.4(c) Assess the accuracy of a measurement from the percentage error | 1.9 Explain how accuracy relates to percentage error |
| 1.4(d) Identify systematic and random errors | 1.10 Identify systematic and random errors |
| 1.4(e) Suggest ways to reduce errors | 1.11 Suggest improvements to reduce errors |
| 1.4(f) Calculate percentage error | 1.12 Calculate percentage error and percentage uncertainty |

**Examiner Expectations / 考官期望:**
- **English:** Students must be able to clearly distinguish between accuracy and precision using experimental examples. They should understand that high precision does not guarantee high accuracy (e.g., a precise but inaccurate measurement due to systematic error). Students must also be able to assess precision from the spread of repeated readings and accuracy from the percentage difference from the true value.
- **中文:** 学生必须能够通过实验例子清晰区分准确度和精密度。他们应理解高精密度并不保证高准确度（例如，由于系统误差导致的精密度高但不准确的测量）。学生还必须能够根据重复读数的离散程度评估精密度，并根据与真实值的百分比差异评估准确度。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Accuracy** / 准确度 | The degree to which a measured value agrees with the true or accepted value. | 测量值与真实值或公认值的一致程度。 | ❌ Confusing accuracy with precision. A measurement can be precise but inaccurate. |
| **Precision** / 精密度 | The degree to which repeated measurements under unchanged conditions show the same results (i.e., the spread of readings). | 在不变条件下重复测量结果的一致程度（即读数的离散程度）。 | ❌ Thinking precision means "small uncertainty" — it actually means "small spread". |
| **True Value** / 真实值 | The value that would be obtained in an ideal measurement with no errors. | 在无误差的理想测量中会获得的值。 | ❌ Assuming the true value is always known — it is often unknown and approximated. |
| **Systematic Error** / 系统误差 | An error that causes readings to be consistently above or below the true value, affecting accuracy. | 导致读数始终高于或低于真实值的误差，影响准确度。 | ❌ Confusing with random errors — systematic errors are consistent, not random. |
| **Random Error** / 随机误差 | An error that causes readings to scatter around the true value, affecting precision. | 导致读数在真实值周围散开的误差，影响精密度。 | ❌ Thinking random errors can be eliminated — they can only be reduced by averaging. |
| **Percentage Error** / 百分比误差 | The absolute difference between measured and true value expressed as a percentage of the true value. | 测量值与真实值的绝对差，表示为真实值的百分比。 | ❌ Forgetting to divide by the true value before multiplying by 100%. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Accuracy-Precision Distinction / 准确度与精密度的区别

### Explanation / 解释
**English:**
Accuracy and precision are independent qualities of a measurement. A measurement can be:
- **Accurate and precise** (ideal — close to true value with small spread)
- **Accurate but imprecise** (close to true value but large spread)
- **Precise but inaccurate** (small spread but far from true value — often due to systematic error)
- **Neither accurate nor precise** (far from true value with large spread)

The classic analogy is a target (dartboard): accuracy is how close the darts are to the bullseye (true value), while precision is how close the darts are to each other.

**中文:**
准确度和精密度是测量的两个独立品质。测量结果可以是：
- **准确且精密**（理想情况——接近真实值且离散度小）
- **准确但不精密**（接近真实值但离散度大）
- **精密但不准确**（离散度小但远离真实值——通常由系统误差引起）
- **既不准确也不精密**（远离真实值且离散度大）

经典的类比是靶心：准确度是飞镖离靶心（真实值）的远近，而精密度是飞镖之间的接近程度。

### Physical Meaning / 物理意义
**English:**
- **Accuracy** reflects the absence of systematic error. If a measurement is accurate, systematic errors are small.
- **Precision** reflects the absence of random error. If a measurement is precise, random errors are small.
- High precision with low accuracy indicates a systematic error that shifts all readings consistently.
- Low precision with high accuracy indicates random errors that average out over many readings.

**中文:**
- **准确度**反映系统误差的大小。如果测量准确，则系统误差小。
- **精密度**反映随机误差的大小。如果测量精密，则随机误差小。
- 高精密度但低准确度表明存在系统误差，使所有读数一致偏移。
- 低精密度但高准确度表明存在随机误差，通过多次读数取平均可以消除。

### Common Misconceptions / 常见误区
- ❌ "Precision means the measurement is correct." → No, precision only describes consistency, not correctness.
- ❌ "A precise measurement is always accurate." → No, systematic errors can make precise measurements inaccurate.
- ❌ "Accuracy and precision are the same thing." → They are independent concepts.
- ❌ "More decimal places means more precision." → Precision is about spread, not the number of digits.

### Exam Tips / 考试提示
- **English:** When asked to comment on accuracy, always compare to the true/accepted value. When asked about precision, look at the range of repeated readings. Use the target diagram analogy in explanations.
- **中文:** 当被要求评论准确度时，始终与真实值/公认值进行比较。当被问及精密度时，观察重复读数的范围。在解释中使用靶心图类比。

> 📷 **IMAGE PROMPT — ACC-PREC-01: Target Diagram for Accuracy vs Precision**
> A 2×2 grid of dartboards showing four scenarios: (1) Accurate & Precise: all darts clustered at bullseye, (2) Accurate but Imprecise: darts scattered around bullseye, (3) Precise but Inaccurate: darts tightly clustered away from bullseye, (4) Neither: darts scattered away from bullseye. Each quadrant labeled clearly. Clean, educational style with arrows and annotations.

---

## 4.2 Assessing Precision from Repeated Readings / 从重复读数评估精密度

### Explanation / 解释
**English:**
Precision is assessed by examining the **spread** or **range** of repeated measurements. The smaller the spread, the higher the precision. Common measures include:
- **Range** = maximum value − minimum value
- **Half-range** = (max − min) / 2 (often used as an estimate of uncertainty)
- **Standard deviation** (more rigorous, but not required at AS level)

A precise measurement has a small range; an imprecise measurement has a large range.

**中文:**
精密度通过检查重复测量的**离散程度**或**范围**来评估。离散程度越小，精密度越高。常用指标包括：
- **极差** = 最大值 − 最小值
- **半极差** = (最大值 − 最小值) / 2（常作为不确定度的估计）
- **标准偏差**（更严格，但AS阶段不要求）

精密测量具有小极差；不精密测量具有大极差。

### Physical Meaning / 物理意义
**English:**
The spread of readings is caused by random errors — unpredictable fluctuations in the measurement process. High precision means random errors are small, so readings cluster tightly together.

**中文:**
读数的离散程度由随机误差引起——测量过程中不可预测的波动。高精密度意味着随机误差小，因此读数紧密聚集在一起。

### Exam Tips / 考试提示
- **English:** When given a set of repeated readings, always calculate the range. A small range indicates high precision. Be prepared to comment on whether the precision is adequate for the experiment.
- **中文:** 当给出一组重复读数时，始终计算极差。小极差表示高精密度。准备好评论精密度是否足以满足实验要求。

---

## 4.3 Assessing Accuracy from Percentage Error / 从百分比误差评估准确度

### Explanation / 解释
**English:**
Accuracy is assessed by comparing the measured value to the true or accepted value. The **percentage error** quantifies this:

$$ \text{Percentage Error} = \frac{|\text{Measured Value} - \text{True Value}|}{\text{True Value}} \times 100\% $$

A small percentage error indicates high accuracy; a large percentage error indicates low accuracy.

**中文:**
准确度通过将测量值与真实值或公认值进行比较来评估。**百分比误差**量化了这一比较：

$$ \text{百分比误差} = \frac{|\text{测量值} - \text{真实值}|}{\text{真实值}} \times 100\% $$

小百分比误差表示高准确度；大百分比误差表示低准确度。

### Physical Meaning / 物理意义
**English:**
The percentage error tells us how far the measurement deviates from the truth. If the percentage error is large, the measurement is inaccurate — likely due to systematic errors.

**中文:**
百分比误差告诉我们测量值偏离真实值的程度。如果百分比误差大，则测量不准确——很可能是由系统误差引起的。

### Exam Tips / 考试提示
- **English:** Always use the absolute value in the numerator. If the true value is not given, you cannot calculate percentage error — you can only comment on precision. Be careful with units: ensure numerator and denominator have the same units.
- **中文:** 分子中始终使用绝对值。如果未给出真实值，则无法计算百分比误差——只能评论精密度。注意单位：确保分子和分母具有相同的单位。

---

# 5. Essential Equations / 核心公式

## 5.1 Percentage Error / 百分比误差

$$ \text{Percentage Error} = \frac{|\text{Measured Value} - \text{True Value}|}{\text{True Value}} \times 100\% $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| Measured Value | The value obtained from the experiment | 实验获得的值 | Same as quantity |
| True Value | The accepted or theoretical value | 公认值或理论值 | Same as quantity |
| Percentage Error | The relative error expressed as a percentage | 以百分比表示的相对误差 | % (dimensionless) |

**Derivation / 推导:**
The percentage error is derived from the concept of fractional error: $\text{Fractional Error} = \frac{|\text{Measured} - \text{True}|}{\text{True}}$. Multiplying by 100% converts it to a percentage.

**Conditions / 适用条件:**
- **English:** The true value must be known (from a standard, theory, or accepted value). If the true value is zero, percentage error is undefined — use absolute error instead.
- **中文:** 必须已知真实值（来自标准、理论或公认值）。如果真实值为零，则百分比误差未定义——改用绝对误差。

**Limitations / 局限性:**
- **English:** Percentage error does not distinguish between systematic and random errors. A small percentage error could result from cancellation of errors. It also becomes misleading when the true value is very small.
- **中文:** 百分比误差不区分系统误差和随机误差。小百分比误差可能是误差相互抵消的结果。当真实值非常小时，它也会产生误导。

---

## 5.2 Range (for Precision Assessment) / 极差（用于精密度评估）

$$ \text{Range} = x_{\text{max}} - x_{\text{min}} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $x_{\text{max}}$ | Maximum reading | 最大读数 | Same as quantity |
| $x_{\text{min}}$ | Minimum reading | 最小读数 | Same as quantity |
| Range | Spread of readings | 读数的离散程度 | Same as quantity |

**Conditions / 适用条件:**
- **English:** Only meaningful when there are at least 2-3 repeated readings. A single reading gives no information about precision.
- **中文:** 只有在至少有2-3次重复读数时才有意义。单次读数无法提供关于精密度的信息。

**Limitations / 局限性:**
- **English:** The range is sensitive to outliers (extreme values). It is a rough measure — standard deviation is more robust but not required at AS level.
- **中文:** 极差对异常值（极端值）敏感。这是一个粗略的度量——标准偏差更稳健，但AS阶段不要求。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Measurement Distribution Graph / 测量分布图

### Axes / 坐标轴
- **X-axis:** Measured value / 测量值
- **Y-axis:** Frequency of occurrence / 出现频率

### Shape / 形状
- **High precision:** Narrow, tall peak (readings cluster tightly)
- **Low precision:** Wide, flat peak (readings spread out)
- **High accuracy:** Peak centered on true value
- **Low accuracy:** Peak shifted away from true value

### Gradient Meaning / 斜率含义
Not applicable — this is a frequency distribution, not a continuous function.

### Area Meaning / 面积含义
The total area under the curve represents the total number of measurements.

### Exam Interpretation / 考试解读
- **English:** A narrow distribution indicates high precision. A distribution centered on the true value indicates high accuracy. A narrow distribution shifted away from the true value indicates high precision but low accuracy (systematic error).
- **中文:** 窄分布表示高精密度。以真实值为中心的分布表示高准确度。偏离真实值的窄分布表示高精密度但低准确度（系统误差）。

> 📷 **IMAGE PROMPT — ACC-PREC-02: Measurement Distribution Curves**
> Four frequency distribution curves on the same axes: (1) Tall narrow curve centered on true value (accurate & precise), (2) Short wide curve centered on true value (accurate but imprecise), (3) Tall narrow curve shifted right of true value (precise but inaccurate), (4) Short wide curve shifted left of true value (neither). True value marked with vertical dashed line. Clean educational style with labels.

---

# 7. Required Diagrams / 必备图表

## 7.1 Target Diagram (Dartboard Analogy) / 靶心图（飞镖类比）

### Description / 描述
**English:** A 2×2 grid of dartboards showing the four combinations of accuracy and precision. Each board has a bullseye (true value) and several darts (measurements). This is the most common diagram used to explain the distinction.

**中文:** 一个2×2的靶心网格，展示准确度和精密度的四种组合。每个靶心有一个靶心点（真实值）和几支飞镖（测量值）。这是解释两者区别最常用的图表。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — ACC-PREC-03: Detailed Target Diagram**
> A 2×2 grid of dartboards. Top-left: "Accurate & Precise" — all darts clustered at bullseye. Top-right: "Accurate but Imprecise" — darts scattered around bullseye. Bottom-left: "Precise but Inaccurate" — darts tightly clustered in top-left quadrant away from bullseye. Bottom-right: "Neither Accurate nor Precise" — darts scattered in bottom-right quadrant. Each quadrant labeled with title. Bullseye marked "True Value". Clean, educational style with arrows.

### Labels Required / 需要标注
- **English:** "True Value" at bullseye; "Accurate & Precise", "Accurate but Imprecise", "Precise but Inaccurate", "Neither" in each quadrant
- **中文:** 靶心处标注"真实值"；每个象限标注"准确且精密"、"准确但不精密"、"精密但不准确"、"既不准确也不精密"

### Exam Importance / 考试重要性
- **English:** Extremely high — this diagram is frequently used in exam questions to test understanding of the distinction. Students are often asked to identify which quadrant a given experimental scenario belongs to.
- **中文:** 极高——该图表常用于考试题中测试对两者区别的理解。学生常被要求识别给定实验场景属于哪个象限。

---

## 7.2 Measurement Distribution Diagram / 测量分布图

### Description / 描述
**English:** A graph showing frequency distributions for two different measurement sets, illustrating precision (width of distribution) and accuracy (position relative to true value).

**中文:** 显示两组不同测量频率分布的图表，说明精密度（分布宽度）和准确度（相对于真实值的位置）。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — ACC-PREC-04: Distribution Comparison**
> Two frequency distribution curves overlaid. Curve A: tall, narrow, centered on true value (high precision, high accuracy). Curve B: tall, narrow, shifted to the right (high precision, low accuracy). True value marked with vertical dashed line. X-axis labeled "Measured Value", Y-axis labeled "Frequency". Clean educational style.

### Labels Required / 需要标注
- **English:** "True Value" (vertical dashed line); "High Precision, High Accuracy" (Curve A); "High Precision, Low Accuracy" (Curve B)
- **中文:** "真实值"（垂直虚线）；"高精密度，高准确度"（曲线A）；"高精密度，低准确度"（曲线B）

### Exam Importance / 考试重要性
- **English:** High — helps visualize how systematic errors shift the entire distribution without affecting precision.
- **中文:** 高——有助于可视化系统误差如何在不影响精密度的情况下移动整个分布。

---

# 8. Worked Examples / 典型例题

## Example 1: Identifying Accuracy and Precision / 示例1：识别准确度和精密度

### Question / 题目
**English:**
A student measures the acceleration due to gravity ($g$) five times using a pendulum. The accepted value is $9.81 \text{ m s}^{-2}$. The student's readings are: $9.72, 9.74, 9.73, 9.71, 9.73 \text{ m s}^{-2}$.

(a) Calculate the mean value of $g$.
(b) Calculate the range of the readings.
(c) Calculate the percentage error.
(d) Comment on the precision and accuracy of the measurements.

**中文:**
一名学生使用单摆测量重力加速度（$g$）五次。公认值为 $9.81 \text{ m s}^{-2}$。学生的读数为：$9.72, 9.74, 9.73, 9.71, 9.73 \text{ m s}^{-2}$。

(a) 计算 $g$ 的平均值。
(b) 计算读数的极差。
(c) 计算百分比误差。
(d) 评论测量的精密度和准确度。

### Solution / 解答

**(a) Mean value / 平均值:**

$$ \bar{g} = \frac{9.72 + 9.74 + 9.73 + 9.71 + 9.73}{5} = \frac{48.63}{5} = 9.726 \text{ m s}^{-2} $$

**(b) Range / 极差:**

$$ \text{Range} = 9.74 - 9.71 = 0.03 \text{ m s}^{-2} $$

**(c) Percentage error / 百分比误差:**

$$ \text{Percentage Error} = \frac{|9.726 - 9.81|}{9.81} \times 100\% = \frac{0.084}{9.81} \times 100\% = 0.856\% $$

**(d) Comment / 评论:**

**English:**
- **Precision:** The range is only $0.03 \text{ m s}^{-2}$, which is very small compared to the mean value. This indicates **high precision** — the readings are tightly clustered.
- **Accuracy:** The percentage error is $0.856\%$, which is small (less than 1%). The mean value ($9.726 \text{ m s}^{-2}$) is close to the true value ($9.81 \text{ m s}^{-2}$). This indicates **high accuracy**.
- **Overall:** The measurements are both precise and accurate.

**中文:**
- **精密度：** 极差仅为 $0.03 \text{ m s}^{-2}$，与平均值相比非常小。这表明**高精密度**——读数紧密聚集。
- **准确度：** 百分比误差为 $0.856\%$，很小（小于1%）。平均值（$9.726 \text{ m s}^{-2}$）接近真实值（$9.81 \text{ m s}^{-2}$）。这表明**高准确度**。
- **总体：** 测量既精密又准确。

### Final Answer / 最终答案
**Answer:** (a) $9.726 \text{ m s}^{-2}$, (b) $0.03 \text{ m s}^{-2}$, (c) $0.856\%$, (d) High precision and high accuracy | **答案：** (a) $9.726 \text{ m s}^{-2}$, (b) $0.03 \text{ m s}^{-2}$, (c) $0.856\%$, (d) 高精密度和高准确度

### Quick Tip / 提示
**English:** When commenting on precision, always mention the range. When commenting on accuracy, always mention the percentage error or the difference from the true value. Never say "precise" without evidence from the data.
**中文:** 评论精密度时，始终提及极差。评论准确度时，始终提及百分比误差或与真实值的差异。没有数据证据时，不要只说"精密"。

---

## Example 2: Precise but Inaccurate / 示例2：精密但不准确

### Question / 题目
**English:**
Another student measures $g$ using the same method and obtains: $9.45, 9.46, 9.44, 9.45, 9.46 \text{ m s}^{-2}$. The accepted value is $9.81 \text{ m s}^{-2}$.

(a) Calculate the mean, range, and percentage error.
(b) Comment on precision and accuracy.
(c) Suggest a possible cause for the discrepancy.

**中文:**
另一名学生使用相同方法测量 $g$，得到：$9.45, 9.46, 9.44, 9.45, 9.46 \text{ m s}^{-2}$。公认值为 $9.81 \text{ m s}^{-2}$。

(a) 计算平均值、极差和百分比误差。
(b) 评论精密度和准确度。
(c) 建议可能造成差异的原因。

### Solution / 解答

**(a) Calculations / 计算:**

$$ \bar{g} = \frac{9.45 + 9.46 + 9.44 + 9.45 + 9.46}{5} = \frac{47.26}{5} = 9.452 \text{ m s}^{-2} $$

$$ \text{Range} = 9.46 - 9.44 = 0.02 \text{ m s}^{-2} $$

$$ \text{Percentage Error} = \frac{|9.452 - 9.81|}{9.81} \times 100\% = \frac{0.358}{9.81} \times 100\% = 3.65\% $$

**(b) Comment / 评论:**

**English:**
- **Precision:** The range is only $0.02 \text{ m s}^{-2}$, even smaller than the first example. This indicates **very high precision**.
- **Accuracy:** The percentage error is $3.65\%$, which is significantly larger. The mean value ($9.452 \text{ m s}^{-2}$) is far from the true value ($9.81 \text{ m s}^{-2}$). This indicates **low accuracy**.
- **Overall:** The measurements are **precise but inaccurate** — a classic case of systematic error.

**中文:**
- **精密度：** 极差仅为 $0.02 \text{ m s}^{-2}$，甚至比第一个例子还小。这表明**非常高的精密度**。
- **准确度：** 百分比误差为 $3.65\%$，明显更大。平均值（$9.452 \text{ m s}^{-2}$）远离真实值（$9.81 \text{ m s}^{-2}$）。这表明**低准确度**。
- **总体：** 测量**精密但不准确**——系统误差的典型案例。

**(c) Possible cause / 可能原因:**

**English:** A systematic error such as measuring the pendulum length incorrectly (e.g., including the radius of the bob incorrectly) or timing errors due to reaction time. The consistent offset suggests a fixed error in the experimental setup.

**中文:** 系统误差，例如错误测量摆长（例如，错误包含摆锤半径）或由于反应时间导致的计时误差。一致的偏移表明实验装置中存在固定误差。

### Final Answer / 最终答案
**Answer:** (a) $9.452 \text{ m s}^{-2}$, $0.02 \text{ m s}^{-2}$, $3.65\%$; (b) High precision, low accuracy; (c) Systematic error in measurement setup | **答案：** (a) $9.452 \text{ m s}^{-2}$, $0.02 \text{ m s}^{-2}$, $3.65\%$; (b) 高精密度，低准确度; (c) 测量装置中的系统误差

### Quick Tip / 提示
**English:** A small range with a large percentage error is the hallmark of a systematic error. Always look for this pattern in exam questions.
**中文:** 小极差伴随大百分比误差是系统误差的标志。在考试题中始终寻找这种模式。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Distinguish between accuracy and precision using experimental data | Very High | Easy | 📝 *待填入* |
| Calculate percentage error and comment on accuracy | Very High | Medium | 📝 *待填入* |
| Calculate range and comment on precision | High | Easy | 📝 *待填入* |
| Identify whether a measurement is precise but inaccurate | High | Medium | 📝 *待填入* |
| Suggest causes of systematic error leading to inaccuracy | Medium | Medium | 📝 *待填入* |
| Interpret target diagram or distribution graph | Medium | Easy | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Distinguish between", "Calculate", "Comment on", "Suggest", "Explain", "State"
- **中文:** "区分"、"计算"、"评论"、"建议"、"解释"、"陈述"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Accuracy and precision are fundamental to all practical work in physics. Key connections include:

1. **Repeated Measurements:** Taking multiple readings improves precision by allowing averaging to reduce random errors. The spread of readings directly indicates precision.

2. **Graph Plotting:** When plotting graphs, precision affects the scatter of data points around the best-fit line. Accuracy affects whether the line passes through the expected theoretical point.

3. **Uncertainty Estimation:** The range of repeated readings is used to estimate the uncertainty in a measurement (see [[Uncertainty from Repeated Measurements]]).

4. **Error Analysis:** Identifying whether errors are systematic or random helps determine whether accuracy or precision is compromised (see [[Systematic vs Random Errors]]).

5. **Instrument Selection:** Choosing instruments with appropriate resolution affects precision. Calibration affects accuracy.

6. **Experimental Design:** To improve accuracy, identify and eliminate systematic errors (e.g., zero error, parallax error). To improve precision, take more readings and use more sensitive instruments.

**中文:**
准确度和精密度是所有物理实验工作的基础。关键联系包括：

1. **重复测量：** 多次读数通过取平均减少随机误差来提高精密度。读数的离散程度直接指示精密度。

2. **图表绘制：** 绘制图表时，精密度影响数据点围绕最佳拟合线的离散程度。准确度影响直线是否通过预期的理论点。

3. **不确定度估计：** 重复读数的极差用于估计测量的不确定度（参见[[Uncertainty from Repeated Measurements]]）。

4. **误差分析：** 识别误差是系统性的还是随机性的有助于确定准确度还是精密度受损（参见[[Systematic vs Random Errors]]）。

5. **仪器选择：** 选择具有适当分辨率的仪器影响精密度。校准影响准确度。

6. **实验设计：** 为提高准确度，识别并消除系统误差（例如，零误差、视差误差）。为提高精密度，进行更多次读数并使用更灵敏的仪器。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    A[Accuracy vs Precision] --> B[Accuracy]
    A --> C[Precision]
    
    B --> D[Definition: Closeness to True Value]
    B --> E[Assessed by: Percentage Error]
    B --> F[Affected by: Systematic Errors]
    
    C --> G[Definition: Closeness of Repeated Readings]
    C --> H[Assessed by: Range / Spread]
    C --> I[Affected by: Random Errors]
    
    D --> J[True Value must be known]
    E --> K[Formula: |Measured - True| / True × 100%]
    
    H --> L[Range = Max - Min]
    H --> M[Small Range = High Precision]
    
    F --> N[Systematic Errors shift all readings]
    I --> O[Random Errors cause scatter]
    
    N --> P[Example: Zero error, Calibration error]
    O --> Q[Example: Parallax, Temperature fluctuations]
    
    A --> R[Four Combinations]
    R --> S[Accurate & Precise]
    R --> T[Accurate but Imprecise]
    R --> U[Precise but Inaccurate]
    R --> V[Neither]
    
    S --> W[Ideal measurement]
    U --> X[Systematic error present]
    
    A --> Y[Related Topics]
    Y --> Z[[Systematic vs Random Errors]]
    Y --> AA[[Absolute, Fractional and Percentage Uncertainty]]
    Y --> AB[[Uncertainty from Repeated Measurements]]
    Y --> AC[[Graph Plotting Skills]]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | **Accuracy:** Closeness to true value (准确度：接近真实值) |
| | **Precision:** Closeness of repeated readings (精密度：重复读数接近程度) |
| **Key Formula / 核心公式** | $\text{Percentage Error} = \frac{|\text{Measured} - \text{True}|}{\text{True}} \times 100\%$ |
| | $\text{Range} = x_{\text{max}} - x_{\text{min}}$ |
| **Key Graph / 核心图表** | Target diagram (dartboard) — 4 quadrants showing combinations |
| | Frequency distribution — narrow = precise, centered = accurate |
| **Exam Tip / 考试提示** | Small range + large % error = systematic error (precise but inaccurate) |
| | Large range + small % error = random error (accurate but imprecise) |
| | Always calculate range for precision, % error for accuracy |
| **Common Mistake / 常见错误** | ❌ Confusing accuracy with precision |
| | ❌ Thinking precise = accurate |
| | ❌ Forgetting absolute value in % error formula |
| **Improvement / 改进方法** | Improve precision: take more readings, use sensitive instruments |
| | Improve accuracy: calibrate instruments, eliminate systematic errors |
| **Memory Aid / 记忆技巧** | **A**ccuracy = **A**ccepted value (A for A) |
| | **P**recision = **P**roximity of readings to each other (P for P) |
| | Target analogy: bullseye = accuracy, cluster = precision |